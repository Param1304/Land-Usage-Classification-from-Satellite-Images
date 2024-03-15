from PIL import Image 
import json 
import io 
img_path = "/kaggle/input/tile-1-5-png/tile_1.5.png" 
# image = Image.open(img_path)
# image = Image.open(image)
image = Image.open(img_path)
# image = image.to(device)
# image.show()
# image

print(type(image)) 
print(image.size)
image.show()

# Transform image
input = test_transform(image)
input = input.to(device)
# Predict on sample
output = model(input.unsqueeze(0))

# Get corresponding class label
_, pred = torch.max(output, 1)
pred = class_names[pred[0]]

# Visualize results
fig, ax = plt.subplots(figsize=(4,4))
ax.imshow(image)
ax.set_title("Predicted class: {}".format(pred));

