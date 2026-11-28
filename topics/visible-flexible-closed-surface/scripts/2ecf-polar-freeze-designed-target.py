#!/usr/bin/env python3
"""Freeze one actual saved log-radius target; no nonlinear step is counted.

The immutable metric definition keeps every binary64 coefficient as an
exact dyadic, the full physical spline, original mathematical base source,
and both endpoint two-jets. Later position solves cannot change alpha.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import math

SCHEMA = '2ecf-polar-actual-designed-target-freeze-v1'
DESIGN_SCHEMA = '2ecf-polar-full-XYZ-C2-log-radius-new-metric-design-LM-v1-state'
DESIGN_ENTRY_SHA = '21ce120289efa4f35decd7e7de120d501fa4392cb9bb4deb6c562e656662ea3d'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def load_frozen(path, prepared_sha=None, base_source=None, basis=None):
    saved = json.loads(Path(path).read_text())
    target = saved['frozenMetricDefinition']
    alpha = target['coefficients']
    if (saved.get('schema') != SCHEMA
            or saved['entrySHA256'] != sha(__file__)
            or canonical(target) != saved['frozenMetricDefinitionSHA256']
            or target['coefficientsStillProvisionalUntilDesignExplicitlyFrozen'] is not False
            or target['metricParametersFrozen'] is not True
            or len(alpha) != 87 or not all(math.isfinite(v) for v in alpha)
            or [float(v).hex() for v in alpha] != target['exactCoefficientHex']
            or saved['ownFrozenMetricAttempts'] != 0 or saved['ownFrozenMetricAcceptedSteps'] != 0):
        raise ValueError('Exact complete immutable target and zero freeze counters required')
    if prepared_sha is not None and saved['sourcePreparedSHA256'] != prepared_sha:
        raise ValueError('Original complete prepared source changed')
    if base_source is not None and target['baseSourceIdentity'] != base_source:
        raise ValueError('The frozen mathematical base source changed')
    if basis is not None and target['physicalSplineBasis'] != basis:
        raise ValueError('The frozen log-radius physical spline changed')
    return saved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--state', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError('A fresh immutable freeze manifest is required')
    state = json.loads(args.state.read_text())
    model, old = state['modelDefinition'], state['provisionalMetricDefinition']
    if (state.get('schema') != DESIGN_SCHEMA or not state['accepted']
            or canonical(model) != state['modelDefinitionSHA256']
            or model['solveEntrySHA256'] != DESIGN_ENTRY_SHA
            or canonical(old) != state['provisionalMetricDefinitionSHA256']
            or old['coefficients'] != state['logRadiusCoefficients']
            or old['physicalSplineBasis'] != model['basis']
            or old['baseSourceIdentity'] != model['baseSourceIdentity']
            or old['sourcePorts'] != model['sourcePorts']):
        raise ValueError('An actual accepted complete published design state is required')
    target = copy.deepcopy(old)
    target['schema'] = SCHEMA + '-immutable-metric-definition'
    target['coefficientsStillProvisionalUntilDesignExplicitlyFrozen'] = False
    target['metricParametersFrozen'] = True
    result = dict(schema=SCHEMA, entrySHA256=sha(__file__),
        parentDesignStateSHA256=sha(args.state),
        parentDesignModelDefinitionSHA256=state['modelDefinitionSHA256'],
        parentProvisionalMetricDefinitionSHA256=state['provisionalMetricDefinitionSHA256'],
        sourcePreparedSHA256=state['preparedSHA256'],
        sourceDefinitionSHA256=model['sourceMetadata']['sourceDefinitionSHA256'],
        parentDesignAcceptedSteps=state['ownMetricDesignAcceptedSteps'],
        parentDesignAttempts=state['ownMetricDesignAttempts'],
        frozenMetricDefinition=target, frozenMetricDefinitionSHA256=canonical(target),
        mathematicalMetricChangedByFreezing=False,
        allCoefficientsAndPhysicalSplineExactlyPreserved=True,
        sourcePositionUnchanged=True, targetPortTwoJetsUnchanged=True,
        freezeIsNotAnOptimizationAttempt=True, designAcceptsBorrowedAsFixedMetric=False,
        ownFrozenMetricAttempts=0, ownFrozenMetricAcceptedSteps=0,
        sameMetricRefinementNotYetComputed=True,
        continuousMetricCertified=False, wholeClosedReachCertified=False)
    args.output.write_text(json.dumps(result, separators=(',', ':'), allow_nan=False)+'\n')
    load_frozen(args.output)
    print(json.dumps(dict(event='actual_saved_target_frozen', SHA256=sha(args.output),
        frozenMetricDefinitionSHA256=result['frozenMetricDefinitionSHA256'],
        parentDesignAcceptedSteps=result['parentDesignAcceptedSteps'],
        newFixedMetricAccepts=0, alphaInfinityNorm=max(map(abs, target['coefficients'])))), flush=True)


if __name__ == '__main__':
    main()
