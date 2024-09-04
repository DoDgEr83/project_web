from flask import Flask, request, jsonify
from functions import *
from sqlalchemy import create_engine
from Models import *
from Config import config

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:admin@lockalhost:3386/price_test"
# app.config.from_object(config)
# migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/page_1")
def page_1():
    name = request.args.get("name")
    if not name:
        return {"error": "Missing name"}
    return f"<h1> Hi {name} </h1>"


@app.route('/prices', methods=['GET', 'POST'])
def prices():
    return jsonify(get_prices(request.args['ticker']))


# @app.route('/upload_prices', methods=['GET', 'POST'])
# def upload_prices():
#     ticker = request.args['ticker']
#     prices_data = get_prices(ticker)
#     with Session(engine) as session:
#         prices_list = []
#         for price in prices_data:
#             prices_list.append(HistModel(date=price['Date'], close=price['Close'], ticker=ticker))
#         session.add_all(prices_list)
#         session.commit()
#     return jsonify(get_prices(request.args['ticker']))


@app.route('/upload_prices', methods=['GET', 'POST'])
def upload_prices():
    ticker = request.args['ticker']
    prices_data = get_prices(ticker)
    with Session(engine) as session:
        for price in prices_data:
            # Create an instance of the model
            hist_entry = HistModel(date=price['Date'], close=price['Close'], ticker=ticker)
            # Use the merge method to insert or update
            session.merge(hist_entry)
        session.commit()
    return jsonify(get_prices(request.args['ticker']))


if __name__ == '__main__':
    engine = create_engine(config("conn_str"), echo=True)
    Base.metadata.create_all(engine)
    app.run()
