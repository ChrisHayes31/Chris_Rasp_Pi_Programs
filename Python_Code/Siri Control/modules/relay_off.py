#You can import any modules required here

#This is name of the module - it can be anything you want
moduleName = "off"

#These are the words you must say for this module to be executed
commandWords = ["relay","off"]

#This is the main function which will be execute when the above command words are said
def execute(command):
    #print("\n")
    print("-sending to Node Red- turn relay off")
    #print("\n")
