# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：389f38e01ffe622e59428e91722df25ab6826655**（2026-11-28 04:31 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull 2026-11-27 01:48 Asia/Taipei；04:21重试仍无可用执行环境，shell未启动。按根规则8连接器同步、读diff、expected_sha非force提交，拒绝立即同步重基重推至成功；环境恢复立即pull --rebase。下一次真实尝试不晚于2026-11-28 05:21。令牌只CLI。数学程序仅本公开仓库Actions；本地/V8仅metadata/文本，不作数学计算。[此前偏差纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-arithmetic-endpoint-span.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：完整一般 p；原单位与实际 cochain

[R1003](results/R1003-global-scope-and-remaining-branches.md)保全部N_ns主范围；R317的整j/固定K/σ1/二三小域及小惯性C³均不可删。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)原good≥floor(p/16)+3、forced Ω(p/logp)，完整T链预算不改1/16。候选O(p^1.5logp)和有界惰性CM不推Q-CM，单cusp无Runge。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)已付同时非零/localization、导子和判别式，选素界仍不够小；[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)分母annihilator允许−1modp整支。几何Weil零不消HS混合项。

[原整K₂](notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)残余μp⊗J(K)[p]、全cusp Δ分裂及[整p Chen/Ohta](notes/2026-11-27-original-prime-p-Chen-isogeny-and-odd-torsion-reduction.md)均已付；Σ(p²)[p∞]=0不消非Shimura odd。R1131 forced r=p−1−2j及两Bernoulli门锁实际非分裂rank2/Fricke+，radical β_(4j+2)而非βr，规范K₂角色2j+2零。R1132低偶r两Bernoulli门迫full块w负、原正商该p块零，规范K₂角色2−r零；r2需p∤Bp−3，p7mod8指定低偶r无条件。只运输已证明的简单socle/整torsion，不代K₂/p。

[原整单位关系](notes/2026-11-28-original-integral-Manin-relations-and-cusp-constants.md)仅将原单位符号格中已有理为零的平凡角色关系整提升，保实cusps、e₀/平均/S-unit transfer及R1132前提；不除12p。

[R1133](results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)原half范数恢复Vχ，Heis/class4 p⁵塔及Fourier交换已成；cusp须四moments，Norm只给M0，p⁷纤维积仅两极端四阶。原aux-c相关保𝒫=2c²{M_a,M_b}−2c⁴C_ab，原弦跨line保实际第二槽ψ₂²和全部cross；常Lie中心读K₂/p的ω²，不代e₀整torsion。全部公式/links沿前态，四阶proper/arithmetic下降继续。

[R1136](results/R1136-original-forced-compact-Manin-sources.md)原两秩紧致源/J/transfer/θ² diamond及ordinary Hecke全部付清；§§11–13付full-basis regularity/Gysin、CRT/adjugate、rank1 exact p²/Fricke+ twist（保quadratic-St）与整away-p order。物理σ修正给I_(2j+2k+2)，四阶指定邻对仍在低mixed门外。

[R1138](results/R1138-original-integral-bare-cup-smoothing-comparison.md)原辅助c除子比较在augmentation后给Lχθ′=nq*Gχ−χ(n²)π*Gχ、T̃_nGχ=(n+χ(n²))Gχ，Gχ=2Fχ/m；完整四项Cor合并为S_n=(4/m²)(n⁴−n^(a+2)T_n+n^(2a+1)){Fχ,Fψ}。全部n>3,n≠p成立，不除κχ(n)/p/分裂度。左侧是R1136两秩的完整紧致读数；其紧致target公共核由R1139在低mixed门下消去，未宣杯积零。


[R1139](results/R1139-original-compact-target-unsmoothing-and-bare-cup.md)在R1136 F33门下付整个compact H²θ的单位理想：geom H²(2)=μp奇角色消，HS保Jacobian/base两层；F=E+(1−E)V/v给(F−1)²0，故(2−F)F=1。Pic/Br商及全部cusp均保，(4/m²)原cup=Ψ(c)准确无公共核歧义；指定Ψ(c)值与门外四阶仍开。

[R1140](results/R1140-original-low-weight-Manin-source-reduction.md)对原j1,k2直接模p证明C¹=0、C²=(16δ²/21)C_Eis；实际J/apolar/三低权商及Merel完整Hecke给端点λℓ=ℓ⁻²+ℓ³。无Bernoulli门已有β=β_E+β₈，v_n=n⁻¹¹(n⁵−1)(n¹⁰−1)选unit，β_E=S_n/v_n而V_nβ₈0；两者均为真实compact像。p∤B16 B_(p−15)才删β₈；原端点值未零，不造F0。继续actual arithmetic endpoint/高cochains。

R1140§§10–12再以真实degree-p norm（不除p）把端点写成p-isogeny两槽G₄/G₈；trace-fixed付24常数，原一次Galois/Cartan权为u⁴v⁸，fixed-Weil n⁻⁴与两cross给完整V_n。β_E=16δ² V_n₀𝒯{W*G₄,G₈}/(21m²v₀)；保V投影，不假bare trace proper。

[R1141](results/R1141-original-arithmetic-endpoint-and-circular-unit-cup.md)在p∤B_(p−5)时付原arith-compact θ=ω⁻⁶的整个I3像=span{Fχ1,βχ2}，允许零。原torsor延拓全S={p}，Hecke闭包保支撑；BrS0/完整Pic商、MW可除项及DVR π支付真实socle提升。Q下降为ω5→V→ω10，B10单位删商H¹。再B16/B_(p−15)门得∃c原cup{F1,F2/ε2^c}=0于fieldK₂/p；c未定，proper Pic H²障碍与高cover不删。继续原p-isogeny端点标量/cochains。

## O1：指定 U^m 的原两 jet

[原Tate normal-FM](notes/2026-11-27-original-Tate-three-torsion-normal-FM-variation.md)保原Miller/Verschiebung、kerV/−Q刚化、全自然基及P/N连接。§16真正普通Picard连接为(D_R+h_Z)T̂[f]=T̂[(Ψε+H D_T)f]，保moving-zero的HD_T与全部高极；首normal旁列unit不代指定e/K4，p-curvature仅核尺度。

[R1137](results/R1137-original-Lame-conjugation-with-complete-boundaries.md)付D₀/Λ全部rank3端点、D⁴的δ⁴c_N及原U/B/C变换，指定φ满足2Λ³φ+3ΨΛ²φ+6Φ(V)φ+3δΨ=0；Λ非局部D，moving p极仍保，真实两jet消元继续。

R1137§2现从同一原moving-p核付实际Padé：N=(p−5)/6，Q=H(−v²x)、P=−J(−v²x)/a0，QF−P恰在2N+1阶起且首系数unit，F=₂F₁(1/3,1/2;4/3)。e/K4双零 iff Q0=Q1=0，P也含x²，约去后deg≤N−2/contact2N−1。sqrt(1−x)不能删；继续排这个指定二次缺陷。

[固定Prym三同源](notes/2026-11-28-original-fixed-Prym-three-isogeny-and-trace.md)付真实φ=[−s]ψ到同一E及全部trace尺度；Ξ、Υ读3e、−3K4而同在一个CM线，不由完美性推双非零。原genus4双cover的branch不被τ保持，Norm=U³+125v²/4非平方。[genus4全局Raynaud](notes/2026-11-28-original-genus-four-global-Raynaud-vanishing.md)付e0 iff原非hyperelliptic Y全β0，不反用单向引理。

R1113完整Lamé谱/三Darboux、R1130邻项δ、R1126六CM十五配对、原Fermat全矩与短旗标均已成，**两原和e/K4非同时零仍开**；全span/零谱投影/相邻unit/非CM ordinary均不替代指定原输入。旧至500000窗口不重扫。[R1134](results/R1134-original-single-source-low-Euler-obstruction.md)原四输入十五Euler列fullrank，run/hash已消费，有限结论不外推。完整旧公式与其它输入沿上列前态/open续接。

## O2：原 Gaussian good-mask 与共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md) p4k3且p|Bp−3时χ2 coarse一次斜率unit，只付跨盘。剩余p∤Bp−3；盘内还需原高度。[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)给线性多个非constant，未付独立/纤维唯一。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)与[原有限重建](notes/2026-11-28-original-Gaussian-finite-contiguity-and-spectral-reconstruction.md)付完整good mask、常数/高尾、Möbius及R² Newton商；h≥1的L−2h可逆，h0不外推。R1135低行给至多一unordered pair，另一支Δ_low/48仍开；norm2消V₂后保c₃=−40G_(p−3)+25H+8a³V₃/81−4a⁴V₄/243。另两二同源仅原偶band对角运输，标准旁unit在CM gauge抵消。

R1135§10已付同coarse component两实际twist的全部运输：α^p=iα，t*′=it*，z′=−z；δ′=ηδ，Kronecker γ′=ηγ、N_R′=η⁻¹N_R，而Weil γ_W/bχ保持。完整核及i0常数给Π′(z′)=Π(−z′)，两线统一为z∈Fp。低行唯一unordered pair/Δ分离范围因此覆盖两线；保S0/P0，不合并其他components，不宣Δunit。

## 已完成与永久边界

[R1125](results/R1125-original-full47-rational-point-classification.md)完整47Q恰八CM，所有高度/whole盘及独立审计均成。真实run/hash沿归档保留，不重跑47/41/旧窗口。

同h仍须本原/Legendre/fi gj两mask。R971 full-span、R1006全p稳定已否，特定A/E4/mark仍开。R948仅有限Abel零集，候选MW像可非零；原σ/cY、η_h、d/N、nonp/Poincaré/splitting不可删。R907原artifact真404，不据摘要重造；R1004导子下界不代高度上界。O3–6全部准确输入与旧断点见open及逐字归档。主标准不变，继续。
