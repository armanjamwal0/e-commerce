from flask import Flask , redirect , render_template , url_for , request , flash
from sqlalchemy import INTEGER, String , Float , Text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase , Mapped, mapped_column ,relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user , login_required
from flask_migrate import Migrate
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b" # hear create a flask key go to the chat gpt and search for create a flask key and here

login_manager = LoginManager()
login_manager.init_app(app)

class base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:arman123@localhost:5432/Zshop" # you can add here your own database url to  connect to pgadmin4 

db = SQLAlchemy(model_class=base)
migrate = Migrate(app, db)  # Add migration support
db.init_app(app)

class User(UserMixin, db.Model):

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(250),nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

class Product(db.Model):
    __tablename__ = "products"
    
    id:Mapped[int] = mapped_column(INTEGER, primary_key=True)
    title:Mapped[str] = mapped_column(String(250),nullable=False, unique=True)
    image:Mapped[str] = mapped_column(String(250),nullable=False)
    price:Mapped[int] = mapped_column(INTEGER,nullable=False)
    description:Mapped[str] = mapped_column(Text,nullable=False)
    color:Mapped[str] = mapped_column(String(250), nullable=False)
    discount:Mapped[int] = mapped_column(INTEGER,nullable=False)
    model:Mapped[str] = mapped_column(String(250),nullable=False)
    
    #forginkey Brand and category
    brand_id: Mapped[int] = mapped_column(INTEGER,db.ForeignKey('brands.id'), nullable=False)
    category_id: Mapped[int] = mapped_column(INTEGER,db.ForeignKey('categorys.id'), nullable=False)
    
    # relationship
    brand = relationship('Brand',back_populates='products')
    category = relationship('Category',back_populates='products')
    cart_items = relationship('Cart',back_populates='product')

class Brand(db.Model):
    __tablename__= "brands"
    id:Mapped[int] = mapped_column(INTEGER,primary_key=True)
    brand:Mapped[str] = mapped_column(String(250),nullable=False)
    
    products = relationship('Product',back_populates='brand')


class Category(db.Model):
    __tablename__ = "categorys"

    id:Mapped[int]  = mapped_column(INTEGER,primary_key=True)
    category:Mapped[str] = mapped_column(String(250),nullable=False)
    
    products = relationship('Product',back_populates='category')
    
class Cart(db.Model):
    __tablename__ = "carts"  # Corrected
    id:Mapped[int] = mapped_column(INTEGER,primary_key=True)
    quantity:Mapped[int] = mapped_column(INTEGER,nullable=False)
    
    product_id:Mapped[int] = mapped_column(INTEGER, db.ForeignKey('products.id'), nullable=False)
    
    product = relationship('Product',back_populates='cart_items')  

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    return User.query.get(int(user_id))

# # Custom error message when user is not logged in   , this is coustimize login_required that can 
# @login_manager.unauthorized_handler
# def unauthorized():
#     return render_template('error.html'),401 

@app.route('/')
def home():
    all_data = db.session.query(Product).all()
    return render_template('index.html', all_data = all_data)


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('Username')
        email = request.form.get('email')
        password = request.form.get('password')
        response = db.session.execute(db.select(User).where(User.email == email))
        user = response.scalar()
        
        if user :
            flash('This email is already Register')
            return redirect(url_for('register'))
        hash_password = generate_password_hash(password,
                                               method='pbkdf2:sha256',
                                               salt_length=16)
        new_user = User(
            name = name,
            email = email,
            password = hash_password
        )
        db.session.add(new_user)
        db.session.commit()
    return render_template('login_and_register.html')
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        response = db.session.execute(db.select(User).where(User.email == email))
        user = response.scalar()
        if not user:
            flash('Please Check Your Email')
        
        elif not  check_password_hash(user.password, password=password):
            flash('Please Check Your Password')
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login_and_register.html')


@app.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/product', methods=['GET','POST'])
def product():
    product_id = request.args.get('id')
    response = db.session.execute(db.select(Product).where(Product.id == product_id))
    data = response.scalar()    
    return render_template('product.html',data=data)



@app.route('/cart', methods=['POST','GET'])
def Cart_page():
    product_id = request.args.get('id')
    if product_id:  
        new_cart = Cart(
                quantity = 1,
                product_id = product_id
            )
        db.session.add(new_cart)
        db.session.commit()
        return redirect(url_for('Cart_page'))
    cart_data = db.session.execute(db.select(Cart,Product).join(Product,Cart.product_id == Product.id)).all()

    return render_template('cart.html', cart_data=cart_data)
@app.route('/delete')
def delete():
    cart_id  = request.args.get('id')
    cart_delete = db.session.execute(db.select(Cart).where(Cart.id == cart_id)).scalar()
    db.session.delete(cart_delete)
    db.session.commit()
    return redirect(url_for('Cart_page'))
if __name__ =="__main__":
    app.run(debug=True)