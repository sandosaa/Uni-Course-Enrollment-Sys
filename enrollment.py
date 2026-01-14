import click
import json
import os

@click.group()
def cli():
    """A tool for CLI""" 
    pass

file = 'test.json'
#for json file :)

def load_data():
    if not os.path.exists(file):
        return []
    with open(file,'r'):
        return json.load(file)
    
def save(data_file):
    with open(file,'w'):
        json.dump(data_file,file,indent=2)



@cli.command()
@click.option('--name','-n',nargs=2,help="Add a fullname student to the system")
@click.option('--course','-c',help="Enroll an available course")
@click.option('--email','-e',help="Add an email")

def add(name,course,email):
    if name:
        click.echo(f'{name[0]} {name[1]} is added to the system')
        
        if course:
            click.echo(f'You enrolled this course successfully "{course}"')
        if not course:
            click.echo(f"You didin't enroll yet, use 'update' to enroll..",fg='red')
        
        if email:
            click.secho(f'Added an email',fg='green')
        

@cli.command()
@click.option('--course','-c',help="Enroll an available course")
@click.option('--email','-e',help="Update the email info")
def update(course,email): #using id 
    pass

@cli.command()
@click.confirmation_option(prompt="Are you sure? You'll delete the student from the sys..")
def delete(): #using id -> we will create a file without the id you've chosen 
    pass

def view(): 
    pass

def info(): #maybe about the courses?
    pass

# @cli.command()
# @click.option('--course','-c',help="Enroll an available course")
# def enroll(course):
#     click.echo(f'You enrolled this course successfully "{course}"')


if __name__=="__main__":
    cli()