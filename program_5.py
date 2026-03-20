# Name: Ariana Fafach
# Date: 3/20/2026
# Title: Program #5: Course Info


# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.


def make_dictionary():
    
    # Define course_dictionary:
    course_dictionary = {}

    # Initialize y as 'yes'
    y = 'yes'
    # 'while' loop iterates over the following code until the user types somthing other than 'yes' as an answer:
    while y == 'yes':
        # Get user input for the course ID:
        course_ID = input("Enter the course ID (example: 'COS 2005'):  ")
        # Get user input for the course name:
        name =  input ("Enter the name of that course (example: 'Python Programming'):  ")

        # Add the course ID and name to the course dictionary as long as the course ID is not already in the dictionary:
        if course_ID not in course_dictionary:
            course_dictionary[course_ID] = name
        # If the course ID is already in the dictionary, tell the user:
        else:
            print("You already added that course ID.")

        # Ask user if they want to add another course ID, course name pair:
        y = input("Would you like to enter another course ID, course name pair? Enter yes or no:  ")

    return course_dictionary


def display_subjects(course_dictionary):

    # Get the subject from the user:
    subject = input("Enter the subject (example: 'COS'):  ")
    
    # Iterate through the course dictionary and make a new dictionary of all the key value pairs where the key contains the subject that the user just entered:
    for key in course_dictionary:
        chosen_subject = {k:v for k, v in course_dictionary.items() if subject in k}
    # Print first part of the message:
    print (f"Your courses with the subject '{subject}' are:")
    #  Print the rest of the message:
    for key in chosen_subject:
        print (key, chosen_subject[key])

# Call both functions:
course_dictionary = make_dictionary()
display_subjects(course_dictionary)



