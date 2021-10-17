from PIL import Image, ImageDraw, ImageFont

import sys

text = sys.argv[1]

img = Image.new('RGB', (100, 30), color = 'black')

newsize = (1080, 608) 	
img = img.resize(newsize)
fnt = ImageFont.truetype('NotoSans/NotoSans-Regular.ttf', 30)
d = ImageDraw.Draw(img)
idk = 540 - len(text)/2 * 2
d.text((int(idk),304), f'{text}', font=fnt, fill=(255, 255, 255))
img.save('post.jpeg')
