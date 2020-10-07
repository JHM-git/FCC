

class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    added_object = {
      "amount": amount,
      "description": description
    }
    self.ledger.append(added_object)

  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    else:
      return False
  
  def withdraw(self, amount, description=''):
    negative_amount = 0 - amount
    added_object = {
      "amount": negative_amount,
      "description": description
    }
    if self.check_funds(amount):
      self.ledger.append(added_object)
      return True
    else:
      return False

  def get_balance(self):
    funds = 0
    for obj in self.ledger:
      funds = funds + obj["amount"]
    return funds

  def transfer(self, amount, category):
    withdraw_msg = "Transfer to " + category.name
    deposit_msg = "Transfer from " + self.name
    if amount <= self.get_balance():
      self.withdraw(amount, withdraw_msg)
      category.deposit(amount, deposit_msg)
      return True
    else:
      return False

  def __repr__(self):
    blank = ' '
    asterix = '*'
    newline = '\n'
    receipt = ''
    if len(self.name) % 2 == 0:
      receipt = receipt + int((30-len(self.name)) / 2) * asterix + self.name + int((30-len(self.name)) / 2) * asterix + newline
    else:
      receipt = receipt + int((30-len(self.name)-1) / 2 + 1) * asterix + self.name + int((30-len(self.name)-1) / 2) * asterix + newline
    description = ''
    amount = ''
    for item in self.ledger:
      description = item['description']
      amount = str(format(float(item['amount']), '.2f'))
      receipt = receipt + description[:23] + (23-len(description)) * blank + (7-len(amount)) * blank + amount[:7] + newline
    total = str(format(self.get_balance(), '.2f'))
    receipt = receipt + 'Total: ' + total
    return receipt

def create_spend_chart(categories):
  spent_by_cgory = []
  for category in categories:
    category_spend = 0
    for item in category.ledger:
      if item['amount'] < 0:
        category_spend = category_spend + item['amount'] * -1
    spent_by_cgory.append(category_spend)
  total_spent = 0
  for item in spent_by_cgory:
    total_spent = total_spent + item
  spend_precentages = []
  spend_precentage = 0
  for item in spent_by_cgory:
    spend_precentage = int(item / total_spent * 100)
    spend_precentages.append(spend_precentage)
  spend_dicts = []
  spend_dict = {}
  for i in range(len(categories)):
    spend_dict = {
      'category': categories[i].name,
      'spend': spend_precentages[i]
    }
    spend_dicts.append(spend_dict)
  newline = '\n'
  blank = ' '
  dash = '-'
  output = 'Percentage spent by category' + newline
  lines =[{'value': 100, 'line': '100| '}, {'value': 90, 'line': ' 90| '}, {'value': 80, 'line': ' 80| '}, 
  {'value': 70, 'line': ' 70| '}, {'value': 60, 'line': ' 60| '}, {'value': 50, 'line': ' 50| '}, {'value': 40, 'line': ' 40| '},
  {'value': 30, 'line': ' 30| '}, {'value': 20, 'line': ' 20| '}, {'value': 10, 'line': ' 10| '}, {'value': 0, 'line': '  0| '}]
  for spend in spend_dicts:
    for line in lines:
      if spend['spend'] >= line['value']:
        line['line'] = line['line'] + 'o  '
      else:
        line['line'] = line['line'] + '   '
  for line in lines:
    output = output + line['line'] + newline
  dashline = '    ' + (len(spend_dicts) * 3 + 1) * dash + newline
  output = output + dashline
  category_max_len = 0
  for item in spend_dicts:
    if len(item['category']) > category_max_len:
      category_max_len = len(item['category'])
  equal_len_categories = []
  equal_str = ''
  for item in spend_dicts:
    equal_str = item['category'] + (category_max_len - len(item['category'])) * blank
    equal_len_categories.append(equal_str)
  i = 0
  while i < category_max_len:
    output = output + 5 * blank
    for item in equal_len_categories:
      output = output + item[i] + 2 * blank
    if i < category_max_len - 1:
      output = output + newline
    i = i + 1
  return output
