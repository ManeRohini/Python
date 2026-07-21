
def filterX(Task,elements):
   result =[]

   for no in elements:
      ret = Task(no)
      if(ret==True):
            result.append(no)
            return result


def mapX(Task,elements):
    result =[]

    for no in elements:
        ret =Task(no)
        result.append(ret)
    return result

def reduceX(Task,elements):
    sum=0

    for no in elements:
        sum = Task(sum,no)
    return sum

