# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：b074d70ff0d0689076713e125936c30cb916528b**（2026-11-28 00:33 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull 2026-11-27 01:48 Asia/Taipei；23:53重试执行器仍报无可用环境，shell未启动。按根规则8连接器同步、读diff、expected_sha非force提交，拒绝立即同步重基重推至成功；环境恢复立即pull --rebase。下一次真实尝试不晚于2026-11-28 00:53。令牌只CLI。数学程序仅本公开仓库Actions；本地/V8仅metadata/文本，不作数学计算。[此前偏差纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-unconditional-low-Cartan-block.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：一般 p；整平方层与实际 cochain

[R1003](results/R1003-global-scope-and-remaining-branches.md)保完整N_ns主范围。旧R317只在整j、K=Q(√−3)、σ1及二/三小域一致下使用；p2/5mod9还需小惯性C³。完整惯性、非整j、变化K/σ/异小域仍开。[最新primary范围](notes/2026-11-27-latest-primary-literature-scope.md)的条件开像/固定121不补一般p。

R1062–71已付全原cusp、étale/p-only、角色/phase/twists，无regular/Vandiver；原候选O(p^1.5logp)，有界惰性CM代表不推Q-CM，单cusp无Runge。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)给实际good维数≥floor(p/16)+3，forced-only Ω(p/logp)；总irregular预算完整T链不能改进1/16。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)付原圆单位同时非零密度(1−1/p)^d/(p−1)、localization、精确分歧/判别式及ℓ_faith≪p^(1215p−867−521r_min)，仍不够小/不付同点像。[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)原分母annihilator准确判据、−1modp整支相容。继续actual cochain/算术cup；几何Weil零不消HS混合项。

[原整K₂笔记](notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)：未分歧整K₂[p]/常数=μ_p⊗J(K)[p]，全cusp平均Δ分裂；even规范剩余为odd J。扩张0→ω^r→E→ω^(1−r)→0的radical是ω^(2−2r)，反向ω^(2r)，不是β_r。

[整p Chen/Ohta](notes/2026-11-27-original-prime-p-Chen-isogeny-and-odd-torsion-reduction.md)：真实Q上p单位同源J₂⁺→J_ns×J₀(p)，保整p∞/Hecke/Δ；Ohta arithmetic X₁(p)、N=1消J₀(p)(K)[p∞]⁻。odd障碍全在Fricke+平方层；LO又付Σ(p²)[p∞]=0。不能令Ohta N=p，不能把全部odd当Shimura，指定极化未付。

[R1131](results/R1131-original-square-level-Eisenstein-lattice-and-odd-torsion.md)：forced r=p−1−2j，若B_(4j+2)、B_(p−1−4j)均unit，Ca DVR/trace BC=m付原自由rank2格及实际非分裂方向。全块Fricke+，K有理odd p∞零；真实扭点域K(β_(4j+2)^(1/p))。规范K₂角色ω^(2j+2)零；p1mod4至少五块，p3mod8指定j=(p−3)/8无条件。只运输简单cuspline，不把二维socle当单射。

[R1132](results/R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md)：完整Y=X_ns(p)的真实低奇cuspline为w负；full第一Chen整同源及唯一new rank2/Schur迫全块负，原正商几何p-divisible块不存在。范围偶2≤r<(p−1)/2、B_(2r)B_(p+1−2r)unit。r2只需p∤B_(p−3)，遂消规范平凡Δ整K₂[p]。§8.1另付p7mod8的r=(p+1)/4无条件、K₂角色3(p+1)/4零；不删常数门前提。

[原整单位关系](notes/2026-11-28-original-integral-Manin-relations-and-cusp-constants.md)：angular specialization/全cusp平均用于整个p∞；实cusps使even有限p-primary tame全零。原Tate leading是S-unit，先e₀再平均，经K₂(Z[1/6p]) transfer消常数。因此R1132门内，原actual canonical unit符号格的已知有理平凡角色关系准确整提升。须继续给原整数指数/真实关系/低cochain；不除12p、不代任意K₂/p杯积或四阶cover。

### 固定47与来源审计均已完成

[R1125](results/R1125-original-full47-rational-point-classification.md)原完整X_ns^+(47)(Q)恰八CM。235坏盘/十good、283/4513同点、全非q高度含非整j及2/3、73维整QC、八完整盘唯一全付。§10后到q²run45977769585与交叉核46025141482/job140594489905全相容，四73维及16读数同；result SHA06c8bbd4fa4a437eaf3ce5b0fa2ce998c661329ca593fbb63c07352d92383173。全部source/hash/失败范围保正文。**不重跑固定47或审计。**

## O1：原 Picard 两 jet 与真实 Tate 族

[原Tate normal-FM](notes/2026-11-27-original-Tate-three-torsion-normal-FM-variation.md) §§1–11已付实际Verschiebung/Miller、kerV截面、−Q刚化与全自然奇源。6v·dot t̂=ΦN_full f，全H上6v·dot Ĵ_coeff=P_TJ，三平移6v·dot S=[P,S]，N_full+P=D²+U；原Pf=Nf+U^(m+1)。§8保Vε²约化项（旧错误草稿未发布）。

§9证明全V₀上ΦNΦ⁻¹不能是阶≤p−3目标微分算子，未排指定Um/−Q关系。§10付全dot A和6v·dot A=A(Nf,g)−A(f,Pg)，dot A(Ψ,Ψ)=δ/(6v)。原Um首normal×Picard一/四阶均零，normal零阶unit。

§11从同一3-cover得Prym商Y²=−(3x+ε)(x³+2v)，η|₀=−z/w、u+ν=−3dx/Y和相对F全保；原normal值恰等完整Hasse多项式，全ε^(3j+1)系数unit、首项回N14。固定C的Picard移动不保三挠，**不能当原e/K4共同非零**。o1继续真实vertical theta接口。

[原Lamé短旗标](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)保B简单谱/D³单Jordan、Green、normal列、全Cartier Newton矩阵、原R/移位R²及纯极反对角Φ。e₀0迫邻e单位，不代K4。原e/K4 iff短η_k/ν_k，R1077加权2k不代短k。

[R1130](results/R1130-original-inverse-center-recurrence-and-adjacent-unit.md)全WZ/短Ramanujan已成，真实邻项I_(n+2)+I_n=3δ/4只回旧单位；run46015627853/source4a0f6f21、证书9b825833…仅消费。[R1126](results/R1126-original-X108-complete-CM-Raynaud-pairing.md)六CM十五配对保A/S/T，Pfaffian不含原S；R1060非CM ordinary不推S。旧所有prime窗口至500000已成，不再扫描。

## O2：原 Gaussian mask / 共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)：p4k3且p|Bp−3时原χ=ω²出现，B₂good，coarse一次斜率−aβ₀⁴λ²/(20bχ)unit。只付跨盘；剩余可设p∤Bp−3，盘内仍需原高度。

[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)：constant iff ord_bG_v≥s，degree=(s−ord)/2；实际good非constant至少max{3,floor(p/96)+2}，渐近p/96+(log24/12)p/logp−O1。不推独立或共纤维唯一。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md) §§7–9保全Kronecker gauge/低乘积/高尾和mask；f_n=−Θ^nG_v/(n!(v)_n)，有限Möbius流给实际点对差(47)/(48)，weight≤p−3。Θ^p在SS为δ²∂w，不为0；不可横向微分某点对等式。o2继续实际masked共同纤维。

[R1114](results/R1114-original-Gaussian-adjacent-mixed-coefficient-unit.md)：5H+(8a²/45)K=16G_(p−3)unit；c₃保V₂/V₃/V₄完整卷积，B_(p−5)good/c₃unit未付且profile含i4。[norm2分布](notes/2026-11-27-original-Gaussian-norm-two-Kronecker-distribution.md)全部twists/相位/平方根/低项保留。

## 其它实际边界

原同h=6i+7须本原/Legendre/fi gj两mask同时满足；R971full-span和R1006全p稳定已否，特定A/E4/原mark仍开。R1009粗CM阶≤4不代零阶。

[R1095](results/R1095-original-theta-kernel-dual-Psi-normalization.md)全J#可逆、B_J(Ψ,Ψ)=1、最高边界/三平移Gram/fullFay/FSF/Miller皆保；Φ(SΨ)=(V+v)(2vΨ−δU)/U²不代指定短配对。R988全部phase/carry/共振与本原门，R1041/48 bare范数和AS端点平方边界仍在。

原MW后M1、λ=−6(b+1)/r、最低w/deep盘整尺度及野3障碍沿归档；R696/832仅指定Ω，R948仅两有限Abel零集，一般候选MW像可非零。旧R907四artifact真404不重造；R707主41，R1004仅导子下界。主完成标准不变。
