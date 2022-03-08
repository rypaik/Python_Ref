# pdf_to_audiobook.py

```python
import pyttsx3
import PyPDF2
pdf_book = open('book.pdf','rb')
pdf_book_reader = PyPDF2.PdfFileReader(pdf_book)
pages_no = pdf_book_reader.numPages
print(pages_no)
speaker = pyttsx3.init()
for number in range(8,pages_no):
  page_start = pdf_book_reader.getPage(8)
  text = page_start.extractText()
  speaker.say(text)
  speaker.runAndWait()
```

