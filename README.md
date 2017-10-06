# PerlinPy

Python implementation of the perlin noise algorithm.

# Getting Started

All that's needed is a python interpreter. Here's some code that will generate noise at a specific point.

```
import Perlin
noise = Perlin(50) #pass desired frequency
noise.genNoise(10, 15) #returns a value in the range of 0.0 to 1.0
```
