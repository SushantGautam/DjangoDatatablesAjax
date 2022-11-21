from django.contrib.auth.models import User
from django.views.generic import ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
from faker import Faker

from WebApp.models import TestModel

# Create your views here.

fake = Faker()
Faker.seed(0)

FilteredList = {}
for i in range(100):
    id = fake.random_int(min=1, max=100)
    FilteredList[id] = {
        "id": id,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "company": fake.company(),
        # "job": fake.job(),
        # "date": fake.date(),
        # "time": fake.time(),
    }


class HomeView(ListView):
    template_name = "home.html"
    model = User
    context_object_name = "users"


class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = TestModel

    # define the columns that will be returned
    columns = ['id', 'name', 'email', 'address', 'address', 'company']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non-sortable columns use empty
    # value like ''
    # order_columns = ['number', 'user', 'state', '', '']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    # max_display_length = 500

    # def render_column(self, row, column):
    #     # We want to render user as a custom column
    #     if column == 'user':
    #         # escape HTML for security reasons
    #         return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
    #     else:
    #         return super(OrderListJson, self).render_column(row, column)
    #
    # def filter_queryset(self, qs):
    #     # use parameters passed in GET request to filter queryset
    #
    #     # simple example:
    #     search = self.request.GET.get('search[value]', None)
    #     if search:
    #         qs = qs.filter(name__istartswith=search)
    #
    #     # more advanced example using extra parameters
    #     filter_customer = self.request.GET.get('customer', None)
    #
    #     if filter_customer:
    #         customer_parts = filter_customer.split(' ')
    #         qs_params = None
    #         for part in customer_parts:
    #             q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
    #             qs_params = qs_params | q if qs_params else q
    #         qs = qs.filter(qs_params)
    #     return qs
