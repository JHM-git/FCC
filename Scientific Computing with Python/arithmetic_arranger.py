

string = '632 + 45'
the_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(lst, boole=False):
  blank = ' '
  four_blanks = '    '
  dash = '-'
  first_line = ''
  second_line = ''
  third_line = ''
  fourth_line = ''
  if len(lst) > 5:
    return "Error: Too many problems."
  for string in lst:
    lst_from_str = string.split(' ')
    item1, operator, item2 = lst_from_str[0], lst_from_str[1], lst_from_str[2]
    try:
      num1, num2 = int(item1), int(item2)
    except:
      return "Error: Numbers must only contain digits."
    result = 0
    if operator.find('+') == -1 and operator.find('-') == -1:
      return "Error: Operator must be '+' or '-'."
    if operator.find('+') != -1:
      result = num1 + num2
    else:
      result = num1 - num2
    result_str = str(result)
    length = 0
    if len(item1) > 4 or len(item2) > 4:
      return "Error: Numbers cannot be more than four digits."
    if len(item1) >= len(item2):
      length = len(item1) + 2
    else:
      length = len(item2) + 2
    first_line = first_line + (length - len(item1)) * blank + item1 + four_blanks
    second_line = second_line + operator + (length - len(item2) - 1) * blank + item2 + four_blanks
    third_line = third_line + length * dash + four_blanks
    fourth_line = fourth_line + (length - len(result_str)) * blank + result_str + four_blanks
  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  third_line = third_line.rstrip()
  fourth_line = fourth_line.rstrip()

  arranged_problems = ''
  if boole is True:
    arranged_problems = first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
  else:
    arranged_problems = first_line + '\n' + second_line + '\n' + third_line
  return arranged_problems
