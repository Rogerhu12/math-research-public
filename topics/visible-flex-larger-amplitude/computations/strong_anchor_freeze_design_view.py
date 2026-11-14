#!/usr/bin/env python3
"""Original genuine fixed-view conversion with explicit current-anchor hook.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original --prepare-source-record option does not load a field. Actual
conversion still requires the full original accepted raw/quintic/H/RMS/BC
identities and starts no new BVP or worker.
"""
from strong_frontload_anchor_loader_adapter import build


def main():
    namespace,_=build('fixed_view',__file__);namespace['main']()


if __name__=='__main__':main()
