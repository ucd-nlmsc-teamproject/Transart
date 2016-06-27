__author__ = 'fanfan'

import urllib
from datetime import datetime
from bs4 import BeautifulSoup
import nltk
import pytz

from articles.models import Article

def createArticleObject(title, subtitle, body, date, keywords, url, type, source):
    #print([title, subtitle, body, date, keywords, url, type, source])
    print("3")
    # media_image=str(media_image)
    # print(media_image)
    # print(type(type))
    # print(type(media_image))
    try:
        article = Article(Headline=title, SubHeadline=subtitle,
                      Content=body, Url=url,
                      DateTime=date, Keywords=keywords,
                      Type=type,
                      Source=source)
        print("5")
    except Exception as err:
                print("In createArticleObject():"+ err)
    return article

def createArticleByUrl(url):
    print("1")
    [title, subtitle, body, date, keywords, source] = getArticleDetailsByUrl(url)
    print("2")
    article = createArticleObject(title, subtitle, body, date, keywords, url, "RSS", source)
    return article



def getArticleDetailsByUrl(url):
    print("getarticle.......enter.......")
    # request = urllib.request.Request(url)
    # request.add_header('Accept-Encoding','gzip, deflate')
    # page = urllib.request.urlopen(url).read()
    # soup = BeautifulSoup(page,"html.parser")
    # soup.prettify()
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page,"html.parser")
    soup.prettify()
    title = soup.title.string
    #print("in getArticlesDetails(), title: "+ title + " Done!")

    title_clean = str.split(soup.title.string, ' | ')[0]
    doc_descr = soup.head.find("meta",attrs={"name":"description"}).get('content')
    doc_body = ''
    print("enter2.........")

    if "Chinadaily" in title:
        for body_p_tag in soup.find("div",attrs={"id": "Content"}).find_all("p"):
       # for body_p_tag in soup.article.find_all("p"):
            doc_body += body_p_tag.get_text() + '\n'
            doc_body=doc_body.strip()

    elif "BBC" in title:
        for tag in soup.find("div", attrs={"class": "story-body"}).find_all("p"):
            if "JavaScript" not in tag.get_text():
                doc_body += tag.get_text() + '\n'


    print("Hello.........")
    print("Chinadaily" in title)

    date = datetime.utcnow()
    source = "Other"
    if "Chinadaily" in title or "chinadaily" in title:
        source = "ChinaDaily"
        #body_p_tag = soup.article.find("div", attrs={"class": "last_updated"}).find("p")
       # body_p_tag = soup.head.find("meta", attrs={"itemprop": "datePublished"}).get('content')
        #body_p_tag = soup.body.find("class", attrs={"class": "greyTxt6 block mb15"})
        body_p_tag = soup.head.find("meta", attrs={"name": "publishdate"}).get('content')
        print("A")
        print(body_p_tag)
        #date = datetime.strptime(body_p_tag.get_text(), "%a, %b %d, %Y, %H:%M")
        date = datetime.strptime(body_p_tag, " %Y-%m-%d")
        #date = body_p_tag
        print("B")
        local_dt = pytz.timezone('Europe/Dublin').localize(date, is_dst=None)
        print("C")
        date = local_dt.astimezone(pytz.utc)
        print("D")
    elif "BBC" in title:
        source = "BBC"
        tag = soup.find("div", attrs={"class": "date date--v2"})
        print("A")
        date = tag.get_text()
        print("B")
        #print(date)
        #tag = soup.find("span", attrs={"class": "time"})
        #date += " " + tag.get_text()
        if "GMT" in date:
            date = datetime.strptime(date, "%d %B %Y")
        else:
            date = datetime.strptime(date, "%d %B %Y")
            local_dt = pytz.timezone('Europe/Dublin').localize(date, is_dst=None)
            date = local_dt.astimezone(pytz.utc)
        media_image = soup.find("img", attrs={"class": "js-image-replace"}).get("src")
        print("before")
        print(media_image);
        print(type(media_image))
        print("after")

    keywords = extractKeywords(title_clean)


    #print([title_clean, doc_descr, doc_body, date, keywords, source])

    return [title_clean, doc_descr, doc_body, date, keywords, source]


def extractKeywords(text):
    stop_words = load_stopwords()
    keywords = []
    tokens = nltk.word_tokenize(text)
    #print(tokens)

    for token in tokens:
        if token not in stop_words:
            keywords.append(token.lower())

    #print(keywords)
    return ", ".join(keywords)

def load_stopwords():
    stop_words = nltk.corpus.stopwords.words('english')
    # custom stop words
    stop_words.extend(['this', 'that', 'the', 'might', 'have', 'been', 'from',
                           'but', 'they', 'will', 'has', 'having', 'had', 'how', 'went'
                            'were', 'why', 'and', 'still', 'his','her',
                           'was', 'its', 'per', 'cent',
                           'a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among',
                           'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can',
                           'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every',
                           'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his',
                           'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let',
                           'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor',
                           'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said',
                           'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their',
                           'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us',
                           'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who',
                           'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your', 've', 're', 'rt'])
    #turn list into set for faster search
    stop_words = set(stop_words)
    return stop_words