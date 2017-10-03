
import Perlin
import math
from PIL import Image

noise = Perlin.Perlin(500)
img = Image.new('L', (1000, 1000), 255)
data = img.load()
for x in range(1000):
	for y in range(1000):
		#print(x, y, math.floor((noise.genNoise(x, y) + 1) * 128))
		data[x,y] = (math.floor((noise.genNoise(x, y)) * 255),)
img.save('image.png', "PNG")
print("DONE")