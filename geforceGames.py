import csv

with open('geforce_games_with_no_steam.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    appCount = 0
    gameCount = 0

    try:
        for row in csv_reader:
            if row.__contains__('GAME'):
                gameCount += 1
                
            elif row.__contains__('APPLICATION'):
                appCount += 1
            
            print(f'TYPE: {row[0]}, TITLE: {row[1]} PUBLISHER: {row[2]} DEVELOPER: {row[3]} '+
                    f'STORE: {row[6]}\n')
            
    except Exception as e:
        with open('ERRORS.txt','a') as err:
            err.write(f'\n{e}\n')


    print(f'Application Count = {appCount}\nGame Count = {gameCount}')
