import os

print("📥 Downloading protected MOHIT Downloader...")

# Download files from correct raw URLs
os.system("curl -O https://raw.githubusercontent.com/MohitGu2006/YouTube-video-download-Only-Termux/main/main.py")
os.system("curl -O https://raw.githubusercontent.com/MohitGu2006/YouTube-video-download-Only-Termux/main/pyarmor_runtime_000000/__init__.py")
os.system("curl -O https://raw.githubusercontent.com/MohitGu2006/YouTube-video-download-Only-Termux/main/pyarmor_runtime_000000/pyarmor_runtime.pyd")

# Setup runtime folder
os.makedirs("pyarmor_runtime_000000", exist_ok=True)
os.rename("__init__.py", "pyarmor_runtime_000000/__init__.py")
os.rename("pyarmor_runtime.pyd", "pyarmor_runtime_000000/pyarmor_runtime.pyd")

# Run main script
os.system("python main.py")

# Optional cleanup (uncomment if needed)
# os.remove("main.py")
# os.remove("runner.py")
