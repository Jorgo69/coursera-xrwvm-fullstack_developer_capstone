# Décommentez les imports nécessaires
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Modèle CarMake
class CarMake(models.Model):
    # Nom de la marque (champ obligatoire)
    name = models.CharField(max_length=100)

    # Description de la marque (champ obligatoire)
    description = models.TextField()

    # Autres champs facultatifs
    founded_year = models.IntegerField(null=True, blank=True, help_text="Année de création de la marque")
    headquarters = models.CharField(max_length=200, null=True, blank=True, help_text="Siège social de la marque")

    def __str__(self):
        return self.name  # Retourne le nom comme représentation textuelle


# Modèle CarModel
class CarModel(models.Model):
    # Types de voitures possibles (choix limités)
    CAR_TYPES = [
        ('SEDAN', 'Berline'),
        ('SUV', 'SUV'),
        ('WAGON', 'Break'),
        ('COUPE', 'Coupé'),
        ('CONVERTIBLE', 'Cabriolet'),
    ]

    # Relation Many-to-One avec CarMake (une marque peut avoir plusieurs modèles)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="car_models")

    # Nom du modèle (champ obligatoire)
    name = models.CharField(max_length=100)

    # Identifiant du concessionnaire (IntegerField) se réfère à un concessionnaire créé dans la base de données Cloudant
    dealer_id = models.IntegerField(help_text="Identifiant du concessionnaire associé à ce modèle")

    # Type de voiture (champ obligatoire, choix limités)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SEDAN')

    # Année du modèle (champ obligatoire, avec validation)
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)],
        help_text="Année du modèle (entre 2015 et 2023)"
    )

    # Autres champs facultatifs
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Prix du modèle")
    created_at = models.DateTimeField(default=now, help_text="Date de création de l'entrée")

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # Exemple : "Toyota Corolla (2020)"