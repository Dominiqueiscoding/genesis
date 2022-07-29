import json

# These functions have intentionally been left barebones so you can make the code your own
# And use it as you please. This should help with keeping track of results.

def file_writer():
    '''
        Function to take a dictionary and write it to a json
    '''
    test_dictionary = {
        "Mitra" : "is",
        "the" : "best"
    }

    dumper = json.dumps(test_dictionary)
    with open("TestDictionary.json", 'w') as f:
        f.write(dumper)
        f.close()

def file_reader():
    '''
        Function to take a json and make it a dictionary
    '''
    test_dictionary = dict(json.load(open("TestDictionary.json")))
    print(test_dictionary)

# Good example of how to use main as a way to execute code with more control than just 
# Writing them in the file.

if __name__ == "__main__":

    # Uncomment down here to run functions individually

    # file_writer()
    # file_reader()
