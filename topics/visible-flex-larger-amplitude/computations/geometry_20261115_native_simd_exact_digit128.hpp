// R414: SIMD exact signed-20-bit partial reductions for the complete R405 dot.
// This independent header includes, and does not edit, the frozen R405 kernel:
// geometry_20261115_native_exact_digit128.hpp
// 18871 bytes; SHA256 5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc.
// Runtime AVX2 selection only changes exact integer reduction order. All stored
// significand/exponent bits, packing limits, wide arithmetic and RN113 stay in
// R405. No claim of equivalence to the old sequential binary128 dot graph.
#ifndef VISIBLE_NATIVE_SIMD_EXACT_DIGIT128_HPP
#define VISIBLE_NATIVE_SIMD_EXACT_DIGIT128_HPP

#include "geometry_20261115_native_exact_digit128.hpp"

#if (defined(__x86_64__) || defined(__i386__)) && defined(__GNUC__) && \
    !defined(__clang__) && __GNUC__ >= 5
#include <immintrin.h>
#define VISIBLE_R414_GNU_X86_AVX2 1
#else
#define VISIBLE_R414_GNU_X86_AVX2 0
#endif

namespace exact_digit_simd128 {
using Q=exact_digit128::Q;
using Poll=exact_digit128::Poll;
using VectorView=exact_digit128::VectorView;
using PackedVector=exact_digit128::PackedVector;
using exact_digit128::prepare;
using exact_digit128::encode;
using exact_digit128::checked_product;
using exact_digit128::poll_if;
constexpr unsigned DIGIT_BITS=exact_digit128::DIGIT_BITS;
constexpr size_t REDUCTION_BLOCK=exact_digit128::REDUCTION_BLOCK;
constexpr size_t FAST_LIMB_LIMIT=exact_digit128::FAST_LIMB_LIMIT;
constexpr size_t PACKING_BYTES_LIMIT=exact_digit128::PACKING_BYTES_LIMIT;
static_assert(DIGIT_BITS==20,"R414 partial reduction is for the original 20-bit digits");
static_assert(REDUCTION_BLOCK==2048,"R414 keeps the original complete block bound");
static_assert(FAST_LIMB_LIMIT==12,"R414 keeps the original exponent-span fallback");

enum class Backend : unsigned char { scalar=0,gnu_x86_avx2=1 };
inline const char *backend_name(Backend b){
  return b==Backend::gnu_x86_avx2?"gnu-x86-avx2-signed-even-and-odd":
    "complete-scalar-signed-int64";
}
struct Stats : exact_digit128::Stats {
  uint64_t scalar_digit_blocks=0,avx2_digit_blocks=0,
    avx2_complete_octets=0,avx2_even_products=0,avx2_odd_products=0,
    scalar_backend_products=0,avx2_scalar_tail_products=0,
    delegated_zero_calls=0,delegated_wide_calls=0;
  size_t largest_digit_block=0;
  void join(const Stats &s){
    exact_digit128::Stats::join(s);
#define R414_ADD(name) name+=s.name
    R414_ADD(scalar_digit_blocks);R414_ADD(avx2_digit_blocks);
    R414_ADD(avx2_complete_octets);R414_ADD(avx2_even_products);
    R414_ADD(avx2_odd_products);R414_ADD(scalar_backend_products);
    R414_ADD(avx2_scalar_tail_products);R414_ADD(delegated_zero_calls);
    R414_ADD(delegated_wide_calls);
#undef R414_ADD
    largest_digit_block=std::max(largest_digit_block,s.largest_digit_block);
  }
};

namespace detail {
// Private reducer contract: 0 <= count <= 2048; every input digit is one
// produced by the unchanged R405 prepare, hence |digit| <= 2^20-1.
// Each product is formed after signed widening. Every subset absolute sum
// is <= 2048*(2^20-1)^2 < 2^51, including horizontal and tail reductions.
inline int64_t scalar_partial(const int32_t *a,const int32_t *b,size_t count){
  int64_t out=0;
  for(size_t i=0;i<count;++i)out+=int64_t(a[i])*int64_t(b[i]);
  return out;
}

#if VISIBLE_R414_GNU_X86_AVX2
// Only this function may contain AVX2 instructions. The translation unit
// must retain the original baseline target (no global -mavx2/-march=native).
// noinline separates the feature-specific body from runtime dispatch.
__attribute__((target("avx2"),noinline))
inline int64_t avx2_partial(const int32_t *a,const int32_t *b,size_t count){
  __m256i even=_mm256_setzero_si256(),odd=_mm256_setzero_si256();
  size_t i=0;
  for(;count-i>=8;i+=8){
    __m256i av,bv;
    // memcpy expresses an unaligned, alias-safe load of exactly eight
    // int32 words; the loop condition forbids reading past either input.
    std::memcpy(&av,a+i,sizeof(av));std::memcpy(&bv,b+i,sizeof(bv));
    even=_mm256_add_epi64(even,_mm256_mul_epi32(av,bv));
    // Within each 64-bit lane this moves the original odd int32 bit
    // pattern to its low half. mul_epi32 interprets that low half as
    // SIGNED int32, including negative odd inputs; no unsigned multiply.
    const __m256i ao=_mm256_srli_epi64(av,32),bo=_mm256_srli_epi64(bv,32);
    odd=_mm256_add_epi64(odd,_mm256_mul_epi32(ao,bo));
  }
  int64_t ev[4],od[4];
  std::memcpy(ev,&even,sizeof(even));std::memcpy(od,&odd,sizeof(odd));
  int64_t out=0;
  for(unsigned lane=0;lane<4;++lane){out+=ev[lane];out+=od[lane];}
  for(;i<count;++i)out+=int64_t(a[i])*int64_t(b[i]);
  return out;
}
#endif

using Partial=int64_t(*)(const int32_t*,const int32_t*,size_t);
struct Dispatch { Backend backend;Partial partial; };
inline const Dispatch &dispatch(){
  // Ordinary runtime use, not an ifunc resolver or pre-runtime constructor.
  // Function-local initialization is thread-safe; compiler feature detection
  // selects a usable compiled backend. No measurement or science criterion.
  static const Dispatch selected=[](){
#if VISIBLE_R414_GNU_X86_AVX2
    __builtin_cpu_init();
    if(__builtin_cpu_supports("avx2"))
      return Dispatch{Backend::gnu_x86_avx2,&avx2_partial};
#endif
    return Dispatch{Backend::scalar,&scalar_partial};
  }();
  return selected;
}
} // namespace detail

inline Backend selected_backend(){return detail::dispatch().backend;}
inline const char *selected_backend_name(){return backend_name(selected_backend());}
inline bool avx2_body_compiled(){return VISIBLE_R414_GNU_X86_AVX2!=0;}

inline Q dot(const PackedVector &a,const PackedVector &b,Stats &stats,Poll poll=nullptr){
  if(a.length()!=b.length())throw std::runtime_error("exact-digit128-dot-shape");
  // Delegate complete zero/wide cases without changing any of their exact
  // exponent, sign, carry, quantization, nonfinite or resource semantics.
  if(a.zero||b.zero){
    ++stats.delegated_zero_calls;
    return exact_digit128::dot(a,b,static_cast<exact_digit128::Stats&>(stats),poll);
  }
  if(!a.packed||!b.packed){
    ++stats.delegated_wide_calls;
    return exact_digit128::dot(a,b,static_cast<exact_digit128::Stats&>(stats),poll);
  }
  ++stats.exact_dot_calls;++stats.packed_dot_calls;
  const size_t k=a.length();
  exact_digit128::ExactSum sum(a.base+b.base);
  const detail::Dispatch &dispatch=detail::dispatch();
  for(size_t la=0;la<a.layers;++la)if(a.active[la])
    for(size_t lb=0;lb<b.layers;++lb)if(b.active[lb]){
      const int32_t *av=a.plane(la),*bv=b.plane(lb);
      for(size_t start=0;start<k;){
        poll_if(poll);
        const size_t count=std::min(REDUCTION_BLOCK,k-start);
        const int64_t partial=dispatch.partial(av+start,bv+start,count);
        stats.digit_products+=count;++stats.integer_partial_sums;
        stats.largest_digit_block=std::max(stats.largest_digit_block,count);
        if(dispatch.backend==Backend::gnu_x86_avx2){
          ++stats.avx2_digit_blocks;
          const size_t octets=count/8;
          stats.avx2_complete_octets+=octets;
          stats.avx2_even_products+=4*octets;
          stats.avx2_odd_products+=4*octets;
          stats.avx2_scalar_tail_products+=count%8;
        }else{
          ++stats.scalar_digit_blocks;stats.scalar_backend_products+=count;
        }
        // Original limb-pair order, block partition and shift remain exact.
        sum.add_signed(partial,static_cast<unsigned>(DIGIT_BITS*(la+lb)));
        start+=count;
      }
    }
  return sum.rounded(static_cast<exact_digit128::Stats&>(stats));
}
inline Q dot(VectorView a,VectorView b,Stats &stats,Poll poll=nullptr){
  size_t budget=PACKING_BYTES_LIMIT;
  const PackedVector pa=prepare(a,budget,stats,poll),pb=prepare(b,budget,stats,poll);
  return exact_digit_simd128::dot(pa,pb,stats,poll);
}
inline std::vector<Q> multiply(const Q *a,const Q *b,size_t m,size_t k,size_t n,
    Stats &stats,Poll poll=nullptr){
  // Same full row-major coverage and packing allocation as R405. This is
  // a complete matrix product, not a selected-column or low-rank kernel.
  const size_t ac=checked_product(m,k),bc=checked_product(k,n),
    oc=checked_product(m,n);
  if((ac&&!a)||(bc&&!b))throw std::runtime_error("exact-digit128-null-matrix");
  std::vector<Q> out(oc,encode(false,0,0));
  if(!m||!n||!k)return out;
  std::vector<PackedVector> columns;columns.reserve(n);
  const size_t row_need=checked_product(checked_product(FAST_LIMB_LIMIT,k),sizeof(int32_t));
  const size_t row_reserve=std::min(row_need,PACKING_BYTES_LIMIT);
  size_t column_budget=PACKING_BYTES_LIMIT-row_reserve;
  for(size_t j=0;j<n;++j){
    poll_if(poll);columns.push_back(prepare({b+j,k,n},column_budget,stats,poll));
  }
  for(size_t i=0;i<m;++i){
    poll_if(poll);size_t row_budget=row_reserve;
    const PackedVector row=prepare({a+i*k,k,1},row_budget,stats,poll);
    for(size_t j=0;j<n;++j)
      out[i*n+j]=exact_digit_simd128::dot(row,columns[j],stats,poll);
  }
  return out;
}
} // namespace exact_digit_simd128
#undef VISIBLE_R414_GNU_X86_AVX2
#endif
