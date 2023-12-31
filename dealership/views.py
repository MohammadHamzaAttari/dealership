from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


@csrf_exempt
def SignUp(request):
    if request.method=='POST':
        try:
            data=JSONParser().parse(request)
            
            user=User.objects.create_user(data['username'],password=data['password'])
            user.save()
            token=Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=201)
        except IntegrityError:
            return JsonResponse({'error':'username already been taken'},status=400)
        
@csrf_exempt
def Login(request):
    if request.method=='POST':
        
        data=JSONParser().parse(request)
        
        user=authenticate(request,username=data['username'],password=data['password'])
        if user is None:
            return JsonResponse({'error':'Could not login, Please check the username and Password'},status=400)
        else:
            try:
                token=Token.objects.get(user=user)
            except:
                token=Token.objects.create(user=user)
                
        return JsonResponse({'token':str(token)},status=200)