from library.app import app
from config import BaseConfig

from flask import render_template, request, redirect, url_for
from flask import session
import spotipy
import spotipy.util as util
import os
import requests

def oauth_prep(config=BaseConfig, scope='user-library-read'):
    ''' Connect to Spotify using spotipy & our app config credentials'. '''

    oauth = spotipy.oauth2.SpotifyOAuth(client_id=config.CLIENT_ID,
                                client_secret=config.CLIENT_SECRET,
                                redirect_uri=config.REDIRECT_URI,
                                scope=scope)
    return oauth


#@app.route('/login', methods=['POST', 'GET'])
def login(config=BaseConfig, scope='user-library-read'):
    '''
    prompts user to login via OAuth2 through Spotify
    this shows up in index.html

    if current_user.is_authenticated():
        return redirect(url_for('choose_parameters'))

    '''
    # utility of spotify.oauth2.SpotifyOauth
    # lets us store everythin in 1 container, as well as give us the auth URL



    oauth = oauth_prep(config, scope)
    payload = {'client_id': oauth.client_id,
            'response_type': 'code', 'redirect_uri': oauth.redirect_uri,
            'scope': oauth.scope}
    r = requests.get(oauth.OAUTH_AUTHORIZE_URL, params=payload)
    return (r.url)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home(config=BaseConfig, scope='user-library-read'):
    if request.method == 'GET':
        if not 'code' in request.args:
            oauth = login(config=BaseConfig, scope=scope)
            return render_template('home.html', login=False, oauth=oauth)
        else:
            oauth = oauth_prep(config)
            response = oauth.get_access_token(request.args['code'])
            token = response['access_token']

            s = spotipy.Spotify(auth=token)
            offset = 0
            albums = s.current_user_saved_tracks(limit=50, offset=offset)
            return render_template('home.html', albums=albums['items'],
                                    login=True)

