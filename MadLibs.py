#adlibs code
#you need to open the story.txt we made 
with open("MadLibsStory.txt", "r") as f: #with open opens up any file you need it toom then the story name then we have the type of editor we in we did r because r means read there is also w that means you can write over the file then f is basically the variable
    story = f.read()# basically the story which is our main variable now we have our story named as f so then if we f.read it will move that all into our new story variable

words = set() # we did this because we need to add all our empty words into something
start_of_word = -1 #haven't found the beginning of the any word
target_start = "<" # this is what we are trying to find all the missing words and it all has this beginning
target_end = ">" # same thing as the one above
#now trying to find all the missing words in our story
for i, char in enumerate(story):#what this is  loop to iterate over the characters in a variable called story enumarte just checks through characters
    if char == target_start:#when we find a word that starts with < then it will store into i
        start_of_word = i #will store in i

    if char == target_end and start_of_word != -1:# if the current character is the ending character of a word, and we have previously found the beginning of a word.
        word = story[start_of_word: i+1] #basically right here is where we take the word we want to replace. our word will equal the story and then index into the start of the word and then we found the end of the word
        words.add(word) # now it will append to the word list
        start_of_word = -1 #reset it because we found one whole world and now redo it.

#now up to this part of the code we have found all the missing words in our story
#we will change words=[] to words = set() because in a regular [] we can have dupilcates so then in a set its only one
    
#now we will want the missing words with answers we will make a dictionary
answers = {} #leave it as an empty dictionary

for word in words:# right here it will cycle through the missing words
    answer = input("Enter a word for " + word + ":") # right here it will ask for input for the missing word
    answers[word] = answer #now it will create a dictionary and it wll ask for each word then you will give an example'

for word in words:#now after we have all our answers we will replace the missing words
    story = story.replace(word, answers[word])#we will replace the missing word with the answers of the missing word
    # we had to make it a new story because this makes it the offical new story
print(story)

