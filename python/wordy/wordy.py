def answer(question):
    while len(equation) > 1:
            try: 
            # The questionable/error-prone code goes here,in an indented block
            # It can contain statements, loops, if-else blocks, or other executable code. 
                x_value, operation, y_value, *rest = equation


            except:
                # Code for what to do when an error gets thrown in the code above.
                # This could be one error, or more complicated logging, error checking and messaging.
                raise ValueError("syntax error")





# if the question contains an unknown operation.
raise ValueError("unknown operation")

# if the question is malformed or invalid.
raise ValueError("syntax error")
