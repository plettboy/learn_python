#make a class
#e.g.
class User:
    #initialize a special function in a class
    def __init__(self, user_id, username):
        ('print new user being created..')
        #to set an object
        self.id = user_id
        self.username = username
#always include self so that it can call its paramters
    def follow(self, user):
        user.followers += 1
        self.following += 1



#long way, wrong way
user_1 = User()
user_1.id = '001'
user_1.username = 'angela'

#CLASS WAY OF CREATION
user_1 = User('001', 'angela')
print(user_1.id)
#THE OBJECT IS NOW CREATED FROM THE CLASS
#________________________________________

#Adding methods to a class
#see up






#to leave an empty function or class
def function()
    pass

class question:
  def quest_func(self, text, answer):
    self.text = text
    self.answer = answer


new_question = question('klfkldfs', 'true')
