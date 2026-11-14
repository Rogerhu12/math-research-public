// R104 exact comparisons of selected dyadics observed in the completed primary.
// Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
// This V8/BigInt ledger does not reread the currently unavailable large primary,
// rerun Arb, certify additional modes, or infer a true operator lower bound.
function r104SelectedLedger() {
 const dyad=(n,e)=>e>=0?{n:BigInt(n)<<BigInt(e),d:1n}:{n:BigInt(n),d:1n<<BigInt(-e)};
 const times=(a,k)=>({n:a.n*BigInt(k),d:a.d});
 const gt=(a,n)=>a.n>BigInt(n)*a.d;
 const out=a=>({numerator:a.n.toString(),denominator:a.d.toString()});
 const a=dyad("39937085760109759278246886004",-94);
 const b=dyad("42000374313864553167573788734",-85);
 const cutV=dyad("1051299658881783402097311",-179);
 const gates={
  original_source_positions18:2*9===18,
  ordered_source_target_pairs171:18*19/2===171,
  mode_source_target_pairs342:2*(18*19/2)===342,
  three_material_rows1026:3*2*(18*19/2)===1026,
  wide_centre_9_084_below_safe10:9084n<10000n,
  chosen_positive_diagonal11_3_above64:gt(times(a,40),64),
  chosen_positive_diagonal10_3_above32768:gt(times(b,40),32768),
  true_cut_local_V_strictly_positive:gt(cutV,0)
 };
 if(!Object.values(gates).every(Boolean))throw Error("Unpaid selected R104 integer comparison");
 return {
  schema:"visible-flex-R104-selected-observed-dyadics-v1",
  author:"exact_closure (GPT-6 Astra Pro; AI-assisted)",
  status:"Actual V8 BigInt comparison only; no new Arb/ODE or large-primary reread",
  all_gates:true,gates,
  observation_origin:{
   primary:"notes/2026-11-13-closure-middle-causal-mixed-m94m96-r1.json",
   sha256:"62156ade93e31729c7500e79dbc01c3f4267d1a89a2b7730af7fe1c6440df45a",
   bytes:429376,tool_session:"54526",tool_exitcode:0,
   wait4_exitcode:0,termination_signal:null,wall_seconds_observed:"96.79877495765686",
   peak_rss_kib_observed:36396,
   source_sha256:"3bbbecae0b3df6927b157d56d0d11add096a6fe979e0d222339383a90d31f2b2"
  },
  values:{
   complete_centre_at_strip18over125_safe_constant:"10",
   complete_weak_derivative_coefficient:"40",
   chosen_gamma1_cell11segment3_mode94:out(a),
   chosen_gamma1_cell10segment3_mode96:out(b),
   chosen_Jdiagonal_cell11segment3:out(times(a,40)),
   chosen_Jdiagonal_cell10segment3:out(times(b,40)),
   true_cut_V_first:out(cutV)
  },
  interpretation:"Lower statements concern the chosen positive upper-budget coefficients, not the true Green/operator norm. Diagonal scalar reweighting cannot reduce these selected comparison diagonals.",
  source_and_output_units:"c_background V^p source-x weak mass to physical strong output, same constant strip; output has no V divisor",
  full18_block_nonlinear_contraction:false,
  actual_middle_solution_claimed:false,
  real_PDE_nonexistence_claimed:false
 };
}
if(typeof module!=="undefined")module.exports={r104SelectedLedger};
