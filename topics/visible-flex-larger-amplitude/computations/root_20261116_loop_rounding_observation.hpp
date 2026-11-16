// R583: one current rounding-mode observation per complete original inner loop.
// The whole R564 113-by53 product kernel is retained except its name, one
// explicit mode argument and the source of that same qualification predicate.
// All original path counters, last fields, Q fallbacks and result words remain.
// Equivalence requires the actual thread mode to stay constant within the loop.
// No floating exception-flag, running-time or resource-frontier claim is made.
#ifndef VISIBLE_R583_LOOP_ROUNDING_OBSERVATION_HPP
#define VISIBLE_R583_LOOP_ROUNDING_OBSERVATION_HPP

static inline Q r583_exact_lifted_factor_product_at_loop_mode(Q left,Q factor,
    R564ProductPathStats &s,int angle,int index,int observed_rounding){
  ++s.terms;s.begin(angle,index);
  auto original=[&](const char *phase)->Q{
    ++s.original_multiply;s.last_phase=phase;return left*factor;
  };
#if defined(__SIZEOF_INT128__) && __SIZEOF_INT128__ == 16 && defined(__BYTE_ORDER__) && defined(__ORDER_LITTLE_ENDIAN__) && __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
  if(!(sizeof(Q)==16 && FLT128_MANT_DIG==113 && FLT128_MAX_EXP==16384 &&
       FLT128_MIN_EXP==-16381 && std::numeric_limits<unsigned char>::digits==8)){
    ++s.fallback_layout;return original("original-layout-fallback");
  }
  // The containing complete inner loop observes its actual thread mode once.
  // Its source body does not change that mode; no mode is set by this helper.
  if(observed_rounding!=FE_TONEAREST){
    ++s.fallback_rounding;return original("original-rounding-mode-fallback");
  }
  using U=unsigned __int128;
  U lw=0,fw=0;std::memcpy(&lw,&left,sizeof(Q));std::memcpy(&fw,&factor,sizeof(Q));
  const unsigned le=static_cast<unsigned>((lw>>112)&static_cast<U>(0x7fff));
  const unsigned fe=static_cast<unsigned>((fw>>112)&static_cast<U>(0x7fff));
  s.last_left_exponent=static_cast<int>(le);
  s.last_factor_exponent=static_cast<int>(fe);
  if(le==0x7fff){
    ++s.fallback_left_nonfinite;return original("original-left-nonfinite");
  }
  if(fe==0x7fff){
    ++s.fallback_factor_nonfinite;return original("original-factor-nonfinite");
  }
  const U sign=(lw^fw)&(static_cast<U>(1)<<127);
  if((lw<<1)==0 || (fw<<1)==0){
    Q result;std::memcpy(&result,&sign,sizeof(Q));
    ++s.exact_signed_zero;s.last_phase="exact-finite-signed-zero";
    s.last_result_exponent=0;return result;
  }
  if(le==0){
    ++s.fallback_left_subnormal;return original("original-left-subnormal");
  }
  if(fe==0){
    ++s.fallback_factor_subnormal;return original("original-factor-subnormal");
  }
  const U low60=(static_cast<U>(1)<<60)-1;
  if((fw&low60)!=0){
    ++s.fallback_factor_precision;return original("original-factor-more-than-53-bits");
  }
  const U unit112=static_cast<U>(1)<<112;
  const U fraction112=unit112-1;
  const U a=unit112|(lw&fraction112);
  const uint64_t b=static_cast<uint64_t>((unit112|(fw&fraction112))>>60);
  // a = a0 + 2^64*a1, with a1 < 2^49 and 2^52 <= b < 2^53.
  // The exact 166-bit product is high*2^64 + low.
  const U p0=static_cast<U>(static_cast<uint64_t>(a))*static_cast<U>(b);
  const U high=(a>>64)*static_cast<U>(b)+(p0>>64);
  const uint64_t low=static_cast<uint64_t>(p0);
  const int lead=(high>>101)!=0?1:0;
  const int discard=52+lead;
  int result_exponent=static_cast<int>(le)+static_cast<int>(fe)-16383+lead;
  s.last_discard=discard;
  if(result_exponent<1 || result_exponent>32766){
    ++s.fallback_result_range;return original("original-result-range");
  }
  U rounded=(high<<(64-discard))|static_cast<U>(low>>discard);
  const uint64_t remainder=low&((uint64_t(1)<<discard)-1);
  const uint64_t half=uint64_t(1)<<(discard-1);
  const bool up=remainder>half || (remainder==half && (rounded&1)!=0);
  s.last_integer_rounding_formed=true;
  s.last_relation=remainder<half?"below-half":remainder==half?"exact-half":"above-half";
  s.last_rounded_up=up;
  if(up)++rounded;
  const bool carry=rounded==(static_cast<U>(1)<<113);
  s.last_carry=carry;
  if(carry){rounded>>=1;++result_exponent;}
  if(result_exponent>32766){
    ++s.fallback_result_range;return original("original-rounded-overflow-range");
  }
  const U output=sign|(static_cast<U>(result_exponent)<<112)|(rounded-unit112);
  Q result;std::memcpy(&result,&output,sizeof(Q));
  ++s.exact_normal;
  if(remainder<half)++s.rounding_below_half;
  else if(remainder==half)++s.rounding_exact_half;
  else ++s.rounding_above_half;
  if(up)++s.rounded_up;
  if(carry)++s.carry_to_next_exponent;
  s.last_phase="exact-normal-113-by53-nearest-even";
  s.last_result_exponent=result_exponent;
  return result;
#else
  ++s.fallback_layout;return original("original-layout-fallback");
#endif
}


#endif
