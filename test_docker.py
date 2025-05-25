#!/usr/bin/env python3
"""
Quick test script to verify Docker environment is working properly.
Run this inside the Docker container to test all imports.
"""

def test_imports():
    """Test that all required packages can be imported."""
    print("Testing imports...")
    
    try:
        import openai
        print("✓ openai")
    except ImportError as e:
        print(f"✗ openai: {e}")
    
    try:
        import pandas
        print("✓ pandas")
    except ImportError as e:
        print(f"✗ pandas: {e}")
    
    try:
        import numpy
        print("✓ numpy")
    except ImportError as e:
        print(f"✗ numpy: {e}")
    
    try:
        import yaml
        print("✓ yaml")
    except ImportError as e:
        print(f"✗ yaml: {e}")
    
    try:
        import requests
        print("✓ requests")
    except ImportError as e:
        print(f"✗ requests: {e}")
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv")
    except ImportError as e:
        print(f"✗ python-dotenv: {e}")

def test_file_structure():
    """Test that expected files are present."""
    print("\nTesting file structure...")
    
    import os
    expected_files = [
        "code/run_experiment.py",
        "requirements.txt",
        "README.md"
    ]
    
    for file_path in expected_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path}")

def test_environment():
    """Test environment variables."""
    print("\nTesting environment...")
    
    import os
    
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        print(f"✓ OPENAI_API_KEY is set ({openai_key[:8]}...)")
    else:
        print("! OPENAI_API_KEY not set (expected for test)")
    
    google_key = os.getenv("GOOGLE_MAPS_API_KEY") 
    if google_key:
        print(f"✓ GOOGLE_MAPS_API_KEY is set ({google_key[:8]}...)")
    else:
        print("! GOOGLE_MAPS_API_KEY not set (expected for test)")

if __name__ == "__main__":
    print("Docker Environment Test")
    print("=" * 30)
    
    test_imports()
    test_file_structure()
    test_environment()
    
    print("\n" + "=" * 30)
    print("Test complete! If no ✗ errors above, Docker setup is working.") 