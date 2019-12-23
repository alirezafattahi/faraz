from django.urls import path
from . import views



app_name= 'service'
urlpatterns = [
    path ('',views.index , name = 'index'),
    path ('pro/new/',views.pro , name = 'pro'),
    path('contracts' , views.contract_list , name = 'contract_list'),
    path('contracts/details/<int:id>' , views.contract_details , name ='contract_details'),
    path('msg/<str:s>/<str:r>' , views.msg_send , name ='msg'),
    path('persons' , views.person_list , name='person_list' ),
    path('person/<int:id>' , views.profile , name='profile_name' ),
    path('msg/box/<str:reciver>/<str:sender>' , views.msg_box , name='msg_box'),
]