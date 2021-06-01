from bs4 import BeautifulSoup
import requests

class kissmangaapi():
    def __init__(self, query, mangaid, chapterNo):
        self.query = query
        self.mangaid = mangaid
        self.chapterNo = chapterNo

    def mangaSearch(query):
        try:
            url = f"http://kissmanga.nl/search?q={query}"
            response = requests.get(url)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'lxml')
            manga2 = soup.findAll("div", class_="media mainpage-manga")
            manga_search_list = []
            for manga in manga2:
                mangatitle = manga.a["title"]
                link = manga.a["href"]
                split = link.split("/")
                split2 = split[-1].split("?")
                mangaid = split2[0]
                r = (mangatitle, mangaid)
                manga_search_list.append(r)
            if manga_search_list == []:
                return "No search results found for the query"           
            return res_list_search
        except requests.exceptions.ConnectionError:
            return "Check the host's network Connection"
       
    def mangaDetails(mangaid):
        try:
            url = f"http://kissmanga.nl/manga/{mangaid}"
            response = requests.get(url)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'lxml')
            mangatitle = soup.find("h1", class_="title-manga")
            image = soup.find("div", class_="media-left cover-detail").img
            image_link = image["src"]
            gen_man_list = []
            genres = soup.find("p", class_="description-update").findAll("a")
            for genre in genres:
                gen_man_list.append(genre.text)
            chap = soup.find("a", class_="xanh")
            chapter = chap["title"]
            chapSplit = chapter.split(' ')
            chaplast = chapSplit[-1]
            return [mangatitle.text, imagelink, gen_man_list[:-2], chapterlast]
        except AttributeError:
            return "No search results found for the Mangaid"
        except requests.exceptions.ConnectionError:
            return "Check the host's network Connection"

    def mangaChapter(mangaid, chapterNo): 
        try:
            Url = f"http://kissmanga.nl/{mangaid}-chapter-{chapterNo}"
            results = requests.get(Url)
            plaintext = results.text
            soup = BeautifulSoup(plaintext, "lxml")
            sourceurl = soup.find("div", {"class": "chapter-content-inner text-center image-auto"}).p
            mangalinks = sourceurl.text
            mangalinksSplit = mangalinks.split(",")
            totalPages = len(mangalinksSplit)
            return mangalinksSplit
        except AttributeError:
            return "No search results found for the Chapter Number"
        except requests.exceptions.ConnectionError:
            return "Check the host's network Connection"

def mangaLatest():
        try:
            url = f"http://kissmanga.nl"
            response = requests.get(url)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'lxml')
            manga2 = soup.findAll("div", class_="media mainpage-manga")
            manga_search_list = []
            for manga in manga2:
                mangatitle = manga.a["title"]
                link = manga.a["href"]
                r = (mangatitle)
                manga_search_list.append(r)
            if manga_search_list == []:
                return "No search results found for the query"           
            return res_list_search
        except requests.exceptions.ConnectionError:
            return "Check the host's network Connection"
       
