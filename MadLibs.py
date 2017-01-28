import Epic

adjective = Epic.userString("Enter an adjective:")
adjective2 = Epic.userString("Enter another adjective:")
pluralNoun = Epic.userString("Enter a plural noun:")
pluralNoun2 = Epic.userString("Enter another plural noun:")
celebrity = Epic.userString("Enter a celebrity:")
noun = Epic.userString("Enter a noun:")

sentence = ("In the shadowy world of spies, a/an ADJ1 organization like the US "
           "Government uses spies to infiltrate ADJ2 groups for the purpose of "
         "obtaining top secret PLNOUN1. A teacher, CELEB, or even the little "
           "old NOUN with a cane and fifteen pet PLNOUN2 could be a spy.")

print

sentence = sentence.replace ("ADJ1", adjective)
sentence = sentence.replace ("ADJ2", adjective2)
sentence = sentence.replace ("PLNOUN1", pluralNoun)
sentence = sentence.replace ("PLNOUN2", pluralNoun2)
sentence = sentence.replace ("CELEB", celebrity)
sentence = sentence.replace ("NOUN", noun)

print sentence
