# Clearbit-API-POC
Experimenting with Clearbit API

Before attempting to run either companyApi.Py or personCompany.py, please install the following

##1. Install pip / Easy_install
##2. Install clearbit package.
    Use PyPI
    pip install clearbit
    
    Or use easy_install
    easy_install clearbit
    
    

Once installed, executing <b>companyApi.py</b> will give info about <b>amazon.com</b>,We have harded coded this to
prevent multiple request being made to clearbit.The free usage limits the number of requests to 50/month. This uses
<a href="https://clearbit.com/docs?python#domain-lookup">domain lookup API</a> exposed by clearbit.

Executing <b>personCompany.py</b> will give info about the person and the company present in the domain of the email. In this
case we have harded coded it to <b>pg@ycombinator.com</b>. This uses the <a href="https://clearbit.com/docs?python#combined-lookup">combined lookup API</a> exposed by Clearbit.

<a href="https://clearbit.com/docs?python#api-reference">Clearbit API reference</a>

