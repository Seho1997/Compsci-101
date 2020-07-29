"""
Se Ho lee
UPI: slee626
ID: 890218467
Question 4
"""

def read(filename):
    file = open(filename, 'r')
    details = file.read()
    list_of_teams = details.split('\n')
    file.close()
    return list_of_teams

def sort(input_list):
    for element in range(len(input_list) - 1, 0, -1):
        for item in range(0, element):
            difference1 = int(input_list[item][3]) - int(input_list[item][4])
            difference2 = int(input_list[item + 1][3]) - int(input_list[item + 1][4])
            if int(input_list[item][2]) == int(input_list[item + 1][2]):
                if difference1 == difference2:
                    if input_list[item][3] < input_list[item + 1][3]:
                        input_list[item], input_list[item + 1] = input_list[item + 1], input_list[item]
                if difference1 < difference2:
                    input_list[item], input_list[item + 1] = input_list[item + 1], input_list[item]
            if int(input_list[item][2]) < int(input_list[item + 1][2]):
                input_list[item], input_list[item + 1] = input_list[item + 1], input_list[item]

def goal_difference(goal_element):
    goal_difference = int(goal_element[3]) - int(goal_element[4])
    return goal_difference

def main():
    title = "UPI: slee626"
    print(title)
    team_info = read('table1.txt')
    team_list = []
    for team in team_info:
        team_list += [team.split(',')]
    sort(team_list)

    list_number = 1
    print('{0:3} {1:10} {2:10} {3:8} {4:9} {5:1}'.format(" ", "Team", "Conference", "Points", "Diff", "Goals"))
    for info in team_list:
        print('{0:2}. {1:15} {2:7} {3:4} {4:5} {5:2} {6:5}:{7:1}'.format(list_number, info[0], info[1], info[2], goal_difference(info), " ", info[3], info[4]))
        list_number += 1

    for conference_number in range(1, 5):
        print()
        print(" Conference", conference_number)
        print('{0:3} {1:10} {2:10} {3:8} {4:9} {5:1}'.format(" ", "Team", "Conference", "Points", "Diff", "Goals"))
        list_number2 = 1
        for info in team_list:
            if int(info[1]) == conference_number:
                print('{0:2}. {1:15} {2:7} {3:4} {4:5} {5:2} {6:5}:{7:1}'.format(list_number2, info[0], info[1], info[2], goal_difference(info), " ", info[3], info[4]))
                list_number2 += 1

main()

    
                
