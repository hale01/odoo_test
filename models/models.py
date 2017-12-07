# -*- coding: utf-8 -*-

from odoo import models, api


class TestCrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.onchange('email_from')
    def change_email_from(self):
        # mail.thread абстрактная модель, и всеравно использует MailMessage для хранения сообщений
        MailMessage = self.env['mail.message']
        MailMessage.create({
            'model': self._name,
            'body': f'Изменение поля "email_from". Старое значение {self._origin.email_from},'
                    f' новое значение {self.email_from}',
            'subject': 'Изменение поля "email_from"',
            'record_name': 'Изменение поля "email_from"',
            'message_type': 'notification',
            'res_id': self._origin.id,
        })
