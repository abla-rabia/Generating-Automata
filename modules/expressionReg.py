from modules.automate import Automate


class ExpressionReg:
    def __init__(self, X, ER):
        self.X = X
        self.ER = ER

    def expr(self):
        print(f"Mon alphabet : {self.X} et je suis : {self.ER}")

    def infix_to_postfix(self):
        precedence = {'*': 3, '.': 2, '|': 1}
        output = []
        operator_stack = []

        for symbol in self.ER:
            if symbol.isalpha():
                # If the symbol is a letter, add it to the output
                output.append(symbol)
            elif symbol == '(':
                # If the symbol is an open parenthesis, push it onto the stack
                operator_stack.append(symbol)
            elif symbol == ')':
                # If the symbol is a closing parenthesis, pop operators from the stack and add them to the output until an open parenthesis is encountered
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Discard the open parenthesis
            else:
                # If the symbol is an operator, pop operators from the stack and add them to the output until an operator with lower precedence or an open parenthesis is encountered
                while operator_stack and operator_stack[-1] != '(' and precedence[operator_stack[-1]] >= precedence[symbol]:
                    output.append(operator_stack.pop())
                operator_stack.append(symbol)

        # Pop any remaining operators from the stack and add them to the output
        while operator_stack:
            output.append(operator_stack.pop())

        self.ER= ''.join(output)
        
    def evaluate_postfix(self,automate1):
        stack = []
        automate2=Automate(automate1.X)
        for symbol in self.ER:
            if symbol.isalpha():
            # If the symbol is a letter (operand), push it onto the stack
                 tempAuto=Automate(automate1.X)
                 tempAuto.constAutoTrivial(symbol)
                 stack.append(tempAuto)
            elif symbol in ['.', '|','*']:
            # print(f"Processing: {operand1} {operator}")
                 if(symbol=="*"):
                     automate1=stack.pop() 
                     automate1.Iteration()
                     stack.append(automate1)
                    
                 elif(symbol=="."):
                             automate2=stack.pop()
                             automate1=stack.pop() 
                             
                             automate1.ConcatenationDroite(automate2)
                             stack.append(automate1)
                 else:#symbole="|"
                              automate2=stack.pop()
                              
                              automate1=stack.pop() 
                              automate1.Union(automate2)
                              stack.append(automate1)
                             
          
    # The final result should be on the top of the stack
        return stack[0]
 