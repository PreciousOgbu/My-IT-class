 # Create a tuple containing the names of your brothers and sisters 

def family_tuple():
    brothers = ("Chidi", "Onyi", "Ugo", "Kc", "Nonso")
    sisters = ("Confi", "Mira", "ND", "Dabby", "JJ")
    siblings = brothers + sisters
    print(len(siblings))
    print(f"My siblings are {siblings}")
    
    # Modifying to add mother and father
    # father = ("Daniel")
    # mother = ("Helen")
    parents = ("Daniel", "Helen")
    family_members =  parents + siblings 
    print (len(family_members))
    print (f'These are my family members {family_members}')

 # Unpacking siblings 
    siblings = family_members [2:12] 
    print (f'Unpacking my siblings {siblings} from family members')

    # Unpacking parents
    parents = family_members[:2]
    return f'Unpacking my parents {parents} from family members'
    




  
print(family_tuple()) 




