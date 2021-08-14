from django.urls import path
from . import views
urlpatterns = [
path('', views.welcome),
path('existing', views.greeting),
path('signup', views.sign_up),
path('success', views.success),
path('signup2', views.sign_up_with_model_form),
path('list_one', views.list_one),
path('list_all', views.list_all),
path('list_n/<int:n>', views.list_n,),
path('clickable_list', views.clickable_list),
path('list_particular/<int:id>', views.list_particular, name='showbyid'),
path('get_by_id_from_browser_form', views.get_by_id_from_browser_form),
path('filter_name_contains', views.filter_name_contains)
]
