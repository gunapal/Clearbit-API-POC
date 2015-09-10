#Access the company API

import clearbit
import json

def Authenticate():
	"This method Authenticate's using the secret key"
	clearbit.key = 'ee9bf34f0b29e34ff6b28a42213c4050'

def GetCompanyInfoBasedOnDomain(domainUrl):
	"Get the company information based on domain"
	company = clearbit.Company.find(domain=domainUrl)
	if company != None and 'pending' not in company:
  		print json.dumps(company, indent=4, sort_keys=True)


def main():
	Authenticate()
 	GetCompanyInfoBasedOnDomain('Amazon.com')


if __name__ == '__main__':
	main()

