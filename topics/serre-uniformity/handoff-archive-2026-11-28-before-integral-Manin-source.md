# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：d213b696c828d16c2fa96d4d334c58ab22800a3f**（2026-11-28 10:32 Asia/Taipei；连接器同步main，两README差异已核；最近真实pull 2026-11-28 09:54 Asia/Taipei，Actions）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull：2026-11-28 09:54:17 Asia/Taipei，Actions run46095394596/job140825442860，blob:none浅clone后真实pull --rebase至254139af；两README diff空且全文hash同；[回执](notes/2026-11-28-terminal-rule-sync.md)。下次请求≤10:44、pull≤10:54。本地09:55仍无环境，恢复即pull。提交均fresh main/diff/expected_sha非force，拒绝立即同步重推；令牌只CLI。数学仅本公开Actions，V8仅metadata/文本；[此前纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-integral-four-line-source.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：完整一般 p、原算术 cochains 与新增尖点中心

[R1003](results/R1003-global-scope-and-remaining-branches.md)保full N_ns；R317整j/固定K/σ1/二三小域/小惯性C³未全关。R1128 good≥floor(p/16)+3、forced Ω(p/logp)、候选O(p^1.5logp)，不以惰性CM推Q-CM；R1112小aux仍大。R1115原abelian−1整支保留。

[R1131–40](results.md)完整门沿open/前态；原class4全四cusp矩/phase、radical角色与已付端点不改，不重扩扫描。

[R1133 §11](results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)付原D(α)同根路径的完整算术五项cochain：h=χ̃2+ab、h−ab/2=−li2、dh=−a∪b，五项交替和=ρ1−ξρ1−η。bar Cor逐陪集乘积全保，不变成两个Norm之积。实际全M目标的Manin/pushout和下降仍须付；R1156已付固定配置raw源的内点延伸，未套小开集H¹0。

[R1143–44](results.md)原Eisenstein单位及proper修正杯积已付，全部transfer/HS/polar尺度沿文；未修正非零socle及MW d0/1仍保。

[R1146](results/R1146-original-proper-arithmetic-Heisenberg-cover.md)原proper Heis p³、满几何像及全部cusps/ℓ≠p含2、3已付。B8中心H¹/H²0给唯一global lift；twists=J(K)[p]ω⁻⁷，B16门仍保。

[R1147](results/R1147-original-canonical-moment-Heisenberg-lift.md)全S0兼容整塔/规范proper Heis/原theta尺度及未分歧43格FL已付。§16：同原quotient的真实兼容generic整塔在全部noncusp自动补点（Z∞(−1)权−14），唯一识别原P∞；须相容整cocycle，不从单层/rational lift推出。指定filling仍构造中，Cartan I仅modp。

[R1149–50](results.md)原43塔Hodge截面、E6/E10连接、中央连接0、log Frobenius完整次序与Tate a5=u5已付；horizontal period gauge/proper-log下降/H¹etZ0锁同塔。完整u=pt整Taylor、finite q_t/λ/binomial、原CM β参数沿文；Gaussian/cubic粗次数1/2/3、1/1/2，cubic首斜率unit。Cartan仅modp，整未分歧短盘范围与最高中央F0边界保留。

[R1151](results/R1151-original-finite-Frobenius-global-subtraction.md)付H¹(Qp,Heis)↔Fp³的实际finiteFL坐标。p>Ccyc全global像(rx,sy,zxy)，s=T0；零r/s完整七分支保文。rs非零时真实障碍rs h−zab；Gaussian顶为16δ³c_g⁶(rs z12−z x4y8)，cubic顶为16δ³c_g⁶(rs z12−z λA*y7/6)。首数字0只迫u∈p²，不冒whole盘排点；继续实际两个中央组合。

[R1148](results/R1148-original-canonical-cusp-Heisenberg-and-minus-one-Frobenius.md)同一Ξ5,9;14 cusp、完整奇项/六次label及原abelian−1整支已付。已刊Soulé/Kurihara给p>Ccyc=exp(9^(224·9⁴))的原γ3/5/9全global基，局部Bp−3/5/9单位不外推；Θ/Ξ共享γ5、p⁵群与密度1/p²全保。大Chebotarev同时存在affine lift，不能代affine空，继续小素/p-local。

R1152 §§1–13付原Θ∞/MT(Z)、全尾/词表及绝对有限读数：β3=Bp−3、β5=Bp−5、J=Har_p(1,3,4)，r=2β3/3、s=24β5/5、z=48(J+2β3β5)/25。原c3/c5、七退化支/完整中央减法沿文。rs非零κ=6/5+3J/(5β3β5)，原F0最高组合与深盘仍开。

[R1153](results/R1153-original-Kummer-to-Fontaine-Laffaille-calibration.md)付原Q1/Q2→finiteFL的U/U²、实际Miller phase、全部可见x2..4/y4..8及Gaussian x4/y8、cubic y7。generic Fp SS存在范围取max(C_SS,C_cyc)，全尺度/β参数沿文；U★γ★⁻²仅β3好或p4k3且β5好时恰1，两β坏不外推，z12仍开。

[R1155 §§1–10](results/R1155-original-primitive-dilogarithmic-Frobenius-readout.md)原D/rev/BK、强mod pO_L有限dilog及SS单位已付。§8 v=u^p+pε完整右运输保h=−ℓ2/(1−u^p)−ε²/{2u^p(1−u^p)}；§9全S3。§10同一五点配置的五个ε由两个base误差实际生成，Σalt h=e_Ce_D/(CD)、Σalt BCH=0，保全部carry/nilpotents。任意分歧仅fibres间运输；未分歧v=σu才actual同点。原filling/逐coset transfer/moment与F0 z12继续，不套ramified FL。

[R1156](results/R1156-original-four-line-integral-cochain-and-transfer.md)付原三除子的有限四线整cochain：根相位dρ、全部常数/一般位置、prime-to-p辅助域及显式Cor–res同伦均保。固定函数p∞根塔与E[pⁿ] moment分布严格区分。Δ^(c²−1)h_c¹²是真全局单位；raw完整Zp(2)塔在全部noncusp内点惯性因H⁰(k,Zp(1))0消去，可先延伸再modp。ordered尺度保−12(c²−1)d(DT)，不误删相位/correlation。实际指定B_n的raw bilinear pushout、GL2/Weil/算术下降和原交换商规范仍须付，之后才在原M用H¹Z₁0识别。

## O1：原两 jet、Gauss–Padé 与固定 Dixon

[R1137](results/R1137-original-Lame-conjugation-with-complete-boundaries.md)原Padé N=(p−5)/6，F=₂F₁(1/3,1/2;4/3)，contact2N+1首余项/P_N均unit。双缺陷⇔P,Q含x²，约后deg≤N−2/contact2N−1；F²=D_N−g_N²x^(2N+1)，D/G无重根互素，实际Pell余式W≠0、deg≤N−3但W0未unit。原Λ/rank3/moving p极与全部尺度沿文；双缺陷未排。

[原固定Dixon](notes/2026-11-28-original-genus-four-Dixon-Jordan-chain.md)§§1–10付D^(p−5)η、原Fermat/同Dixon生成式、Hesse全Frel/Schur谱。normal=12tr(adjQ A²)不等spectral=tr(adjQ)，全Jordan不代指定中列；原双零未排。R1145八带系统仅标量、旧5372/十五Euler/Prym/六CM/normal-FM均只消费，不重跑。

[原genus4 §§6–11](notes/2026-11-28-original-genus-four-global-Raynaud-vanishing.md)完整Fermat45槽、七维0…4插入/K4、primitive交换及A3/A9回Dixon已付；同一E*的Λ/σ与全部相位沿文。§11付六点主部的κ–Serre对角单位及真实有限Thomae，全部九三元组的三张量在Fp²全交替；九mixed槽合为一参数。原尺度新闭e=δS_n/(ρs)、S_n=−9ρ²A_orig，不除共同值。σ/Λ、mixed/123循环系数及原T仍未unit；高插入与指定e/K4非同时零继续，不由三形式radical/Serre perfectness推非零。

## O2：原 Gaussian 全 good-mask 与共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md) p4k3且p|Bp−3时χ2 coarse一次unit只付跨盘；盘内须高度，余支p∤Bp−3。[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)线性多个非constant不代独立/注入。

R1116及原重建的gauge/高尾/mask、h≥1逆与Newton商已成，h0不外推；完整来源沿open/归档。

[R1135 §§1–17](results/R1135-original-Gaussian-low-row-fiber-constraint.md)两下降线Π′(z′)=Π(−z′)统一z∈Fp；actual-good代数A0=Fp[W²,W(W²−d)]或Fp[W]，导子W²−d，d0/非平方分Fp点，非零平方余对须actual O_R(d)。原heat/Hasse/Katz、finiteGauss全部坏行/安全jet/余项付；Δ_low=8(3bc−td)/(4455rβ²)，Q⁶顶unit不代det，向量场闭性仍未付。原norm2/CM gauge/两twist与全尺度保文。

R1154 §§1–12付同源Legendre/finite-log全部carry、三移位核与真实Newton算子。H_p0锁q=Qν，minor保Cν(q)+(3/8)Bp−3D2。新Actions run46094809839以p1019否定无条件Cν(Qν)=0，未满足q=Q；[回执](notes/2026-11-28-new-weighted-Legendre-probe.md)，不扩扫。§12付T E(T+1)+(T+1)E(T)=−2(T^p−T)；原D_(S,P)算子Z_D在全good相等时缺至T^(2k+4)、顶15Gp−3/8单位，前两项恰原H_p/Δ_low。缺项本身非矛盾。spectral §10付被删完整C_pr=Σa_(k+1−h)b_(h−1)/(2h)!，含全部低行；其Euler核恰−(R^p−R)，不推C_pr或b_k零。继续真实二根D与差分，保全部mask。

## 已成、禁止重做与其它入口

[R1125](results/R1125-original-full47-rational-point-classification.md)原完整47Q恰八CM，全部4513 whole盘/高度/全维来源和后到q²审计已成，不重跑47/41/旧端值窗口；run/hash沿原文/归档。

同h仍须本原/Legendre/实际mask；full-span/全p稳定已否，特定A/E4/mark未否。原σ/cY、η_h、d/N、nonp/Poincaré/splitting不能删；R907 artifact真404不据摘要重造。O3–6沿open/归档；主标准未达，继续。
