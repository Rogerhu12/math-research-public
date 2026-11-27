# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：b7559704cf6919978b1ba0eef6a6d51182c250de**（2026-11-28 07:21 Asia/Taipei；连接器同步main，两README差异已核；最近真实pull 2026-11-28 07:05 Asia/Taipei，Actions）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull：2026-11-28 07:05 Asia/Taipei，公开Actions run46080481087/job140778033392，在blob:none浅部分克隆中真实pull --rebase至ffd8a7ed，两README diff空且SHA与已读全文相同；[源/回执入口](notes/2026-11-28-terminal-rule-sync.md)。下次请求≤07:55、真实pull≤08:05。本地07:07仍无环境；恢复即pull。每次提交仍按根规则8 fresh main/diff/expected_sha非force，拒绝立即同步重推。令牌只CLI，当前同步workflow匿名无token。数学程序仅本公开Actions；V8仅metadata/文本。[此前纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-relative-Hodge-connection.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：完整一般 p、原算术 cochains 与新增尖点中心

[R1003](results/R1003-global-scope-and-remaining-branches.md)保完整N_ns；R317整j/固定K/σ1/二三小域和小惯性C³均未删。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)原good≥floor(p/16)+3、forced Ω(p/logp)，候选O(p^1.5logp)；有界惰性CM不推Q-CM。[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)原圆单位同时非零、导子/判别式已付，最小辅助素仍太大。[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)原abelian标签容−1整支；新非阿贝尔限制见R1148，不反改原结论。

[R1131–32](results.md)分别在原forced高偶r的两Bernoulli门、低偶r的B2r/Bp+1−2r门锁完整DVR/Fricke符号，消各自指定odd-K扭点及整K₂角色；r2须Bp−3，p7mod8指定r由二次类数无条件。实际radical β_(4j+2)非β_r。全cusp平均/原整rational-zero关系已付；不代任意K₂/p或全部块。

[R1133](results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)原half范数、Heis/class4 p⁵塔与Fourier交换已付；cusp四矩仍须全零，Norm仅M0，p⁷纤维积只保两极端四阶。aux-c/跨line全部cross、ψ₂²及常Lie ω²非e₀整torsion均保open/前态。四阶proper/arithmetic仍开。

[R1136–40](results.md)完整Manin、J/transfer/Hecke/cross/p-isogeny/degree-p norm和全tame已付。S_n=(4/m²)V_n{Fχ,Fψ}；一般F33门不扩大。指定j1,k2的rank1零/rank2端点16δ²/21，旧原尺度沿结果消费。

[R1143](results/R1143-original-Eisenstein-lattice-and-exact-cuspidal-endpoint.md)无条件c_Eis=−2016δ²Pχ1≠0。[R1141–42](results.md)Bp−5单位时原proper I3 H²=O/p，constant cup非零socle；MW d0/1对应field像非零/零，d未定。

[R1144](results/R1144-original-finite-moments-and-exact-proper-cup.md)无条件p>37付原proper算术 A1∪A2=−8δ² A1∪ε4/11，修正pair杯积零；ε4=βχ2/(1−a⁻⁴)，v4=1/252、v8=1/132。完整Tate算术transfer、cyclic cup、HS检测/polar/两factor2及proper回填已付。指定β8=0且Ψ_E(Pχ1)={F1,ε4}/(132δ²)，不扩一般pairs/四阶或误删未修正proper非零。

[R1146](results/R1146-original-proper-arithmetic-Heisenberg-cover.md)原L3/L5/L8的proper Heis p³、满几何像和全部cusps/ℓ≠p含2、3已付。B8给base中心H¹/H²0，每个global abelian pair唯一lift，p-local中心一维。曲线twists=J(K)[p]ω⁻⁷，B16/Bp−15门内删I8才全无。

[R1147](results/R1147-original-canonical-moment-Heisenberg-lift.md)无门以全S0有限矩/Z的H¹0/H²单射给唯一p⁴²源及规范proper Heis，det/polar/2/3/cusp/purity全付。§§8–12原primitive p^n norm/Q-cor/phase与非单位轨道给唯一compatible塔，v_d∞=(1−p^d)B_(d+2)/(d+2)、修正21(1+p⁴)/11。§§13–15同一good E fibre全部crys；未分歧F原43维格幅14经FL准确恢复原modp四维Heis quotient。未升I、未给relative矩阵/SS首jet；global继续已刊theta/relative来源。

[R1148](results/R1148-original-canonical-cusp-Heisenberg-and-minus-one-Frobenius.md)付p>691同一canonical cusp fibre φ_h(Ξ_5,9;14)：Tate整支撑/低偶权消失/q_h奇项全付。ℓ−1时κ=z−xy/2、κcusp=u_h³κΞ/4；self补项全消，六次幂同cusp判据与逐label密度准确，原abelian−1整支未反改。

[R1148 §§10–11](results/R1148-original-canonical-cusp-Heisenberg-and-minus-one-Frobenius.md)以已刊Soulé/Kurihara付p>C_cyc=exp(9^(224·9⁴))的全global H¹L3/5/9分别由原γ3/5/9生成。全部pairs=(aγ3,bγ5)，Θ与Ξ共享γ5的实际p⁵群给[M:Q]=(p−1)p⁵；共同cusp排除恰κΘ0/κΞ非零，密度1/p²。未宣loc_p单位，Bp−3/5/9局部门仍保。

R1148 §12付同一cover的rank-p character trace ψ(z−ab/2)、H¹维2p(g−1)，故 |N_t−#X/p|≤2(p−1)(g−1)√ℓ。全部中央值ℓ>p⁸时在affine上出现；共同cusp排除素ℓ>4D_p²（充分p⁸/144）仍有同一个affine点兼容全部labels并升Qℓ，D_p=g+p(p−1)(g−1)。继续小素真实值/p-local，不能再用大Chebotarev存在代affine空。

## O1：原两 jet、Gauss–Padé 与固定 Dixon

[R1137](results/R1137-original-Lame-conjugation-with-complete-boundaries.md)原Padé N=(p−5)/6，F=₂F₁(1/3,1/2;4/3)，contact2N+1首余项/P_N均unit。双缺陷⇔P,Q含x²，约后deg≤N−2/contact2N−1；F²=D_N−g_N²x^(2N+1)，D/G无重根互素，实际Pell余式W≠0、deg≤N−3但W0未unit。原Λ/rank3/moving p极与全部尺度沿文；双缺陷未排。

[原固定Dixon源](notes/2026-11-28-original-genus-four-Dixon-Jordan-chain.md)付 e=K4=0 iff D^(p−5)η=0 iff整P_(p−5)全系数被p整除。原2k Laurent块唯一核、两端单位及L∈{3k+1,3k+4,…,p−1}已付；单Jordan不代中列长度。§§6–8真实Fermat平移、D³=2vT与两生成式给r_N(λ)=R1076 η_k(λ/3)。Γ=(2v)^(2k)，q_N(0)=δr_N(0)/(2Γ)，e0时导数同比；r_N′(0)=ν_k/3。原Dixon逆σ_D的互倒平方根精确读全谱/相邻系数，分母<p，未删卷积或宣非同时零。

[R1145](results/R1145-original-Pade-banded-self-adjoint-exclusion.md)八个带宽1/2系统只有标量；四输入及run46071081257/job140747905385只排有限机制。旧5372素数扫描/R1134十五Euler列/Prym/六CM/normal-FM全部只消费，source和全常数保open/前态。o1继续真实Hesse变分时须保αD²/α²D及原主块边界。

## O2：原 Gaussian 全 good-mask 与共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md) p4k3且p|Bp−3时χ2 coarse一次unit只付跨盘；盘内须高度，余支p∤Bp−3。[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)线性多个非constant不代独立/注入。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)及[原重建](notes/2026-11-28-original-Gaussian-finite-contiguity-and-spectral-reconstruction.md)保gauge/高尾/mask，h≥1逆及Newton商/完整principal已付；h0不外推，Θ^p在SS非零。

[R1135](results/R1135-original-Gaussian-low-row-fiber-constraint.md)原两低good支至多一非对角pair，另一支Δ_low/48待unit；norm2完整V3/V4和CM gauge未删。§10两下降线真正运输给Π′(z′)=Π(−z′)，同component统一z∈Fp，保S0/P0。§11 actual-good代数仅A0=Fp[W²,W(W²−d)]或Fp[W]，导子W²−d；d0或非平方已分Fp点，非零平方须实际O_R(d)≠0。旧Δ/(2Gp−7)即该导子类；向量场闭性仍未付。

同文§12付3024Δ_low=(F∂²K−4K∂²F+aFK)(a,0)，原bad Bp−7支q阶1/2首系数unit，Gaussian取值仍开。

R1135 §13付原固定Δ曲线Y²=X³−Δ/27、∂X=2Y/∂Y=3X²；p11mod12导子p次零，p7mod12为明确Hasse单位×∂。bad Bp−7时原F/G/K/W极阶全准确，W最高系数−315/−243，指定Gaussian零⇔b²整除全权W。A_b/A_aa与F/G的准确cusp差已写出；Hasse值unit不能代真实K/W。继续原Cartier/forcing与实际good mask。

## 已成、禁止重做与其它入口

[R1125](results/R1125-original-full47-rational-point-classification.md)原完整47Q恰八CM，全部4513 whole盘/高度/全维来源和后到q²审计已成，不重跑47/41/旧端值窗口；run/hash沿原文/归档。

同h仍须本原/Legendre/fi gj实际mask。R971 full-span、R1006全p稳定已否，特定A/E4/mark未否；R948仅有限Abel零集，MW像可非零；原σ/cY、η_h、d/N、nonp/Poincaré/splitting不能删。R907原artifact真404，不据摘要重造；R1004导子下界不代高度上界。O3–6完整断点见open/归档。主标准未变，继续。
