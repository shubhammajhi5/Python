from requests_html import HTMLSession

session = HTMLSession()
source = session.get('https://coreyms.com/').html

articles = source.find('article')

for article in articles:
    try:
        title = article.find('.entry-title-link', first = True).text
        release_date = article.find('.entry-time', first = True).text
        filed_under = article.find('.entry-categories', first = True).text.split(': ')[1]
        tagged_with = article.find('.entry-tags', first = True).text.split(': ')[1]
        summary = article.find('.entry-content p', first = True).text
        vid_code = article.find('iframe', first = True).attrs['src'].split('/')[4].split('?')[0]
        link = f'https://www.youtube.com/watch?v={vid_code}'
        print(title, summary, filed_under, tagged_with, link)
        
    except:
        pass