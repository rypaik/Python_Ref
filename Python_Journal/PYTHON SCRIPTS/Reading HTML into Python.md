# Reading HTML into Python

Local HTML into Python

[How to import html file into python variable?](https://stackoverflow.com/questions/51794609/how-to-import-html-file-into-python-variable)

```python
with open('test.html', 'r') as f: 
        html_string = f.read()


fname = "FILE.html"
html_file = open(fname, 'r', encoding='utf-8')
source_code = html_file.read() 
print(source_code)
```

Processing HTML read with BS4

[How to parse local HTML file in Python? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/)

BS4

[Python - Reading HTML Pages](https://www.tutorialspoint.com/python_data_science/python_reading_html_pages.htm)

RIL

[Importing data from HTML page in Python](https://svitla.com/blog/importing-data-from-html-page-in-python)

