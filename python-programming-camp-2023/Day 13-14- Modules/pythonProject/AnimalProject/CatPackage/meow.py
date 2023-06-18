

def speak():
    print("meow")

def speak2():
    print("meow2")

def speak_directed():
    print("meow directed")

#burada veya dışarıda çalıştığını belirtir
def speak2_imported():
    print("meow imported")

if __name__=="__main__":
    speak_directed()
else:
    speak2_imported()