import string

import pytest
import requests

url_ddg = "https://duckduckgo.com"
def test_ddg_response():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    related_Topics = rsp_data['RelatedTopics']
    presidents = [
        'Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Van Buren', 'Harrison', 'Tyler', 'Polk',
        'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur',
        'Cleveland', 'Harrison', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover',
        'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush',
        'Clinton', 'Bush', 'Obama', 'Trump', 'Biden']
    for text in list(presidents):
        if text.strip("',") in related_Topics:
            presidents.remove(text)
            assert len(presidents) == 0















