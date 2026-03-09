from django.db import models

class QRCode(models.Model):

    TYPE = (
        ('url','URL'),
        ('email','Email'),
        ('phone','Phone'),
        ('contact','Contact'),
        ('pdf','PDF'),
    )

    qr_type = models.CharField(max_length=20, choices=TYPE)
    data = models.TextField()
    color = models.CharField(max_length=20, default="black")

    qr_image = models.ImageField(upload_to='qr_codes/')

    scans = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qr_type