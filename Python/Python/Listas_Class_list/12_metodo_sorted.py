#SORTED - a função sorted para ordenar interaveis por ordens de tamanho
linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))

print()