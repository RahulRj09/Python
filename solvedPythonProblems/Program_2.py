#variables
Total = 0
#ask user to input the number of boxes
boxes = int(input("Please enter the number of boxes(maximim 1000):\n>"))
total = boxes
#checking for invalid length
if boxes > 1000:
    print("INVALID LENGHT")
    exit()
if boxes >=48:
    box_48 = int(boxes/48)
    print('48 X ' + str(box_48) + " = " + str(box_48*48))
    boxes = boxes - (box_48*48)
    Total += box_48
if boxes >=24:
    box_24 = int(boxes/24)
    print('24 X ' + str(box_24) + " = " + str(box_24*24))
    boxes = boxes - (box_24*24)
    Total += box_24
if boxes >=12:
    box_12 = int(boxes/12)
    print('12 X ' + str(box_12) + " = " + str(box_12*12))
    boxes = boxes - (box_12*12)
    Total += box_12
if boxes >=6:
    box_6 = int(boxes/6)
    print('6 X ' + str(box_6) + " = " + str(box_6*6))
    boxes = boxes - (box_6*6)
    Total += box_6
if boxes < 6:
    if boxes == 0:
        print ("Remaininig Boxes = " + str(boxes))
    else:
        print ("Remaininig Boxes " + str(boxes) + " X 1 = " + str(boxes))
        Total += 1
print("Total number of boxes " + str(total))
print("Total number of carotns " + str(Total))
