import requests
import json

payid = 'PAYID-MCHLSEQ6H742977CM282664J'

def getToken():
	url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
	cid = "AaBHxNYrqOmbdEo8-PFoQi4-7n9ZVLjDLAx4X6TKYq7aZiMMyGYaQ_9a0YgdtRUb_ISlBen6lcRBnKGi"
	secret = "EFkFWwB-Z7k3cutV79Yqa5ljIU7JY50-7V6mHgDKNheAoaeS6hwlHF-0fr7Vs8wBo1vE-RtWSp5DGb6l"
	header = {"Accept":"application/json", "Accept-Language":"en_US" }
	data = {"grant_type":"client_credentials"}
	req = requests.post(url, auth=(cid, secret), headers=header, data=data).json()
	access_token = req['access_token']
	return access_token

def makeRequest():
	token = getToken()
	url = "https://api-m.sandbox.paypal.com/v1/payments/payment/PAYID-MCHLSEQ6H742977CM282664J/"
	page = 1
	page_size = 100
	invoice_numer = "BVHMMZI3NIXRV4Z4111M"
	tid = "3XY77185V6431531T"
	# url = f"https://api-m.sandbox.paypal.com/v2/invoicing/search-invoices?page={page}&page_size={page_size}&total_required=true"
	header = {"Content-Type":"application/json", "Authorization": f"Bearer {token}"}
	# url = f"https://api-m.sandbox.paypal.com/v2/invoicing/invoices?total_required=true"
	req = requests.get(url, headers=header).json()
	print(json.dumps(req, indent=4))

makeRequest()
