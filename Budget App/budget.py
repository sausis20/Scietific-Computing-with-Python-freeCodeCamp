class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        text = self.category.center(30, '*') + "\n"
        for item in self.ledger:
            a = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            text += a +"\n"
        text += 'Total: ' + str(self.get_balance())
        return text
    
    def deposit(self, amount, description=''):
        temp = {}
        temp['amount'] = amount
        temp['description'] = description
        self.ledger.append(temp)
    
    
    def withdraw(self, amount, description=''):
        temp = {}
        if self.check_funds(amount):
            temp['amount'] = -amount
            temp['description'] = description
            self.ledger.append(temp)
            return True
        return False
        
        
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return(balance)
        
        
    def transfer(self, amount, expense_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + expense_cat.category)
            expense_cat.deposit(amount, "Transfer from " + self.category)
            return True
        return False
    
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    spend = []
    for category in categories:
        temp = 0
        for item in category.ledger: 
            if item['amount'] < 0:
                temp += abs(item['amount'])
        spend.append(temp)
    total = sum(spend)
    percentage = [i/total * 100 for i in spend]
    
    b = "Percentage spent by category"
    for i in range(100, -1, -10):
        b += "\n" + str(i).rjust(3) + "|"
        for a in percentage:
            if a > i:
                b += " o "
            else:
                b += "   "
        b += " "
    b += "\n" + "    "

    for i in percentage:
        b += "-"*3
    b += "-"
    
    cat_lenght = []
    for category in categories:
        cat_lenght.append(len(category.category))
    max_lenght = max(cat_lenght)
    
    for y in range(max_lenght):
        b += "\n    "
        for c in range(len(categories)):
            if y < cat_lenght[c]:
                b += " " + categories[c].category[y] + " "
            else:
                b += "   "
        b += " "

    return b