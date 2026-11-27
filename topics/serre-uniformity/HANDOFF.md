# Serre 一致性交接

## 目标、认领与规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN；未达到课题README完成标准。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读两README/H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则读至36cf1ed2。不重做已登记结论或窗口。

**公开两README已读提交：6497e9e890f1ba95392f69121a37d70de1980e2e**（2026-11-27 23:30 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异并立刻执行。

22:55再试pull仍报无可用执行环境，shell未运行；按根规则8用连接器小文本同步、读差异、带expected_sha非force提交，恢复后立即pull --rebase。拒绝即同步重基再推至成功。令牌仅CLI；数学程序仅本公开仓库Actions，禁止本地/V8数学计算。root维护main/H/open/index/log，子研究独立稿，每条结论立即推；此前V8偏差及停用见[纠正记录](notes/2026-11-26-execution-path-deviation-and-correction.md)。

H<10KB、open尽量<30KB、每MD<100KB、topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-27-before-Tate-normal-FM.md)沿链保全部旧公式/来源/run/hash；[open](open.md)、[索引](results.md)为完整入口。历史“R1003 norm3准备中”未交付，现R1003为范围纠错。

## O0：所有充分大素数；固定47已完成

[R1003](results/R1003-global-scope-and-remaining-branches.md)保完整N_ns主范围：p2/5mod9仍需小惯性C³；R317需整j、K=Q(√−3)、σ1及二/三小域一致。完整惯性、非整j、变化K、非平凡σ与异小域仍开。[最新primary范围](notes/2026-11-27-latest-primary-literature-scope.md)的条件开像/固定121不补一般p。

R1062–71保原全cusp、étale/p-only、全部角色与twists，无regular/Vandiver。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)给实际good维数≥floor(p/16)+3，forced-only Ω(p/logp)；仅总irregular预算的完整T链不能改善1/16。原候选O(p^1.5logp)，有界惰性CM代表不推Q-CM，单cusp无Runge。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)给原圆单位同时非零密度(1−1/p)^d/(p−1)、完整localization同构、精确conductor/discriminant及有效ℓ_faith≪p^(1215p−867−521r_min)。该p^{O(p)}界不付足够小辅助素或same-point像。[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)给原分母annihilator精确判据，−1modp整支仍相容。继续实际整四阶cochain、算术cup与原同点函数；几何Weil pairing零不付HS混合阻碍。

[原K₂[p]全尖点规范](notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)：整未分歧K₂[p]模常数准确为μ_p⊗J(K)[p]，全cusp leading平均给Δ等变分裂；规范后的even剩余落在odd J(K)[p]，既有even cusp模块不控制它。须实际付p-torsion、全tame、常数与odd分量，未得到cup零或四阶cover。§7条件式原两维层0→ω^r→E→ω^(1−r)→0的Kummer radical实际为ω^(2−2r)，即T(r)=p+1−2r；反向为ω^(2r)，不能接β_r。实际J整层/重数/圆单位相等仍开。

### 原完整X_ns^+(47)：只消费；新旧来源交叉审计在做

[R1125](results/R1125-original-full47-rational-point-classification.md)完整八CM分类已付：235坏盘/十good标签、283与4513同一点、全部非q高度含非整j及2/3、73维整Hodge/MW/log/height、16Cartier值及八完整4513盘唯一。来源/run/hash保R1125与逐字归档，不重算固定47。

旧Miller run45973334832/job140418866621已budget AlarmInterrupt失败，无完整新值；不重跑。旧q² run45977769585/job140433713916成功，source ccad9f4a…，17370.253秒，四个原23y−C∞的完整λ73均输出；root核四hash及总canonical结果5a084d55b4df85ab0a4eb38e8e5032292960ff83a81b6babfd3c54235d5ea734。它不是R1125依赖；现核其与旧Bu₄/q及R1120带符号坐标的实际B_q/Hodge转换，尚不声称数值一致。只做新回执交叉核，不再算长链/高矩。独立[交叉核方法](notes/2026-11-27-full-p47-CM-log-crosscheck-method.md)及600/30秒Actions已提交；首run46024515504/job140592329768在读旧日志前URLError、completed空；已将下载改为host TLS预取/容器只读固定临时文件，完整B_q/ρ/c及16旧读数仍待真实回执。mismatch是合法完整结果。

## O1：原同一标签、Picard两jet与实际Gaussian mask

[原Tate三挠normal-FM](notes/2026-11-27-original-Tate-three-torsion-normal-FM-variation.md)已付实际ε族的Verschiebung一阶、全Miller核及相对Cartier变分。原有限偶源上 N=2(U³+v²)∂U²+5U²∂U+U，6v·dot t_f=Φ(Nf)−δRcal·Φf；N保持原V₀。指定f=U^m给6v·dot t=−δRcal·t+(3v²/2)Φ(U^(m−2))，在−Q恢复原normal单位。移动标架可有2p−2极，不能删项或认作Picard D⁴；实际normal-to-Picard桥及e/K4共同非零仍开。 §§6–7另从实际kerV全局截面付M₀=(1+εδRcal/(6v))s^(p−1)及−Q刚化，修正后12v·dot J=(D_T²−2U_T²D_T/V_T)J；全odd自然源矩阵/移动基变分也保，未换成Picard D⁴。

[原Lamé短旗标](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)保B简单谱/D³单Jordan及严格短像；两端Green/normal列给e₀=0⇒e_±1单位、e₁=−5e_−1。§§9–10付完整Cartier Newton矩阵，e/K4分别为同矩阵R和移位R²读数；末零行/短cut全保。原Φ在半常数纯极基反对角，U^m全部系数和两jet有限和已付；完美性不代指定非正交。R1113保原Lamé谱、η_k/D_N(1)准确单位尺度、Lax与Darboux carry。原e=K4=0的短η_k/ν_k门仍开，R1077加权2k不代短k，R1109首除层不代直接比较。

[R1130](results/R1130-original-inverse-center-recurrence-and-adjacent-unit.md)完整WZ及一阶解给原I_n和截断m=(p−5)/6的Ramanujan和，PF强迫边界unit保全。§6付实际邻项来源及I_(n+2)+I_n=3δ/4；旁单位只回旧C(Uω)，不再当独立K4入口。run46015627853/job140561880424，source4a0f6f21…、证书SHA9b825833…只消费；不重跑prime窗口。

[R1126](results/R1126-original-X108-complete-CM-Raynaud-pairing.md)保六CM十五对配对与十维目标，实际Aut保A/S/T；完整Pfaffian不含原S，不能从非CM普通性推S单位。R1060/R1092原非CM Cartier/六三挠值已unit，无S0⇒B0桥。R1111准确p-block公因子MD(b³−1)^(2ε)，ε1 iff原f_N0；此支仍开。

### 原Gaussian完整gauge与共纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)：p4k3且p|B_(p−3)时实际χ=ω²出现，B₂恒good，完整coarse一次单位斜率−aβ₀⁴λ²/(20bχ)。只付跨盘；剩余Gaussian可设p∤B_(p−3)，盘内仍需原高度。

[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)完整坐标constant iff ord_bG_(v_R)≥s_R；非constant degree=(s_R−ord)/2。原三层实际角色链给至少max{3,floor(p/96)+2}个非恒定good坐标，精确渐近p/96+(log24/12)p/logp−O(1)。不推函数独立/首jet单位/共同纤维唯一。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)§§7–9付完整短Appell/profile、全部低乘积/常数/高尾与原Bernoulli mask；完整差来自K_w=e^(wTU)K。f_n=−Θ^nG_v/(n!(v)_n)，有限Möbius流及实际共纤维式(47)/(48)只读权≤p−3。Hasse C=B−wH、ΘH=C、ΘC0；Θ^p=H²Θ+HC E+C²∂w，在SS为δ²∂w，不能误设0或横向微分某个点对等式。最高两个可疑low单位行实际缺席，不能偷加行；继续原masked矩阵与共同纤维。

[R1114](results/R1114-original-Gaussian-adjacent-mixed-coefficient-unit.md)原5H_p+(8a²/45)K_p=16G_(p−3)unit；H0迫Kpunit。§7准确接第二forced首项c₃，三个低卷积V₂/V₃/V₄全保；实际B_(p−5)good和c₃非零尚未付。该profile含i4非affine。原[norm2分布](notes/2026-11-27-original-Gaussian-norm-two-Kronecker-distribution.md)保(1+i)两极、全部twist相位/平方根及低卷积，内段同时零仍开。

原同h=6i+7须本原/Legendre/fi gj两mask同时满足；R971全span和R1006全p稳定已否，特定A/E4开。R1009粗CM阶≤4不代零阶。旧5992+7878至500000及4008至200000窗口全部已成，只消费沿归档来源。

## O2及旧全局边界

[R1095](results/R1095-original-theta-kernel-dual-Psi-normalization.md)原完整J#可逆，B_J(Ψ,g)=ℓ_p(g)、B_J(Ψ,Ψ)=1；三平移Gram与最高边界已付。完整Fay/FSF三极、正规常数及移位Miller项全部保留，Φ(SΨ)=(V+v)(2vΨ−δU)/U²；不代指定短非正交。R1041/48 bare核范数与实际AS端点平方不互代；R1034 r8保多项式部。R988原trace/高balanced值准确等价，全相位/carry/K共振/primitive保open。

R1063全Hecke消MW与真辛商、R1058全部根留数与最多七jet只缺实际单位；R1047共同根界不代非中心排除。R1011实际非CM半秩商首Abel jet非零不付p整单位半径。R1007/08真实高度格三挠Picard/ℓ²及野3障碍继续生效。R696/832只为指定Ω，R948只为两有限Abel零集；一般有理候选MW像可能非零。

R805–930固定源与R907四artifact真404保逐字归档，不重造。R707主41非47，R1004仅导子下界；Jaswal121未公认主结论不用。原λ=−6(b+1)/r、MW后M1及最低w/deep盘全部尺度保open；达到README主标准才收尾。
