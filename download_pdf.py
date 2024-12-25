import requests
from bs4 import BeautifulSoup
url = "https://www.mlit.go.jp/kankocho/seisaku_seido/dmo/ichiran/toroku_dmo.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

pdf_links = []
for link in soup.find_all("a", href=True):
	if link["href"].endswith(".pdf"):
		pdf_links.append(link["href"])

for pdf_link in pdf_links:
	pdf_url = pdf_link if pdf_link.startswith("http") else f"https://www.mlit.go.jp{pdf_link}"
	response = requests.get(pdf_url)
	if response.status_code == 200:
		file_name = pdf_url.split("/")[-1]
		with open(file_name, "wb") as file:
			file.write(response.content)
		print(f"Downloaded {file_name}")
	else:
		print(f"Failed to download {pdf_url}")