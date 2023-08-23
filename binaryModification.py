from PIL import Image
from scipy import ndimage
import numpy as np
from readImage import ReadImage

class BinarModification(ReadImage):
    def __init__(self, fileName):
        super().__init__(fileName)

    def binaryzation(self):
        copyImage = self.image.copy()
        greyImage = copyImage.convert('L')
        threshold = 130
        pixels = greyImage.load()
        for i in range(greyImage.size[0]):
            for j in range(greyImage.size[1]):
                if pixels[i, j] > threshold:
                    pixels[i, j] = 255
                else:
                    pixels[i, j] = 0
        greyImage = greyImage.convert('1')

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        greyImage.save(f'{newImageName}.jpg')
        greyImage.show()
        greyImage.close()

    def erosion(self):
        erosionImage = self.image.copy()
        erosionArray = np.array(erosionImage.convert('1'))
        erosionFiltr = np.ones((2, 1))
        erosion = ndimage.binary_erosion(erosionArray, structure=erosionFiltr).astype(erosionArray.dtype)
        newImage = Image.fromarray(erosion)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        newImage.save(f'{newImageName}.jpg')
        newImage.show()
        newImage.close()

    def open(self):
        openImage = self.image.copy()
        openArray = np.array(openImage.convert('1'))
        openFiltr = np.ones((1, 1))
        open = ndimage.binary_opening(openArray, structure=openFiltr).astype(openArray.dtype)
        newImage = Image.fromarray(open)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        newImage.save(f'{newImageName}.jpg')
        newImage.show()
        newImage.close()

    def closed(self):
        closedImage = self.image.copy()
        closedArray = np.array(closedImage.convert('1'))
        closedFiltr = np.ones((2, 5))
        closed = ndimage.binary_closing(closedArray, structure=closedFiltr).astype(closedArray.dtype)
        newImage = Image.fromarray(closed)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        newImage.save(f'{newImageName}.jpg')
        newImage.show()
        newImage.close()