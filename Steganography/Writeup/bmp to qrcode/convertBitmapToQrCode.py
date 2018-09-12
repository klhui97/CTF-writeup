from PIL import Image, ImageFont, ImageDraw

flagImage = Image.new('RGB', (1000,1000), "white")
im = Image.open('solved.bmp')
im = im.convert('RGB')

for x in range(350):
	for y in range(229):
		if im.getpixel((x,y)) == (0,0,0):
			dr = ImageDraw.Draw(flagImage)
			dr.rectangle(((x,y),(x+5,y+5)), fill="black", outline = "black")




flagImage.save("flag2.png")
