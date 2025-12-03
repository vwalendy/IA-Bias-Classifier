import sys
import os

print("Importing httpx...")
try:
    import httpx
    print("Imported httpx.")
except Exception as e:
    print(f"Failed httpx: {e}")

print("Importing openai...")
try:
    import openai
    print("Imported openai.")
except Exception as e:
    print(f"Failed openai: {e}")
