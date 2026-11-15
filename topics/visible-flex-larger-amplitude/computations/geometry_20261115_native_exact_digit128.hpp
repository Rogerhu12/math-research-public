// R405: exact finite-binary128 dot products, then one RN113.
// Independent source; no BLAS, Boost, ideal trigonometric identities, or
// truncated fixed-six-limb conversion. This is NOT the old sequential-Q
// reduction graph and is NOT a complete root-derivative error certificate.
#ifndef VISIBLE_NATIVE_EXACT_DIGIT128_HPP
#define VISIBLE_NATIVE_EXACT_DIGIT128_HPP
#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <cstring>
#include <limits>
#include <stdexcept>
#include <vector>

#if !defined(__SIZEOF_INT128__) || __SIZEOF_INT128__ != 16
#error R405 requires the existing GCC unsigned 128-bit integer type
#endif
#if !defined(__BYTE_ORDER__) || __BYTE_ORDER__ != __ORDER_LITTLE_ENDIAN__
#error R405 binary128 word transport requires the original little-endian target
#endif
#if !defined(__FLT128_MANT_DIG__) || __FLT128_MANT_DIG__ != 113
#error R405 requires the original IEEE binary128 format
#endif
#if __FLT128_MIN_EXP__ != -16381 || __FLT128_MAX_EXP__ != 16384
#error R405 requires the original IEEE binary128 exponent range
#endif

namespace exact_digit128 {
using Q=__float128;
using U128=__uint128_t;
using Poll=void(*)();
static_assert(sizeof(Q)==16,"binary128 has sixteen bytes");
static_assert(sizeof(uint64_t)==8 && sizeof(int64_t)==8,"64-bit words");
static_assert(sizeof(uint32_t)==4 && sizeof(int32_t)==4,"32-bit digits");
static_assert(std::numeric_limits<uint64_t>::digits==64,"unsigned 64-bit words");
static_assert(std::numeric_limits<int64_t>::digits==63,"signed 64-bit accumulators");
static_assert(std::numeric_limits<int32_t>::digits==31,"signed 32-bit digits");
static_assert(sizeof(size_t)<=8,"the complete-vector count has at most 64 bits");

constexpr unsigned DIGIT_BITS=20;
constexpr uint32_t DIGIT_MASK=(uint32_t(1)<<DIGIT_BITS)-1;
constexpr size_t REDUCTION_BLOCK=2048;
constexpr size_t FAST_LIMB_LIMIT=12;
constexpr size_t PACKING_BYTES_LIMIT=size_t(64)*1024*1024;
// All finite binary128 products span at most 65,820 bits even after
// summing a size_t-bounded number of terms. This checked allocation ceiling
// is deliberately larger; it never discards an exponent or a carry.
constexpr size_t WIDE_WORD_LIMIT=2048;

struct Stats {
  uint64_t decoded_values=0,zero_input_words=0,negative_zero_input_words=0,
    subnormal_input_words=0,nonfinite_input_failures=0,
    packed_vectors=0,wide_span_vectors=0,packing_budget_vectors=0,
    complete_digit_planes=0,zero_digit_planes=0,
    exact_dot_calls=0,zero_dot_calls=0,packed_dot_calls=0,wide_dot_calls=0,
    complete_scalar_products=0,digit_products=0,integer_partial_sums=0,
    exact_zero_outputs=0,inexact_roundings=0,subnormal_outputs=0,
    rounded_zero_outputs=0,overflow_outputs=0;
  unsigned max_observed_span_bits=0,max_observed_limb_count=0;
  size_t max_positive_words=0,max_negative_words=0;
  void join(const Stats &s){
#define R405_ADD(name) name+=s.name
    R405_ADD(decoded_values);R405_ADD(zero_input_words);
    R405_ADD(negative_zero_input_words);R405_ADD(subnormal_input_words);
    R405_ADD(nonfinite_input_failures);R405_ADD(packed_vectors);
    R405_ADD(wide_span_vectors);R405_ADD(packing_budget_vectors);
    R405_ADD(complete_digit_planes);R405_ADD(zero_digit_planes);
    R405_ADD(exact_dot_calls);R405_ADD(zero_dot_calls);
    R405_ADD(packed_dot_calls);R405_ADD(wide_dot_calls);
    R405_ADD(complete_scalar_products);R405_ADD(digit_products);
    R405_ADD(integer_partial_sums);R405_ADD(exact_zero_outputs);
    R405_ADD(inexact_roundings);R405_ADD(subnormal_outputs);
    R405_ADD(rounded_zero_outputs);R405_ADD(overflow_outputs);
#undef R405_ADD
    max_observed_span_bits=std::max(max_observed_span_bits,s.max_observed_span_bits);
    max_observed_limb_count=std::max(max_observed_limb_count,s.max_observed_limb_count);
    max_positive_words=std::max(max_positive_words,s.max_positive_words);
    max_negative_words=std::max(max_negative_words,s.max_negative_words);
  }
};
inline void poll_if(Poll poll){if(poll)poll();}
inline size_t checked_product(size_t a,size_t b){
  if(a && b>std::numeric_limits<size_t>::max()/a)
    throw std::runtime_error("exact-digit128-size-overflow");
  return a*b;
}
inline unsigned bits64(uint64_t x){
  if(!x)return 0;
  return 64u-static_cast<unsigned>(__builtin_clzll(x));
}
inline unsigned bits128(U128 x){
  const uint64_t hi=static_cast<uint64_t>(x>>64);
  return hi?64u+bits64(hi):bits64(static_cast<uint64_t>(x));
}
struct Word {
  U128 mantissa=0;
  int exponent=0;
  bool negative=false;
};
inline Word decode(Q x,Stats &stats){
  uint64_t words[2];std::memcpy(words,&x,sizeof(x));
  ++stats.decoded_values;
  const unsigned field=static_cast<unsigned>((words[1]>>48)&0x7fffu);
  Word out;
  out.negative=(words[1]>>63)!=0;
  out.mantissa=(U128(words[1]&UINT64_C(0x0000ffffffffffff))<<64)|words[0];
  if(field==0x7fffu){
    ++stats.nonfinite_input_failures;
    throw std::runtime_error("exact-digit128-nonfinite-input");
  }
  if(field){
    out.mantissa|=U128(1)<<112;
    out.exponent=static_cast<int>(field)-16383-112;
  }else{
    out.exponent=-16494;
    if(out.mantissa)++stats.subnormal_input_words;
  }
  if(!out.mantissa){
    ++stats.zero_input_words;
    if(out.negative)++stats.negative_zero_input_words;
    return out;
  }
  // Remove only bits known to be zero in the exact stored significand.
  const uint64_t lo=static_cast<uint64_t>(out.mantissa);
  const unsigned trailing=lo?static_cast<unsigned>(__builtin_ctzll(lo)):
    64u+static_cast<unsigned>(__builtin_ctzll(static_cast<uint64_t>(out.mantissa>>64)));
  out.mantissa>>=trailing;out.exponent+=static_cast<int>(trailing);
  return out;
}
inline Q encode(bool negative,unsigned exponent_field,U128 fraction){
  if(exponent_field>0x7fffu || (fraction>>112)!=0)
    throw std::runtime_error("exact-digit128-encoding-range");
  uint64_t words[2]={static_cast<uint64_t>(fraction),
    static_cast<uint64_t>(fraction>>64)|(uint64_t(exponent_field)<<48)|
      (uint64_t(negative)<<63)};
  Q out;std::memcpy(&out,words,sizeof(out));return out;
}

class Magnitude {
  std::vector<uint64_t> limbs_;
public:
  size_t size()const{return limbs_.size();}
  uint64_t word(size_t i)const{return i<limbs_.size()?limbs_[i]:0;}
  void trim(){while(!limbs_.empty()&&!limbs_.back())limbs_.pop_back();}
  void add_word(size_t i,uint64_t v){
    while(v){
      if(i>=WIDE_WORD_LIMIT)throw std::runtime_error("exact-digit128-wide-carry-range");
      if(i>=limbs_.size())limbs_.resize(i+1,0);
      const U128 sum=U128(limbs_[i])+v;
      limbs_[i]=static_cast<uint64_t>(sum);
      v=static_cast<uint64_t>(sum>>64);++i;
    }
  }
  void add_shifted_word(uint64_t v,unsigned shift){
    if(!v)return;
    const size_t i=shift/64;const unsigned offset=shift%64;
    if(!offset){add_word(i,v);return;}
    add_word(i,v<<offset);
    add_word(i+1,v>>(64-offset));
  }
  void add_shifted_product(const uint64_t product[4],unsigned shift){
    for(unsigned i=0;i<4;++i)
      add_shifted_word(product[i],shift+64u*i);
  }
  int compare(const Magnitude &b)const{
    size_t na=limbs_.size(),nb=b.limbs_.size();
    while(na&&!limbs_[na-1])--na;while(nb&&!b.limbs_[nb-1])--nb;
    if(na!=nb)return na<nb?-1:1;
    for(size_t i=na;i;--i)if(limbs_[i-1]!=b.limbs_[i-1])
      return limbs_[i-1]<b.limbs_[i-1]?-1:1;
    return 0;
  }
  static Magnitude subtract(const Magnitude &a,const Magnitude &b){
    if(a.compare(b)<0)throw std::runtime_error("exact-digit128-negative-magnitude");
    Magnitude out;out.limbs_.resize(a.size(),0);uint64_t borrow=0;
    for(size_t i=0;i<a.size();++i){
      const uint64_t av=a.word(i),bv=b.word(i),t=av-bv;
      const bool first=av<bv,second=t<borrow;
      out.limbs_[i]=t-borrow;borrow=uint64_t(first||second);
    }
    if(borrow)throw std::runtime_error("exact-digit128-unresolved-borrow");
    out.trim();return out;
  }
  unsigned bit_length()const{
    size_t n=limbs_.size();while(n&&!limbs_[n-1])--n;
    return n?static_cast<unsigned>(64*(n-1))+bits64(limbs_[n-1]):0;
  }
  bool bit(unsigned i)const{return ((word(i/64)>>(i%64))&1u)!=0;}
  bool any_below(unsigned count)const{
    const size_t whole=count/64;const unsigned rest=count%64;
    for(size_t i=0;i<std::min(whole,limbs_.size());++i)if(limbs_[i])return true;
    if(rest && whole<limbs_.size() &&
        (limbs_[whole]&((uint64_t(1)<<rest)-1)))return true;
    return false;
  }
  U128 low_after_right_shift(unsigned shift)const{
    const size_t i=shift/64;const unsigned b=shift%64;
    if(!b)return (U128(word(i+1))<<64)|word(i);
    const uint64_t lo=(word(i)>>b)|(word(i+1)<<(64-b));
    const uint64_t hi=(word(i+1)>>b)|(word(i+2)<<(64-b));
    return (U128(hi)<<64)|lo;
  }
  U128 round_to_integer(int shift,Stats &stats)const{
    // Callers arrange that the retained integer has at most 113 bits.
    if(shift<=0){
      const unsigned left=static_cast<unsigned>(-shift);
      if(left>=128 || bit_length()+left>113)
        throw std::runtime_error("exact-digit128-exact-left-shift-range");
      return low_after_right_shift(0)<<left;
    }
    const unsigned right=static_cast<unsigned>(shift);
    if(bit_length()>right+113u)
      throw std::runtime_error("exact-digit128-retained-integer-range");
    U128 kept=low_after_right_shift(right);
    const bool guard=bit(right-1),sticky=any_below(right-1);
    if(guard||sticky)++stats.inexact_roundings;
    if(guard&&(sticky||(kept&1)))++kept;
    return kept;
  }
};
inline void multiply_significands(U128 a,U128 b,uint64_t out[4]){
  // Each input has at most 113 bits. All four products and middle sums
  // below are unsigned; their stated sizes are below 128 bits.
  const uint64_t a0=static_cast<uint64_t>(a),a1=static_cast<uint64_t>(a>>64),
    b0=static_cast<uint64_t>(b),b1=static_cast<uint64_t>(b>>64);
  const U128 p00=U128(a0)*b0,p01=U128(a0)*b1,
    p10=U128(a1)*b0,p11=U128(a1)*b1;
  out[0]=static_cast<uint64_t>(p00);
  const U128 middle=(p00>>64)+static_cast<uint64_t>(p01)+static_cast<uint64_t>(p10);
  out[1]=static_cast<uint64_t>(middle);
  const U128 upper=(p01>>64)+(p10>>64)+static_cast<uint64_t>(p11)+(middle>>64);
  out[2]=static_cast<uint64_t>(upper);
  const U128 high=(p11>>64)+(upper>>64);
  if((high>>64)!=0)throw std::runtime_error("exact-digit128-product-carry-range");
  out[3]=static_cast<uint64_t>(high);
}
inline Q round_magnitude(const Magnitude &m,int base,bool negative,Stats &stats){
  const unsigned length=m.bit_length();
  if(!length){++stats.exact_zero_outputs;return encode(false,0,0);}
  const int high=static_cast<int>(length)-1;
  int exponent=base+high;
  if(exponent < -16382){
    // Direct subnormal quantization, NOT normal rounding followed by a
    // second rounding. It includes ties at zero and at minimum normal.
    const U128 fraction=m.round_to_integer(-16494-base,stats);
    if(!fraction){++stats.rounded_zero_outputs;return encode(negative,0,0);}
    if(fraction==(U128(1)<<112))return encode(negative,1,0);
    if(fraction>(U128(1)<<112))
      throw std::runtime_error("exact-digit128-subnormal-rounding-range");
    ++stats.subnormal_outputs;return encode(negative,0,fraction);
  }
  U128 significand=m.round_to_integer(high-112,stats);
  if(significand==(U128(1)<<113)){significand>>=1;++exponent;}
  if(exponent>16383){++stats.overflow_outputs;return encode(negative,0x7fff,0);}
  if(significand<(U128(1)<<112) || significand>=(U128(1)<<113))
    throw std::runtime_error("exact-digit128-normal-rounding-range");
  return encode(negative,static_cast<unsigned>(exponent+16383),
      significand-(U128(1)<<112));
}
struct ExactSum {
  int base;Magnitude positive,negative;
  explicit ExactSum(int e):base(e){}
  void add_signed(int64_t value,unsigned shift){
    if(!value)return;
    const bool neg=value<0;
    const uint64_t magnitude=neg?uint64_t(-(value+1))+1:uint64_t(value);
    (neg?negative:positive).add_shifted_word(magnitude,shift);
  }
  void add_product(const Word &a,const Word &b){
    if(!a.mantissa||!b.mantissa)return;
    const int shift=a.exponent+b.exponent-base;
    if(shift<0)throw std::runtime_error("exact-digit128-product-base");
    uint64_t product[4];multiply_significands(a.mantissa,b.mantissa,product);
    ((a.negative!=b.negative)?negative:positive).add_shifted_product(
        product,static_cast<unsigned>(shift));
  }
  Q rounded(Stats &stats)const{
    stats.max_positive_words=std::max(stats.max_positive_words,positive.size());
    stats.max_negative_words=std::max(stats.max_negative_words,negative.size());
    const int ordering=positive.compare(negative);
    if(!ordering){++stats.exact_zero_outputs;return encode(false,0,0);}
    const bool neg=ordering<0;
    const Magnitude magnitude=neg?Magnitude::subtract(negative,positive):
      Magnitude::subtract(positive,negative);
    return round_magnitude(magnitude,base,neg,stats);
  }
};
struct VectorView {
  const Q *data=nullptr;size_t length=0,stride=1;
  Q at(size_t i)const{return data[i*stride];}
  void validate()const{
    if(length&&!data)throw std::runtime_error("exact-digit128-null-vector");
    if(length>1 && stride>std::numeric_limits<size_t>::max()/(length-1))
      throw std::runtime_error("exact-digit128-vector-stride-overflow");
  }
};
struct PackedVector {
  std::vector<Word> words;
  std::vector<int32_t> digits;
  std::vector<unsigned char> active;
  int base=0;unsigned span=0;size_t layers=0;
  bool zero=true,packed=false;
  size_t length()const{return words.size();}
  const int32_t *plane(size_t i)const{return digits.data()+i*length();}
};
inline PackedVector prepare(VectorView input,size_t &packing_budget,
    Stats &stats,Poll poll=nullptr){
  input.validate();PackedVector out;out.words.reserve(input.length);
  int low=0,high=0;
  for(size_t i=0;i<input.length;++i){
    if((i&255u)==0)poll_if(poll);
    Word w=decode(input.at(i),stats);
    if(w.mantissa){
      const int top=w.exponent+static_cast<int>(bits128(w.mantissa))-1;
      if(out.zero){low=w.exponent;high=top;out.zero=false;}
      else{low=std::min(low,w.exponent);high=std::max(high,top);}
    }
    out.words.push_back(w);
  }
  if(out.zero){out.packed=true;return out;}
  out.base=low;out.span=static_cast<unsigned>(high-low+1);
  out.layers=(out.span+DIGIT_BITS-1)/DIGIT_BITS;
  stats.max_observed_span_bits=std::max(stats.max_observed_span_bits,out.span);
  stats.max_observed_limb_count=std::max(stats.max_observed_limb_count,
      static_cast<unsigned>(out.layers));
  if(out.layers>FAST_LIMB_LIMIT){++stats.wide_span_vectors;return out;}
  const size_t cells=checked_product(out.layers,input.length),
    bytes=checked_product(cells,sizeof(int32_t));
  if(bytes>packing_budget){++stats.packing_budget_vectors;return out;}
  // Allocation failure is a real resource exception; it is not represented
  // as a zero result. Only the explicit packing budget takes the exact
  // alternative path below.
  out.digits.assign(cells,0);out.active.assign(out.layers,0);
  for(size_t l=0;l<out.layers;++l){
    poll_if(poll);const int plane_bit=static_cast<int>(DIGIT_BITS*l);
    int32_t *dest=out.digits.data()+l*input.length;
    for(size_t i=0;i<input.length;++i){
      const Word &w=out.words[i];if(!w.mantissa)continue;
      const int relative=plane_bit-(w.exponent-low);uint32_t digit=0;
      if(relative>=0){
        if(relative<128)digit=static_cast<uint32_t>(w.mantissa>>relative)&DIGIT_MASK;
      }else if(relative>-static_cast<int>(DIGIT_BITS)){
        digit=(static_cast<uint32_t>(w.mantissa)<<static_cast<unsigned>(-relative))&DIGIT_MASK;
      }
      dest[i]=w.negative?-static_cast<int32_t>(digit):static_cast<int32_t>(digit);
      if(digit)out.active[l]=1;
    }
    ++stats.complete_digit_planes;if(!out.active[l])++stats.zero_digit_planes;
  }
  out.packed=true;packing_budget-=bytes;++stats.packed_vectors;return out;
}
inline Q dot(const PackedVector &a,const PackedVector &b,Stats &stats,Poll poll=nullptr){
  if(a.length()!=b.length())throw std::runtime_error("exact-digit128-dot-shape");
  ++stats.exact_dot_calls;
  if(a.zero||b.zero){++stats.zero_dot_calls;++stats.exact_zero_outputs;return encode(false,0,0);}
  const size_t k=a.length();
  if(a.packed&&b.packed){
    ++stats.packed_dot_calls;ExactSum sum(a.base+b.base);
    for(size_t la=0;la<a.layers;++la)if(a.active[la])
      for(size_t lb=0;lb<b.layers;++lb)if(b.active[lb]){
        const int32_t *av=a.plane(la),*bv=b.plane(lb);
        for(size_t start=0;start<k;){
          poll_if(poll);const size_t end=start+std::min(REDUCTION_BLOCK,k-start);
          int64_t partial=0;
          for(size_t n=start;n<end;++n){
            // Both factors are explicitly widened BEFORE multiplication.
            // Each |factor| <= 2^20-1; every partial absolute sum < 2^51.
            partial+=int64_t(av[n])*int64_t(bv[n]);
          }
          stats.digit_products+=end-start;++stats.integer_partial_sums;
          sum.add_signed(partial,static_cast<unsigned>(DIGIT_BITS*(la+lb)));
          start=end;
        }
      }
    return sum.rounded(stats);
  }
  ++stats.wide_dot_calls;
  bool nonzero=false;int base=0;
  for(size_t n=0;n<k;++n)if(a.words[n].mantissa&&b.words[n].mantissa){
    const int e=a.words[n].exponent+b.words[n].exponent;
    if(!nonzero||e<base)base=e;nonzero=true;
  }
  if(!nonzero){++stats.exact_zero_outputs;return encode(false,0,0);}
  ExactSum sum(base);
  for(size_t n=0;n<k;++n){
    if((n&255u)==0)poll_if(poll);
    if(a.words[n].mantissa&&b.words[n].mantissa){
      sum.add_product(a.words[n],b.words[n]);++stats.complete_scalar_products;
    }
  }
  return sum.rounded(stats);
}
inline Q dot(VectorView a,VectorView b,Stats &stats,Poll poll=nullptr){
  size_t budget=PACKING_BYTES_LIMIT;
  const PackedVector pa=prepare(a,budget,stats,poll),pb=prepare(b,budget,stats,poll);
  return dot(pa,pb,stats,poll);
}
inline std::vector<Q> multiply(const Q *a,const Q *b,size_t m,size_t k,size_t n,
    Stats &stats,Poll poll=nullptr){
  // Inputs and output are ordinary row-major binary128 matrices. All B
  // columns are decoded once; A rows are decoded one at a time.
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
    for(size_t j=0;j<n;++j)out[i*n+j]=dot(row,columns[j],stats,poll);
  }
  return out;
}
} // namespace exact_digit128
#endif
