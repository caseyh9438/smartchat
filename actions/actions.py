from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
from requests import request
import json


class GetEmailForm(FormAction):

   def name(self):
       # type: () -> Text
       """Unique identifier of the form"""

       return "get_email_form"

   @staticmethod
   def required_slots(tracker):
       # type: () -> List[Text]
       """A list of required slots that the form has to fill"""

       return ["email"]

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
       """Define what the form has to do
           after all required slots are filled"""
       first_name = tracker.get_slot("first_name")
       dispatcher.utter_message("It's nice to meet you {}. I'm here to analyze any problem you might be dealing with regarding Huntington's disease and recommend a path forward. Just broadly describe the problem you're facing.".format(first_name))
       return [SlotSet("first_name", first_name)]


class PassControl(Action):

    def name(self):
        return 'pass_control_action'

    def run(self, dispatcher, tracker, domain):
        #r = requests.get('http://127.0.0.1:4040')
        #incoming_message = r.json()
        app_id = 263902037430900
        page_access_token = "EAADFWBftMjABAIuAAiqgYt9eGcMLdhspZB1SFpP08aZAwS5tI03WHR6DZAqz5tfHBIzZCXiRbSCp84pP1Dk8omEPVZCNVI2xqbHjAe4xsYon60Fb6WKnf1sTWAZCm2lE2zmqZBMObvZAyZBjiAksN76VAMBVuOd8qCONneOZAPWU3vfAZDZD"
        ps_id = 2230539113625885
        pass_url = "https://graph.facebook.com/v2.6/me/pass_thread_control?access_token={}".format(page_access_token)
        data = json.dumps({"recipient": {"id": ps_id}, "target_app_id": app_id, "metadata": "Conversation elevated"})

        requests.post(pass_url, headers={"Content-Type": "application/json"}, data=data)

        response = """I am connecting you with someone on the team now."""
        dispatcher.utter_message(response)
        return []
