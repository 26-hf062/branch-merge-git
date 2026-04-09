from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)


urlpatterns = [
    # path("", views.home, name="home"),
    # path("hello/<name>", views.hello_there, name="hello_there"),
    # path("", views.home, name="home"),          # 홈 페이지
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),  # About 페이지
    path("contact/", views.contact, name="contact"),  # Contact 페이지
    path("log/", views.log_message, name="log"),      # Log Message 페이지
]