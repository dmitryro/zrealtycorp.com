# User object
class User():
   def __init__(self,*args):
       self.name = args[0]

# Foobar object
class Foobar():
    # create a new Foobar
    def __init__(self,*args,**kwargs):
        self.raising = 0
        self.wire = 0
        self.reserved = 0

    def create(self,*args,**kwargs):
        if  args[0]=='raising':
            self.raising = args[1]
            print 'OK'

    # fund a foobar
    def fund(self):
        if (int(self.wire) < int(self.raising)):
             print 'Not enough money raised'
        else:
             print 'OK, Foobar funded'
        
    # wire and amount
    def wire_money(self,*args,**kwargs):
        self.user = args[0]
        self.wire = self.wire+int(args[1])
        print 'OK'

    # reserver
    def reserve_money(self,*args,**kwargs):
        self.user = args[0]
        self.reserved = args[1]
        print 'OK'


# Handle the input
def handle_input(foo,users):
    
    res = raw_input(">").split()

    if res[0] =='create':
        # Create a Foobar
        if res[1] == 'Foobar':
            transact = res[2] # read the transaction type
            amount = res[3] # read from console the amount
            foo.create(transact,amount)  # set a new raising deal
        # Create a user
        if res[1]  == 'user':
            u = User(res[2])
            print 'Created user '+u.name
            users[u.name]=u
         
    # User operation - wire, reserve and fund, to quit just type quit
    if res[0] == 'user':
        name = res[1]
         
        try:  # Brut force verify if the user exists        
            u = users[name]
        except:
            print 'User '+name+' does not exist!'

   
        if(res[2]=='wires'):  # wire some money
            amount = res[3]  
            foo.wire_money(name,amount)

        if(res[2]=='reserves'): # reserve some money
            amount = res[3] 
            foo.reserve_money(name,amount)
          
    # we try to fund - report an error if funding emount is not enough
    if res[0] == 'fund':
        foo.fund()

    # Quit
    if res[0]== 'quit':
        print 'Ok. Bye'
        exit()

def main():
   foo = Foobar()
   users = dict()
   while(True):
       handle_input(foo,users)

if __name__=="__main__":
    main()
