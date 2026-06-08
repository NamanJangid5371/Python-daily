s = set()

s.add('Naman')
s.add('Kushal')
s.add('Mannu')
s.add('Harsh')
s.add('Raghunandan')

print("Set after adding elements:",s)

s.remove('Raghunandan')
s.add('Anshu')

print("New set after replacing name:",s)

s.remove('Anshu')
s.remove('Harsh')

print("New set after removeing Two names:",s)