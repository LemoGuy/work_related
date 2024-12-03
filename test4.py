import bs4
import requests
import pandas as pd # 

def parse_Ferhengi_Xall(result):
    definitions = []
    list_items = result.select('.resultDef ul li')
    for item in list_items:
        definitions.append(item.text.strip())
    return {"dictionary": "Ferhengî Xall", "definitions": definitions}

def parse_Ferhenga_Kani(result):
    definitions = []
    list_items = result.select('.resultDef ul li')
    for item in list_items:
        definitions.append(item.text.strip())
    return {"dictionary": "Ferhenga Kanî", "definitions": definitions}

def parse_Ferhengi_Shexani(result):
    definitions = []
    synonyms_div = result.select_one('.resultDef .synonymes')
    if synonyms_div:
        definitions.append(synonyms_div.text.strip())
    return {"dictionary": "Ferhengî Şêxanî", "definitions": definitions}

def parse_Ferhenga_Koma_Kurdiya_Kurmanci(result):
    definitions = []
    list_items = result.select('.resultDef ul li')
    for item in list_items:
        definitions.append(item.text.strip())
    return {"dictionary": "Ferhenga Koma Kurdîya Kurmancî", "definitions": definitions}

def parse_Ferheng_e_Pishk_en_Kurdi(result):
    definitions = []
    entries = result.select('.resultDef > div')
    for entry in entries:
        tag = entry.find("span", {"class": "tag"})
        if tag:
            text = f"{tag.text.strip()}: {entry.text.replace(tag.text, '').strip()}"
        else:
            text = entry.text.strip()
        definitions.append(text)
    return {"dictionary": "Ferheng ê Pîşk ên Kurdî", "definitions": definitions}

def parse_Ferhenga_Desti(result):
    definitions = []
    list_items = result.select('.resultDef ul li')
    for item in list_items:
        definitions.append(item.text.strip())
    return {"dictionary": "Ferhenga Destî", "definitions": definitions}

def parse_placeholder(result):
    return {"dictionary": "Unknown", "definitions": ["Parser not implemented."]}

PARSERS = {
    "Ferhengî Xall": parse_Ferhengi_Xall,
    "Ferhenga Kanî": parse_Ferhenga_Kani,
    "Ferhengî Şêxanî": parse_Ferhengi_Shexani,
    "Ferhenga Koma Kurdîya Kurmancî": parse_Ferhenga_Koma_Kurdiya_Kurmanci,
    "Ferheng ê Pîşk ên Kurdî": parse_Ferheng_e_Pishk_en_Kurdi,
    "Ferhenga Destî": parse_Ferhenga_Desti,

}


def main():
    words = pd.read_csv('esra7.1k-words.csv') # 
    for word in words['wprd-text']: #
        url = f'https://lex.vejin.net/en/search/?t={word}' # 

        response = requests.get(url)
        if response.status_code != 200:
            print("Faileed")
            return

        document = bs4.BeautifulSoup(response.content.decode('utf-8'), features='html.parser')
        results = document.findAll('div', {"class": "result"})

        extracted_data = []
        for result in results:
            dict_name_element = result.select_one('.resultHead span.fromDict')
            if not dict_name_element:
                continue
            dict_name = dict_name_element.text.strip()

            if dict_name in PARSERS:
                parsed_data = PARSERS[dict_name](result)
            else:
                parsed_data = {"dictionary": dict_name, "definitions": ["No parser implemented."]}

            extracted_data.append(parsed_data)

        for data in extracted_data:
            print(f"Dictionary: {data['dictionary']}")
            print("Definitions:")
            for definition in data['definitions']:
                print(f"  - {definition}")
            print("-" * 40)

if __name__ == '__main__':
    main()
