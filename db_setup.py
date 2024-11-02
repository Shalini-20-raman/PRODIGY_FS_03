import sqlite3


def init_db():
    conn = sqlite3.connect('stationery.db')
    cursor = conn.cursor()

    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price REAL,
            stock INTEGER,
            image TEXT
        )
    ''')

    # Insert up to 50 products
    products = [('Notebook', 'A5 size, ruled, 100 pages', 2.99, 100, 'product_1.jpg'),
        ('Pen', 'Ballpoint pen, blue ink', 0.99, 200, 'product_2.jpg'),
        ('Highlighter', 'Set of 4 highlighters', 4.50, 150, 'product_3.jpg'),
        ('Stapler', 'Standard stapler with 1000 staples', 3.25, 75, 'product_4.jpg'),
        ('Paper Clips', 'Pack of 100 paper clips', 1.50, 300, 'product_5.jpg'),
        ('Sticky Notes', 'Pack of 5 color sticky notes', 3.99, 250, 'product_6.jpg'),
        ('Binder', '1-inch ring binder', 4.75, 120, 'product_7.jpg'),
        ('Scissors', '8-inch sharp scissors', 2.99, 80, 'product_8.jpg'),
        ('Glue Stick', 'Pack of 2 large glue sticks', 1.75, 180, 'product_9.jpg'),
        ('Ruler', '12-inch plastic ruler', 0.99, 160, 'product_10.jpg'),
        ('Correction Tape', 'Pack of 3 correction tapes', 2.99, 90, 'product_11.jpg'),
        ('Eraser', 'Non-smudge eraser', 0.50, 400, 'product_12.jpg'),
        ('Pencil', 'Set of 12 HB pencils', 1.99, 220, 'product_13.jpg'),
        ('Whiteboard Marker', 'Pack of 4 assorted colors', 4.50, 140, 'product_14.jpg'),
        ('Calculator', 'Basic 8-digit calculator', 5.99, 100, 'product_15.jpg'),
        ('Desk Organizer', 'Mesh desk organizer', 7.99, 70, 'product_16.jpg'),
        ('File Folder', 'Pack of 10 plastic folders', 6.25, 130, 'product_17.jpg'),
        ('Tape Dispenser', 'Weighted tape dispenser', 3.50, 60, 'product_18.jpg'),
        ('Marker', 'Permanent marker, black', 1.25, 180, 'product_19.jpg'),
        ('Pencil Sharpener', 'Manual pencil sharpener', 1.00, 250, 'product_20.jpg'),
        ('Envelope', 'Pack of 50 white envelopes', 3.75, 120, 'product_21.jpg'),
        ('Clipboard', 'Standard letter-size clipboard', 2.50, 85, 'product_22.jpg'),
        ('Index Cards', 'Pack of 100 index cards', 1.99, 200, 'product_23.jpg'),
        ('Push Pins', 'Pack of 100 push pins', 1.50, 240, 'product_24.jpg'),
        ('Hole Punch', '3-hole punch, adjustable', 6.99, 90, 'product_25.jpg'),
        ('Rubber Bands', 'Pack of 500 rubber bands', 2.50, 300, 'product_26.jpg'),
        ('Letter Tray', 'Stackable letter tray', 4.99, 100, 'product_27.jpg'),
        ('Desk Mat', 'Leather desk writing pad', 12.99, 50, 'product_28.jpg'),
        ('Staple Remover', 'Standard staple remover', 1.50, 180, 'product_29.jpg'),
        ('Paper Shredder', 'Cross-cut paper shredder', 39.99, 30, 'product_30.jpg'),
        ('Label Maker', 'Portable label maker', 24.99, 40, 'product_31.jpg'),
        ('Business Cards', 'Pack of 100 blank business cards', 7.99, 110, 'product_32.jpg'),
        ('Presentation Folder', 'Set of 5 presentation folders', 5.50, 75, 'product_33.jpg'),
        ('Binder Clips', 'Pack of 12 large binder clips', 2.99, 150, 'product_34.jpg'),
        ('Staples', 'Box of 1000 staples', 1.25, 220, 'product_35.jpg'),
        ('Document Holder', 'Plastic document holder', 3.50, 130, 'product_36.jpg'),
        ('Desk Lamp', 'LED desk lamp', 15.99, 40, 'product_37.jpg'),
        ('Memo Pad', 'Pack of 3 memo pads', 2.99, 200, 'product_38.jpg'),
        ('Laminating Pouches', 'Pack of 50 A4 laminating pouches', 9.99, 70, 'product_39.jpg'),
        ('Mouse Pad', 'Standard mouse pad', 4.50, 100, 'product_40.jpg'),
        ('Document Scanner', 'Portable document scanner', 89.99, 15, 'product_41.jpg'),
        ('Presentation Board', 'Whiteboard with stand', 49.99, 20, 'product_42.jpg'),
        ('Shipping Labels', 'Pack of 200 shipping labels', 12.99, 60, 'product_43.jpg'),
        ('Pen Holder', 'Metal mesh pen holder', 3.99, 80, 'product_44.jpg'),
        ('USB Flash Drive', '32GB USB flash drive', 9.99, 90, 'product_45.jpg'),
        ('Desk Chair Cushion', 'Memory foam chair cushion', 19.99, 35, 'product_46.jpg'),
        ('Paper Cutter', 'A4 guillotine paper cutter', 29.99, 25, 'product_47.jpg'),
        ('Writing Pad', 'A4 size writing pad', 2.99, 160, 'product_48.jpg'),
        ('Desk Divider', 'Felt desk privacy divider', 39.99, 20, 'product_49.jpg'),
        ('Office Chair', 'Ergonomic office chair', 129.99, 10, 'product_50.jpg')
    ]

    cursor.executemany('''
        INSERT INTO products (name, description, price, stock, image) 
        VALUES (?, ?, ?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
