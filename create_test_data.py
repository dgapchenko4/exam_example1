import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoe_store.settings')
django.setup()

from products.models import Category, Product

print("Создание тестовых данных...")

# Создание категорий
categories_data = [
    {'name': 'Кроссовки', 'description': 'Спортивная обувь для активного образа жизни'},
    {'name': 'Туфли', 'description': 'Классическая и деловая обувь'},
    {'name': 'Сапоги', 'description': 'Зимняя и осенняя обувь'},
    {'name': 'Ботинки', 'description': 'Повседневная обувь'},
    {'name': 'Сандалии', 'description': 'Летняя обувь'},
    {'name': 'Тапочки', 'description': 'Домашняя обувь'},
]

categories = {}
for cat_data in categories_data:
    category = Category.objects.create(
        name=cat_data['name'],
        description=cat_data['description']
    )
    categories[cat_data['name']] = category
    print(f'✓ Создана категория: {category.name}')

# Создание товаров
products_data = [
    {
        'name': 'Nike Air Max 270',
        'description': 'Удобные кроссовки с воздушной подушкой для максимального комфорта при ходьбе и беге. Идеально подходят для спорта и повседневной носки.',
        'price': 7990,
        'category': categories['Кроссовки'],
        'is_available': True
    },
    {
        'name': 'Adidas Ultraboost 22',
        'description': 'Беговые кроссовки с инновационной технологией Boost для превосходной амортизации и возврата энергии. Подходят для серьезных тренировок.',
        'price': 8990,
        'category': categories['Кроссовки'],
        'is_available': True
    },
    {
        'name': 'Кожаные туфли Oxford',
        'description': 'Элегантные классические туфли из натуральной кожи ручной работы. Идеальны для деловых встреч и формальных мероприятий.',
        'price': 6990,
        'category': categories['Туфли'],
        'is_available': True
    },
    {
        'name': 'Зимние сапоги Timberland',
        'description': 'Теплые зимние сапоги с водонепроницаемой мембраной и утеплителем. Гарантируют сухость и тепло в любую погоду.',
        'price': 12990,
        'category': categories['Сапоги'],
        'is_available': True
    },
    {
        'name': 'Ботинки Dr. Martens 1460',
        'description': 'Культовые ботинки с воздушной подошвой и знаменитой желтой строчкой. Символ стиля и надежности.',
        'price': 14990,
        'category': categories['Ботинки'],
        'is_available': True
    },
    {
        'name': 'Сандалии Birkenstock Arizona',
        'description': 'Ортопедические сандалии с пробковой стелькой, повторяющей форму стопы. Обеспечивают правильную поддержку и комфорт.',
        'price': 5990,
        'category': categories['Сандалии'],
        'is_available': True
    },
    {
        'name': 'Домашние тапочки с мехом',
        'description': 'Мягкие и теплые домашние тапочки с натуральным мехом. Идеальны для холодных вечеров дома.',
        'price': 1990,
        'category': categories['Тапочки'],
        'is_available': True
    },
    {
        'name': 'Кроссовки New Balance 574',
        'description': 'Стильные кроссовки для повседневной носки с классическим дизайном и современными технологиями комфорта.',
        'price': 7490,
        'category': categories['Кроссовки'],
        'is_available': True
    },
    {
        'name': 'Лоферы из замши',
        'description': 'Стильные лоферы из мягкой замши без шнуровки. Универсальная обувь для офиса и отдыха.',
        'price': 5490,
        'category': categories['Туфли'],
        'is_available': True
    },
    {
        'name': 'Осенние ботинки Chelsea',
        'description': 'Стильные ботинки Chelsea с резиновыми вставками для легкого надевания. Идеальны для городской носки.',
        'price': 8990,
        'category': categories['Ботинки'],
        'is_available': True
    },
    {
        'name': 'Резиновые сапоги',
        'description': 'Водонепроницаемые резиновые сапоги для дождливой погоды. Практичные и удобные.',
        'price': 2990,
        'category': categories['Сапоги'],
        'is_available': True
    },
    {
        'name': 'Пляжные сланцы',
        'description': 'Легкие и удобные сланцы для пляжа и бассейна. Быстро сохнут и не скользят.',
        'price': 1490,
        'category': categories['Сандалии'],
        'is_available': True
    },
]

for prod_data in products_data:
    product = Product.objects.create(**prod_data)
    print(f'✓ Создан товар: {product.name} - {product.price} руб.')

print(f'\n{"="*50}')
print(f'ИТОГО: Создано {Category.objects.count()} категорий')
print(f'       Создано {Product.objects.count()} товаров')
print('='*50)
