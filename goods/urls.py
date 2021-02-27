from django.urls import re_path
from goods import views

urlpatterns = [
    re_path(r'^goods/(?P<pk>\d*)', views.GoodsGenericAPIView.as_view()),
    re_path(r'^parse_excel/', views.ExcelViewSet.as_view({'post': 'parse_excel'})),
]
