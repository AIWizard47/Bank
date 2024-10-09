count = 0
pinstore = 1234
balance = 10000
while True:
    print('Hello IES Bank')
    pin = int(input('Please Enter your Pin: '))
    if pin != pinstore:
        count +=1
        if count==2:
            print('Wrong Password')
        elif count==3:
            print('You are Block by Ies Bank Please Contact to bank!!')
            break
        continue
    else:
        print('Enter a your choice')
        
        while True:
            print('1. Balance Inquiry')
            print('2. withdraw')
            print('3. Mini Statement')
            print('4. Pin Change')
            
            ch = int(input(': > '))
            if ch==1 or ch==3:
                print(f"Your Balance is Rs.{balance}")
                break
            if ch==2:
                w = int(input("Please Enter withdrawal Money: "))
                if balance<5000:
                    print('You Have insufficient Balance')
                else:
                    if w<=balance:
                        balance -= w
                    print(f"You recieved {w} Amount and left {balance}")
                break
            if ch==4:
                p = int(input("Please Enter Your New pin: "))
                pinstore = p
                print("New Pin updated Successfully.")
                break
                
            
            
    
