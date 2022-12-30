import os
from PIL import Image


def filter1(item):
    return item.endswith(validFormats)


def isempty(items):
    return True if len(items) == 0 else False


validFormats = (".jpg", ".jpeg", ".png", ".JPG", ".PNG")
files = os.listdir()
sorted_files = sorted(files)
pictures = list(filter(filter1, sorted_files))
picturestock = []

print("----------------------------- CONVERT PNG TO JPG --------------------------------")
if isempty(pictures):
    print(" [Error] there are no pictrues in the directory ! ")
else:
    print("pictures are : {0}".format(pictures))

for picture in pictures:
    picturestock.append(Image.open(picture).convert("RGB"))

picturestock[0].save(pictures[0] + ".pdf", save_all=False, append_images=pictures[1:])
picturestock[1].save(pictures[1] + ".pdf", save_all=False, append_images=pictures[1:])

for i in pictures:
    print(f"picture {i} saved as {i}.pdf")

print("---------------------------- END CONVERT PNG TO JPG -----------------------------")
