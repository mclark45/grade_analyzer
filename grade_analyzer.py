scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# create dictionary for the grades
grade_buckets = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "F": []
}

# takes a score and gets its letter grade value
def get_bucket(score):
    if 90 <= score <= 100: return "A"
    if 80 <= score <= 89: return "B"
    if 70 <= score <= 79: return "C"
    if 60 <= score <= 69: return "D"
    return "F"

#get total number of scores and initialize other variables
total_scores = len(scores)
total_unaveraged_score = sum(scores)
highest = max(scores)
lowest = min(scores)
passing = 0
failing = 0

# loop through scores
for score in scores:
    bucket = get_bucket(score)
    grade_buckets[bucket].append(score)
    if bucket == "F":
        failing += 1
    else:
        passing += 1

# calculate average and pass/fail rate
average_score = total_unaveraged_score / total_scores
pass_rate = passing/total_scores * 100
fail_rate = failing/total_scores * 100

# print out the information
print("=== Grade Analyzer ===")
print(f"Total scores: {total_scores}")
print(f"Average: {average_score:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Passing: {passing} ({pass_rate:.1f}%)")
print(f"Failing: {failing} ({fail_rate:.1f}%)\n")

print("Grade Distribution:")
for grade, bucket in grade_buckets.items():
    print(f"{grade}: {len(bucket)} students")

print("\n--- Add More Scores ---")

# loop while user wants to add scores
while True:
    # ask what user wants to do
    choice = input("Enter a score (or 'done' to finish): ").strip()

    # end if user is done
    if choice.lower() == "done":
        break

    try:
        # convert string to int
        num = int(choice)

        if not 0 <= num <= 100:
            print("Score must be between 0 and 100.")
            continue

        # update main list
        scores.append(num)
        total_unaveraged_score += num
        total_scores += 1

        # update highest and lowest
        highest = max(highest, num)
        lowest = min(lowest, num)

        # update grade distribution
        bucket = get_bucket(num)
        grade_buckets[bucket].append(num)

        if bucket == "F":
            failing += 1
        else:
            passing += 1

        # calculate new average and print it out
        average_score = total_unaveraged_score / total_scores
        print(f"Updated average: {average_score:.1f}")
    except ValueError:
        # tell user there input was wrong
        print("Invalid input. Enter an integer or 'done'.")

# print final average
print(f"\nFinal average: {average_score:.1f}")
