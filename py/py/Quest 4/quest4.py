stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

minimum = -1
best_brand = ""
for brand, sales in stats.items():
    if sales > minimum:
        minimum = sales
        best_brand = brand
print(f"Лучший бренд: {best_brand}")
        
        