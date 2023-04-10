class Category:

  # Intiate the attributes (name)
  def __init__(self, category_name):
    self.category_name = category_name
    self.ledger = []
    self.balance = 0
    self.total_spendings = 0

  # Create deposit method // Add an amount and a description to the category
  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  # Create the check_funds // True if the amount <= balance / False otherwise
  def check_funds(self, amount):
    if self.balance - amount < 0:
      return False
    return True

  # Create withdraw method // Add a negative amount to the ledger
  def withdraw(self, amount, description=''):
    amount = round(amount, 2)
    if not self.check_funds(amount):
      return False
    self.total_spendings += amount
    amount = 0 - amount
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount
    return True

  # Create get balance
  def get_balance(self):
    return self.balance

  # Create transfer method that transfers founds from ca category to another one
  def transfer(self, amount, category):
    if not self.check_funds(amount):
      return False
    self.withdraw(amount, f'Transfer to {category.category_name}')
    category.deposit(amount, f'Transfer from {self.category_name}')
    return True

  # Create print fucntion
  def __str__(self):

    printing = ''  # This will be the string that will be printed

    # Print name with * -> while loop with added * at the beggining and end until len = 30
    name = self.category_name
    while len(name) < 30:
      name = '*' + name
      if len(name) == 30:
        break
      name = name + '*'
    printing = printing + name + "\n"

    # Print the list of deposits and withdraws
    for i in range(0, len(self.ledger)):
      amount = str(self.ledger[i]['amount'])
      description = self.ledger[i]['description']

      # If the string is to long we have to short it
      
      if len(description + '%.2f' % float(amount)) > 29:
        description = list(description)
        while len(description) + len('%.2f' % float(amount)) > 29:
          description.pop()
        description = ''.join(description)
      while len(description + '%.2f' % float(amount)) < 30:
        description = description + ' '
      printing = printing + description + '%.2f' % float(amount) + '\n'

    # Print category total
    printing = printing + 'Total: ' + str(self.balance)

    return printing


def create_spend_chart(categories):

  percentage_line = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
  chart = []
  categorie_percentage = []  # used to calculate the percentage for all the categories

  # Calculate the total withdraw
  total = 0
  max_string = 0
  max_len = 0  # used to create the strings
  for categorie in categories:
    total = total + categorie.total_spendings
    if len(categorie.category_name) > max_string:
      max_string = len(categorie.category_name)

  # Create the percentage for each categorie
  for categorie in categories:
    categorie_percentage.append(categorie.total_spendings * 100 / total - ((categorie.total_spendings * 100 / total)%10))

  # Create the string
  max_len += 12 + max_string  # 12 because of percentage and the ----- line
  line = []
  percentage = 100
  for i in range(0, max_len):
    # Create the percentage line
    if percentage - 10 >= 0:
      if len(str(percentage)) == 3:
        line.append(str(percentage) + '| ')
      elif len(str(percentage)) == 2:
        line.append(' ' + str(percentage) + '| ')
    elif percentage == 0:
      line.append('  ' + '0' + '| ')
    elif percentage == -10:
      line.append('    -')
    else:
      line.append('     ')
    percentage -= 10
  chart.append(line)

  # Create the lines for categories
  for categorie_index in range(0, len(categories)):
    line = []
    for i in range(0, len(percentage_line)):
      if percentage_line[i] > categorie_percentage[categorie_index]:
        line.append('   ')
      else:
        line.append('o  ')
    line.append('---')
    name = [i + '  ' for i in categories[categorie_index].category_name]
    line = line + name
    while len(line) < max_len:
      line.append('   ')
    chart.append(line)

  # Print the chart
  vertical_chart = 'Percentage spent by category'
  for i in range(0, max_len):
    vertical_chart += '\n'
    for line in chart:
      vertical_chart += line[i]  
  return vertical_chart
