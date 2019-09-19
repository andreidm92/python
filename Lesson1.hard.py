# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = int(input('Введите ваш возраст: '))
weight = int(input('Введите ваш вес: '))

if 50 <= weight <= 120:
    if age <= 30:
        print(name + ' ' + surname + ',', str(age) + ' год,', 'вес ' + str(weight) + ' кг,', '- вы в отличном состоянии!')
    else:
        print(name + ' ' + surname + ',', str(age) + ' год,', 'вес ' + str(weight) + ' кг,', '- вы все еще в хорошей форме!')
elif weight < 50 or weight > 120:
    if 30 <= age <= 40:
        print(name + ' ' + surname + ',', str(age) + ' год,', 'вес ' + str(weight) + ' кг,', '- вам нужно заняться собой!')
    elif age > 40:
        print(name + ' ' + surname + ',', str(age) + ' год,', 'вес ' + str(weight) + ' кг,', '- вам срочно требуется медосмотр!')
    else:
        print(name + ' ' + surname + ',', str(age) + ' год,', 'вес ' + str(weight) + ' кг,', '- вы молоды и пока еще прекрасны!')

