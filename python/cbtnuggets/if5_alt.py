# run this script from am OS shell prompt; it works better

while ( s = input('Enter a string of at least 4 characters, or q to quit') ) != 'q':

    if len(s) < 4:
        print ("Value is too small")
        continue

    print ("The string was of sufficient length.")

    raise SystemExit # try this from the OS command line
