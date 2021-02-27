from django.db import transaction
from django.shortcuts import render
from rest_framework.views import APIView
import pandas as pd
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.response import Response
from goods.models import Goods
from rest_framework import status
from goods.serializers import GoodsModelSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet


# Create your views here.


class GoodsGenericAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin,
                          DestroyModelMixin):
    # queryset = Book.objects.all()

    # 获取查询集
    def get_queryset(self):
        return Goods.objects.all()

    # 设置序列化器
    serializer_class = GoodsModelSerializer

    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ExcelViewSet(ViewSet):
    def parse_excel(self, request, *args, **kwargs):
        _ = self
        print(request.data, request.FILES.get('file'))
        file = request.FILES.get('file')
        if file is None:
            return Response({
                'message': '文件未找到'
            }, status=status.HTTP_404_NOT_FOUND)
        file_name = default_storage.save('即时库存表.xlsx', ContentFile(file.read()))

        df = pd.read_excel('media/' + file_name)
        data = df.values
        for row in data:
            serializer = GoodsModelSerializer(data={
                'code': row[0],
                'title': row[1],
                'price': row[7],
                'counter': 0
            })
            serializer.is_valid()  # 验证字段的完整性
            serializer.save()
        return Response({
            'message': '解析成功'
        }, status=status.HTTP_200_OK)
