from textblob import TextBlob

def analyze_tone(email_content):
    blob = TextBlob(email_content)
    
    sentiment_polarity = blob.sentiment.polarity
    
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def display_tone_analysis(email_content):
    print("\nAnalyzing the tone of your email...\n")
    tone = analyze_tone(email_content)
    print(f"The tone of the email is: {tone}")
    
def main():
    print("Welcome to the Email Tone Checker!\n")
    
    email_content = input("Please enter the content of your email:\n")
    
    display_tone_analysis(email_content)
    
    tone = analyze_tone(email_content)
    if tone == "Negative":
        print("\nIt seems like the email has a negative tone. You might want to revise it to sound more positive or neutral.")
    elif tone == "Neutral":
        print("\nThe email has a neutral tone, which is appropriate for professional communication.")
    else:
        print("\nThe email has a positive tone. Great job in maintaining a polite and friendly tone!")

if __name__ == "__main__":
    main()
