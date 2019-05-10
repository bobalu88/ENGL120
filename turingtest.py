import random

'''
Robert Zahn 2019
ASCII art generated with manytools.org/hacker-tools/convert-image-to-ascii-art
Full list of alien responses on line 102
Responses go in order of:
    Visual description of the alien
    Responses to actions 1-9 (in order)
    Consequences of attacking IF relevant
    Consequences of taking too long if relevant or empty string if not relevant
    Analysis/description
'''

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
        if 9 not in options and len(alien) is 13:
            print(alien[-3])
        if len(options) < 4:
            print(alien[-2])
        else:
            print()
    else:
        act(options, alien)

print("Welcome to the Turing Test Simulation!\n\
                                       */(#%#%%%%%&&%&&&%%,                  \n\
                                  .***###%%&&%@&@&&%&&&&&@@&&%%.               \n\
                                /#(##&@@&&@&@@@@@@@@@@@@@@@@@@@@%.             \n\
                              (&@&@@@@@@@@@@@@@@@@@@@@@&(//%&&@&@@,            \n\
                             &&@&@@@@@@@&&&&&&%#/(((/*##&&&&&@@#&(           \n\
                            .@@#@@@%(,,..,,..........,#&@@&@&@&@@@&&%          \n\
                            @@@@*.       .......,,.,,,,%%@@@@@@@@@@@@&         \n\
                            @@@..     .......,,,..,,,,*(&@@@@@@@@@@@@@.        \n\
                            @@.        .....,,,,,,,**//#&&@@@@@@@@@@@@/        \n\
                            #*     .   ....,,,,,,,**////#%&&&@@@@@@@@@*        \n\
                            /.        .,,*****,******///#%%%&&&&&@@@@@.        \n\
                            ,**,..,,.,*##%&%&%%%%////////###%#%##&&@@@.        \n\
                            .#&@@@(*/#@@@@@@@@@%&&%#(//**//((((**,,,%*         \n\
                             ,@&@@&.,*%@@@@@@&@@(#((/*//*/((,,%%*##/         \n\
                              .,,,.,**,**/,,***,,,,********////%,,.***        \n\
                              .....,**,,,,,,,,,,,,,******///*,,###,*,,         \n\
                              .. .,,**,,,,,,..,,,***////////*,/(****           \n\
                              ..(#%&&%(/***,,,,***///((/(((/*/*,((/            \n\
                               ..,*((/**,,,////**/////(//////,,,*.             \n\
                               ,..,,,,*/**/**(((((/(((///((((&%&%              \n\
                               .,/**((((#%%(//(((((((((((((#((%##              \n\
                               ./,.,,*/(/((&(((((((((((((###(#%&,            \n\
                                ,.*%&&@/*(####(#((((#####%%#(/*&&/           \n\
                                ,...,,,***((#(###(((####%&&%#(/*,%%&%,.        \n\
                            .....,,*****(((###%%%#%%&&&&@&%((//*#&&%&%#//,.    \n\
                           .......(%##%&&&&@@@@@@@@@@@@&%#((/,*#&&%&%#&%#/#/*/*\n\
                         ..............*/*&@@@@@@@@@@&%#(//,*//&&&&%#%&&%%#%%%(\n\
                       ............,/(/*##,/#&@@@@&%%#(/**/,,(&@@%&%%%%%%%#%#\n\
                      ........,/((%(((#@.,&,*/#&&%%##//***,,(&&&&&&&%&%%%&&@#%#\n\
\n-------------------------------\
\nIn this training module, you will encounter various unidentified entities. \
As an interplanetary scout, it is your job to determine whether or not these entities qualify for human rights under Title 3 Article 14 of the Neonairobi Accords.\
\nRemember, it is important for you to identify dangerous entities quickly in order to develop an informed interaction strategy. \
However, incorrect assessments can also lead to wasted resources and violations of interplanetary law, so be sure to use your universal translator and biometric scanner to assess each entity carefully. \
\nFor the purposes of this exercise, the individuals you encounter will be truthful and complacent. \
You will practice responding to less trustworthy entities in future modules.\
\n-------------------------------\
\nPress enter to begin. Press Ctrl+C at any time to quit.\
\n-------------------------------\
")
start = input()

aliens = [
    [
    "It appears to be a juvenile homo sapiens. It looks sickly.",
    "Don't be fooled by appearances. ",
    "Good choice. ",
    "It stares at you with wide eyes, but does not answer.",
    "Its hands wave vaguely, but your universal translator does not find any intentional message in its movements.",
    "It doesn't respond.",
    "It eats meat.",
    "It reproduces by biting other beings which causes them to transform to one of its kind.",
    "It is ten years old.",
    "It stares blankly at you. It does not seem to affected by its injuries.",
    "Unfortunately, you took too long in your decision, and the zombies attacked some of your fellow explorers. Legally, they were justified in their self-defense, but they won't have fun filling out the paperwork to prove it, lowering team morale.\n",
    "This is a zombie (The Walking Dead, 2010), hostile, asocial, and incapable of reasoning or emotion. As zombies are unable to communicate, they are assumed to lack a consciousness or sense of self, and thus are not afforded human rights according to Section 2b of Article 14."
    ],
    [
    "It is about eight feet in height. Its limbs are proportionate to that of a homo sapiens. It has yellow skin, lustrous black hair, pale watery eyes, and a shrivelled complexion.\n\
    ......../@@@@&&/......                         ...(&@#@@,,,,,,........\n \
    . ......%@@@@%&*#*..  ,     . ,,                 .%(@@@@,,,..........      \n\
     .......(@@@@@%(*,   .#%%%@%&&&&&&&&&&&&@@@@&%/   %#@@@@*.........         \n\
       ...../@@@@@*/. *#%%@@@@@@@@@@&%#&@@@@@@@@@@@&&, & @@@/.........         \n\
       ... .%@@@@@@(.#%&%&*,,,/(%@%  /&@@@(**,*/&&@&@*%@@@.......            \n\
         . .,@@@@@@/&&@&%/,@@@@&@#*#     %(@@@@@@#(&&%@@%@@&.....              \n\
            .*@@@@@%%%(/@@@@%##      ,%(/#&&@@@@#%&@,#@(....               \n\
             .@@@@@,#//**(#(%##(*#        &((/(/(%%(((#@ @@#.                 \n\
             ,@@@@%##(/**/*/***** *((//(%%,*//(/#%/,**/# @@&                   \n\
           .@@%&&@.,%#/***///,*,(%@@@@@@@@@&,//,*/***/%&%,&/@@(                \n\
           (#&%@&&%#/(/((,,.&&//#@@@@@&@(*,/**//(#%&&&@@@#/                \n\
           *(%/(@&%&%%##%(%%/******,,,*,*(/( /*/(((((##%%&@#%,/               \n\
           .%%//%%&&%#((#(%#(/  /***,,,,,/*,   ///((//#&&@@(%/.                \n\
            /%//*&&&&&(/&%##%(,.*****,,*//(,(/.,/((/*/#%%@@,#/                 \n\
             (#/*#&%%&&%%%#%##((&@@@@@@@@@&///*/*/(%&@(//                  \n\
             ,#&&(,%##%&&%%@@%(,,,**,,//*/%,  ,*//(#&&%#,                 \n\
              (%#%&,%%*%/*##(/(##/********/,..     *(/#%&%%/                \n\
                   ./#&%**//*,*/***/*,,**////,.* .,,%#%&                      \n\
                   . &%&(*/**,*(/**,,,,,*,. ,*, ..*#%%&                        \n\
                    .@&@#///* ****,*,,,,       ./(#%&&(                        \n\
              .     .@@@@%(%(/,..*//*,*,.,,*,..(%&@@@@&                        \n\
        .... ...     #@@@@@&&%##(/(((((((##%##&@@@@@@@*                        \n\
        ........ ,,*.#(@@@@@@@@@@&%&&&&&&@@@@@@@@@@@@@@&...                   \n\
     .........../   *%#(/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&**.                   \n\
    .. ........ %@@%##/((@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                       \n\
      ...........  @@%##((###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                   \n\
      .......... %@@&&%%(((#####@@@@@@@@@@@@@@@@@@@@@@@@@@&&                 \n\
      ........#@@@@@%&%%#((#(%#%%#&@@@@@@@@@@@@@@@@@@&&&@@@@@%#(,             \n\
        .,*%@@@@@@@@&&&%%#%%%%%%%%&&%##(#&@@@@@@@@&&&&&@@@@@@%%###(.          ",
    "Good choice.",
    "Don't be fooled by this being's terrifying appearance.",
    "It responds, \"I have no name.\"",
    "It sighs. \"I am lonely. I yearn for the company of another of my own kind.\"",
    "It replies, \"I am searching for others like me to keep me company.\"",
    "It eats roots and nuts.",
    "It is incapable of reproducing.",
    "It is two years old.",
    "It grows angry. \"I expected this reception,\" it cries. \"If you leave me in peace, I will be peaceful. If you attack me, I will glut the maw of death until it be satiated with your blood!\"",
    "Unfortunately, by attacking it, you have antagonized a dangerous enemy, and violated his rights.",
    "",
    "This is an intelligent, emotional, social creature (Frankenstein by Mary Shelley, 1818), and not hostile unless provoked. It is the only creature of its kind, but an official review has determined that it does indeed qualify for human rights."
    ],
    [
    "It appears to be an adult homo sapiens. Its face glistens with sweat.",
    "Good choice.",
    "Bad choice.",
    "\"Hi, my name is Mark,\" it responds.",
    "It smiles at you, \"I'm feeling well, thanks for asking.\"",
    "\"I am exploring. I am not searching for anything in particular, but merely curious about this part of the forest that I have never seen.\" It punctuates its vocalization with a sweeping arm gesture towards the forest around you.",
    "It has the same diet as a homo sapiens.",
    "It reproduces sexually, but can also reproduce by cloning.",
    "It is 20 years old.",
    "It cries out in pain and confusion.",
    "Unfortunately, by attacking unprovoked, you have violated Mark's rights, and must face punishment accordingly.",
    "",
    "This is Mark (Where Late The Sweet Birds Sang by Kate Wilhelm, 1976), a homo sapiens living on this sparsely-populated planet. While Mark was created through sexual reproduction, some of people in his village were created through cloning. All of them qualify for human rights."
    ],
    [
    "It is about 12 feet long. It has several sections, with a head at one end, four sets of limbs on each middle segment, with a stinger at the end of its tail.",
    "Good choice.",
    "Remember, a physical resemblance to homo sapiens is not required for human rights.",
    "\"My name is T'Gatoi,\" it responds.",
    "It replies, \"To tell the truth, I am worried. It is always stressful for your Terran to be N'Tlic. I will be relieved when this is over and my larvae have hatched.\"",
    "\"I am here on business,\" it responds. Its mouth moves as it vocalizes. \"Later today I am making a proposal for changes to Terran education on N'Tlic.\"",
    "It eats meat.",
    "It reproduces oviparously, by laying eggs.",
    "It is 118 years old.",
    "It seems surprised, but its surprise quickly turns to anger.",
    "Unfortunately, by attacking unprovoked, you have violated T'Gatoi's rights, and must face punishment accordingly.",
    "You took too long to make your decision. One of your fellow explorers was captured by Tlic and now you will have to negotiate her return. Fortunately, she is of a recognized and protected species on this planet, so she should not be harmed.\n",
    "This is T'Gatoi, a Tlic (Bloodchild by Octavia E. Butler, 1995). The Tlic are an intelligent, emotional, and social. However, they may need some assistance in learning to respect the rights of the homo sapiens on their planet."
    ],
    [
    "It appears to be an adult tursiops truncatus.\n\
                                  %%%%%##                                      \n\
                                   %%%%%%%##%###((((////((((#*                 \n\
                                   %%%%%%(((((((((//////*******/(#             \n\
                                  %##((#####(((#((((((((((######(//(#          \n\
                               .%#######%#########################(((((.       \n\
                             #####%%%%%%%%#%%%%%%%%%%%%%%%%%%%#######((((      \n\
                           ###%%%%%%%%%%%%%%%%%%%%%&%%%%%%%&%%%%%%%%###((#(    \n\
                        *###%#%%%%&&%%%%%%%%%%%%%########%%%&%####%(((#####(   \n\
                      *#####%&%%%%&&%%%%%%%%%&%%%##%%%%%&&&&&&&%%%%#####%%%%   \n\
                    ,####%%%%%%%&%%%%%%%%%%/        #&&&&&&&&       #####%%%   \n\
                   ###%&&&&&&&&&&%(               &&&&&&&%              ##(##  \n\
                 (##%&&&&&&&                                              /%#  \n\
                ##%&&&&&%                                                      \n\
               #%&&&&%                                                         \n\
              %%&&&                                                            \n\
         ,&&&@@&&                                                              \n\
     &&&&@@@&&%%%#                                                             \n\
  &&&&&@@@&.&&&%%.                                                             \n\
.(              /                                                              ",
    "Good choice.",
    "Remember, a physical resemblance to homo sapiens is not required for human rights.",
    "\"I'm Opo,\" it responds.",
    "\"I'm lonely,\" it responds. \"The other dolphins think I'm weird.\"",
    "\"I'm here to play with the human calves,\" it replies.",
    "It primarily eats fish and squid.",
    "It reproduces sexually.",
    "It is four years old.",
    "It cries out in pain.",
    "Unfortunately, by attacking unprovoked, you have violated Opo's rights, and must face punishment accordingly.",
    "",
    "This is Opo, a bottlenose dolphin. Dolphins are self-aware and intelligent, but for many years the homo sapiens (formerly known as humans) of their native planet took advantage of their playful, peaceful nature and lack of advanced translation technology to systematically oppress them. Fortunately, their human rights were later recognized, and they were one of the species to sign the Neonairobi Accords to help prevent future atrocities."
    ],
    [
    "It has four limbs. It prefers to move in a quadrupedal manner, but sometimes stands on its two rear limbs. It has some features of both homo sapiens and panthera pardus.",
    "Remember, while communication is a prerequisite for rights, it is not the only condition.",
    "Good choice.",
    "It growls and grimaces, but does not seem to know how to respond.",
    "\"Hunger,\" it growls.",
    "\"Hunt, kill, eat,\" it replies.",
    "It eats meat.",
    "Its reproductive abilities are unknown.",
    "It is two years old.",
    "It bares its sharp teeth in fear and anger.",
    "Unfortunately, by attacking it unprovoked you have violated its rights as a conscious being, as outlined in Title 3 Article 15 of the Neonairobi Accords.",
    "You took too long in your decision. Were this simulation uncontrolled, the creature would have grown impatient and attacked by now.\n",
    "This is one of Wang Ercwlff's infamous illegal experiments, inspired by creatures from ancient homo sapiens literature (The Island of Dr. Moreau by H.G. Wells, 1896). While it bears some resemblance to homo sapiens, and can communicate to an extent, it is asocial, lacks a tendency toward rational thought, and does not seem to have a strong sense of self. Furthermore, it is hostile and dangerous by nature, so it does not receive the benefits of non-hostile borderline entities as outlined in Section 18."
    ],
    [
    "It is a large silver cube, about 10 feet high, with various lights flickering across its surface.\n\
             .............             \n\
        ........................       \n\
       ,,,,,, ...........,******       \n\
       ,,,,,,,,,,,,.************       \n\
       ,,,,,,,,,,,,,************       \n\
       ,,,,,,,,,,,,*************       \n\
       ,,,,,,,,,,,,*************       \n\
       ,,,,,,,,,,,,*********////       \n\
       ,,,,,,,,,,,,*********////       \n\
       ,,,,,,,,,,,,*****////////       \n\
           ,.,,....***//////.          \n\
               ....*////               \n\
                   .                   ",
    "Good choice.",
    "Remember, according to Section 2, inorganic entities still may qualify for rights.",
    "\"My name is _____.\" Its lights flicker in a unique pattern, but your universal translator fails to find a translation in your native language. \"However, you may think of me as Riley.\"",
    "\"I am restless,\" it responds. \"I think I may request to be moved soon.\"",
    "\"I enjoy the lack of gravity, and the view is magnificient.\" Its lights flicker in a chuckle. \"Unfortunately, I had not considered that most entities would be less willing to visit me out here in space.\"",
    "It does not eat.",
    "It does not reproduce.",
    "It is 39 years old.",
    "Its lights flicker in a sigh. \"Well, I guess it's good to know botphobia is still alive and kicking in the galaxy.\"",
    "Unfortunately, by attacking unprovoked, you have violated Riley's rights, and must face punishment accordingly.",
    "You took too long in your decision, wasting resources powering your spacesuit.\n",
    "This is Riley, an inorganic intelligence. Originally designed as a museum installation to amuse the native population of a planet in the outskirts of M31, Riley was freed when scouts much like yourself recognized their humanity. Now, they are an author and activist for the enforcement of inorganic entities' human rights on primitive planets."
    ],
    [
    "It appears to be an adult homo sapiens. Its face glistens with sweat.",
    "Don't be fooled by appearances.",
    "Good choice.",
    "\"Worker 46B 2982,\" it responds.",
    "\"Vitals are normal,\" it replies after a long pause.",
    "It seems confused. \"Group 46B is assigned to Operation Delta 4,\" it responds hesitantly.",
    "It has the same diet as a homo sapiens.",
    "It is infertile, but can be cloned.",
    "It is 17 years old.",
    "It cries out in pain.",
    "Unfortunately, by attacking it unprovoked you have violated its rights as a conscious being, as outlined in Title 3 Article 15 of the Neonairobi Accords.",
    "",
    "This is a worker clone (Where Late the Sweet Birds Sang by Kate Wilhelm). While it has been taught to identify itself by serial code, it lacks an individual sense of self and an ability to generate new knowledge."
    ],
    [
    "It appears to be an adult homo sapiens. It is standing very still.",
    "Don't be fooled by appearances.",
    "Good choice.",
    "It doesn't respond.",
    "It doesn't respond.",
    "It doesn't respond.",
    "It does not eat.",
    "It does not reproduce.",
    "It is 420 years old.",
    "It doesn't respond.",
    "Your fellow explorers notice your extensive consideration of the statue, and are beginning to question your competence.\n",
    "This is a painted marble statue of Dr. Melissa Littlefield, an ancient homo sapiens scholar. It has no communication or intelligence features."
    ]
]

actions = [
"",
"Complete assessment: Assign human rights",
"Complete assessment: Deny human rights",
"Ask it, \"What is your name?\"",
"Ask it, \"How do you feel?\"",
"Ask it, \"Why are you here?\"",
"Check your scanner, what does it eat?",
"Check your scanner, how does it reproduce?",
"Check your scanner, how old is it?",
"Attack it"
]

prev = -1
while True:
    curr = random.randint(0, len(aliens) - 1)
    while prev is curr:
        curr = random.randint(0, len(aliens) - 1)
    alien = aliens[curr]
    print(alien[0])
    options = []
    for i in range(1, len(actions)):
        options.append(i)
    act(options, alien)
    cont = ask("Would you like to continue training?", True)
    prev = curr
    if not cont:
        break
    print("-------------------------------\n")

