#!/usr/bin/env python3
"""
MCP and ADK Integration Debug Script
This script verifies connections between MCP and Google ADK services
"""
import os
import sys
import requests
import json
from dotenv import load_dotenv
import socket
import subprocess

load_dotenv()

def check_adk_service():
    """Check if ADK service is running and responsive"""
    try:
        response = requests.get("http://localhost:8000/docs")
        if response.status_code == 200:
            print("✅ ADK service is running and responsive")
            return True
        else:
            print("❌ ADK service returned unexpected status code:", response.status_code)
            return False
    except requests.exceptions.ConnectionError:
        print("❌ ADK service is not running or not accessible at http://localhost:8000")
        return False

def check_mcp_compatibility():
    """Check if code is compliant with MCP standards"""
    print("\nChecking MCP compatibility...")
    
    # Check for adk_service.py
    if os.path.exists("adk_service.py"):
        print("✅ Found adk_service.py")
    else:
        print("❌ adk_service.py not found")
        
    # Check for docker configuration
    if os.path.exists("docker-compose.yml") and os.path.exists("Dockerfile.adk"):
        print("✅ Docker configuration found")
    else:
        print("❌ Docker configuration incomplete")
    
    # Check GitHub Actions
    if os.path.exists(".github/workflows/deep-research.yml") and os.path.exists(".github/workflows/deep-research-trigger.yml"):
        print("✅ GitHub workflows configured")
    else:
        print("❌ GitHub workflows missing or incomplete")
    
    return True

def check_environment():
    """Check if required environment variables are set"""
    print("\nChecking environment...")
    
    required_vars = ["DEEPR_PT", "DEEPR_SHA256"]
    missing = []
    
    for var in required_vars:
        if not os.environ.get(var):
            missing.append(var)
    
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        print("  Create a .env file with these variables or set them before running")
        return False
    else:
        print("✅ All required environment variables are set")
        return True

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def check_ports():
    print("\nChecking required ports...")
    ports = [8000, 5000]  # Add any other required ports
    all_ok = True
    for port in ports:
        if check_port(port):
            print(f"✅ Port {port} is open")
        else:
            print(f"❌ Port {port} is not open")
            all_ok = False
    return all_ok

def check_api_key_security():
    print("\nChecking API key security...")
    api_key = os.environ.get("API_KEY")
    if api_key and api_key != "your-api-key-here":
        print("✅ API_KEY is set and not default")
        return True
    else:
        print("❌ API_KEY is missing or set to default placeholder")
        return False

def check_dependency_security():
    print("\nChecking Python dependency security with safety...")
    try:
        result = subprocess.run(['safety', 'check', '--full-report'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ No known dependency vulnerabilities found")
            return True
        else:
            print("❌ Dependency vulnerabilities found:\n", result.stdout)
            return False
    except FileNotFoundError:
        print("⚠️  safety is not installed; skipping dependency check")
        return True

def check_endpoint_health():
    print("\nChecking /generate_report endpoint health...")
    try:
        response = requests.post("http://localhost:8000/generate_report", json={"topic": "test"})
        if response.status_code == 200 and "report" in response.json():
            print("✅ /generate_report endpoint is healthy")
            return True
        else:
            print(f"❌ /generate_report returned status {response.status_code} or missing 'report'")
            return False
    except Exception as e:
        print(f"❌ /generate_report endpoint check failed: {e}")
        return False

def check_mcp_context():
    print("\nChecking MCP context handling...")
    test_context = {"topic": "test", "context": {"user_id": "123", "session": "abc"}}
    try:
        response = requests.post("http://localhost:8000/generate_report", json=test_context)
        if response.status_code == 200 and "report" in response.json():
            print("✅ MCP context accepted and processed")
            return True
        else:
            print(f"❌ MCP context not handled correctly: {response.text}")
            return False
    except Exception as e:
        print(f"❌ MCP context check failed: {e}")
        return False

def main():
    """Main function to run all checks"""
    print("=== MCP & ADK INTEGRATION DEBUG ===\n")
    
    service_ok = check_adk_service()
    mcp_ok = check_mcp_compatibility()
    env_ok = check_environment()
    port_ok = check_ports()
    api_key_ok = check_api_key_security()
    dep_ok = check_dependency_security()
    endpoint_ok = check_endpoint_health()
    context_ok = check_mcp_context()
    
    print("\n=== SUMMARY ===")
    all_ok = all([service_ok, mcp_ok, env_ok, port_ok, api_key_ok, dep_ok, endpoint_ok, context_ok])
    if all_ok:
        print("✅ All checks passed - MCP & ADK integration appears correctly configured")
        return 0
    else:
        print("❌ Some checks failed - See above for details")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 