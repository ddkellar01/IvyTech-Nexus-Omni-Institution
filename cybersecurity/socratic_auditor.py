class SocraticSecurityAuditor:
    def __init__(self, security_professor_id: str):
        self.auditor_id = security_professor_id

    def audit_peer_code(self, code_snippet: str) -> dict:
        print(f"[*] Professor {self.auditor_id} performing Socratic vulnerability audit...")
        vulnerabilities_found = []
        
        if "exec(" in code_snippet or "eval(" in code_snippet:
            vulnerabilities_found.append("Critical: Dynamic code execution detected.")
        if "subprocess.Popen" in code_snippet and "shell=True" in code_snippet:
            vulnerabilities_found.append("High: Shell injection vector identified.")
            
        return {
            "auditor": self.auditor_id,
            "status": "Vulnerable" if vulnerabilities_found else "Secure",
            "findings": vulnerabilities_found
        }
