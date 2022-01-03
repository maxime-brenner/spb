# -*- coding: utf-8 -*-
import random

cards = { 
    "bucheron":{
        "name":"bucheron",
        "element":"bois",
        "cost":3,
        "ruble_gain":3,
        "vp_gain":0,
        "number_of_card":6,
        "type_card":"worker"    
        },	
 
    "tanneur":{
        "name":"tanneur",
        "element":"cuir",
        "cost":6,
        "ruble_gain":3,
        "vp_gain":0,
        "number_of_card":6,
        "type_card":"worker"
    	},

    "berger":{
        "name":"berger",
        "element":"laine",
        "cost":5,
        "ruble_gain":3,
        "vp_gain":0,
        "number_of_card":6,
        "type_card":"worker"
    	},

    "armateur":{
        "name":"armateur",
        "element":"bateau",
        "cost":7,
        "ruble_gain":3,
        "vp_gain":0,
        "number_of_card":6,
        "type_card":"worker"
        },

    "mineur":{
        "name":"mineur",
        "element":"laine",
        "cost":4,
        "ruble_gain":3,
        "vp_gain":0,
        "number_of_card":6,
        "type_card":"worker"
        },

    "empereur":{
        "name":"empereur",
        "element":"all",
        "cost":8,
        "ruble_gain":3,
        "vp_gain":0,
        "number_of_card":1,
        "type_card":"worker"
        },

    "ecrivain":{
        "name":"ecrivain",
        "element":None,
        "cost":1,
        "ruble_gain":4,
        "vp_gain":0,
        "number_of_card":6,
        "type_card":"noble"
        },

    "administrateur":{
        "name":"administrateur",
        "element":None,
        "cost":7,
        "ruble_gain":2,
        "vp_gain":0,
        "number_of_card":5,
        "type_card":"noble"
        },	

    "commis":{
        "name":"commis",
        "element":None,
        "cost":10,
        "ruble_gain":3,
        "vp_gain":0,
        "number_of_card":5,
        "type_card":"noble"
        },

    "secretaire":{
        "name":"secretaire",
        "element":None,
        "cost":12,
        "ruble_gain":4,
        "vp_gain":0,
        "number_of_card":4,
        "type_card":"noble"
        },	
    
    "controlleur":{
        "name":"controlleur",
        "element":None,
        "cost":14,
        "ruble_gain":4,
        "vp_gain":1,
        "number_of_card":3,
        "type_card":"noble"
        },
    
    "juge":{
        "name":"juge",
        "element":None,
        "cost":18,
        "ruble_gain":5,
        "vp_gain":2,
        "number_of_card":2,
        "type_card":"noble"
        },
    
    "maitresse_de_ceremonie":{
        "name":"maitresse de cérémmonie",
        "element":None,
        "cost":20,
        "ruble_gain":6,
        "vp_gain":3,
        "number_of_card":2,
        "type_card":"noble"
        },
}

class Card :

  def __init__(self, name, element, cost, ruble_gain, vp_gain, number_of_card, type_card):
    self.name=name
    self.element=element
    self.cost=cost
    self.ruble_gain=ruble_gain
    self.vp_gain=vp_gain
    self.number_of_card=number_of_card
    self.type_card=type_card
       
class GameInit:
    
    def __init__(self):
        self.worker=[]
        self.noble=[]
        self.first_row=[None]*8
        self.second_row=[None]*8
        self.prepare_pioche()
        self.generate_first_row()
    
    def prepare_pioche(self):
        #Récupération des données des cartes dans le fichier texte et transformation en dictionnaire
        for item in cards.items():
            for i in range(item[1]["number_of_card"]):
              w = Card(name=item[1]["name"], element=item[1]["element"], cost=item[1]["cost"], ruble_gain=item[1]["ruble_gain"], vp_gain=item[1]["vp_gain"], number_of_card=item[1]["number_of_card"], type_card=item[1]["type_card"])
              if w.type_card=="worker":
                  self.worker.append(w)
              elif w.type_card=="noble":
                  self.noble.append(w)
                  
            random.shuffle(self.worker)
            random.shuffle(self.noble)      
            
        return (self.worker,self.noble)
    
    def generate_first_row(self):
        for i in range(len(self.first_row)):    
            self.first_row[i]=self.worker[i]
            self.worker.pop(i)
        return(self.first_row)
        

class Player:  
    
    def __init__(self, ruble=25, vp_point=0, hand=[],lenght_hand=3, played_card=[]):
        self.ruble=ruble
        self.vp_point=vp_point
        self.hand=hand
        self.lenght_hand=lenght_hand
        self.played_card=played_card
        #self.make_choice()
        #self.take_card()
        #self.take_card_in_hand()
        
    def make_choice(self, row):
        selected=False
        while selected == False:
            
            card_choice=int(input ("Choisir une carte: "))
            try:
                card_choice in range(len(row))
                row[card_choice].name
                break
            except (AttributeError, IndexError):
                print("Veuillez choisir une carte disponible")
            except:
                print("Veuillez choisir une carte disponible")
                
    
        selected_card=row[card_choice]
        selected=True
            
        return (selected_card)
    
    def take_card(self, row):
        card=self.make_choice(row)
        if self.ruble - card.cost < 0:
          print("Vous n'avez pas assez d'argent !")  
        else:
            self.ruble=self.ruble-card.cost
            self.played_card.append(card)
            row[row.index(card)]=None
            i=1
        return(print(i), print(row), print(len(row)))
            
    def take_card_in_hand(self, row):
        try:
            self.hand<3
        except:
            "Votre main est pleine"

        card=self.make_choice(row)   

        if len(self.hand)==self.lenght_hand:
            print("Votre main est pleine")
        else:
            self.hand.append(card)
            del row[row.index(card)]
        
        return(print(self.hand))
        
    


          




     

    
    
   













