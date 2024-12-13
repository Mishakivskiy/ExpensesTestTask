from django.db.models import Model, CharField, EmailField, ForeignKey, DecimalField, DateField, CASCADE


class User(Model):
    username = CharField(max_length=150, unique=True)
    email = EmailField(unique=True)

    def __str__(self):
        return self.username


class Expense(Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other'),
    ]

    user = ForeignKey(User, on_delete=CASCADE, related_name='expenses')
    title = CharField(max_length=255)
    amount = DecimalField(max_digits=10, decimal_places=2)
    date = DateField()
    category = CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.category}) - {self.amount}"
