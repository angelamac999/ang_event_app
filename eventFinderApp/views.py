from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm, EditEventForm
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = "eventFinderApp/index.html"
    context_object_name = "events_list"
    

    def get_queryset(self):
        """Return the events."""
        return Event.objects.all()



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = EventFilter(self.request.GET, queryset=self.get_queryset())
    #     return context


class AccountView(generic.ListView):
    template_name = "eventFinderApp/account.html"
    context_object_name = "events_list"

    def get_queryset(self):
        """Return the events."""
        return Event.objects.filter(host=self.request.user)


class EventView(generic.DetailView):
    model = Event
    template_name = "eventFinderApp/event.html"


def account(request):
    return render(request, "eventFinderApp/account.html")





def addevent(request):
    if request.method =="POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event_item = form.save(commit=False)
            event_item.save()
    else:
        form = EventForm()
    return render(request, 'EventFinderApp/account.html', {'form': form})


def editevent(request, id=None):
    item = get_object_or_404(Event, id=id)
    form = EditEventForm(request.POST or None, instance=item)
    if form.is_valid():
        event_item = form.save(commit=False)
        event_item.save()
    else:
        form = EditEventForm
    return render(request, 'eventFinderApp/editevent.html', {'form': form})


# class EditEventView(generic.UpdateView):
    
#     model = Event

#     form_class = EventForm

#     success_url = reverse_lazy('eventFinderApp:account')

#     template_name = 'eventFinderApp/edit_event.html'

# def edit_event(request, pk):
#     # post = get_object_or_404(Event, pk=pk)
#     if request.method == "POST":
#         form = EventForm(request.POST, instance=Event)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.author = request.user
#             # event.published_date = timezone.now()
#             event.save()
#             return redirect('EventView', pk=event.pk)
#     else:
#         form = EventForm(instance=event)
#     return render(request, 'eventFinder/edit_event.html', {'form': form})


#here is what i had before djangogirls tutorial:
# # the fucntional view for add event
# def addevent(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = EventForm(request.POST)
        
#         # check whether it's valid:
#         if form.is_valid():
           
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = EventForm()

#     return render(request, 'eventFinderApp/index.html', {'form': form})

# context = {
#         'form': form,
#         'book_instance': book_instance,
#     }

#     return render(request, 'catalog/book_renew_librarian.html', context)





# mine original
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse, reverse_lazy
# from django.views import generic
# from django.shortcuts import render
# from .models import Event
# from .forms import EventForm
# from django.contrib import messages


# class IndexView(generic.ListView):
#     template_name = "eventFinderApp/index.html"
#     context_object_name = "events_list"

#     def get_queryset(self):
#         """Return the events."""
#         return Event.objects.all().order_by('start_time')


# class AccountView(generic.ListView):
#     template_name = "eventFinderApp/account.html"
#     context_object_name = "events_list"

#     def get_queryset(self):
#         """Return the events."""
#         return Event.objects.filter(host=self.request.user).order_by('start_time')


# class EventView(generic.DetailView):
#     model = Event
#     template_name = "eventFinderApp/event.html"


# def account(request):
#     return render(request, "eventFinderApp/account.html")


# # the fucntional view for add event
# def addevent(request):
    
#     form = EventForm(request.POST)
#     # success = False
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
        
#         # check whether it's valid:
#         if form.is_valid():
#             # save the data from the form
#             # new_event = form.save(commit=False)
#             # new_event.host = request.user
#             form.save()
#             messages.success(request, 'details updated.')
#             # success = True
#             # redirect to the event list
#             return render(request, "eventFinderApp/thanks")
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = EventForm()
#     # return the invalid or new form to the template
#     return render(request, 'eventFinderApp/thanks.html', {'form': EventForm})


# # the Class based view for add event
# class AddEventView(generic.View):
#     # in the class basded view we handle the GET request with a get() function
#     def get(self, request):
#         # create our form instance
#         form = EventForm()
#         # assign it to the context
#         context = {"form": eventform}
#         # return our template with our context
#         template = "eventFinderApp/addevent.html"
#         return render(request, template, context)

#     # in the class based view we handle the POST request with a post() function
#     def post(self, request):
#         # we create our form instance with the data from the request
#         form = EventForm(request.POST)
#         # check if the form is valid
#         if form.is_valid():
#             # save the data of the form
#             form.save()
#             messages.success(request, 'details updated.')
#             # redirect to the list of events
#             return render(request, "eventFinderApp/thanks")
#             # return HttpResponseRedirect(reverse("eventFinderApp/thanks"))
#         # if the form isn't valid return the form (with automatic errors)
#         # create the context for our template
#         context = {"form": EventForm}
#         # build the response with our template
#         template = "eventFinderApp/addevent.html"
#         return render(request, template, context)
