import random
bucket_1 = []
bucket_2 = []
bucket_3 = []
rolls = []
def fill_first_bucket ():
    value_1_0 = bucket_1.count(0)
    value_1_1 = bucket_1.count(1)
    if value_1_0 == 3:
        bucket_1.clear()
        for element in range(3):
            bucket_1.append(1)
    elif value_1_1 == 3:
        pass
    elif 0 < value_1_0 <3 :
        for element in range(value_1_0):
            bucket_1.pop(0)
            bucket_1.append(1)
    bucket_1_water = bucket_1.count(1)
    print(f"1.nci kovadaki fill sonrası su : {value_1_1} ⟶ {bucket_1_water}")   
        
    
def generate_first_bucket ():
    roll_first = random.randint(0, 3)
    rolls.append(roll_first)
    for element in range(roll_first):
        bucket_1.append(0)
    roll_1 = 3-roll_first
    for element in range(roll_1):
        bucket_1.append(1) 
    bucket_1_water = bucket_1.count(1)
    print(f"1.nci kovadaki mevcut su : {bucket_1_water}")
        
        
def fill_second_bucket ():
    value_2_0 = bucket_2.count(0)
    value_2_1 = bucket_2.count(1)
    if value_2_0 == 5 :
        bucket_2.clear()
        for element in range(5):
            bucket_2.append(1)
    elif value_2_1 == 5:
        pass
    elif 0 < value_2_0 < 5 :
        for element in range(value_2_0):
            bucket_2.pop(0)
            bucket_2.append(1)
    bucket_2_water = bucket_2.count(1)
    print(f"2.nci kovadaki fill sonrası su : {value_2_1} ⟶ {bucket_2_water}") 
       
def generate_second_bucket ():
    roll_second = random.randint(0, 5)
    rolls.append(roll_second)
    for element in range (roll_second):
        bucket_2.append(0)
    roll_2 = 5-roll_second
    for element in range (roll_2):
        bucket_2.append(1)
    bucket_2_water = bucket_2.count(1)
    print(f"2.nci kovadaki mevcut su : {bucket_2_water}")



def fill_third_bucket ():
    
    value_3_0 = bucket_3.count(0)
    value_3_1 = bucket_3.count(1)
    
    if value_3_0 == 9:
        bucket_3.clear()
        for element in range(9):
            bucket_3.append(1)
    elif value_3_1 == 9:
        pass
    elif 0 < value_3_0 < 9 :
        for element in range(value_3_0):
            bucket_3.pop(0)
            bucket_3.append(1)
    bucket_3_water = bucket_3.count(1)
    print(f"3.ncü kovadaki fill sonrası su : {value_3_1} ⟶ {bucket_3_water}")     
    
def generate_third_bucket ():
    roll_third = random.randint(0,9)
    rolls.append(roll_third)
    for element in range (roll_third):
        bucket_3.append(0)
    roll_3 = 9-roll_third
    for element in range(roll_3):
        bucket_3.append(1)
    bucket_3_water = bucket_3.count(1)
    print(f"3.ncü kovadaki mevcut su : {bucket_3_water}")


#1-2------------------------------- işlemler ----------------
    
def bucket_1_to_2 ():
    value_11_ = bucket_1.count(1)
    value_20_ = bucket_2.count(0)
    print(f"1.nci kovadaki {value_11_} litre su 2.nci kovaya alabildiği kadar koyuldu ")
    if value_20_ >= value_11_ :
        for element in range(value_11_): 
            placement = bucket_1.index(1)
            placement_0 = bucket_2.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_2.pop(placement_0)
            bucket_2.append(1)
            
    elif  value_20_ < value_11_ :
        for element in range(value_20_):
            bucket_1.pop(1)
            bucket_1.append(0)
            bucket_2.pop(0)
            bucket_2.append(1)
            
    else :
        print("error_bucket1__to_2")

def bucket_1_to_2_out ():
    value_11_ = bucket_1.count(1)
    value_20_ = bucket_2.count(0)
    print(f"1.nci kovadaki {value_11_} litre su 2.nci kova'nın üzerine döküldü  ")
    if value_20_ >= value_11_ :
        for element in range(value_11_): 
            placement = bucket_1.index(1)
            placement_0 = bucket_2.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_2.pop(placement_0)
            bucket_2.append(1)
        bucket_1.clear()
        for element in range(3):
            bucket_1.append(0)
            
    elif  value_20_ < value_11_ :
        for element in range(value_20_):
            bucket_1.pop(1)
            bucket_1.append(0)
            bucket_2.pop(0)
            bucket_2.append(1)
        bucket_1.clear()
        for element in range(3):
            bucket_1.append(0)
            
        
    else :
        print("error_bucket1__to_2")

#1-3-------------------------------------------------

def bucket_1_to_3 ():
    value_11_ = bucket_1.count(1)
    value_30_ = bucket_3.count(0)
    print(f"1.nci kovadaki {value_11_} litre su 3.ncü kovaya alabildiği kadar koyuldu ")
    if value_30_ >= value_11_ :
        for element in range(value_11_): 
            placement = bucket_1.index(1)
            placement_0 = bucket_3.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_3.pop(placement_0)
            bucket_3.append(1)
            
    elif  value_30_ < value_11_ :
        for element in range(value_30_):
            bucket_1.pop(1)
            bucket_1.append(0)
            bucket_3.pop(0)
            bucket_3.append(1)
            
    else :
        print("error_bucket1__to_3")

def bucket_1_to_3_out ():
    value_11_ = bucket_1.count(1)
    value_30_ = bucket_3.count(0)
    print(f"1.nci kovadaki {value_11_} litre su 3.ncü kova üzerine döküldü ")
    if value_30_ >= value_11_ :
        for element in range(value_11_): 
            placement = bucket_1.index(1)
            placement_0 = bucket_3.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_3.pop(placement_0)
            bucket_3.append(1)
        bucket_1.clear()
        for element in range(3):
            bucket_1.append(0)
            
    elif  value_30_ < value_11_ :
        for element in range(value_30_):
            bucket_1.pop(1)
            bucket_1.append(0)
            bucket_3.pop(0)
            bucket_3.append(1)
        bucket_1.clear()
        for element in range(3):
            bucket_1.append(0)
            
    else :
        print("error_bucket1__to_3")

#2-1-------------------------------------------------
        
def bucket_2_to_1 ():
    value_10_ = bucket_1.count(0)
    value_21_ = bucket_2.count(1)
    print(f"2.nci kovadaki {value_21_} litre su 1.nci kovaya alabildiği kadar koyuldu ")
    if value_21_ <= value_10_ :
        for element in range(value_21_): 
            placement = bucket_2.index(1)
            placement_0 = bucket_1.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_1.pop(placement_0)
            bucket_1.append(1)
            
    elif  value_21_ > value_10_ :
        for element in range(value_10_):
            placement = bucket_2.index(1)
            bucket_2.append(0)
            bucket_1.pop(0)
            bucket_1.append(1)
            
    else :
        print("error_bucket_2_to_1")

def bucket_2_to_1_out ():
    value_10_ = bucket_1.count(0)
    value_21_ = bucket_2.count(1)
    print(f"2.nci kovadaki {value_21_} litre su 1.nci kova'nın üzerine döküldü ")
    if value_21_ <= value_10_ :
        for element in range(value_21_): 
            placement = bucket_2.index(1)
            placement_0 = bucket_1.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_1.pop(placement_0)
            bucket_1.append(1)
        bucket_2.clear()
        for element in range(5):
            bucket_2.append(0)
        
            
    elif  value_21_ > value_10_ :
        for element in range(value_10_):
            placement = bucket_2.index(1)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_1.pop(0)
            bucket_1.append(1)
        bucket_2.clear()
        for element in range(5):
            bucket_2.append(0)
            
    else :
        print("error_bucket_2_to_1")
        
#2-3-------------------------------------------------

def bucket_2_to_3 ():
    value_30_ = bucket_3.count(0)
    value_21_ = bucket_2.count(1)
    print(f"2.nci kovadaki {value_21_} litre su 3.ncü kovaya alabildiği kadar koyuldu ")
    if value_21_ <= value_30_ :
        for element in range(value_21_): 
            placement = bucket_2.index(1)
            placement_0 = bucket_3.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_3.pop(placement_0)
            bucket_3.append(1)
            
    elif  value_21_ > value_30_ :
        for element in range(value_30_):
            placement = bucket_2.index(1)
            bucket_2.append(0)
            bucket_3.pop(0)
            bucket_3.append(1)
            
    else :
        print("error_bucket_2_to_1")

def bucket_2_to_3_out ():
    value_30_ = bucket_3.count(0)
    value_21_ = bucket_2.count(1)
    print(f"2.nci kovadaki {value_21_} litre su 3.ncü kova'nın üzerine döküldü ")
    if value_21_ <= value_30_ :
        for element in range(value_21_): 
            placement = bucket_2.index(1)
            placement_0 = bucket_3.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_3.pop(placement_0)
            bucket_3.append(1)
        bucket_2.clear()
        for element in range(5):
            bucket_2.append(0)
            
    elif  value_21_ > value_30_ :
        for element in range(value_30_):
            placement = bucket_2.index(1)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_3.pop(0)
            bucket_3.append(1)
        bucket_2.clear()
        for element in range(5):
            bucket_2.append(0)
            
    else :
        print("error_bucket_2_to_1")
        
#3-1-------------------------------------------------

def bucket_3_to_1 ():
    value_10_ = bucket_1.count(0)
    value_31_ = bucket_3.count(1)
    print(f"3.ncü kovadaki {value_31_} litre su 1.nci kovaya alabildiği kadar koyuldu ")
    if value_31_ <= value_10_ :
        for element in range(value_31_): 
            placement = bucket_3.index(1)
            placement_0 = bucket_1.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_1.pop(placement_0)
            bucket_1.append(1)
    elif  value_31_ > value_10_ :
        for element in range(value_10_):
            placement = bucket_3.index(1)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_1.pop(0)
            bucket_1.append(1)
            
    else :
        print("error_bucket_3_to_1")

def bucket_3_to_1_out ():
    value_10_ = bucket_1.count(0)
    value_31_ = bucket_3.count(1)
    print(f"3.ncü kovadaki {value_31_} litre su 1.nci kova'nın üzerine döküldü")
    if value_31_ <= value_10_ :
        for element in range(value_31_): 
            placement = bucket_3.index(1)
            placement_0 = bucket_1.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_1.pop(placement_0)
            bucket_1.append(1)
        bucket_3.clear()
        for element in range(9):
            bucket_3.append(0)
            
    elif  value_31_ > value_10_ :
        for element in range(value_10_):
            placement = bucket_3.index(1)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_1.pop(0)
            bucket_1.append(1)
        bucket_3.clear()
        for element in range(9):
            bucket_3.append(0)
            
    else :
        print("error_bucket_3_to_1")
    
#3-2-------------------------------------------------   
    
def bucket_3_to_2 ():
    value_20_ = bucket_2.count(0)
    value_31_ = bucket_3.count(1)
    print(f"3.ncü kovadaki {value_31_} litre su 2.nci kovaya alabildiği kadar koyuldu ")
    if value_31_ <= value_20_ :
        for element in range(value_31_): 
            placement = bucket_3.index(1)
            placement_0 = bucket_2.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_2.pop(placement_0)
            bucket_2.append(1)
            
    elif  value_31_ > value_20_ :
        for element in range(value_20_):
            placement = bucket_3.index(1)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_2.pop(0)
            bucket_2.append(1)
            
    else :
        print("error_bucket_3_to_2")

def bucket_3_to_2_out ():
    value_20_ = bucket_2.count(0)
    value_31_ = bucket_3.count(1)
    print(f"3.ncü kovadaki {value_31_} litre su 2.nci kova'nın üzerine döküldü")
    if value_31_ <= value_20_ :
        for element in range(value_31_): 
            placement = bucket_3.index(1)
            placement_0 = bucket_2.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_2.pop(placement_0)
            bucket_2.append(1)
        bucket_3.clear()
        for element in range(9):
            bucket_3.append(0)
    elif  value_31_ > value_20_ :
        for element in range(value_20_):
            placement = bucket_3.index(1)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_2.pop(0)
            bucket_2.append(1)
        bucket_3.clear()
        for element in range(9):
            bucket_3.append(0)   
    else :
        print("error_bucket_3_to_2")

#--------------------------------------------------------------------alldone...
def useable_commands ():
    # generate_first_bucket()
    # generate_second_bucket()
    # generate_third_bucket()
    
    # bucket_1_to_2()
    # bucket_1_to_2_out()
    # bucket_1_to_3()
    # bucket_1_to_3_out()

    # bucket_2_to_1()
    # bucket_2_to_1_out()
    # bucket_2_to3()
    # bucket_2_to3_out()

    # bucket_3_to_1()
    # bucket_3_to_1_out()
    # bucket_3_to_2()
    # bucket_3_to_2_out()
    print("")

def bucket_1_empty ():
    bucket_1.clear()
    for element in range(3):
        bucket_1.append(0)
    print("1.nci kova boşaltıldı")

def bucket_2_empty ():
    bucket_2.clear()
    for element in range(5):
        bucket_2.append(0)
    print("2.nci kova boşaltıldı")
    
def bucket_3_empty ():
    bucket_3.clear()
    for element in range(9):
        bucket_3.append(0)
    print("3.ncü kova boşaltıldı")

#--------------------------------------------------------------------start_of_choose_sequence


generate_first_bucket()
generate_second_bucket()
generate_third_bucket()
print(bucket_1)
print(bucket_2)
print(bucket_3)
bucket_3_empty()
print(bucket_1)
print(bucket_2)
print(bucket_3)
fill_second_bucket()
print(bucket_1)
print(bucket_2)
print(bucket_3)
bucket_1_to_3_out()
print(bucket_1)
print(bucket_2)
print(bucket_3)
bucket_2_to_3_out()
print(bucket_1)
print(bucket_2)
print(bucket_3)
print(f" \nSırası ile 1.nci , 2.nci ve 3.ncü kova için atılan zarlar {rolls}")





      
        