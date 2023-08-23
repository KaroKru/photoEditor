from readImage import ReadImage
from changeImageColour import ChangeImageColour
from binaryModification import BinarModification
from blurImage import BlurImage
from compresImage import CompresImage

def description():
    print("Simple photo editor")

def menu():
    print("1. Color Space Transformation")
    print("2. Negative")
    print("3. Binarization")
    print("4. Erosion")
    print("5. Open")
    print("6. Close")
    print("7. User Filter")
    print("8. Histogram Equalization")
    print("9. Compression")
    print("10. Smoothing by Averaging")

def imageChoose():
    print("Selected photo name, which will be modified:\n", "autumn.jpg\n", "person.jpg\n", "animal.jpg\n")

def options(answear, colourImage, blurImage, binarImage, compresImage):
    choose = 0

    if answear == 1:
        print("Selected color space transformation")
        print("Possible color changes:\n", "1 black and white\n", "2 blue\n", "3 red\n", "4 green\n", "5 sepia\n", "6 define your own\n")

        try:
            choose = int(input("Selected an image color: "))
            if choose >= 1 and choose <=6:
                print("Selected a value within the range of 1 to 6")
            else:
                choose = 0
                print("Selected value over range")
        except ValueError:
            print("Selected value over range")

        if choose == 1:
            colourImage.grayscale()
        elif choose == 2:
            colourImage.bluscale()
        elif choose == 3:
            colourImage.redscale()
        elif choose == 4:
            colourImage.greenscale()
        elif choose == 5:
            colourImage.sepia()
        elif choose == 6:
            colourImage.userScale()
    elif answear == 2:
        print("Selected negativ")
        colourImage.negative()
    elif answear == 3:
        print("Selected binaryzation")
        binarImage.binaryzation()
    elif answear == 4:
        print("Selected erosion")
        binarImage.erosion()
    elif answear == 5:
        print("Selected open")
        binarImage.open()
    elif answear == 6:
        print("Selected close")
        binarImage.closed()
    elif answear == 7:
        print("Selected user filter")
        blurImage.filtr()
    elif answear == 8:
        print("Selected histogram equalization")
        blurImage.histogram()
    elif answear == 9:
        print("Selected compression")
        compresImage.compres()
    elif answear == 10:
        print("Selected smoothing by averaging")
        blurImage.averageHistogram()

def main():
    description()

    imageChoose()

    while True:
        try:
            imageName = input("Enter the image name with the file extension: ")

            if imageName not in ["autumn.jpg", "person.jpg", "animal.jpg"]:
                print("Selected an incorrect file, please enter the file name again.")
            else:
                break
        except ValueError:
            print("File name not provided.")
        except TypeError:
            print("Entered a number.")


    print("Information about the selected image:")
    image = ReadImage(imageName)
    image.openImage()
    image.originalImageSize()
    image.originalBytesImage()
    image.originalImageColour()

    colourImage = ChangeImageColour(imageName)
    blurImage = BlurImage(imageName)
    binarImage = BinarModification(imageName)
    compresImage = CompresImage(imageName)

    menu()

    try:
        repeat = "yes"
        answer = 0
        while repeat == "yes":
            try:
                answer = int(input("What do you want to do? Enter a value: "))
                if answer >= 1 and answer <= 10:
                    print("Selected a value within the range of 1 to 10.")
                else:
                    print("Selected a value outside the range.")
                    continue
            except ValueError:
                print("Selected a value outside the range.")
                continue
            except TypeError:
                print("Invalid type.")
                continue
            except AssertionError as err:
                print(err)

            options(answer, colourImage, blurImage, binarImage, compresImage)

            repeat = input("Do you want to repeat: ")

    except KeyboardInterrupt:
        print("User interrupted the program.")

main()