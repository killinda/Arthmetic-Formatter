def arithmetic_arranger(problems,need_result=None):
  if len(problems) > 5:
      arranged_problems = "Error: Too many problems."
  else:
      first_number_list = []
      second_number_list = []
      symbol_list = []
      result_list= []
      position =[]
      for i in problems:
          if i.split(" ")[1] not in ("-","+"):
              arranged_problems = "Error: Operator must be '+' or '-'."
              break   
          if (len(i.split(" ")[0])>4 or len(i.split(" ")[2])>4)== True:
              arranged_problems = "Error: Numbers cannot be more than four digits."
              break 
          if (i.split(" ")[0].isdigit() and i.split(" ")[2].isdigit()) == False:
              arranged_problems = "Error: Numbers must only contain digits."
              break         
          position = 2+max(len(i.split(" ")[2]),len(i.split(" ")[0]))
          first_number_list.append((" "*(position-len(i.split(" ")[0])))+i.split(" ")[0])
          symbol_list.append(((position)*"-"))
          second_number_list.append(i.split(" ")[1]+(" "*(position-1-len(i.split(" ")[2])))+i.split(" ")[2])
          if i.split(" ")[1] =="-":
              result_number = int(i.split(" ")[0])-int(i.split(" ")[2])    
          else:
              result_number = int(i.split(" ")[0])+int(i.split(" ")[2])
          result_number = str(result_number)
          result_list.append(" "*(position-len(result_number))+result_number)    
      if len(first_number_list)==len(problems):
          first_number = "    ".join(first_number_list)+"\n"
          second_number = "    ".join(second_number_list)+"\n" 
          result = "    ".join(result_list)

          if need_result== None:
              need_result = False
          if need_result ==True:
              symbol = "    ".join(symbol_list)+"\n"  
              arranged_problems_list = first_number+second_number+symbol+result
          else:
              symbol = "    ".join(symbol_list) 
              arranged_problems_list = first_number+second_number+symbol
          arranged_problems = "".join(arranged_problems_list)
  return arranged_problems
