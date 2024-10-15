import json
from textblob import TextBlob

class MediatorModel:
    def __init__(self):
        self.user_profiles = self.load_user_profiles()

    def load_user_profiles(self):
        try:
            with open('data/user_profiles.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"users": []}

    def save_user_profiles(self):
        with open('data/user_profiles.json', 'w') as f:
            json.dump(self.user_profiles, f)

    def add_user_profile(self, username):
        if not any(user['username'] == username for user in self.user_profiles['users']):
            self.user_profiles['users'].append({"username": username, "history": []})
            self.save_user_profiles()

    def log_mediation(self, username, argument1, argument2, solution):
        user = next((user for user in self.user_profiles['users'] if user['username'] == username), None)
        if user:
            user['history'].append({"argument1": argument1, "argument2": argument2, "solution": solution})
            self.save_user_profiles()

    def get_user_profile(self, username):
        return next((user for user in self.user_profiles['users'] if user['username'] == username), None)

    def analyze_argument(self, argument):
        analysis = TextBlob(argument)
        return analysis.sentiment.polarity

    def suggest_solution(self, argument1, argument2):
        score1 = self.analyze_argument(argument1)
        score2 = self.analyze_argument(argument2)

        if score1 > score2:
            return "Consider validating the points made in argument 2."
        elif score2 > score1:
            return "Consider addressing the concerns raised in argument 1."
        else:
            return "Both arguments have similar sentiments. Consider finding common ground."

