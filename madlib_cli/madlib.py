###import regex###
import re

###Initial function definitions###

# Read and save template file.
def read_template(filename):

  #Is there a valid file with that name?
  try:
    with open(filename) as file:
      x = file.read()
      return x

  #spit out a file not found error if not.
  except:
    input("no file with that name found! press enter to continue.")
    raise FileNotFoundError



def parse_template(contents):

  regex = r"{(.*?)}"

  # make a list of all of our variables in the madlib template...
  all_parts_list = re.findall(regex,contents)
  # ... Then convert it to tuple
  all_parts = tuple(all_parts_list)

  # Make "stripped" a string that is our template with all madlibs replaced with empty {}s.
  stripped = re.sub(regex, "{}", contents)

  return stripped,all_parts

#
def prompt_for_responses(all_parts):

  user_responses_array = []
  for i in all_parts:
    user_responses_array.append(input(f"{i} >>> "))
  
  responses = tuple(user_responses_array)
  return responses




def merge(stripped, responses):
  regex = r"{}"

  #perform our regex on our stripped text file and substitute the blank {} for our "responses" (submitted madlib responses)
  for i in responses:
    stripped = re.sub(regex, i, stripped,1)

  return stripped


def save_to_txt(finalized_madlib):
    with open('output.txt', 'w') as file2:
      file2.write(finalized_madlib)

####Main body####


#opening prompt
filename = input('welcome to Casey\'s madlib!\n\nYou will be prompted to provide words, fitting into a category.\n\nFor example, if you see the prompt "a planet >>>" you could respond with "Earth" or "Mars" or any other.\n\nOnce you have completed all prompts, you will receive back a text file, that puts your answers into an assembled madlib!\n\nBut first, please enter the filename of your madlib template, or input read_template.txt for a pre-made one! \n>>> ')



#read the file, parse the file, and and save both the stripped out madlib and the component madlib prompts into stripped, and all_parts respectively.
stripped, all_parts = (parse_template(read_template(filename)))


#prompt the user for a response to each of the madlib parts (adjective,noun, number, etc.) and save as responses.
responses = prompt_for_responses(all_parts)


#Create the finalized string by merging in all of the responses into the stripped madlib.
finalized_madlib = merge(stripped,responses)


#create output.txt, which contains the finalized madlib string.
save_to_txt(finalized_madlib)


#return the finalized madlib to user, and tell them about the output file.
print(f"Your finalized madlib:\n\n {finalized_madlib} \n\nmadlib saved to output.txt!")

