from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seeds the database with sample listings"

    def handle(self, *args, **kwargs):
        data = [
            {
                "title": "Lekki Beach Apartment",
                "description": "A cozy apartment near the beach in Lagos.",
                "location": "Lagos",
                "price_per_night": 20000,
                "available": True,
            },
            {
                "title": "Abuja City Suite",
                "description": "Luxury suite in the heart of Abuja with a great view.",
                "location": "Abuja",
                "price_per_night": 35000,
                "available": True,
            },
            {
                "title": "Kano Traditional Stay",
                "description": "Cultural home experience in Kano city.",
                "location": "Kano",
                "price_per_night": 15000,
                "available": False,
            },
        ]

        for item in data:
            Listing.objects.get_or_create(**item)

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))
