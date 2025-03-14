from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import View

from .forms import OrganizationForm, FileForm
from .models import Contract
from .models import ContractType, Organization


# Главная страница
def home(request):
    return render(request, 'home.html', {'title': 'Главная'})

# Views для ContractType
class ContractTypeListView(ListView):
    model = ContractType
    template_name = 'contract-type/contract-type-list.html'
    context_object_name = 'contract_types'

class ContractTypeDetailView(DetailView):
    model = ContractType
    template_name = 'contract-type/contract-type-detail.html'
    context_object_name = 'contract_type'

class ContractTypeCreateView(CreateView):
    model = ContractType
    template_name = 'contract-type/contract-type-create.html'
    fields = ['name', 'description', 'is_active']
    success_url = reverse_lazy('contract-type-list')

class ContractTypeUpdateView(UpdateView):
    model = ContractType
    template_name = 'contract-type/contract-type-update.html'
    fields = ['name', 'description', 'is_active']
    success_url = reverse_lazy('contract-type-list')

class ContractTypeDeleteView(DeleteView):
    model = ContractType
    template_name = 'contract-type/contract-type-delete.html'
    success_url = reverse_lazy('contract-type-list')

class ContractTypeView(View):
    def get(self, request):
        try:
            # Получаем уникальные типы договоров
            types = Contract.objects.values('contract_type').distinct()

            # Проверяем, есть ли хотя бы один тип
            if not types.exists():
                return JsonResponse({'error': 'Типы договоров не найдены'}, status=404)

            # Форматируем ответ в более удобном виде
            formatted_types = [
                {'id': i, 'type': type['contract_type']}
                for i, type in enumerate(types, start=1)
            ]

            return JsonResponse({'types': formatted_types}, safe=False)

        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Типы договоров не найдены'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


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
    template_name = 'contract/contract-list.html'
    context_object_name = 'contracts'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contract/contract-detail.html'
    context_object_name = 'contract'

class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contract/contract-create.html'
    fields = '__all__'  # или перечислить конкретные поля
    success_url = reverse_lazy('contract-list')

class ContractUpdateView(UpdateView):
    model = Contract
    template_name = 'contract/contract-update.html'
    fields = '__all__'  # или перечислить конкретные поля
    success_url = reverse_lazy('contract-list')

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contract/contract-delete.html'
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