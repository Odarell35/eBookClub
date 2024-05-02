from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import json
from web_site import db, app
from web_site.models.Books_model import Books
from web_site.models.contact import Contact_us
from web_site.models.Category_model import Category
from web_site.models.Review_model import Reviews
from web_site.models.User_model import User
from flask_login import login_required, current_user

app_views = Blueprint('app_views', __name__)

@app_views.route('/', strict_slashes=False)
def landing():
    return render_template("landing.html")

@app_views.route('/Home', strict_slashes=False)
@login_required
def home():
    """home page"""
    #return jsonify({"success": True, "redirect": url_for('app_views.my_account')})
    return render_template("index.html")

@app_views.route('/About', strict_slashes=False)
def about():
    """About page"""
    return render_template("about.html")


@app_views.route('/Category', strict_slashes=False)
def category():
    categories = Category.query.all()
    
    return render_template("categories.html", categories=categories, title='categories')

@app_views.route('/book_by_category/<category_name>/', strict_slashes=False)
def list_books(category_name):
    categories = Category.query.filter_by(category_name=category_name).all()

    book = Books.query.filter_by(Catergory_name=category_name).all()
    

    return render_template('books_by_cat.html', book=book, categories=categories)


@app_views.route('/single_book/<int:book_id>', strict_slashes=False)
def single_book(book_id):
    book = Books.query.get(book_id)
    cat = book.Catergory_name
    img = book.img_link
    if book:
        return render_template('single_book.html', book=book, cat=cat, img=img, book_id=book.id)
    else:
        return ('NOT FOUND'), 404

@app_views.route('/books', strict_slashes=False)
def books():
    books = Books.query.all()

    return render_template("books.html", books=books)

@app_views.route('/review/<int:book_id>', methods=['GET', 'POST'], strict_slashes=False)
def review(book_id):
    book = Books.query.get(book_id)
    if request.method == 'POST':
        data = request.get_json()
        review_text = data.get('review_text')
        rating = int(data.get('rating'))
        
        if book:
            new_review = Reviews(
                Book_id=book.id,
                Bookname=book.title,
                user_id=current_user.id,
                username=current_user.name,
                Review_text=review_text,
                rating=rating
            )

            db.session.add(new_review)
            db.session.commit()

            db.session.close()
            flash('Review posted successfully!', category='success')
            return jsonify({"success": True, "redirect": url_for('app_views.post_review')})
        else:
            flash("No book found")

    return render_template('review.html', book=book)

@app_views.route('/post_review',  strict_slashes=False)
@login_required
def post_review():
    list_reviews = Reviews.query.all()

    return render_template("all_reviews.html", list_reviews=list_reviews)

@app_views.route('/My_account',  strict_slashes=False)
@login_required
def my_account():
    user = User.query.get(current_user.id)
    user_id = user.id
    q = Reviews.query.filter_by(user_id=current_user.id).all()
    return render_template("my_account.html", user=user, q=q )

@app_views.route('/contact-us', strict_slashes=False, methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        data = request.get_json()
        name1 = data.get('name')
        email1 = data.get('email')
        phone = data.get('phone_number')
        message_box = data.get('message_box')

        new_details = Contact_us(name=name1, email=email1, phone_number=phone, message_box=message_box)
        db.session.add(new_details)
        db.session.commit()
        db.session.close()
        return jsonify({'success': True, 'redirect': url_for('app_views.home')})
    
    return render_template("contact.html")
