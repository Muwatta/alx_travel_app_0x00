from django.core.management.base import BaseCommand
from listings.models import Destination

class Command(BaseCommand):
    help = "Seeds initial data into the database"

    def handle(self, *args, **kwargs):
        Destination.objects.create(
            name="Lagos Island",
            description="A vibrant cultural hub with beaches and nightlife.",
            price=150,
            available=True,
        )
        self.stdout.write(self.style.SUCCESS("✅ Data seeded successfully"))
