from django.http import HttpResponse
from django.template import loader
from .models import CutleryFactory  # Import the model

def main(request):
    template = loader.get_template('main.html')  # Main homepage template
    return HttpResponse(template.render(None, request))

def factories_list(request):
    factories = CutleryFactory.objects.all().values()  # Fetch all factories
    template = loader.get_template('allfactories.html')
    context = {'factories': factories}
    return HttpResponse(template.render(context, request))

def all_detail(request, id):
    factory = CutleryFactory.objects.get(id=id)  # Fetch factory by ID
    template = loader.get_template('alldetail.html')
    context = {'factory': factory}
    return HttpResponse(template.render(context, request))
