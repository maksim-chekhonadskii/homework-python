goods = []
features = {'Наименование продукта': '', 'Цена': '', 'Количество': '', 'ед.': ''}
analytics = {'Наименование продукта': [], 'Цена': [], 'Количество': [], 'ед.': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода наберите 'Q', для продолжения нажмите 'Enter', для получения аналитики наберите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))