# reports.py
def generate_report(orders):
    """Generate a basic report from completed/cancelled order records."""
    completed = 0
    cancelled = 0
    sales = 0.0
    cancelled_value = 0.0

    # Nested loop: outer loop processes orders; inner loop can process items.
    for order_record in orders:
        status = order_record["status"]

        if status == "COMPLETED":
            completed += 1
            sales += order_record["total"]

            for item, quantity in order_record["items"].items():
                # This loop demonstrates item-level processing for reporting.
                _ = item, quantity

        elif status == "CANCELLED":
            cancelled += 1
            cancelled_value += order_record["total"]

    return {
        "completed_orders": completed,
        "cancelled_orders": cancelled,
        "sales": sales,
        "cancelled_value": cancelled_value,
    }


def display_report(report):
    """Display the report in a readable format."""
    print("\n========== ORDER REPORT ==========")
    print(f"Completed orders:       {report['completed_orders']}")
    print(f"Cancelled orders:       {report['cancelled_orders']}")
    print(f"Total sales:            ₹{report['sales']:.2f}")
    print(f"Cancelled order value:  ₹{report['cancelled_value']:.2f}")
    print("==================================")
