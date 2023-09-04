import argparse


emote_dictionary={
    "bored":"""
    \\
     \\
      \\  ()__()
         (-.- )
        (")("))\u2184""",

    "happy":"""
    \\
     \\
      \\  ()__()
         (^.^ )
        (")("))\u2184""",

    "mad":"""
    \\
     \\
      \\  ()__()
         (>o< )
        (")("))\u2184""",

    "shock":"""
    \\
     \\
      \\  ()__()
         ('o' )
        (")("))\u2184""",

    "cry":"""
    \\
     \\
      \\  ()__()
         (T.T )
        (")("))\u2184""",

    "sad":"""
    \\
     \\
      \\  ()__()
         (u.u )
        (")("))\u2184""",
        
    "greedy":"""
    \\
     \\
      \\  ()__()
         ($.$ )
        (")("))\u2184"""}


def wrap_lines(words):
    lines = []
    max_width=46
    fin_str,temp_str=words[0],""
    for i in range(1,len(words),1):
        if (len(fin_str)+len(words[i]))<max_width:
            temp_str=" ".join([fin_str,words[i]])
            fin_str=temp_str[0:]
        else:
            lines.append(fin_str)
            fin_str,temp_str=words[i],""
    lines.append(fin_str)
    return lines


def generate_text_bubble(text):
    text=" ".join(text)
    words = [i.strip() for i in str(text).split(" ")]
    lines = wrap_lines(words)
    text_width = max([len(i) for i in lines])
    output = []
    output.append("  " + "_" * text_width)
    if len(lines) > 1:
        output.append(" /" + " " * text_width + "\\")
    for line in lines:
        output.append("| " + line + " " * (text_width - len(line) + 1) + "|")
    if len(lines) > 1:
        output.append(" \\" + " " * text_width + "/")
    output.append("  " + "-" * text_width)
    return output


def generate_bunny(char, text_width):
    output = []
    char_lines = char.split("\n")
    char_lines = [i for i in char_lines if len(i) != 0]
    for line in char_lines:
        output.append(" " * text_width + line)
    return output


def draw(char, text):
    output = generate_text_bubble(text)
    text_width = max([len(i) for i in output]) - 4
    output += generate_bunny(char, text_width)
    for i in output:
        print(i)
    return '\n'.join(output)


def get_output_string(emote, text):
    if emote in emote_dictionary:
        return draw(emote_dictionary[emote], text)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--emote", default="bored", help="choose different emote for bunny")
    parser.add_argument("text", nargs="*", default="Default Text")
    args=parser.parse_args()
    if args.emote in emote_dictionary.keys():
        get_output_string(args.emote,args.text)
    else:
        print(list(emote_dictionary.keys()))


main()