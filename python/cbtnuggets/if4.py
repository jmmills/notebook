fmenu = {'spam':1.50, 'ham':1.99, 'eggs':0.99}

corder = input("What will you have today--spam, ham, eggs? ")
corder = 'eggs by default' if corder not in fmenu else corder
price = fmenu[corder] if corder in fmenu else fmenu['eggs']

print ("For the %s, that will be" % corder, "$", "%.2f" % price, ", please.")
