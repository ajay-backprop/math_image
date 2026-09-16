import numpy as np
from PIL import Image

# 1. Define resolution
width, height = 500, 500

# 2. Create coordinate grids (x, y) normalized from 0 to 1
m, n = np.meshgrid(np.arange(1, width+1), np.arange(1, height+1))

print(m, n)

x = m/width
y = n/height

print(x, y)


# 3. Define math region masks
box_outer  = ((x >= 0.3) & (x <= 0.7) & (y >= 0.3) * (y <= 0.7)).astype(int)
box_inner = ((x >= 0.32) & (x <= 0.68) & (y >= 0.32) & (y <= 0.68)).astype(int)

print(box_outer, box_inner)

# 4. Compute RGB channels mathematically
R = 255 * box_outer
G = 255 * (box_outer - box_inner)
B = 255 * (1 - box_outer)

# 5. Stack channels and save image
rgb_array = np.dstack((R, G, B)).astype(np.uint8)
print(rgb_array)

img = Image.fromarray(rgb_array)
print(img)
img.save("math_box.png")



import numpy as np
from PIL import Image

width, height = 500, 500
m, n = np.meshgrid(np.arange(1, width + 1), np.arange(1, height + 1))

# Center coordinates around (0,0) from -1 to 1
x = (m - 250) / 250
y = (250 - n) / 250

# Polar Coordinates
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

# 1. Background: Smooth Radial Glow
bg_glow = np.exp(-2 * (r**2))

# 2. Wave Mask (Bottom Half Wave)
wave = y < (0.1 * np.sin(8 * x) - 0.3)

# 3. Polar 5-Point Star Mask
star_radius = 0.4 + 0.15 * np.sin(5 * theta)
star_mask = r < star_radius

# Combine into RGB Channels (0 to 255)
R = np.clip(255 * (star_mask * 0.9 + bg_glow * 0.3), 0, 255)
G = np.clip(255 * (wave * 0.6 + bg_glow * 0.2), 0, 0)
B = np.clip(255 * (bg_glow * 0.8 + wave * 0.8), 0, 0)

rgb_array = np.dstack((R, G, B)).astype(np.uint8)
img = Image.fromarray(rgb_array)
img.save("math_art.png")