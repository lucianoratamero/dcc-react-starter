from django.core.management import call_command
from django.core.management.base import BaseCommand

from {{cookiecutter.project_slug}}.users.tests.factories import UserFactory
from {{cookiecutter.project_slug}}.cheeses.models import Cheese
from {{cookiecutter.project_slug}}.cheeses.tests.factories import CheeseFactory


class Command(BaseCommand):
    help = "Adds sample cheeses and users to the database, so you can get started."

    def handle(self, *args, **kwargs):
        print('Creating "cheesehead" user and cheeses...')
        cheesehead_user = UserFactory(
            username="cheesehead",
            email="cheesehead@example.com",
            password="ilovecheese",
            name="Jacky Cheddar",
        )
        CheeseFactory(
            creator=cheesehead_user,
            name="Colby",
            description="Similar to Cheddar but without undergoing"
            " the cheddaring process, Colby is a mild, creamy"
            " cheese that was first created in 1885 in Colby,"
            " Wisconsin.",
            firmness=Cheese.Firmness.SEMI_HARD,
            country_of_origin="US",
        )
        CheeseFactory(
            creator=cheesehead_user,
            name="Camembert",
            description="A French cheese with a white, powdery rind and a soft, delicately salty interior.",
            firmness=Cheese.Firmness.SOFT,
            country_of_origin="FR",
        )
        CheeseFactory(
            creator=cheesehead_user,
            name="Stracchino",
            description="Semi-sweet cheese that goes well with starches.",
            firmness=Cheese.Firmness.SOFT,
            country_of_origin="IT",
        )
        CheeseFactory(
            creator=cheesehead_user,
            name="Gouda",
            description="A Dutch yellow cheese that develops"
            " a slight crunchiness and a complex salty toffee-like flavor as it ages.",
            firmness=Cheese.Firmness.HARD,
            country_of_origin="NE",
        )
        CheeseFactory(
            creator=cheesehead_user,
            name="Cheddar",
            description="A relatively hard, pale yellow to off-white, and sometimes sharp-tasting cheese.",
            firmness=Cheese.Firmness.HARD,
            country_of_origin="GB",
        )
        print("Creating a superuser...")
        call_command("createsuperuser")
        print(
            "Done! Now run the server and check the admin for new data."
        )
