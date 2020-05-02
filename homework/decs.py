def my_logging_decorator(func):
    def wrapper(*args): #self, instance, value

        if func.__name__  == '__init__':
            func(*args)
            args[0].logger_inf.info('Был создан новый пациент')

        elif func.__name__  == 'save':
            func(*args)
            args[0].logger_inf.info('Запись о новом пациенте сохранена')

        else:
            f = False  # флаг на изменение
            if func.__name__ == '__set__':
                if args[0].name in args[1].__dict__ and getattr(args[1], args[0].name):
                    f = True
            try:
                func(*args)
                if f:
                    args[1].logger_inf.info(f'{args[0].name} изменен')
            except TypeError:
                args[1].logger_err.error(f'TypeError: {args[2]} must be string')
                raise TypeError
            except ValueError:
                args[1].logger_err.error(f'ValueError: wrong value - {args[2]}')
                raise ValueError
            except AttributeError:
                args[1].logger_err.error(f'AttributeError: Переназначение не предусмотрено - {args[2]}')
                raise AttributeError
    return wrapper