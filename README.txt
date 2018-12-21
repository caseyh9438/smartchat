##Rasa Commands:
## Train NLU
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

## Train Core
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue

## Connect Rasa Core & Rasa NLU locally
python -m rasa_core.run -d models/dialogue -u models/current/nlu


## Passing message to stand alone chatbot
curl -XPOST --header 'content-type: application/json' --data '{"message": "Hey"}' http://localhost:5005/webhooks/rest/webhook


## Passing Facebook Credentials to handle msgs
python -m rasa_core.run -d models/dialogue -u models/nlu/current \
   --port 5002--credentials credentials/credentials.yml

## In order to test Facebook locally run ngrok
Download and unzip ngrok, setup and run


## To Run Rasa action server locally
python -m rasa_core_sdk.endpoi-actions actions.actions --port 5055


## Run Docker Yaml
docker-compose up

##Facebook Webhook
https://__________/webhooks/facebook/webhook

