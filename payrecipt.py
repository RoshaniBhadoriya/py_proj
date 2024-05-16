from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import uuid

def create_receipt(receipt_number, customer_name, book_title, amount_paid, payment_method):
    doc = SimpleDocTemplate("payment_receipt.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    # Define content
    content = []

    # Header
    header_text = "<b>Payment Receipt</b>"
    header_para = Paragraph(header_text, styles['Title'])
    content.append(header_para)
    content.append(Spacer(1, 12))

    # Receipt Number
    receipt_number_text = f"<b>Receipt Number:</b> {receipt_number}"
    receipt_number_para = Paragraph(receipt_number_text, styles['Normal'])
    content.append(receipt_number_para)
    content.append(Spacer(1, 12))

    # Date
    date_text = f"<b>Date:</b> {datetime.now().strftime('%Y-%m-%d')}"
    date_para = Paragraph(date_text, styles['Normal'])
    content.append(date_para)
    content.append(Spacer(1, 12))

    # Customer Name
    customer_text = f"<b>Customer:</b> {customer_name}"
    customer_para = Paragraph(customer_text, styles['Normal'])
    content.append(customer_para)
    content.append(Spacer(1, 12))

    # Book Title
    title_text = f"<b>Book Title:</b> {book_title}"
    title_para = Paragraph(title_text, styles['Normal'])
    content.append(title_para)
    content.append(Spacer(1, 12))

    # Amount Paid
    amount_text = f"<b>Amount Paid:</b> ${amount_paid:.2f}"
    amount_para = Paragraph(amount_text, styles['Normal'])
    content.append(amount_para)
    content.append(Spacer(1, 12))

    # Payment Method
    method_text = f"<b>Payment Method:</b> {payment_method}"
    method_para = Paragraph(method_text, styles['Normal'])
    content.append(method_para)
    content.append(Spacer(1, 12))

    # Thanks message
    thanks_text = "<b>Thank you for visiting!</b>"
    thanks_para = Paragraph(thanks_text, styles['Normal'])
    content.append(thanks_para)

    # Build PDF
    doc.build(content)

def get_input():
    customer_name = input("Enter customer name: ")
    book_title = input("Enter title of the book: ")
    amount_paid = float(input("Enter amount paid: "))
    payment_method = input("Enter payment method: ")
    return customer_name, book_title, amount_paid, payment_method

# Example usage
customer_name, book_title, amount_paid, payment_method = get_input()
receipt_number = str(uuid.uuid4())[:8]  # Generate a unique receipt number
create_receipt(receipt_number, customer_name, book_title, amount_paid, payment_method)
