from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django import http
from authtools.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy


from .models import Expense
from .forms import ExpenseForm

class ExpenseMixin(object):
    model = Expense

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'expenses'})
        return kwargs


class ExpenseFormMixin(ExpenseMixin):
    form_class = ExpenseForm
    template_name = 'ledger/expense_form.html'


class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'ledger/expense_list.html'
    context_object_name = 'expense_list'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ExpenseList, self).get_context_data(**kwargs)
        context['total_expense'] = self.total_expenses()
        return context

    def total_expenses(self):
        items = Expense.objects.all()
        return sum(item.amount for item in items)



class ExpenseDetail(ExpenseMixin, DetailView):
    pass


class NewExpense(ExpenseMixin,LoginRequiredMixin, CreateView):
    fields = ['amount', 'details']
    success_url = reverse_lazy('expenses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditExpense(ExpenseMixin, UpdateView):
    pass


class DeleteExpense(ExpenseMixin, DeleteView):
    template_name = 'ledger/expense_list.html'
    success_url = reverse_lazy('expenses')

    def post(self,*a, **kw):
        return self.delete(*a, **kw)

# Create your views here.
# def index(request):
#     items = Expense.objects.order_by('-created_on')
#     template = loader.get_template('ledger/index.html')
#     context = RequestContext(request, {
#         'items': items,
#     })
#     return HttpResponse(template.render(context))
#
# def expenses(request):
#     items = Expense.objects.order_by('-created_on')
#     total = sum(item.amount for item in items)
#     template = loader.get_template('ledger/expense_list.html')
#     context = RequestContext(request, {
#         'items': items,
#         'total_expense':total,
#     })
#     return HttpResponse(template.render(context))
#
#
# # @user_passes_test(lambda u: u.is_superuser)
# def add_expense(request):
#     form = ExpenseForm(request.POST or None)
#     if form.is_valid():
#         expense = form.save(commit=True)
#         # expense.user = request.user.id
#         # expense.save()
#         return redirect('expenses')
#     return render_to_response('ledger/expense_form.html',
#                               { 'form': form },
#                               context_instance=RequestContext(request))
#
# def detail(request, item_id):
#     return HttpResponse("you are looking at item %s." % item_id)
#
#     # def login(request):
#     # return redirect_field_name("fjs")