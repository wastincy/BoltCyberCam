from django.shortcuts import render
import pyrebase

config = {
  'apiKey': "AIzaSyB64vSByVmE47k11lRRmPkSXwu0IJjGgUs",
  'authDomain': "cybercam-67066.firebaseapp.com",
  'databaseURL': "https://cybercam-67066-default-rtdb.firebaseio.com",
  'projectId': "cybercam-67066",
  'storageBucket': "cybercam-67066.appspot.com",
  'messagingSenderId': "419241012586",
  'appId': "1:419241012586:web:68a066dd0e56c2f6124913",
  'measurementId': "G-XLT8HZNYP2"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def singin(request):
    return render(request, 'main/singin.html')
def index(request):
    return render(request, 'main/index.html')
def postsing(request):
    '''email = request.POST.get('email')
    passw = request.POST.get('pass')
    user = auth.sign_in_with_email_and_password(email, passw)'''
    return render(request, 'main/welcome.html')

