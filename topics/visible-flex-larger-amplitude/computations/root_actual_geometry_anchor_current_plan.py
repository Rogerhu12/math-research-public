#!/usr/bin/env python3
"""Prepare the same accepted M32 baseline and eighteen corrected-provider fields.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No field is computed by preparation; no future accepted input is supplied here.
"""
from root_geometry_anchor_current_interfaces import build


def main():
    namespace,unused=build('plan',__file__)
    namespace['main']()


if __name__=='__main__':main()
