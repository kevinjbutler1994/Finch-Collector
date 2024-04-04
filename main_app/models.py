from django.db import models
from datetime import date

# Create your models here.
# A tuple of 2-tuples

# new code above
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

class Finch(models.Model):
 name = models.CharField(max_length=100)
 description = models.TextField(max_length=250)
 age = models.IntegerField()
 toys = models.ManyToManyField(Toy)

 def __str__(self):
  return self.name
 
def fed_for_today(self):
  return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Add new Feeding model below Finch model
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

  # Create a finch_id FK
finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
    ordering = ['-date']
...
age = models.IntegerField()