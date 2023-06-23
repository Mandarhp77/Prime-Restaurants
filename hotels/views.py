from django.shortcuts import render, redirect
from .models import Hotels

# Create your views here.
def home(request):
    return render(request, 'hotels.html')

final_result = None
def get_data(request):
    hotels = Hotels.objects.all()
    global final_result
    if request.method=='POST':
        name = request.POST['dname']

        #For future purpose
        #location = request.POST['location']
        #cuisine = int(request.POST['cuisine'])

        items = []
        id = []
        result_ids = []
        price = []
        cuisines = []
        details = []
        address = []
    

        # for loop to seperate table columns
        for i in hotels:
            items.append(i.items)
            details.append(i.full_details)
            id.append(i.id)
        #-----------------------------------------------------------

        # for loop to fetch name of dish and its price
        for unique_id, item, detail in zip(id, items, details):
            dic = eval(item)

            for key, value in dic.items():
                #print(key)
                if(name == key):
                    res = Hotels.objects.get(id = unique_id)
                    result_ids.append(unique_id)
                    price.append(value)
                    
                    details = res.full_details
                    if details is not None:
                        if "cuisines" in details:
                            cuisine_index = res.full_details.index("cuisines")+12
                            currency_index = res.full_details.index("currency")-4
                            cuisines.append(details[cuisine_index:currency_index])

                        if "address" in details:
                            city_index = res.full_details.index("city")+8
                            city_id_index = res.full_details.index("city_id")-4
                            post_address_index = res.full_details.index("address")+11
                            pre_address_index = res.full_details.index("address")-4
                            address.append(details[post_address_index:city_id_index])

        #----------------------------------------------------------

        # for loop to fetch the details of restaurants
        final_result = []
        context ={}
        for id, rate, cuisine, add_rss in zip(result_ids, price, cuisines, address):
            row = Hotels.objects.get(id = id)
            context = {'name':row, 
                    'rate': rate, 
                    'cuisine': cuisine,
                    'address': add_rss}
            final_result.append(context)

       # print(final_result)

        #------------------------------------------------------------     
        return redirect("get_data")

    if final_result is None:
        return render(request, 'hotels.html')
    elif final_result is not None:
        return render(request, 'hotels.html', {"result":final_result})




