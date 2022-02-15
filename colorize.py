import webcolors
from color_groups import color_groups_dict

def hex_to_rgb(hex_):
	hex_ = hex_.lstrip('#')
	return tuple(int(hex_[i:i+2], 16) for i in (0, 2, 4))

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def closest_color_by_rgb(rgb_):
    try:
        closest_name = webcolors.rgb_to_name(rgb_)
    except ValueError:
        closest_name = closest_colour(rgb_)
    return closest_name

def closest_color_by_hex(hex_):
    rgb_ = hex_to_rgb(hex_)
    try:
        closest_name = webcolors.rgb_to_name(rgb_)
    except ValueError:
        closest_name = closest_colour(rgb_)
    return closest_name

def color_group_by_hex(hex_):
	color_name = closest_color_by_hex(hex_)

	for color in color_groups_dict.keys():
		if color_name == color:
			return color_name
		else:
			for color_ in color_groups_dict[color]:
				if color_name == color_:
					return color

def color_group_by_rgb(rgb_):
    color_name = closest_color_by_rbg(rgb_)

    for color in color_groups_dict.keys():
        if color_name == color:
            return color_name
        else:
            for color_ in color_groups_dict[color]:
                if color_name == color_:
                    return color