import sys

def main(filename, col_width):
    ascii_input = open(filename, 'r').read()

    if len(filename.split(".")) > 1:
        out_file = ".".join(filename.split(".")[:-1]) + ".ook"
    else:
        out_file = filename + ".ook"
    print out_file

    ascii_output = ""
    prev_char = 0

    for char in ascii_input:
        cur_char = ord(char)
        if cur_char - prev_char < 0:
            ascii_output += "Ook. Ook. "*abs(cur_char-prev_char) + \
                "Ook! Ook? Ook. Ook? Ook! Ook! Ook? Ook. Ook! Ook! Ook? Ook! Ook. Ook? Ook! Ook. Ook? Ook. "
        elif cur_char - prev_char > 0:
            ascii_output += "Ook. Ook. "*(cur_char-prev_char) + \
                "Ook! Ook? Ook. Ook? Ook. Ook. Ook? Ook. Ook! Ook! Ook? Ook! Ook. Ook? Ook! Ook. Ook? Ook. "
        elif cur_char == prev_char:
            ascii_output += "Ook. Ook? Ook! Ook. Ook? Ook. "
        prev_char = cur_char

    ascii_output = "\n".join([ascii_output[i:i+col_width] for i in xrange(0,len(ascii_output),col_width)])

    open(out_file, "w").write(ascii_output)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))