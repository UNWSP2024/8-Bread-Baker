# Name: Ariana Fafach
# Date: 3/17/2026
# Title: Program #1: Initials


# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11


def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    
    # Creat a list where each value is one of the names.
    name_list = personsName.split(' ')
    
    for i in name_list:
        
        # Get the first letter of each name and capitalize it.
        initials = i[0].upper()
        # Append each initial onto the personsInitials string, along with a period and a space between each one.
        personsInitials += initials + '. '

    # Return the personsInitials string and strip off all leading and trailing whitespaces.
    return personsInitials.strip()

# Example usage
if __name__=="__main__":
    
    personsName = input('Enter the users first, middle, and last name: ')

    initials = initials_generator(personsName)

    print(initials)
