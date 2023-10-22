import pygad
import random
import math

# Given text containing emojis and other characters.
text = "😗😎 👻🤕🐥 😉💔😌 💀❌🤒🔒 🐧😝🤑🐱 🍒🤐🤢🐧 🤑😍 😁👿🤒⚽🤠 🍒😝🤒🐧 👻🤕🐥 😝🤒😜🥰 🤠🐥🌸🌸💻🐱🤠😎🐥🧐🤧👻 🍊👿😉🤑😙💚😇🤖🤐🐌 😚🙂 😄⌛🍊 👻🤨🐥 🌹🤑🤧🧐 🐼🥰 😄🌹💔👽🔒🎃🍊 😄😅 💻🤢😍💀💡 😙🤕😗⚽🍒 😚😎 😘😷🐥 🤒🤖💻 🙂😝💻 😎😚💀🤠🍐 🤨😅❌ 🤕😎 😉🤨🚄👽🐱❌ 💡😀🚗🖤😍 😎👽🤕😁 🍐😈🤑🐱 😙😷😚⚽🍒 🍒🐶❌ 😀🚗😗⌛ 😚☠ 😍😝😄🙂 🍒😝🎃💀👿 🚗👽❌ 😁💔⌛👻 😙🤕🤑⌛🙂🐱 😗😅 ❌😜🥰🖤😘🤨😅🎃 🧐😗😎🎃 🙂😈💔😍 👽❌😁💡😚😌 🎃⚽🌸🤖😘😀🐧💻🐌 🤑😅 🐶😚🐱 💚👿🚗🤖🐧 🚄😌🍐😚🤧 🍒🐶👿 🍊💔😘 🤕😎 🤮🚄🍊🍌😁❌😅🐧 🤒 😙🎃🤖🐱🤕😅 🌸🤒😅 😌🤐😜❌🤖 🐼❌ 🤮🐥🐌🍌❌🐌 🤨⌛🧐👻 🐼😘 😍😈🤐 🌹😷🖤🔒🤠 😍😈👿👻 🤠💔👻 😍😈😇 🍒😝🤑⌛🍌☠ 🐧💚🤐😘 🐌😷 💔⚽🔒 🐧😈❌ 😉🐶🤨😗🌸❌🐱 🐧😈❌👻 💔💀🎃 😎🤕🖤🌸👿🐌 😍🤕 😁🤒🍎🎃 😝🤨🌹 😁💡⌛👻 😙🥰🤕😀🧐🎃 🐼🚄💀😗🥰🔒 🐱😇🌸🤖😇😍🐱 💔⌛🔒 🔒💻🐱🤑🤖😇🐱 😗😅 🐧😝❌😗🤖 😝❌💡💀🙂🤠 🐥⌛🙂😗🤧 🙂💚🥰 👿⚽🔒 🚗⌛🐌 😉🤕🚄🧐🔒 😌🤨😍 🖤😇💔😉😈 🍒💚👿😛 🖤👿🍌💀🥰🍒 💔🙂 😍😝😇 🎃😌🔒 🌹🥰 🐥☠❌ 🐱🤨😛😇 😛💻💡⌛😗⌛🍌🤧😇🤠🤠 🌹😷🖤🍊🐱 🍐🤕 😛😗🤠🧐🥰💡🔒 😘🤕🐥 ❤🤢🤮🍎😜 🚗🐼🌹🍌🤖 😈🍎❤🐼🌹🤢🤮😜💔 🤖🤮❤🤢🍎❤ 💡🤢🤮🍎❤ 😙🧐❌🤒🤠🥰 🤠💻😌🔒 😁🤐 🍐😈😚🐱 🐧👿🤢😍 🍐😷 😁👻 🤐😁🚗😗🧐 🐧🐶😇 😍😚🍐🤧👿 🤨😎 😍💚🎃 😛😄😗🤧 🤠💚🤕🐥🧐🐌 🐼🤐 🙂🐶😇 🌸🤖🤕🌹☠ 🤒💀❌ 🌸🤨😌🐱😙🤑💀😚😅🍌"

chars = dict()
for c in text:
    if c == ' ' or (ord(c) > ord('a') and ord(c) < ord('z')):
        continue
    if c not in chars:
        chars[c] = len(chars)
print(chars)
words_freq = dict()
with open('unigram_freq.csv') as wf:
    for i, line in enumerate(wf):
        if i == 0:
            continue
        word, freq = line.strip().split(',')
        words_freq[word] = math.log(float(freq) * len(word) / 12711.)

def replace_text(gene):
    new_text = list(text)
    for i, c in enumerate(new_text):
        if c == ' ' or (ord(c) > ord('a') and ord(c) < ord('z')):
            continue
        new_text[i] = chr(ord('a') + gene[chars[c]])
    return ''.join(new_text)

def fitness_fun(solution, solution_idx):
    new_text = replace_text(solution)
    fit = 0
    for i, word in enumerate(new_text.split()):
        if word in words_freq:
            fit += words_freq[word]
    return fit

ga_instance = pygad.GA(num_generations=1000,
                       num_parents_mating=150,
                       fitness_func=fitness_fun,
                       sol_per_pop=700,
                       gene_type=int,
                       num_genes=62,
                       init_range_low=0,
                       init_range_high=25,
                       mutation_probability=0.05,
                       mutation_type="random",
                       mutation_by_replacement=True,
                       random_mutation_min_val=0,
                       random_mutation_max_val=25)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(replace_text(solution))

ga_instance.plot_fitness()
