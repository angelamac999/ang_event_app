from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from django.conf.urls import url

app_name = 'eventFinderApp'


urlpatterns = [

    # event-finder/

    path('', views.IndexView.as_view(), name='index'),

    # event-finder/1

    path('eventFinder/<int:pk>/', views.EventView.as_view(), name='event'),

    # event-finder/my-account

    path('my-account/', views.AccountView.as_view(), name='account'),

    # event-finder/add-event

    path('eventFinder/addevent/', views.addevent, name='addevent'),
    path('eventFinder/<id>/editevent/', views.editevent, name='editevent'),

    # path(r'^eventFinder/event/(?P<id>\d+)/$', views.editevent, name='editevent'),

    # path('eventFinder/(?P<id>\d+)/', views.editevent, name='edit'),

    # url(r'^eventFinderApp/addevent/$', views.addevent, name='addevent'),



    # event-finder/user

    # path("event/edit/", views.edit_event, name="edit_event"),
    # path('thanks/', views.thankyouView.as_view(), name='thanks'),

    # path('eventFinder/thanks/', TemplateView.as_view(template_name="thanks")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


