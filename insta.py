import matplotlib.pyplot as plt
from PIL import Image

coffee = Image.open("coffee.jpg")
print(coffee)

print('coffee (RGB)')
plt.imshow(coffee)
plt.show()
r, g, b = coffee.split()

texture = Image.open('texture.jpg')
print(texture)

print('texture (RGB)')
plt.imshow(texture)
plt.show()

rT, gT, bT = texture.split()

new_image = Image.merge("RGB", (bT,g,b))
plt.imshow(new_image)
# plt.xticks([]), plt.yticks([])
plt.show()


new_image = Image.merge("RGB", (rT,g,b))
plt.imshow(new_image)
# plt.xticks([]), plt.yticks([])
plt.show()


new_image = Image.merge("RGB", (bT,rT,b))
plt.imshow(new_image)
# plt.xticks([]), plt.yticks([])
plt.show()


new_image = Image.merge("RGB", (g,gT,bT))
plt.imshow(new_image)
# plt.xticks([]), plt.yticks([])
plt.show()