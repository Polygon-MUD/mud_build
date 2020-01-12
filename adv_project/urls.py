from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),
]
