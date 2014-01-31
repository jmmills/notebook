lb = int( input("Enter lower bound: ") )
ub = int( input("Enter upper bound: ") )

print (
    "\nYou chose {0} as your lower bound, \
and {1} as your upper bound.".format(lb, ub)
    )

verif = input( "\nProceed? (y/n): " )
response = verif.lower()

if response == 'y':
    for m in range( lb, (ub + 1) ):
        for i in range (1, 11):
            print (i, 'x', m, '=', i * m)
else:
    print ("We're done!")

