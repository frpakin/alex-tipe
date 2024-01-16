# %matplotlib notebook
# %% 2D Perlin and Fractal Noise
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from perlin_numpy.perlin_numpy import (
    generate_perlin_noise_2d, generate_fractal_noise_2d,
    generate_fractal_noise_3d, generate_perlin_noise_3d
)
from ipywidgets import interact

np.random.seed(0)
noise = generate_perlin_noise_2d((256, 256), (8, 8))
plt.imshow(noise, cmap='magma', interpolation='lanczos')
plt.colorbar()
# %% 2D Perlin and Fractal Noise
np.random.seed(0)
noise = generate_fractal_noise_2d((256, 256), (8, 8), 5)
plt.figure()
plt.imshow(noise, cmap='magma', interpolation='lanczos')
plt.colorbar()
plt.show()

# %% 2D Perlin and Fractal Noise
np.random.seed(0)
noise = generate_fractal_noise_2d((256, 256), (8, 8), 5)
plt.figure()
plt.imshow(noise, cmap='magma', interpolation='hermite')
plt.colorbar()
plt.show()

# %% 3D Fractal Noise
np.random.seed(0)
noise = generate_fractal_noise_3d(
    (32, 256, 256), (1, 4, 4), 4, tileable=(True, False, False)
)

fig = plt.figure()
images = [
    [plt.imshow(
        layer, cmap='magma', interpolation='lanczos', animated=True
    )]
    for layer in noise
]
animation_3d = animation.ArtistAnimation(fig, images, interval=50, blit=True)
plt.show()

# %% 3D Perlin Noise
np.random.seed(0)
noise = generate_perlin_noise_3d(
    (32, 256, 256), (1, 4, 4), tileable=(True, False, False)
)

fig = plt.figure()
images = [
    [plt.imshow(
        layer, cmap='magma', interpolation='lanczos', animated=True
    )]
    for layer in noise
]
animation_3d = animation.ArtistAnimation(fig, images, interval=50, blit=True)
plt.show()
