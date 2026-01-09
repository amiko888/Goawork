
real_password = 'Nino1234!' #vqmnit parols
attemps = 3  #sul mcdelobis raodenoba gvaqvs 3

user_attempts = 0 #mcdelobebis dasawyisi

while attemps > user_attempts: #rodesac mcdelobebis raodenoba metia momxmareblis raodenobaze
    remaining = attemps - user_attempts #itvlis darchenil mcdelobebes
    user_input = input(f'Guess the password again You have {remaining}, Attemp(s) left To Guess the password: ') #momxmarebels eubneba ramdeni mcdelobac darcha da stxovs parolis sheyvanas
    user_attempts += 1 #yoveli mcdelobis shemdeg gazrdilia mcdeloba

    if user_input == real_password: #tu momxmareblis sheyvanili paroli daemtxveva namdvil parols mashin
        print('Congrats you have guessed the correct password!') #ibewdeba es
        break #da aq wydeba kodi
    else: #sxva shemtxvevashi ki
        print('Wrong please try again later!') #bewdavs rom tavidan cados mogvianebit
else: #es gaeshveba mashin roca amowuravs mcdelobebis raodenobas
    print('You have reached the maximum number of attempts')