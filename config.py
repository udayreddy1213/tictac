from flask import Flask, render_template, request
import game_logic

app = Flask(__name__)

# Routes and functions to handle game interactions