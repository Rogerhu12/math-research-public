# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：e210c40591aff9a7e8d273f84adff645529baf76**（2026-11-28 01:41 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull 2026-11-27 01:48 Asia/Taipei；00:50重试执行器仍报无可用环境，shell未启动。按根规则8连接器同步、读diff、expected_sha非force提交，拒绝立即同步重基重推至成功；环境恢复立即pull --rebase。下一次真实尝试不晚于2026-11-28 01:50。令牌只CLI。数学程序仅本公开仓库Actions；本地/V8仅metadata/文本，不作数学计算。[此前偏差纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-auxiliary-c-Manin.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：一般 p；整平方层与实际 cochain

[R1003](results/R1003-global-scope-and-remaining-branches.md)保完整N_ns主范围。旧R317只在整j、K=Q(√−3)、σ1及二/三小域一致下使用；p2/5mod9还需小惯性C³。完整惯性、非整j、变化K/σ/异小域仍开。[最新primary范围](notes/2026-11-27-latest-primary-literature-scope.md)的条件开像/固定121不补一般p。

R1062–71已付全原cusp、étale/p-only、角色/phase/twists，无regular/Vandiver；原候选O(p^1.5logp)，有界惰性CM代表不推Q-CM，单cusp无Runge。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)给实际good维数≥floor(p/16)+3，forced-only Ω(p/logp)；总irregular预算完整T链不能改进1/16。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)付原圆单位同时非零密度(1−1/p)^d/(p−1)、localization、精确分歧/判别式及ℓ_faith≪p^(1215p−867−521r_min)，仍不够小/不付同点像。[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)原分母annihilator准确判据、−1modp整支相容。继续actual cochain/算术cup；几何Weil零不消HS混合项。

[原整K₂笔记](notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)：未分歧整K₂[p]/常数=μ_p⊗J(K)[p]，全cusp平均Δ分裂；even规范剩余为odd J。扩张0→ω^r→E→ω^(1−r)→0的radical是ω^(2−2r)，反向ω^(2r)，不是β_r。

[整p Chen/Ohta](notes/2026-11-27-original-prime-p-Chen-isogeny-and-odd-torsion-reduction.md)：真实Q上p单位同源J₂⁺→J_ns×J₀(p)，保整p∞/Hecke/Δ；Ohta arithmetic X₁(p)、N=1消J₀(p)(K)[p∞]⁻。odd障碍全在Fricke+平方层；LO又付Σ(p²)[p∞]=0。不能令Ohta N=p，不能把全部odd当Shimura，指定极化未付。

[R1131](results/R1131-original-square-level-Eisenstein-lattice-and-odd-torsion.md)：forced r=p−1−2j、B_(4j+2)B_(p−1−4j)unit时，Ca DVR/trace BC=m及实际偶cuspline锁非分裂rank2格。全块Fricke+，K有理odd p∞零，扭点域K(β_(4j+2)^(1/p))；规范K₂角色2j+2零。p1mod4至少五块，p3mod8指定j=(p−3)/8无条件；只运输简单socle。

[R1132](results/R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md)：full Cartan真实低奇cuspline为w负；full整p Chen/唯一new rank2/Schur迫整块负，原正商该几何p块不存在。偶2≤r<(p−1)/2、B_(2r)B_(p+1−2r)unit时规范K₂角色2−r零。r2只需p∤Bp−3而消平凡整torsion；p7mod8的r=(p+1)/4由二次类数无条件。不能替代K₂/p杯积。

[原整单位关系](notes/2026-11-28-original-integral-Manin-relations-and-cusp-constants.md)：全cusp angular平均处理p∞；实cusps消even有限p-primary tame。原Tate leading S-unit先e₀再平均，经K₂(Z[1/6p]) transfer消常数。R1132门内仅将原actual unit符号的已知有理平凡角色关系整提升；还须真实关系/低cochain，不除12p，不代任意K₂/p。

[R1133](results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)：实际坐标差A+B=1及half Cartan加权范数，以dχ(a)=Δ²χ(t²)|a−Δ²χ(t²)|2准确恢复每个原Vχ；原两个缺席边界/偶根数付可逆a，保leading、不取12p幂。原范数杯积须保完整跨轨道Cor，常Lie中心读K₂/p的ω²，不是e₀整torsion。§9从同一Norm单位见证给阶p⁵/class4真塔及UT5首层(a,a,a,b)；cusp iff四赋值矩全零，即n∈(σ−1)^4，Norm只付M0。四种p mod8均有forced双字母指标，原见证未付。§10完整Fourier单位和/λp相位精确识别交换两槽的同一Heisenberg商，真纤维积给p⁵的两三阶方向及p⁷的两极端四阶方向；混合四阶仍零，proper/原不同角色下降仍开。

[原aux-c整Manin](notes/2026-11-28-original-auxiliary-c-torsion-Manin-correlation.md)：真实K₃残数给Ψc(P,Q)=c²{hcP,hcQ}−Σ_t Cor{hc(P+t),hc(Q−t)}的整三项式，含t0阶c²−1。原双权重首项为4c²κχκψ/m²·{Fχ,Fψ}；任何实际两角色可同选奇3≤c<p使κ均unit/aux field度p单位。原same-t相关mask及指定Manin组合仍待付；个别hc有Hodge权，只有augmentation乘积真权零。

### 固定47与来源审计均已完成

[R1125](results/R1125-original-full47-rational-point-classification.md)原完整X_ns^+(47)(Q)恰八CM；全部global标签/非q项/73维整QC/八whole4513盘已付。§10后到q²与独立全维核对全部相容：run46025141482/job140594489905，result SHA06c8bbd4fa4a437eaf3ce5b0fa2ce998c661329ca593fbb63c07352d92383173。**固定47及来源审计均已完成，不重跑。**

## O1：原 Picard 两 jet 与真实 Tate 族

[原Tate normal-FM](notes/2026-11-27-original-Tate-three-torsion-normal-FM-variation.md) §§1–15保原Verschiebung/Miller、kerV/−Q刚化、全自然基及P/N连接。6v·dot t̂=ΦN_fullf，6v·dotĴ_coeff=P_TJ，6v·dotS=[P,S]；§9排全V₀低阶目标共轭，不排指定读数。§10全dot A及dotA(Ψ,Ψ)=δ/(6v)；Um首normal×Picard一/四阶零，normal零阶unit。

§§11–12真实三挠cover相位η=−z/w给Prym Y²=−(3x+ε)(x³+2v)、原θ完整Hasse/rank2 Gauss；θ=θ′0·ε₂F₁(1/2,5/6;4/3;ε³/(54v))到k−1，保−3dx/Y、cup1/(9v)、period安全<p及首共振p+1。§13全族Dε^p=HεDε、DεΨε=HεU−βε、加律M^p−HεM。§14保6v·dotR=δ/2−U²Ψ/V−S_(p−3)，S全二次和/常数及最高项相消；Ψε(Q)=(εH−ε^p)/6与二阶导数全付。

§15固定同一Prym x³+3xr²+2v=0：Ξ=Ψ(u−ν)=d(xR/r)+3v(R/U)ωP，Υ=−3R²ωP；CΞ=3eωP′，CΥ=−3K4ωP′。高极proper类的p次自由项由原CM权排除；两类同ζ线，分别zero iff原读数zero，不能用rank2配对。L_j=C(r^(6j+2)ωP)/ωP′完整Fermat初值/递推付L0..k−1 units、Lk..2k−1=0，e=vΣr_iL_i、K4=Σr_ir_jL_(i+j+1)。**原两和非同时零仍开**，继续实际primitive消元；moving三挠normal不代fixed Picard。

[原Lamé续稿](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)保短旗标/Green、全Newton矩阵/纯极Φ，e0零迫邻e单位不代K4。[R1130](results/R1130-original-inverse-center-recurrence-and-adjacent-unit.md)真实邻项只回旧δ单位；run46015627853/source4a0f6f21、证书9b825833仅消费。[R1126](results/R1126-original-X108-complete-CM-Raynaud-pairing.md)六CM十五配对保A/S/T，Pfaffian不含S；R1060非CM ordinary不推S。旧所有素数窗口至500000已成，不重扫。

## O2：原 Gaussian mask / 共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)：p4k3且p|Bp−3时原χ=ω²出现，B₂good，coarse一次斜率−aβ₀⁴λ²/(20bχ)unit。只付跨盘；剩余可设p∤Bp−3，盘内仍需原高度。

[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)：constant iff ord_bG_v≥s，degree=(s−ord)/2；实际good非constant至少max{3,floor(p/96)+2}，渐近p/96+(log24/12)p/logp−O1。不推独立或共纤维唯一。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md) §§7–9保全Kronecker gauge/低乘积/高尾和mask；f_n=−Θ^nG_v/(n!(v)_n)，有限Möbius流给实际点对差(47)/(48)，weight≤p−3。Θ^p在SS为δ²∂w，不为0；不可横向微分某点对等式。o2继续实际masked共同纤维。

[R1114](results/R1114-original-Gaussian-adjacent-mixed-coefficient-unit.md)：5H+(8a²/45)K=16G_(p−3)unit；c₃保V₂/V₃/V₄完整卷积，B_(p−5)good/c₃unit未付且profile含i4。[norm2分布](notes/2026-11-27-original-Gaussian-norm-two-Kronecker-distribution.md)全部twists/相位/平方根/低项保留。

## 其它实际边界

原同h=6i+7须本原/Legendre/fi gj两mask同满足；R971 full-span、R1006全p稳定已否，特定A/E4/原mark仍开。R1095保全J#、三平移Gram、全Fay/FSF/Miller及最高边界，完美性不代短指定配对；R988全phase/carry/共振、本原门及R1041/48 bare端点仍在。

旧MW/高度、lowest/deep整尺度、野3/非p/Poincaré/splitting沿逐字归档；R696/832仅指定Ω，R948仅两有限Abel零集，候选MW像可非零。R907原artifact真实404不重造；R707主41已成、R1004仅导子下界。主完成标准不变。
