class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.mail=f'{self.name}@{self.age}.com'
        
    def mail(self):
        self.mail=f'{self.name}@{self.age}.com'
        return self.mail