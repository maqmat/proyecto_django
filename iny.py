from django_app import Post

Post.objects.filter(title__icontains='iPhone').values('id', 'title', 'category')