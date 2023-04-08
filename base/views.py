from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone_accounts_details, Email_accounts_details
import requests
import json

# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def result(request):
    email = request.POST.get('email', None)
    mobile_no = request.POST.get('mobile_no', None)
    if mobile_no:
        url = "https://truecaller4.p.rapidapi.com/api/v1/getDetails"
        querystring = {"phone":mobile_no,"countryCode":"IN"}
        headers = {
            "X-RapidAPI-Key": "dfdb3ad499msh35fefbe08b931f3p19c36djsn2017e5e59104",
            "X-RapidAPI-Host": "truecaller4.p.rapidapi.com"
        }
        tc_response = requests.request("GET", url, headers=headers, params=querystring)

        url = "https://api.seon.io/SeonRestService/phone-api/v1.4/" + mobile_no
        headers = {
            "X-API-KEY": "ae997e94-4a1f-4cc3-8c45-3a1205605b89"
        }

        api_response = requests.request("GET", url, headers=headers)
        pd = Phone_accounts_details()
        pd.phone_no = mobile_no
        pd.truecaller = json.dumps(tc_response)
        for data in json.loads(api_response['data']['account_details']):
            flag = api_response['data']['account_details'][data]['registered']
            data = api_response['data']['account_details'][data]
            if flag == 'true':
                flag = True
            else:
                flag = False

            if data == 'facebook':
                pd.facebook = flag
            if data == 'google':
                pd.google = json.dumps(data)
            if data == 'twitter':
                pd.twitter = flag
            if data == 'instagram':
                pd.instagram = flag
            if data == 'yahoo':
                pd.yahoo = flag
            if data == 'microsoft':
                pd.microsoft = flag
            if data == 'snapchat':
                pd.snapchat = flag
            if data == 'kakao':
                pd.kakao = flag
            if data == 'flipkart':
                pd.flipkart = flag
            if data == 'bukalapak':
                pd.bukalapak = flag
            if data == 'skype':
                pd.skype = json.dumps(data)
            if data == 'whatsapp':
                pd.whatsapp = json.dumps(data)
            if data == 'telegram':
                pd.telegram = json.dumps(data)
            if data == 'viber':
                pd.viber = json.dumps(data)
            if data == 'kakao':
                pd.kakao = json.dumps(data)
            if data == 'ok':
                pd.ok = json.dumps(data)
            if data == 'zalo':
                pd.zalo = json.dumps(data)
            if data == 'line':
                pd.line = json.dumps(data)
        pd.save()

        
    if email:
        url = "https://api.seon.io/SeonRestService/email-api/v2.2/" + email
        headers = {
            "X-API-KEY": "ae997e94-4a1f-4cc3-8c45-3a1205605b89"
        }

        api_response = requests.request("GET", url, headers=headers)
        api_response = api_response.json()
        ed = Email_accounts_details()
        ed.email = email
        
        for data in (api_response['data']['account_details']):
           
            flag = api_response['data']['account_details'][data]['registered']
            cdata = api_response['data']['account_details'][data]
            if flag == 'true':
                flag = True
            else:
                flag = False

            if data == 'apple':
                print('in in in in ')
                ed.apple = flag
            if data == 'ebay':
                ed.ebay = flag
            if data == 'github':
                ed.github = flag
            if data == 'instagram':
                ed.instagram = flag
            if data == 'lastfm':
                ed.lastfm = flag
            if data == 'microsoft':
                ed.microsoft = flag
            if data == 'myspace':
                ed.myspace = flag
            if data == 'pinterest':
                ed.pinterest = flag
            if data == 'spotify':
                ed.spotify = flag
            if data == 'tumblr':
                ed.tumblr = flag
            if data == 'twitter':
                ed.twitter = flag
            if data == 'vimeo':
                ed.vimeo = flag
            if data == 'weibo':
                ed.weibo = flag
            if data == 'yahoo':
                ed.yahoo = flag
            if data == 'discord':
                ed.discord = flag
            if data == 'kakao':
                ed.kakao = flag
            if data == 'booking':
                ed.booking = flag
            if data == 'amazon':
                ed.amazon = flag
            if data == 'qzone':
                ed.qzone = flag
            if data == 'adobe':
                ed.adobe = flag
            if data == 'mailru':
                ed.mailru = flag
            if data == 'wordpress':
                ed.wordpress = flag
            if data == 'imgur':
                ed.imgur = flag
            if data == 'disneyplus':
                ed.disneyplus = flag
            if data == 'netflix':
                ed.netflix = flag
            if data == 'jdid':
                ed.jdid = flag
            if data == 'flipkart':
                ed.flipkart = flag
            if data == 'bukalapak':
                ed.bukalapak = flag
            if data == 'archiveorg':
                ed.archiveorg = flag
            if data == 'lazada':
                ed.lazada = flag
            if data == 'zoho':
                ed.zoho = flag
            if data == 'samsung':
                ed.samsung = flag
            if data == 'evernote':
                ed.evernote = flag
            if data == 'envato':
                ed.envato = flag
            if data == 'patreon':
                ed.patreon = flag
            if data == 'tokopedia':
                ed.tokopedia = flag
            if data == 'rambler':
                ed.rambler = flag
            if data == 'quora':
                ed.quora = flag
            if data == 'atlassian':
                ed.atlassian = flag
            if data == 'facebook':
                ed.facebook = json.dumps(cdata)
            if data == 'flickr':
                ed.flickr = json.dumps(cdata)
            if data == 'foursquare':
                ed.four_square = json.dumps(cdata)
            if data == 'github':
                ed.github = flag
            if data == 'google':
                ed.google = json.dumps(cdata)
            if data == 'gravatar':
                ed.gravatar = json.dumps(cdata)
            if data == 'linkedin':
                ed.linkedin = json.dumps(cdata)
            if data == 'skype':
                ed.skype = json.dumps(cdata)
            if data == 'ok':
                ed.ok = json.dumps(cdata)
            if data == 'airbnb':
                ed.airbnb = json.dumps(cdata)
            
        ed.save()


    return render(request, 'base/result.html')
