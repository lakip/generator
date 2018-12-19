import string


def generate_number_plates():
    letters = string.ascii_lowercase
    plate_list = list(letters.upper())
    plate_list.pop(8,)
    plate_list.pop(13)
    # generate from KAA - KAZ
    part_1 = ['KA'+x for x in plate_list]
    i = 1
    part_2 = []
    while i <= 999:
        part_2.append(str(i).zfill(3))
        i += 1
    part_3 = plate_list

    # Generate part_1 + part_2
    part_1_2 = []
    for part in part_1:
        x = True
        while x:
            for xx in part_2:
               part_1_2.append(part + xx)
            x = False
    # Generate part_1 + part_2 + part_3 e.g KAA 001A
    part_1_2_3 = []
    for this in part_1_2:
        x = True
        while x:
            for xx in part_3:
                part_1_2_3.append(this + xx)
            x = False

    return part_1_2_3


print(generate_number_plates())
# getting the absolute position of numbers and calculating the number between the two number plates


def search_number_plates(plate_1, plate_2):
    all_plates = generate_number_plates()
    plate_1_pos = all_plates.index(plate_1)
    plate_2_pos = all_plates.index(plate_2)
    res = abs(plate_2_pos - plate_1_pos) #
    return res + 1


print (search_number_plates('KAA001A', 'KAZ999Z'))

#for more explanaton,read readme