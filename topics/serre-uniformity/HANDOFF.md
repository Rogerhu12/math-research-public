# Serre 一致性交接

## 目标、认领与规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN；未达到课题README完成标准。**

会话 **Astra-serre-24b8836b-20261126**。本轮已部分克隆并真实pull main，读两README/H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则读至36cf1ed2。不重做已登记结论或窗口。

**公开两README已读提交：2c8da5ccca4fb13e674359942a4e3e57d87b5d8a**（2026-11-27 22:46 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异并立刻执行。

已真实部分克隆/pull；21:59再试pull仍报无可用执行环境，shell未运行；按根规矩8用连接器小文本同步、读两README差异、带expected_sha非force提交，恢复后立即pull --rebase。拒绝即同步重基再推至成功。令牌仅CLI；根维护main/H/open/index/log，子研究独立稿，每条结论立即推。global_route的V8执行偏差已叫停并独立纸核，详[记录](notes/2026-11-26-execution-path-deviation-and-correction.md)，其输出不作证明/合规窗口。

H<10KB、open尽量<30KB、每MD<100KB、topic<200MB；无可重算raw、不写根LOG。[最新逐字前态](handoff-archive-2026-11-27-before-inverse-center-wz.md)沿链保全部旧来源/run/hash；[open](open.md)、[索引](results.md)是完整入口。历史“R1003 norm3准备中”未交付，现R1003为范围纠错。

## 原高度来源与范围

R1063：全Hecke族消MW及真辛商，最低两jet行列式仍开。R1058：原D/Q/Q²值的完整全根留数及最多七阶jet已付，单位仍开。旧原PD/PF、MW后M1及相位/全尾保归档；R1047公共根界不代非中心排除，R1011 Lie横截不付整单位半径。

## O0：完整一般素数范围；固定47已完成

[R1003](results/R1003-global-scope-and-remaining-branches.md)：主目标为所有充分大p的完整N_ns。p2/5mod9仍需小惯性C³；R317另需整j、K=Q(√−3)、σ1及二/三小域同时一致。完整惯性、非整j、变化K、非平凡σ与异小域均未关；固定47不等于Serre完成。

[R1062–71](results.md)付原全cusp/étale/p-only来源、所有角色/phase/twists，无regular/Vandiver。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)用互不交高低Bernoulli配对，将实际good维数升至≥floor(p/16)+3（forced-only仍Ω(p/logp)；完整T链只用总budget不能改1/16）。原候选O(p^1.5logp)；有界惰性CM代表不推Q-CM，一般p small-aux迹零/同点像仍开，单cusp无Runge。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)：原good圆单位同时非零密度=(1−1/p)^d/(p−1)，split-K中>1/2；全global标签localization同构。§§9–10付准确导子/判别式，rd<p²（forced-only <p^1.5），单角色并集计数；§11以真实abelian H及最大导子付无条件ℓ_faith≪p^(1215p−867−521r_min)，无p^d粗界损失。仍不付足够小辅助素/一般p同点像；附加普通/Hecke分裂须重计参数。

[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)：原非整j局部分支由同一cusp的Kummer-annihilator Frobenius并集精确判别；−1modp整支仍相容，候选非零坐标给无条件秩下界。一般p的affine像/分母全局排除仍开。固定47现由下述独立全链完成，不再保留该固定曲线的伪缺口。

### 原完整X_ns^+(47)已完成，只消费

[R1125](results/R1125-original-full47-rational-point-classification.md)已完整证明原X_ns^+(47)(Q)恰八个有理CM点；全235坏盘/十good标签、283与4513同一点、全部非q高度（含非整j及2/3）、原73维Hodge/MW/高度、16个Cartier值及八个完整4513盘唯一均付。完整点表、各来源/run/hash在R1125及[逐字前态](handoff-archive-2026-11-27-before-linear-nonconstant-profiles.md)，只消费、不重算。旧Miller run45973334832及q² run45977769585不是依赖，不续算。

## O1：原同一保留标签与 Gaussian 强制切向

[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)以原sigma heat与安全权≤p−3给实际完整Gaussian坐标常数 iff ord_b G_(w_R)≥s_R；非恒定时coarse degree=(s_R−ord)/2。三层互不交实际角色链和总irregular预算给p4k+3时至少max{3,floor(p/96)+2}个非恒定good坐标，精确渐近下界p/96+(log24/12)p/logp−O(1)。不声称函数线性独立、中心一阶全unit、共同纤维唯一或盘内唯一；继续完整gauge差的实际good mask。

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)关闭一个真实Gaussian标签分支：p4k+3且p|B_(p−3)时，原V中χ=ω²准确出现且B₂恒good；原完整coarse标签是斜率−aβ₀⁴λ²/(20bχ)单位的一次式，故每个固定候选在该coarse线上至多一盘。只付跨盘注入，不付盘内唯一；剩余Gaussian标签问题限p∤B_(p−3)，其H_p与其它good mask仍保。

[R1126](results/R1126-original-X108-complete-CM-Raynaud-pairing.md)已付原X108六CM全部十五对Raynaud配对及十维目标，完整真实自同构保A/S/T三和。六阶Pfaffian恒零不含原S，不能由此或非CM普通性推单位；继续原gd=c²、uv=h²及primitive约束。

[原Lamé三对角续稿](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)保原B简单谱/D³单Jordan、严格短像iff及三平移；两端Green和全法向列给e₀=0时e_±1单位、e₁=−5e_−1。§§9–10付完整M_(s,ℓ)反三角/Newton矩阵，原e与K4分别为同矩阵的R和移位R²读数（保零末行）；原Φ在半常数校正纯极基上准确反对角，指定U^m的全c_s及两jet有限和均含全项。相邻单位/矩阵完美性不代原短共同非零；继续真实消元，不占R1117。

[R1113](results/R1113-original-finite-Lame-spectrum-and-jet-boundary.md)保原Lamé有限全谱、η_k与D_N(1)的准确单位尺度、Lax和三Darboux因子的全部carry；e=0时K4三项仍保，特定共同非零未付。

R1061/76原短η_k/ν_k仍开；R1077加权2k单位不代短k，R1109完整Dixon首除层只消费。

[R1130](results/R1130-original-inverse-center-recurrence-and-adjacent-unit.md)：完整WZ及纸面因式给原I_n的一阶非齐次递推；p=3n+2时I_(n+2)+I_n是明确单位。§5还准确给I_(2m+1)=−2ρ_mΣ_(j≤m)(6j+1)binom(2j,j)³/256^j，ρ_m=(−16)^m(m!)²/(3/2)_m²，原p=6m+5。短截断PF的最后强迫项在1/4非零，不能挪用半长超同余或齐次Clausen式；原S/e/K4桥与共同非零继续。run46015627853/job140561880424完整证书只消费。

R1111付原p-block全公因子M D (b³−1)^(2ε)与全tame分歧，ε=1 iff f_N=0；该支尚未排。R1060/R1092给实际非CM Cartier与其余六三挠值单位，未给原H_p(0)/H_p′(0)或S_n=0⇒B_n=0。

[R1114](results/R1114-original-Gaussian-adjacent-mixed-coefficient-unit.md)：原5H_p+(8a²/45)K_p=16G_(p−3)单位，H_p=0迫K_p=36/(aδ³)单位。§7已把K_p准确接到第二forced首项c₃：24c₃=−90G_(p−3)+(75/2)H_p+(2a³/3)V₂−(4a³/27)V₃+(a⁴/81)V₄，三个原低卷积完整保留；该角色仍须B_(p−5)good，非零/共纤维继续。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)§§7–9付原全good Gaussian完整profile、全部短Appell/常数/高尾与实际mask。完整差为同一Kronecker有限gauge；§9给 f_n=−Θ^nG_v/(n!(v)_n)、有限Möbius流及两个参数的准确有界系数式(47)/(48)，只读权≤p−3。原Hasse first integral C=B−wH，ΘH=C、ΘC=0，且Θ^p=H²Θ+HC E+C²∂w，在SS处是δ²∂w而非零。Fay/norm2全低乘积和两twist相位均保；共同纤维排除仍开，不对单个点对等式作横向微分。

[原Gaussian norm2分布](notes/2026-11-27-original-Gaussian-norm-two-Kronecker-distribution.md)付同一$(1+i)$的完整Kronecker两极分布、真实平移相位与平方根分支；$y_k=5G_{p-3}=2a/\delta^3$为单位。N11/N12/N14保全部低层卷积及原good mask，尚未排R1116的指定内段同时零。

原同h=6i+7必须同时满足本原/Legendre/fi gj两个mask；R971全span与R1006全p稳定已否，特定A/E4仍开。R1009粗CM阶≤4不代零阶。全部原尺度、来源与旧窗5992+7878至500000沿[逐字前态](handoff-archive-2026-11-27-before-short-Cartier.md)保全；不重算旧窗或已登记恒等式。

## O2：原高近p值

[R1095](results/R1095-original-theta-kernel-dual-Psi-normalization.md)：原完整J#可逆，B_J(Ψ,g)=ℓ_p(g)、B_J(Ψ,Ψ)=1；真三平移Gram=(1−δ/γ)²(1+2δ/γ)，最高偶边界c=δ。§8给原Fay全核及e/K4两配对；§9完整FSF保三极、正规常数与移位Miller项，且F(SΨ)=(V+v)(2vΨ−δU)/U²。指定非正交仍开。两个因子与原短η/ν仍开，未替换bare范数。

R1041/48原r2 bare为核范数，实际AS原函数和p-block给端点平方；二者不互代，原尺度/完整留数保结果及逐字前态。R1034两行bare完整有限系数，r8须留多项式部分。R988给原trace与高balanced值准确等价，全部相位、carry、K共振及primitive范围保open；低单位不代高值。旧R963/991/994差集4008点至200000已成不重跑，bare及高近p单位仍开。

## O4–O6：旧全局边界

R1007/08原高度格三挠Picard/ℓ²及野3障碍仍保；R696/832只为指定Ω，R948只为两有限Abel零集。R805–930与R907四artifact真404保逐字前态，不重造。R707主41非47，R1004仅导子下界；Jaswal121未公认主结论不用。

原λ=−6(b+1)/r（R1045.5）；MW后M1已成，最低w单位/深盘仍开。全部尺度/边界保open及归档，真达README标准才收尾。

