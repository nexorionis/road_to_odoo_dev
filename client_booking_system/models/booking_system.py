from odoo import models,fields


class BookingSystem(models.Model):
    _name = 'booking.system' #booking_system
    _description = 'Booking System'

    name = fields.Char('Name')