from cryptography.hazmat.primitives.asymmetric import ed25519
from urllib.parse import urlparse, urlencode
import urllib
import json
import requests
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ApiTradingClient:

  secret_key = None,
  api_key = None

  def __init__(self, secret_key:str, api_key:str):
        self.secret_key = secret_key
        self.api_key = api_key
        self.base_url = "https://coinswitch.co"
        self.headers = {
            "Content-Type": "application/json"
        }


  def call_api(self, url: str, method: str, headers: dict = None, payload:dict = {}):
    '''
    make an API call on webserver and return response

    Args:
      url (str): The API url to be called
      method (str): The API method
      headers (dict): required headers for API call
      payload (dict): payload for API call

    Returns:
      json: The response of the request
    '''
    final_headers = self.headers.copy()
    if headers is not None:
      final_headers.update(headers)
    
    response = requests.request(method, url, headers=headers, json=payload)
    return response.json()


  def signatureMessage(self, method: str , url: str, payload: dict):
    '''
      Generate signature message to be signed for given request

      Args:
        url (str): The API url to be called
        method (str): The API method
        payload (dict): payload for API call

      Returns:
        json: The signature message for corresponding API call
    '''
    message = method + url + json.dumps(payload, separators=(',', ':'), sort_keys=True)
    return message


  def get_signature_of_request(self, secret_key: str, request_string: str) -> str:
    '''
      Returns the signature of the request
      
      Args:
        secret_key (str): The secret key used to sign the request.
        request_string (str): The string representation of the request.

      Returns:
        str: The signature of the request.
    '''
    request_string = bytes(request_string, 'utf-8')
    secret_key_bytes = bytes.fromhex(secret_key)
    secret_key = ed25519.Ed25519PrivateKey.from_private_bytes(secret_key_bytes)
    signature_bytes = secret_key.sign(request_string)
    signature = signature_bytes.hex()
    return signature


  def make_request(self, method:str, endpoint:str, payload:dict = {}, params:dict = {}):
    '''
    Make the request to :
      a. generate signature message
      b. generate signature signed by secret key
      c. send an API call with the encoded URL

    Args:
        method (str): The method to call API
        endpoint (str): The request endpoint to make API call
        payload (dict): The payload to make API call for POST request
        params (dict): The params to make GET request

      Returns:
        dict: The response of the request.

    '''
    decoded_endpoint = endpoint
    if method == "GET" and len(params)!=0:
      endpoint += ('&', '?')[urlparse(endpoint).query == ''] + urlencode(params)
      decoded_endpoint = urllib.parse.unquote_plus(endpoint)

    signature_msg = self.signatureMessage(method, decoded_endpoint, payload)

    signature = self.get_signature_of_request(self.secret_key, signature_msg)

    headers = {
        "X-AUTH-SIGNATURE" : signature,
        "X-AUTH-APIKEY": self.api_key
    }

    url = f"{self.base_url}{endpoint}"

    response = self.call_api(url, method, headers = headers, payload = payload)
    return json.dumps(response, indent=4)


  def check_connection(self):
    return self.make_request("GET", "/api-trading-service/api/v1/ping")

  def validate_keys(self):
    return self.make_request("GET", "/api-trading-service/api/v1/validate/keys")

  def create_order(self,payload:dict = {}):
    return self.make_request("POST", "/api-trading-service/api/v1/order/create", payload = payload)

  def cancel_order(self, payload:dict = {}):
    return self.make_request("PUT", "/api-trading-service/api/v1/order/cancel", payload = payload)

  def get_open_orders(self, params:dict = {}):
    return self.make_request("GET", "/api-trading-service/api/v1/orders/get/open", params = params)

  def get_closed_orders(self, params:dict = {}):
    return self.make_request("GET", "/api-trading-service/api/v1/orders/get/closed", params = params)

  def get_user_portfolio(self):
    return self.make_request("GET", "/api-trading-service/api/v1/user/portfolio")

  def get_24h_all_pairs_data(self, params:dict = {}):
    return self.make_request("GET", "/api-trading-service/api/v1/ticker/24hr/all-pairs", params = params)

  def get_24h_coin_pair_data(self, params:dict = {}):
    return self.make_request("GET", "/api-trading-service/api/v1/ticker/24hr", params = params)

  def get_depth(self, params:dict = {}):
    return self.make_request("GET", "/api-trading-service/api/v1/depth", params = params)

  def get_trades(self, params:dict = {}):
    return self.make_request("GET", "/api-trading-service/api/v1/trades", params = params)

  def get_candelstick_data(self, params:dict = {}):
    return self.make_request("GET", "/api-trading-service/api/v1/getDataForCandlestick", params = params)
  
  def get_exchange_precision(self, payload:dict = {}):
    return self.make_request("POST", "/api-trading-service/api/v1/exchange-precision", payload = payload)


secret_key = "3dd4327c45784f3d8ba0ce7c55ebafd53e23e5cfeba501e531d6f39f00902e54"
api_key = "345173bd8edc2fc60e45e6c7cd9a9e022747e98cc4a80a22dcc4e614ad24deee"
api_trading_client = ApiTradingClient(secret_key, api_key)

y=api_trading_client.get_user_portfolio()
json_data = json.loads(y)
data = json.loads(y); name = "Indian Rupee"; iv = next((item["invested_value"] for item in data["data"] if item["name"] == name), None); print(f"Main balance for {name}: {iv}")
a= iv
if iv>1200:
	subject = "ALERT"
	body = "Alert.  Note that your coinswitch's portfolio amount is too high.  The order could not be executed due to a problem with the program. The current portfolio amount is given below.Ignore this email if you are trading manually or settling unsold crypto currencies or you are aware about it:\n{}".format(a)
	message = f"Subject: {subject}\n\n{body}"
	smtp_server = "smtp.gmail.com"
	port = 587
	username = "keerak0009@gmail.com"
	password = "oywqosuhvhqxtlvy"
	with smtplib.SMTP(smtp_server, port) as smtp:
		            			smtp.starttls()
		            			smtp.login(username, password)
		            			smtp.sendmail('keerak0009@gmail.com', 'arpitkeer30@gmail.com', message)
	            
else:
	print("nothing to worrry about")

url = "http://mysite09.pagekite.me/"

def send_email(subject, message):
    # Email configuration
    sender_email = "keerak0009@gmail.com"
    sender_password = "oywqosuhvhqxtlvy"
    receiver_email = "arpitkeer9@gmail.com"

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Website is up and running (Status 200 OK)")
    else:
        error_message = f"Website is down! Status code: {response.status_code}"
        print(error_message)
        send_email("Website Down", error_message)
except requests.exceptions.RequestException as e:
    error_message = f"Error while trying to access the website: {str(e)}"
    print(error_message)
    send_email("Website Error", error_message)
except Exception as e:
    error_message = f"An unexpected error occurred: {str(e)}"
    print(error_message)
    send_email("Website Error", error_message)


