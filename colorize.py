import webcolors
from color_groups import color_groups_dict

def hex_to_rgb(hex_):
	hex_ = hex_.lstrip('#')
	return tuple(int(hex_[i:i+2], 16) for i in (0, 2, 4))

def get_color_names_list_by_industry(industry):
	companies = api_views.get_by_industry_company(industry)

	color_names_by_industry = []
	main_color_groups_by_industry = []

	for brand in companies:
		brand_hex_colors = api_views.get_company_colors(brand)

		for hex_ in brand_hex_colors:
			if len(hex_) == 7 and '#' in hex_:
				precise_color = get_colour_name(hex_to_rgb(hex_))
				color_names_by_industry.append(precise_color)
				main_color_groups_by_industry.append(get_color_group_name(precise_color))

	return main_color_groups_by_industry


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name

def group_duplicates(list_):
	return {i:list_.count(i) for i in list_}

def get_color_group(color_name):
	color_name = color_name.lower()

	for color in color_groups_dict.keys():
		if color_name == color:
			return color_name
		else:
			for color_ in color_groups_dict[color]:
				if color_name == color_:
					return color