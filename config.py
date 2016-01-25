#config.py


class BaseConfig(object):

	with open('credentials.txt', 'r') as cred:
		CLIENT_ID = '559ea4e2334b4cdb9a1808febd6d2166'
		CLIENT_SECRET = 'd5ecaaa1d3f941c4baa4ae5613ca5195'
		REDIRECT_URI = 'http://localhost:5000/home'

	if not CLIENT_ID or not CLIENT_SECRET or not REDIRECT_URI:
		raise Exception('Credentials could not be configured. ',
            'See credentials.txt.')

'''
class BaseConfig(object):

    with open('credentials.txt', 'r') as cred:
        CLIENT_ID = str(cred.readline().split('>')[1].replace('\n', ''))
        CLIENT_SECRET = str(cred.readline().split('>')[1].replace('\n', ''))
        REDIRECT_URI = str(cred.readline().split('>')[1].replace('\n', ''))

    if not CLIENT_ID or not CLIENT_SECRET or not REDIRECT_URI:
        raise Exception('Credentials could not be configured. ',
            'See credentials.txt.')
'''