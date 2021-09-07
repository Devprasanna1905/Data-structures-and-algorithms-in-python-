def anagram(s1,s2):
    s1=s1.replace(" ","")
    s2=s2.replace(" ","")
    if(sorted(s1)==sorted(s2)):
        return " it is anagram"
    return "it is not anagram"  
#input string     
print(anagram("",""))    
