from web_scraper.web_scraper import *


def test_count():
    expected = 5
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    assert actual == expected 

# def test_report():
#     actual = get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')
#     expected = '''

# '''   

#     assert actual == expected 