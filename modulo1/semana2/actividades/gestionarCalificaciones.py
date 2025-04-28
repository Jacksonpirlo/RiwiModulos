insertRatingsCount = int(input('Insert your count ratings: ')) # INSERT COUNT OF RATINGS
ratings = [] # ARRAY TO SAVE RATINGS
average = 0 # VARIABLE TO SAVE THE AVERAGE
if insertRatingsCount >= 0 and insertRatingsCount <= 100 : # "IF" TO VALIDATE IF "insertRatingAcount" IS BETWEN 0 AND 100
    for i in range(insertRatingsCount): # "FOR" TO TRAVELING AROUND THE NUMBER
        nota = float(input(f'Insert rating {i + 1}: ')) # VARIABLE TO INSERT THE RATINGS
        ratings.append(nota) # "APPEND" TO DO PUSH IN ARRAY "RATINGS"
        for j in ratings: # OTHER "FOR" TO TRAVEL IN RATINGS AND MAKE THE SUM
            total = sum(ratings) # WE CREATED A VARIABLE CALLED "TOTAL" TO SAVE THE SUM
            average = total / insertRatingsCount # SPLIT TOTAL WITH "insertRatingsCount" TO MAKE THE AVERAGE
            average = round(average) # MAKE A ROUND OF AVERAGE
    print(average)
    print(ratings)

    if average <= 20: # VALIDATING IF AVERAGE IS LESS THAN 20 FOR CAN TO DO THE SPESIFIC SELECTION
        temp = 0 # OUR TEMPORAL VALIVLE TO SAVE THE RESULT
        print('Approved') # IF AVERAGE IS MORE THAN 20. PRINT("APPROVED")
        ingspecificValue = int(input('Insert an spesific value: ')) # WE SELECTED AN SPESIFIC VALUE
        for k in range(len(ratings)): # # CHECK THE RATINGS TO SEE EACH VALUE
            if ingspecificValue > ratings[k]: # VERIFY IF "ingspecificValue" IS MORE THAN ARRAY'S POSITION
                print(f'{ingspecificValue} is more than {ratings[k]}') # PRINT IS "ingspecificValue" IS MORE THAN ARRAY'S POSITION
                temp = temp + 1 # SAVE THIS RESULT HERE
        print(temp)
    else:
        print('Disapproved') # THE "ELSE" OF THE FIRST CONDITIONAL
else:
    print('Insert ratings betwen 1 and 100') # THE "ELSE" OF THE SECOND CONDITIONAL