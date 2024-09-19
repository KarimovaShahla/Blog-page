from django.urls import path
from . import views


urlpatterns = [
    path(
        "", 
        views.index, 
        name="index"
    ),
    path(
        "post/<int:post_id>",
        views.post_detail_view,
        name="post-detail"
    ),
    path("custom-view/", 
        views.my_custom_view, 
        name="my_custom_view"
    ),
]


