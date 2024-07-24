from PIL import ImageFilter
from ImageInformation import ImageHandler

class EnhTechniques():
    
    def __init__(self, reader):
        self.reader = reader
    
    def gaussianBlur(self):
        radius = int(input("Enter the value of the blur radius "))
        if radius < 0:
            raise ValueError(f"An invalid value has been selected")

        gaussianMask = ImageFilter.GaussianBlur(radius)
        gaussianImage = self.reader.image.copy()
        newImage = gaussianImage.filter(gaussianMask)

        self.reader.saveFile(newImage, "gaussianBlur")

    def histogram(self):
        histogramImage = self.reader.image.copy()
        hist = histogramImage.histogram()
        distribution = [sum(hist[:i+1]) for i in range(len(hist))]
        distributionMap = [int(((distribution[i] - distribution[0]) / (histogramImage.width * histogramImage.height - distribution[0])) * 255) for i in range(len(distribution))]
        newImage = Image.new(histogramImage.mode, histogramImage.size)
        pixels = histogramImage.load()
        newPixels = newImage.load()
        for i in range(histogramImage.width):
            for j in range(histogramImage.height):
                newPixels[i, j] = (distributionMap[pixels[i, j][0]], distributionMap[pixels[i, j][1]], distributionMap[pixels[i, j][2]])

        self.reader.saveFile(newImage, "histogram")

    def averageHistogram(self):
        averageImage = self.reader.image.copy()
        smoothSize = (3, 3)
        averageSmooth = [1/9] * 9
        smoothed = averageImage.filter(ImageFilter.Kernel(smoothSize, averageSmooth))

        self.reader.saveFile(smoothed, "averageHistogram")
    
    def checkOptions(self):
        techniques = [
                "histogram", 
                "gaussian blur", 
                "average histogram"
        ]

        print(f"Possible image enhancement techniques: ")
            
        for id, techniques in enumerate(techniques, start = 1):
            print(f"{id} -> {techniques}")
            
        choose = int(input("What do you want to do? Enter an id value:"))

        match choose:
            case 1:
                self.histogram()
            case 2:
                self.gaussianBlur()
            case 3:
                self.averageHistogram()
            case _:
                print(f"Selected value out of the scope")