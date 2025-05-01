text1: str = ""  # INITIALIZES A STRING VARIABLE TO STORE THE USER INPUT WITH RATINGS
text2: str = ""  # TEMPORARY STRING USED TO BUILD EACH INDIVIDUAL NUMBER FROM THE INPUT

FinallyAverage = 0  # STORES THE FINAL CALCULATED AVERAGE OF ALL VALID RATINGS
ApprovedOrdisapproved: float = 65.00  # MINIMUM AVERAGE REQUIRED TO PASS

numRepeat = 0  # UNUSED VARIABLE (RESERVED FOR POSSIBLE FUTURE USE)
sumList = 0  # ACCUMULATES THE SUM OF ALL VALID RATINGS
average = []  # LIST TO STORE EACH VALID FLOATING POINT RATING ENTERED
count = {}  # DICTIONARY TO COUNT THE NUMBER OF TIMES EACH RATING APPEARS

text1 = str(input('Insert ratings: ')) + ","  # ASKS THE USER FOR RATINGS, ADDS A COMMA TO ENSURE LAST NUMBER IS PROCESSED

for i in text1:  # LOOPS THROUGH EACH CHARACTER IN THE INPUT STRING
    if i != ",":  # IF THE CHARACTER IS NOT A COMMA, IT'S PART OF A NUMBER
        text2 = text2.__add__(i)  # APPENDS THE CHARACTER TO THE TEMPORARY NUMBER STRING
    else:  # IF A COMMA IS FOUND, IT INDICATES THE END OF A NUMBER
        number: float = float(text2)  # CONVERTS THE ACCUMULATED STRING INTO A FLOAT
        if number > 0 and number <= 100:  # CHECKS IF THE NUMBER IS IN THE VALID RANGE
            text2 = ""  # CLEARS THE TEMP STRING FOR THE NEXT NUMBER
            average.append(number)  # ADDS THE VALID NUMBER TO THE LIST
        else:  # IF THE NUMBER IS INVALID (OUT OF RANGE)
            print('Numbers out of range')  # PRINTS AN ERROR MESSAGE

for j in average:  # LOOPS THROUGH EACH VALID RATING IN THE LIST
    sumList += j  # ADDS EACH RATING TO THE TOTAL SUM
    FinallyAverage = sumList / len(average)  # UPDATES THE FINAL AVERAGE AFTER EACH ADDITION

spesificValue = float(input('Insert an spesific value: '))  # PROMPTS THE USER FOR A SPECIFIC VALUE TO COMPARE AGAINST
if spesificValue > 0 and spesificValue <= 100:  # CHECKS IF THE SPECIFIC VALUE IS IN A VALID RANGE
    for k in average:  # LOOPS THROUGH ALL VALID RATINGS
        if k > spesificValue:  # IF A RATING IS HIGHER THAN THE SPECIFIC VALUE
            print(f'''{k} is more than {spesificValue}
''')  # PRINTS THAT THE RATING IS GREATER

for x in average:  # LOOPS THROUGH EACH RATING TO COUNT OCCURRENCES
    if x in count:  # IF THE RATING IS ALREADY IN THE DICTIONARY
        count[x] += 1  # INCREASES ITS COUNT
    else:  # IF IT'S NOT IN THE DICTIONARY YET
        count[x] = 1  # ADDS IT TO THE DICTIONARY WITH INITIAL COUNT OF 1

for num, appear in count.items():  # ITERATES OVER THE DICTIONARY ITEMS (RATING AND COUNT)
    print(f'''This rating {num} appear {appear} times.''')  # PRINTS HOW MANY TIMES EACH RATING APPEARS

if FinallyAverage >= ApprovedOrdisapproved:  # CHECKS IF THE FINAL AVERAGE IS ENOUGH TO PASS
    print(f'''

          REPORT BULLETIN

CONGRATULATIONS! YOU PASSED. HERE'S MORE INFORMATION ABOUT YOUR GRADES:

           YOUR GRADES: {average}
           
           WHAT YOU NEEDED TO GET AHEAD: {ApprovedOrdisapproved}
           WHAT YOU HAVE: {FinallyAverage}

''')  # PRINTS SUCCESS MESSAGE WITH STATS
else:  # IF THE AVERAGE IS NOT ENOUGH TO PASS
    print(f'''
          
          REPORT BULLETIN

SORRY, YOU DIDN'T HAVE ENOUGH PERFORMANCE TO PASS:

           YOUR GRADES: {average}
           
           WHAT YOU NEEDED TO GET AHEAD: {ApprovedOrdisapproved}
           WHAT YOU HAVE: {FinallyAverage}
    
''')  # PRINTS FAILURE MESSAGE WITH STATS
