# Contains func
def contains(str, substr):
    if((str.lower()).find(substr) == -1): return False
    else: return True

txt = "Hello World" # Write your text
print(contains(txt, "Hello")) # Write what you want to find