sentence = input("Enter a sentence:")
sentence = sentence.lower()
count = 0
vowelcount = 0
consonantcount = len(sentence)
for c in sentence:
    if c==' ':
        count=count+1
    if c=='a' or c=='e' or c=='i' or c=='u' or c=='o':
        vowelcount=vowelcount+1
        consonantcount=consonantcount-1
print(f"Words :{count+1}")
print(f"Characters:{len(sentence)}")
print(f"Consonants:{consonantcount-count}")
print(f"Vowel:{vowelcount}")
print(f"Spaces:{count}")
    
