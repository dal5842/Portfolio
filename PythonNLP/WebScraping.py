import bs4
import requests
import os

archive_url = input("file:///Users/dannikalove/Documents/GitHub/Portfolio/docs/resume.html")
def get_linkContents():
    # create response object
    r = requests.get(archive_url)
    print(f"{r=}")
    # create beautiful-soup object
    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    linkText = []
    for item in soup.findAll('a'):
        print(f"{item.text}")
        linkText.append(item.text)
    print(linkText)
    download_toFile(linkText)
    return

def download_toFile(linkText):
    # We are just planning to output one file only here.
    file_name = "outputScrappingText.txt"
    print("Downloading file: " + file_name)
    working_dir = os.getcwd()
    file_deposit = os.path.join(working_dir, file_name)
    print(file_deposit)
    # write to the file:
    with open(file_deposit, 'w') as f:
       for item in linkText:
            f.write(item + '\n')
            # the '\n' adds a return character so each piece of text goes on its own line.
            print("Downloaded " + item)

    return

if __name__ == "__main__":

    # getting all links to files
    get_links = get_linkContents()