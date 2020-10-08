import webbrowser as web


def automate():
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    url = "https://github.com/"
    web.Chrome(chrome_path).open(url)


automate()
