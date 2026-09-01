scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# create list for each grade
a = list()
b = list()
c = list()
d = list()
f = list()

#get total number of scores and initialize other variables
total_scores = len(scores)
total_unaveraged_score = 0
highest = 0
lowest = 100
passing = 0
failing = 0

# loop through scores
for score in scores:
    # add score to total
    total_unaveraged_score += score
    # compare score to highest and adjust if needed
    highest = max(highest, score)
    # compare score to lowest and adjust if needed
    lowest = min(lowest, score)

    # place score in correct grade bracket
    if score >= 90 and score <= 100:
        a.append(score)
        passing += 1
    elif score >= 80 and score <= 89:
        b.append(score)
        passing += 1
    elif score >= 70 and score <= 79:
        c.append(score)
        passing += 1
    elif score >= 60 and score <= 69:
        d.append(score)
        passing += 1
    else:
        f.append(score)
        failing += 1

# calculate average and pass/fail rate
average_score = total_unaveraged_score / total_scores
pass_rate = passing/total_scores * 100
fail_rate = failing/total_scores * 100

# print out the information
print("=== Grade Analyzer ===")
print(f"Total scores: {total_scores}")
print(f"Average: {average_score:.1f}")
print(f"Highest: {highest}")
print(f"Loweset: {lowest}")
print(f"Passing: {passing} ({pass_rate}%)")
print(f"Failing: {failing} ({fail_rate}%)\n")
print("Grade Distribution:")
print(f"A: {len(a)} students")
print(f"B: {len(b)} students")
print(f"C: {len(c)} students")
print(f"D: {len(d)} students")
print(f"F: {len(f)} students\n")
print(f"--- Add More Scores ---")

# loop while user wants to add scores
while True:
    # ask what user wants to do
    choice = input("Enter a score (or 'done' to finish): ")

    # end if user is done
    if choice == "done":
        break

    try:
        # convert string to int
        num = int(choice)
        # append to scores list
        scores.append(num)
        # add num to unaveraged score
        total_unaveraged_score += num
        # increase total score count
        total_scores += 1
        # update highest and lowest score
        highest = max(highest, num)
        lowest = min(lowest, num)

        # update grade distribution
        if 90 <= num <= 100:
            a.append(num)
            passing += 1
        elif 80 <= num <= 89:
            b.append(num)
            passing += 1
        elif 70 <= num <= 79:
            c.append(num)
            passing += 1
        elif 60 <= num <= 69:
            d.append(num)
            passing += 1
        else:
            f.append(num)
            failing += 1

        # calculate new average and print it out
        average_score = total_unaveraged_score / total_scores
        print(f"Update average: {average_score:.1f}")
    except ValueError:
        # tell user there input was wrong
        print("Invalid input. Enter an integer or 'done'.")

# print final average
print(f"\nFinal average: {average_score:.1f}")
