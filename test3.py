import bs4
import requests

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

def parse_Kurdistanica(result):
    pronunciation = result.select_one('.pr')
    pos_tag = result.select_one('.tag.pos')
    definitions = result.select('.defcol .senses')
    data = {
        "pronunciation": pronunciation.text.strip() if pronunciation else None,
        "part_of_speech": pos_tag.text.strip() if pos_tag else None,
        "definitions": {def_col.select_one('.langTitle').text.strip(): def_col.select_one('.senses').text.strip()
                        for def_col in result.select('.defcol')},
    }
    return data

def parse_Henbane_Borine(result):
    definitions = result.select('.defcol')
    data = {
        def_col.select_one('.langTitle').text.strip(): [
            item.text.strip() for item in def_col.select('ol li')
        ]
        for def_col in definitions
    }
    return data

def parse_Merdox(result):
    definitions = result.select('div > span.langTitle')
    data = {
        title.text.strip(): title.find_next_sibling().text.strip() for title in definitions
    }
    return data

def parse_Zhyan(result):
    pronunciation = result.select_one('.pr')
    pos_tag = result.select_one('.tag.pos')
    definitions = result.select('.defcol')
    data = {
        "pronunciation": pronunciation.text.strip() if pronunciation else None,
        "part_of_speech": pos_tag.text.strip() if pos_tag else None,
        "definitions": {def_col.select_one('.langTitle').text.strip(): def_col.select_one('.senses').text.strip()
                        for def_col in definitions},
    }
    return data

def parse_Kurdish_English_Dictionary(result):
    wah_sections = result.select('.wah-se')
    data = []
    for section in wah_sections:
        kurdish_term = section.select_one('.wah-ku .wah-st')
        english_definition = section.select_one('.wah-en')
        pos_tag = section.select_one('.tag.pos')
        data.append({
            "kurdish_term": kurdish_term.text.strip() if kurdish_term else None,
            "english_definition": english_definition.text.strip() if english_definition else None,
            "part_of_speech": pos_tag.text.strip() if pos_tag else None,
        })
    return data

def parse_IT_Dictionary(result):
    data = {"definition": result.text.strip()}
    return data

def parse_Andeek_Dictionary(result):
    pos_tag = result.select_one('.tag.pos')
    definition = result.text.strip().replace(pos_tag.text, '').strip() if pos_tag else result.text.strip()
    data = {
        "part_of_speech": pos_tag.text.strip() if pos_tag else None,
        "definition": definition,
    }
    return data

def parse_Wishename(result):
    definitions = result.select('ul li')
    data = [item.text.strip() for item in definitions]
    return data

def parse_Rejge(result):
    definitions = result.select('.defcol')
    data = {
        def_col.select_one('.langTitle').text.strip(): [
            item.text.strip() for item in def_col.select('ol')
        ]
        for def_col in definitions
    }
    return data

PARSERS = {
    "Ferhengî Xall": parse_Ferhengi_Xall,
    "Ferhenga Kanî": parse_Ferhenga_Kani,
    "Ferhengî Şêxanî": parse_Ferhengi_Shexani,
    "Ferhenga Koma Kurdîya Kurmancî": parse_Ferhenga_Koma_Kurdiya_Kurmanci,
    "Ferheng ê Pîşk ên Kurdî": parse_Ferheng_e_Pishk_en_Kurdi,
    "Ferhenga Destî": parse_Ferhenga_Desti,
    "Kurdistanica": parse_Kurdistanica,
    "Henbane Borîne": parse_Henbane_Borine,
    "Ferhengî Merdox": parse_Merdox,
    "Zhyan": parse_Zhyan,
    "A Kurdish-English Dictionary": parse_Kurdish_English_Dictionary,
    "IT Dictionary": parse_IT_Dictionary,
    "Andeek Dictionary": parse_Andeek_Dictionary,
    "Ferhengî Wişename": parse_Wishename,
    "Ferhengî Rêjge": parse_Rejge,
} #15 out of 17 dictionaries


def main():
    url = 'https://lex.vejin.net/en/search/?t=%DA%A9%D9%88%D8%B1%D8%AF%DB%8C&f=0'
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
