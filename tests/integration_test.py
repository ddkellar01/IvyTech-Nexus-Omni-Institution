import pytest
import sys
import os

# Ensure root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cybersecurity.socratic_auditor import SocraticSecurityAuditor

def test_end_to_end_symposium_workflow():
    print("[IntegrationTest] Starting end-to-end multi-agent professor workflow verification...")
    
    # Instantiate audit component
    auditor = SocraticSecurityAuditor(security_professor_id="Dr. Securington")
    sample_code = "print('IvyTech Omni-Swarm Operational')"
    audit_res = auditor.audit_peer_code(sample_code)
    
    assert audit_res["status"] == "Secure"
    print("[IntegrationTest] End-to-end workflow verified successfully.")

if __name__ == "__main__":
    test_end_to_end_symposium_workflow()
