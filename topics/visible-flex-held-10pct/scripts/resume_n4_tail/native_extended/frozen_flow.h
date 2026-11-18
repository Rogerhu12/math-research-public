#ifndef VISIBLE_FLEX_FROZEN_FLOW_H
#define VISIBLE_FLEX_FROZEN_FLOW_H
#include <stdint.h>
#include <stddef.h>

/* ABI1, little-endian x86_64. Scalar mode0 is the exact double/V8 baseline;
   mode1 is native long double. The latter has64 significand bits, not113.
   Point coefficient order: r3,r4,sqrt2,sqrt12,E,w2,pDenominator,targetFactor,
   sigma,fluxPrefactor,qLNumerator,meanFactor,pNumerator[0..M-1]. */
typedef struct VFConfig {
    int32_t abi_version, M, N, spacing, nq, root_iterations, n_halves;
    double floor, tolerance, fallback_tolerance, scale_floor;
    const double *cosine, *sine, *halves;
} VFConfig;

typedef struct VFStep {
    int32_t profile, step, point_a, point_mid, point_end;
    double x, h;
} VFStep;

typedef struct VFStage {
    int32_t nsteps, npoints;
    const VFStep *steps;
    const double *coefficients, *initial42;
} VFStage;

/* Exact-baseline scalar callbacks. The batched callback evaluates only
   sqrt(D) and, when needed, expm1(-1.5*log1p(-u)), using the old V8 bridge.
   Return nonzero on an engineering failure; such a failure cannot be accepted
   as a point-root fallback. Long-double mode does not use these callbacks. */
typedef int (*VFDoubleTrans)(size_t n, const double *D, const double *u,
    int need_jac, double *sqrtD, double *bm_nonlinear, void *user);
typedef int (*VFDoubleSqrt)(double value, double *result, void *user);

/* Trace values are canonical little-endian binary64 (mode0,8 bytes each),
   or the10 significant bytes of x87 extended encoding (mode1). Six storage
   padding bytes are never exported or hashed. Values must be copied during
   the callback. Event codes and fields are documented in the Python harness.
   No trace callback is needed by the whole-evaluate production protocol. */
typedef int (*VFTrace)(int code, const int64_t *integers, size_t nintegers,
    const unsigned char *values, size_t nvalues, int scalar_mode,
    const char *message, void *user);

typedef struct VFCallbacks {
    VFDoubleTrans double_trans;
    VFDoubleSqrt double_sqrt;
    VFTrace trace;
    void *user;
} VFCallbacks;

typedef struct VFDiagnostics {
    uint64_t root_calls, root_updates, root_fallbacks, trace_events;
    double minA, minD, max_root_relative_residual, min_literal_Jacobian_pivot;
    double kernel_seconds;
    uint32_t scalar_bytes;
} VFDiagnostics;

#ifdef __cplusplus
extern "C" {
#endif
/* These functions are declarations until the reviewed harness is authorized.
   Merely compiling the library does not execute any mathematical evaluator. */
int vf_abi_version(void);
int vf_long_double_significand_bits(void);
int vf_runtime_info(char *output, size_t capacity);

/* Output pointers: state64 is size2*M+2. tangent64 is (2*M+2)*(2*M), or null
   when with_jac=0. Optional native buffers use8/10 canonical bytes per scalar.
   Stage inputs/coefficients are read-only. All state and tangent boundary
   conversions to double occur once after a successful complete stage.
   Error -> nonzero; no successful partial state is returned. */
int vf_run_stage(const VFConfig *config, const VFStage *stage,
    int scalar_mode, int with_jac, const VFCallbacks *callbacks,
    double *state64, double *tangent64,
    unsigned char *native_state, unsigned char *native_tangent,
    VFDiagnostics *diagnostics, char *error, size_t error_capacity);
#ifdef __cplusplus
}
#endif
#endif
