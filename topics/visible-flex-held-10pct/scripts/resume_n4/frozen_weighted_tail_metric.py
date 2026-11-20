"""Bind the actual WeightedTailPort to one unchanged background definition.

This wrapper does not launch a worker, solve an equation, change a tolerance,
or replace any original tail acceptance gate.  It reads the already-live
worker's full ready metadata and checks each actual response.  Its identity
errors are ValueError, not domain failures to hide in a Newton backtrack.

The mathematical background and its finite numerical evaluation are distinct.
The current constructor's calibration/integration settings are held fixed
here; proving that different settings evaluate one exact metric remains a
separate interval/analytic task.  No continuous or infinite-tail certificate
is returned by this module.
"""
import copy
import hashlib
import json
from pathlib import Path


_REQUIRED = (
    "rCut", "wCut", "width", "curvatureBound", "delta0", "R", "a",
    "etaPower", "etaRatioAtN0", "orientation", "prefixR", "prefixEnd",
    "prefixReturnStart", "protectCell", "calibrationSteps", "warpSteps",
    "quadratureTolerance", "slopeCap", "capTransition", "capMode",
    "cuspAwareQuadrature", "valleyControls", "rejoinR20At",
    "rejoinIndexOffset", "rCuff", "oldCut", "epsilonScale",
    "prefixRByCell", "constructor", "warpWeightLevels")
_OPTIONAL = (
    "pulseCaps", "valleyCaps", "flatOuterThroughCell",
    "flatOuterStartSegment", "flatSlope")
_CUT = ("radius", "backgroundSlope", "backgroundSecond", "E", "Ep")
_GEOMETRY_SOURCE_FILES = ("closing_weighted_tail.mjs",
                          "closing_recalibrated_tail.mjs")


class TailMetricIdentityError(ValueError):
    pass


def _key(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      allow_nan=False)


def metric_parameters(parameters):
    """Extract the complete current weighted constructor's metric settings."""
    missing = [key for key in _REQUIRED if key not in parameters]
    if missing:
        raise TailMetricIdentityError(
            "Full actual ready/checkpoint parameters required: "+", ".join(missing))
    if parameters["constructor"] != "closing_weighted_tail_v1":
        raise TailMetricIdentityError("Unsupported physical background constructor")
    return {key: copy.deepcopy(parameters.get(key))
            for key in (*_REQUIRED, *_OPTIONAL)}


class FrozenWeightedTailMetric:
    """Delegate original H -> DN while keeping its background contract fixed.

    expected_definition is a prior level's .definition, containing the full
    expanded metric parameters and geometry sources.  M/RK/angle quadrature/
    shooting partition/depth can then change between levels while these
    background settings remain the same.  That alone proves no refinement
    convergence or infinite-tail theorem.
    """
    def __init__(self, tail, *, prefix_port=None, expected_definition=None,
                 owner=None):
        self._tail = tail
        self._owner = owner
        ready = getattr(tail, "ready", None)
        if not isinstance(ready, dict) or "parameters" not in ready:
            raise TailMetricIdentityError("An already-live actual worker is required")
        self._parameters = copy.deepcopy(ready["parameters"])
        self._geometry = metric_parameters(self._parameters)
        self._ready_key = _key(self._parameters)
        self._sources_key = _key(tail.sources)
        self._worker = tail.proc
        self._config_path = Path(tail.config).resolve()
        config = json.loads(self._config_path.read_text())
        self._config_key = _key(config)
        # In particular, detect a config edited after the worker read it:
        # the original client reads that file again when recording a response.
        for key, value in config.items():
            if key in self._geometry and _key(value) != _key(self._geometry[key]):
                raise TailMetricIdentityError("Config and live background differ: "+key)
        worker_path = Path(self._worker.args[1]).resolve()
        loader = worker_path.with_name("closing_tail_sources.mjs")
        dependency = worker_path.parent.parent/"notes/closing_tail_dependency_blobs.json"
        source_binding = {name: tail.sources[name] for name in _GEOMETRY_SOURCE_FILES}
        source_binding["source_loader_sha256"] = hashlib.sha256(
            loader.read_bytes()).hexdigest()
        source_binding["dependency_blobs"] = json.loads(dependency.read_text())
        self._definition = dict(
            metric_parameters=copy.deepcopy(self._geometry),
            geometry_sources=source_binding)
        self._definition_key = _key(self._definition)
        if (expected_definition is not None and
                _key(expected_definition) != self._definition_key):
            raise TailMetricIdentityError("The preceding level's tail metric changed")
        self._cut = {key: ready["cut"][key] for key in _CUT}
        # The short prefix port is useful as a cross-check but omits defaults;
        # it is never the sole definition of the tail metric.
        self._port = prefix_port
        self._port_key = _key(prefix_port) if prefix_port is not None else None
        if prefix_port is not None:
            for key, value in prefix_port.get("parameters", {}).items():
                if key in self._geometry and _key(value) != _key(self._geometry[key]):
                    raise TailMetricIdentityError("Prefix port and live metric differ: "+key)
        self._prefix_cut_difference = (
            {key: float(prefix_port["cut"][key])-float(self._cut[key])
             for key in _CUT}
            if prefix_port is not None else None)

    def __getattr__(self, name):
        return getattr(self._tail, name)

    @property
    def definition(self):
        """Small scalar/source definition for the next refinement level."""
        return copy.deepcopy(self._definition)

    @property
    def description(self):
        return dict(
            fixed_tail_definition=self.definition,
            background_cut=copy.deepcopy(self._cut),
            prefix_minus_tail_cut=copy.deepcopy(self._prefix_cut_difference),
            config_sha256=hashlib.sha256(self._config_key.encode()).hexdigest(),
            config_hash_scope="canonical JSON, not the raw file bytes",
            same_live_tail_worker_required=True,
            original_acceptance_gates_changed=False,
            continuous_tail_metric_certified=False,
            fixed_g_refinement_convergence_proved=False,
            scope="checks the declared finite background, not an infinite-tail "
                  "existence or exact-integral evaluation certificate")

    def check(self):
        if (self._tail.proc is not self._worker or
                _key(self._tail.ready["parameters"]) != self._ready_key or
                _key(self._tail.sources) != self._sources_key or
                _key(json.loads(self._config_path.read_text())) != self._config_key):
            raise TailMetricIdentityError(
                "Actual tail worker, ready metadata, config or source binding changed")
        if self._port is not None and _key(self._port) != self._port_key:
            raise TailMetricIdentityError("The prefix port changed")
        if self._owner is not None:
            if self._owner.tail is not self or self._owner.port is not self._port:
                raise TailMetricIdentityError("The bound BVP tail or port was replaced")

    def solve(self, height, jacobian=True, audit=False):
        self.check()
        # Delegate to the original client: its convergence/failure handling
        # and caller's original residual threshold remain in force.
        response = self._tail.solve(height, jacobian=jacobian, audit=audit)
        checkpoint = response.get("checkpoint")
        if not isinstance(checkpoint, dict) or "parameters" not in checkpoint:
            raise TailMetricIdentityError(
                "Actual response lacks its complete background checkpoint")
        if _key(metric_parameters(checkpoint["parameters"])) != _key(self._geometry):
            raise TailMetricIdentityError("DN response changed the frozen metric")
        jets = response.get("jets", {})
        for key in _CUT:
            if key not in jets or jets[key] != self._cut[key]:
                raise TailMetricIdentityError("DN response changed background cut "+key)
        self.check()
        return response


def attach_frozen_tail_metric(obj, *, expected_definition=None):
    """Attach the guard to an already constructed BVP; no worker is launched."""
    wrapper = FrozenWeightedTailMetric(
        obj.tail, prefix_port=obj.port, expected_definition=expected_definition,
        owner=obj)
    obj.tail = wrapper
    return wrapper

