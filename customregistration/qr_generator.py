import qrcode
import frappe

def create_qr_code(doc, method=None):
#   print(doc.first_name)
    registered_user = frappe.new_doc("Qr_Generator")
    registered_user.first_name = doc.first_name
    data = {
        "first_name": doc.first_name
    }

    filename = "profile.png"
    img = qrcode.make(data)
    registered_user.profile_image = img.save(filename)
    registered_user.save()
    
