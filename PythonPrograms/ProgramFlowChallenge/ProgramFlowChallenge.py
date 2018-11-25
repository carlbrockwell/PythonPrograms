ip_address = input("Please enter your ip address:")
segment_count = 0
segment = ''
for char in ip_address:
    if char == '.':
        segment_count += 1
        print("Segment {0}: ".format(segment_count) + " is " + str(len(segment)) + " long")
        segment = ''
    else:
        segment += str(char)
        print(char)
else:
    segment_count += 1
    print("Segment {0}: ".format(segment_count) + " is " + str(len(segment)) + " long")
