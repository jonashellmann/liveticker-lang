import argparse


def read_source_code(filename: str) -> list[str]:
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def transform_code(lines: list[str]) -> str:
    source = ''
    indentation = 0

    for line in lines:
        source += "\n" + "\t" * indentation
        if "says" in line:
            source += 'print("' + line[line.find("says") + 6:len(line) - 1] + '")'

    return source


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default=None)
    args = parser.parse_args()

    content = read_source_code(args.file)
    code = transform_code(content)
    exec(code)
