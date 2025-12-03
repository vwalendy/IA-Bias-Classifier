import sys
import os

# Add current directory to sys.path
sys.path.append(os.getcwd())

print("Importing schemas...")
try:
    import models.schemas
    print("Imported schemas.")
except Exception as e:
    print(f"Failed schemas: {e}")

print("Importing llm_client...")
try:
    import services.llm_client
    print("Imported llm_client.")
except Exception as e:
    print(f"Failed llm_client: {e}")

print("Importing bias_analyzer...")
try:
    import services.bias_analyzer
    print("Imported bias_analyzer.")
except Exception as e:
    print(f"Failed bias_analyzer: {e}")

print("Importing main...")
try:
    from main import app
    print("Imported main.")
except Exception as e:
    print(f"Failed main: {e}")
