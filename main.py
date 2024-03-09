from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import json

from agent.board import *
from agent.alpha_beta import *
from agent.mcts import *

board = Board()

app = Flask(__name__)
app.secret_key = "3d"
app.config["DEBUG"] = True


@app.route("/", methods=("GET", "POST"))
def home():
    if request.method == "POST":
        session["diff"] = request.form["diff"]
        return redirect(url_for("index"))
    return render_template("home.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/postmethod", methods=["POST"])
def main():
    game_diff = session["diff"]
    game_mode = int(request.form["mode"])
    agent_turn = int(request.form["player"])
    cur_board = json.loads(request.form["board"].encode("utf-8"))

    board.input(cur_board, agent_turn)

    if game_mode == 2:
        return json.dumps(list(alpha_beta(board, 4, game_diff)))


app.run()
