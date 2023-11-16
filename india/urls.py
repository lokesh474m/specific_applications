from india.views import *
from django.urls import path
app_name='sachin'

urlpatterns = [

path('kohli/',kohli,name='kohli'),
path('shami/',shami,name='shami'),

]


