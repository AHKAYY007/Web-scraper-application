import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def web_scrape(website):
    print('launching browser...')

    chrome_driver_path = './chromedriver.exe'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path, options=options))

    driver.get(website)
    print('page loaded....')
    html = driver.page_source

    driver.quit()

    return html
   
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ''

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
    
    #this section removes any uneccessary '\n' characters and white spaces

    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):

    #this code will split our dom content into batches of 6000 chracters while feeding it to an LLM for faster processes
    
    return [
        dom_content [i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
