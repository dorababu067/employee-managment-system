from django.shortcuts import render
from .models import Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import EmployeeFilter

# Create your views here.


def index(request):
    # filter based on the input date
    queryset = EmployeeFilter(request.GET, queryset=Employee.objects.all()).qs

    # paginating the employee objects
    page_num = request.GET.get("page", 1)
    paginator = Paginator(queryset, 3)  # 3 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context=context)
