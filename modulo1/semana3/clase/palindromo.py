def es_palindromo(word:list="reconocer")->str:
    word_array:list= []
    for i in word:
        word_array.append(i)
    word_array_reverse:list= word_array[::-1]
    if word_array == word_array_reverse:
        return "Palindromo"
    else:
        return "No palindromo"

        
def main():
    print(es_palindromo())

main()