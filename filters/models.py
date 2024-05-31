from base import config
from django.db import models
from interests.models import Interest


TYPE = (
    ("WORLD", config.VERBOSE_NAME_WORLD),
    ("COUNTRY", config.VERBOSE_NAME_COUNTRY),
    ("REGION", config.VERBOSE_NAME_REGION),
    ("LOCAL", config.VERBOSE_NAME_LOCAL),
    ("CITY", config.VERBOSE_NAME_CITY),
    ("FACILITY", config.VERBOSE_NAME_FACILITY),
    ("SERVICE", config.VERBOSE_NAME_SERVICE),
    ("RATING", config.VERBOSE_NAME_RATING),
    ("SP1", config.VERBOSE_NAME_SP1),
    ("SP2", config.VERBOSE_NAME_SP2),
    ("SP3", config.VERBOSE_NAME_SP3),
)

class Filter(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    types = models.CharField(max_length=20, choices=TYPE)
    name = models.CharField(max_length=255)
    interests = models.ManyToManyField(Interest, blank=True, related_name="interest_filter")
    order = models.IntegerField(blank= True, null=True)

    class Meta:
        ordering = ('types', 'name',)
    
    def __str__(self):
        try:
            return f"{self.get_types_display()} : {self.ordering_name()}"
        except:
            return self.name

    def ordering_name(self):
        if self.parent:
            return f"{self.parent.ordering_name()} - {self.name}"
        return self.name
