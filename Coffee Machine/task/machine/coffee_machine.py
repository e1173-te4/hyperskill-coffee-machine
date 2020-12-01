class CoffeeMachine:
    def __init__(self):
        # operations
        self.BUY = 'buy'
        self.FILL = 'fill'
        self.TAKE = 'take'
        self.REMAINING = 'remaining'

        # starting status
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.action = None

        self.greetings(None)

    def get(self, string):
        if self.action == self.BUY:
            self.buy_coffee(string)
        elif self.action == self.FILL:
            self.fill_machine(string)
        elif self.action == self.TAKE:
            self.take_money(string)
        elif self.action == self.REMAINING:
            self.remaining()
        else:
            self.greetings(string)
        return string

    # def call_status(self, status):
    #     if status == self.BUY:
    #         self.buy_coffee()
    #     elif status == self.FILL:
    #         self.fill_machine()
    #     elif status == self.TAKE:
    #         self.take_money()
    #     elif status == self.REMAINING:
    #         self.remaining()
    #     return status

    def remaining(self):
        print(f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money
        ''')
        self.greetings(None)

    def greetings(self, string):
        print('Write action (buy, fill, take, remaining, exit):')
        self.action = string

    def operations(w=0, m=0, b=0, p=0, c=0, making_coffee=False):
        global water, milk, beans, money, cups
        water += w
        milk += m
        beans += b
        money += p
        cups += c
        if making_coffee:
            print('I have enough resources, making you a coffee!')

    def resources(w=0, m=0, b=0, c=0):
        if abs(w) > water:
            print('Sorry, not enough water!')
            return False
        elif abs(m) > milk:
            print('Sorry, not enough milk!')
            return False
        elif abs(b) > beans:
            print('Sorry, not enough beans!')
            return False
        elif abs(c) > cups:
            print('Sorry, not enough cups!')
            return False
        else:
            return True


    def buy_coffee():
        chosen = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if chosen == '1':
            if resources(w=-250, b=-16, c=-1):
                operations(w=-250, b=-16, p=4, c=-1, making_coffee=True)
        elif chosen == '2':
            if resources(w=-350, m=-75, b=-20, c=-1):
                operations(w=-350, m=-75, b=-20, p=7, c=-1, making_coffee=True)
        elif chosen == '3':
            if resources(w=-200, m=-100, b=-12, c=-1):
                operations(w=-200, m=-100, b=-12, p=6, c=-1, making_coffee=True)

    def fill_machine():
        operations(w=int(input('Write how many ml of water do you want to add: \n')))
        operations(m=int(input('Write how many ml of milk do you want to add: \n')))
        operations(b=int(input('Write how many grams of coffee beans do you want to add: \n')))
        operations(c=int(input('Write how many disposable cups of coffee do you want to add: \n')))

    def take_money():
        print(f'I gave you ${money}')
        operations(p=-money)


cm = CoffeeMachine()
while cm.get(input()) != 'exit':
    None


# while action != 'exit':
#     action = greetings()
#     if action == BUY:
#         buy_coffee()
#     elif action == FILL:
#         fill_machine()
#     elif action == TAKE:
#         take_money()
#     elif action == REMAINING:
#         remaining()
