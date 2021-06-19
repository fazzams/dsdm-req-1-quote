import requests as requests

r = requests.get('http://quotes.toscrape.com/')
html = r.text
with open('quotes.txt', 'w') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
            line = line.strip()
            f.write(line)
            f.write("\n")