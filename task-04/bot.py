import requests
from typing import Final
from telegram import Update ,InlineKeyboardButton ,InlineKeyboardMarkup
from telegram.ext import Updater , filters , CommandHandler ,MessageHandler , ContextTypes , Application , CallbackQueryHandler

TOKEN: Final = '7498966429:AAG3n3fDaHo6Q0OhhEWmFOoQ7cryCNJR9SY'

username: Final = '@goptaskbot'
url = "https://www.googleapis.com/books/v1/volumes"



async def start(update : Update , context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text('Konnichiwa , {} '.format(name))
    print(f'Start command called by {name}')
    

async def help(update : Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/start , /book , /preview, /list, /reading_list are the commands that I follow')


async def book(update : Update , context: ContextTypes.DEFAULT_TYPE):
    user_q1 = ' '.join(context.args)

    if not user_q1:
        await update.message.reply_text('Please enter the name of the book you would like to preview')
        return
    params = {
    "q" : user_q1,
    "key": "AIzaSyCfeaj2C1PQ7FuQklK3ZVIvWCqbbVVkcxY"
    }
    response = requests.get(url,params=params)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            for item in data['items']:
                book = item['volumeInfo']
                title = book.get('title', 'No title available')
                authors = ', '.join(book.get('authors', ['Unknown author']))

                message = (
                    f"**Title**: {title}\n"
                    f"**Authors**: {authors}\n"
                )
                await update.message.reply_text(message, parse_mode='Markdown')
        else:
            await update.message.reply_text('No books found matching your query.')
    else:
        await update.message.reply_text('Failed to fetch data from Google Books API.')



async def preview(update : Update , context: ContextTypes.DEFAULT_TYPE):
    user_q2 = ' '.join(context.args)

    if not user_q2:
        await update.message.reply_text('Please enter the name of the book you would like to preview')
        return
    params = {
    "q" : user_q2,
    "key": "AIzaSyCfeaj2C1PQ7FuQklK3ZVIvWCqbbVVkcxY"
    }
    response = requests.get(url,params=params)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items'])>0:
            book = data['items'][0]['volumeInfo']
            title = book.get('title', 'No title available')
            authors = ', '.join(book.get('authors', ['Unknown author']))
            description = book.get('description', 'No description available')
            preview_link = book.get('previewLink', 'No preview link available')
            
            message = f"**Title**: {title}\n**Authors**: {authors}\n**Description**: {description}\n[Preview Link]({preview_link})"
            await update.message.reply_text(message, parse_mode='Markdown')
        else:
            await update.message.reply_text('No books found matching your query.')
    else:
        await update.message.reply_text('Failed to fetch data from Google Books API.')

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        user_q3 = ' '.join(context.args)
    else:
        await update.message.reply_text('Please enter the name of the book.')
        return
    
    params = {
        "q": user_q3,
        "key": "AIzaSyCfeaj2C1PQ7FuQklK3ZVIvWCqbbVVkcxY"
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            book = data['items'][0]['volumeInfo']
            title = book.get('title', 'No title available')
            context.user_data['book_title'] = title  
            
            await update.message.reply_text(f'Book "{title}" found. Executing /reading_list command...')
            await reading_list(update, context) 
        else:
            await update.message.reply_text('No books found matching your query.')
    else:
        await update.message.reply_text('Failed to fetch data from Google Books API.')

async def reading_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    book_title = context.user_data.get('book_title', 'No book selected')

    buttons = [
        [InlineKeyboardButton("Add a book", callback_data='add_book')],
        [InlineKeyboardButton("Delete a book", callback_data='delete_book')],
        [InlineKeyboardButton("View Reading List", callback_data='view_list')]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(f'Manage your reading list for "{book_title}":', reply_markup=keyboard)

async def button_handler(update : Update , context : ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    reading_list = context.user_data.get('reading_list', [])
    book_title = context.user_data.get('book_title', 'No book selected')

    if query.data=="add_book":
        if book_title != 'No book selected.':
            if book_title not in reading_list:
                reading_list.append(book_title)
                context.user_data['reading_list'] = reading_list
                await query.message.reply_text(f'Book ${book_title} added to your archieve')
            else:
                await query.message.reply_text(f'Book ${book_title} already in your archieve')
        else:
            await query.message.reply_text(f'No book selected')


    elif query.data == "delete_book":
        if book_title in reading_list:
            reading_list.remove(book_title)
            context.user_data['reading_list'] = reading_list
            await query.message.reply_text(f'Book "{book_title}" removed from your reading list.')
        else:
            await query.message.reply_text("Book not found in your reading list.")


    elif query.data == "view_list":
        if reading_list:
            list_message = "Your Reading List:\n" + "\n".join(reading_list)
        else:
            list_message = "Your reading list is empty."
        await query.message.reply_text(list_message)
    
    else:
        await query.message.reply_text(f'Please click one button to proceed')

async def error(update : Update , context : ContextTypes.DEFAULT_TYPE):
    print('Update {update} caused the {context.error}')


if __name__=='__main__':
    print('Starting bot.....')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("book",book))
    app.add_handler(CommandHandler("preview",preview))
    app.add_handler(CommandHandler("list",list))
    app.add_handler(CommandHandler("reading_list",reading_list))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
