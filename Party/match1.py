import random, time

class party:
   
    def __init__(self):
        num_boys = 0
        num_girls = 0
    
    def boy_check_in(self):
        self.num_boys += 1
    
    def girl_check_in(self):
        self.num_girls += 1
    
    def boy_check_out(self):
        if(self.num_girls > 0): 
            self.num_boys -= 1
            party.girl_check_out(self)
    
    def girl_chek_out(self):
        self.num_girls -= 1

def participant_generator(name,gender,party):
   
    if(gender == 0):
        party.boy_check_in(name)
        
        yield    
    
    if(gender == 1):
        party.girl_check_in(name)
        yield
    
        rand = random.randint(0,1)
    
    if(party.num_boys > 0):
        party.boy_check_out(name)
        yield  
      
def main():
    p = party()
    
    num_boys = 0;
    num_girls = 0;

    participants = []
    for i in range(10):
        if random.randint(0,1) == 0:
            pg = participant_generator(i, True, p)
            num_boys += 10
        else:
            pg = participant_generator(i, False, p)
            num_girls += 10
        participants.append(pg)
        
    t0 = time.time()
    while len(participants) > 0 and time.time() - t0 < 1:
        task = random.choice(participants)
        try:
            task.next()
        except StopIteration:
            participants.remove(task)

    print 'boy enter: %s' %num_boys
    print 'girl enter: %s' %num_girls
    print 'pair: %s' %int(p.pair)

    assert min(num_boys, num_girls) == int(p.pair)
    
if __name__ == '__main__':
    main()