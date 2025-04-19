import os

cwd = os.getcwd() #curren worker directory
print(f"Directorio actual {cwd}")

#listar archivos
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt", txt_files)

#renombrar archivo
os.rename("file001.txt", "file.txt")

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt", txt_files)
