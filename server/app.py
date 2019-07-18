#!/usr/bin/env python3
import uuid

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from flask_cors import CORS

#Config
DEBUG = True

#Instantiate app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config.from_object(__name__) #Not sure what this line is doing anymore

#Enables CORS
CORS(app, resources={r'/*': {'origins': '*'}})

class Ticket(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    issue_department = db.Column(db.String(120), unique=False)
    issue_type = db.Column(db.String(120), unique=False)
    issue = db.Column(db.String(120), unique=False)
    previous_ticket = db.Column(db.String(120), unique=False)
    location_site = db.Column(db.String(120), unique=False)
    location_room = db.Column(db.String(120), unique=False)
    submitted_by_first_name = db.Column(db.String(120), unique=False)
    submitted_by_last_name = db.Column(db.String(120), unique=False)
    contact_email = db.Column(db.String(120), unique=False)
    contact_phone = db.Column(db.String(120), unique=False)
    assigned_to = db.Column(db.String(120), unique=False)
    status = db.Column(db.String(120), unique=False)

    def __init__(
    self,
    id,
    issue_department,
    issue_type,
    issue,
    previous_ticket,
    location_site,
    location_room,
    submitted_by_first_name,
    submitted_by_last_name,
    contact_email,
    contact_phone,
    assigned_to,
    status
    ):
        self.id = id
        self.issue_department = issue_department
        self.issue_type = issue_type
        self.issue = issue
        self.previous_ticket = previous_ticket
        self.location_site = location_site
        self.location_room = location_room
        self.submitted_by_first_name = submitted_by_first_name
        self.submitted_by_last_name = submitted_by_last_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.assigned_to = assigned_to
        self.status = status

class TicketSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
        'id',
        'issue_department',
        'issue_type',
        'issue',
        'previous_ticket',
        'location_site',
        'location_room',
        'submitted_by_first_name',
        'submitted_by_last_name',
        'contact_email',
        'contact_phone',
        'assigned_to',
        'status')

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

def remove_ticket(ticket_id):
    for ticket in TICKETS:
        if ticket['id'] == ticket_id:
            TICKETS.remove(ticket)
            return True
    return False

@app.route("/tickets", methods=["POST"])
def add_ticket():
    id = uuid.uuid4().hex
    issue_department = request.json['issue_department']
    issue_type = request.json['issue_type']
    issue = request.json['issue']
    previous_ticket = request.json['previous_ticket']
    location_site = request.json['location_site']
    location_room = request.json['location_room']
    submitted_by_first_name = request.json['submitted_by_first_name']
    submitted_by_last_name = request.json['submitted_by_last_name']
    contact_email = request.json['contact_email']
    contact_phone = request.json['contact_phone']
    assigned_to = 'null'
    status = request.json['status']

    new_ticket = Ticket(
    id,
    issue_department,
    issue_type,
    issue,
    previous_ticket,
    location_site,
    location_room,
    submitted_by_first_name,
    submitted_by_last_name,
    contact_email,
    contact_phone,
    assigned_to,
    status
    )

    db.session.add(new_ticket)
    db.session.commit()

    return jsonify(request.json)
    #return jsonify(new_ticket)

@app.route("/tickets", methods=["GET"])
def get_tickets():
    response_object = {'status': 'sucess'}

    all_tickets = Ticket.query.all()
    tickets = tickets_schema.dump(all_tickets)

    response_object['tickets'] = tickets.data
    return jsonify(response_object)
@app.route("/tickets/<ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    response_object = {'status': 'success'}

    ticket = Ticket.query.get(ticket_id)
    response_object['ticket'] = ticket.data
    return jsonify(response_object)
@app.route("/tickets/<ticket_id>", methods=["DELETE"])
def delete_user(ticket_id):
    response_object = {'status': 'success'}

    ticket = Ticket.query.get(ticket_id)
    db.session.delete(ticket)
    db.session.commit()

    response_object['ticket'] = ticket.data
    return jsonify(response_object)
@app.route("/tickets/<ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    response_object = {'status': 'success'}

    ticket= Ticket.query.get(ticket_id)
    '''
    issue_department = request.json['issue_department']
    issue_type = request.json['issue_type']
    issue = request.json['issue']
    previous_ticket = request.json['previous_ticket']
    location_site = request.json['location_site']
    location_room = request.json['location_room']
    submitted_by_first_name = request.json['submitted_by_first_name']
    submitted_by_last_name = request.json['submitted_by_last_name']
    contact_email = request.json['contact_email']
    contact_phone = request.json['contact_phone']
    assigned_to = 'null'
    '''
    status = request.json['status']
    '''
    ticket.issue_department = issue_department
    ticket.issue_type = issue_type
    ticket.issue = issue
    ticket.previous_ticket = previous_ticket
    ticket.location_site = location_site
    ticket.location_room = location_room
    ticket.submitted_by_first_name = submitted_by_first_name
    ticket.submitted_by_last_name = submitted_by_last_name
    ticket.contact_email = contact_email
    ticket.contact_phone = contact_phone
    ticket.assigned_to = assigned_to
    '''
    ticket.status = status

    db.session.commit()

    response_object['ticket'] = ticket.data
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
