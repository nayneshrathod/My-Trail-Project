from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")


# Create your views here.
def index(request):
    if request.method=='GET':
        page = requests.get(
            "https://www.google.com/search?sxsrf=ALeKk020wotEefDUvDX4XeXqnTNhvbDZwQ:1587623817287&q=coronavirus+tips&oi=ddle&ct=153607377&hl=en&sa=X&ved=0ahUKEwjkoKjN9_3oAhW5yzgGHS2fDRcQPQgN&biw=1316&bih=637&dpr=1#wptab=s:H4sIAAAAAAAAAONgVuLVT9c3NMwySk6OL8zJecTozS3w8sc9YSmnSWtOXmO04eIKzsgvd80rySypFNLjYoOyVLgEpVB1ajBI8XOhCvHsYuL2SE3MKckILkksKV7EKpicX5Sfl1iWWVRarFAMEgMAoubRkIEAAAA")
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify())
        # tonight = soup.find('table', attrs={'jsname': 'NLtp9', 'class': 'e1WeKc'})
        # print(tonight.prettify())
        data = {"Source_Code": soup.prettify(), }

        return render(request, 'index.html', context=data)


def home(request, number):
    title = """<h1>This Is a Sample page of World life... %s !</h1>""" % number
    return HttpResponse(title)
