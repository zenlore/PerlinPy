# PerlinPy

Python implementation of the perlin noise algorithm.

# Getting Started

All that's needed is a python interpreter. Here's some code that will generate noise at a specific point.

```
import Perlin
noise = Perlin(50) #pass desired grid size
noise.genNoise(10, 15) #returns a value in the range of 0.0 to 1.0
```

If you'd like to layer multiple octaves of noise in the same range

```
#noise.octave(x, y, numOfOctaves, persistence)
noise.octave(10, 15, 5, 0.25)
```

The number of octaves controls how many seperate octaves are calculated. Each octave has half the frequency of
the previous octave.

Persistence controls how much effect each successive octave has on the output. 
