from django.shortcuts import render
from django.views.generic import TemplateView 

# import pyrebase


# # import requests.packages.urllib3.contrib.appengine
# # from urllib3.contrib.appengine import is_appengine_sandbox

# config={
#     'apiKey': "AIzaSyD9qiYtSXNNqMLWMw4GzfWdBFO-s35nhXo",
#     'authDomain': "shopify-c1c38.firebaseapp.com",
#     'projectId': "shopify-c1c38",
#     'storageBucket': "shopify-c1c38.appspot.com",
#     'messagingSenderId': "95670561450",
#     'appId': "1:95670561450:web:415158d81bc03618e0fed3",
#     'databaseURL': "https://shopify-c1c38-default-rtdb.firebaseio.com",
# }

# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()
# # Create your views here.

class map(TemplateView):
    template_name = "map.html"


# def index(request):
#     channel_name=database.child('Data').child('Name').get().val()
#     channel_type=database.child('Data').child('Type').get().val()
#     channel_sub=database.child('Data').child('Sub').get().val()
#     return render(request,'index.html' , {
#         "channel_name": channel_name,
#         "channel_type": channel_type,
#         "channel_sub": channel_sub
        
#     })