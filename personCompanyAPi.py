#Access the company API

import clearbit
import json

def Authenticate():
	"This method Authenticate's using the secret key"
	clearbit.key = 'ee9bf34f0b29e34ff6b28a42213c4050'

def GetPersonAndCompanyInfo(emailID):
	"Get the person and company based email id and domain on email id"
	response = clearbit.PersonCompany.find(email=emailID)

	if 'pending' in response:
	  # Lookup queued - try again later
	  print 'Lookup queued'

	if 'person' in response:
	  print response['person']['name']['fullName']

	if 'company' in response:
	  print response['company']['name']

  	print json.dumps(response, indent=4, sort_keys=True)


def main():
	Authenticate()
 	GetPersonAndCompanyInfo('pg@ycombinator.com')


if __name__ == '__main__':
	main()

