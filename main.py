from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from flask import Flask, jsonify

# Flask backend setup
flask_app = Flask(__name__)

@flask_app.route('/api/welcome')
def welcome():
    return jsonify({"message": "Welcome to GoldTask App!"})

@flask_app.route('/api/ads')
def ads():
    # Example for fetching ads info (like AdMob or other platforms)
    return jsonify({
        "ads": [
            {"platform": "AdMob", "link": "your_admob_link_here"},
            {"platform": "Unity", "link": "your_unity_ads_link_here"},
            {"platform": "Facebook", "link": "your_facebook_ads_link_here"}
        ]
    })

# Kivy frontend setup
class GoldTaskApp(App):
    def build(self):
        # Layout to hold buttons and labels
        layout = BoxLayout(orientation='vertical')

        # Title
        title = Label(text="Welcome GoldTask 🪙", font_size=32, color=(1, 1, 0, 1))
        layout.add_widget(title)

        # Login Button
        login_button = Button(text="Login", on_press=self.login)
        layout.add_widget(login_button)

        # SignUp Button
        signup_button = Button(text="SignUp", on_press=self.signup)
        layout.add_widget(signup_button)

        # Task Section
        task_button = Button(text="Watch Ads", on_press=self.watch_ads)
        layout.add_widget(task_button)

        return layout

    def login(self, instance):
        print("Login button pressed")
        # Handle login logic here, show a popup or transition to login screen

    def signup(self, instance):
        print("SignUp button pressed")
        # Handle signup logic here

    def watch_ads(self, instance):
        print("Watch Ads button pressed")
        # Show ads or redirect to a page with ads

if __name__ == "__main__":
    from threading import Thread

    # Running Flask app in a separate thread
    def run_flask():
        flask_app.run(debug=True, use_reloader=False)

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Running Kivy app
    GoldTaskApp().run()
