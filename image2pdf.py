from PIL import Image
import os


class Image2pdf:
    def __init__(self):
        self.validFormats = (".jpg", ".jpeg", ".png", ".JPG", ".PNG")
        self.pictures = []
        self.files = os.listdir()
        self.convertpictures()
        input("Done ..... (Press Any Key To Exit)")

    def filter(self, item):
        return item.endswith(self.validFormats)

    def sortfiles(self):
        return sorted(self.files)

    def getpictures(self):
        pictures = list(filter(self.filter, self.sortfiles()))
        if self.isempty(pictures):
            print(" [Error] there are no pictrues in the directory ! ")
            # raise Exception(" [Error] there are no pictrues in the directory !")
        print("pictures are : \n {}".format(pictures))
        return pictures

    @staticmethod
    def isempty(items):
        return True if len(items) == 0 else False

    def convertpictures(self):
        for picture in self.getpictures():
            self.pictures.append(Image.open(picture).convert("RGB"))
        self.save()

    def save(self):
        self.pictures[0].save(
            "result.pdf", save_all=True, append_images=self.pictures[1:]
        )


if __name__ == "__main__":
    Image2pdf()
