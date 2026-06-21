print("================================")
print("      LAWYER BABA CHATBOT")
print("================================")
print("Type 'help' to see commands or 'bye' to exit.")

while True:
    question = input("\nAsk something: ").lower()

    if "help" in question:
        print("Available Questions: name, age, city, profession, education, hobby, routine, memory, goal, peace, case, hearing, judge, court, fee, contact, bye")

    elif "name" in question:
        print("Muhammad Yousaf")

    elif "age" in question:
        print("50 years old")

    elif "city" in question:
        print("Multan")

    elif "profession" in question or "lawyer" in question:
        print("Muhammad Yousaf is a professional lawyer.")

    elif "education" in question:
        print("He completed his LLB degree.")

    elif "hobby" in question:
        print("Reading newspapers and books.")

    elif "routine" in question:
        print("He starts his day early and works full day.")

    elif "memory" in question:
        print("His happiest memory is becoming a lawyer and winning an important case.")

    elif "goal" in question:
        print("His future goal is to become a Judge.")

    elif "peace" in question:
        print("Creating peace is the most important thing in life.")

    elif "case" in question:
        print("Case No: 123/2026")

    elif "hearing" in question:
        print("Next Hearing Date: 25 June 2026")

    elif "judge" in question:
        print("Judge: Ahmed Khan")

    elif "court" in question:
        print("Court Room No. 3, District Court")

    elif "fee" in question:
        print("Consultation Fee: Rs. 5000")

    elif "contact" in question:
        print("Contact Number: 0300-1234567")

    elif "bye" in question:
        print("Goodbye! Have a nice day.")
        break

    else:
        print("Sorry, I don't have information about that.")
