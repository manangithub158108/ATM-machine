import random

class ATM():
    def __init__(self, card_number, pin_number):
        self.card_num = card_number
        self.pin_num = pin_number

        def Balance_enquiry():
            print('The balance enquiry has been sent for approval');

        def CashWithDrawal():

            if card_num == '' and pin_num is '':
                print('You are not approved');
            else:
                print('You are successfully approved');

            money_input = input('Please enter how much money do you want >>> ');
            
            if money_input == '':
                print('Plesse enter some money next time you run it')
            else:
                print('You have recieved the money in your bank account');

        Balance_enquiry();
        CashWithDrawal();

card_num = input('Please enter your card no. >>> ');
pin_num = input('Please write your pin number >>> ');
            
atm = ATM(card_num, pin_num);
