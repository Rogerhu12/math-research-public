#!/usr/bin/env python3
"""Complete original mean warm geometry with the explicit corrected anchor hook.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Uses the frozen initial-laws entry and explicit old/new provider provenance.
The original --geometry-initial-laws-prepare-only option remains available.
"""
from strong_frontload_anchor_loader_adapter import build


def main():
    namespace,_=build('geometry',__file__);namespace['main']()


if __name__=='__main__':main()
