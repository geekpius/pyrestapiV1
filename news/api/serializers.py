from rest_framework import serializers
from news.models import Article
from datetime import datetime
from django.utils.timesince import timesince


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication  = serializers.SerializerMethodField()
    
    class Meta: 
        model = Article
        # fields = "__all__" # we want all fields of Article model
        # fields = ("title", "description", "body") # we want these specified fields of Article model
        exclude = ("id",) # we dont want to show these specified fields of Article model


    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        delta_time = timesince(publication_date, now)
        return delta_time


    """ Object level validations """
    """ check if title and description are different  """
    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description should be different")
        return data


    """ Field level validations """
    """ check if title less than 30 characters  """
    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("Title must be 30 and above characters")
        return value





# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)


#     # Methods
#     def create(self, validated_data):
#         print (validated_data)
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get("author", instance.author)
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.body = validated_data.get("body", instance.body)
#         instance.location = validated_data.get("location", instance.location)
#         instance.publication_date = validated_data.get("publication_date", instance.publication_date)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance


#     """ Object level validations """
#     """ check if title and description are different  """
#     def validate(self, data):
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and description should be different")
#         return data


#     """ Field level validations """
#     """ check if title less than 30 characters  """
#     def validate_title(self, value):
#         if len(value) < 30:
#             raise serializers.ValidationError("Title must be 30 and above characters")
#         return value