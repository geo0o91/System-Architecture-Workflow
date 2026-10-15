import os

source_dir = "knowledge_source"
if not os.path.exists(source_dir):
    os.makedirs(source_dir)

# This physically writes your professional background into the text file
with open(os.path.join(source_dir, "sample.txt"), "w", encoding="utf-8") as f:
    f.write("George B is a WES-certified Computer Engineer based in Ottawa, Canada, specializing in AI Agent architectures and automated systems.")

print("✅ Professional profile written successfully to knowledge_source/sample.txt!")
