
import frappe
import json

@frappe.whitelist()
def create_partial_invoice(sales_order, percentage):
	percentage = json.loads(percentage)
	so = frappe.get_doc("Sales Order", sales_order)
	
	doc = frappe.new_doc("Sales Invoice")
	item = []
	tab = so.items
	for i in range(0, len(tab)):
		qty = tab[i].get("qty")
		per = percentage
		percentage_decimal = per / 100
		balance = percentage_decimal * qty
		# rounded_qty = round(balance)
		
		# so.items[i].invoice_qty = tab[i].get("invoice_qty")+rounded_qty
		
		item.append({
			"custom_ref_no": tab[i].get("custom_ref_no"),
			"item_code": tab[i].get("item_code"),
			"qty": balance,
			"original_qty": tab[i].get("qty"),
			"rate": tab[i].get("rate"),
			"amount": tab[i].get("rate")*balance,
			"original_amount": tab[i].get("amount"),
			"project": tab[i].get("project"),
			"sales_order": sales_order,
			"so_detail": tab[i].get("name")
		})
	doc.update({
		"customer": so.customer,
		"company": so.company,
		"posting_date": so.delivery_date,
		"due_date": so.delivery_date,
		"order_percentage": percentage,
		"items": item,
		"original_total": so.total,
		"taxes_and_charges": so.taxes_and_charges,
		"vat_emirate": so.vat_emirate,
		"project": so.project
	})
	doc.save(ignore_permissions=True)
	so.partial_invoice = so.partial_invoice + percentage
	so.save(ignore_permissions=True)
	frappe.msgprint("Partial Sales Invoice created successfully.")
	return doc.name

