// R522: complete two-output dyadic dots with one shared left-plane load.
// The R405/R414 decoder, packing budget, wide fallback, ExactSum and RN113
// remain original. This is a source-only implementation, not a timing result.
#ifndef VISIBLE_NATIVE_PAIRED_EXACT_DIGIT128_HPP
#define VISIBLE_NATIVE_PAIRED_EXACT_DIGIT128_HPP
#include "geometry_20261115_native_simd_exact_digit128.hpp"
#include <array>

#if (defined(__x86_64__) || defined(__i386__)) && defined(__GNUC__) && \
    !defined(__clang__) && __GNUC__ >= 5
#include <immintrin.h>
#define VISIBLE_R522_GNU_X86_AVX2 1
#else
#define VISIBLE_R522_GNU_X86_AVX2 0
#endif

namespace paired_digit128 {
using Q=exact_digit_simd128::Q;
using Poll=exact_digit_simd128::Poll;
using VectorView=exact_digit_simd128::VectorView;
using PackedVector=exact_digit_simd128::PackedVector;
using Stats=exact_digit_simd128::Stats;
using Backend=exact_digit_simd128::Backend;
using exact_digit_simd128::checked_product;
using exact_digit_simd128::prepare;
using exact_digit_simd128::encode;
using exact_digit_simd128::poll_if;
constexpr unsigned DIGIT_BITS=exact_digit_simd128::DIGIT_BITS;
constexpr size_t REDUCTION_BLOCK=exact_digit_simd128::REDUCTION_BLOCK;
constexpr size_t FAST_LIMB_LIMIT=exact_digit_simd128::FAST_LIMB_LIMIT;
constexpr size_t PACKING_BYTES_LIMIT=exact_digit_simd128::PACKING_BYTES_LIMIT;
static_assert(DIGIT_BITS==20 && REDUCTION_BLOCK==2048 && FAST_LIMB_LIMIT==12,
              "R522 retains the original complete digit contract");

namespace detail {
struct PairPartial {int64_t first=0,second=0;};

// Private contract: all three arrays have count <= 2048 original R405
// signed 20-bit digits. Each output separately has absolute sum < 2^51.
// Sharing the read of a[i] introduces no arithmetic between the outputs.
inline PairPartial scalar_pair(const int32_t *a,const int32_t *b,
                               const int32_t *c,size_t count){
  PairPartial out;
  for(size_t i=0;i<count;++i){
    const int64_t av=static_cast<int64_t>(a[i]);
    out.first+=av*static_cast<int64_t>(b[i]);
    out.second+=av*static_cast<int64_t>(c[i]);
  }
  return out;
}

#if VISIBLE_R522_GNU_X86_AVX2
__attribute__((target("avx2"),noinline))
inline PairPartial avx2_pair(const int32_t *a,const int32_t *b,
                            const int32_t *c,size_t count){
  __m256i be=_mm256_setzero_si256(),bo=_mm256_setzero_si256(),
          ce=_mm256_setzero_si256(),co=_mm256_setzero_si256();
  size_t i=0;
  for(;count-i>=8;i+=8){
    __m256i av,bv,cv;
    std::memcpy(&av,a+i,sizeof(av));
    std::memcpy(&bv,b+i,sizeof(bv));
    std::memcpy(&cv,c+i,sizeof(cv));
    // mul_epi32 sign-extends the low int32 word in each 64-bit lane.
    // Logical shifts move the original odd int32 bit patterns to that slot.
    const __m256i ao=_mm256_srli_epi64(av,32),
                  b_odd=_mm256_srli_epi64(bv,32),
                  c_odd=_mm256_srli_epi64(cv,32);
    be=_mm256_add_epi64(be,_mm256_mul_epi32(av,bv));
    bo=_mm256_add_epi64(bo,_mm256_mul_epi32(ao,b_odd));
    ce=_mm256_add_epi64(ce,_mm256_mul_epi32(av,cv));
    co=_mm256_add_epi64(co,_mm256_mul_epi32(ao,c_odd));
  }
  int64_t bev[4],bov[4],cev[4],cov[4];
  std::memcpy(bev,&be,sizeof(be));std::memcpy(bov,&bo,sizeof(bo));
  std::memcpy(cev,&ce,sizeof(ce));std::memcpy(cov,&co,sizeof(co));
  PairPartial out;
  for(unsigned lane=0;lane<4;++lane){
    out.first+=bev[lane];out.first+=bov[lane];
    out.second+=cev[lane];out.second+=cov[lane];
  }
  for(;i<count;++i){
    const int64_t av=static_cast<int64_t>(a[i]);
    out.first+=av*static_cast<int64_t>(b[i]);
    out.second+=av*static_cast<int64_t>(c[i]);
  }
  return out;
}
#endif

inline PairPartial reduce_pair(const int32_t *a,const int32_t *b,
                               const int32_t *c,size_t count){
#if VISIBLE_R522_GNU_X86_AVX2
  if(exact_digit_simd128::selected_backend()==Backend::gnu_x86_avx2)
    return avx2_pair(a,b,c,count);
#endif
  return scalar_pair(a,b,c,count);
}

inline void count_partial(Stats &stats,size_t count){
  stats.digit_products+=count;++stats.integer_partial_sums;
  stats.largest_digit_block=std::max(stats.largest_digit_block,count);
  if(exact_digit_simd128::selected_backend()==Backend::gnu_x86_avx2){
    ++stats.avx2_digit_blocks;
    const size_t octets=count/8;
    stats.avx2_complete_octets+=octets;
    stats.avx2_even_products+=4*octets;
    stats.avx2_odd_products+=4*octets;
    stats.avx2_scalar_tail_products+=count%8;
  }else{
    ++stats.scalar_digit_blocks;stats.scalar_backend_products+=count;
  }
}
} // namespace detail

// Both complete outputs are returned, or an original error/resource
// exception is propagated. Neither a completed prefix nor a partial sum
// is fabricated as a matrix output.
inline std::array<Q,2> dot_pair(const PackedVector &a,const PackedVector &b,
                              const PackedVector &c,Stats &stats,Poll poll=nullptr){
  if(a.length()!=b.length()||a.length()!=c.length())
    throw std::runtime_error("exact-digit128-dot-shape");
  // When any operand is zero or needs the original wide representation,
  // use the complete old implementation for BOTH dots in original order.
  if(a.zero||b.zero||c.zero||!a.packed||!b.packed||!c.packed)
    return {exact_digit_simd128::dot(a,b,stats,poll),
            exact_digit_simd128::dot(a,c,stats,poll)};
  ++stats.exact_dot_calls;++stats.packed_dot_calls;
  ++stats.exact_dot_calls;++stats.packed_dot_calls;
  exact_digit128::ExactSum first(a.base+b.base),second(a.base+c.base);
  const size_t k=a.length(),right_layers=std::max(b.layers,c.layers);
  const auto &dispatch=exact_digit_simd128::detail::dispatch();
  for(size_t la=0;la<a.layers;++la)if(a.active[la])
    for(size_t lb=0;lb<right_layers;++lb){
      const bool use_b=lb<b.layers&&b.active[lb],
                 use_c=lb<c.layers&&c.active[lb];
      if(!use_b&&!use_c)continue;
      const int32_t *av=a.plane(la),
                    *bv=use_b?b.plane(lb):nullptr,
                    *cv=use_c?c.plane(lb):nullptr;
      for(size_t start=0;start<k;){
        poll_if(poll);
        const size_t count=std::min(REDUCTION_BLOCK,k-start);
        const unsigned shift=static_cast<unsigned>(DIGIT_BITS*(la+lb));
        if(use_b&&use_c){
          const detail::PairPartial both=detail::reduce_pair(av+start,bv+start,cv+start,count);
          detail::count_partial(stats,count);
          first.add_signed(both.first,shift);
          // Same absolute caller clock; no private timer or budget reset.
          // A shared reducer performs at most TWO original 2048-term
          // integer blocks before this next poll.
          poll_if(poll);
          detail::count_partial(stats,count);
          second.add_signed(both.second,shift);
        }else if(use_b){
          const int64_t part=dispatch.partial(av+start,bv+start,count);
          detail::count_partial(stats,count);first.add_signed(part,shift);
        }else{
          const int64_t part=dispatch.partial(av+start,cv+start,count);
          detail::count_partial(stats,count);second.add_signed(part,shift);
        }
        start+=count;
      }
    }
  // Same independent ExactSum, sign handling, exponent and one RN113.
  // Exact cancellation returns +0; negative nonzero underflow retains -0.
  return {first.rounded(static_cast<exact_digit128::Stats&>(stats)),
          second.rounded(static_cast<exact_digit128::Stats&>(stats))};
}

inline std::vector<Q> multiply(const Q *a,const Q *b,size_t m,size_t k,size_t n,
                              Stats &stats,Poll poll=nullptr){
  const size_t ac=checked_product(m,k),bc=checked_product(k,n),
               oc=checked_product(m,n);
  if((ac&&!a)||(bc&&!b))throw std::runtime_error("exact-digit128-null-matrix");
  std::vector<Q> out(oc,encode(false,0,0));
  if(!m||!n||!k)return out;
  // Exactly the original one-row packing reservation and B-column order.
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
    size_t j=0;
    for(;n-j>=2;j+=2){
      const auto both=dot_pair(row,columns[j],columns[j+1],stats,poll);
      out[i*n+j]=both[0];out[i*n+j+1]=both[1];
    }
    if(j<n)out[i*n+j]=exact_digit_simd128::dot(row,columns[j],stats,poll);
  }
  return out;
}
} // namespace paired_digit128
#undef VISIBLE_R522_GNU_X86_AVX2
#endif
