#!/usr/bin/env python3
"""One fixed positive-weight audit, p=227 and auxiliary modulus 65537.

All arithmetic runs only in the public Actions job.  This is not a search
over target primes or a p-adic unit assertion.  It reads the entire
canonical D_- coefficient at n=p^2-3 and S coefficient at n+2.

Source formulas: original-psi4-canonical-positive-slot-and-degree102-negative-source.md
(8), (21), (27), (29).  No stored coefficient array is consumed or emitted.
"""
import ctypes
import hashlib
import json
import math
import pathlib
import subprocess
import tempfile
import time
from flint import nmod_poly

TARGET_P = 227
AUX_ELL = 65537
NATIVE = r"""
#include <stdint.h>
static int64_t power(int64_t a, int64_t n, int64_t q) {
    int64_t r = 1;
    while(n) {
        if(n & 1) r = r*a % q;
        a = a*a % q;
        n >>= 1;
    }
    return r;
}
int wp_coefficients(int64_t *a, int n, int64_t q) {
    if(n < 2) return 1;
    a[0] = 1;
    a[1] = (q-power(7,q-2,q)) % q;
    for(int m=2; m<n; ++m) {
        int64_t acc=0;
        for(int i=1; i<m; ++i) acc += a[i]*a[m-i];
        int64_t den = (((int64_t)6*m-2)*((int64_t)6*m-3)-12) % q;
        if(den == 0) return 2;
        a[m] = ((6*(acc % q)) % q)*power(den,q-2,q) % q;
    }
    return 0;
}
int exp_coefficients(const int64_t *b, int64_t *e, int n, int64_t q) {
    e[0]=1;
    for(int m=1; m<n; ++m) {
        int64_t acc=0;
        for(int j=1; j<=m; ++j) acc += b[j]*e[m-j];
        if(m % q == 0) return 3;
        e[m]=(acc % q)*power(m,q-2,q) % q;
    }
    return 0;
}
"""

def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))

def polynomial_digest(poly, length):
    raw = json.dumps([int(poly[i]) for i in range(length)], separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def exact_r102_coefficients():
    # Coefficients are indexed by x^(1+3j).
    # In the two full Weyl words every odd power of y cancels.
    # delta^(34-2l)=(-3)^(17-l), and y^(2l)=(x^3+1)^l.
    out = [0]*17
    for a, r in zip((1,4,7,10,13,16), (256,1376,1216,58,-37,1)):
        for l in range((34-a)//2+1):
            signed = 0
            for i in range(a+1):
                j=2*l-i
                if 0 <= j <= 34-2*a:
                    signed += (-1)**i * math.comb(a,i)*math.comb(34-2*a,j)
            scale=r*(2**(a+1))*(-1)**a*((-3)**(17-l))*signed
            for v in range(l+1):
                index=(a-1)//3+v
                assert 0 <= index < 17
                out[index] += scale*math.comb(l,v)
    assert out[16] == 301056
    return out

def main():
    start=time.monotonic()
    p, ell=TARGET_P, AUX_ELL
    assert prime(p) and p > 211 and p % 6 == 5 and p not in (2,3,7,17)
    assert prime(ell)
    n=p*p-3
    positive=n+2
    assert (n-4) % 6 == 0 and (positive-6) % 6 == 0
    index=(n-4)//6
    assert index == (positive-6)//6
    precision=index+1
    # Every rational recurrence/integration denominator is an ell-unit.
    assert 6*(precision-1)+1 < ell and 301056 % ell and 7 % ell
    # The native accumulation bound is below signed 64-bit overflow.
    assert precision*(ell-1)**2 < 2**63
    Array=ctypes.c_int64*precision
    xarr=Array()
    with tempfile.TemporaryDirectory(prefix="rank2-p227-exact-") as temporary:
        folder=pathlib.Path(temporary)
        src=folder/"recurrences.c"
        lib=folder/"recurrences.so"
        src.write_text(NATIVE)
        subprocess.run(["cc","-O3","-std=c11","-shared","-fPIC",str(src),"-o",str(lib)],
                       check=True,capture_output=True)
        native=ctypes.CDLL(str(lib))
        native.wp_coefficients.argtypes=[ctypes.POINTER(ctypes.c_int64),ctypes.c_int,ctypes.c_int64]
        native.exp_coefficients.argtypes=[ctypes.POINTER(ctypes.c_int64),ctypes.POINTER(ctypes.c_int64),ctypes.c_int,ctypes.c_int64]
        assert native.wp_coefficients(xarr,precision,ell) == 0
        x=nmod_poly(list(xarr),ell)
        q=nmod_poly([0,1],ell)
        zder=(-2*x+6*q*x.derivative()).truncate(precision)
        # Full first-order elliptic identity, independent of the second-order recurrence.
        assert (zder.mul_low(zder,precision)-4*x.pow_trunc(3,precision)-4*q).truncate(precision).is_zero()
        log_sigma=[0]+[
            (-int(xarr[m])*pow(((6*m-1)*(6*m)) % ell,-1,ell)) % ell
            for m in range(1,precision)
        ]
        logs=nmod_poly(log_sigma,ell)
        exponentials={}
        for charge in (34,102):
            derivative_coefficients=Array(*[
                (charge*m*log_sigma[m]) % ell for m in range(precision)
            ])
            earr=Array()
            assert native.exp_coefficients(derivative_coefficients,earr,precision,ell) == 0
            es=nmod_poly(list(earr),ell)
            # Full differential identity of exp(charge log(sigma/z)).
            assert (es.derivative()-charge*logs.derivative().mul_low(es,precision-1)).truncate(precision-1).is_zero()
            assert int(es[0]) == 1
            exponentials[charge]=es

        # Canonical positive source x^2 (X+1)(X-8)(7X^2-4X+16)/7.
        rpos=((q+1)*(q-8)*(7*q*q-4*q+16))*pow(7,-1,ell)
        positive_core=nmod_poly([],ell)
        for j in range(5):
            positive_core += (x.pow_trunc(2+3*j,precision)*int(rpos[j])).left_shift(4-j)
        positive_core=positive_core.truncate(precision)
        source_s=exponentials[34].mul_low(positive_core,precision)

        # Entire degree102 negative source; retain all 17 reduced coefficients.
        r102=exact_r102_coefficients()
        negative_core=nmod_poly([],ell)
        for j in range(17):
            negative_core += (x.pow_trunc(1+3*j,precision)*(r102[j] % ell)).left_shift(16-j)
        negative_core=negative_core.truncate(precision)*pow(301056,-1,ell)
        source_d=exponentials[102].mul_low(negative_core,precision)
        assert int(source_s[0]) == 1 and int(source_d[0]) == 1
        d_value, s_value=int(source_d[index]), int(source_s[index])
        report={
            "audit":"original-psi4-one-fixed-positive-weight",
            "target_prime":p,"positive_integer_parameter":1,
            "negative_taylor_index":n,"positive_taylor_index":positive,
            "auxiliary_modulus":ell,"auxiliary_modulus_is_target_prime":False,
            "q_variable":"z^6","q_index":index,"q_precision":precision,
            "negative_coefficient_mod_aux":d_value,
            "positive_coefficient_mod_aux":s_value,
            "nonzero_characteristic_zero_pair_certified":bool(d_value and s_value),
            "full_elliptic_identity":"PASS",
            "both_full_exponential_differential_identities":"PASS",
            "two_first_source_coefficients":[int(source_d[0]),int(source_s[0])],
            "negative_degree102_polynomial_sha256":hashlib.sha256(
                json.dumps(r102,separators=(",",":")).encode()).hexdigest(),
            "full_negative_prefix_sha256":polynomial_digest(source_d,precision),
            "full_positive_prefix_sha256":polynomial_digest(source_s,precision),
            "native_source_sha256":hashlib.sha256(NATIVE.encode()).hexdigest(),
            "script_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            "elapsed_seconds":round(time.monotonic()-start,3),
            "persisted_outputs":False,
            "scope":"Single positive-weight characteristic-zero nonvanishing audit only; no p-adic unit, augmentation, infinite-prime or Sha claim."
        }
        print(json.dumps(report,sort_keys=True))

if __name__ == "__main__":
    main()
