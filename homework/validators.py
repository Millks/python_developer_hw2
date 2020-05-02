import datetime
import time
import homework.decs as decs


class Name_discr(object):
    def __set_name__(self, owner, name):
        self.name = name

    @decs.my_logging_decorator
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Неверный тип имени')
        value = value.strip()
        for i in value:
            if value.isalpha():
                instance.__dict__[self.name] = value
            else:
                raise ValueError("ValueError: 'Неверное имя'")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

class Date_discr(object):
    def __set_name__(self, owner, name):
        self.name = name

    @decs.my_logging_decorator
    def __set__(self, instance, value):
        month_dict = {'Января': '01', 'Февраля': '02', 'Марта': '03', 'Апреля': '04', 'Мая': '05', 'Июня': '06',
                      'Июля': '07', 'Августа': '08', 'Сентября': '09', 'Октября': '10', 'Ноября': '11', 'Декабря': '12'}
        if not isinstance(value, str):
            raise TypeError('Неверный тип данных')
        value = value.strip()
        for symbol in value:
            if symbol == ' ' or symbol == "-":
                value = value.replace(symbol, '.')
        birth_lst = value.split('.')
        if len(birth_lst) == 3:
            if not birth_lst[1].isdigit() and birth_lst[1].title() in month_dict:
                birth_lst[1] = month_dict[birth_lst[1].title()]
            try:
                datetime.date(int(birth_lst[0]), int(birth_lst[1]), int(birth_lst[2]))
            except ValueError:
                birth_lst[0], birth_lst[2] = birth_lst[2], birth_lst[0]

            f = True  # флаг, указание на то, что есть число из четырех цифр
            for i in range(len(birth_lst)):
                if len(birth_lst[i]) == 1:
                    birth_lst[i] = '0' + birth_lst[i]
                if len(birth_lst[i]) == 4:
                    if birth_lst[i][0:2] == "19" or "20":
                        f = False
                    else:
                        raise AttributeError('Неверный формат года')

            if f:
                if (len(birth_lst[2]) == 2 and int(birth_lst[2]) > 20):
                    birth_lst[2] = '19' + birth_lst[2]
                elif len(birth_lst[2]) == 2 and int(birth_lst[2]) <= 20:
                    birth_lst[2] = '20' + birth_lst[2]
            value = "-".join(birth_lst)
            try:

                #if self.name in instance.__dict__ and getattr(instance, self.name):
                 #   instance.logger_inf.info("Дата рождения изменена")
                instance.__dict__[self.name] = time.strftime("%Y-%m-%d", time.strptime(str(value), "%Y-%m-%d"))
            except ValueError:
                raise ValueError('Неверный формат даты')
        else:
            raise ValueError(f'Неверный формат даты {birth_lst}')

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Phone_discr(object):
    def __set_name__(self, owner, name):
        self.name = name

    @decs.my_logging_decorator
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Неверный тип данных')
        value = value.strip()
        new_value = ""
        for i in value:
            if i.isdigit():
                new_value += i
        if len(new_value) != 11:
            raise ValueError('Неверный формат номера телефона')
        else:
            new_value = "7" + new_value[1:]
            #if self.name in instance.__dict__ and getattr(instance, self.name):
            #    instance.logger_inf.info("Телефон изменен")
            instance.__dict__[self.name] = new_value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Doc_type_discr(object):
    def __set_name__(self, owner, name):
        self.name = name

    @decs.my_logging_decorator
    def __set__(self, instance, value):
        white_lst = ['Паспорт', 'Заграничный паспорт', 'Водительские права']
        if not isinstance(value, str):
            raise TypeError('Неверный тип данных')
        value = str(value)
        value = value.strip()
        if value.capitalize() in white_lst:
            value = value.capitalize()
            #if self.name in instance.__dict__ and getattr(instance, self.name):
            #    instance.logger_inf.info("Тип документа изменен")
            instance.__dict__[self.name] = value
        else:
            raise ValueError('Неверный формат документа')

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Doc_id_discr(object):
    def __set_name__(self, owner, name):
        self.name = name

    @decs.my_logging_decorator
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Неверный тип данных')
        value = str(value)
        value = value.strip()

        doc_dict = {'Паспорт': 10, 'Водительские права': 10, 'Заграничный паспорт': 9}
        wrong_symbls = r"\/- "
        for symbol in value:
            if symbol in wrong_symbls or symbol == '\n':
                value = value.replace(symbol, '')
        for i in value:
            if not i.isdigit():
                raise ValueError(f'Неверный формат номера документа {value}')

        if len(value) == doc_dict[getattr(instance, 'document_type')]:
            #if self.name in instance.__dict__ and getattr(instance, self.name):
            #    instance.logger_inf.info("Тип документа изменен")
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f'Неверный формат номера документа {value}')

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

class Not_renamalbe(Name_discr):
    def __set_name__(self, owner, name):
        self.name = name

    @decs.my_logging_decorator
    def __set__(self, instance, value):
        if self.name in instance.__dict__ and getattr(instance, self.name):
            raise AttributeError('Переназначение не предусмотрено')
        else:
            super().__set__(instance, value)


