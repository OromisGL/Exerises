# Eigene Klasse
 
# Suche dir ein Objekt aus deiner Umgebung/Fantasie.
# Schreibe eine eigene Klasse dazu mit
# Konstruktor
# Objekt-Attributen
# Objekt-Methoden
# Statischem Attribut
# ToString-Methode - __str__()
# Entsprechende Getter & Setter
 
# Erzeuge dann einige Objekte, verändere sie und lasse sie wieder anzeigen.


# Eine Aufgabe die ich bei Codecademy machen musste:
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"
  
  def calculate_bill(self, purchased_items):
    return sum(self.items[item] for item in purchased_items)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menu = menus
  
  def __repr__(self):
    return f"Our Franchise store is located at {self.address}"
  
  def available_menus(self, time):
    available_menus = []

    for menu in self.menu:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)
        return available_menus
    return [menu for menu in self.menu if menu.start_time <= time <= menu.end_time]
  
brunch = {
  'pancakes':       7.50, 
  'waffles':        9.00, 
  'burger':         11.00, 
  'home fries':     4.50, 
  'coffee':         1.50, 
  'espresso':       3.00, 
  'tea':            1.00, 
  'mimosa':         10.50, 
  'orange juice':   3.50
}

early_bird = {  
  'salumeria plate':                                8.00, 
  'salad and breadsticks (serves 2, no refills)':   14.00, 
  'pizza with quattro formaggi':                    9.00, 
  'duck ragu':                                      17.50, 
  'mushroom ravioli (vegan)':                       13.50, 
  'coffee':                                         1.50, 
  'espresso':                                       3.00,
}
dinner = {
  'crostini with eggplant caponata':    13.00, 
  'caesar salad':                       16.00, 
  'pizza with quattro formaggi':        11.00, 
  'duck ragu':                          19.50, 
  'mushroom ravioli (vegan)':           13.50, 
  'coffee':                             2.00, 
  'espresso':                           3.00,
}
kids = {
  'chicken nuggets':                6.50, 
  'fusilli with wild mushrooms':    12.00, 
  'apple juice':                    3.00
}
arepa = {
  'arepa pabellon':     7.00, 
  'pernil arepa':       8.50, 
  'guayanes arepa':     8.00, 
  'jamon arepa':        7.50
}


brunch = Menu('brunch', brunch, 11, 16)
early_bird = Menu('early bird', early_bird, 12, 16)
dinner = Menu('dinner', dinner, 17, 23)
kids = Menu('kids', kids, 11, 21)
arepa = Menu("Take a' Arepa", arepa, 10, 18)

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", menus)

class Business:
  def __init__(self, name, franchise):
    self.name = name
    self.franchise = franchise

business = Business("Basta Fazoolin' with my Heart", [new_installment, flagship_store])

new_business = Business("Take a' Arepa", arepas_place)

print(Franchise(flagship_store, kids))
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))