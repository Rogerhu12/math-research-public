#!/usr/bin/env python3
"""R493 exact IEEE binary128 word -> binary64 protocol projection.

This is an independent library for a future same-job live response assembler.
It does not solve a tail, reconstruct any deleted array, select a native call,
or confer native/full-DN acceptance. Scientific callers must run in the public
Actions job and keep all ordinary original finite/shape/residual checks.

Only integer arithmetic chooses the binary64 word. struct merely installs
that selected word as a Python float; no decimal or binary64 arithmetic is an
intermediate rounding operation. Raw numeric arrays remain same-job payload.
"""
from __future__ import annotations

import hashlib
import os
import re
import struct
from pathlib import Path
from typing import Callable, Optional

SCHEMA = "R493-exact-binary128-to-binary64-protocol-projection-v1"
ROUNDING = "nearest-ties-to-even-on-the-complete-exact-dyadic-value"
SOURCE_SCOPE = "independent-projection-only-not-a-live-response-or-native-solver"

FRAC128 = (1 << 112) - 1
SIGN64 = 1 << 63
EXP64_ALL = 0x7FF << 52
HEX_DYADIC = re.compile(r"^([+-]?)0x([0-9a-fA-F]+)(?:\.([0-9a-fA-F]*))?p([+-]?[0-9]+)$")


class ProjectionInputError(ValueError):
    """A real source/format/complete-word error, not a scientific acceptance."""


class NonfiniteProjection(ValueError):
    """The original finite-value requirement failed at this actual word."""

    def __init__(self, location: dict, reason: str):
        super().__init__(reason)
        self.location = dict(location)
        self.reason = reason


def require_public_actions() -> None:
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise ProjectionInputError("Actual scientific word projection runs only in the public Actions job")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def checked_input(descriptor: dict, *, runner: Path) -> Path:
    if not isinstance(descriptor, dict):
        raise ProjectionInputError("A complete actual file descriptor is required")
    if type(descriptor.get("bytes")) is not int or descriptor["bytes"] < 0:
        raise ProjectionInputError("Actual byte count is required")
    digest = descriptor.get("sha256")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ProjectionInputError("Actual SHA-256 is required")
    supplied = Path(descriptor["file"])
    if not supplied.is_absolute():
        raise ProjectionInputError("The new caller supplies a real absolute same-job file path")
    if supplied.is_symlink():
        raise ProjectionInputError("A live numeric input is not a symlink")
    path = supplied.resolve(strict=True)
    if path == runner or not path.is_relative_to(runner) or not path.is_file():
        raise ProjectionInputError("A live numeric input must be a file below actual RUNNER_TEMP")
    if path.stat().st_size != descriptor["bytes"]:
        raise ProjectionInputError("Actual live numeric input length differs")
    return path


def _nearest_even_integer(magnitude: int, exponent: int, quantum: int) -> int:
    """Return RN_even(magnitude * 2**exponent / 2**quantum), exactly."""
    shift = exponent - quantum
    if shift >= 0:
        return magnitude << shift
    removed = -shift
    integer = magnitude >> removed
    remainder = magnitude - (integer << removed)
    halfway = 1 << (removed - 1)
    return integer + int(remainder > halfway or (remainder == halfway and (integer & 1) != 0))


def dyadic_binary64_word(sign: int, magnitude: int, exponent: int) -> int:
    """Project one finite exact dyadic to IEEE binary64, including overflow.

    sign is 0/1, magnitude is a nonnegative integer. The exact value is
    (-1)**sign * magnitude * 2**exponent. The integer result is the complete
    binary64 word; infinity from overflow is returned, not saturated.
    """
    if type(sign) is not int or sign not in (0, 1):
        raise ProjectionInputError("A real sign bit is required")
    if type(magnitude) is not int or magnitude < 0 or type(exponent) is not int:
        raise ProjectionInputError("An exact nonnegative integer dyadic is required")
    sign_word = SIGN64 if sign else 0
    if magnitude == 0:
        return sign_word
    high = magnitude.bit_length() - 1 + exponent
    if high > 1023:
        return sign_word | EXP64_ALL
    if high < -1022:
        integer = _nearest_even_integer(magnitude, exponent, -1074)
        # integer == 2**52 is the legitimate carry to minimum normal.
        if integer > (1 << 52):
            raise ProjectionInputError("Internal subnormal carry exceeds the exact rounding range")
        return sign_word | integer
    integer = _nearest_even_integer(magnitude, exponent, high - 52)
    if integer == (1 << 53):
        integer >>= 1
        high += 1
    if high > 1023:
        return sign_word | EXP64_ALL
    if not (1 << 52) <= integer < (1 << 53):
        raise ProjectionInputError("Internal normal significand is outside the exact rounding range")
    return sign_word | ((high + 1023) << 52) | (integer - (1 << 52))


def binary128_word_to_binary64_word(word: int) -> int:
    """Project the complete little-endian IEEE binary128 word as an integer.

    Input infinities and NaNs are not assigned a finite replacement.
    Accurate zero retains its sign; a negative nonzero value rounding to zero
    also retains its sign. The implementation never uses a float to choose
    an exponent, significand, tie, or carry.
    """
    if type(word) is not int or not 0 <= word < (1 << 128):
        raise ProjectionInputError("Exactly one unsigned 128-bit word is required")
    sign = word >> 127
    exponent_field = (word >> 112) & 0x7FFF
    fraction = word & FRAC128
    if exponent_field == 0x7FFF:
        raise NonfiniteProjection(
            {"binary128_hex_word": format(word, "032x")},
            "The actual binary128 producer word is nonfinite")
    if exponent_field == 0:
        return dyadic_binary64_word(sign, fraction, -16494)
    return dyadic_binary64_word(sign, (1 << 112) | fraction, exponent_field - 16383 - 112)


def exact_hex_to_binary64_word(text: str) -> int:
    """Project an exact hexadecimal dyadic such as an actual quadmath %Qa.

    This parses an exact dyadic literal. It does not use its adjacent decimal
    report, assume a decimal round trip, or claim that an arbitrary literal
    was produced by a trusted native caller; the assembler must bind that
    actual report and call separately.
    """
    if not isinstance(text, str):
        raise ProjectionInputError("An actual exact hexadecimal literal is required")
    match = HEX_DYADIC.fullmatch(text)
    if match is None:
        raise ProjectionInputError("The actual exact hexadecimal literal is malformed or nonfinite")
    sign_text, integer_hex, fraction_hex, exponent_text = match.groups()
    fraction_hex = fraction_hex or ""
    magnitude = int(integer_hex + fraction_hex, 16)
    exponent = int(exponent_text) - 4 * len(fraction_hex)
    return dyadic_binary64_word(int(sign_text == "-"), magnitude, exponent)


def binary64_float(word: int) -> float:
    """Install the already chosen complete binary64 word, without arithmetic."""
    if type(word) is not int or not 0 <= word < (1 << 64):
        raise ProjectionInputError("Exactly one unsigned 64-bit word is required")
    return struct.unpack("<d", word.to_bytes(8, "little"))[0]


def is_finite_word(word: int) -> bool:
    return ((word >> 52) & 0x7FF) != 0x7FF


def new_projection_record(label: str, count: int) -> dict:
    if not isinstance(label, str) or not label or type(count) is not int or count < 0:
        raise ProjectionInputError("Actual field label and full element count are required")
    return {
        "schema": SCHEMA,
        "field": label,
        "expected_words": count,
        "completed_words": 0,
        "complete": False,
        "rounding": ROUNDING,
        "source_scope": SOURCE_SCOPE,
        "raw_binary128_byte_order": "little",
        "binary128_significand_bits": 113,
        "binary64_significand_bits": 53,
        "input_zero_words": 0,
        "input_negative_zero_words": 0,
        "input_subnormal_nonzero_words": 0,
        "output_negative_zero_words": 0,
        "nonzero_to_zero_words": 0,
        "output_subnormal_nonzero_words": 0,
        "output_nonfinite_words": 0,
        "first_unprojected_index": 0,
        "error": None,
        "no_decimal_intermediate": True,
        "no_native_or_fullDN_acceptance_conferred": True,
        "complete_original_finite_checks_still_required": True,
    }


def _account(record: dict, input_word: int, output_word: int) -> None:
    input_fraction = input_word & FRAC128
    input_exponent = (input_word >> 112) & 0x7FFF
    zero = input_exponent == 0 and input_fraction == 0
    if zero:
        record["input_zero_words"] += 1
        if input_word >> 127:
            record["input_negative_zero_words"] += 1
    elif input_exponent == 0:
        record["input_subnormal_nonzero_words"] += 1
    output_exponent = (output_word >> 52) & 0x7FF
    output_fraction = output_word & ((1 << 52) - 1)
    output_zero = output_exponent == 0 and output_fraction == 0
    if output_word == SIGN64:
        record["output_negative_zero_words"] += 1
    if output_zero and not zero:
        record["nonzero_to_zero_words"] += 1
    if output_exponent == 0 and output_fraction != 0:
        record["output_subnormal_nonzero_words"] += 1
    if output_exponent == 0x7FF:
        record["output_nonfinite_words"] += 1


def project_actual_array(descriptor: dict, *, label: str, shape: tuple[int, ...],
                         record: dict, check_resource: Optional[Callable[[], None]] = None) -> list[float]:
    """Read and project a complete actual same-job f128 array.

    The caller owns record from new_projection_record(). On any exception it
    retains that record and the original source file. Returned values are an
    internal protocol payload, never a necessary-summary scientific table.
    No file is deleted and no state is replaced by its projection.

    The descriptor SHA is verified on the one complete stream actually read.
    A resource exception leaves first_unprojected_index and the actual partial
    metadata; it never yields a complete shortened array.
    """
    require_public_actions()
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    if not isinstance(shape, tuple) or not shape or any(type(x) is not int or x < 0 for x in shape):
        raise ProjectionInputError("Explicit full array dimensions are required")
    count = 1
    for size in shape:
        count *= size
    if record.get("schema") != SCHEMA or record.get("field") != label or record.get("expected_words") != count:
        raise ProjectionInputError("The actual field projection record does not match its full shape")
    if record.get("completed_words") != 0 or record.get("complete") is not False:
        raise ProjectionInputError("Each actual input array is projected into one fresh record")
    path = checked_input(descriptor, runner=runner)
    if descriptor["bytes"] != 16 * count:
        raise ProjectionInputError("The complete f128 array length differs from the explicit shape")
    record["input"] = dict(descriptor)
    record["shape"] = list(shape)
    actual_sha = hashlib.sha256()
    projected_sha = hashlib.sha256()
    values: list[float] = []
    try:
        with path.open("rb") as stream:
            while len(values) < count:
                if check_resource is not None:
                    check_resource()
                expected = min(4096, count - len(values)) * 16
                block = stream.read(expected)
                if len(block) != expected:
                    raise ProjectionInputError("The live binary128 array ended before the full requested words")
                actual_sha.update(block)
                for offset in range(0, len(block), 16):
                    index = len(values)
                    input_word = int.from_bytes(block[offset:offset + 16], "little")
                    try:
                        output_word = binary128_word_to_binary64_word(input_word)
                    except NonfiniteProjection as error:
                        error.location.update(field=label, index=index, shape=list(shape), input=dict(descriptor))
                        raise
                    _account(record, input_word, output_word)
                    if not is_finite_word(output_word):
                        raise NonfiniteProjection({
                            "field": label, "index": index, "shape": list(shape),
                            "input": dict(descriptor), "binary128_hex_word": format(input_word, "032x"),
                            "projected_binary64_hex_word": format(output_word, "016x"),
                        }, "The actual once-rounded protocol value is nonfinite")
                    packed = output_word.to_bytes(8, "little")
                    projected_sha.update(packed)
                    values.append(struct.unpack("<d", packed)[0])
                    record["completed_words"] = len(values)
                    record["first_unprojected_index"] = len(values)
            if stream.read(1):
                raise ProjectionInputError("The live binary128 array contains unexpected additional words")
        digest = actual_sha.hexdigest()
        record["actual_input_sha256"] = digest
        if digest != descriptor["sha256"]:
            raise ProjectionInputError("The actual streamed binary128 input SHA differs")
        record["projected_binary64le_bytes"] = 8 * count
        record["projected_binary64le_sha256"] = projected_sha.hexdigest()
        record["complete"] = True
        record["first_unprojected_index"] = None
        return values
    except BaseException as error:
        record["error"] = {
            "type": type(error).__name__, "message": str(error),
            "location": getattr(error, "location", None),
        }
        # The owning caller retains the actual failure and raw source, then
        # follows its original quiet/readback/cleanup rule. Nothing is retried.
        raise


def project_actual_hex_scalar(text: str, *, label: str) -> tuple[float, dict]:
    """Project one already source-bound exact scalar word, with a small receipt."""
    require_public_actions()
    word = exact_hex_to_binary64_word(text)
    record = {
        "schema": SCHEMA, "field": label, "actual_exact_hexadecimal_literal": text,
        "projected_binary64_hex_word": format(word, "016x"), "rounding": ROUNDING,
        "no_decimal_intermediate": True, "no_native_or_fullDN_acceptance_conferred": True,
    }
    if not is_finite_word(word):
        raise NonfiniteProjection(record, "The actual once-rounded scalar protocol value is nonfinite")
    return binary64_float(word), record


def project_actual_array_file(descriptor: dict, *, label: str, shape: tuple[int, ...],
                              output: Path, record: dict,
                              check_resource: Optional[Callable[[], None]] = None) -> dict:
    """The same integer projection, streamed to an actual same-job f64 file.

    This is used only for the already required full stage maps retained by the
    original optional warm predictor. It does not put those arrays into the
    protocol JSON or necessary summary, and it does not alter any original
    binary128 file. A partial output is retained and explicitly remains partial.
    """
    require_public_actions()
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    if not isinstance(shape, tuple) or not shape or any(type(x) is not int or x < 0 for x in shape):
        raise ProjectionInputError("Explicit full array dimensions are required")
    count = 1
    for size in shape:
        count *= size
    if (record.get("schema") != SCHEMA or record.get("field") != label
            or record.get("expected_words") != count
            or record.get("completed_words") != 0 or record.get("complete") is not False):
        raise ProjectionInputError("One fresh record for the actual complete array is required")
    source = checked_input(descriptor, runner=runner)
    output = Path(output).resolve()
    if not output.is_relative_to(runner) or output == runner or output.exists():
        raise ProjectionInputError("A fresh same-job temporary projection file is required")
    if descriptor["bytes"] != 16 * count:
        raise ProjectionInputError("Complete binary128 input byte count differs")
    output.parent.mkdir(parents=True, exist_ok=True)
    record.update(input=dict(descriptor), shape=list(shape), output_file=str(output))
    original_sha, projected_sha = hashlib.sha256(), hashlib.sha256()
    try:
        with source.open("rb") as src, output.open("xb") as dst:
            while record["completed_words"] < count:
                if check_resource is not None:
                    check_resource()
                n = min(4096, count-record["completed_words"])
                block = src.read(16*n)
                if len(block) != 16*n:
                    raise ProjectionInputError("Actual binary128 source ended before every word")
                original_sha.update(block)
                projected = bytearray()
                for offset in range(0, len(block), 16):
                    index = record["completed_words"]
                    input_word = int.from_bytes(block[offset:offset+16], "little")
                    try:
                        output_word = binary128_word_to_binary64_word(input_word)
                    except NonfiniteProjection as error:
                        error.location.update(field=label, index=index, shape=list(shape),
                                              input=dict(descriptor))
                        raise
                    _account(record, input_word, output_word)
                    if not is_finite_word(output_word):
                        raise NonfiniteProjection({
                            "field": label, "index": index, "shape": list(shape),
                            "input": dict(descriptor),
                            "binary128_hex_word": format(input_word, "032x"),
                            "projected_binary64_hex_word": format(output_word, "016x"),
                        }, "The original finite stage-predictor input is nonfinite")
                    projected.extend(output_word.to_bytes(8, "little"))
                    record["completed_words"] += 1
                    record["first_unprojected_index"] = record["completed_words"]
                dst.write(projected)
                projected_sha.update(projected)
            if src.read(1):
                raise ProjectionInputError("Unexpected additional binary128 words")
            dst.flush()
        record["actual_input_sha256"] = original_sha.hexdigest()
        if record["actual_input_sha256"] != descriptor["sha256"]:
            raise ProjectionInputError("The actual complete source changed during projection")
        record.update(complete=True, first_unprojected_index=None,
                      projected_binary64le_bytes=8*count,
                      projected_binary64le_sha256=projected_sha.hexdigest())
        return dict(file=str(output), bytes=8*count, sha256=projected_sha.hexdigest(),
                    shape=list(shape), dtype="<f8", order="C")
    except BaseException as error:
        record["error"] = dict(type=type(error).__name__, message=str(error),
                              location=getattr(error, "location", None))
        record["actual_partial_output_bytes"] = output.stat().st_size if output.is_file() else 0
        raise
