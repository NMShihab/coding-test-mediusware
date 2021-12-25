from django.views import generic
from django.views.generic.list import ListView

from product.models import Variant, ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductListView(ListView):
    template_name = "products/list.html"
    model = ProductVariantPrice
    paginate_by	= 2
    
    