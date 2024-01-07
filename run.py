class Person:
    def __init__(self, exists, has_chai):
        self.exists = exists
        self.has_chai = has_chai
    
    def drink_chai(self):
        self.has_chai = False
    
    def ask_about_chai(self):
        chai_q = input('chai good?')
        return chai_q
        
vova = Person(True, False)
ana = Person(True, True)
    
def vkusniy_chai():
    answer = vova.ask_about_chai()
    if ana.has_chai and answer == 'da':
        vova.has_chai = True
        print('vova pyot chai')
    else:
        print('vova gets no chai')
        
vkusniy_chai()