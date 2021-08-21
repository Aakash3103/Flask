# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 21:14:57 2021

@author: aakas
"""

from flask import Flask,render_template
app= Flask(__name__)


#Making Dictionaries
posts=[
      {'Name':'Aakash',
       'Qualification':"Master's",
       'learning':'Flask'},
      
      {'Name':'Anurag',
       'Qualification':"Master's",
       'learning':'Hadoop pyspark'
       },
      
      {'Name':'XYZ',
       'Qualification':"Bacheler's",
       'learning':'XXX'
       }
      ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title='home_page')

@app.route("/about")
def about():
    return render_template('about.html',title='about_Page')

if __name__=='__main__':
    app.run(debug=True)
