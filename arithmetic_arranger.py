def arithmetic_arranger(problems, t=False):

  if len(problems) > 5:
    return('Error: Too many problems.')
  
  str1_list = list()
  num1_list = list()
  str2_list = list()
  num2_list = list()
  sign_list = list()
  result_list = list()

  for eqn in problems:
    (str1, sign, str2) = eqn.split()
    str1_list.append(str1)
    str2_list.append(str2)
    sign_list.append(sign)

  if sign_list.count('*') > 0 or sign_list.count('/') > 0:
    return("Error: Operator must be '+' or '-'.") 

  for str1 in str1_list:
    try: 
      num1 = int(str1)
      num1_list.append(num1)
    except: 
      return('Error: Numbers must only contain digits.')
    
  for str2 in str2_list:
    try: 
      num2 = int(str2)
      num2_list.append(num2)
    except: 
      return('Error: Numbers must only contain digits.')

  for str1 in str1_list:
    if len(str1) > 4:
      return('Error: Numbers cannot be more than four digits.')

  for str2 in str2_list:
    if len(str2) > 4:
      return('Error: Numbers cannot be more than four digits.') 
  
  row1_list = str()
  row2_list = str()
  row3_list = str()
  row4_list = str()
  result_list = list()
  lengths = list()
  first = True

  for i in range(len(problems)):
    length = max(len(str1_list[i])+2, len(str2_list[i])+2)
    lengths.append(length)
  
  if t == False:
    for i in range(len(problems)):
      if first == True:
        row1 = str1_list[i].rjust(lengths[i])
        row1_list += row1
        row2 = sign_list[i] + " " + str2_list[i].rjust(lengths[i]-2)
        row2_list += row2
        row3 = "-"*lengths[i]
        row3_list += row3
        first = False
      
      else:
        row1 = "    " + str1_list[i].rjust(lengths[i])
        row1_list += row1
        row2 = "    " + sign_list[i] + " " + str2_list[i].rjust(lengths[i]-2)
        row2_list += row2
        row3 = "    " + str("-"*lengths[i]).rjust(lengths[i])
        row3_list += row3
    
    return(row1_list + '\n' + row2_list + '\n' + row3_list)


  lengths2 = list()

  if t==True:
    for i in range(len(problems)):
      if sign_list[i] == "+":
        result = num1_list[i] + num2_list[i]
      
      if sign_list[i] == "-":
        result = num1_list[i] - num2_list[i]
      result_list.append(str(result))
      length = max(len(str1_list[i]),len(str2_list[i])+2,len(str(result)))
      lengths2.append(length)
    
    for i in range(len(problems)):
     if first == True:
        row1 = str1_list[i].rjust(lengths[i])
        row1_list += row1
        row2 = sign_list[i] + " " + str2_list[i].rjust(lengths[i]-2)
        row2_list += row2
        row3 = "-"*lengths[i]
        row3_list += row3
        row4 = result_list[i].rjust(lengths[i])
        row4_list += row4
        first = False
      
     else:
        row1 = "    " + str1_list[i].rjust(lengths[i])
        row1_list += row1
        row2 = "    " + sign_list[i] + " " + str2_list[i].rjust(lengths[i]-2)
        row2_list += row2
        row3 = "    " + str("-"*lengths[i]).rjust(lengths[i])
        row3_list += row3
        row4 = "    " + result_list[i].rjust(lengths[i])
        row4_list += row4
    return(row1_list + '\n' + row2_list + '\n' + row3_list + '\n' + row4_list)
