# from mediawikiapi import MediaWikiAPI
from mediawikiapi import MediaWikiApi

# mediawikiapi = MediaWikiAPI()
# mediawikiapi.config.language = 'ru'

# titles = mediawikiapi.search("Пермский период", results=20)
# print(titles)

# for i, title in enumerate(titles, 1):
#     print(f"\n[{i}/{len(titles)}] Загружаю: {title}")
#     page = mediawikiapi.page(title)
#     full_content = page.content
#     print(full_content)

m = MediaWikiApi()
titles = m.get_titles('Пермский период')
print(titles)
print(m.get_text(titles[0]))