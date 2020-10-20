import Basics.Output.simple_message as simple_message
import Basics.Output.multiline_message as multiline_message
import Basics.Output.escape_characters as escape_characters
import Basics.Output.ascii_art as ascii_art
import Basics.Input.user_input as user_input
import Basics.Input.data_types as data_types
import Basics.Input.string_operators as string_operators
import Basics.Input.overall_review as overall_review
import Basics.Repetitions.While_loop.simple as simple
import Basics.Repetitions.While_loop.len as len
import Basics.Repetitions.While_loop.factorial as factorial
import Basics.Repetitions.While_loop.count as count
import Basics.Repetitions.While_loop.sum_user_numbers as sum_user_numbers
import Basics.Repetitions.While_loop.sum_100 as sum_100
import Basics.Repetitions.While_loop.ascii as ascii
import Basics.Repetitions.For_loop.simple as simple_for
import Basics.Repetitions.For_loop.reverse as reverse
import Basics.Repetitions.For_loop.range as range_for
import Basics.Repetitions.For_loop.membership_operators as membership_operators
import Basics.Repetitions.For_loop.count_down as count_down
import Basics.Repetitions.For_loop.characters as characters
import Basics.Repetitions.Nested_loop.nested as nested_loop
import Basics.Repetitions.Nested_loop.nesting as nesting
import Basics.Decisions.and_operator as and_operator
import Basics.Decisions.or_operator as or_operator
import Basics.Decisions.Review as review
import Basics.Decisions.nested_decisions.nestception as nestception
import Basics.Decisions.nested_decisions.nested as nested
import Basics.Decisions.Simple_Decisions.comparison_operators.bot as bot
import Basics.Decisions.Simple_Decisions.Counter.bot as bot_counter
import Basics.Decisions.Simple_Decisions.if_elif_else.bot as if_elif_else_bot
import Basics.Decisions.Simple_Decisions.modulo_operator.bot as modulo_operator_bot
import Basics.Decisions.Simple_Decisions.if_else as if_else
import Basics.Decisions.Simple_Decisions.if_if as if_if
import Basics.Functions.ascii_character as ascii_character
import Basics.Functions.ascii_code as ascii_code
import Basics.Functions.function_with_loop as function_with_loop
import Basics.Functions.function_with_nesting as function_with_nesting
import Basics.Functions.function_with_parameter as function_with_parameter
import Basics.Functions.function_with_parameters as function_with_parameters
import Basics.Functions.multiple_functions as multiple_functions
import Basics.Functions.return_values as return_values
import Basics.Functions.simple_function as simple_function
import Basics.Functions.function_calls as function_calls
import Basics.Modules.guess_the_number as guess_the_number



def run_block_a():
    print("\nWhich program in 'Block A: Basics' do you wish to run?")
    response = input()
    if (response == "simple_message"):
        simple_message.run()
    elif (response == "multiline_message"):
        multiline_message.run()
    elif (response == "escape_characters"):
        escape_characters.run()
    elif (response == "ascii_art"):
        ascii_art.run()
    elif (response == "data_types"):
        data_types.run()
    elif (response == "user_input"):
        user_input.run()
    elif (response == "string_operators"):
        string_operators.run()
    elif (response == "overall_review"):
        overall_review.run()
    elif (response == "simple"):
        simple.run()
    elif (response == "len"):
        len.run()
    elif (response == "factorial"):
        factorial.run()
    elif (response == "count"):
        count.run()
    elif (response == "sum_user_numbers"):
        sum_user_numbers.run()
    elif (response == "sum_100"):
        sum_100.run()
    elif (response == "ascii"):
        ascii.run()
    elif (response == "simple_for"):
        simple_for.run()
    elif (response == "reverse"):
        reverse.run()
    elif (response == "range_for"):
        range_for.run()
    elif (response == "membership_operators"):
        membership_operators.run()
    elif (response == "count_down"):
        count_down.run()
    elif (response == "characters"):
        characters.run()
    elif (response == "and_operator"):
        and_operator.run()
    elif (response == "or_operator"):
        or_operator.run()
    elif (response == "review"):
        review.run()
    elif (response == "nestception"):
        nestception.run()
    elif (response == "nested"):
        nested.run()
    elif (response == "bot"):
        bot.run()
    elif (response == "bot_counter"):
        bot_counter.run()
    elif (response == "if_elif_else_bot"):
        if_elif_else_bot.run()
    elif (response == "modulo_operator_bot"):
        modulo_operator_bot.run()
    elif (response == "if_else"):
        if_else.run()
    elif (response == "if_if"):
        if_if.run()
    elif (response == "ascii_character"):
        ascii_character.run()
    elif (response == "ascii_code"):
        ascii_code.run()
    elif (response == "functions_with_loop"):
        function_with_loop.run()
    elif (response == "functions_with_nesting"):
        function_with_nesting.run()
    elif (response == "functions_with_parameter"):
        function_with_parameter.run()
    elif (response == "functions_with_parameters"):
        function_with_parameters.run()
    elif (response == "multiple_functions"):
        multiple_functions.run()
    elif (response == "return_values"):
        return_values.run()
    elif (response == "simple_function"):
        simple_function.run()
    elif (response == "function_calls"):
        function_calls.run()
    elif (response == "nested_loop"):
        nested_loop.run()
    elif (response == "nesting"):
        nesting.run()
    elif (response == "guess_the_number"):
        guess_the_number.run()
    
    
    
    
    
    
    



def run():
    is_running = True

    while(is_running):
        print("\nWhat would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()