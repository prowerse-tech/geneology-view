from django.urls import path
from . import views, utils
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.render_tree_view, name='tree_view'),
    path('get_tree_data/', views.get_tree_data, name='get_tree_data'),
    path('person/<int:person_id>/', views.person_detail, name='person_detail'),
    path('d3-collapsible-tree/', views.d3_collapsible_tree, name='d3_collapsible_tree'),
    path('child/<int:child_id>/', views.child_detail, name='child_detail'),  # URL pattern for child detail
    path('create_person/', views.create_person, name='create_person'),   
    path('import_data_from_csv/', views.import_data_from_csv, name='import_data_from_csv'),  
    path('generate_tree_data/', views.generate_tree_data, name='generate_tree_data'),
]
