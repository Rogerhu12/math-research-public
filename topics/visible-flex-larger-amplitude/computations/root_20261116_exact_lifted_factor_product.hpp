// R564: exact original RN128 value for a finite normal Q operand times
// the actual at-most-53-bit normal factor word, with all other cases using
// the original Q multiplication. No table/state cache and no reordered sum.
#ifndef VISIBLE_R564_EXACT_LIFTED_FACTOR_PRODUCT_HPP
#define VISIBLE_R564_EXACT_LIFTED_FACTOR_PRODUCT_HPP

struct R564ProductPathStats {
  uint64_t terms=0,exact_normal=0,exact_signed_zero=0,original_multiply=0,
    fallback_layout=0,fallback_rounding=0,fallback_left_nonfinite=0,
    fallback_factor_nonfinite=0,fallback_left_subnormal=0,
    fallback_factor_subnormal=0,fallback_factor_precision=0,
    fallback_result_range=0,rounding_below_half=0,rounding_exact_half=0,
    rounding_above_half=0,rounded_up=0,carry_to_next_exponent=0;
  bool last_present=false,last_integer_rounding_formed=false;
  bool last_rounded_up=false,last_carry=false;
  const char *last_phase="absent",*last_relation="not-formed";
  int last_angle=-1,last_index=-1,last_left_exponent=-1,
    last_factor_exponent=-1,last_result_exponent=-1,last_discard=-1;
  void begin(int angle,int index){
    last_present=true;last_phase="actual-operands-received";
    last_angle=angle;last_index=index;last_left_exponent=-1;
    last_factor_exponent=-1;last_result_exponent=-1;last_discard=-1;
    last_relation="not-formed";last_integer_rounding_formed=false;
    last_rounded_up=false;last_carry=false;
  }
  void join(const R564ProductPathStats &s){
    terms+=s.terms;exact_normal+=s.exact_normal;
    exact_signed_zero+=s.exact_signed_zero;original_multiply+=s.original_multiply;
    fallback_layout+=s.fallback_layout;fallback_rounding+=s.fallback_rounding;
    fallback_left_nonfinite+=s.fallback_left_nonfinite;
    fallback_factor_nonfinite+=s.fallback_factor_nonfinite;
    fallback_left_subnormal+=s.fallback_left_subnormal;
    fallback_factor_subnormal+=s.fallback_factor_subnormal;
    fallback_factor_precision+=s.fallback_factor_precision;
    fallback_result_range+=s.fallback_result_range;
    rounding_below_half+=s.rounding_below_half;
    rounding_exact_half+=s.rounding_exact_half;
    rounding_above_half+=s.rounding_above_half;
    rounded_up+=s.rounded_up;carry_to_next_exponent+=s.carry_to_next_exponent;
    if(s.last_present){
      last_present=true;last_phase=s.last_phase;last_angle=s.last_angle;
      last_index=s.last_index;last_left_exponent=s.last_left_exponent;
      last_factor_exponent=s.last_factor_exponent;
      last_result_exponent=s.last_result_exponent;last_discard=s.last_discard;
      last_relation=s.last_relation;
      last_integer_rounding_formed=s.last_integer_rounding_formed;
      last_rounded_up=s.last_rounded_up;last_carry=s.last_carry;
    }
  }
};
struct R564ProductStats {
  R564ProductPathStats root_residual,root_gram,primal_flux;
  void join(const R564ProductStats &s){
    root_residual.join(s.root_residual);root_gram.join(s.root_gram);
    primal_flux.join(s.primal_flux);
  }
};

static inline Q r564_exact_lifted_factor_product(Q left,Q factor,
    R564ProductPathStats &s,int angle,int index){
  ++s.terms;s.begin(angle,index);
  auto original=[&](const char *phase)->Q{
    ++s.original_multiply;s.last_phase=phase;return left*factor;
  };
#if defined(__SIZEOF_INT128__) && __SIZEOF_INT128__ == 16 && defined(__BYTE_ORDER__) && defined(__ORDER_LITTLE_ENDIAN__) && __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
  if(!(sizeof(Q)==16 && FLT128_MANT_DIG==113 && FLT128_MAX_EXP==16384 &&
       FLT128_MIN_EXP==-16381 && std::numeric_limits<unsigned char>::digits==8)){
    ++s.fallback_layout;return original("original-layout-fallback");
  }
  // This observes the current mode for this multiplication; it never changes it.
  if(std::fegetround()!=FE_TONEAREST){
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

static void r564_print_product_path(std::ostream &o,const R564ProductPathStats &s){
  o<<"{\"terms\":"<<s.terms<<",\"exact_normal\":"<<s.exact_normal
   <<",\"exact_signed_zero\":"<<s.exact_signed_zero
   <<",\"original_multiply\":"<<s.original_multiply
   <<",\"fallback_layout\":"<<s.fallback_layout
   <<",\"fallback_rounding\":"<<s.fallback_rounding
   <<",\"fallback_left_nonfinite\":"<<s.fallback_left_nonfinite
   <<",\"fallback_factor_nonfinite\":"<<s.fallback_factor_nonfinite
   <<",\"fallback_left_subnormal\":"<<s.fallback_left_subnormal
   <<",\"fallback_factor_subnormal\":"<<s.fallback_factor_subnormal
   <<",\"fallback_factor_precision\":"<<s.fallback_factor_precision
   <<",\"fallback_result_range\":"<<s.fallback_result_range
   <<",\"rounding_below_half\":"<<s.rounding_below_half
   <<",\"rounding_exact_half\":"<<s.rounding_exact_half
   <<",\"rounding_above_half\":"<<s.rounding_above_half
   <<",\"rounded_up\":"<<s.rounded_up
   <<",\"carry_to_next_exponent\":"<<s.carry_to_next_exponent
   <<",\"last_present\":"<<(s.last_present?"true":"false")<<",\"last\":";
  if(!s.last_present)o<<"null";
  else{
    o<<"{\"phase\":"<<quoted(s.last_phase)
     <<",\"angle_zero_based\":"<<(s.last_angle<0?"null":std::to_string(s.last_angle))
     <<",\"index_zero_based\":"<<(s.last_index<0?"null":std::to_string(s.last_index))
     <<",\"left_biased_exponent\":"<<(s.last_left_exponent<0?"null":std::to_string(s.last_left_exponent))
     <<",\"factor_biased_exponent\":"<<(s.last_factor_exponent<0?"null":std::to_string(s.last_factor_exponent))
     <<",\"result_biased_exponent\":"<<(s.last_result_exponent<0?"null":std::to_string(s.last_result_exponent))
     <<",\"discarded_bits\":"<<(s.last_discard<0?"null":std::to_string(s.last_discard))
     <<",\"integer_rounding_formed\":"<<(s.last_integer_rounding_formed?"true":"false")
     <<",\"rounding_relation\":"<<quoted(s.last_relation)
     <<",\"rounded_up\":";
    if(s.last_integer_rounding_formed)o<<(s.last_rounded_up?"true":"false");else o<<"null";
    o<<",\"carry_to_next_exponent\":";
    if(s.last_integer_rounding_formed)o<<(s.last_carry?"true":"false");else o<<"null";
    o<<"}";
  }
  o<<"}";
}
static void r564_print_product_stats(std::ostream &o,const R564ProductStats &s){
  o<<"{\"schema\":\"R564-exact-lifted-factor-product-v1\",\"root_residual\":";
  r564_print_product_path(o,s.root_residual);
  o<<",\"root_gram\":";r564_print_product_path(o,s.root_gram);
  o<<",\"primal_flux\":";r564_print_product_path(o,s.primal_flux);
  o<<",\"operands_are_actual_original_words\":true"
   <<",\"normal_shortcut_is_full_113_by53_integer_product_and_nearest_even\":true"
   <<",\"original_first_product_RN128_word_preserved\":true"
   <<",\"original_first_Q_multiplication_not_executed_on_shortcut\":true"
   <<",\"all_fallbacks_execute_original_Q_multiplication\":true"
   <<",\"R561_second_product_selection_unchanged\":true"
   <<",\"all_original_sums_terms_and_directional_bodies_retained\":true"
   <<",\"no_table_state_or_cross_call_cache\":true"
   <<",\"floating_exception_flag_equivalence_not_claimed\":true"
   <<",\"merge_order\":\"original-stage-index-order\""
   <<",\"resource_frontier_speed_or_scientific_acceptance_not_claimed\":true}";
}
#endif
