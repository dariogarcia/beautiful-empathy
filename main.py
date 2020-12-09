import csv

def game_init():
    input('Welcome to Beautiful Empathy. Press Enter to begin one round of 5 questions.')
    

#change input to keyboard    
    
with open('Questions - Sheet1.tsv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:


        if line_count == 0:
            game_init()
            line_count += 1
#count 5 rounds here!
        else:
#increase size
            print(f'{row[0].replace("mask","   ")}')
            input('Press Space for the words')
            print(f'{row[1]}  -  {row[2]}')
            input('Press Enter for next question')




            line_count += 1
    print(f'Processed {line_count} lines.')





input("Press Enter to continue...")
