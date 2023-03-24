from requests_html import HTMLSession

s = HTMLSession()
query = 'tamilnadu'
url = f'https://www.google.com/search?q=weather+{query}'
r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
# print(r.html.find('title'))
temp = r.html.find('span#wob_tm',first=True).text
# unit = r.html.find('div.vk_bk.wob-unit span.wot_t', first=True).text
unit = r.html.find('div.vk_bk.wob-unit', first=True).find('span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
print(query, temp, unit, desc)