from odoo import api, fields, models, _, tools
import logging
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning



_logger = logging.getLogger(__name__)

#   Sale Order Line Item 메뉴 구현 부분

class SaleOrderItem(models.Model):
    _inherit = 'sale.order.line'

    tax_ids = fields.Many2many('sale.order.line.tax_id', string="단기/세금")
    add_text = fields.Html(string='Text')


#   Sale Other Info Reporting 구현 부분

class SaleInfoReporting(models.Model):
    _inherit = 'sale.order'

    opportunity_id = fields.Many2one(
        'crm.lead', string='Opportunity', check_company=True,
        domain="[('type', '=', 'opportunity'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    customer_code_id = fields.Many2one('res.partner.customer_code', string='Customer Code')


# Contacts Customer Code 구현 부분

class ResPartner(models.Model):
    _inherit='res.partner'

    default_code = fields.Char(string='Customer Code', required=True)


    def _get_name(self):
        """ Utility me thod to allow name_get to be overrided without re-browse the partner """
        partner = self
        name = super(ResPartner, self)._get_name()
        return "[%s] %s" % (partner.default_code or '', name)

        if partner.company_name or partner.parent_id:
            if not name and partner.type in ['invoice', 'delivery', 'other']:
                name = dict(self.fields_get(['type'])['type']['selection'])[partner.type]
            #if not partner.is_company:
            #    name = "%s, %s" % (partner.commercial_company_name or partner.parent_id.name, name)
        if self._context.get('show_address_only'):
            name = partner._display_address(without_company=True)
        if self._context.get('show_address'):
            name = name + "\n" + partner._display_address(without_company=True)
        name = name.replace('\n\n', '\n')
        name = name.replace('\n\n', '\n')
        if self._context.get('address_inline'):
            name = name.replace('\n', ', ')
        if self._context.get('show_email') and partner.email:
            name = "%s <%s>" % (name, partner.email)
        if self._context.get('html_format'):
            name = name.replace('\n', '<br/>')
        if self._context.get('show_vat') and partner.vat:
            name = "%s %s" % (name, partner.vat)

        return name

    _sql_constraints = [
        ('name_unique', 'UNIQUE(display_name)', "'Customer Code' must be unique."),
    ]

# Purchase Merge 부분
class PuchaseOrderNames(models.Model):
    _inherit = 'merge.purchase.order'




