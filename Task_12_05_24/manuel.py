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
    elif 0 < value_1_0 < 3 :
        for element in range(value_1_0):
            bucket_1.pop(0)
            bucket_1.append(1)
    
    
        
    
def generate_first_bucket ():
    roll_first = random.randint(0, 3)
    rolls.append(roll_first)
    for element in range(roll_first):
        bucket_1.append(0)
    roll_1 = 3-roll_first
    for element in range(roll_1):
        bucket_1.append(1) 
    
    
        
        
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
    
     
       
def generate_second_bucket ():
    roll_second = random.randint(0, 5)
    rolls.append(roll_second)
    for element in range (roll_second):
        bucket_2.append(0)
    roll_2 = 5-roll_second
    for element in range (roll_2):
        bucket_2.append(1)
    
   



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
    
       
    
def generate_third_bucket ():
    roll_third = random.randint(0,9)
    rolls.append(roll_third)
    for element in range (roll_third):
        bucket_3.append(0)
    roll_3 = 9-roll_third
    for element in range(roll_3):
        bucket_3.append(1)
    


#1-2------------------------------- işlemler ----------------
    
def bucket_1_to_2 ():
    value_11_ = bucket_1.count(1)
    value_20_ = bucket_2.count(0)
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
            placement = bucket_1.index(1)
            placement_0 = bucket_2.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_2.pop(placement_0)
            bucket_2.append(1)
            
    else :
        print("error_bucket1__to_2")

def bucket_1_to_2_out ():
    value_11_ = bucket_1.count(1)
    value_20_ = bucket_2.count(0)
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
            placement = bucket_1.index(1)
            placement_0 = bucket_2.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_2.pop(placement_0)
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
            placement = bucket_1.index(1)
            placement_0 = bucket_3.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_3.pop(placement_0)
            bucket_3.append(1)
            
    else :
        print("error_bucket1__to_3")

def bucket_1_to_3_out ():
    value_11_ = bucket_1.count(1)
    value_30_ = bucket_3.count(0)
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
            placement = bucket_1.index(1)
            placement_0 = bucket_3.index(0)
            bucket_1.pop(placement)
            bucket_1.append(0)
            bucket_3.pop(placement_0)
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
            placement_0 = bucket_1.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_1.pop(placement_0)
            bucket_1.append(1)
            
    else :
        print("error_bucket_2_to_1")

def bucket_2_to_1_out ():
    value_10_ = bucket_1.count(0)
    value_21_ = bucket_2.count(1)
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
            placement_0 = bucket_1.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_1.pop(placement_0)
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
            placement_0 = bucket_3.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_3.pop(placement_0)
            bucket_3.append(1)
            
    else :
        print("error_bucket_2_to_1")

def bucket_2_to_3_out ():
    value_30_ = bucket_3.count(0)
    value_21_ = bucket_2.count(1)
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
            placement_0 = bucket_3.index(0)
            bucket_2.pop(placement)
            bucket_2.append(0)
            bucket_3.pop(placement_0)
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
            placement_0 = bucket_1.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_1.pop(placement_0)
            bucket_1.append(1)
            
    else :
        print("error_bucket_3_to_1")

def bucket_3_to_1_out ():
    value_10_ = bucket_1.count(0)
    value_31_ = bucket_3.count(1)
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
            placement_0 = bucket_1.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_1.pop(placement_0)
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
            placement_0 = bucket_2.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_2.pop(placement_0)
            bucket_2.append(1)
            
    else :
        print("error_bucket_3_to_2")

def bucket_3_to_2_out ():
    value_20_ = bucket_2.count(0)
    value_31_ = bucket_3.count(1)
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
            placement_0 = bucket_2.index(0)
            bucket_3.pop(placement)
            bucket_3.append(0)
            bucket_2.pop(placement_0)
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
    
    # bucket_1_empty()
    # bucket_2_empty()
    # bucket_3_empty()
    print("")

def bucket_1_empty ():
    bucket_1.clear()
    for element in range(3):
        bucket_1.append(0)

def bucket_2_empty ():
    bucket_2.clear()
    for element in range(5):
        bucket_2.append(0)
    
def bucket_3_empty ():
    bucket_3.clear()
    for element in range(9):
        bucket_3.append(0)

#--------------------------------------------------------------------r.generator & choice_maker

def choice_maker ():
    if True :
        
        if bucket_1.count(1) == 7 - bucket_3.count(1) :
            bucket_1_to_3_out()
        elif bucket_2.count(1) == 7 - bucket_3.count(1):
            bucket_2_to_3_out()
        elif bucket_1.count(1) + bucket_2.count(1) == 7 - bucket_3.count(1):
            bucket_1_to_2_out()
            bucket_1_to_3_out()    
        elif bucket_1.count(0) == 7 -bucket_3.count(1):
            bucket_3_to_1_out()
        elif bucket_2.count(1) == 7 -bucket_3.count(1):
            bucket_3_to_2_out()
        elif bucket_1.count(0) + bucket_2.count(0) == 7 -bucket_3.count(1):
            bucket_3_to_1_out()
            bucket_3_to_2_out()
        # elif bucket_1.count(1) < bucket_2.count(1) and bucket_2.count(1) - bucket_1.count(0) == 7 - bucket_3.count(1) and bucket_3.count(1) != 7 and bucket_2.count(1) - bucket_1.count(0) > 0:
        #     bucket_1_to_2_out()
        #     while bucket_3.count(1) != 7:
        #         if bucket_2.count(1) >= bucket_3.count(0) and bucket_2.count(1) > 0 and bucket_3.count(0) > 0 :
        #             index_2 = bucket_2.index(1)
        #             bucket_2.pop(index_2)
        #             bucket_2.append(0)
        #             for element in range(bucket_3.count(0)):
        #                 index_3 = bucket_3.index(0)
        #                 bucket_3.pop(index_3)
        #                 bucket_3.append(1)                                                                                                                                                               
        #             break
        #         elif bucket_3.count(0) > bucket_2.count(1):
        #             index_2 = bucket_2.index(1)
        #             bucket_2.pop(index_2)
        #             bucket_2.append(0)
        #             for element in range(bucket_2.count(1)):
        #                 index_3 = bucket_3.index(0)
        #                 bucket_3.pop(index_3)
        #                 bucket_3.append(1)   
        #             break
        #         else :
        #             print("Hata_kodu_erdem")
        # elif first_bucket.count(1) > second_bucket.count(1) and first_bucket.count(1) - (5 - second_bucket.count(1)) == 7 - third_bucket.count(1) and third_bucket.count(1) != 7 and first_bucket.count(1) - (5 - second_bucket.count(1)) > 0:
    
    
def random_generator ():
    while bucket_3.count(1) != 7:
        zar = random.randint(1, 12)
        
        if zar == 1:
            if bucket_1.count(1) == 3:
                continue
            fill_first_bucket()
        elif zar == 2:
            if bucket_2.count(1) == 5:
                continue
            fill_second_bucket()
        elif zar == 3:
            if bucket_3.count(1) == 9:
                continue
            fill_third_bucket()
        elif zar == 4:
            if bucket_1.count(1) == 0:
                continue
            bucket_1_empty()
        elif zar == 5:
            if bucket_2.count(1) == 0 :
                continue
            bucket_2_empty() 
        elif zar == 6:
            if bucket_3.count(1) == 0:
                continue
            bucket_3_empty()
        elif zar == 7:
            if bucket_1.count(1) == 0 or bucket_2.count(1) == 5:
                continue
            bucket_1_to_2()
        elif zar == 8:
            if bucket_1.count(1) == 0 or bucket_3.count(1) == 9:
                continue
            bucket_1_to_3()
        elif zar == 9:
            if bucket_2.count(1) == 0 or bucket_1.count(1) == 1:
                continue
            bucket_2_to_1()
        elif zar == 10:
            if bucket_2.count(1) == 0 or bucket_3.count(1) == 9:
                continue
            bucket_2_to_3()
        elif zar == 11:
            if bucket_3.count(1) == 0 or bucket_1.count(1) == 3:
                continue
            bucket_3_to_1()
        elif zar == 12:
            if bucket_3.count(1) == 0 or bucket_2.count(1) == 5:
                continue
            bucket_3_to_2()
        choice_maker()
        global stage
        stage += 1
        if bucket_3.count(1) == 7:
            break

#--------------------------------------------------------------------start_of_choose_sequence
tryed = 0
stage = 0
while tryed != 1000 :
    tryed += 1
    
    bucket_1.clear()
    bucket_2.clear()
    bucket_3.clear()
    rolls.clear()
    
    generate_first_bucket()
    generate_second_bucket()
    generate_third_bucket()
    	
    
    choice_maker()
    random_generator()
    
print(f"total {stage} adımda çözüldü")
print("İşlem 1000 kere yapıldı sonuç:")
print(stage/tryed)        
    
kova_1_last = bucket_1.count(1)
kova_2_last = bucket_2.count(1)
kova_3_last = bucket_3.count(1)	
    
print(f"Son durum :\n1.Kova : {bucket_1} = {kova_1_last}\n2.Kova: {bucket_2} = {kova_2_last}\n3.Kova: {bucket_3} = {kova_3_last}")
    

print(f"Sırası ile 1.nci , 2.nci ve 3.ncü kova için atılan zarlar {rolls}\n\n\n")


      
        