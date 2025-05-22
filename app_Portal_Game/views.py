from django.shortcuts import render, Http404

# Create your views here.
news_items = [
                 {
                     "id":1,
                     "title": "KK",
                     "image": "https://www.egierki.pl/app/uploads/2020/05/Tic-Tac-Toe.jpg",
                     "description": "Gra rozgrywana przez dwóch graczy",
                     "date": "",
                     "label": None,
                     "iframe": 'tt/index.html'
                 },
                 {
                    "id":2,
                     "title": "Snake",
                     "image": "https://a.allegroimg.com/original/113ada/38446c7a4f94b85fa75c5d1b4fc1/zabawka-gra-zrecznosciowa-waz-gryzie-snake",
                     "description": "Gra komputerowa, w której gracz kontroluje węża, poruszającego się po planszy.",
                     "date": "",
                     "label": "Akcja",
                     "iframe": 'snejk/index.html'
                 },
                 {
                    "id":3,
                     "title": "Tetris",
                     "image": "https://ramiz.pl/5514-superlarge_default/gra-tetris-jenga.jpg",
                     "description": "Klasyczna gra logiczna, w której gracz kontroluje spadające klocki różnego kształtu i układa je w studni, aby tworzyć ciągłe poziome linie.",
                     "date": "",
                     "label": None,
                      "iframe": 'tetres/index.html'
                 },
             ]


def index(request):
    context = {"news_items": news_items}

    return render(request, 'index.html', context)


def details(request, id):
    try:
        item = news_items[id - 1]
    except IndexError:
        raise Http404("Nie znaleziono wpisu.")

    context = {"item": item}
    return render(request, 'details.html', context)
