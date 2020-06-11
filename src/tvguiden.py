from bs4 import BeautifulSoup as _bs
import requests as _requests
import datetime as _dt
from datetime import timedelta
from src import channel as tvshow

_baseURL = "http://tvtid.tv2.dk"
_programUrl = "https://tvtid.tv2.dk/program/{0}/{1}"

def getChannels():
    response = _requests.get(_baseURL)
    if response.ok:
        doc = _bs(response.text, "html.parser")
        channels = dict()
        articles =  doc.findAll("article",{"class":"tv2epg-channel"})
        for article in articles:
            data = tvshow.Channel(article.find('header')['title'], article['data-channel-id'])
            channels[data.name] = data
        return channels


def get_content(channel_id:str, program_id:str):
    response = _requests.get(_programUrl.format(channel_id, program_id))
    if response.ok:
        doc = _bs(response.text, "html.parser")
        try:
            data = doc.find('div',{"class":"o-article_body"}).find('p').text
            return data
        except AttributeError:
            """There might not be any text, so pass and return empty string"""
            pass
    return ""

def getChannel(dataChannelId):
    response = _requests.get(_baseURL)
    if response.ok:
        doc = _bs(response.text,'html.parser')
        channel =  doc.find("article", {"class":"tv2epg-channel","data-channel-id":dataChannelId})
        channelList = channel.find("ul", {"class":"tv2epg-program"})
        returnValue = []
        isToday = True
        rightNow = _dt.datetime.now()
        tomorrow = False
        for li in channelList.findAll('li'):
            time = li.find('a').find('time')
            hour, minute = [int(x) for x in time.text.split(':')]
            title = li['title']
            data_program_id = li['data-program-id']
            start = _dt.datetime.fromtimestamp(int(li['data-start']))
            stop = _dt.datetime.fromtimestamp(int(li['data-stop']))

            date = _dt.datetime(year=rightNow.year, month=rightNow.month, day=rightNow.day, hour=hour, minute=minute)

            if not tomorrow and len(returnValue) > 0:
                lastEntry = returnValue[len(returnValue) - 1].start
                if lastEntry > date:
                    tomorrow=True

            if tomorrow:
                date = date + timedelta(days=1)
            content = get_content(dataChannelId, data_program_id)
            program = tvshow.Program(name=title, start=start, stop=stop, program_id=data_program_id, content=content)
            returnValue.append(program)
        return tvshow.Listing(returnValue)
