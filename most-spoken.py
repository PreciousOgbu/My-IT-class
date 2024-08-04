import langdetect

def most_spoken_languages():
    language_names = {
        'en': 'English', 'es': 'Spanish', 'fr': 'French', 'zh-cn': 'Mandarin', 'hi': 'Hindi',
        'ar': 'Arabic', 'bn': 'Bengali', 'pt': 'Portuguese', 'ru': 'Russian', 'ja': 'Japanese',
        'pa': 'Punjabi', 'de': 'German', 'jv': 'Javanese', 'wu': 'Wu', 'te': 'Telugu',
        'vi': 'Vietnamese', 'mr': 'Marathi', 'ko': 'Korean', 'ta': 'Tamil'
    }
    entered_languages = []
    while True:
        user_input = input("Enter some text (or 'exit' to print and quit): ")
        if user_input.lower() == 'exit':
            print("Here are the languages you entered in descending order:")
            for i, language in enumerate(sorted(entered_languages, key=lambda x: entered_languages.count(x), reverse=True), start=1):
                print(f"{i}. {language_names.get(language, 'Unknown')}")
            break
        try:
            language = langdetect.detect(user_input)
            entered_languages.append(language)
            if language in language_names:
                print(f"The language you entered is {language_names[language]}, which is one of the most spoken languages!")
            else:
                print("Sorry, this language is not one of the most spoken in the world. Try again.")
        except langdetect.lang_detect_exception.LangDetectException:
            print("Sorry, unable to detect language. Try again.")

most_spoken_languages()

