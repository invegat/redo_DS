import random

class  Product:
  def __init__(self, name, price=10, weight=20, flammablility=0.5):
    self.name = name
    self.price=price
    self.weight= weight
    self.flammablility = flammablility
    self.identifier = random.randint(1000000 , 9999999)
    def __str__(self):
        return "|%g/t|%g/t|%g/t|%g/t|%g/t| "%(self.name, self.price, self.weight,self.flammablility, self.identifier)
    
  def  stealability(self):
    return  " Very stealable!" if  self.price/self.weight   <  0.5 else  ( "Not so stealable..."  if  self.price/self.weight  >= 1 else  "Kinda stealable")
  def  explode(self):
    return  "...fizzle."  if    self.flammablility *  self.weight   <  10 else  ( "...BABOOM!!" if  self.flammablility * self.weight  >  50  else  "..boom!")

class  BoxingGlove(Product):
  def __init__(self, name, price=10, weight=10, flammablility=0.5):
     super().__init__(name,price,weight,flammablility)
    
  def  explode(self):
    return  "...it's a glove."
    
  def punch(self):
    return  "That tickles."  if    self.weight   <  5 else  (  "OUCH!"  if  self.weight  >=  15  else "Hey that hurt!'")          


""""
 11/2  The number for our credit Management team is 1-(888) 302-9291(TTY/TDD: 1-800-325-2865). This department is available everyday of the week from 9am-10pm ES

""""
      
        
  
