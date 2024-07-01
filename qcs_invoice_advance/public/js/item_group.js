frappe.ui.form.on('Item Group', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__("Update Price List"), () => {
				frappe.call({
					method: "qcs_invoice_advance.controller.item.update_item_price",
					args: {
						"item_group": cur_frm.doc.name,
                        "contract_price": cur_frm.doc.custom_contract_price,
                        "dealer_price": cur_frm.doc.custom_dealer_price,
                        "retail_price": cur_frm.doc.custom_retail_price
					},
					callback: function (r) {
						if (!r.exc) {
							if (r.message) {
								frappe.set_route("Form", "Account", r.message);
							}
							d.hide();
						}
					},
				});
			});
        }  
    }
});