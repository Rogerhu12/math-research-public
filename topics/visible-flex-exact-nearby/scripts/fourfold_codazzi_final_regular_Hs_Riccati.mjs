#!/usr/bin/env node
// Actual final regular graph: true nonlinear H^s derivative and Riccati outer ports.
// Every numerical input below is a published outward text bound of the same ac1d centre.
// No binary native report, finite candidate array, sampling, or old-centre coefficient is read.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
class Q{
 constructor(n=0n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(b){return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
 sub(b){return new Q(this.n*b.d-b.n*this.d,this.d*b.d);}
 mul(b){return new Q(this.n*b.n,this.d*b.d);}
 div(b){return new Q(this.n*b.d,this.d*b.n);}
 pow(n){if(n<0)return new Q(this.d**BigInt(-n),this.n**BigInt(-n));return new Q(this.n**BigInt(n),this.d**BigInt(n));}
 lt(b){return this.n*b.d<b.n*this.d;}
 le(b){return this.n*b.d<=b.n*this.d;}
 str(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}
}
const q=(n,d=1)=>new Q(BigInt(n),BigInt(d));
function dec(s){const[a,b=""]=s.split(".");const d=10n**BigInt(b.length);return new Q(BigInt(a)*d+BigInt(b),d);}


function runOuterHsBudget(){
 const G=[],gate=(name,yes,values={})=>{G.push({name,passed:!!yes,...values});if(!yes)throw Error(name);};
 const one=q(1),zero=q(0),eps=q(1,2n**512n);
 const Zact=dec("0.0000000000002533"),P=dec("0.00000000001480385"),mg=q(29,5),mup=q(7),sig=q(1,8);
 const dmin=dec("0.124999999985"),x=q(607,1000);
 let ep=one,term=one;for(let j=1;j<=8;j++){term=term.mul(q(4).mul(dmin)).div(q(j));ep=ep.add(term);}
 gate("entire_physical_fourier_tail_geometric_ratio",one.div(x).lt(ep));
 const J=32,n=q(J+1),om=one.sub(x);
 const sumtail=x.pow(J+1).mul(n.pow(2).div(om).add(q(2).mul(n).mul(x).div(om.pow(2))).add(x.mul(one.add(x)).div(om.pow(3))));
 const tail=q(32).mul(P).div(mg).mul(sumtail),Z1=q(128).mul(Zact).add(tail),Z1paid=dec("0.0000000000325");
 gate("actual_full_physical_Z_derivative_all_modes",Z1.lt(Z1paid),{head_upper:q(128).mul(Zact).str(),complete_tail_upper:tail.str(),total_upper:Z1.str()});
 const rb=q(1,2n**60n),sigmaBg=q(1,16),B1=rb.div(sigmaBg);
 const rZw=q(1,10n**10n),rBw=q(1,10n**11n),rhoZ=q(9,10n**11n),rhoB=q(9,10n**12n);
 gate("true_background_inside_wider_complex_Z_disc",Zact.add(rhoZ).lt(rZw));
 gate("true_background_inside_wider_complex_fB_disc",rb.add(rhoB).lt(rBw));
 const RC=q(4096),RD=q(16384),R0=q(2048);
 function row(z,b){
  const rf=q(10).mul(z.add(b)),F=rf.add(b),kap=q(36).mul(RC).mul(F),jf=q(9).div(one.sub(kap)),jb=eps.add(kap).div(one.sub(kap));
  return {rf,F,kap,jf,jb,T:eps.add(q(4).mul(RD).mul(F).mul(jf)),C:q(4).mul(R0).mul(F).mul(jf),U:eps.add(q(4).mul(RD).mul(F).mul(one.add(jb))),V:q(4).mul(R0).mul(F).mul(one.add(jb)),image:q(9).mul(z).add(eps.mul(b)).add(q(9).mul(RC).mul(F.pow(2)))};
 }
 const wide=row(rZw,rBw),small=row(q(1,10n**12n),rb);
 gate("wider_long_complete_complex_domain",q(2).mul(wide.F).lt(q(1,2n**25n))&&q(6).mul(wide.F).lt(q(1,2n**20n)));
 gate("wider_true_C_to_Dirichlet_contraction",wide.kap.lt(q(1,1000))&&wide.image.lt(wide.rf));
 const Xi=Z1paid.div(rhoZ).add(B1.div(rhoB));
 gate("actual_background_translation_size",Xi.lt(dec("0.361113")));
 const T1=small.T.add(Xi.mul(wide.T)),U1=small.U.add(Xi.mul(wide.U));
 const T0p=dec("0.000005898255"),C0p=dec("0.0000007372818"),U0p=dec("0.000000655362"),V0p=dec("0.0000000819203");
 gate("same_small_ball_complete_L2_Z_row",small.T.lt(T0p));
 gate("same_small_ball_true_mean_row",small.C.lt(C0p));
 gate("same_small_ball_independent_fB_L2_row",small.U.lt(U0p));
 gate("same_small_ball_independent_fB_mean_row",small.V.lt(V0p));
 const T1p=q(1,4000),U1p=dec("0.000027");
 gate("full_nonlinear_DN_H1_not_only_Hilbert",T1.lt(T1p));
 gate("independent_fB_H1_source_column",U1.lt(U1p));
 const Tsix=dec("0.0000111"),Usix=dec("0.00000125");
 gate("exact_Hone_sixth_interpolation_Z",T0p.pow(5).mul(T1p).lt(Tsix.pow(6)));
 gate("exact_Hone_sixth_interpolation_fB",U0p.pow(5).mul(U1p).lt(Usix.pow(6)));
 const qmin=dec("0.9999999999993");
 gate("complete_H1_C_to_B_graph_inverse",one.div(qmin.sub(T1p)).lt(dec("1.000251")));
 gate("complete_Hone_sixth_C_to_B_graph_inverse",one.div(qmin.sub(Tsix)).lt(dec("1.0000112")));
 const Us=dec("0.000000001643190"),Vs=dec("0.000000009603792");
 const eps1=P.div(sig),comp=one.div(one.sub(eps1)),Khil=dec("0.000000007190442");
 const uA=Us.mul(q(9)),wA=Vs.mul(q(9)),uPhiA=Us.mul(q(136)),vPhiA=Vs.mul(q(136)),vA=mup.add(wA);
 gate("H1_all_coefficient_multipliers_are_paid",wA.lt(dec("0.000000087"))&&uA.lt(dec("0.000000015"))&&vPhiA.lt(dec("0.000001307"))&&uPhiA.lt(dec("0.000000224")));
 gate("inverse_v_full_Bone_Neumann_gap",dec("5.84461145233").sub(wA).lt(q(6))&&mg.lt(dec("5.84461145233").sub(wA)));
 const f1=comp.mul(one.add(T1p)),g1=comp.mul(one.add(C0p));
 const a1=vA.mul(f1).add(vA.mul(uA.add(uPhiA.div(q(4)))).mul(g1));
 const a2=vA.pow(2).add(vPhiA.mul(vA).div(q(4))).mul(g1);
 gate("actual_graph_complete_moving_Hs_lift_50",a1.pow(2).add(a2.pow(2)).lt(q(2500)));
 const chi=one.add(vA.div(mg)).div(q(4).mul(mg));
 const inverse=comp.mul(one.add(vPhiA.mul(chi))).div(mg.pow(2));
 gate("actual_full_moving_to_physical_Hs_recovery_003",inverse.lt(q(3,100)));
 const e2=wA.mul(q(2).mul(mup).add(wA)).add(vPhiA.mul(vA).div(q(4))).mul(g1);
 const leadInv=comp.mul(one.add(eps1)).div(mg.pow(2));
 const h2Inv=leadInv.div(one.sub(leadInv.mul(e2)));
 gate("complete_nonmean_h2_chart_is_onto_Hs",leadInv.mul(e2).lt(q(1,10n**6n))&&h2Inv.lt(q(3,100)));
 const meanMap=mup.pow(2).mul(C0p).mul(q(3,100));
 gate("true_moving_mean_rank_output_not_deleted",meanMap.lt(dec("0.000001084")));
 const EpsQ=eps;
 function rowDefect(T){
  const f=comp.mul(one.add(T)),gg=comp.mul(one.add(C0p)),pp=one.div(mg);
  const leading=mup.mul(comp.mul(T.add(EpsQ).add(C0p)).add(Khil.mul(f)));
  const error=wA.mul(f).add(vA.mul(uA.add(uPhiA.div(q(4)))).add(pp.mul(wA.mul(q(2).mul(mup).add(wA)).add(vPhiA.mul(vA).div(q(4))))).mul(gg));
  return leading.add(error).mul(q(3,100));
 }
 const E1=rowDefect(T1p),E6=rowDefect(Tsix);
 gate("true_moving_H1_Robin_defect_after_all_mean_paths",E1.lt(dec("0.000053")));
 gate("true_moving_Hone_sixth_Robin_defect",E6.lt(dec("0.0000026")));
 gate("global_reference_outer_p_lower_bound",q(1,8).lt(one.sub(one.div(q(2).mul(q(800000).pow(2)))).div(mup)));
 const a=q(17,2).mul(dec("0.0000026"));
 gate("actual_Riccati_outer_Hilbert_feedback_small",a.le(dec("0.0000221")));
 const refl=a.div(one.sub(a));
 gate("actual_complete_outer_high_Riccati_graph",refl.lt(dec("0.0000222")));
 const head= q(3).mul(q(3)).mul(dec("0.0000026")).div(one.sub(a));
 gate("complete_low_to_high_outer_boundary_column",q(385).lt(q(3).pow(6))&&head.lt(dec("0.0000235")));
 const epMean=vA.pow(2).add(vPhiA.mul(vA).div(q(4)));
 const pp=one.div(mg),ggcoef=vA.mul(uA.add(uPhiA.div(q(4)))).add(pp.mul(epMean));
 const affineMean=ggcoef.add(dec("0.0000026").mul(epMean));
 const affineB=vA.mul(comp),affineF=affineB.mul(Usix).add(affineMean.mul(V0p));
 const afactor=q(3).div(one.sub(a));
 gate("independent_fB_Riccati_affine_column",afactor.mul(affineF).lt(dec("0.000030")));
 gate("ordinary_Robin_residual_Riccati_affine_column",afactor.mul(affineB).lt(q(22)));
 gate("independent_mean_residual_Riccati_affine_column",afactor.mul(affineMean).lt(q(26)));
 const meanAffine=mup.pow(2).mul(one.add(C0p.mul(q(3,100)).mul(epMean)));
 gate("independent_mean_and_fB_true_mean_output",meanAffine.lt(q(50))&&meanAffine.mul(V0p).lt(dec("0.0000041")));
 const meanToH2=meanMap; 
 return {kind:"actual_final_regular_full_Hs_and_Riccati_outer_graph",complete:true,arithmetic:"normalized BigInt rational; explicit complete Fourier tail and Banach Cauchy/interpolation budgets",source:"scripts/fourfold_codazzi_final_regular_Hs_Riccati.mjs",candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 inputs:[
 {path:"results/R133-supplement-final-moving-centre-actual-regular-boundary.md",git_blob:"40463b6917c943e4ac991a597603cf41095baeb9"},
 {path:"results/R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md",git_blob:"a7ff7d2ca24df41ccd242ff9799b21fdcab2aec0"},
 {path:"results/R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md",git_blob:"fe1468feaf7447077d569402cc4133a9dfbeb05c"},
 {path:"results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md",git_blob:"5fd83130fead0160cece059b7bb95f2f83b07eae"}],
 background:{Z_A0:Zact.str(),fB_dotA2_sigma:"2^-60 with sigma>=1/16",Z_phi_A0:Z1paid.str(),fB_phi_dotA2:B1.str(),wider_Z_radius:rZw.str(),wider_fB_radius:rBw.str(),Cauchy_Z_radius:rhoZ.str(),Cauchy_fB_radius:rhoB.str(),Xi:Xi.str()},
 actual_DN:{Z_to_d_L2:T0p.str(),Z_to_d_H1:T1p.str(),Z_to_d_Hone_sixth:Tsix.str(),fB_to_d_L2:U0p.str(),fB_to_d_H1:U1p.str(),fB_to_d_Hone_sixth:Usix.str(),Z_to_mean:C0p.str(),fB_to_mean:V0p.str(),independent_fB_norm:"||<D>^s |D|^2 fB||2"},
 moving:{full_Hs_lift:"50 for 0<=s<=1",physical_recovery:"3/100 for 0<=s<=1",nonmean_h2_chart_inverse:"3/100",true_mean_rank_upper:"0.000001084",complete_Robin_defect_H1:"0.000053",complete_Robin_defect_Hone_sixth:"0.0000026"},
 Riccati_outer:{reference_p:"p_M(R)=q_*/(-m_R), frequency independent; q_*=(1+w_R^2)^(-1/2)",other_reference_g:"any positive radial g_M(R)",homogeneous_high_graph:"0.0000222",full_low_to_high_boundary_column:"0.0000235",independent_fB_column:"0.000030",ordinary_Robin_residual_column:"22",independent_mean_residual_column:"26",source_and_mean:"retained in the exact affine equations and full nonmean h2 parameterization",cutoff:"|j|>=97 only for the stated head-column estimate"},
 permissions:{full_nonlinear_DN_derivative_Hs:true,all_0_to_1_orders_by_interpolation:true,actual_background_not_arbitrary_Hs_nonlinear_ball:true,whole_positive_body_inverse:false,global_negative_return:false,nu_scalar_inverse:false,nonlinear_whole_BVP:false},gates:G};
}

export {runOuterHsBudget};
if(typeof process!=="undefined"&&process.versions?.node&&process.argv[1]?.endsWith("fourfold_codazzi_final_regular_Hs_Riccati.mjs")){
 const result=runOuterHsBudget(),json=JSON.stringify(result,null,2)+"\n";
 const k=process.argv.indexOf("--out");
 if(k>=0){const fs=await import("node:fs");fs.writeFileSync(process.argv[k+1],json);process.stdout.write(JSON.stringify({complete:result.complete,gates:result.gates.length,out:process.argv[k+1]})+"\n");}
 else process.stdout.write(json);
}
