# Student Scores Analysis Program

def get_student_data():
    """Get student names and scores, returning a dictionary."""
    # Predefined list of students and scores
    students = {
        "Ayella": 87,
        "Bob": 73,
        "Charlie": 92,
        "David": 65,
        "Eva": 78,
        "Frank": 88
    }
    return students


def calculate_grade(score):
    """Return the grade based on the score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'


def class_statistics(scores):
    """Return minimum, maximum, and average score as a tuple."""
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)
    return min_score, max_score, avg_score


def sum_scores(n):
    """Recursive function to sum numbers from 1 to n."""
    if n <= 0:
        return 0
    else:
        return n + sum_scores(n - 1)


def main():
    students = get_student_data()
    scores = list(students.values())

    # Print each student with their score and grade
    print("\nStudent Scores and Grades:")
    for student, score in students.items():
        grade = calculate_grade(score)
        print(f"{student}: Score = {score}, Grade = {grade}")

    # Calculate class statistics
    min_score, max_score, avg_score = class_statistics(scores)
    print(
        f"\nClass Statistics:\nMinimum Score: {min_score}\nMaximum Score: {max_score}\nAverage Score: {avg_score:.2f}")

    # Filter top performers
    top_performers = filter(lambda item: item[1] > avg_score, students.items())
    print("\nTop Performers:")
    for student, score in top_performers:
        print(f"{student}: {score}")

    # User Interaction
    while True:
        print("\nMenu:")
        print("1. View All Student Grades")
        print("2. View Class Statistics")
        print("3. Add New Student")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            for student, score in students.items():
                grade = calculate_grade(score)
                print(f"{student}: Score = {score}, Grade = {grade}")

        elif choice == '2':
            min_score, max_score, avg_score = class_statistics(scores)
            print(
                f"\nClass Statistics:\nMinimum Score: {min_score}\nMaximum Score: {max_score}\nAverage Score: {avg_score:.2f}")

        elif choice == '3':
            new_student = input("Enter the student's name: ")
            new_score = int(input(f"Enter {new_student}'s score: "))
            students[new_student] = new_score
            scores.append(new_score)
            print(f"Added {new_student} with score {new_score}.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()