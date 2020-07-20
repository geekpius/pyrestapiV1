# pyrestapiV1
Python API for news. My objective was to understand the JSON parsers and renders and how serializers works

# On The Shell

+ from news.models import Article
+ from news.api.serializers import ArticleSerializer
+ article_instance = Article.objects.first()
+ article_instance
<Article: John Doe Happy Birthday ISS: 20 Years of the International Space Station>
+ serializer = ArticleSerializer(article_instance)
+ serializer
ArticleSerializer(<Article: John Doe Happy Birthday ISS: 20 Years of the International Space Station>):
    id = IntegerField(read_only=True)
    author = CharField()
    title = CharField()
    description = CharField()
    body = CharField()
    location = CharField()
    publication_date = DateField()
    active = BooleanField()
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
+ serializer.data
{'id': 1, 'author': 'John Doe', 'title': 'Happy Birthday ISS: 20 Years of the International Space Station', 'description': 'Some fancy description', 'body': 'Some content', 'location': 'Earth', 'publication_date': '2020-07-20', 'active': True, 'created_at': '2020-07-20T09:08:12.371447Z', 'updated_at': '2020-07-20T09:08:12.371486Z'}
+ from rest_framework.renderers import JSONRenderer
+ json = JSONRenderer().render(serializer.data)
+ json
b'{"id":1,"author":"John Doe","title":"Happy Birthday ISS: 20 Years of the International Space Station","description":"Some fancy description","body":"Some content","location":"Earth","publication_date":"2020-07-20","active":true,"created_at":"2020-07-20T09:08:12.371447Z","updated_at":"2020-07-20T09:08:12.371486Z"}'
+ import io
+ from rest_framework.parsers import JSONParser
+ stream = io.BytesIO(json)
+ data = JSONParser().parse(stream)
+ data
{'id': 1, 'author': 'John Doe', 'title': 'Happy Birthday ISS: 20 Years of the International Space Station', 'description': 'Some fancy description', 'body': 'Some content', 'location': 'Earth', 'publication_date': '2020-07-20', 'active': True, 'created_at': '2020-07-20T09:08:12.371447Z', 'updated_at': '2020-07-20T09:08:12.371486Z'}
+ serializer = ArticleSerializer(data=data)
+ serializer.is_valid()
True
+ serializer.validated_data
OrderedDict([('author', 'John Doe'), ('title', 'Happy Birthday ISS: 20 Years of the International Space Station'), ('description', 'Some fancy description'), ('body', 'Some content'), ('location', 'Earth'), ('publication_date', datetime.date(2020, 7, 20)), ('active', True)])
+ serializer.save()
{'author': 'John Doe', 'title': 'Happy Birthday ISS: 20 Years of the International Space Station', 'description': 'Some fancy description', 'body': 'Some content', 'location': 'Earth', 'publication_date': datetime.date(2020, 7, 20), 'active': True}
<Article: John Doe Happy Birthday ISS: 20 Years of the International Space Station>
+ Article .objects.all()
<QuerySet [<Article: John Doe Happy Birthday ISS: 20 Years of the International Space Station>, <Article: John Doe Happy Birthday ISS: 20 Years of the International Space Station>]>
