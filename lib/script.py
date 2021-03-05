from capitals import states
import random

# print(states)

print('Welcome to the state-capitals game\n')
repeat_game = 'yes'

while repeat_game == 'yes':
    random.shuffle(states)    
    correct_ans_count = 0
    wrong_ans_count = 0
    
    
    for i in range (0, len(states)):
        print(f"\nWhat is the capital of {states[i]['name']}?")
        answer = input('Your answer is: ')
        if answer.lower() == states[i]["capital"].lower():        
            print("Correct!")
            correct_ans_count +=1        
        else:
            print("It is: ", states[i]["capital"])
            wrong_ans_count +=1
        
        total_count = correct_ans_count + wrong_ans_count        
        if total_count != 0:
            print(f'Total played: {total_count}')
            print("Your running score: ", int(100*correct_ans_count/total_count),'%')
    
    print("\nWould you like to play again? (Y/N)")
    answer1 = input()
    if answer1 == 'Y' or answer1 == 'y':
        repeat_game = 'yes'
        print('Good luck!')
    else:
        repeat_game = 'no'
        print('BYE')
  

