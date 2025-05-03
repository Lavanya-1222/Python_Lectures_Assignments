import mysql.connector

print("Starting connection attempt...")

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',    # Make sure this is correct
        password='lava',  # Ensure the password is correct
        # database='your_database',  # Optional for testing
        connection_timeout=10  # Set timeout for connection
    )

    if connection.is_connected():
        print("✅ Connected to MySQL database!")
    else:
        print("⚠️ Connection failed silently. Check database settings.")

except mysql.connector.Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection is closed")
    else:
        print("🔁 No active connection to close.")
