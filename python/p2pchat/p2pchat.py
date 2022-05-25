#import the necessary packages to start a listen server on port 4000
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import requests
import os
import sys
import time
import datetime
import random
import numpy as np

#define the function responsibile to handle the connection
def handle_connection(conn):
    #receive the data from the client
    data = conn.recv(1024)
    #decode the data
    data = data.decode()
    #print the data
    print(data)
    #send the data back to the client
    conn.send(data.encode())
    #close the connection
    conn.close()
