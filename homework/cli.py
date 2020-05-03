import click
import sqlite3
from patient import Patient, PatientCollection

@click.group()
def cli():
    pass

@click.command()
@click.argument('f_name')
@click.argument('s_name')
@click.option('--birth-date')
@click.option('--phone')
@click.option('--document-type')
@click.option('--document-number', type=(str, str))
def create(f_name, s_name, birth_date, phone, document_type, document_number):
    document_number = ''.join(document_number)
    p = Patient(f_name, s_name, birth_date, phone, document_type, document_number)
    p.save()

@click.command()
@click.argument('limit', default = 10)
def show(limit):
    conn = sqlite3.connect('covid19.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM covid19 ORDER BY ROWID DESC LIMIT {limit}")
    print(*cursor.fetchall()[::-1], sep="\n")

@click.command()
def count():
    k=0
    collection = PatientCollection('covid19.db')
    for i in collection:
        k+=1
    print(k)

cli.add_command(create)
cli.add_command(show)
cli.add_command(count)

if __name__ == '__main__':
    cli()