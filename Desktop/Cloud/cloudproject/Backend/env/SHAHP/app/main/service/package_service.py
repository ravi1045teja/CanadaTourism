from app.main import db
from app.main.model.models import Package


def get_all_packages():
    return Package.query.all()

def search_packages(keyword):
    search = "%{}%".format(keyword)
    return  Package.query.filter(Package.destination.like(search)).all()

def get_a_package(location):
    return Package.query.filter_by(destination=location).first()