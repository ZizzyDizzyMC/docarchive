import re, requests, argparse, os.path

# Constants
searchStr = 'data.docsbay.net%2fpdf%2f([a-zA-Z0-9].*).pdf'

# Arguments
parser = argparse.ArgumentParser(description='Download a pdf from Docsbay.')
parser.add_argument('--url', metavar='-U', default='https://docsbay.net/be-inspired-at-karralyka', help="Url to download.")
parser.add_argument('--dir', metavar='-D', default=os.path.realpath('.'), help="Directory to save to.")
args = parser.parse_args()


print("Test of path arg " + args.dir) 
print("Test of url arg " + args.url)


class Download(object):
    def __init__(self,url,path,pdfUUID=''):
        self.url = url
        self.path = path
        self.pdfUUID = pdfUUID
        super(Download, self).__init__()
    def download(self):
        pageSrc = requests.get(self.url)
        pdfUUID = re.search(searchStr, pageSrc.text, re.I).group(1)
        pdfUrl = 'https://data.docsbay.net/pdf/' + pdfUUID + '.pdf?sign=1'
        return Download(pdfUrl, pdfUUID).save()
    def save(self):
        print(self.url)
        pdfBinary = requests.get(self.url).content
        with open(self.path + self.pdfUUID + '.pdf', 'wb') as f:
            f.write(pdfBinary)
        
        

def yeet():
    return Download(args.url, args.dir).download()
    
yeet()