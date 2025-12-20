import requests


class MediaWikiApi:

    def __init__(self, lang: str) -> None:
        match lang:
            case 'ru':
                self.url: str = 'https://ru.wikipedia.org/w/api.php'
            case _:
                pass

    def get_titles(self, srsearch: str, srlimit: int, search_in_text: bool = True):
        """
        """'https://www.mediawiki.org/wiki/API:Tutorial'

        params: dict[str, str] = {
            'action': 'query',
            'format': 'json',
            'list': 'search',
            'srsearch': srsearch,
            'srlimit': srlimit,
        }
        if search_in_text:
            params['srwhat'] = 'text' # Поиск по тексту статей

        response = requests.get(self.url, params=params, headers={'User-Agent': 'MyResearchBot/1.0 (myemail@example.com)'})
        data = response.json()
        results = []
        if 'query' in data:
            for item in data['query']['search']:
                results.append(item['title'])
        return results

    def get_text(self, title: str):
        """_summary_

        :param str title: _description_
        """

        params: dict[str, str] = {
            'action': 'query',
            'prop': 'extracts',
            'explaintext': True,
            'titles': title,
            'format': 'json'
        }

        response = requests.get(self.url, params=params, headers={'User-Agent': 'MyResearchBot/1.0 (myemail@example.com)'})
        data = response.json()

        pages = data.get('query', {}).get('pages', {})
        for page in pages.values():
            return page.get('extract', '')

        return ''