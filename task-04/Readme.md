# Gopal and his PagePal

1. Creatin a telegram bot.
2. First part is easy i just have to go to BotFather and use the create new bot to create a new one and then copy
the bots token into my file. TOKEN= '7498966429:AAG3n3fDaHo6Q0OhhEWmFOoQ7cryCNJR9SY'

For a description of the Bot API, see this page: https://core.telegram.org/bots/api'
3. I have set the user name and description using the BotFather itself. @username = @'goptaskbot'
4. Now im setting up a virtual envioment because what i understood from a video is that the file that im trying to 
create is not in its usual enviornment( the folder does not know what a telegram is and all...) for that im using
python -m venv .venv  (my envionrment name is .venv)
5. Now it will still show the pip not found message so i had to close and open new terminal.
6. To use google api i went to google cloud platform and seearchedbooks api and then enabled it 
7. It showed to add credentials to access the api.
8. Account details for projext - email- telebot@gopal-pagepal.iam.gserviceaccount.com
			      - service account name = Telebot
			      - API KEY = AIzaSyCfeaj2C1PQ7FuQklK3ZVIvWCqbbVVkcxY
9. Now i used a url to store the url and a parameters a dictionary which stores the api key and the qeury at first.
10. I had a problem while handling the buttons because i was not using a callback query_handler