from bs4 import BeautifulSoup


with open('index.html', 'r') as html_file: # Open the HTML on read mode and put in a variable 
    content = html_file.read() # Read the html content
    # print(content)

    soup = BeautifulSoup(content, 'lxml') # Used to print in a lxml - to process XML and HTML files with Python

    tags = soup.find('h1')
    print(tags)

    # print(soup.prettify()) # prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string

