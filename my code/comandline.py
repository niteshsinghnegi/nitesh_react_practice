import argparse
import requests

def DownloadFile(url, local_filename):
    r = requests.get(url, stream=True)   # stream=True for large files
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=512 * 1024): 
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    return

parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("output", help="Name to save the downloaded file as")
args = parser.parse_args()

print("Downloading from:", args.url)
print("Saving as:", args.output)

DownloadFile(args.url, args.output)









