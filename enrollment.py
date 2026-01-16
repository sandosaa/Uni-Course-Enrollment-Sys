import click
import json
import os

"""
Available courses 
1. Databases
2. Computational Intelligence
3. Data Structures
4. Natural Language Processing
5. Operating Systems
6. Multi Agent Systems Design
7. Computer Security

"""
courses=['Databases','Computational Intelligence',
        'Data Structures','Natural Language Processing',
        'Operating Systems','Multi Agent Systems Design',
        'Computer Security']

@click.group()
def cli():
    """A tool for CLI""" 
    pass

json_file = ('test.json')
#for json file :)

def load_data():
    if not os.path.exists(json_file):
        return []
    with open(json_file,'r') as file:
        return json.load(file)
    
def save(data_file):
    with open(json_file,'w') as file:
        json.dump(data_file,file,indent=2)


@cli.command()
@click.option('--name','-n',nargs=2,help="Add First & Last student's name to the system")
@click.option('--course','-c',help="Enroll an available course ...",type=int)
@click.option('--email','-e',help="Add an email")

def add(name,course,email):
    
    if name:   
        data=load_data()
        if not data:
            data_id = 1
        else:
            data_id =1
            for i in data:
                if i['id']> data_id:
                    data_id = i['id']
            data_id+=1
                
        click.echo(f'{name[0]} {name[1]} is added to the system, its ID = {data_id}')
        data_name=name[0]+" "+name[1]
        
        
        if course:
            data_course=courses[course-1]
            click.echo(f'You enrolled this course successfully "{data_course}"')
            

        if not course:
            click.secho(f"You didin't enroll yet, use 'update' to enroll..",fg='red')
        
        if email:
            data_email=email
            click.secho(f'Added an email: {data_email}',fg='green')
            
        if not email:
            data_email= "Not signed"
    
        new_student={
            'id':data_id,
            'name':data_name,
            'course':[data_course],
            'email': data_email
        }
        data.append(new_student)
        save(data)

    elif not name and (course or email):
        click.secho('Warning!',bold=True,blink=True,fg='red')
        click.secho('You have to enter name first!',fg='red')
        

@cli.command()
@click.option('--course','-c',help="Enroll an available course")
@click.option('--email','-e',help="Update the email info")
def update(course,email): #using id 
    pass

@cli.command()
@click.confirmation_option(prompt="Are you sure? You'll delete the student from the sys..")
def delete(): #using id -> we will create a file without the id you've chosen 
    pass

@cli.command()
def view(): 
    pass

@cli.command()
def info(): #maybe about the courses?
    click.secho("University Course Enrollment System",blink=True,fg='blue',bold=True)
    click.secho('Welcome to our System!',fg='green')
    click.echo("""Available courses in this term:
    1. Databases
    2. Computational Intelligence
    3. Data Structures
    4. Natural Language Processing
    5. Operating Systems
    6. Multi Agent Systems Design
    7. Computer Security""")
    click.secho('To choose a course, enter the NO. (e.g. 3)',fg='green')
    click.secho("Note: a student cannot be enrolled in the same course twice",fg='red')
    
    pass

# @cli.command()
# @click.option('--course','-c',help="Enroll an available course")
# def enroll(course):
#     click.echo(f'You enrolled this course successfully "{course}"')


if __name__=="__main__":
    cli()


#Possible problems :
#1. You can't enter more than one course in add function