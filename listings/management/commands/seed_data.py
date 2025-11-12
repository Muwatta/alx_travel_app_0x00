from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with initial listings'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()
        Listing.objects.create(title="Paris Trip", description="Visit the Eiffel Tower")
        Listing.objects.create(title="New York Tour", description="Explore Times Square")
        Listing.objects.create(title="Tokyo Adventure", description="Experience Shibuya Crossing")
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
