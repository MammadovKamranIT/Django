from django.urls import path


from . import views


app_name = 'notes'

urlpatterns = [

path('', views.notes_view_list, name='notes_list'),
path('<int:note_id>/', views.notes_detail, name = 'notes_detail'),
path('create/', views.notes_create, name='notes_create' ),
path('update/<int:note_id>/', views.notes_update, name='notes_update'),
path('delete/<int:note_id>/', views.notes_delete, name='notes_delete'),
path('feedback/', views.contact, name='notes_feedback'),


]



# app_name = 'accounts'
# urlpatterns = [

# path('login/', login_view, name = 'login'),

# path('logout/', logout_view, name = 'logout'),

# path('login/', login_view, name = 'register'),

# path('login/', login_view, name = 'login'),

# path('login/', login_view, name = 'login'),


# ]