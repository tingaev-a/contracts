from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ContractType, Organization, Position, Contract, File
from .forms import ContractForm, OrganizationForm, PositionForm, FileForm, ContractTypeForm

# Главная страница
def home(request):
    return render(request, 'home.html', {'title': 'Главная'})

# Views для ContractType
class ContractTypeListView(ListView):
    model = ContractType
    template_name = 'contracttype/contracttype-list.html'
    context_object_name = 'contracttypes'

class ContractTypeDetailView(DetailView):
    model = ContractType
    template_name = 'contracttype/contracttype-detail.html'

class ContractTypeCreateView(CreateView):
    model = ContractType
    form_class = ContractTypeForm
    template_name = 'contracttype/contracttype-form.html'
    success_url = reverse_lazy('contracttype-list')

class ContractTypeUpdateView(UpdateView):
    model = ContractType
    form_class = ContractTypeForm
    template_name = 'contracttype/contracttype-form.html'
    success_url = reverse_lazy('contracttype-list')

class ContractTypeDeleteView(DeleteView):
    model = ContractType
    template_name = 'contracttype/contracttype-confirm_delete.html'
    success_url = reverse_lazy('contracttype-list')

# Views для Organization
class OrganizationListView(ListView):
    model = Organization
    template_name = 'organization/organization-list.html'
    context_object_name = 'organizations'

class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'organization/organization-detail.html'

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/organization-create.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/organization-update.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'organization/organization-delete.html'
    success_url = reverse_lazy('organization-list')

# Views для Contract
class ContractListView(ListView):
    model = Contract
    template_name = 'main/templates/contract_list.html'
    context_object_name = 'contracts'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'main/templates/contract_detail.html'

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'main/templates/contract_form.html'
    success_url = reverse_lazy('contract-list')

class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'main/templates/contract_form.html'
    success_url = reverse_lazy('contract-list')

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'main/templates/contract_confirm_delete.html'
    success_url = reverse_lazy('contract-list')

# Аналогичные views для Position, Contract и File

# Пример функции для загрузки файла
def upload_file(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.contract = contract
            file.save()
            return redirect('contract-detail', pk=contract_id)
    else:
        form = FileForm()
    return render(request, 'main/file_form.html', {'form': form})

def contract_view(request):
    return render(request, 'contracttype/contracttype-list.html')

def organization_view(request):
    return render(request, 'organization/organization-list.html')