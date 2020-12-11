import argparse
import liveticker


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
        a, b = liveticker.translate_string(line)
        source += a
        indentation += b

    return source


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default=None)
    args = parser.parse_args()

    content = read_source_code(args.file)
    code = transform_code(content)
    print(code)
    exec(code)
