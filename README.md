# COLORRED
colorred is a python module that can name every HEX or RGB color as accurately as possible.

![pasted image 0](https://user-images.githubusercontent.com/47318592/210171733-1eef07e3-c908-47ec-97cf-4cfb45a8a54b.png)

#INSTALLATION

installing colorred_py with pip
```
pip install colorred_py
```

# USING COLORRED:

there are couple of ways to use colorred. first one is to convert hex or rgb to a color group
- **WHITE**
- **BLACK**
- **RED**
- **BROWN**
- **GREEN**
- **YELLOW**
- **ORANGE**
- **PURPLE**
- **PINK**
- **CYAN**
- **GRAY**

you can call `color_group_by_rgb` or `color_group_by_hex`
```
from colorred_py.colorize import color_group_by_hex

color_name1 = color_group_by_hex('#fff232')
color_name2 = color_group_by_rgb((255, 242, 50))

print(color_name1)
print(color_name2)
```
as both colors are the exact same colors the output will be
```
white
white
```
`closest_color_by_rgb` or `closest_color_by_hex` returns more specific color names
you can see all of the available named colors in todays css [HTML Color Names](https://www.w3schools.com/colors/colors_names.asp) 

```
from colorred_py.colorize import closest_color_by_hex

color_name1 = closest_color_by_hex('#ff00ff')

print(color_name1)
```
output:
```
magenta
```

