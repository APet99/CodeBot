from lxml import etree
import requests


def connect_to_black_board():
    consent_cookie = {
        "domain": "calbaptist.blackboard.com",
        "name": "COOKIE_CONSENT_ACCEPTED",
        "path": "/",
        "secure": "false",
        "value": "true"
    }
    session = requests.Session()
    session.cookies.set(**consent_cookie)
    r = session.get("https://calbaptist.blackboard.com/")
    html_tree = etree.HTML(r.text)
    elements = html_tree.xpath('/html/body/div[1]/div/div/div[7]/section/ul[1]/li[2]/div/form/input[3]')
    security_val = elements[0].get('value')
    url = "https://calbaptist.blackboard.com/webapps/login/"
    payload = 'action=login&blackboard.platform.security.NonceUtil.nonce={0}&login=Login&new_loc=&password=Manafest1%21&user_id=644941'.format(
        security_val)
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Sec-Fetch-Dest': 'document',
        'Origin': 'https://calbaptist.blackboard.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    session.request("POST", url, headers=headers, data=payload)
    return session
