###  Wzorowane na przykładzie Rona Zacharskiego
##
##
##from math import sqrt
##
##users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
##         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
##         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
##         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
##         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
##         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
##         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
##         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
##        }
##
##
##
##def manhattan(rating1, rating2):
##    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
##       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
##       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
##       
##    # TODO: wpisz kod
##    pass
##
##
##def computeNearestNeighbor(username, users):
##    """dla danego użytkownika, zwróć listę innych użytkowników według bliskości preferencji"""
##    distances = []
##    # TODO: wpisz kod
##    return distances
##
##def recommend(username, users):
##    """Zwróć listę rekomendacji dla użytkownika"""
##    # znajdź preferencje najbliższego sąsiada
##    nearest = computeNearestNeighbor(username, users)[0][1]
##
##    recommendations = []
##    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiada
##    # TODO: wpisz kod
##    # using the fn sorted for variety - sort is more efficient
##    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)
##
### przykłady
##
##print( recommend('Hela', users))
###print( recommend('Celina', users))
##

print( "Nazywam si� Maria Szumska, m�j login to: szumska. Je�li chodzi o temat mojej pracy magisterkiej to jestem na etapie szukania. Najprawdopodobniej b�dzie to praca na temat: Analizy przestrzenne zdarze� sejsmicznych na obszarze Polski z wykorzystaniem oprogramowania GIS")
print("Wed�ug mnie w powy�yszm kodzie u�ytkownicy przyznaj� oceny wymienionym wykonawc�. Na podstawie wystawionych ocen znajdowani s� u�ytkownicy o podobnym gu�cie muzycznym")
       
