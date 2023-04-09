from django.http import HttpResponse
from .models import Phone_accounts_details, Email_accounts_details
import requests
from django.contrib.auth.models import User
import json
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
def home(request):
    user = User.objects.get(id=request.user.id)
    email_data = Email_accounts_details.objects.filter(user=user)
    phone_data = Phone_accounts_details.objects.filter(user=user)
    date = []
    type = []
    for i in  email_data:
        date.append(i.created_at)
        type.append(i.email)
        
    
    for i in phone_data:
        date.append(i.created_at)
        type.append(i.phone_no)

    context = {'msg':'Data Fetched', 'date':date, 'type': type}
    return render(request, 'base/home.html', context = context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="base/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def result(request):
    email = request.POST.get('email', None)
    mobile_no = request.POST.get('mobile_no', None)
    mobile_api_response = None
    email_api_response = None
    m_out = []
    m_head = []
    e_out = []
    e_head = []
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
        mobile_api_response = mobile_api_response.json()
        pd = Phone_accounts_details()
        pd.phone_no = mobile_no
        pd.truecaller = json.dumps(tc_response)
        for data in mobile_api_response['data']['account_details']:
            flag = mobile_api_response['data']['account_details'][data]['registered']
            data = mobile_api_response['data']['account_details'][data]
            # if flag == 'true':
                
            #     flag = True
            # else:
            #     flag = False

            if data == 'facebook':
                pd.facebook = flag
                m_out.append(flag)
                m_head.append(data)
            if data == 'google':
                pd.google = json.dumps(data)
            if data == 'twitter':
                m_out.append(flag)
                m_head.append(data)
                pd.twitter = flag
            if data == 'instagram':
                m_out.append(flag)
                m_head.append(data)
                pd.instagram = flag
            if data == 'yahoo':
                m_out.append(flag)
                m_head.append(data)
                pd.yahoo = flag
            if data == 'microsoft':
                m_out.append(flag)
                m_head.append(data)
                pd.microsoft = flag
            if data == 'snapchat':
                m_out.append(flag)
                m_head.append(data)
                pd.snapchat = flag
            if data == 'kakao':
                pd.kakao = flag
            if data == 'flipkart':
                m_out.append(flag)
                m_head.append(data)
                pd.flipkart = flag
            if data == 'bukalapak':
                pd.bukalapak = flag
            if data == 'skype':
                m_out.append(flag)
                m_head.append(data)
                pd.skype = json.dumps(data)
            if data == 'whatsapp':
                m_out.append(flag)
                m_head.append(data)
                pd.whatsapp = json.dumps(data)
            if data == 'telegram':
                m_out.append(flag)
                m_head.append(data)
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

        email_api_response = requests.request("GET", url, headers=headers)
        email_api_response = email_api_response.json()
        ed = Email_accounts_details()
        ed.email = email
        
        for data in (email_api_response['data']['account_details']):
           
            flag = email_api_response['data']['account_details'][data]['registered']
            print(flag)
            cdata = email_api_response['data']['account_details'][data]
            # if flag == 'True':
            #     flag = True
            # else:
            #     flag = False

            if data == 'apple': 
                e_out.append(flag)
                e_head.append(data)
                ed.apple = flag
            if data == 'ebay':
                e_out.append(flag)
                e_head.append(data)
                ed.ebay = flag
            if data == 'github':
                e_out.append(flag)
                e_head.append(data)
                ed.github = flag
            if data == 'instagram':
                e_out.append(flag)
                e_head.append(data)
                ed.instagram = flag
            if data == 'lastfm':
                ed.lastfm = flag
            if data == 'microsoft':
                e_out.append(flag)
                e_head.append(data)
                ed.microsoft = flag
            if data == 'myspace':
                ed.myspace = flag
            if data == 'pinterest':
                e_out.append(flag)
                e_head.append(data)
                ed.pinterest = flag
            if data == 'spotify':
                ed.spotify = flag
            if data == 'tumblr':
                ed.tumblr = flag
            if data == 'twitter':
                e_out.append(flag)
                e_head.append(data)
                ed.twitter = flag
            if data == 'vimeo':
                ed.vimeo = flag
            if data == 'weibo':
                ed.weibo = flag
            if data == 'yahoo':
                e_out.append(flag)
                e_head.append(data)
                ed.yahoo = flag
            if data == 'discord':
                e_out.append(flag)
                e_head.append(data)
                ed.discord = flag
            if data == 'kakao':
                ed.kakao = flag
            if data == 'booking':
                ed.booking = flag
            if data == 'amazon':
                e_out.append(flag)
                e_head.append(data)
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
                e_out.append(flag)
                e_head.append(data)
                ed.flipkart = flag
            if data == 'bukalapak':
                ed.bukalapak = flag
            if data == 'archiveorg':
                ed.archiveorg = flag
            if data == 'lazada':
                ed.lazada = flag
            if data == 'zoho':
                e_out.append(flag)
                e_head.append(data)
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

    context = {'msg':'data created', 'm_out':m_out, 'm_head':m_head, 'e_out':e_out, 'e_head': e_head, 'email':email, 'phone':mobile_no}
    return render(request, 'base/result.html', context=context)

