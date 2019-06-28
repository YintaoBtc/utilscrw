from .models import Project
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator



class StaffRequired(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequired, self).dispatch(request, *args, **kwargs)



# Create your views here.
class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


@method_decorator(staff_member_required, name='dispatch')
class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'content', 'addr_shop', 'categories', 'amount_goal']
    success_url = reverse_lazy("projects:projects")


@method_decorator(staff_member_required, name='dispatch')
class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'content', 'addr_shop', 'categories', 'amount_goal']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('projects:update', args=[self.object.id]) + "?ok"


@method_decorator(staff_member_required, name='dispatch')
class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy("projects:projects")