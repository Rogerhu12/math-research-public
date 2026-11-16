// R572: the exact R564 product on five original root synthesis paths.
// The left expressions, original table reads and original += order remain.
// R535 fixed-word construction and all directional arithmetic are unchanged.
#ifndef VISIBLE_R572_EXACT_ROOT_SYNTHESIS_PRODUCTS_HPP
#define VISIBLE_R572_EXACT_ROOT_SYNTHESIS_PRODUCTS_HPP

struct R572SynthesisStats {
  R564ProductPathStats fixed_fallback_P,fixed_fallback_Pt,L,
    evaluation_u_words,evaluation_u_fallback;
  void join(const R572SynthesisStats &s){
    fixed_fallback_P.join(s.fixed_fallback_P);
    fixed_fallback_Pt.join(s.fixed_fallback_Pt);
    L.join(s.L);
    evaluation_u_words.join(s.evaluation_u_words);
    evaluation_u_fallback.join(s.evaluation_u_fallback);
  }
};

static void r572_print_synthesis_stats(std::ostream &o,const R572SynthesisStats &s){
  o<<"{\"schema\":\"R572-exact-root-synthesis-products-v1\",\"fixed_fallback_P\":";
  r564_print_product_path(o,s.fixed_fallback_P);
  o<<",\"fixed_fallback_Pt\":";r564_print_product_path(o,s.fixed_fallback_Pt);
  o<<",\"L\":";r564_print_product_path(o,s.L);
  o<<",\"evaluation_u_words\":";r564_print_product_path(o,s.evaluation_u_words);
  o<<",\"evaluation_u_fallback\":";r564_print_product_path(o,s.evaluation_u_fallback);
  o<<",\"last_index_is_original_zero_based_mode_j\":true"
   <<",\"P_and_U_factor_table_column_is_j\":true"
   <<",\"Pt_and_L_factor_table_column_is_j_plus_one\":true"
   <<",\"all_five_paths_reuse_actual_R564_product_qualification\":true"
   <<",\"all_five_original_RN128_product_words_preserved\":true"
   <<",\"original_Q_multiply_not_executed_on_qualified_shortcut\":true"
   <<",\"all_original_Q_fallbacks_preserved\":true"
   <<",\"left_expressions_and_all_accumulation_orders_unchanged\":true"
   <<",\"original_R535_fixed_word_construction_and_eligibility_unchanged\":true"
   <<",\"original_R535_U_word_construction_and_eligibility_unchanged\":true"
   <<",\"original_R564_three_angular_average_products_unchanged\":true"
   <<",\"original_R561_second_product_selection_unchanged\":true"
   <<",\"original_directional_arithmetic_body_unchanged\":true"
   <<",\"no_new_table_state_or_cross_root_cache\":true"
   <<",\"floating_exception_flag_equivalence_not_claimed\":true"
   <<",\"merge_order\":\"original-stage-index-order\""
   <<",\"resource_frontier_speed_or_scientific_acceptance_not_claimed\":true}";
}
#endif
