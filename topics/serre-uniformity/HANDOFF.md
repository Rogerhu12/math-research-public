# Serre 一致性交接

## 目标、认领与规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN；未达到课题README完成标准。**

会话 **Astra-serre-24b8836b-20261126**。本轮已部分克隆并真实pull main，读两README/H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则读至36cf1ed2。不重做已登记结论或窗口。

**公开两README已读提交：727471cc2e70a4e33f866df2ff4e8a6c54a7f50e**（2026-11-27 21:16 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异并立刻执行。

已真实部分克隆/pull；21:09再试pull仍报无可用执行环境，shell未运行；按根规矩8用连接器小文本同步、读两README差异、带expected_sha非force提交，恢复后立即pull --rebase。拒绝即同步重基再推至成功。令牌仅CLI；根维护main/H/open/index/log，子研究独立稿，每条结论立即推。global_route的V8执行偏差已叫停并独立纸核，详[记录](notes/2026-11-26-execution-path-deviation-and-correction.md)，其输出不作证明/合规窗口。

H<10KB、open尽量<30KB、每MD<100KB、topic<200MB；无可重算raw、不写根LOG。[最新逐字前态](handoff-archive-2026-11-27-before-full47-classification.md)沿链保全部旧来源/run/hash；[open](open.md)、[索引](results.md)是完整入口。历史“R1003 norm3准备中”未交付，现R1003为范围纠错。

## 原高度来源与范围

R1063：全Hecke族消MW及真辛商，最低两jet行列式仍开。R1058：原D/Q/Q²值的完整全根留数及最多七阶jet已付，单位仍开。旧原PD/PF、MW后M1及相位/全尾保归档；R1047公共根界不代非中心排除，R1011 Lie横截不付整单位半径。

## O0：完整一般素数范围；固定47已完成

[R1003](results/R1003-global-scope-and-remaining-branches.md)：主目标为所有充分大p的完整N_ns。p2/5mod9仍需小惯性C³；R317另需整j、K=Q(√−3)、σ1及二/三小域同时一致。完整惯性、非整j、变化K、非平凡σ与异小域均未关；固定47不等于Serre完成。

[R1062–71](results.md)付原全cusp/étale/p-only来源、所有角色/phase/twists，无regular/Vandiver。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)用互不交高低Bernoulli配对，将实际good维数升至≥floor(p/16)+3（forced-only仍Ω(p/logp)）。原候选O(p^1.5logp)；有界惰性CM代表不推Q-CM，一般p small-aux迹零/同点像仍开，单cusp无Runge。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)：原全部good圆单位同时非零密度=(1−1/p)^d/(p−1)，split-K中>1/2；全global标签localization同构，可加p互素Galois分裂。§§9–10付同一圆单位场精确导子/判别式，rd<p²（forced-only rd<p^1.5）；单角色degree p(p−1)的逐素并集界避整p^d场误差。有效小辅助素、一般p同点曲线像仍开。固定47的附加普通/Hecke分裂仅为已付固定输入。

[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)：原非整j局部分支由同一cusp的Kummer-annihilator Frobenius并集精确判别；−1modp整支仍相容，候选非零坐标给无条件秩下界。一般p的affine像/分母全局排除仍开。固定47现由下述独立全链完成，不再保留该固定曲线的伪缺口。

### 原完整X_ns^+(47)已完成，只消费

[R1125](results/R1125-original-full47-rational-point-classification.md)证明原完整X_ns^+(47)(Q)恰为八个有理CM点，准确j表和原点身份保正文。R1072/1074的全235坏47盘、全10 good全局标签及283同点筛选，只余八盘；R1086的全4513标签含scalar/twists/cusps/R36零坐标，锁定同一CM点。R1074§9的whole-C47 tube和R1103§6.1付全部非q项，包含非整j与2/3；未另加整j、二次域或proper inertia假设。

R1090/93、R1096/1101与R1102付同一原73维Hodge/MW整格、对数满格及全部真实高度；R1105/06付八点切向和23角；R1119/20付原带符号CM全坐标。R1118/21/23完整Cartier法付16个本除子局部值，原C_row=1−Bq(H)全矩阵桥通过。每个来源、尺度和完整run/hash见R1125入口与逐字前态，不重算已成数据。

[R1122](results/R1122-certified-original-six-complete-CM-disks.md)（run45996561850/job140497301328，117.953秒）及[R1124](results/R1124-certified-original-two-special-CM-disks.md)（run46000409994/job140510309243，117.687秒）给八盘全rank2/gcd=t/单位B，原整尾付整个4513盘各只余其CM点。六盘det2141/884/1790/1720/3453/4287；0/141的det294/3157。两次完成结果SHA与全部行存原文，非只深邻域。

旧Miller run45973334832/job140418866621、q² run45977769585/job140433713916仍可能在途；原所需输入已完整取得，它们不是依赖，不续算或补跑。若后成仅消费真实记录，不将相同数值再登记成新结论。

## O1：原同一保留标签与 Gaussian 强制切向

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)关闭一个真实Gaussian标签分支：p4k+3且p|B_(p−3)时，原V中χ=ω²准确出现且B₂恒good；原完整coarse标签是斜率−aβ₀⁴λ²/(20bχ)单位的一次式，故每个固定候选在该coarse线上至多一盘。只付跨盘注入，不付盘内唯一；剩余Gaussian标签问题限p∤B_(p−3)，其H_p与其它good mask仍保。

[R1126](results/R1126-original-X108-complete-CM-Raynaud-pairing.md)付原X108六CM输入的全部十五对Raynaud配对，目标保十维；真实R/I/σ和p逆半线性准确给A/S/T三有限和及完整表。原S_n仍为gd/uv通道；六阶Pfaffian恒零且不含S，不能从此或非CM普通性推出S单位。后继沿真实gd=c²、uv=h²及primitive求高阶约束。

[原Lamé三对角续稿](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)付W_C上B的准确三对角/简单谱与D³的单Jordan块；e=K4=0 iff DF∈(D³)²(U²k[V]≤k−3)，原首余核杀常数，真实三平移保全部乘子。只付同源短旗标接口，未排该包含、未占R1117；不能把全空间谱代短minor。 §6原Green两端列的所有分量单位，准确(B+v)y⁻=−4v e_−N、(B−v)y⁺=4v e_N；保0×pole端残项，原J1完整强迫不能换成端点。

[R1113](results/R1113-original-finite-Lame-spectrum-and-jet-boundary.md)付原有限Lamé全谱、完整jet递推及η_k=(16v²g0/(3δ))D_N(1)；g0单位，e=0时K4必须保全部三项。R1061/76的同一T=−2vΨ³/δ³、η_j=j[z^j]T、ν_j=j[z^j]T²/40不换；指定η_k/ν_k非同时零仍开。R1077加权2k次单位不代短k次。R1109完整Dixon首除层仅消费。

R1113 §§8–9新增原B=D³−3UD−3V的完整联合简单谱、真实三Darboux因子与全部三阶jet carry；C=UD+V仅在明确W_C上半单，原U^m为唯一零列。每个实际列的relative Cartier读数e_ℓ给精确p−1系数；仍未付指定e/K4非同时零。

R1111付原p-block全公因子M D (b³−1)^(2ε)与全tame分歧，ε=1 iff f_N=0；该支尚未排。R1060/R1092给实际非CM Cartier与其余六三挠值单位，未给原H_p(0)/H_p′(0)或S_n=0⇒B_n=0。

[R1114](results/R1114-original-Gaussian-adjacent-mixed-coefficient-unit.md)：原5H_p+(8a²/45)K_p=16G_(p−3)单位，H_p=0强制K_p=36/(aδ³)单位；K_p至其它真实forced标签的桥仍开。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)把全部Gaussian forced切向准确读为Kronecker原反对角c_(2j−1)，保good mask与全部低层乘积；指定半段缺失未排。

[原Gaussian norm2分布](notes/2026-11-27-original-Gaussian-norm-two-Kronecker-distribution.md)付同一$(1+i)$的完整Kronecker两极分布、真实平移相位与平方根分支；$y_k=5G_{p-3}=2a/\delta^3$为单位。N11/N12/N14保全部低层卷积及原good mask，尚未排R1116的指定内段同时零。

原同h=6i+7必须同时满足本原/Legendre/fi gj两个mask；R971全span与R1006全p稳定已否，特定A/E4仍开。R1009粗CM阶≤4不代零阶。全部原尺度、来源与旧窗5992+7878至500000沿[逐字前态](handoff-archive-2026-11-27-before-short-Cartier.md)保全；不重算旧窗或已登记恒等式。

## O2：原高近p值

[R1095](results/R1095-original-theta-kernel-dual-Psi-normalization.md)：原完整J#可逆，B_J(Ψ,g)=ℓ_p(g)、B_J(Ψ,Ψ)=1；真三平移Gram=(1−δ/γ)²(1+2δ/γ)，最高偶边界c=δ。§8给原Fay全核及e/K4两配对；§9完整FSF保三极、正规常数与移位Miller项，且F(SΨ)=(V+v)(2vΨ−δU)/U²。指定非正交仍开。两个因子与原短η/ν仍开，未替换bare范数。

R1041/48原r2 bare为核范数，实际AS原函数和p-block给端点平方；二者不互代，原尺度/完整留数保结果及逐字前态。R1034两行bare完整有限系数，r8须留多项式部分。R988给原trace与高balanced值准确等价，全部相位、carry、K共振及primitive范围保open；低单位不代高值。旧R963/991/994差集4008点至200000已成不重跑，bare及高近p单位仍开。

## O4–O6：旧全局边界

R1007/08原高度格三挠Picard/ℓ²及野3障碍仍保；R696/832只为指定Ω，R948只为两有限Abel零集。R805–930与R907四artifact真404保逐字前态，不重造。R707主41非47，R1004仅导子下界；Jaswal121未公认主结论不用。

原λ=−6(b+1)/r（R1045.5）；MW后M1已成，最低w单位/深盘仍开。全部尺度/边界保open及归档，真达README标准才收尾。

