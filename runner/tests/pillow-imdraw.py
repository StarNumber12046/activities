from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
print(os.path)
path = os.getcwd()
parent = os.path.dirname(path).replace("\\", "/")
img = Image.open("img.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text",(255,255,255),font=font)
img.save('sample-out.jpg')