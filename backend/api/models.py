from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VacancyList(BaseModel):
    selected_date = models.DateTimeField()
    no_of_vacancy = models.PositiveIntegerField(default=5)

    def __str__(self):
        return str(self.selected_date)


class BookingEntry(BaseModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_cost = models.FloatField()

    def __str__(self):
        return self.total_cost
