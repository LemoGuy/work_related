import requests
from bs4 import BeautifulSoup
import os
import time

def download_file(url, save_dir, current, total):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = os.path.join(save_dir, url.split("/")[-1])
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"({current}/{total}) Downloaded: {filename} [{(current/total)*100:.2f}%]")
    else:
        print(f"({current}/{total}) Failed to download: {url} [{(current/total)*100:.2f}%]")

webpage_url = "https://www.koskikurd.net/ferhengekan.htm"  

response = requests.get(webpage_url)
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the webpage.")
    exit()

base_url = "https://www.koskikurd.net/"  

save_directory = "files"
os.makedirs(save_directory, exist_ok=True)

soup = BeautifulSoup(html_content, 'html.parser')

pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]

total_files = len(pdf_links)

if total_files == 0:
    print("No PDF files found.")
else:
    print(f"Found {total_files} PDF file(s) to download.")

for index, link in enumerate(pdf_links, start=1):
    full_url = link if link.startswith("http") else base_url + link
    download_file(full_url, save_directory, index, total_files)
    time.sleep(1)  
