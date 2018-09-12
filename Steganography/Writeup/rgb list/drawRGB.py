from PIL import Image

with open("origin.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

myPixelsArray = []
for x in content:
  array = x.split(",")
  array = tuple([int(w) for w in array])
  myPixelsArray.append(array)

myImage = Image.new("RGB", (323, 167))
myImage.putdata(myPixelsArray)
myImage.save("flag.jpg")