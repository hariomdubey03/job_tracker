from django.db import models


class Candidate(models.Model):
    # Added full text index for name field due to Django ORM limitations.
    name = models.CharField(max_length=255)

    age = models.IntegerField()
    GENDER_CHOICES = [
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    class Meta:
        indexes = [
            models.Index(
                fields=["name"],
                name="idx_name",
            ),
            models.Index(fields=["email"], name="idx_email"),
        ]
