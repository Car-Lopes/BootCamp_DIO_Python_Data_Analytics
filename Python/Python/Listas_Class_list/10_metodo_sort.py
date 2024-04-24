#[].sort - Para ordernar os valores
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() 
print(linguagens) # [“c”, “csharp”, “java”, “js”, “python”]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  
print(linguagens)   # [“python, “js”, “java”, “csharp”, “c”]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))   # [“c” , “js”, “java”, “python”, “csharp”,]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)   # [“python”, “csharp”, “java”, “js”, “c”] 
print(linguagens)

print()
print()