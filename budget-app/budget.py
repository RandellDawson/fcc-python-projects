import math

class Category:
    
    def __init__(self, category):
        self.name = category
        self.ledger = []
        
    def __repr__(self):
        number_left_stars = 15 - math.ceil(len(self.name) / 2)
        number_right_stars = 30 - number_left_stars - len(self.name)
        header = f"{number_left_stars * '*'}{self.name}{number_right_stars * '*'}\n"
        items = ""
        total = 0
        for item in self.ledger:
            currency = ("%.2f" % item['amount'])
            padded_amount = currency.rjust(7, ' ')
            items += f"{item['description'][:23].ljust(23, ' ')}{padded_amount}\n"
            total += item['amount']
        return header + items + f"Total: {('%.2f' % total)}"
        
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
        
    def get_balance(self):
        return sum(transaction['amount'] for transaction in self.ledger)

    def transfer(self, amount, transfer_to_category):
        if self.check_funds(amount):
            description =  "Transfer to " + transfer_to_category.name
            self.withdraw(amount, description)
            description = "Transfer from " + self.name
            transfer_to_category.deposit(amount, description)
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
def create_spend_chart(categories):
    summary = []
    total = 0
    final = []
    final.append(['1'])
    col = ['0']
    col.extend([str(x) for x in list(range(9, 0, -1))])
    col.append(' ')
    final.append(col)
    final.append(['0'] * 11)
    final.append(['|'] * 11)
    final.append(blank_col())

    for cat in categories:
        ledger = cat.ledger
        subtotal = 0
        for trans in ledger:
            amount = trans['amount'] 
            if amount < 0:
                subtotal += -1 * amount
        total += subtotal
        summary.append([cat.name, subtotal])
        final.append([])
        final.append(blank_col())
        final.append(blank_col())

    index_offset = 0
    for index, category_details in enumerate(summary):
        data = [' '] * 11
        name, subtotal = category_details
        percent = 100 * ( subtotal / total)
        rounded = math.floor(percent / 10) * 10
        for data_index, item in enumerate(data):
            if (rounded >= data_index * 10):
                data[data_index] = 'o'
        data.reverse()
        data.append('-')
        data.extend(list(name))
        final[index + 5 + index_offset].extend(data)
        index_offset += 2
    
    padding = len(max(final, key=len))
    padded_list = [item + [' ']*(padding - len(item)) for item in final]
    transposed_list = list(zip(*padded_list))
    title = "Percentage spent by category\n"
    chart_data = '\n'.join([''.join([str(cell) for cell in row]) for row in transposed_list])
    return title + chart_data
    
def blank_col():
    col = [' '] * 11
    col.append('-')
    return col