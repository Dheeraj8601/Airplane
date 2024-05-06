// Copyright (c) 2024, Dheeraj S and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {        
        frm.add_custom_button('Assign Seat', function() {    
            frappe.prompt([
                {
                    fieldname: 'seat_number',
                    label: 'Seat Number',
                    fieldtype: 'Data',
                    reqd: true 
                }
            ], function(values){
                frm.set_value('seat', values.seat_number);
            }, 'Enter Seat Number', 'Assign');
        });
    }
});
