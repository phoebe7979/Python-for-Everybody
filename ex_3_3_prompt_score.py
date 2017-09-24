#Prompt score then assign grade
score = input("Enter Score: ")
try:
    fscore = float(score)
except:
    print("Please enter a numeric value.")
    quit()
if fscore < 0.6:
    print("F")
elif fscore < 0.7 and fscore >= 0.6:
    print("D")
elif fscore < 0.8 and fscore >= 0.7:
    print("C")
elif fscore < 0.9 and fscore >= 0.8:
    print("B")
elif fscore <= 1 and fscore >= 0.9:
    print ("A")
else:
    print ("ERROR. Please enter a numeric value between 0.0 and 1.0")
    quit()
