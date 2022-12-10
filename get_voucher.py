import requests

from bs4 import BeautifulSoup

def get_voucher():
    rs = requests.get("https://magiamgia.com/now/")
    soup = BeautifulSoup(rs.text, 'html.parser')

    info_vouchers = soup.find_all("div", attrs={'class':'polyxgo_title'})
    codes = soup.find_all("div", attrs={'class':'copy-code'})

    list_code = []
    for code in codes:
        list_code.append(code.get("data-clipboard-text"))

    dict_vouchers = {}
    index = 0
    for info in info_vouchers:
        tag_spans = info.find_all("span")
        dict_info = {}
        
        if len(tag_spans) == 6:
            key_max = " ".join(tag_spans[0].text.split())
            vaLue_max = " ".join(tag_spans[1].text.split())
            key_min = " ".join(tag_spans[2].text.split())
            vaLue_min = " ".join(tag_spans[3].text.split())
            dict_info[key_max] = vaLue_max
            dict_info[key_min] = vaLue_min
            
        elif len(tag_spans) != 6:
            key_max = " ".join(tag_spans[0].text.split())
            vaLue_max = " ".join(tag_spans[1].text.split())
            dict_info[key_max] = vaLue_max
            
        dict_vouchers[list_code[index]] = dict_info
        index += 1

    return dict_vouchers

