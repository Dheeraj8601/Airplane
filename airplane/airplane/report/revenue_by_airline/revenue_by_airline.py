import frappe

def execute(filters=None):
    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 150},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 150}
    ]
    
    data = get_data(filters)
    
    return columns, data

def get_data(filters):
    data = []

    # Execute SQL query to fetch revenue by airline
    sql_query = """
        SELECT
            airline AS Flight,
            SUM(total_amount) AS `Total Amount`
        FROM
            `tabAirplane Ticket`
        WHERE
            airline IS NOT NULL
            AND ticket_status != 'Cancelled'
        GROUP BY
            airline;
    """
    result = frappe.db.sql(sql_query, as_dict=True)
    
    # Format result as per the expected data structure
    for row in result:
        data.append({"airline": row["Flight"], "revenue": row["Total Amount"]})
    
    return data
