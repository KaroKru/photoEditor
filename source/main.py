import os
from ImageInformation import ImageHandler
from ChangeImageColour import ColourTransformation
from BinaryModification import MorphoTransformation
from BlurImage import EnhTechniques
from CompresImage import CompressImage

def samplePhotoInformation():
    print("Please add your own photo or select one of sample photos\n")
    directory = os.path.join('..', 'photo')

    try:
        files = os.listdir(directory)
        print(f"Files in {directory}:")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def chooseOption(fileToChange):
    options = [
        "Color space transformation",
        "Morphological transformations",
        "Image enhancement techniques",
        "Image compression"
    ]

    print(f"Select one option from many possibles:")
    for idx, option in enumerate(options, start = 1):
        print(f"{idx} -> {option}")

    answer = int(input("What do you want to do? Enter an id value: "))
                
    match answer:
        case 1:
            print(f"Selected colour space transformation")
            
            colour = ColourTransformation(fileToChange)
            colour.colourOptions()
        case 2:
            print(f"Selected morphological transformations")
            
            binary = MorphoTransformation(fileToChange)
            binary.transformationOptions()
        
        case 3: 
            print(f"Selected image enhancement techniques")
            
            blur = EnhTechniques(fileToChange)
            blur.checkOptions()
        case 4: 
            print(f"Selected image compression")
            
            compression = CompressImage(fileToChange)
            compression.compress()
        case _:
            print(f"Invalid value")


def openFile():
    samplePhotoInformation()

    repeat = "yes"

    while repeat == "yes":
        try:
            photoName = input("Enter the image name with the file extension: ")
            photoPath = os.path.join('..', 'photo', photoName)

            if photoPath is None:
                raise ValueError(f"Problem with file.")

            if photoPath.lower().endswith('.jpg'):
                readPhoto = ImageHandler(photoPath)
                readPhoto.openImage()
                chooseOption(readPhoto)
            else:
                raise ValueError(f"Choose other file type")

        except Exception as e:
            print(f"Error: {e}")
            raise

        userAnswear = input("Do you want to repat?")
        repeat = userAnswear.lower()
    
    print("Closed")

if __name__ == "__main__":
    openFile()