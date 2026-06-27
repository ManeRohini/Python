#What happens if a module contains print statements outside any function?

#When Python imports a module, it runs all the code at the top level (outside functions/classes) once.

#This includes variable assignments, function definitions, and print statements.
#Any print() outside functions executes during the import.

#Output appears even before you call any function from the module.