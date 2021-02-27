from rest_framework import serializers
from goods.models import Goods


class GoodsListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        for index, goods in enumerate(instance):
            self.child.update(goods, validated_data[index])
        return instance


class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        # fields = ('code', 'title', 'alias', 'price', 'units', 'counter', 'sale_counter')
        fields = ('code', 'title', 'price', 'counter')

        extra_kwargs = {
            'title': {
                'max_length': 20,
                'min_length': 2,
            },
            # 'alias': {
            #     'read_only': True  # 只参与序列化
            # },
            # 'sale_counter': {
            #     'read_only': True  # 只参与序列化
            # }
        }

        list_serializer_class = GoodsListSerializer
