# Blackliner
#### Video Demo:  https://youtu.be/iZIPXCpkU6c
#### Description: A simple web-based tool to compare two texts.

This is a simple web-based tool that compare two texts. User can conduct a quick comparison of texts on the go without the need using any application, such as the compare tool with Microsoft Office.

#### Codes

Other than this readme file, this program conists of three other files. The first is a html page which the user can interact. It has two forms for text input, a "compare button", space for showing the result a "copy button".

The file app.py contains the usual flask application codes and calls the compare function after taking the texts from the html file. The compare function itself is in helpers.py. It makes use of a python libary called difflib which can compare a list of texts and return the position of the same and different text. Re.split is also used to remove excessive spaces etc. for better comparison result.

The compared text is then sent back to the html page and use jinja to display.

