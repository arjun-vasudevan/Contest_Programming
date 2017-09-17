speedLimit = input("")
recordedSpeed = input("")

if recordedSpeed <= speedLimit:
    print "Congratulations, you are within the speed limit!"
elif recordedSpeed - speedLimit >= 1 and recordedSpeed - speedLimit <= 20:
    print "You are speeding and your fine is $100."
elif recordedSpeed - speedLimit >= 21 and recordedSpeed - speedLimit <= 30:
    print "You are speeding and your fine is $270."
elif recordedSpeed - speedLimit >= 31:
    print "You are speeding and your fine is $500."
