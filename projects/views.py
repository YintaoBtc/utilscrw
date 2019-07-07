from .models import Project
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from wallet.commands.instruct_wallet import instruct_wallet



class StaffRequired(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequired, self).dispatch(request, *args, **kwargs)



# Create your views here.
class ProjectListView(ListView):
    model = Project
        

class ProjectDetailView(DetailView):
    model = Project

    queryset = Project.objects.all()

    def get_object(self):
        project = super().get_object()

        if project.addr_donate == None:
            address_new = instruct_wallet("getnewaddress", [str(project.title)])["result"]
            project.addr_donate = address_new
            project.save()
            print("This is title: {} and this is address: {} ".format(project.title, address_new))   

        balance = instruct_wallet("getbalance", [str(project.title)])["result"]
        needed = project.amount_goal - balance
        progress = int(balance / project.amount_goal * 100)

        if balance >= project.amount_goal:
            #Set True on completed and save
            project.completed = True
            project.save()

            send_tx = instruct_wallet("sendfrom", [str(project.title), str(project.addr_shop), 1]) #Cambiar ammount
            print(send_tx)
            return project

        else:
            # Record the last accessed date
            progress_finish = str(progress) + "%"
            project.amount_needed = needed
            project.amount_donate = balance
            project.progress = progress_finish
            project.save()
            return project


        


@method_decorator(staff_member_required, name='dispatch')
class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'content', 'addr_shop', 'image', 'categories', 'amount_goal']
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