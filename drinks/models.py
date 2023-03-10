from django.db import models

# ALL THESE CLASSES FOR WHISK APP #########################


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True)
    dateOfBirth = models.DateTimeField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)

    def __str__(self):
        return self.firstName


class RecipeCategory(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipeCategories')
    orderID = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=100)
    time = models.PositiveIntegerField(null=True)
    pictureUrl = models.CharField(max_length=500, null=True)
    videoUrl = models.CharField(max_length=500, null=True)
    videoImage = models.CharField(max_length=500, null=True)
    videoTitle = models.CharField(max_length=500, null=True)
    is_editor_choice = models.BooleanField(default=False)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE, related_name='recipes')
    orderID = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    @property
    def __repr__(self):
        return self.name


class Unit(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    @property
    def __repr__(self):
        return self.name


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True)
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='itemID')
    quantity = models.FloatField(null=True)
    unitID = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='UnitID', null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    orderNumber = models.PositiveIntegerField()

    @property
    def __repr__(self):
        return self.id


class Step(models.Model):
    id = models.UUIDField(primary_key=True)
    description = models.CharField(max_length=500)
    orderID = models.PositiveIntegerField(null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')

    @property
    def __repr__(self):
        return self.id


class ShoppingListCategory(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shoppingListCategories')
    orderID = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ShoppingListItem(models.Model):
    id = models.UUIDField(primary_key=True)
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_id')
    categoryID = models.ForeignKey(ShoppingListCategory, on_delete=models.CASCADE, related_name='items')
    isCheck = models.BooleanField(default=False)
    orderNumber = models.PositiveIntegerField()

    @property
    def __repr__(self):
        return self.id











