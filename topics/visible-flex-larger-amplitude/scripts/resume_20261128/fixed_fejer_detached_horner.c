/* The scalar polynomial from the complete working Rodrigues coefficient definitions.
   The caller supplies the actual CPython-rounded coefficient words and Torch output buffers. */
#include <stddef.h>
#include <float.h>
#include <fenv.h>
#include <xmmintrin.h>

#if defined(__FAST_MATH__) || FLT_EVAL_METHOD != 0 || DBL_MANT_DIG != 53 || DBL_MAX_EXP != 1024
#error "The original binary64 recurrence requires separate double-precision operations"
#endif

int fixed_fejer_rounding(void) { return fegetround(); }
unsigned int fixed_fejer_mxcsr(void) { return _mm_getcsr(); }

void fixed_fejer_horner(size_t count, int derivative, const double *restrict z,
                       const double *restrict coefficient, double *restrict out)
{
    int slots = 2 * (derivative + 1);
    for (int slot = 0; slot < slots; ++slot) {
        const double *row = coefficient + 13 * slot;
        double *dest = out + (size_t) slot * count;
        for (size_t index = 0; index < count; ++index) {
            double value = 0.0;
            double coordinate = z[index];
            for (int power = 12; power >= slot/2; --power) {
                double product = value * coordinate;
                value = product + row[power];
            }
            dest[index] = value;
        }
    }
}
