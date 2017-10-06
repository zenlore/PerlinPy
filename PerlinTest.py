
import Perlin
import math
from PIL import Image

noise = Perlin.Perlin(75)
img = Image.new('L', (1000, 1000), 255)
data = img.load()
outOfRangeCount = 0
for x in range(1000):
	for y in range(1000):
		value = noise.genNoise(x, y)
		if value < 0 or value > 1:
			outOfRangeCount += 1
		data[x,y] = (math.floor(value * 255),)

img.save('image.png', "PNG")
print("DONE")
print("Values out of range:", outOfRangeCount)