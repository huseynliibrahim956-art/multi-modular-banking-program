#main part
import numpy as np
runnin=True
registered=False
added_money=False
print('_______BANKING-PROGRAM______')
while runnin:
    print('1.registration')
    print('2.your card')
    print('3.deposit')
    print('4.our best workers workers')
    print('_________________________')
    user=input('welcome to our banking site pls enter a num')
    print('________________________________________________')
    if user.isdigit():
        user=int(user)
        match user:
            case 1:
                    import registration as r
                    print('------INFORMATIONS--------')
                    user11_dict={
                        'name':r.user1.name,
                        'phone number':r.user1.phone_num,
                        'country':r.user1.country,
                        'card type':r.user1.card_type,
                        'via code':r.user1.via_code
                        }
                    print('-----------------------------')
                    for key,value in user11_dict.items():
                        print(f'{key}:{value}')
                    registered=True
            case 2:
                if not registered:
                    print('you didnt register yet')
                elif registered:
                    if added_money:
                     import card as cd
                    elif added_money==False:
                        print(f'{r.user1.name},{r.user1.via_code} balance:${0}')
            case 3:
                if not registered:
                    print('you didnt register yet')
                elif registered:
                 import deposit as dp
                 added_money=True
            case 4:
                import workers as wr
            case val if val>=5 or val<=0:
                print('the num was expected to be between 1-4 included')
                print('-------------------------------------------------')
                pass
    else:
        pass