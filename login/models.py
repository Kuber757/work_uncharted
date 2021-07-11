from django.db import models


#projects section
class projects:
    def __init__(self, pk, name, num_img, url_list):
        self.pk = pk
        self.name = name
        self.num_img = num_img
        self.url_list = url_list

li = ['images/Desktop_View/selenite/' + str(i) + '.jpg' for i in range(1,20)]
projects_list = [
    projects(1,'PARK HYATT VIENNAE', 13, li),
    projects(2,'PRIVATE RESENDENCIES', 5, li),
    projects(3,'SINGAPORE', 3, li),
    projects(4,'RIO', 8, li),
    projects(5,'SHANGHAI', 8, li),
    projects(6,'PARIS', 6, li),
    projects(7,'YATCH', 6, li),
    projects(8,'GRAND HYATT GURGAON', 6, li),
    projects(9,'CAPETOWN', 6, li),
    projects(10,'MILAN', 6, li),
    projects(11,'NEWYORK', 6, li),
    projects(12,'CLASS 55 YACHT', 6, li),
    projects(13,'KL WELLNESS CENTER', 6, li),
    projects(14,'OFFICE', 6, li),
]


#collections section
class collections:
    def __init__(self, pk, name, num_img, url_list):
        self.pk = pk
        self.name = name
        self.num_img = num_img
        self.url_list = url_list

li = ['images/Desktop_View/selenite/' + str(i) + '.jpg' for i in range(1,26)]
collections_list = [
    collections(1,'VASES', 13, li),
    collections(2,'LIGHTS', 13, li),
    collections(3,'TABLES', 13, li),
    collections(4,'LAMPS', 13, li),
    collections(5,'CHAIRS', 13, li),
    collections(6,'BOWLS', 13, li),
    collections(7,'CABINS', 13, li),
    collections(8,'BRASS FURNITURE', 13, li),
    collections(9,'ACCESSORY SETS', 13, li),
    collections(10,'BATHROOM SETS', 13, li),
    collections(11,'BONE & HORN', 13, li),
    collections(12,'CARPETS', 13, li),
    collections(13,'CUSHIONS', 13, li),
    collections(14,'TRAY', 13, li),
]


#materials section
class materials:
    def __init__(self, pk, name, num_img, url_list,col_list=[],pro_list=[]):
        self.pk = pk
        self.name = name
        self.num_img = num_img
        self.url_list = url_list
        self.collections = col_list
        self.projects = pro_list

li = ['images/Desktop_View/selenite/' + str(i) + '.jpg' for i in range(1,24)]
materials_list = [
    materials(1,'SEMI PRECIOUS STONE', 13, li, [1,3,5], [2,3]),
    materials(2,'STRAW MACQUERTY', 13, li, [2,3], [1,]),
    materials(3,'GLASS', 13, li, [5,], [1,4]),
    materials(4,'MOTHER OF PEARL', 13, li, [6,7], [3,5]),
    materials(5,'STONE', 13, li),
    materials(6,'SELENITE', 13, li),
    materials(7,'STINGRAY', 13, li),
    materials(8,'GRAND HYATT GURGAON', 13, li),
    materials(9,'BRASS', 13, li),
    materials(10,'LEATHER', 13, li),
    materials(11,'WOOD', 13, li),
    materials(12,'PARCHMENT', 13, li),
    materials(13,'BONE', 13, li),
    materials(14,'BONE', 13, li),
    materials(15,'HORN', 13, li),
    materials(16,'LEAFING', 13, li),
    materials(17,'LACQUERWARE', 13, li),
    materials(18,'NATURE MATERIAL', 13, li),
]
