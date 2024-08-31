import sys
import os

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"sys.path:")
for path in sys.path:
    print(f"  {path}")

try:
    import torch
    print(f"\nPyTorch version: {torch.__version__}")
    print(f"PyTorch installation directory: {os.path.dirname(torch.__file__)}")
    print(f"CUDA available: {torch.cuda.is_available()}")
except ImportError as e:
    print(f"\nFailed to import torch: {e}")
except Exception as e:
    print(f"\nAn error occurred while checking torch: {e}")

print("\nChecking for fbgemm.dll:")
torch_lib_path = os.path.join(os.path.dirname(torch.__file__), 'lib')
fbgemm_path = os.path.join(torch_lib_path, 'fbgemm.dll')
print(f"Expected path: {fbgemm_path}")
print(f"File exists: {os.path.exists(fbgemm_path)}")

print("\nListing files in torch lib directory:")
for file in os.listdir(torch_lib_path):
    print(f"  {file}")