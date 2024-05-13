from django.urls import path

from network.apps import NetworkConfig
from network.views import ObjectCreateAPIView, ObjectListAPIView, ObjectUpdateAPIView, ObjectRetrieveAPIView, ObjectDestroyAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('objects/create/', ObjectCreateAPIView.as_view(), name='unit-create'),
    path('objects/', ObjectListAPIView.as_view(), name='unit-list'),
    path('objects/<int:pk>/', ObjectRetrieveAPIView.as_view(), name='unit-get'),
    path('objects/update/<int:pk>/', ObjectUpdateAPIView.as_view(), name='unit-update'),
    path('objects/delete/<int:pk>/', ObjectDestroyAPIView.as_view(), name='unit-delete')
]