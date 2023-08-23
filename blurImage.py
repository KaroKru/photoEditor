from PIL import ImageFilter
from readImage import ReadImage

class BlurImage(ReadImage):
    def __init__(self, fileName):
        super().__init__(fileName)

    def filtr(self):
        while 1:
            try:
                radius = int(input("Enter the value of the blur radius "))
                if radius < 0:
                    print("A negative blur radius value has been selected")
                    continue
                else:
                    break
            except ValueError:
                print("The provided value does not meet the requirements")
            except TypeError:
                print("An invalid type has been selected")

        gaussianMask = ImageFilter.GaussianBlur(radius)
        gaussianImage = self.image.copy()
        newImage = gaussianImage.filter(gaussianMask)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        newImage.save(f'{newImageName}.jpg')
        newImage.show()
        newImage.close()

    def histogram(self):
        histogramImage = self.image.copy()
        hist = histogramImage.histogram()
        distribution = [sum(hist[:i+1]) for i in range(len(hist))]
        distributionMap = [int(((distribution[i] - distribution[0]) / (histogramImage.width * histogramImage.height - distribution[0])) * 255) for i in range(len(distribution))]
        newImage = Image.new(histogramImage.mode, histogramImage.size)
        pixels = histogramImage.load()
        newPixels = newImage.load()
        for i in range(histogramImage.width):
            for j in range(histogramImage.height):
                newPixels[i, j] = (distributionMap[pixels[i, j][0]], distributionMap[pixels[i, j][1]], distributionMap[pixels[i, j][2]])

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        newImage.save(f'{newImageName}.jpg')
        newImage.show()
        newImage.close()

    def averageHistogram(self):
        averageImage = self.image.copy()
        smoothSize = (3, 3)
        averageSmooth = [1/9] * 9
        smoothed = averageImage.filter(ImageFilter.Kernel(smoothSize, averageSmooth))

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        smoothed.save(f'{newImageName}.jpg')
        smoothed.show()
        smoothed.close()
