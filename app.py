from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  #frontend se interaction

#Motivational Quotes
quotes = [
"Believe in yourself and all that you are",  
"Dream big. Start small. Act now",  
"Do what you can with what you have where you are",  
"Success is not final failure is not fatal",  
"Your only limit is your mind",  
"Make today so awesome that yesterday gets jealous",  
"Every moment is a fresh beginning",  
"Don’t wish for it work for it",  
"A little progress each day adds up to big results",  
"Nothing will work unless you do",  
"You miss 100% of the shots you don’t take",  
"Stay hungry stay foolish",  
"Opportunities don’t happen you create them",  
"Small steps lead to big achievements",  
"Doubt kills more dreams than failure ever will",  
"Failure is the opportunity to begin again more intelligently",  
"Push yourself because no one else is going to do it for you",  
"Don’t stop until you’re proud",  
"The secret of getting ahead is getting started",  
"Great things never come from comfort zones",  
"Fall seven times stand up eight",  
"Don’t be afraid to give up the good to go for the great",  
"Act as if what you do makes a difference It does",  
"You are stronger than you think",  
"Everything you can imagine is real",  
"Happiness depends upon ourselves",  
"It does not matter how slowly you go as long as you do not stop",  
"The best time to plant a tree was 20 years ago The second best time is now",  
"You can either experience the pain of discipline or the pain of regret",  
"If opportunity doesn’t knock build a door",  
"Success is getting what you want Happiness is wanting what you get",  
"Your time is limited so don’t waste it living someone else’s life",  
"It always seems impossible until it’s done",  
"Difficulties in life are intended to make us better not bitter",  
"Life is 10% what happens to you and 90% how you react to it",  
"The harder the struggle the greater the triumph",  
"Winners never quit and quitters never win",  
"Be a voice not an echo",  
"Hustle in silence and let your success make the noise",  
"Be yourself everyone else is already taken",  
"Act without expectation",  
"Courage is resistance to fear mastery of fear—not absence of fear",  
"A year from now you will wish you had started today",  
"You don’t have to be great to start but you have to start to be great",  
"A smooth sea never made a skilled sailor",  
"Hard work beats talent when talent doesn’t work hard",  
"Do it now Sometimes 'later' becomes 'never'",  
"You are what you do not what you say you’ll do",  
"Dare to be different The world is full of ordinary",  
"Life begins at the end of your comfort zone"  
]
# Get a random quote
@app.route("/quote", methods=["GET"])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
