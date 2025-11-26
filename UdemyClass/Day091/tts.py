from gtts import gTTS
import pdfplumber
import tkinter
from tkinter import filedialog

# pip install pdfplumber
# pip install gTTS


# mytext = "Hello Dave, welcome to Python!"

# tts = gTTS(text=mytext, lang='en', slow=False)

# tts.save("output.mp3")

pdf_filename = ""

def fileconvert(): 
    global pdf_filename
    print("Call file convert")
    
    mytext = ""
    
    print("Converting PDF to Text...")
    with pdfplumber.open(pdf_filename) as pdf:        
        for page in pdf.pages:
            print(page.extract_text())
            mytext += page.extract_text()
     
    print("Converting text to speech...")       
    tts = gTTS(text=mytext, lang='en', slow=False)

    print("Saving file...")
    tts.save("pdfaudio.mp3")
    print("MP3 file saved!")
    

def fileselectaction():  
    global pdf_filename
   
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])

    if file_path:
        print(f"Selected file: {file_path}") 
        pdf_filename = file_path    

    else:
        print("No file selected.")
        
#Creating a new window and configurations
window = tkinter.Tk()
window.title("PDF to Speedh Converter")
window.minsize(width=500, height=500)

# calls action() when buttons pressed
button = tkinter.Button(text="Select PDF", command=fileselectaction)
button.place(x=100,y=50)

button = tkinter.Button(text="TTS Convert", command=fileconvert)
button.place(x=100,y=100)

window.mainloop()


