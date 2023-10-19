from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import *
from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from .serializer import *
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, filters
import requests
import json
from rest_framework.response import Response
from django.http import Http404
import base64
import sys
from rest_framework.decorators import api_view







# 6 Generics 
#6.1 get and post
class generics_list_msgstypes(generics.ListCreateAPIView):
    queryset = MeesageType.objects.all()
    serializer_class = MsgsTypesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


   
   # authentication_classes = [TokenAuthentication]
    #authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

#6.2 get put and delete 
class generics_pk_msgstypes(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeesageType.objects.all()
    serializer_class = MsgsTypesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    

######################################


###############################################


class AllInfoRelatedToIDView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
    def retrieve(self, request, *args, **kwargs):
        id = self.kwargs.get('id')  # ������ ��� ���� �� ������� URL
        msgtype = MeesageType.objects.get(id=id)  # ������ ��� ��� MessageType �������� ������
        related_messages = Messages.objects.filter(ID_Type_id=msgtype.id)  # ������ ��� ������� �������� �� ���� Messages
        
        msgtype_serializer = MsgsTypesSerializer(msgtype)  # ����� ��� MessageType ��� ������ ����� �������
        messages_serializer = MessegasSerializer(related_messages, many=True)  # ����� ������� �� Messages ��� ������ ����� �������
        
        return Response({
            'message_type_info': msgtype_serializer.data,
            'related_messages_info': messages_serializer.data
        })
    

    
class generics_msgs(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessegasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

#6.2 get put and delete 
class generics_pk_msgs(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessegasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
   


#2 model data default djanog without rest
def msgtypes_api(request):
    data = MeesageType.objects.all()
    response = {

        'MsgsTypesModel': list(data.values('id','MsgTypes','new_msg'))
        #'guests': dict(data.values('name','mobile'))

    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})



def msgsapi (request,id):
    msgtype = MeesageType.objects.get(id=id)
    msg=Messages.objects.all().filter(ID_Type_id=msgtype.id)

    response = {
        'MsgsModel':list(msg.values('id','MessageName','new_msgs','ID_Type_id'))

    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})








def no_rest_msgs_all (request):
    data = Messages.objects.all()
    response = {
        'data': list(data.values('msgs_types','msgs_name','new_msgs'))
    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})

def send_notification_page(request):
    return render(request, 'send_notification.html')

def send_notification(request):
    if request.method == 'POST':
        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {
            'Authorization': 'key=AAAAQoSHBzU:APA91bF8BsHHVYLiTjrFCYKeBLvezTBXg7GTKqS0ur2p8zTtGsbN-FkjUpHrZYUzdETwJ-Rd0uf5Zp8ebC6JWEI_q5TnsI5117skL5RnPFf0qTvJdvnurm1tvPJsjekrV7zyaxFkdeLa',
            'Content-Type': 'application/json'
        }
        payload = {
            'to': '/topics/alert',
            'notification': {
                'title': request.POST.get('title', ''),
                'body': request.POST.get('body', '')
            },
            'data': {
                'data': 'get',
                'pranay': 'pranay',
                'image': 'https://www.webrooper.com/androiddb/uploads/12.jpeg',
                'tag': 'image'
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return HttpResponse(response.text)
    else:
        return HttpResponse('Method Not Allowed')


