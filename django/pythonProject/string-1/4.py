def make_out_word(out, word):
    return out[:2] + word + out[2:]

print(make_out_word('<<>>', 'Yay'))      # Output: '<<Yay>>'
print(make_out_word('<<>>', 'WooHoo'))  # Output: '<<WooHoo>>'
print(make_out_word('[[]]', 'word'))    # Output: '[[word]]'