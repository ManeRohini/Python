#How does Python internally identify the start and end of a code block using indentation?

#When a colon (:) appears after a statement (e.g., if, for, while, def, class), Python expects the next line to be indented.
#The first indented line marks the start of the block.

#Each deeper indentation level represents a new nested block.
#A block ends when the indentation level decreases back to the previous level.
#The interpreter uses this indentation level to determine which block the statement belongs to.

def mynmae(name):          # colon → block starts
    print("Hello,", name) # 1st level indentation
    if name == "Romo":    # colon → nested block starts
        print("Special!") # 2nd level indentation
    print("Done")         # back to 1st level → inner block ended

mynmae("rohini")
mynmae("Romo")