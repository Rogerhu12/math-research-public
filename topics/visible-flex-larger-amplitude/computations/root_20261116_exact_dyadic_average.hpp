// R561: preserve the actual first product and replace only an exact
// positive power-of-two normalization of a normal binary128 word.
// Unsupported inputs use the original second multiplication.
#ifndef VISIBLE_R561_EXACT_DYADIC_AVERAGE_HPP
#define VISIBLE_R561_EXACT_DYADIC_AVERAGE_HPP

struct R561AveragePathStats {
  uint64_t terms=0,exact_normal=0,exact_signed_zero=0,original_multiply=0,
    fallback_layout=0,fallback_count=0,fallback_inverse=0,
    fallback_nonfinite=0,fallback_subnormal=0,fallback_normal_to_subnormal=0;
  bool last_present=false;
  const char *last_phase="absent";
  int last_angle=-1,last_index=-1,last_shift=-1,last_exponent=-1;
  void mark(const char *phase,int angle,int index,int shift,int exponent=-1){
    last_present=true;last_phase=phase;last_angle=angle;last_index=index;
    last_shift=shift;last_exponent=exponent;
  }
  void join(const R561AveragePathStats &s){
    terms+=s.terms;exact_normal+=s.exact_normal;
    exact_signed_zero+=s.exact_signed_zero;original_multiply+=s.original_multiply;
    fallback_layout+=s.fallback_layout;fallback_count+=s.fallback_count;
    fallback_inverse+=s.fallback_inverse;fallback_nonfinite+=s.fallback_nonfinite;
    fallback_subnormal+=s.fallback_subnormal;
    fallback_normal_to_subnormal+=s.fallback_normal_to_subnormal;
    if(s.last_present){
      last_present=true;last_phase=s.last_phase;last_angle=s.last_angle;
      last_index=s.last_index;last_shift=s.last_shift;last_exponent=s.last_exponent;
    }
  }
};
struct R561AverageStats {
  R561AveragePathStats root_residual,root_gram,primal_flux;
  void join(const R561AverageStats &s){
    root_residual.join(s.root_residual);root_gram.join(s.root_gram);
    primal_flux.join(s.primal_flux);
  }
};

// This is a representation eligibility check, not a scientific gate.
// The exact inverse is still computed by the unchanged caller expression.
struct R561DyadicScale {
  Q inverse;
  int shift=-1;
  bool layout_supported=false,power_of_two_count=false,inverse_word_matches=false;
  R561DyadicScale(int count,Q actual_inverse):inverse(actual_inverse){
#if defined(__SIZEOF_INT128__) && __SIZEOF_INT128__ == 16 && defined(__BYTE_ORDER__) && defined(__ORDER_LITTLE_ENDIAN__) && __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
    layout_supported=sizeof(Q)==16 && FLT128_MANT_DIG==113 &&
      FLT128_MAX_EXP==16384 && FLT128_MIN_EXP==-16381 &&
      std::numeric_limits<unsigned char>::digits==8;
    if(!layout_supported)return;
    const unsigned n=count>0?static_cast<unsigned>(count):0;
    if(n==0 || (n&(n-1))!=0)return;
    power_of_two_count=true;shift=0;
    for(unsigned left=n;left>1;left>>=1)++shift;
    using U=unsigned __int128;
    U word=0;std::memcpy(&word,&inverse,sizeof(Q));
    // A positive normal 1 * 2^-shift with all fraction bits zero.
    const U expected=static_cast<U>(16383-shift)<<112;
    inverse_word_matches=word==expected;
#else
    (void)count;
#endif
  }
};

static inline Q r561_average_actual_product(Q product,const R561DyadicScale &scale,
    R561AveragePathStats &s,int angle,int index){
  ++s.terms;
  s.mark("actual-first-product-returned",angle,index,scale.shift);
  const char *fallback="unsupported-native-word-layout";
  if(!scale.layout_supported){++s.fallback_layout;}
  else if(!scale.power_of_two_count){++s.fallback_count;fallback="non-dyadic-count";}
  else if(!scale.inverse_word_matches){++s.fallback_inverse;fallback="actual-inverse-word-not-exact";}
  else{
#if defined(__SIZEOF_INT128__) && __SIZEOF_INT128__ == 16 && defined(__BYTE_ORDER__) && defined(__ORDER_LITTLE_ENDIAN__) && __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
    using U=unsigned __int128;
    U word=0;std::memcpy(&word,&product,sizeof(Q));
    const unsigned exponent=static_cast<unsigned>((word>>112)&static_cast<U>(0x7fff));
    s.last_exponent=static_cast<int>(exponent);
    // Preserve either zero sign. The original inverse is positive and exact.
    if((word<<1)==0){
      ++s.exact_signed_zero;
      s.mark("exact-signed-zero",angle,index,scale.shift,static_cast<int>(exponent));
      return product;
    }
    if(exponent>static_cast<unsigned>(scale.shift) && exponent<0x7fff){
      word-=static_cast<U>(scale.shift)<<112;
      Q result;std::memcpy(&result,&word,sizeof(Q));
      ++s.exact_normal;
      s.mark("exact-normal-exponent-shift",angle,index,scale.shift,static_cast<int>(exponent));
      return result;
    }
    if(exponent==0x7fff){++s.fallback_nonfinite;fallback="original-nonfinite-multiply";}
    else if(exponent==0){++s.fallback_subnormal;fallback="original-subnormal-multiply";}
    else{++s.fallback_normal_to_subnormal;fallback="original-normal-to-subnormal-multiply";}
#endif
  }
  ++s.original_multiply;
  s.mark(fallback,angle,index,scale.shift,s.last_exponent);
  return product*scale.inverse;
}

static void r561_print_average_path(std::ostream &o,const R561AveragePathStats &s){
  o<<"{\"terms\":"<<s.terms<<",\"exact_normal\":"<<s.exact_normal
   <<",\"exact_signed_zero\":"<<s.exact_signed_zero
   <<",\"original_multiply\":"<<s.original_multiply
   <<",\"fallback_layout\":"<<s.fallback_layout
   <<",\"fallback_count\":"<<s.fallback_count
   <<",\"fallback_inverse\":"<<s.fallback_inverse
   <<",\"fallback_nonfinite\":"<<s.fallback_nonfinite
   <<",\"fallback_subnormal\":"<<s.fallback_subnormal
   <<",\"fallback_normal_to_subnormal\":"<<s.fallback_normal_to_subnormal
   <<",\"last_present\":"<<(s.last_present?"true":"false")<<",\"last\":";
  if(!s.last_present)o<<"null";
  else o<<"{\"phase\":"<<quoted(s.last_phase)
    <<",\"angle_zero_based\":"<<(s.last_angle<0?"null":std::to_string(s.last_angle))
    <<",\"index_zero_based\":"<<(s.last_index<0?"null":std::to_string(s.last_index))
    <<",\"positive_dyadic_shift\":"<<(s.last_shift<0?"null":std::to_string(s.last_shift))
    <<",\"original_product_biased_exponent\":"<<(s.last_exponent<0?"null":std::to_string(s.last_exponent))<<"}";
  o<<"}";
}
static void r561_print_average_stats(std::ostream &o,const R561AverageStats &s){
  o<<"{\"schema\":\"R561-exact-normal-dyadic-angular-average-v1\",\"root_residual\":";
  r561_print_average_path(o,s.root_residual);
  o<<",\"root_gram\":";r561_print_average_path(o,s.root_gram);
  o<<",\"primal_flux\":";r561_print_average_path(o,s.primal_flux);
  o<<",\"first_product_is_original_rounded_word\":true"
   <<",\"second_multiply_replaced_only_for_exact_normal_or_signed_zero\":true"
   <<",\"all_other_words_use_original_second_multiply\":true"
   <<",\"original_sum_order_and_all_terms_retained\":true"
   <<",\"original_directional_expressions_unchanged\":true"
   <<",\"no_cross_call_cache_or_numeric_gate\":true"
   <<",\"merge_order\":\"original-stage-index-order\""
   <<",\"resource_frontier_or_speed_equality_not_claimed\":true}";
}
#endif
