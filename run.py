import re, requests, argparse, os.path

# Constants
searchStr = 'data.docsbay.net%2fpdf%2f([a-zA-Z0-9].*).pdf'
searchTitle = '<title>(.+) - DocsBay<\/title>'
# Arguments
parser = argparse.ArgumentParser(description='Download a pdf from Docsbay.')
parser.add_argument('--url', metavar='-U', type=str, help="Url to download.")
parser.add_argument('--dir', metavar='-D', default=os.path.realpath('.'), help="Directory to save to.")
parser.add_argument('--title', action='store_true', help="Output file as title name.")
args = parser.parse_args()


#print("Test of path arg " + args.dir) 
#print("Test of url arg " + args.url)


class Download(object):
    def __init__(self,url,path,pdfUUID='',title=''):
        self.url = url
        self.path = os.path.realpath(path)
        self.pdfUUID = pdfUUID
        self.title = title
        super(Download, self).__init__()
    def download(self):
        pageSrc = requests.get(self.url)
        pdfUUID = re.search(searchStr, pageSrc.text, re.I).group(1)
        url = 'https://data.docsbay.net/pdf/' + pdfUUID + '.pdf?sign=1'
        title = re.search(searchTitle, pageSrc.text, re.I).group(1)
        return Download(url, self.path, pdfUUID, title).save()
    def save(self):
        #print("PDF URL: " + self.url)
        #print("PDF UUID: " + self.pdfUUID)
        pdfBinary = requests.get(self.url).content
        #print("Self Path: " + self.path)
        if args.title:
            path = self.path + "/" + self.title + ".pdf"
        else:
            path = self.path + "/" + self.pdfUUID + ".pdf"
        with open(path, 'wb') as f:
            f.write(pdfBinary)
        
        

def yeet():
    return Download(args.url, args.dir).download()
    
yeet()