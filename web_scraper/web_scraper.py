import requests
import pprint
from bs4 import BeautifulSoup


def request(URL):
    """
    getting the url and return the needed data 
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all(class_='noprint Inline-Template Template-Fact')
    return results



def get_citations_needed_count(URL):
    '''
    Checking the count of the citation in the web & returning the count of citation as an int
    '''
    # URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    all_citation = request(URL)
    return len(all_citation)

   

# pprint.pprint(response.content)
# print(len(results))



def get_citations_needed_report(URL):
    """
    Returning a string that contains the data 
    """
    report = request(URL)
    for i in report:
        citation_text = i.find_parent('p')
        print(citation_text.text)



if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(f'The number of the citation is : {get_citations_needed_count(URL)} ')
    print("") 
    print(get_citations_needed_report(URL))
    print("__________________________________________") 
    print("") 





    


