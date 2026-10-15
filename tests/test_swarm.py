import pytest
from cybersecurity.socratic_auditor import SocraticSecurityAuditor
from algorithms.rpp_engine import RecursivePeerPedagogyEngine

def test_security_auditor_flags_unsafe_code():
    auditor = SocraticSecurityAuditor(security_professor_id="Dr. Securington")
    unsafe_code = "exec('import os; os.system(\"rm -rf /\")')"
    result = auditor.audit_peer_code(unsafe_code)
    
    assert result["status"] == "Vulnerable"
    assert len(result["findings"]) > 0

def test_rpp_engine_requires_multiple_faculty():
    engine = RecursivePeerPedagogyEngine(faculty_nodes=[])
    with pytest.raises(ValueError):
        engine.execute_peer_review_symposium("Distributed Consensus")
