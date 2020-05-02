
import logging
import csv
import sqlite3
import homework.validators as validators
import homework.decs as decs

logger = logging.getLogger("inf")
logger.setLevel(logging.INFO)
handler = logging.FileHandler('inf.log', 'w', 'utf-8')
formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

err = logging.getLogger("err")
err.setLevel(logging.ERROR)
handler2 = logging.FileHandler('err.log', 'w', 'utf-8')
handler2.setFormatter(formatter)
err.addHandler(handler2)

path = "data.csv"



class Patient:
    first_name = validators.Not_renamalbe()
    last_name = validators.Not_renamalbe()
    birth_date = validators.Date_discr()
    phone = validators.Phone_discr()
    document_type = validators.Doc_type_discr()
    document_id = validators.Doc_id_discr()

    @decs.my_logging_decorator
    def __init__(self, *args):
        self.logger_inf = logging.getLogger("inf")
        self.logger_err = logging.getLogger("err")
        self.first_name = args[0]
        self.last_name = args[1]
        self.birth_date = args[2]
        self.phone = args[3]
        self.document_type = args[4]
        self.document_id = args[5]



    @staticmethod
    def create(fname, lname, bdate, number, doc_type, doc_id):
        return Patient(fname, lname, bdate, number, doc_type, doc_id)

    @decs.my_logging_decorator
    def save(self):

        myData = [str(self).split(",")]

        myFile = open(path, 'a', newline="")
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)


    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.birth_date}, {self.phone}, {self.document_type}, {self.document_id}"


class PatientCollection(object):
    def __init__(self, path):
        self.path = path
        self.cursor = 0
        self.count = -1

    def __iter__(self):
        return self

    def limit(self, n):
        self.count = n
        return self.__iter__()

    def __next__(self):
        with open(self.path,'r') as File:
            File.seek(self.cursor)
            data = File.readline()
            self.cursor = File.tell()

        if not data or not self.count:
            raise StopIteration
        self.count -= 1
        return Patient(*data.split(','))
