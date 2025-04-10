jacks_done = 0

while jacks_done < 100:
    print("\nDo 10 jumping jacks!")
    jacks_done += 10

    if jacks_done == 100:
        print("\nCongratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the rest? (yes/y or no/n): ").lower()
        if skip in ["yes", "y"]:
            print(f"\nYou completed a total of {jacks_done} jumping jacks.")
            break

    print(f"{100 - jacks_done} jumping jacks left. Keep going!")
