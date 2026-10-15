class SocraticPromptCompiler:
    """Dynamically compiles system prompts for professor nodes based on academic rigor level."""
    def __init__(self, base_persona: str):
        self.persona = base_persona

    def compile(self, topic: str, difficulty: str = "doctorate") -> str:
        rigor_instructions = {
            "undergraduate": "Explain concepts clearly with fundamental examples.",
            "graduate": "Assume foundational knowledge and introduce architectural trade-offs.",
            "doctorate": "Examine bleeding-edge mathematical proofs, edge cases, and perform rigorous source code critique."
        }
        return f"""[Persona: {self.persona}]
[Rigor Level: {difficulty.upper()}]
{rigor_instructions.get(difficulty, rigor_instructions['doctorate'])}
Topic of Discourse: {topic}"""
