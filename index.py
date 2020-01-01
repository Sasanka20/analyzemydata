#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services/')
def services():
    return render_template('services.html')


@app.route('/about_me/')
def about_me():
    return render_template('about_me.html')


@app.route('/tools/')
def tools():
    return render_template('tools.html')


@app.route('/contact_form/')
def contact_form():
    return render_template('contact_form.html')


@app.route('/index_en/')
def index_english():
    return render_template('en_index.html')


@app.route('/services_en/')
def services_english():
    return render_template('en_services.html')


@app.route('/about_me_en/')
def about_me_english():
    return render_template('en_about_me.html')


@app.route('/tools_en/')
def tools_english():
    return render_template('en_tools.html')


@app.route('/contact_form_en/')
def contact_form_english():
    return render_template('en_contact_form.html')

# vim: set cin et ts=4 sw=4 ft=python :
