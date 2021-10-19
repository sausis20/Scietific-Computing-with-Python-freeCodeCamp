def arithmetic_arranger(problems, solution = False):

    #Check if number of problems > 5
    if len(problems) > 5:
      return "Error: Too many problems."

    first_operand = []
    second_operand = []
    operator = []
    third_line = []
    fourth_line = []

    #Split problems into lines
    for problem in problems:
        symbols = problem.split()
        first_operand.append(symbols[0])
        operator.append(symbols[1])
        second_operand.append(symbols[2])

    #Check that operator is not * or /
    if '*' in operator or '/' in operator:
      return "Error: Operator must be '+' or '-'."

    #Check that problems are digits
    for i in range(len(first_operand)):
      if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
        return "Error: Numbers must only contain digits."
        
    #Check number lenght
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    #Generate dashes
    longest_number = []
    for i in range(len(first_operand)):
        longest_number.append(max(len(first_operand[i]), len(second_operand[i])))

    for i in range(len(longest_number)):
        third_line.append("-"*(longest_number[i]+2))
        
        
    first_line = []
    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            first_line.append("  " + first_operand[i])
        else:
            first_line.append(" "*(len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])
    
    second_line = []
    for i in range(len(second_operand)):
        if len(second_operand[i]) > len(first_operand[i]):
            second_line.append(operator[i] + " " + second_operand[i])
        else:
            second_line.append(operator[i] + " "*(len(first_operand[i]) - len(second_operand[i]) +1 ) + second_operand[i])

    #Generate solution
    if solution:
        for i in range(len(first_operand)):
            if operator[i] == "+":
                a = str(int(first_operand[i]) + int(second_operand[i]))
            else:
                a = str(int(first_operand[i]) - int(second_operand[i]))
            
            if len(a) > max(len(first_operand[i]), len(second_operand[i])):
                fourth_line.append(" " + a)
            else:
                fourth_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(a) +2 ) + a)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)

    return arranged_problems