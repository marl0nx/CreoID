<p align='center'>
  <b>📰 Follow me here 📰</b><br>  
  <a href="https://discord.com/users/1032874064731185152">Discord</a> |
  <a href="https://www.youtube.com/channel/UCwq6NcsqT8PS8ixhhUjM9ZQ">YouTube</a> |
  <a href="https://github.com/marl0nx">Github</a><br><br>
</p>

![Header](https://github.com/marl0nx/creoid/blob/main/images/github-header-image.png?raw=true)
<p>An unique HWID generator, made using Python.</p>

## Why choose CreoID? 
<p>CreoID uses multiple secutity factors (Disks, CPU HWID, Mainboard HWID and more) to make sure that it's hard to bypass.</p>

## Usage/Examples


### Check for updates
```python
from utils import check_for_updates

check_for_updates()
```

### Print all security factors of your system
```python
from utils import print_all_security_factors

print_all_security_factors()
```

### Generate a unique HWID based on all security factors
```python
from utils import generate_unique_hwid

hwid = generate_unique_hwid()
print(hwid)
```

### Check if a HWID matches with your system
```python
def example_check_hwid():
    hwid = generate_unique_hwid()
    r = requests.get('https://marl0nx.github.io/CreoID/example_hwid')  # Replace your own URL.
    if r.text == hwid:
        return True
    else:
        return False

print("HWID matches with your system: " + str(example_check_hwid()))
```


## Authors

- [@marl0nx](https://www.github.com/marl0nx)


## Support
This HWID generator is windows only!

For support, send me a message on Discord. I am pleased to help.

Username: **marl0nx**

