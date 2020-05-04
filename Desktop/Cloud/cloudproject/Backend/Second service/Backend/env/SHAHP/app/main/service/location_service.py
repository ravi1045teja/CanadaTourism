from app.main import db
from app.main.model.models import TouristSpots


def get_all_locations():
    return TouristSpots.query.all()

#def search_packages(keyword):
#    search = "%{}%".format(keyword)
#    return  TouristSpots.query.filter(Package.destination.like(search)).all()

def get_a_location(id):
    return TouristSpots.query.filter_by(id=id).first()