from flask import Blueprint, render_template, request
from .controllers import TicketController

main = Blueprint("main", __name__)

controller = TicketController()

@main.route("/")
def home():
    bookings = controller.list_bookings()
    return render_template("index.html", bookings=bookings)

@main.route("/book", methods=["GET","POST"])
def book():
    if request.method == "POST":
        name = request.form["name"]
        movie = request.form["movie"]
        seats = request.form["seats"]

        controller.create_booking(name,movie,seats)

        return render_template("success.html")

    return render_template("booking.html")