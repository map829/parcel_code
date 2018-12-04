# https://www.post.ch/de/geschaeftlich/themen-a-z/praktisches-empfaengerkunden/empfaengerservices-briefe/sendungen-verfolgen-url
# created with the guide lines defined by Post

import requests
from lxml import html
import sys

def parcel_code ():
    #get pacel tracking number from database
    parcel_NR = '99.60.038478.0000.1341' # function not created as of this point
    return (parcel_NR)

def open_link (parcel_NR):
    link = 'https://www.post.ch/swisspost-tracking?formattedParcelCodes='
    link = link + str(parcel_NR) + str('&&p_language=de')
    try:
        r = requests.get(link)
        mailing_status = html.fromstring('<table class="events_view fullview_tabledata" cellpadding="0" cellspacing="0">')
        mailing_out = mailing_status.xpath('//div[@class="events_view fullview_tabledata"]/text()')[0]
    except requests.exceptions.RequestException as e:
        print(e)

#def writeHTMLWrapper (html):


if __name__ == '__main__':
    parcel_NR = parcel_code()
    open_link(parcel_NR)
