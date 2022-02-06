# Import the python text to speech libarary and the PDF REader library
import pyttsx3 
import PyPDF2
# Read the PDF file binary mode

#Books
# algo = r'D:\ebooks\Programming\Algorithms sedgewick.pdf'
trading = r'D:\ebooks\Stock Market\_Price Action\trend-qualification-and-trading.pdf'

pdf_file = open(trading, 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
#Find the number of pages in the PDF document
number_of_pages = read_pdf.getNumPages()
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init()
for i in range(21, number_of_pages ):
    # Read the PDF page 
    page = read_pdf.getPage(i)
    
    # Extract the text of the PDF page    
    page_content = page.extractText()
    
    # set the audio speed and volume
    newrate=250
    engine.setProperty('rate', newrate)
    newvolume=200
    engine.setProperty('volume', newvolume)
        
    # say method on the engine that passing input text to be spoken 
    engine.say(page_content) 
    
    # run and wait method to processes the voice commands.  
    engine.runAndWait()
