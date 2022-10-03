import cv2
import os

directory, _ = os.path.split(__file__)

image_name = "sample.png"
image_path = f"{directory}/{image_name}"

img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img, int(input("First threshold (default 100): ") or 100), int(input("Second threshold (default 200): ") or 200))

new_image = f"{directory}/new_image.png"

img = cv2.imwrite(new_image, edges)
img = cv2.imread(new_image)

rows = ["".join(["@" if all(img[y,x]) else "." for x in range(img.shape[1])]) for y in range(img.shape[0])]

if "res.txt" not in os.listdir(directory):
    with open(f"{directory}/res.txt", "x") as file:
        pass

with open(f"{directory}/res.txt", "w") as file:
    file.write("\n".join(rows))

os.remove(new_image)
