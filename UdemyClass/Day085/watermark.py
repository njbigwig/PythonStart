from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter
from tkinter import filedialog

def fileselectaction():
    print(f"Do something {entry.get()}")
    
    # Create a hidden root window
    rootwindow = tkinter.Tk()
    rootwindow.withdraw()
    
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")])

    if file_path:
        print(f"Selected file: {file_path}")
        
        # load image
        myimage = Image.open(file_path).convert("RGBA")
        print(myimage.format, myimage.size, myimage.mode)
        
        # Create a transparent overlay
        watermark = Image.new("RGBA", myimage.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)    
        
        # Load a font (adjust path and size as needed)
        try:
            font = ImageFont.truetype("arial.ttf", 100)
        except IOError:
            font = ImageFont.load_default()
        
        # Define watermark text and position
        wmtext = entry.get()
        bbox = draw.textbbox((0, 0), wmtext, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = myimage.width - text_width - 10
        y = myimage.height - text_height - 100 
        
        
        # Draw the text with transparency
        draw.text((x, y), wmtext, font=font, fill=(255, 255, 255, 255))  # Fully opaque white

        # Combine original image with watermark
        watermarked = Image.alpha_composite(myimage, watermark)        
                
        # Save or show the result
        #watermarked.convert("RGB").save("watermarked_image.jpg", "JPEG")
        watermarked.save("watermarked_image.png", "PNG")    
        
        # Convert to ImageTk format
        tk_image = ImageTk.PhotoImage(watermarked)
        
        display_image = watermarked.copy()
        display_image.thumbnail((250, 250))  # Resize to fit window
        tk_image = ImageTk.PhotoImage(display_image)


        # Update the label with the new image
        image_label.configure(image=tk_image)
        image_label.image = tk_image  # Keep a reference!
    

        #myimage.show()
        #watermarked.show()
    else:
        print("No file selected.")

# myimage = Image.open("halfabun.jpg")

# print(myimage.format, myimage.size, myimage.mode)

# # myimage.show()

#Creating a new window and configurations
window = tkinter.Tk()
window.title("Image Watermarker")
window.minsize(width=500, height=500)

# Labels
label = tkinter.Label(text="Watermark Text")
label.place(x=10,y=10)

# Entry Field
entry = tkinter.Entry(width=30)
#Add some text to begin with
entry.insert(tkinter.END, string="")
entry.place(x=100,y=10)
#Gets text in entry
#print(entry.get())
#entry.pack()

# calls action() when pressed
button = tkinter.Button(text="Select image", command=fileselectaction)
button.place(x=100,y=50)
#button.pack()

# holder to show watermarked image
image_label = tkinter.Label(window)
image_label.place(x=50, y=120)  # Adjust position as needed


window.mainloop()