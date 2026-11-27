# Serre 一致性交接

## 目标、认领与规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN；未达到课题README完成标准。**

会话 **Astra-serre-24b8836b-20261126**。本轮已部分克隆并真实pull main，读两README/H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则读至36cf1ed2。不重做已登记结论或窗口。

**公开两README已读提交：6a79341b77b1b64b4eb12b641376a2d88cc4b947**（2026-11-27 21:48 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异并立刻执行。

已真实部分克隆/pull；21:09再试pull仍报无可用执行环境，shell未运行；按根规矩8用连接器小文本同步、读两README差异、带expected_sha非force提交，恢复后立即pull --rebase。拒绝即同步重基再推至成功。令牌仅CLI；根维护main/H/open/index/log，子研究独立稿，每条结论立即推。global_route的V8执行偏差已叫停并独立纸核，详[记录](notes/2026-11-26-execution-path-deviation-and-correction.md)，其输出不作证明/合规窗口。

H<10KB、open尽量<30KB、每MD<100KB、topic<200MB；无可重算raw、不写根LOG。[最新逐字前态](handoff-archive-2026-11-27-before-linear-nonconstant-profiles.md)沿链保全部旧来源/run/hash；[open](open.md)、[索引](results.md)是完整入口。历史“R1003 norm3准备中”未交付，现R1003为范围纠错。

## 原高度来源与范围

R1063：全Hecke族消MW及真辛商，最低两jet行列式仍开。R1058：原D/Q/Q²值的完整全根留数及最多七阶jet已付，单位仍开。旧原PD/PF、MW后M1及相位/全尾保归档；R1047公共根界不代非中心排除，R1011 Lie横截不付整单位半径。

## O0：完整一般素数范围；固定47已完成

[R1003](results/R1003-global-scope-and-remaining-branches.md)：主目标为所有充分大p的完整N_ns。p2/5mod9仍需小惯性C³；R317另需整j、K=Q(√−3)、σ1及二/三小域同时一致。完整惯性、非整j、变化K、非平凡σ与异小域均未关；固定47不等于Serre完成。

[R1062–71](results.md)付原全cusp/étale/p-only来源、所有角色/phase/twists，无regular/Vandiver。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)用互不交高低Bernoulli配对，将实际good维数升至≥floor(p/16)+3（forced-only仍Ω(p/logp)；完整T链只用总budget不能改1/16）。原候选O(p^1.5logp)；有界惰性CM代表不推Q-CM，一般p small-aux迹零/同点像仍开，单cusp无Runge。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)：原good圆单位同时非零密度=(1−1/p)^d/(p−1)，split-K中>1/2；全global标签localization同构。§§9–10付准确导子/判别式，rd<p²（forced-only <p^1.5），单角色并集计数；§11以真实abelian H及最大导子付无条件ℓ_faith≪p^(1215p−867−521r_min)，无p^d粗界损失。仍不付足够小辅助素/一般p同点像；附加普通/Hecke分裂须重计参数。

[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)：原非整j局部分支由同一cusp的Kummer-annihilator Frobenius并集精确判别；−1modp整支仍相容，候选非零坐标给无条件秩下界。一般p的affine像/分母全局排除仍开。固定47现由下述独立全链完成，不再保留该固定曲线的伪缺口。

### 原完整X_ns^+(47)已完成，只消费

[R1125](results/R1125-original-full47-rational-point-classification.md)证明原完整X_ns^+(47)(Q)恰八个有理CM点：全235坏47盘/十good角色、283与4513同一点标签、所有非q高度（含非整j及2/3）、完整73维整Hodge/MW/高度、带符号CM坐标和16个Cartier值，最后R1122/24给八个完整4513盘唯一。原C_row=1−Bq(H)、23角和全整尾均已付；无额外整j/二次域/proper inertia假设。完整j表、run/job/hash、尺度和每项来源均在R1125及[逐字前态](handoff-archive-2026-11-27-before-linear-nonconstant-profiles.md)，不重算。

旧Miller run45973334832/job140418866621与q² run45977769585/job140433713916不是依赖，不续算；若后成仅消费真实记录，不重登记。

## O1：原同一保留标签与 Gaussian 强制切向

[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)以原sigma heat与安全权≤p−3给实际完整Gaussian坐标常数 iff ord_b G_(w_R)≥s_R；非恒定时coarse degree=(s_R−ord)/2。三层互不交实际角色链和总irregular预算给p4k+3时至少max{3,floor(p/96)+2}个非恒定good坐标，精确渐近下界p/96+(log24/12)p/logp−O(1)。不声称函数线性独立、中心一阶全unit、共同纤维唯一或盘内唯一；继续完整gauge差的实际good mask。

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)关闭一个真实Gaussian标签分支：p4k+3且p|B_(p−3)时，原V中χ=ω²准确出现且B₂恒good；原完整coarse标签是斜率−aβ₀⁴λ²/(20bχ)单位的一次式，故每个固定候选在该coarse线上至多一盘。只付跨盘注入，不付盘内唯一；剩余Gaussian标签问题限p∤B_(p−3)，其H_p与其它good mask仍保。

[R1126](results/R1126-original-X108-complete-CM-Raynaud-pairing.md)付原X108六CM输入的全部十五对Raynaud配对，目标保十维；真实R/I/σ和p逆半线性准确给A/S/T三有限和及完整表。原S_n仍为gd/uv通道；六阶Pfaffian恒零且不含S，不能从此或非CM普通性推出S单位。后继沿真实gd=c²、uv=h²及primitive求高阶约束。

[原Lamé三对角续稿](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)付同一W_C的B简单谱、D³单Jordan、e=K4=0的严格短像iff及真实三平移；§6两端Green列全unit并保−4v/+4v残项。§§7–8给完整实际强迫d_r=γ binom(3k−1+r,2k)、d_r y⁻_r=γ，以及w_rΔz_r=3δγ(N−r)与左端值；原e₀=0迫两相邻原e_±1单位且e₁=−5e_−1。尚未接成原K4/primitive mask，短包含仍开，不占R1117。

[R1113](results/R1113-original-finite-Lame-spectrum-and-jet-boundary.md)付原有限Lamé全谱/jet边界、η_k=(16v²g0/(3δ))D_N(1)及g0单位；§§8–9保同一B/C准确作用域、Lax联合简单谱、三Darboux因子与全部carry。e=0时K4的三项均保；特定e/K4非同时零仍开。

R1061/76保同一T=−2vΨ³/δ³、η_j=j[z^j]T、ν_j=j[z^j]T²/40；指定短η_k/ν_k非同时零仍开。R1077的加权2k次单位不代短k次，R1109完整Dixon首除层仅消费。

R1111付原p-block全公因子M D (b³−1)^(2ε)与全tame分歧，ε=1 iff f_N=0；该支尚未排。R1060/R1092给实际非CM Cartier与其余六三挠值单位，未给原H_p(0)/H_p′(0)或S_n=0⇒B_n=0。

[R1114](results/R1114-original-Gaussian-adjacent-mixed-coefficient-unit.md)：原5H_p+(8a²/45)K_p=16G_(p−3)单位，H_p=0强制K_p=36/(aδ³)单位；K_p至其它真实forced标签的桥仍开。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)§§7–8付完整实际Gaussian good profile：全短Appell/常数/高尾给原首项c_(p−R−2)=c_(R−2)，完整多项式为N_R·[T^(p−R)U^R](exp(wTU)−1)K。全部低band、Weil/δ尺度、两twist及principal极部保留；极部仅落实际缺席R=(p+1)/2。norm2准确w→iw，Fay保全低乘积；原双支good mask与全标签注入仍开。

[原Gaussian norm2分布](notes/2026-11-27-original-Gaussian-norm-two-Kronecker-distribution.md)付同一$(1+i)$的完整Kronecker两极分布、真实平移相位与平方根分支；$y_k=5G_{p-3}=2a/\delta^3$为单位。N11/N12/N14保全部低层卷积及原good mask，尚未排R1116的指定内段同时零。

原同h=6i+7必须同时满足本原/Legendre/fi gj两个mask；R971全span与R1006全p稳定已否，特定A/E4仍开。R1009粗CM阶≤4不代零阶。全部原尺度、来源与旧窗5992+7878至500000沿[逐字前态](handoff-archive-2026-11-27-before-short-Cartier.md)保全；不重算旧窗或已登记恒等式。

## O2：原高近p值

[R1095](results/R1095-original-theta-kernel-dual-Psi-normalization.md)：原完整J#可逆，B_J(Ψ,g)=ℓ_p(g)、B_J(Ψ,Ψ)=1；真三平移Gram=(1−δ/γ)²(1+2δ/γ)，最高偶边界c=δ。§8给原Fay全核及e/K4两配对；§9完整FSF保三极、正规常数与移位Miller项，且F(SΨ)=(V+v)(2vΨ−δU)/U²。指定非正交仍开。两个因子与原短η/ν仍开，未替换bare范数。

R1041/48原r2 bare为核范数，实际AS原函数和p-block给端点平方；二者不互代，原尺度/完整留数保结果及逐字前态。R1034两行bare完整有限系数，r8须留多项式部分。R988给原trace与高balanced值准确等价，全部相位、carry、K共振及primitive范围保open；低单位不代高值。旧R963/991/994差集4008点至200000已成不重跑，bare及高近p单位仍开。

## O4–O6：旧全局边界

R1007/08原高度格三挠Picard/ℓ²及野3障碍仍保；R696/832只为指定Ω，R948只为两有限Abel零集。R805–930与R907四artifact真404保逐字前态，不重造。R707主41非47，R1004仅导子下界；Jaswal121未公认主结论不用。

原λ=−6(b+1)/r（R1045.5）；MW后M1已成，最低w单位/深盘仍开。全部尺度/边界保open及归档，真达README标准才收尾。

