from django.urls import path 
from . import views 
from . views import JournalList 

urlpatterns = [
    path('create',views.create_journal, name="create_journal"),
    path('listjournals', views.listjournals, name="listjournals"),
    path('search', views.search, name="search"),
    path('listall',JournalList.as_view(), name="listall"),
    path('delete/<int:id>/',views.delete, name="delete"),
    path('update/<int:id>/',views.update, name="update"),
    path('journal_detail/<int:id>',views.journal_detail, name="journal_detail"),
]
