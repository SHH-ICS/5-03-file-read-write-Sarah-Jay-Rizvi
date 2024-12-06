q = "Where were french fries originally made?"
options = "A) Belgium B) France C) America D) Italy"
print(q, "\n" + options)
answer = input("Enter your answer (A/B/C/D): ").strip().upper()
print("Correct!" if answer == "A" else "Incorrect. The correct answer is A) Belgium.")
