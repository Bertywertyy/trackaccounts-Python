x = int(input('How much money do you have? '))
record = input('Add an expense or income record (desc1 amt1, desc2 amt2, ...):\n')
balance = x
records = [entry.strip() for entry in record.split(',')]
output = "\n".join(records)
balance += sum(int(entry.rsplit(' ', 1)[1]) for entry in records)
print(f"Here's your expense and income records:\n{output}")
print(f"Now you have {balance} dollars.")