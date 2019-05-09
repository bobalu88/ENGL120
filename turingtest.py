import random

def ask(question, answer):
    print(question, " [y/n]")
    response = input()
    if response in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
        if answer:
            print(response)
            return response in ['y', 'Y', 'yes', 'Yes', 'YES']
        else:
            return response in ['n', 'N', 'no', 'No', 'NO']
    else:
        print("Invalid input")
        return ask(question, answer)

def get_int(maximum):
    while True:
        response = input()
        try:
            num = int(response, 10)
            if num > 0 and num <= maximum:
                return num
        except:
            pass
        print("Invalid input. Try again: ")

def act(options, alien):
    print("\nChoose an action: ")
    for i in range(len(options)):
        print("{}: {}".format(i+1, actions[options[i]]))
    index = get_int(len(options)) - 1
    action = options[index]
    print(actions[action])
    print(alien[action])
    options.remove(action)
    if action in [1,2]:
        print(alien[-1])
        if 10 not in options and len(alien) is 14:
            print(alien[-3])
        if len(options) < 4:
            print(alien[-2])
        else:
            print()
    else:
        act(options, alien)

print("Welcome to the Turing Test Simulation!\
\n-------------------------------\
\nIn this training module, you will encounter various unidentified entities. \
As an interplanetary scout, it is your job to determine whether or not these entities qualify for human rights under Title 3 Section 14b of the Neonairobi Code.\
\nRemember, it is important for you to identify dangerous non-human entities quickly so they may be exterminated with maximum efficiency. \
However, incorrect assessments can also lead to wasted resources and violations of interplanetary law, so be sure to use your universal translator and biometric scanner to assess each entity carefully. \
\nFor the purposes of this exercise, the individuals you encounter will be truthful and complacent. \
You will practice responding to less trustworthy entities in future modules.\
\n-------------------------------\
\n\
")

aliens = [
    [
    "It appears to be a homo sapiens child. It looks sickly.",
    "Don't be fooled by appearances. ",
    "Good choice. ",
    "It lets out a moan.",
    "It stares at you with wide eyes, but does not answer.",
    "Its hands wave vaguely, but your universal translator does not find any intentional message in its movements.",
    "It doesn't respond.",
    "It eats meat.",
    "It reproduces by biting other beings which causes them to transform to one of its kind.",
    "It is ten years old.",
    "It stares blankly at you. It does not seem to affected by its injuries.",
    "Unfortunately, you took too long in your decision, and the zombies attacked some of your fellow explorers. Legally, they were justified in their self-defense, but they won't have fun filling out the paperwork to prove it, lowering team morale.\n",
    "This is a zombie (The Walking Dead, 2010), hostile, asocial, and incapable of reasoning or emotion."
    ],
    [
    "It is about eight feet in height. Its limbs are proportionate to that of a homo sapiens. It has yellow skin, lustrous black hair, pale watery eyes, and a shrivelled complexion.",
    "Good choice.",
    "Don't be fooled by this being's terrifying appearance.",
    "It responds, \"I have no name.\"",
    "It sighs. \"I am lonely. I yearn for the company of another of my own kind.\"",
    "\"Yes,\" it replies, \"Fairer creatures generally run from me in terror.\"",
    "It replies, \"I am searching for others like me to keep me company.\"",
    "It eats roots and nuts.",
    "It is incapable of reproducing.",
    "It is two years old.",
    "It grows angry. \"I expected this reception,\" it cries. \"If you leave me in peace, I will be peaceful. If you attack me, I will glut the maw of death until it be satiated with your blood!\"",
    "Unfortunately, by attacking it, you have antagonized a dangerous enemy.",
    "",
    "This is an intelligent, emotional, social creature (Frankenstein by Mary Shelley, 1818), and not hostile unless provoked."
    ],
    [
    "It appears to be a white male homo sapiens.",
    "Good choice.",
    "Bad choice.",
    "\"Hi, my name is Mark,\" it responds.",
    "It smiles at you, \"I'm feeling well, thanks for asking.\"",
    "It replies, \"Right now, yes. My village is just beyond the ridge in the valley.\"",
    "\"I am exploring. I am not searching for anything in particular, but merely curious about this part of the forest that I have never seen.\"",
    "It has the same diet as a homo sapiens.",
    "It reproduces sexually.",
    "It is 20 years old.",
    "It cries out in pain and confusion.",
    "Unfortunately, by attacking unprovoked, you have violated his rights, and must face punishment accordingly.",
    "",
    "This is Mark (Where Late The Sweet Birds Sang by Kate Wilhelm, 1976), a homo sapiens living on this sparsely-populated planet."
    ]
]

actions = [
"",
"Complete assessment: Assign human rights",
"Complete assessment: Deny human rights",
"Ask it, \"What is your name?\"",
"Ask it, \"How do you feel?\"",
"Ask it, \"Are you alone?\"",
"Ask it, \"Why are you here?\"",
"Check your scanner, what does it eat?",
"Check your scanner, how does it reproduce?",
"Check your scanner, how old is it?",
"Attack it"
]

while True:
    curr = random.randint(0, len(aliens) - 1)
    alien = aliens[curr]
    print(alien[0])
    options = []
    for i in range(1, len(actions)):
        options.append(i)
    act(options, alien)
    cont = ask("Would you like to continue training?", True)
    if not cont:
        break
    print("-------------------------------\n")

