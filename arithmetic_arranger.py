def arithmetic_arranger(problems, true=0):
  if len(problems) > 5:
    print('Error: Too many problems.')
    quit()

  num1l = list()
  num2l = list()
  row2l = list()
  row2list = list()
  signs = list()
  results = list()
  lengths = list()
  num_prob = len(problems)
  ind = 0

  for eqn in problems:
    if eqn.find('*') != -1 or eqn.find('/') != -1:
      print("Error: Operator must be ' + ' or ' - '.")
      quit()
    
    elif eqn.find('+') != -1:
      sign = eqn.find('+')
      first_str = eqn[:sign - 1]
      second_str = eqn[sign + 2:]
      asign = "+"

    elif eqn.find('-') != -1:
      sign = eqn.find('-')
      first_str = eqn[:sign - 1]
      second_str = eqn[sign + 2:]
      asign = "-"



    try:
      first_num = int(first_str)
      second_num = int(second_str)
    except:
      print('Error: Numbers must only contain digits.')
      quit()

    if len(str(first_num)) > 4 or len(str(second_num)) > 4:
      print('Error: Numbers cannot be more than four digits.')
      quit()

    num1l.append(first_num)
    num2l.append(second_num)
    signs.append(asign)
    row2l.append(asign + " " + second_str)

  if true == 1:
    for num1 in num1l:
      if signs[ind] == "+":
        result = num1 + num2l[ind]
      elif signs[ind] == "-":
        result = num1 - num2l[ind]
      results.append(result)
      length = max(len(str(num1)), len(str(num2l[ind])) + 2, len(str(result)))
      lengths.append(length)
      ind = ind + 1

    fir1 = str(num1l[0]).rjust(lengths[0])
    sec1 = str(signs[0]+" "+str(num2l[0])).rjust(lengths[0])
    slash1 = "-" * lengths[0]
    result1 = str(results[0]).rjust(lengths[0])

    if num_prob > 1:
      i = 1
      rest1s = str()
      rest2s = str()
      slashrests = str()
      resultrests = str()
      while i < num_prob:
        rest1 = str(num1l[i]).rjust(lengths[i] + 4)
        rest1s = rest1s + rest1
        rest2 = str(signs[i]+" "+str(num2l[i])).rjust(lengths[i] + 4)
# Ends here, try to fix second row indent issues
        rest2s = rest2s + rest2
        slashrest = "-" * lengths[i]
        slashrests = slashrests + slashrest.rjust(lengths[i] + 4)
        resultrest = str(results[i]).rjust(lengths[i] + 4)
        resultrests = resultrests + resultrest
  
        i += 1
      arranged_problems = fir1 + rest1s + '\n' + sec1 + rest2s + '\n' + slash1 + slashrests +'\n' + result1 + resultrests
 

    else:
      arranged_problems = fir1 + '\n' + sec1 + '\n' + slash1 + '\n' + result1

  else:
    for num1 in num1l:
      length = max(len(str(num1)), len(str(num2l[ind]))+2)
      lengths.append(length)
      ind = ind + 1

    fir1 = str(num1l[0]).rjust(lengths[0])
    sec1 = str(row2l[0]).rjust(lengths[0])
    slash1 = "-" * lengths[0]

    if num_prob > 1:
      i = 1
      rest1s = str()
      rest2s = str()
      slashrests = str()
      while i < num_prob:
        rest1 = str(num1l[i]).rjust(lengths[i] + 4)
        rest1s = rest1s + rest1
        rest2 = str(row2l[i]).rjust(lengths[i] + 4)
        rest2s = rest2s + rest2
        slashrest = "-" * lengths[i]
        slashrests = slashrests + slashrest.rjust(lengths[i] + 4)
        i += 1
      arranged_problems = fir1 + rest1s + '\n' + sec1 + rest2s + '\n' + slash1 + slashrests
 

    else:
      arranged_problems = fir1 + '\n' + sec1 + '\n' + slash1 + '\n'

 
  return arranged_problems
