# Spotify Playlist Backup

Super simple python program to update a duplicate of a Spotify playlist. Mostly for me to practice documenting projects on github. :)

### Use case:

Collaborative playlists cannot be added to your profile, so to share one of these playlists you must create a copy. However this copy will not be updated with new additions in the source playlist. This program can be deployed to Heroku or similar to update the playlist every hour or day etc.

### How to run the python code:

Clone or download this repository and fill in the information at the top of the **main.py** script:

```python
src = '' # The source playlist
dst = '' # The destination playlist

username = '' # Your Spotify username
client_id = '' # Your Spotify app client id
client_secret = '' # And secret
redirect_uri = 'http://localhost:8000/' # The redirect url set on your Spotify app, must be identical!

removeFromDst = True; # Should songs ever be removed from the dst playlist if they are removed from the source. If true songs will be removed - mirror
```

The client id and secret can be created on [Spotify's developer dashboard.](https://developer.spotify.com/dashboard/)

Then run the program with python3.

### How to deploy to Heroku and schedule executions for free:

- [Sign up](https://signup.heroku.com/login) for a Heroku account and create a new app.
- Follow the **Deploy using Heroku Git** instructions on the Heroku dashboard inside the folder for this repository. You will need the **requirements.txt** file for Heroku to recognise this build as python.
- Once you have deployed your app, go back to the Heroku dashboard and select configure add-ons under the overview section.
- Enter **Heroku Scheduler** in the search field and submit the order form.
- Next click on the Heroku scheduler link and create a job.
- Select your prefered time interval and enter `python main.py` as the command. This command can also be used from the Heroku console or command line to test your app
