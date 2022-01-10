#question 2
gross_income = int(input( "the income of user is"))
standard_deduction = 10000
number_of_dependents = int ( input( "number of dependents are"))
dependentdeductionamount = (number_of_dependents*3000)
taxable_income=(gross_income-standard_deduction-dependentdeductionamount)
tax_to_be_paid=((20/100)*taxable_income)
print ("the amount of tax is")
print(tax_to_be_paid)


