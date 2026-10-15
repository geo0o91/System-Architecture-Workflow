import os

# Define the target directory
source_dir = "knowledge_source"

# 1. Ensure the folder exists
if not os.path.exists(source_dir):
    os.makedirs(source_dir)
    print(f"📁 Created folder: {source_dir}")

# 2. Overwrite the file with generic corporate IT system text
file_path = os.path.join(source_dir, "server_protocols.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(
        "PROTOCOL_ID: 9042\n"
        "SYSTEM_STATUS: Operational\n"
        "LOCATION: Toronto Data Center Rack 4\n"
        "CORE_STACK: Linux Ubuntu 22.04, PostgreSQL Cluster, Redis Cache.\n"
        "SECURITY_RULE: All inbound traffic to port 8080 must pass through the regional reverse proxy firewall."
    )
print(f"📝 Written corporate system protocols to: {file_path}")

# 3. Clean up and remove the old file containing personal info if it exists
old_file_path = os.path.join(source_dir, "sample.txt")
if os.path.exists(old_file_path):
    os.remove(old_file_path)
    print("🧹 Removed old sample.txt file containing personal information.")

print("\n✅ Step 1 complete! Your dataset is now completely generic and enterprise-ready.")
