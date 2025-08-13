class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # self.mail=f'{self.name}@{self.age}.com'

    @property
    def mail(self):
        email=f'{self.name}@{self.age}.com'
        return email
    
    def update_mail(self,newname,newage):
        self.name=newname
        self.age=newage

emp=Employee('mohan',11)
print('mail',emp.mail)
emp.update_mail('ravi',34)
print('mail',emp.mail)
