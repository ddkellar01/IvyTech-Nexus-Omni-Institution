import pytest
from faculty.gemini_thinking_reasoning import GeminiThinkingEngine
from faculty.claude_craftsmanship import ClaudeCodeRefactorer
from pipelines.flowx_parallel_renderer import FlowXParallelRenderer

def test_omni_faculty_integration():
    gemini_chair = GeminiThinkingEngine()
    claude_prof = ClaudeCodeRefactorer()
    renderer = FlowXParallelRenderer(render_nodes_count=4)

    reasoning_res = gemini_chair.execute_deep_reasoning("Test Swarm Architecture")
    assert reasoning_res["status"] == "Reasoning Verified"

    refactored = claude_prof.audit_and_refactor("print('test')")
    assert "Refactored" in refactored

    output_asset = renderer.render_cinematic_sequence({})
    assert output_asset == "google_flowx_master_output.mp4"
