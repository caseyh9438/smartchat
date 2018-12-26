conda install Twisted
pip install rasa_nlu
pip install rasa_core


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


##Most Recent Version of Rasa_core
git clone https://github.com/RasaHQ/rasa_core.git
cd rasa_core
pip install -r requirements.txt
pip install -e .

##Most Recent Version of Rasa_nlu
git clone https://github.com/RasaHQ/rasa_nlu.git
cd rasa_nlu
pip install -r requirements.txt
pip install -e .

##To install Anaconda on Digital Ocean
curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh
source ~/.bashrc


##Create Conda Environment/Activate
conda create --name my_env python=3
source activate NAME
conda install PACKAGE NAME


##Obtain HTTPS
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
#add website next to server_name (replace the '_')
sudo nano /etc/nginx/sites-available/default
sudo systemctl reload nginx
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'

 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/hdlabs.tech/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/hdlabs.tech/privkey.pem
   Your cert will expire on 2019-03-21. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"