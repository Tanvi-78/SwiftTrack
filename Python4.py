shipment = {
    "tracking_id": "SWIFT001",
    "status": "In Transit",
    "city": "Panvel",
    "delivery_date": "15 July 2026"
}

print(shipment["status"])     
shipment["delivery_date"] = "16 July 2026"  
shipment["priority"] = "High"  
for key, value in shipment.items():
    print(f"{key} -> {value}")
