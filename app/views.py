import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .import metrics


@login_required(login_url="login")
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    grafic_product_category_metrics = metrics.get_grafic_product_category_metrics()
    grafic_product_brand_metric = metrics.get_grafic_product_brand_metric()

    context = {
        "product_metrics": product_metrics,
        "sales_metrics": sales_metrics,
        "daily_sales_data": json.dumps(daily_sales_data),
        "daily_sales_quantity_data": json.dumps(daily_sales_quantity_data),
        "product_count_by_category": json.dumps(grafic_product_category_metrics),
        "product_count_by_brand": json.dumps(grafic_product_brand_metric),
    }
    return render(request, "home.html", context)
