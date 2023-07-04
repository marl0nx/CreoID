import requests
import wmi
import hashlib


VERSION = "v1.0"


def get_cpu_hwid():
    c = wmi.WMI()
    processors = c.Win32_Processor()
    cpu_hwid = ""
    for processor in processors:
        cpu_hwid += processor.ProcessorId.strip()
    return cpu_hwid


def get_total_cpu_cores():
    c = wmi.WMI()
    processors = c.Win32_Processor()
    total_cpu_cores = 0
    for processor in processors:
        total_cpu_cores += processor.NumberOfCores
    return total_cpu_cores


def get_motherboard_hwid():
    c = wmi.WMI()
    motherboards = c.Win32_BaseBoard()
    return motherboards[0].SerialNumber.strip()


def get_graphics_card_model():
    c = wmi.WMI()
    graphics_cards = c.Win32_VideoController()
    if graphics_cards:
        graphics_card = graphics_cards[0]  # Erste Grafikkarte (Hauptgrafikeinheit)
        return graphics_card.Name.strip()
    return None


def get_bios_hwid():
    c = wmi.WMI()
    bios = c.Win32_BIOS()[0]
    return bios.SerialNumber


def get_windows_uuid():
    c = wmi.WMI()
    os = c.Win32_OperatingSystem()[0]
    return os.SerialNumber


def get_total_ram():
    c = wmi.WMI()
    ram_modules = c.Win32_PhysicalMemory()
    total_ram = 0
    for module in ram_modules:
        total_ram += int(module.Capacity)
    return total_ram


def check_for_all_existing_users():
    c = wmi.WMI()
    users = c.Win32_UserAccount()
    user_names = []
    for user in users:
        user_names.append(user.Name)
    return user_names


def get_mac_addresses():
    c = wmi.WMI()
    mac_addresses = []
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        mac_addresses.append(interface.MACAddress)
    return mac_addresses


def get_ram_speed():
    c = wmi.WMI()
    ram_modules = c.Win32_PhysicalMemory()
    ram_speed = 0
    for module in ram_modules:
        ram_speed = module.Speed
    return ram_speed


def get_cpu_vendor():
    c = wmi.WMI()
    processors = c.Win32_Processor()
    processor_vendor = ""
    for processor in processors:
        processor_vendor += processor.Manufacturer.strip()
    return processor_vendor


def get_disks_model():
    c = wmi.WMI()
    disks = c.Win32_DiskDrive()
    disks_names = ""

    for ssd in disks:
        interface_types = ssd.InterfaceType.split()

        # Filter SSD, HDD, and NVMe SSD devices
        if any(interface_type.lower() in ['scsi', 'ide', 'sata', 'nvme'] for interface_type in interface_types):
            disks_names += ssd.Model.strip()

    return disks_names


def get_disks_hwid():
    c = wmi.WMI()
    disks = c.Win32_DiskDrive()

    disks_hwids = []

    for disk in disks:
        interface_types = disk.InterfaceType.split()

        # Filter SSD, HDD, and NVMe SSD devices
        if any(interface_type.lower() in ['scsi', 'ide', 'sata', 'nvme'] for interface_type in interface_types):
            ssd_hardware_id = disk.SerialNumber.strip()
            disks_hwids.append(ssd_hardware_id)

    return disks_hwids


def get_graphics_card_vram():
    c = wmi.WMI()
    graphics_cards = c.Win32_VideoController()
    max_vram = 0
    for graphics_card in graphics_cards:
        vram = graphics_card.AdapterRAM
        if vram > max_vram:
            max_vram = vram
    return max_vram


def get_graphics_card_uuid():
    c = wmi.WMI()
    graphics_cards = c.Win32_VideoController()
    if graphics_cards:
        graphics_card = graphics_cards[0]  # Erste Grafikkarte (Hauptgrafikeinheit)
        return graphics_card.PNPDeviceID
    return None


def generate_unique_hwid():
    hwid = ""
    hwid += str(get_disks_model())
    hwid += str(get_disks_hwid())
    hwid += str(get_cpu_vendor())
    hwid += str(get_cpu_hwid())
    hwid += str(get_total_cpu_cores())
    hwid += str(get_total_ram())
    hwid += str(get_ram_speed())
    hwid += str(get_graphics_card_model())
    hwid += str(get_graphics_card_vram())
    hwid += str(get_graphics_card_uuid())
    hwid += str(get_bios_hwid())
    hwid += str(get_motherboard_hwid())
    hwid += str(get_windows_uuid())
    hwid = hashlib.sha256(hwid.encode()).hexdigest()

    # Convert to a better looking format (e.g. 2a2b2c2d -> 2A2B2C2D) and every 8 characters add a dash
    hwid = hwid.upper()
    hwid = '-'.join(hwid[i:i + 8] for i in range(0, len(hwid), 8))
    return hwid


def print_all_security_factors():
    print("Disk Model: " + str(get_disks_model()))
    print("Disk HWID: " + str(get_disks_hwid()))
    print("CPU HWID: " + str(get_cpu_hwid()))
    print("CPU Vendor: " + str(get_cpu_vendor()))
    print("Total CPU Cores: " + str(get_total_cpu_cores()))
    print("Graphics Card Model: " + str(get_graphics_card_model()))
    print("Graphics Card VRAM: " + str(get_graphics_card_vram()))
    print("Graphics Card UUID: " + str(get_graphics_card_uuid()))
    print("Total RAM: " + str(get_total_ram()))
    print("RAM Speed: " + str(get_ram_speed()))
    print("BIOS HWID: " + str(get_bios_hwid()))
    print("Motherboard HWID: " + str(get_motherboard_hwid()))
    print("Windows UUID: " + str(get_windows_uuid()))


def check_for_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/marl0nx/creoid/main/VERSION")
        if r.status_code == 200:
            version = r.text.replace("\n", "")
            if version != VERSION:
                print("New version available: " + version + " | " + "Current version installed: " + VERSION)
                print("Download: https://github.com/marl0nx/creoid")
            else:
                print("You are using the latest version.")
    except Exception as e:
        pass
