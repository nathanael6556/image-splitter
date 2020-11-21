Author: "Nathanael"
Date: "July 21'st, 2020"
Title: "Image Splitter"
Description: "Split image into equal sized smaller images."

# Import

from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilenames,askdirectory
from os.path import exists,split,join

def img_split(imfn,dirs):

    # Checks if chosen file(s) and folder exist
    
    if not exists(imfn):
        print("ALERT: File doesn't exist!")
        return

    if not exists(dirs):
        print("ALERT: Folder doesn't exist!")
        return

    # Open the image

    try:
        im = Image.open(imfn)
        print("Opening file \"{}\"".format(imfn))
    except:
        print("Unable to open the file. Please choose an appropiate file !")
        return

    # Ask for grid size

    w = int(input("Horizontal: "))
    h = int(input("Vertical: "))

    # Extract information
    
    image_name = split(imfn)[-1].split(".")[0]
    image_ext = '.png'
    loaded_image = im.convert('RGBA')
    x,y = im.size

    # Alert for rounded width and height (if any)
    
    if x%w != 0:
        print("ALERT: Float width encountered")
        if input("Proceed to continue (y/n)? >>>").lower() == n:
            return
        
    if y%h != 0:
        print("ALERT: Float height encountered")
        if input("Proceed to continue (y/n)? >>>").lower() == n:
            return

    # Calculate the result image resolution
    # (temporarily in float for better precision)
    
    new_x = float(x)/float(w)
    new_y = float(y)/float(h)

    # Iterate for every section
        
    for b in range(h):
        for a in range(w):
            
            index = b*w+a
            temp_img = loaded_image.crop((round(a*new_x),
                                 round(b*new_y),
                                 round((a+1)*new_x),
                                 round((b+1)*new_y)))

            # Save the result image

            try:
            
                savename = join(dirs,image_name+"({})".format(index)+image_ext)
                temp_img.save(savename,"PNG")
                
                if index < 1:
                    print(str(index+1)+" image saved.")
                else:
                    print(str(index+1)+" images saved.")

            except:
                print("ALERT: Unable to save image")


def main():
    
    # Ask for file(s)

    filenames = askopenfilenames(filetypes=(("JPG Files",'.jpg'),("PNG Files",'.png'),("All Files","*.*")),parent=display,title="Choose image(s)")
    if filenames == "":
        print("No files were chosen")
        return

    # Ask for saving directory

    savedir = askdirectory(title="Choose saving directory")
    if savedir == "":
        print("No directory was chosen")
        return

    # Iterate for every file

    for filename in filenames:
        
        img_split(filename,savedir)
        print('Done !')


# Init Tk

display = Tk()
display.withdraw()

# Running main function

if __name__ == "__main__":

    # Define variable restart just in case restart is prefered than quit.
    
    restart = True
    while restart:
        main()
        if input("Restart (y/n)? >>> ").lower() == "y":
            restart = True
        else:
            restart = False
        

# Let the user know if the program will ends
    
input("\n\nPress ENTER to quit")
