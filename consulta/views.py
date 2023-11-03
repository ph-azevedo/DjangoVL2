from django.shortcuts import render
from consulta.models import Livros, Estoque
from django.views.generic.list import ListView

def index(request):
    query = Livros.objects.get(nbook = 'pa1649')

    context = {'query': query

    }

    return render(request, 'index.html', context)

class SearchView(ListView):
    model = Livros
    template_name = 'search.html'
    context_object_name = 'result'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     result = self.queryset
    #     context = {
    #         'stock': self.stock,
    #         'result': result
    #     }
    #     return context
    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')

       if query:
          postresult = Livros.objects.get(isbn1=query)
          #poststock = Estoque.objects.get(nbook=postresult.nbook)
          #self.estoquetotal = int(poststock.disp)
          result = postresult
          stock = self.get_estoque(postresult.nbook)
          result = postresult
          self.stock = stock
          self.result = result
       else:
           result = None
           self.result = result
           self.stock = None
       return (self.result, self.stock)

    def get_estoque(self, nbook):
        poststock = Estoque.objects.filter(nbook=nbook).first()
        self.poststock = poststock.disp + poststock.disp_ff
        return self.poststock