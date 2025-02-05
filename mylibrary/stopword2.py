class StopwordManager:
    def __init__(self):
        self.languages = {
            "arabic": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\arabic.txt",
            "bulgarian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\bulgarian.txt",
            "catalan": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\catalan.txt",
            "czech": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\czech.txt",
            "danish": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\danish.txt",
            "dutch": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\dutch.txt",
            "english": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\english.txt",
            "finnish": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\finnish.txt",
            "french": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\french.txt",
            "german": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\german.txt",
            "gujarati": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\gujarati.txt",
            "hebrew": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\hebrew.txt",
            "hindi": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\hindi.txt",
            "hungarian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\hungarian.txt",
            "indonesian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\indonesian.txt",
            "italian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\italian.txt",
            "malaysian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\malaysian.txt",
            "norwegian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\norwegian.txt",
            "polish": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\polish.txt",
            "portuguese": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\portuguese.txt",
            "romanian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\romanian.txt",
            "russian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\russian.txt",
            "slovak": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\slovak.txt",
            "spanish": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\spanish.txt",
            "swedish": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\swedish.txt",
            "turkish": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\turkish.txt",
            "ukrainian": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\ukrainian.txt",
            "vietnamese": r"C:\Users\Abed Alkareem\Desktop\stopword_28 language\vietnamese.txt"
        }

    def get_stopword_file(self, language):
        return self.languages.get(language.lower(), None)

    def load_stopwords(self, language):
        file_path = self.get_stopword_file(language)
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    return set(f.read().splitlines())
            except FileNotFoundError:
                print(f"Error: Stopwords file for '{language}' not found.")
                return set()
        else:
            print(f"Error: Language '{language}' is not supported.")
            return set()
