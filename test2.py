import bs4
import requests


def Ferhengi_Xall_parser(result):
    meanings = result.select('.resultDef')[0].find_all('span')

    for meaning in meanings:
        print(meaning.text)


def main():
    html = requests.get('https://lex.vejin.net/en/search/?t=%D9%87%D9%84%D8%A7%DA%A4%DB%8E%D8%AA%D9%86')
    document = bs4.BeautifulSoup(html.content.decode('utf-8'), features='html.parser')

    results = document.findAll('div', {"class": "result"})

    for result in results:
        dict_name = result.select('span')[0].text

        if dict_name == 'Ferhengî Xall':
            data = Ferhengi_Xall_parser(result)
        elif dict_name == 'Henbane Borîne':
            pass


if __name__ == '__main__':
    main()

Kurdistanica//
Henbane Borîne//

Ferhengî Wişename//

Ferhengî Xall//
Ferhengî Merdox//
Ferhenga Destî//
Zhyan//
Ferhengî Şêxanî//
Ferhenga Kanî//

Ferhengî Newekan

Ferhenga Koma Kurdîya Kurmancî//
A Kurdish-English Dictionary//

Ferhengî Rêjge//

Andeek Dictionary//

IT Dictionary//

Ferheng ê Pîşk ên Kurdî//

Xişil û Poşakî Jinaney Mukiryan



<div class="result"><div class="resultHead ltr"><a href="/en/def/kurdistanica/bra">bra <span class="fromDict">Kurdistanica</span></a></div><div class="resultDef rtl"><div class="senses ltr"><span class="pr">/brɑː/</span>
 <span class="tag pos">noun</span>
</div>

<div class="twocol"><div class="defcol"><div class="langTitle">کوردی:</div><div class="senses rtl">مەمک‌بەند، سینەبەند، شاماکی (braless <span class="tag pos">adjective</span>
)</div>

</div><div class="defcol"><div class="langTitle">فارسی:</div><div class="senses rtl">کرست</div></div></div></div></div>


<div class="result"><div class="resultHead rtl"><a href="/en/def/henbaneborine/شاماکی">شاماکی <span class="fromDict">Henbane Borîne</span></a></div><div class="resultDef rtl"><div class="twocol"><div class="defcol"><div class="langTitle">کوردی:</div><ol><li>مەمک بەند</li>
</ol></div><div class="defcol"><div class="langTitle">فارسی:</div><ol>
<li>پستان بند</li>
</ol></div></div></div></div>



<div class="result"><div class="resultHead rtl"><a href="/en/def/merdox/کورد">کورد <span class="fromDict">Ferhengî Merdox</span></a></div><div class="resultDef rtl"><div><span class="langTitle">کوردی:</span>  <span class="tag note">(گەلێکن لە ڕەگەزی ئاری.)</span>
</div><div><span class="langTitle">فارسی:</span> 
 کُرد. (گروهی هستند از نژاد آری.)</div><div><span class="langTitle">العربية:</span> 
 كُرد.</div>
</div></div>




<div class="result"><div class="resultHead ltr"><a href="/en/def/zhyan/Kurd">Kurd <span class="fromDict">Zhyan</span></a></div><div class="resultDef rtl"><div class="senses ltr"><span class="pr">/kɜːrd/</span>
 <span class="tag pos">noun</span>
</div>

<div class="twocol"><div class="defcol"><div class="langTitle">کوردی:</div><div class="senses rtl">کورد، خەڵکی کوردستان</div>

</div><div class="defcol"><div class="langTitle">فارسی:</div><div class="senses rtl">کرد، اهل کردستان</div></div></div></div></div>



<div class="result"><div class="resultHead ltr"><a href="/en/def/wahby-edmonds/Kurd">Kurd <span class="fromDict">A Kurdish-English Dictionary</span></a></div><div class="resultDef ltr"><div class="wah"><span class="tag pos">noun and adjective</span> <span class="wah-en">Kurd, Kurdish</span>
<div class="wah-se"><span class="wah-ku"><span class="wah-st">Kurd</span>ayetî</span>: <span class="tag pos">noun</span> <span class="wah-en">Kurdish patriotic movement</span></div><div class="wah-ex">(<span class="wah-ku"><span class="wah-st">Kurd</span>ayetî kirdin</span>: <span class="wah-en">be an active Kurdish nationalist</span>)</div><div class="wah-se"><span class="wah-ku"><span class="wah-st">Kurd</span>enamûsî</span>: <span class="tag pos">noun</span> generally <span class="wah-ku">kirdin e <span class="wah-st">Kurd</span>enamûsî</span>: <span class="wah-en">fulfil patriotic obligation to help other Kurd in need</span></div><div class="wah-se"><span class="wah-ku"><span class="wah-st">Kurd</span>ewarî</span>: <span class="tag pos">noun</span> <span class="wah-en">the Kurdish world, something typically Kurdish</span></div><div class="wah-se"><span class="wah-ku"><span class="wah-st">Kurd</span>istan</span>: <span class="tag pos">noun</span> <span class="wah-en">land of the Kurds</span></div><div class="wah-se"><span class="wah-ku"><span class="wah-st">Kurd</span>î</span>: <span class="tag pos">adjective and noun</span> <span class="wah-en">Kurdish, the Kurdish language</span></div></div></div></div>



<div class="result"><div class="resultHead ltr"><a href="/en/def/zkurd-IT/web">web <span class="fromDict">IT Dictionary</span></a></div><div class="resultDef rtl">وێب</div></div>



<div class="result"><div class="resultHead ltr"><a href="/en/def/andeek/web">web <span class="fromDict">Andeek Dictionary</span></a></div><div class="resultDef rtl"><span class="tag pos">noun</span> تۆڕی جاڵجاڵۆکە</div></div>



<div class="result"><div class="resultHead rtl"><a href="/en/def/wishename/گوڕی">گوڕی <span class="fromDict">Ferhengî Wişename</span></a></div><div class="resultDef rtl"><ul><li>گوڕی</li>
<li>بە کەیفی</li>
<li>بە هێزی و توانایی</li></ul></div></div>



<div class="result"><div class="resultHead rtl"><a href="/en/def/reejge/ڕێژگە">ڕێژگە <span class="fromDict">Ferhengî Rêjge</span></a></div><div class="resultDef rtl"><div class="twocol"><div class="defcol"><div class="langTitle">کوردی:</div><ol><div class="tag note">مانای تر جگە لە مانای هەنبانەبۆرینە</div>
 ئەوشوێنەی کە چۆمەڵ تێکەڵ ڕووباری گەورە دەبێ.شوێنی تێکەڵ‌بوونەوەی دوو چۆم.
</ol></div><div class="defcol"><div class="langTitle">فارسی:</div><ol>
محل به‌هم پیوستن دو رودخانه‌</ol></div></div></div></div>