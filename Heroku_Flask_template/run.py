# imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import time
import pickledb


# initialize Flask app
app = Flask(__name__)


# flask routes
@app.route('/')
def base():
    return render_template('base.html', title="Home")



# run Flask app
if __name__ == '__main__':
    app.run(debug=True)
    
