from bs4 import BeautifulSoup

# 1ST STEP - SCRAPING

# ----------------------------------------------

    #with open('index.html', 'r') as html_file: # Open the HTML on read mode and put in a variable 
    #    content = html_file.read() # Read the html content
    #    # print(content)
    #
    #    soup = BeautifulSoup(content, 'lxml') # Used to print in a lxml - to process XML and HTML files with Python
    #
    #    tags = soup.find('h5')
    #    print(tags) # It only shows the first occurrence
    #
    #    # print(soup.prettify()) # prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string
    #
    #    # If you want to get every single occurrence on the Scrap, u will need to use the funcion soup.find_all
    #    coursesHtmlTag = soup.find_all('h5')
    #    print(coursesHtmlTag) 
    #    
    #    # We can get the text into every h5 we take and print it in a better way
    #    for course in coursesHtmlTag:
    #        print(course.text)

# ----------------------------------------------

# 2ND STEP - SCRAPING
