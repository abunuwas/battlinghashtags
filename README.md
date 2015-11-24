# battlinghashtags
Basic elements for a website in which you can select two hashtags 
and make them fight!

## Directives

### Obtain Twitter OAuth credentials (API key, API secret, Access token and Access token secret)

1. Create a twitter account if you do not already have one.
2. Go to https://apps.twitter.com/ and log in with your twitter credentials.
3. Click "Create New App"
4. Fill out the form, agree on the terms, and click "Create your Twitter application".
5. In the next page, click on the "API keys" tab, and copy your "API key" and "API secret".
6. Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret". 
7. Copy these keys in lines 18-21 of the battles/twitter_streaming.py file. 

### How to run the application

1. The application has only been tested for Django 1.8 and Python 3. 
2. Clone the whole repository locally.
3. Open the command line and cd to the repository. 
4. type `python manage.py runserver` to start the server. 
The command will tell you which port will be listening to
the application. You can also personalize this feature with
the following command: `python manage.py runserver <PORT_NUMBER>`,
where `<PORT_NUMBER>` is the port in which you want to listen to the
application (e.g. `8080`).
5. To access the index page of the project, go to 
`<PORT_NUMBER>/battles`. Here you can create the first
battle between two hashtags. 
6. The application uses the StreamListener class provided by tweepy 
to retrieve tweets with the specified tags. A temporizer for how long
we want to connect with the Twitter stream can set in the code, in the
battle_span attribute of the newBattle class, in line 46 of the 
battles/views.py file. The argument passed to this attributed is
interpreted as seconds. At a later stage, a date picker will be added
to make this functionality more convenient for the user. 
7. The application doesn't check whether a specific chosen tag 
actually exists in Twitter or not. In case it doesn't, the listener
will never close. In fact, the listener will not close until it 
gets passed a tweet at a point later than that set in the temporizer. 
If it takes too long for the listener to close, it's better to change
the url: this will interrupt the process. 
8. As it stands now, the application only compares the amount of tweets
tagged with each hashtag during the specified time set in the temporizer. 
At a later stage, more complex functionality to compare hashtags in more 
meaningful ways will be added. 
9. The application uses SQLite for the database backend in order
to make things simple and avoid problems with config files. SQLite
is not bad for prototyping, but for a real application it would be
preferable to use something more robust, such as PostgreSQL. 
10. The application doesn't have yet any tests. 
