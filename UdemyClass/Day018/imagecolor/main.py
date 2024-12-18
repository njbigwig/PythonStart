###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('myimage.jpg', 50)
for color in colors:
    print(color.rgb.r, color.rgb.g, color.rgb.b)
    mytuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(mytuple)

print(rgb_colors)