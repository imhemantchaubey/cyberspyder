from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from base.models import Email_accounts_details, Phone_accounts_details
import json
import requests

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    print(request.user.id)
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


class RequestAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, *args, **kwargs):
        email = None
        mobile_no = None
        data = {
            'user': request.user.id,
            'email': request.data.get('email'),
            'mobile_no': request.data.get('mobile_no')
        }
        email = data['email']
        mobile_no = data['mobile_no']
        mobile_api_response = None
        email_api_response = None
        tc_response = None
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

            mobile_api_response = requests.request("GET", url, headers=headers)
            pd = Phone_accounts_details()
            pd.phone_no = mobile_no
            pd.truecaller = json.dumps(tc_response)
            user = User.objects.get(id=request.user.id)
            pd.user = user
            for data in json.loads(mobile_api_response['data']['account_details']):
                flag = mobile_api_response['data']['account_details'][data]['registered']
                cdata = mobile_api_response['data']['account_details'][data]
                if flag == 'true':
                    flag = True
                else:
                    flag = False

                if data == 'facebook':
                    pd.facebook = flag
                if data == 'google':
                    pd.google = json.dumps(cdata)
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
                    pd.skype = json.dumps(cdata)
                if data == 'whatsapp':
                    pd.whatsapp = json.dumps(cdata)
                if data == 'telegram':
                    pd.telegram = json.dumps(cdata)
                if data == 'viber':
                    pd.viber = json.dumps(cdata)
                if data == 'kakao':
                    pd.kakao = json.dumps(cdata)
                if data == 'ok':
                    pd.ok = json.dumps(cdata)
                if data == 'zalo':
                    pd.zalo = json.dumps(cdata)
                if data == 'line':
                    pd.line = json.dumps(cdata)
            pd.save()

            
        if email:
            url = "https://api.seon.io/SeonRestService/email-api/v2.2/" + email
            headers = {
                "X-API-KEY": "ae997e94-4a1f-4cc3-8c45-3a1205605b89"
            }

            email_api_response = requests.request("GET", url, headers=headers)
            email_api_response = email_api_response.json()
            ed = Email_accounts_details()
            ed.email = email
            user = User.objects.get(id=request.user.id)
            ed.user = user
            for data in (email_api_response['data']['account_details']):
            
                flag = email_api_response['data']['account_details'][data]['registered']
                cdata = email_api_response['data']['account_details'][data]
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
            
        return Response({'msg':'data created', 'mobile_data':mobile_api_response, 'email_data':email_api_response, 'truecaller_data':tc_response})
    
class HomeAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = [permissions.IsAuthenticated]
  def get(self,request,*args,**kwargs):
    
    user = User.objects.get(id=request.user.id)
    email_data = Email_accounts_details.objects.filter(user=user)
    phone_data = Phone_accounts_details.objects.filter(user=user)
    email = {"Date":[], "Email":[]}
    phone = {"Date":[], "Phone":[]}
    for i in  email_data:
        email['Date'].append(i.created_at)
        email['Email'].append(i.email)
    
    for i in phone_data:
        phone['Date'].append(i.created_at)
        phone['Phone'].append(i.phone_no)
    return Response({'msg':'Data Fetched', 'email':email, 'phone':phone})