from bs4 import BeautifulSoup
import requests
import re

# FIRST SCRAPE LYRICS FROM GENIUS
# first go to genius.com and scrape lyrics information from the site



all_links = []

def scrap_page(page_url):
    read_lyrics(page_url)
    links = get_page_links(page_url)
    for link in links:
        scrap_page(link)



# read lyrics for the song
def read_lyrics(page_url):

    result = requests.get(page_url)
    html_page = result.content
    soup = BeautifulSoup(html_page)

    # start extracting information from the site
    tittle = soup.select(".header_with_cover_art-primary_info-title")
    artist = soup.select(".header_with_cover_art-primary_info-primary_artist")
    featuring = soup.select(".drop-target drop-element-attached-top.drop-target-attached-bottom.drop-element-attached-center.drop-target-attached-center")
    producer = soup.select(".drop-target.drop-element-attached-top.drop-target-attached-bottom.drop-element-attached-center.drop-target-attached-center")
    lyrics = soup.select(".lyrics")


    if len(lyrics) > 0:

        for a in lyrics[0].findAll('a'):
            a.decompose()

        lyrics = lyrics[0].findChildren("p")

        text_lyrics = ""
        for lyric in lyrics:
            text_lyrics += str(lyric)
            text_lyrics += '\n'

        tittle = tittle[0].text
        artist = artist[0].text
        if len(featuring) > 0:
            featuring = featuring[0].text
        if len(producer) > 0:
            producer = producer[0].text

        print(tittle)
        print(artist)
        print(featuring)
        print(producer)
        # print(lyrics)

        print('------------------------')


# get all links on the site
def get_page_links(page_url):
    global all_links
    result = requests.get(page_url)
    html_page = result.content
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^https://genius.com/")}):
        if link.get('href') not in all_links:
            links.append(link.get('href'))
            all_links.append(link.get('href'))

    return links

def clean_lyrics(dirty_lyrics):
    print(dirty_lyrics)

scrap_page("https://genius.com/Jala-brat-and-buba-corelli-kamikaza-lyrics")