from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'almoxarifado'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.almoxarifado, name='almoxarifado'),
    path('cadastro_item/', views.item_create, name='cadastro_item'),
    path('update_item/<int:item_id>/', views.item_update, name='update_item'),
    path('delete_item/<int:item_id>/', views.item_delete, name='delete_item'),
    path('aloca_item/<int:item_id>/', views.aloca_item, name='aloca_item'),
    path('retira_item/<int:item_id>/', views.retira_item, name='retira_item'),
    path('historico/', views.historico_view, name='historico'),
]