# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：468c8a40bd07b72998cbb9199b7c95b2a6a72e57**（2026-11-28 01:54 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull 2026-11-27 01:48 Asia/Taipei；01:47重试执行器仍报无可用环境，shell未启动。按根规则8连接器同步、读diff、expected_sha非force提交，拒绝立即同步重基重推至成功；环境恢复立即pull --rebase。下一次真实尝试不晚于2026-11-28 02:47。令牌只CLI。数学程序仅本公开仓库Actions；本地/V8仅metadata/文本，不作数学计算。[此前偏差纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-original-p-configuration.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：一般 p；整平方层与实际 cochain

[R1003](results/R1003-global-scope-and-remaining-branches.md)保完整N_ns主范围。R317附加整j/K=Q(√−3)/σ1/二三小域，p2/5mod9还需小惯性C³；其余全范围未关。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)付原good≥floor(p/16)+3，forced-only Ω(p/logp)，预算完整T链不改1/16。原候选O(p^1.5logp)、有界惰性CM代表不推Q-CM，单cusp无Runge。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)付同时非零/localization与准确导子判别式，ℓ_faith≪p^(1215p−867−521r_min)仍不够小。[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)付分母annihilator判据，−1modp整支仍相容。几何Weil零不消HS混合项。

[原整K₂](notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)给未分歧K₂[p]/常数=μp⊗J(K)[p]，全cusp平均Δ分裂；even残余落odd J。[整p Chen/Ohta](notes/2026-11-27-original-prime-p-Chen-isogeny-and-odd-torsion-reduction.md)付真实同素数p单位同源，N=1消旧odd，剩余在Fricke+平方层；Σ(p²)[p∞]=0不消非Shimura odd。扩张0→ωr→E→ω1−r→0的radical是ω2−2r，非βr。

[R1131](results/R1131-original-square-level-Eisenstein-lattice-and-odd-torsion.md)：forced r=p−1−2j、B_(4j+2)B_(p−1−4j)unit时，Ca DVR/trace BC=m锁实际非分裂rank2格，全块Fricke+且odd K有理p∞零，扭点域K(β_(4j+2)^(1/p))；规范K₂角色2j+2零。p1mod4≥五块，p3mod8指定j无条件；仅运输简单socle。[R1132](results/R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md)：full Cartan低奇cuspline迫全块w负，原正商相应几何p块不存在；偶2≤r<(p−1)/2及B_(2r)B_(p+1−2r)unit时规范K₂角色2−r零。r2只需p∤Bp−3，p7mod8指定低偶r由二次类数无条件；不代K₂/p。

[原整单位关系](notes/2026-11-28-original-integral-Manin-relations-and-cusp-constants.md)仅将原符号格的已知有理平凡角色关系整提升：实cusps消even torsion tame，原S-unit常数先e₀/平均后transfer消去。R1132门前提与真实rational关系不能删，不除12p。

[R1133](results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)：实际A+B=1的half Cartan加权范数以dχ(a)=Δ²χ(t²)|a−Δ²χ(t²)|2恢复每个原Vχ，偶根数付可逆a，保leading。原杯积保crossed Cor，常Lie中心读K₂/p的ω²而非e₀。§9同一Norm见证给p⁵/class4塔与(a,a,a,b)；cusp iff四moment全零，赋值向量∈(σ−1)^4，Norm只控M0。§10 Fourier/λp相位精确交换同一Heis商，真纤维积保两三阶/p⁵和两极端四阶/p⁷；混合四阶零。forced双字母指标已给，原见证/算术下降未付。

[原aux-c整Manin](notes/2026-11-28-original-auxiliary-c-torsion-Manin-correlation.md)：真实K₃残数付Ψc的整三项式，含t0阶c²−1；双κ可同选奇c<p为unit且辅助域度p单位。§7再用实际R_a(T)=∏(xT−xi)^ai、O值1及第二K₃，完整Cor移回原p点：𝒫=2c²{M_a,M_b}−2c⁴C_ab，C_ab=Σi<j(ai bj−bi aj){(xi−xj)/d0,hi/hj}。两次{-1,h}成对整消，C的排序仅二扭；所有cross权保留。须继续指定原Manin组合/配置项，不把它设零或改成c⁴−[c,c]。个别hc有Hodge权，augmentation后才真权零。

### 固定47及全部来源审计已完成

[R1125](results/R1125-original-full47-rational-point-classification.md)原完整X_ns^+(47)(Q)恰八CM；全部标签/非q含2/3/73维QC/八whole4513盘已付。§10独立全维核run46025141482/job140594489905与原q²全相容，result SHA06c8bbd4fa4a437eaf3ce5b0fa2ce998c661329ca593fbb63c07352d92383173。**只消费，不重跑固定47或审计。**

## O1：原 Picard 两 jet / 真 Tate 族

[原Tate normal-FM](notes/2026-11-27-original-Tate-three-torsion-normal-FM-variation.md) §§1–15保实际Verschiebung/Miller、kerV/−Q刚化、全自然基P/N连接。6v·dot t̂=ΦN_fullf，6v·dotĴ=P_TJ，6v·dotS=[P,S]；全V₀低阶目标共轭已排，指定Um未排。首normal×Picard一/四阶零，normal零阶unit。

真实三挠cover η=−z/w给Prym Y²=−(3x+ε)(x³+2v)、θ完整Hasse和rank2 Gauss；θ=θ′0·ε₂F₁(1/2,5/6;4/3;ε³/(54v))到k−1，保−3dx/Y、cup1/(9v)、period安全<p/共振p+1。全族Dε^p=HεDε、DεΨε=HεU−βε、加律M^p−HεM。§14保6v·dotR=δ/2−U²Ψ/V−S_(p−3)，S全二次和/常数；Ψε(Q)=(εH−ε^p)/6与二阶全付。

§15固定Prym x³+3xr²+2v=0：Ξ=Ψ(u−ν)=d(xR/r)+3v(R/U)ωP，Υ=−3R²ωP，CΞ=3eωP′、CΥ=−3K4ωP′。proper高极p次自由项按CM权排，两类同ζ线，zero分别iff原读数zero。完整Fermat矩L0..k−1 units、Lk..2k−1=0，e=vΣr_iL_i、K4=Σr_ir_jL_(i+j+1)。**原两和非同时零仍开**，不能用rank2完美性/moving三挠normal代fixed Picard；继续实际primitive/普通连接。

[原Prym三同源/trace](notes/2026-11-28-original-fixed-Prym-three-isogeny-and-trace.md)：τ(A,B)=(ζA,ζ²B)自由，q=r²−x²,w=r³+3rx²给真实3-isogeny φ=(q/ρ²,w/2)到同一原E；φ*ωE=−3ρ⁻²ωP。有限Newton trace完整给A*=Tr(R/r²)/3、B*=TrR²/3，准确Cartier读e/v、K4；顶项分别3ρ⁻² U^(m−1)、U^(p−1)。proper类的φ*/φ*trace尺度已付，最高项/同源p单位不代原共同非零。

[原Lamé续稿](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)保短旗标/Green/全Newton矩阵/纯极Φ，e0零迫邻e单位不代K4。[R1130](results/R1130-original-inverse-center-recurrence-and-adjacent-unit.md)真实邻项只回旧δ单位，run46015627853仅消费。R1126六CM十五配对保A/S/T，Pfaffian不含S；R1060非CM ordinary不推S。旧素数窗口至500000已成，不重扫。

## O2：原 Gaussian mask / 共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)：p4k3且p|Bp−3时原χ2 good且coarse一次斜率unit，只付跨盘。剩余p∤Bp−3；盘内高度仍需原来源。[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)：constant iff ord_bG_v≥s，degree=(s−ord)/2，非constant≥max{3,floor(p/96)+2}；不推独立/纤维唯一。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)§§7–9保全gauge/低卷积/高尾和mask，f_n=−Θ^nG_v/(n!(v)_n)、有限Möbius流及实际点对差(47)/(48)，weight≤p−3。Θ^p在SS=δ²∂w，不为零；不横向微分单点对等式。继续原去对角差商/Fay。
R1114保全部V₂/V₃/V₄，5H+(8a²/45)K=16G_(p−3)unit不代c₃；Bp−5 good未付。原norm2分布全twists/相位/低项保留。

## 其它实际边界

同h须本原/Legendre/fi gj两mask同满足；R971 full-span、R1006全p稳定已否，特定A/E4/mark仍开。R1095全核完美性/Gram/Fay/FSF不代指定短配对。旧MW/高度、lowest/deep整尺度、野3/非p/Poincaré/splitting沿逐字归档；R948仅两有限Abel零集，候选MW像可非零。R907原artifact真404不重造；R707主41已成、R1004仅导子下界。主完成标准不变。
