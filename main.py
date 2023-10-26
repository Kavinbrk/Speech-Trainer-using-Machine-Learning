#importing needed resources
import speech_recognition as sr
import pyttsx3
import datetime
from difflib import SequenceMatcher

#intializing engines for tts

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 150)

#to recognize user input

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

#to make the text to speak

def speak(text):
    engine.say(text)
    engine.runAndWait()

#communicator mode acts as  conversational kind

def communicator():
    print("Bot: Hey there! What's up?")
    speak("Hey there! What's up?")

    while True:
        user_input = takeCommand().lower()

        if not user_input:
            continue

        if "how are you" in user_input:
            print("Bot: yeah mate im doing great, hope you are doing great too")
            speak("yeah mate im doing great, hope you are doing great too")
        elif "yeah" in user_input or "that's good" in user_input:
            speak("Great to hear that")
        elif "tell me a joke" in user_input:
            print("Bot: Why did the scarecrow win an award? Because he was outstanding in his field!")
            speak("Why did the scarecrow win an award? Because he was outstanding in his field!")
        elif "what's the weather like today" in user_input:
            print("Bot: its like a little lite outside may its seems good when it see you")
            speak("its like a little lite outside may its seems good when it see you")
        elif "speak" in user_input or "different" in user_input or "unique" in user_input:
            speak("Always because I'm designed by the one who was like that")
            print("Always because I'm designed by the one who was like that")
        elif "poda" in user_input or "vaada" in user_input or "macha" in user_input:
            speak("Enakku tamil teriyum    terithu nu nenachutu irukiyyaa")
        elif "tell me a fun fact" in user_input:
            print("Bot: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
            speak("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
        elif "who is your creator" in user_input:
            print("Bot: I was created by a talented programmer named [Your Name].")
            speak("I was created by a talented programmer named [Your Name].")
        elif "exit" in user_input:
            print("Bot: It was nice chatting with you! Have a great day!")
            speak("It was nice chatting with you! Have a great day!")
            break
        elif "interview" in user_input:
            speak("Sure, let's prepare for an interview.")
            simulate_interview()
        elif "trainer" or "voice trainer" in user_input:
            speak("Yep, Now you can go with Voice Trainer")
            wishMe()
            voice_trainer()
        else:
            print("Bot: Sorry, I didn't get that. What else would you like to talk about?")
            speak("Sorry, I didn't get that. What else would you like to talk about?")

# a command to get prepared for an interview
def simulate_interview():
    questions = [
        "Tell me about yourself.",
        "What are your strengths?",
        "What are your weaknesses?",
        "Why do you want to work for this company?",
        "Why should we hire you?",
        "Tell me about a time you faced a challenge at work and how you handled it.",
        "Where do you see yourself in 5 years?",
        "Do you have any questions for us?"
    ]

    answers = [
        "I am a dedicated and hardworking individual with a passion for this field. I have this experience in this skill.",
        "One of my strengths is a skill regarding this job, which I have developed through my previous experiences.",
        "I believe one of my areas for improvement is mention a weakness but I am actively working on improving it.",
        "I am impressed by company's name commitment to innovation and mention something specific about the company. I want to be part of that.",
        "You should hire me because I bring a unique combination of skills and experiences that make me a great fit for this role.",
        "In my previous job, we had a tight deadline for a project and I organized the team effectively, resulting in the successful completion of the project ahead of schedule.",
        "I see myself in a leadership role, taking on more responsibilities and contributing to the growth of the company.",
        "Yes, I'm interested to know more about the company culture and the team dynamics. Can you tell me more about that?"
    ]

    speak("Okay, let's get prepared for the interview. Let's go with the basic interview questions.")
    speak("I will ask you a question, and then I will provide the answer. You can listen to the answer and practice your response.")
    speak("If your answer matches the suggested answer, we'll move on to the next question. If not, we'll stay on the current question for further practice.")

  #evaluating   
  for i, question in enumerate(questions):
        speak(f"Question {i + 1}: {question}")
        print(f"Question {i + 1}: {question}")
        bot_answer = answers[i]
        speak(f"Here's the answer: {bot_answer}")
        print(f"Answer {i + 1}: {bot_answer}")
        speak("Now, you can provide your answer and practice.")
        user_answer = takeCommand().lower()

        while user_answer != bot_answer.lower():
            speak("Your answer doesn't match the suggested answer. Please practice more on this question.")
            speak("Let's stay on this question for further practice.")
            speak("Please provide your answer.")
            user_answer = takeCommand().lower()

        speak("Great! Your answer matches the suggested answer. Let's move on to the next question.")

    speak("That concludes our interview simulation. Remember to practice and refine your answers to these common interview questions.")


def evaluate_pronunciation(correct_pronunciation, user_pronunciation):
    # Calculate the similarity ratio between correct and user pronunciations
    similarity = SequenceMatcher(None, correct_pronunciation, user_pronunciation).ratio()
    return similarity


# voice trainer to train user's voice level by level
def voice_trainer():



    levels = {
      # first level composed of basic words
        1: {
            "Hello": "Hello",
            "Good": "Good",
            "Morning": "Morning",
            "Please": "Please",
            "Thank you": "Thank you",
            "Yes": "Yes",
            "No": "No",
            "Excuse me": "Excuse me",
            "Sorry": "Sorry",
            "How are you?": "How are you?",
            "My name is": "My name is",
            "What's your name?": "What's your name?",
            "I'm fine": "I'm fine",
            "How's the weather?": "How's the weather?",
            "Nice to meet you": "Nice to meet you",
            "Goodbye": "Goodbye",
            "Have a nice day": "Have a nice day",
            "See you later": "See you later",
            "What time is it?": "What time is it?",
            "How's it going?": "How's it going?"
        },

      # seond level on simple q/a
        2: {
            "I am learning English.": "I am learning English.",
            "The weather is nice today.": "The weather is nice today.",
            "What's your favorite color?": "What's your favorite color?",
            "I like to read books.": "I like to read books.",
            "How was your day?": "How was your day?",
            "Can you help me, please?": "Can you help me, please?",
            "Where do you live?": "Where do you live?",
            "What's your phone number?": "What's your phone number?",
            "I have a pet dog.": "I have a pet dog.",
            "What's for dinner?": "What's for dinner?",
            "I enjoy watching movies.": "I enjoy watching movies.",
            "Do you have any siblings?": "Do you have any siblings?",
            "How old are you?": "How old are you?"

        },
      #third level on some uncommon words
        3: {
            "Cacophony": "Cacophony",
            "Ephemeral": "Ephemeral",
            "Serendipity": "Serendipity",
            "Ubiquitous": "Ubiquitous",
            "Quixotic": "Quixotic",
            "Sycophant": "Sycophant",
            "Nefarious": "Nefarious",
            "Juxtaposition": "Juxtaposition",
            "Panacea": "Panacea",
            "Sanguine": "Sanguine",
            "Voracious": "Voracious",
            "Zealous": "Zealous",
            "Ebullient": "Ebullient",
            "Obfuscate": "Obfuscate",
            "Perspicacious": "Perspicacious",
            "Sycophantic behavior is not appreciated.": "Sycophantic behavior is not appreciated.",
            "The juxtaposition of colors in the painting is striking.": "The juxtaposition of colors in the painting is striking."

        },

      #fourth level on idioms
        4: {
            "Bite the bullet": "Bite the bullet",
            "Jump on the bandwagon": "Jump on the bandwagon",
            "Don't count your chickens before they hatch.": "Don't count your chickens before they hatch.",
            "Break a leg!": "Break a leg!",
            "Hit the nail on the head": "Hit the nail on the head",
            "The ball is in your court.": "The ball is in your court.",
            "It's a piece of cake.": "It's a piece of cake.",
            "Don't put all your eggs in one basket.": "Don't put all your eggs in one basket.",
            "The early bird catches the worm.": "The early bird catches the worm.",
            "The show must go on.": "The show must go on.",
            "He spilled the beans.": "He spilled the beans.",
            "She's feeling under the weather.": "She's feeling under the weather.",
            "It's raining cats and dogs.": "It's raining cats and dogs.",
            "They are on cloud nine.": "They are on cloud nine."

        },

      #fifith level with genz words
        5: {
            "Wassup": "Wassup",
            "Chillin'": "Chillin'",
            "Dope": "Dope",
            "Lit": "Lit",
            "FOMO": "FOMO",
            "YOLO": "YOLO",
            "TMI": "TMI",
            "Bae": "Bae",
            "Savage": "Savage",
            "Flex": "Flex",
            "G.O.A.T.": "G.O.A.T.",
            "Throw shade": "Throw shade",
            "Keep it 100": "Keep it 100",
            "On fleek": "On fleek",
            "Shook": "Shook",
            "Slay": "Slay"

        },

      #sixith level with some advanced words
        6: {
            "Entrepreneurship": "Entrepreneurship",
            "Phenomenon": "Phenomenon",
            "Sociopolitical": "Sociopolitical",
            "Quintessential": "Quintessential",
            "Pernicious": "Pernicious",
            "Ostentatious": "Ostentatious",
            "Superfluous": "Superfluous",
            "Indubitably": "Indubitably",
            "Cacophonous": "Cacophonous",
            "Unprecedented": "Unprecedented",
            "Paradigm shift": "Paradigm shift",
            "Esoteric": "Esoteric",
            "Euphemism": "Euphemism",
            "Ubiquity": "Ubiquity",
            "Anachronism": "Anachronism",
            "Efficacious": "Efficacious"

        },

      #seventh level with advanced q/a styled
        7: {
            "Although it was raining, I went for a run.": "Although it was raining, I went for a run.",
            "She couldn't believe her eyes when she saw the result.": "She couldn't believe her eyes when she saw the result.",
            "I'm planning to visit Europe next summer.": "I'm planning to visit Europe next summer.",
            "The concert tickets were sold out within minutes.": "The concert tickets were sold out within minutes.",
            "Innovation is the key to success in today's fast-paced world.": "Innovation is the key to success in today's fast-paced world.",
            "The economy is expected to grow at a steady pace.": "The economy is expected to grow at a steady pace.",
            "His perseverance and dedication paid off in the end.": "His perseverance and dedication paid off in the end.",
            "The film received critical acclaim for its compelling storyline.": "The film received critical acclaim for its compelling storyline.",
            "The company's profits soared to new heights this year.": "The company's profits soared to new heights this year.",
            "She's known for her remarkable achievements in the field of science.": "She's known for her remarkable achievements in the field of science."

        },
    }


    recognizer = sr.Recognizer()
    correct_similarity_threshold = 0.75  # Adjust the threshold as needed

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    current_level = 1

    while current_level <= len(levels):
        words = levels[current_level]
        for word, pronunciation in words.items():
            while True:
                with sr.Microphone() as source:
                    print(f"Speech Training Bot (Level {current_level}): Let's pronounce the word/phrase: '{word}'.")
                    engine.say(f"Let's pronounce the word/phrase: {word}.")
                    engine.runAndWait()

                    audio = recognizer.listen(source)
                    try:
                        user_input = recognizer.recognize_google(audio)
                        print(f"You said: {user_input}")
                        similarity = evaluate_pronunciation(pronunciation, user_input.lower())
                        if similarity >= correct_similarity_threshold:
                            engine.say(f"Good job! You pronounced '{word}' correctly.")
                            engine.runAndWait()
                            break
                        else:
                            engine.say(f"Try again. Your pronunciation is {similarity * 100:.2f}% similar.")
                            engine.runAndWait()
                    except sr.UnknownValueError:
                        engine.say("I couldn't understand your pronunciation.")
                        engine.runAndWait()
                    except sr.RequestError:
                        engine.say("Sorry, I'm experiencing some technical difficulties.")
                        engine.runAndWait()
                    if "mate" or "communicator" in user_input:
                        speak("Yep, Now you can go with your Mate")
                        wishMe()
                        communicator()

        if current_level == 7:
            engine.say("Congratulations! You have completed 7 levels. Great job!")
            engine.runAndWait()
        elif current_level < len(levels):
            engine.say(f"Congratulations! You have completed Level {current_level}. You are now upgraded to Level {current_level + 1}.")
            engine.runAndWait()

        current_level += 1


#to greet the user user according to time
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif 12 <= hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def main():
    wishMe()
    speak("This is Your Personal Speech Trainer Guru, I am here to assist you to improve your communication with two choices:")
    print("This is Your Personal Speech Trainer Guru, I am here to assist you to improve your communication with two choices:")
    speak("To go on with a Communicator say I need a Mate")
    print("To go on with a Communicator say I need a Mate")
    speak("or To make training for words say I need a Trainer")
    print("or To make training for words say I need a Trainer")

    while True:
        choice = takeCommand().lower()
        if choice == "communicator" or choice == "i need a communicator":
            communicator()
        elif choice == "trainer" or choice == "i need a trainer":
            voice_trainer()
        elif "goodbye" in choice or "ok bye" in choice or "stop" in choice:
            speak("Goodbye!")
            break
        else:
            speak("Invalid choice. Please select mate or trainer.")

if __name__ == "__main__":
    main()
