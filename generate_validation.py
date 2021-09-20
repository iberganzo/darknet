import os

image_files = []
os.chdir(os.path.join("data", "objval"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        image_files.append("data/objval/" + filename)
os.chdir("..")
with open("val.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
