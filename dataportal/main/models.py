from django.db import models

# Create your models here.



class AppCategory(models.Model):
    category_name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Application Category"
        verbose_name_plural = "Application Categories"
    
    def __str__(self):
        return self.category_name
        

class App(models.Model):
	app_name = models.CharField(max_length=20)
	app_description = models.CharField(
		max_length=100,
		null=True,
		blank=True,
		)
	release_date = models.DateField()
	app_image = models.ImageField(
		null=True, # empty values stored as null in database
		blank=True, # empty values are allowed
	)
	app_icon = models.CharField(
		max_length=20,
		null=True,
		blank=True,
		) # string for semantic ui icon name
	app_category = models.ForeignKey(
		AppCategory,
		default=1,
		verbose_name="Category",
		on_delete=models.SET_DEFAULT,
		)
    
	class Meta:
		verbose_name = "Application"
		verbose_name_plural = "Applications"
    
	def __str__(self):
		return self.app_name