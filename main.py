from moodf import mood_response

def main():
    user_mood = input("How are you feeling today? ")
    response = mood_response(user_mood)
    print("Response:", response)

if __name__ == "__main__":
    main()