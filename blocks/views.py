from .models import Block
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class BlockListView(ListView):
    model = Block


class BlockDetailView(DetailView):
    model = Block
