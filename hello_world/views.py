from django.shortcuts import render
from hello_world.models import Grid


# Create your views here.
def hello_world(request):
    some_data = Grid(title='1')
    return render(request, 'hello_world.html', {'the_data':some_data.title})


# return render(request, self.hello_world, {'status': 'alive'})
# return render(request, self.hello_world, {'status': 'dead'})
