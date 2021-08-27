## pip install tqdm BeautifulSoup4 urllib3

import urllib3
from tqdm import tqdm
from bs4 import BeautifulSoup


def printMovieList(soup):
    i = 1
    movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
    # tqdm - nice progress bar
    for div_item in tqdm(movieList):
        div = div_item.find('div', attrs={'class': 'lister-item-content'})
        print(f'{i}. ', end="")
        header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
        movie_title = (header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')
        print(f'{str(movie_title)}', end="")
        rating_bar = div.findChildren('div', attrs={'class': 'ratings-bar'})
        if rating_bar:
            imdb_rating_div = rating_bar[0].find('div', attrs={'class': 'inline-block ratings-imdb-rating'})
            imdb_rating = (imdb_rating_div.find('strong')).contents[0].encode('utf-8').decode('ascii', 'ignore')
            print(f' --- {str(imdb_rating)} out of 10')
        else:  # for printing purpose
            print()
        i += 1


# replace url in second param in request method
def scrapUrl():
    urlData = urllib3.PoolManager().request('GET',
                                            'https://www.imdb.com/search/title/?release_date=2021&title_type=feature').data
    soup = BeautifulSoup(urlData, "html.parser")
    printMovieList(soup)


if __name__ == '__main__':
    scrapUrl()
