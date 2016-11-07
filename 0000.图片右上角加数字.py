#coding : utf-8

from PIL import Image,ImageFont, ImageDraw

fontspath = 'fonts/'
imagespath= 'images/'
im = Image.open(imagespath + 'QQ.png')
draw = ImageDraw.Draw(im)
fontsize = int(min(im.size)/4)
font = ImageFont.truetype(fontspath + 'arial.ttf', fontsize)
draw.text((im.size[0]-fontsize, 0), '5', font = font, fill = (256,0,0))
im.save(imagespath + 'QQ_num.png',"png")



