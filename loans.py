class Loan:
  def __init__(self, payment_amount, interest_percent, years):
      self.payment_amount = payment_amount
      self.interest_percent = interest_percent #APR, integer value
      self.years = years #How long to pay back loan

  #calculate total payment of the loan after interest
  def compute_total(self):
      interest_rate = self.interest_percent/100
      total_APR = self.payment_amount * interest_rate * self.years
      total = self.payment_amount + total_APR
      return total


loan = Loan(27000, 3, 6)
print(loan.payment_amount)
print(loan.interest_percent)
print(loan.years)
print("Total:",loan.compute_total())
