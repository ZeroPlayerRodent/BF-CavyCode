def main():
    
    bf_code = "+.[+.]"

    tape_size = 30000

    c_bracket = 0
    brackets = []

    print("eat-hay", tape_size)
    print("mark-territory 0")
    print("eat-pellet 0")
    print("chatter 1")
    print("popcorn-if 0 zoomies-to 0")

    for i in [*bf_code]:
        if i == "+":
            print("eat-hay 1")
            print("popcorn-not 256 chatter 256")
        elif i == "-":
            print("chatter 1")
            print("popcorn-not -1 eat-hay 256")
        elif i == ">":
            print("eat-pellet tunnel poop")
        elif i == "<":
            print("groom-self")
            print("eat-pellet tunnel poop")
            print("groom-self")
        elif i == ",":
            print("chatter tunnel")
            print("eat-hay beg-char")
        elif i == ".":
            print("wheek-char tunnel")
        elif i == "[":
            c_bracket += 2
            brackets.append(c_bracket)
            print("mark-territory", c_bracket)
            print("popcorn-not 0")
            print("zoomies-to", c_bracket + 1)
        elif i =="]":
            print("popcorn-if 0")
            print("zoomies-to", brackets[-1])
            print("mark-territory", brackets[-1] + 1)
            del(brackets[-1])

if __name__ == "__main__":
    main() 
