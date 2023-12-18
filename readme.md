
# Django Shell Practice

## Описание
Этот репозиторий представляет собой примеры использования QuerySet в Django shell. Здесь мы создаем модели `Company`, `Worker`, `Project`, и `Address`, и проводим различные операции, используя различные методы QuerySet и концепции, такие как `related_name`, `related_query_name`, `ManyToManyField`, и `OneToOneField`.


### Импорт моделей и необходимых функций в Python Shell
```python
from product.models import Company, Worker, Project, Address
from django.db.models import Avg, Count, Sum, Min, Max
```
### Создание адреса для компании и компании
```python
company_address = Address.objects.create(city="Bishkek", street="Manasa 62")
company1 = Company.objects.create(name='IT pro', address=company_address)

company_address
<Address: Address object (1)>
company1
<Company: Company object (1)>
```

### Создание работников для компании
```python
worker1 = Worker.objects.create(name='Ivan', age=31, company=company1)
worker2 = Worker.objects.create(name='Igor', age=20, company=company1)
worker3 = Worker.objects.create(name='Elena', age=25, company=company1)
worker4 = Worker.objects.create(name='Alice', age=40, company=company1)
```

### Получение адреса компании и всех работников компании
```python
company1.address
<Address: Address object (1)>
company1.workers.all()
<QuerySet [<Worker: Worker object (1)>, <Worker: Worker object (2)>, <Worker: Worker object (3)>, <Worker: Worker object (4)>]>
```

### Создание проектов
```python
project1 = Project.objects.create(title='New facebook 2.0')
project2 = Project.objects.create(title='New VK 2.0')
project1
<Project: Project object (1)>
```

### Добавление работников к проектам
```python
project1.workers.add(worker1, worker2, worker3, worker4)
project2.workers.add(worker3, worker4)
```

### Получение всех работников для каждого проекта
```python
project1.workers.all()
<QuerySet [<Worker: Worker object (1)>, <Worker: Worker object (2)>, <Worker: Worker object (3)>, <Worker: Worker object (4)>]>
project2.workers.all()
<QuerySet [<Worker: Worker object (3)>, <Worker: Worker object (4)>]>
```

### Получение всех проектов одного работника
```python
worker3.projects.all()
<QuerySet [<Project: Project object (1)>, <Project: Project object (2)>]>
```
### Фильтрация работников в проекте по возрасту
```python
project1.workers.filter(age__gt=30)
<QuerySet [<Worker: Worker object (1)>, <Worker: Worker object (4)>]>
```
### Фильтрация работников компании по имени (по подстроке)
```python
company1.workers.filter(name__contains='I')
<QuerySet [<Worker: Worker object (1)>, <Worker: Worker object (2)>]>
```
### Фильтрация работников компании по имени и возрасту
```python
company1.workers.filter(name__contains='I', age__lt=30)
<QuerySet [<Worker: Worker object (2)>]>
```
### Находим средний возраст работников компании
```python
company1.workers.aggregate(Avg('age'))
{'age__avg': 29.0}
```
### Подсчет количества всех работников компании
```python
company1.workers.aggregate(Count('pk'))
{'pk__count': 4}
```
### Подсчет количества проектов для работника
```python
worker4.projects.aggregate(Count('pk'))
{'pk__count': 2}
```
### Сумма возростов всех работников компании
```python
company1.workers.aggregate(Sum('age'))
{'age__sum': 116}
```
### Минимальный возраст работника проекта 2
```python
project2.workers.aggregate(Min('age'))
{'age__min': 25}
```
### Максимальный возраст работника проекта 1
```python
project1.workers.aggregate(Max('age'))
{'age__max': 40}
```
### Сумма возрастов работникой у которых в имени есть 'I'(чуствительно к регистру)
```python
company1.workers.filter(name__contains = 'I').aggregate(Sum('age'))
{'age__sum': 51}
```
### Получаем всех работников в имени которых есть 'i'(не чуствительно к регистру)
```python
company1.workers.filter(name__icontains = 'i')
<QuerySet [<Worker: Worker object (1)>, <Worker: Worker object (2)>, <Worker: Worker object (4)>]>
```
### Получаем всех работников имя которых начинается с 'I'
```python
company1.workers.filter(name__istartswith = 'I')
<QuerySet [<Worker: Worker object (1)>, <Worker: Worker object (2)>]>
```
### Изменение имени работника
```python
Worker.objects.filter(name='Ivan').update(name='Vanya')
```
### Получение работника по новому имени
```python
Worker.objects.get(name='Vanya')
<Worker: Worker object (1)>
```
### Удаление работника из проекта
```python
worker4.delete()
```
### Получение всех работников после удаления
```python
Worker.objects.all()
<QuerySet [<Worker: Worker object (2)>, <Worker: Worker object (3)>, <Worker: Worker object (1)>]>
```
### Получение работников в проекте после удаления
```python
project2.workers.all()
<QuerySet [<Worker: Worker object (3)>]>
```
### Получение работников в проекте после изменения имени
```python
project1.workers.all()
<QuerySet [<Worker: Worker object (2)>, <Worker: Worker object (3)>, <Worker: Worker object (1)>]>
```
