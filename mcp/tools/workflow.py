"""Workflow orchestration engine."""
import os

PHASE_MAP = {}

def step(slug, workflow, phase, scale=None, context=None):
    return {"workflow": workflow, "phase": phase, "steps": [], "total": 0}

def code_graph_resolve(slug, task, mode="explore"):
    return {"tool": "code_graph_resolve", "chain": [], "rule": "Never fall back to Read+Grep"}
