#!/usr/bin/env python3
"""Prepare a complete current-nine-control combined warm using the original formulas.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The current response, corrected provider, owned resource paths and full grid
are retained; a selected finite LP point is not an accepted nonlinear solution.
"""
from root_geometry_anchor_current_interfaces import build


def main():
    namespace,unused=build('combined',__file__)
    namespace['main']()


if __name__=='__main__':main()
