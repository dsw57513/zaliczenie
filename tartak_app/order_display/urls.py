from django.urls import path
from . import views

app_name = 'order_display'
urlpatterns = [
    path('', views.OrderListView.as_view(), name = "order_list"),
    path('szczegoly/<slug:order>/', views.order_detail_view, name = 'order_detail'),
    path('klient/<slug:client>/', views.client_detail_view, name = 'client_detail'),
    path('edit/<slug:element>', views.element_edit_view, name = 'element_edit'),
    path('nowe/', views.new_order, name = 'new_order'),
    path('show_searches/', views.show_searches, name='show_searches'),
    path('finnish_element/<slug:element>', views.finnish_element, name='finnish_element'),
    path('finnish_order/<slug:order>', views.finnish_order, name='finnish_order'),
    path('archiwum/', views.Archive.as_view(), name ="archiwum"),
    path('brudnopis/', views.Draft.as_view(), name ="brudnopis"),
]