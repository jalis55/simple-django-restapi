
from django.urls import path
from status.views import StatusView,StatusListView,CreateStatusView,StatusDetailView,StatusDeleteView,StatusUpdateView


urlpatterns = [
    path('status/<int:id>/', StatusView.as_view(),name='status_view'),
    path('statuses/', StatusListView.as_view(),name='status_list_view'),
    path('status/create/',CreateStatusView.as_view(),name='create_status_view'),
    path('status/<pk>',StatusDetailView.as_view(),name='status_details_view'),
    path('status/update/<pk>',StatusUpdateView.as_view(),name='status_details_view'),
    path('status/delete/<pk>',StatusDeleteView.as_view(),name='status_details_view'),
]