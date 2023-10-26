from rest_framework import serializers
from .models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ['field1', 'fileld1]
        # fields = ['field1', 'fileld1]



# class PostSerializer(serializers.Serializer):
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     title = serializers.CharField(max_length=240)
#     body = serializers.CharField(allow_blank=True, allow_null=True)
#     created_at = serializers.DateTimeField(read_only=True)

#     # def create(self, validated_data):
#     #     print(validated_data)
#     #     return Post.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         print(instance, 'instance')
#         print(validated_data)
#         instance.category = validated_data.get('category', instance.category)
#         instance.title = validated_data.get('title', instance.title)
#         instance.body = validated_data.get('body', instance.body)
#         instance.save()
#         return instance


