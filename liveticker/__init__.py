def translate_string(line: str) -> tuple[str, int]:
    line = line.strip().lower().replace(".", "")
    for keyword in KEYWORDS:
        if keyword[0] in line:
            return eval(keyword[1] + "(line)")
    return line.replace(" ", "_"), 0


KEYWORDS = [
    ("says", "print_string"),
    ("calls for", "print_variable"),
    ("referee", "end_block"),
    ("plays with", "new_function"),
    ("while", "while_loop"),
    ("if", "if_branch"),
    ("and", "and_connector"),
    ("is better than or as good as", "is_better_than_equals"),
    ("is better than", "is_better_than"),
    ("is worse than or as good as", "is_worse_than_equals"),
    ("is worse than", "is_worse_than"),
    ("gets the ball", "return_statement"),
    ("is not on the pitch", "assignment_zero"),
    ("has the number", "assignment_number"),
    ("scores a goal", "add_one"),
    ("new kickoff", "continue_statement"),
    ("including", "function_call"),
    ("scores no goal", "is_zero"),
    ("gets as many goals denied", "subtraction")
]

arguments = [
    "the_first",
    "the_second",
    "the_third",
    "the_fourth",
    "the_fifth",
    "the_sixth",
    "the_seventh",
    "the_eight",
    "the_ninth"
]


def subtraction(line):
    return translate_string(line[:line.find("gets as") - 1])[0] + " -= " +\
           translate_string(line[find_2nd(line, "as") + 3:])[0], 0


def find_2nd(string, substring):
    return string[string.find(substring) + len(substring):].find(substring) + string.find(substring) + len(substring)


def print_string(line):
    return 'print("' + line[line.find("says") + 6:len(line) - 1] + '")', 0


def print_variable(line):
    return 'print(' + line[line.find("calls for") + 10:].replace(" ", "_") + ')', 0


def end_block(_):
    return "", -1


def new_function(line):
    function_name = line[:line.find("plays with") - 1].replace(" ", "_")
    code = "def " + function_name + "("
    arg_count = int(line[line.find("plays with") + 11:line.find("plays with") + 13])
    for i in range(arg_count):
        if i != 0:
            code += ", "
        code += arguments[i]
    code += "):"
    return code, 1


def while_loop(line):
    return "while " + translate_string(line[line.find("while") + 6:])[0] + ":", 1


def if_branch(line):
    return "if " + translate_string(line[line.find("if") + 3:])[0] + ":", 1


def is_better_than_equals(line):
    return comparison("is better than or as good as", ">=", line)


def is_better_than(line):
    return comparison("is better than", ">", line)


def is_worse_than_equals(line):
    return comparison("is worse than or as good as", "<=", line)


def is_worse_than(line):
    return comparison("is worse than", "<", line)


def and_connector(line):
    return comparison("and", "and", line)


def comparison(compare_string, replacement, line):
    return translate_string(line[:line.find(compare_string) - 1])[0] + " " + replacement + " " + \
           translate_string(line[line.find(compare_string) + len(compare_string) + 1:])[0], 0


def return_statement(line):
    return "return " + line[:line.find("gets the ball") - 1].replace(" ", "_"), 0


def assignment_zero(line):
    return line[:line.find("is not on the pitch") - 1].replace(" ", "_") + " = 0", 0


def assignment_number(line):
    return line[:line.find("has the number") - 1].replace(" ", "_") + " = " +\
           line[line.find("has the number") + 15:], 0


def add_one(line):
    return line[:line.find("scores a goal") - 1].replace(" ", "_") + " += 1", 0


def continue_statement(_):
    return "continue", 0


def function_call(line):
    return (line[:line.find("including") - 1] + line[line.find("("):line.find(")") + 1]).replace(" ", "_") +\
           translate_string(line[line.find(")") + 2:])[0], 0


def is_zero(_):
    return " == 0", 0
