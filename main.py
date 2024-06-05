import cgi
import os

print("Content-Type: text/html")
print()

# Get the user's IP address
ip_address = os.environ.get("REMOTE_ADDR", "Unknown")

# Save the IP address to a file
with open("IPs.txt", "a") as file:
    file.write(f"{ip_address}\n")

print("<html><body>")
print("<h1>IP Address Logged</h1>")
print(f"<p>Your IP address ({}) has been logged.</p>")
print("</body></html>")
