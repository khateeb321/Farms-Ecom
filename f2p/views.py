from django.shortcuts import render
from .models import City, Area,Veges,nutrientsVeges,registeredUser,orderDetails,Fruits,nutrientsFruits,fruitOrder,vegeOrder,farmDesciption,vegeFarm,fruitFarm
import datetime
import smtplib
from django.db.models import Q
from django.template import RequestContext
MY_ADDRESS = 'f2p.preston@gmail.com'
PASSWORD = 'abc123!@#'

v=''
t=''
o=''
n=''
rc=''
def fruits(request):
    fruit=Fruits.objects.all()
    nutrients=nutrientsFruits.objects.all()
    vf=vegeFarm.objects.all()
    ff=fruitFarm.objects.all()

    rc = RequestContext(request, {'veges': fruit, 'nutrients': nutrients,'ff':ff,'vf':vf})
    return render(request, 'f2p/fruits.html', {'rc': rc})

def main(request):
    msg=""
    if 'btnStatus' in request.POST:
        Date=request.POST.get('date')
        cn=request.POST.get('cn')
        try:
            order=orderDetails.objects.filter(user__contactNum=cn,status='on',odate=Date)
            if order.count() == 0:
                msg = "There is no order against contact number and date"
            else:
                for t in order:
                    t.status="off"
                    t.save()
                msg = "Thanks for the review!"
        except:
            msg="There is no order against contact number and date"

    veges=Veges.objects.all()
    nutrientes=nutrientsVeges.objects.all()
    nutrf=nutrientsFruits.objects.all()
    fruit=Fruits.objects.all()
    rc = RequestContext(request, {'veges': veges, 'nutrients': nutrientes,'nutrf':nutrf,'fruits':fruit,'msg':msg})
    # return render(request, 'f2p/fruits.html', {'rc': rc})

    return render(request, 'f2p/mainpage.html', {})
def index(request):
    request.session['v']=""
    request.session['o'] = ""
    request.session['rc'] = ""
    request.session['userContct'] = ""

    if request.method == 'POST':
        print (request.POST.get('ddlCity'))
        city=request.POST.get('ddlCity')
        area=Area.objects.filter(city_label__label=city)
        return render(request, 'f2p/index.html', {'area': area})
    else:
        city=City.objects.all()
        return render(request, 'f2p/index.html', {'city':city})

        # create a forms instance and populate it with data from the request:
    #     form = SearchForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         print("this")
    #         city=form.cleaned_data['city'].choices
    #         print(city)
    #         form.area=Area.objects.filter(city_label__label=city)
    #
    #
    #         # if a GET (or any other method) we'll create a blank form
    #
    # #    form = SearchForm()

#        return render(request, 'f2p/index.html', {'form': form})

def indexCity(request):
    city = request.POST.get('ddlCity')

    area = Area.objects.filter(city_label__label=city)
    return render(request, 'f2p/index.html', {'area': area})

def sendEmail(request,msg):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    s.sendmail(MY_ADDRESS,request.session['email'],msg)
    s.quit()

def indexArea(request):
    veges=Veges.objects.all()
    nutrients=nutrientsVeges.objects.all()
    vf = vegeFarm.objects.all()
    rc=RequestContext(request, {'veges':veges, 'nutrients':nutrients,'vf':vf})
    return render(request, 'f2p/index.html', {'rc': rc})

def btn(request):

    if 'btn1' in request.POST:
        v=Veges.objects.get(pk=1)

    if 'btn2' in request.POST:
        v=Veges.objects.get(pk=2)

    if 'btn3' in request.POST:
        v=Veges.objects.get(pk=3)

    if 'btn4' in request.POST:
        v=Veges.objects.get(pk=4)

    if 'btn5' in request.POST:
        v=Veges.objects.get(pk=5)

    if 'btn6' in request.POST:
        v=Veges.objects.get(pk=6)

    if 'btn7' in request.POST:
        v=Veges.objects.get(pk=7)

    if 'btn8' in request.POST:
        v=Veges.objects.get(pk=8)

    if 'btn9' in request.POST:
        v=Veges.objects.get(pk=9)

    if 'btn10' in request.POST:
        v=Veges.objects.get(pk=10)
    if 'btnf1' in request.POST:
        f=Fruits.objects.get(pk=1)


    if 'btnf2' in request.POST:
        f = Fruits.objects.get(pk=2)

    if 'btnf3' in request.POST:
        f = Fruits.objects.get(pk=3)

    if 'btnf4' in request.POST:
        f = Fruits.objects.get(pk=4)

    if 'btnf5' in request.POST:
        f = Fruits.objects.get(pk=5)

    if 'btnf6' in request.POST:
        f = Fruits.objects.get(pk=6)

    if 'btnf7' in request.POST:
        f = Fruits.objects.get(pk=7)

    if 'btnf8' in request.POST:
        f = Fruits.objects.get(pk=8)

    if 'btnf9' in request.POST:
        f = Fruits.objects.get(pk=9)

    if 'btnf10' in request.POST:
        f=Fruits.objects.get(pk=10)
    o=1
    request.session['o'] = o
    try:
        n = nutrientsVeges.objects.get(vege__label=v.label)
        request.session['v'] = v.label
        ff = vegeFarm.objects.all()
        rc = RequestContext(request, {'v': v, 'n': n, 'o': o,'ff':ff})
    except:
        n = nutrientsFruits.objects.get(fruit__label=f.label)
        request.session['v'] = f.label
        ff = fruitFarm.objects.all()
        rc = RequestContext(request, {'v': f, 'n': n, 'o': o,'ff':ff})


    # request.session['ncarbohydrates'] = n.carbohydrates
    # request.session['ncalcium'] = n.calcium
    # request.session['nproteins'] = n.proteins
    # request.session['niron'] = n.iron
    # request.session['nenergy'] = n.energy
    # request.session['npotassium'] = n.potassium
    # request.session['nsugar'] = n.sugar
    # request.session['nfats'] = n.fats



    return render(request, 'f2p/addtocart.html', {'rc': rc})
    # return render(request, 'f2p/addtocart.html', {'v': v})
def btnConfirmOrder(request):

    # bdy = requests.get('http://127.0.0.1:8000/f2p/btn/')
    # bdy=request.body.decode('utf-8')
    #
    # body=json.loads(bdy)
    # body = json.loads(body_unicode)
    # o = request.POST.get('qty')
    # t = request.POST.get('vege')
    # o = body['qty']
    # o=request.GET.get('qty')
    # t=request.GET.get('vege')
    t = request.session['v']
    o = request.session['o']
    try:
        v = Veges.objects.get(label=t)
        n = nutrientsVeges.objects.get(vege__label=v.label)
    except:
        v = Fruits.objects.get(label=t)
        n = nutrientsFruits.objects.get(fruit__label=v.label)
    if 'btnContct' in request.POST:

        cont=request.POST.get('txtContct')
        request.session['userContct']=cont
        user=registeredUser.objects.get(contactNum=cont)
        rc = RequestContext(request, {'v': v, 'n': n, 'o': o, 'user': user})
        return render(request, 'f2p/addtocart.html', {'rc': rc})
        # return render(request, 'f2p/addtocart.html', {'user': user})
    if 'btnCName' in request.POST:
        try:
            f=registeredUser.objects.get(contactNum=request.POST.get('txtCNumt'))
        except:
            f=registeredUser()
            f.userName=request.POST.get('txtNamet')
            f.contactNum=request.POST.get('txtCNumt')
            f.address=request.POST.get('txtAddrt')
            city=request.POST.get('radioCity')
            a=Area.objects.filter(city_label__label=city)
            f.area=a[0]
            f.save()
        user=f
        request.session['userContct']=user.contactNum
        rc = RequestContext(request, {'v': v, 'n': n, 'o': o, 'user': user})
        return render(request, 'f2p/addtocart.html', {'rc': rc})
    if 'btnCheckout' in request.POST:
        now = datetime.datetime.now()
        h=''
        o1 = orderDetails.objects.filter(user__contactNum=request.session['userContct'], status='on', odate=now.strftime("%Y-%m-%d"))
        user = registeredUser.objects.get(contactNum=request.session['userContct'])
        if o1.count()>0:
            # ow=datetime.date

            total=o1.count()
            o = orderDetails()
            o.user = registeredUser.objects.get(contactNum=user.contactNum)
            o.odate = now.strftime("%Y-%m-%d")
            o.status="on"
            try:
                v = Veges.objects.get(label=request.session['v'])
                aq=vegeOrder()
                aq.vege=v
                h='v'

            except:
                v = Fruits.objects.get(label=request.session['v'])
                aq=fruitOrder()
                aq.fruit = v
                h='f'
            try:
                o.orderID = orderDetails.objects.all().count() + 1
            except:
                o.orderID = 1

            c=request.POST.get('a')
            o.cost=float(c)*v.price

            o.save()
            aq.orderID=o
            aq.save()

            msg = "Reciept\n\nDear " + user.userName + "!\n\nYou have purchased the following item. Given below is the item and its cost" \
                                              "\n\n"
            cst=0

            for s in o1:


                try:
                    filter=fruitOrder.objects.get(orderID__orderID=s.orderID)
                    msg="%s%s%s%s" %(msg,"\nProduct: \t",filter.fruit.label,"\n" \
                    "Total Cost: Rs " + str(s.cost))
                    cst += s.cost
                except:
                    try:
                        filter = vegeOrder.objects.get(orderID__orderID=s.orderID)
                        msg = "%s%s%s" % (msg,"\nProduct: \t", filter.vege.label + "\n" \
                          "Total Cost: Rs " + str(s.cost))
                        cst += s.cost
                    except:
                        i=0

            msg="%s%s%s%s" % (msg,"\nProduct: \t",v.label,"\n" \
                    "Total Cost: Rs " + str(o.cost))

            msg = "%s%s%s%s" % (msg, "\n\nRegards Admin F2P", "\n\nTotal Bill is  Rs.", cst)
        else:
            o=orderDetails()
            o.user=registeredUser.objects.get(contactNum=user.contactNum)
            # date="%Y%s%m%s%d" % (datetime.date.year,"-",datetime.date.month,"-",datetime.date.day)


            o.odate=now.strftime("%Y-%m-%d")
            o.status="on"

            try:
                v = Veges.objects.get(label=request.session['v'])
            except:
                v = Fruits.objects.get(label=request.session['v'])
            c=request.POST.get('a')
            o.cost=float(c)*v.price
            try:
                o.orderID=orderDetails.objects.all().count()+1
            except:
                o.orderID=1
            o.save()
            total=1
            cst=o.cost
            msg=""
            msg = "Reciept\n\nDear " + user.userName + "!\n\nYou have purchased the following item. Given below is the item and its cost" \
                                                       "\n\n"
            msg = "%s%s%s%s" % (msg,"\nProduct: \t", v.label, "\n" \
                                                     "Total Cost: Rs " + str(o.cost))

            msg = "%s%s%s%s" % (msg,"\n\nRegards Admin F2P","\n\nTotal Bill is  Rs. ",cst)
    try:
        request.session['email']=request.POST.get('email')
        sendEmail(request, msg)
    except:
        i=-1

    veges=Veges.objects.all()
    nutrientes=nutrientsVeges.objects.all()
    nutrf=nutrientsFruits.objects.all()
    fruit=Fruits.objects.all()
    rc = RequestContext(request, {'veges': veges, 'nutrients': nutrientes,'nutrf':nutrf,'fruits':fruit})
    return render(request, 'f2p/mainpage.html', {'rc': rc})
