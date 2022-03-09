import re
import os
import time

# \s(?=[^\[\]]*]])
# regex - finds all blank spaces in [[]] 

# STATUS:
# TODO: Find more elegant way to create file than pause program for 1 sec
# TODO: module or class decorator - make a class decorator module
# TODO: input_md needs to take in for loop of file list taken from directory 
# TODO: encapsulate module and import
# TODO: try async and await instead of sleep to check IO on creation of files
# TODO: package vs module -> module because lack of complexity - change main to def

# TODO: write selenium test on github upload     


def cleanup(update_md, new_md):
    """ copies temp file to target fie"""
    copy_md = f'cp { }'
    os.popen(f"cp {new_md} {update_md}")
    time.sleep(1)
    os.remove(new_md)


if __name__ == '__main__':
    source_md ="PYTHON_TOC.md"
    with open(source_md, "r") as f:
        result = re.sub(r"\s(?=[^\[\]]*]])", '%20', f.read())
        temp_md = "tempfile.md"
        file = open(temp_md, "x")
        file.write(result)
        time.sleep(1)
        file.close()
        f.close()
        cleanup(source_md, temp_md)