# 未解决问题与当前接续

主目标：固定一条 $E/\mathbf Q$，完整证明 $\operatorname{rank}E(\mathbf Q)\ge2$ 且无穷不同 $p$ 的通常全 $\Sha(E/\mathbf Q)[p^\infty]$ 有限。**未完成；持续研究。**

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。
[本次整理前完整 open](notes/2026-11-27-open-before-positive-characteristic-forest.md)逐字保全部旧问题、公式、source/run、失败、未付条件与更早归档链；下列整理不删除未闭门或改变既有结论。证明见 [results](results.md)、[R1001–1050 索引](notes/PROOF-INDEX-R1001-R1050.md) 和 [HANDOFF](HANDOFF.md)。

## O新来源. 同一个 canonical 斜率的实际几何非零

[完整 $\psi_4$ 来源](notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)已把正槽严格换回原 $S/H_3/H_5$，负槽为全部三挠 Gaussian Weyl 词的 $\delta$ 拉回，三条 degree102 首4规范1与 raw 分子 $(-7,624,1224)$ 全固定。有限2/3/17角色、wild两陪集、$\delta^{-n}$、完整 Yang 范数均保；复 $n=4$ 非零锚不是增广单位。

[实际 sign 曲面及图](notes/2026-11-27-original-psi4-sign-surface-fulllevel-graphs-and-fp.md)给 $C:s^6=t(1-27t)$、全 $f_{\Omega_4}=-\delta f_4(\tau/6)$、严格有限 Chow 投影、正确 full9 列基和 $+34$ 分量。全18核先重标、$Q_\tau$ 先于 sign，完整两个取向和 proper fp 已闭；没有借旧 full54 的未知 $q_0$。

[新十八图的完整 cross](notes/2026-11-27-original-psi4-full-graphs-artin-and-geometric-newton-cross.md)已付真实 Artin 全 trace、同一 fulllevel 的 fixed-base $p^2$ 全和、Kriz 的实际 $H_{-2}$ 配对及解析 $17^{n(u)}$。实际
$$
L_k(0)=\frac{\kappa_p(p^2-1)}{17}I_k^{\rm new},
\qquad
L_k B_lR_l=L_lB_kR_k,
\qquad
R_k(v)=-3q_\delta^{-v}K_{-,k}(v)J_{+,k}(v).
$$
$B_k\ne0$ 是同一正权真锚给的 Artin 基，$\kappa_p$ 只已付非零。**仅当参考 $r=3$ 或5的 $R_r(0)\ne0$**，才可定义连续 $F_{\rm new}=L_r/(B_rR_r)$，并得
$$
L'_{\rm can}(0)=-3(p-1)B_1F_{\rm new}(0)K_{-,1}(0)J'_S(0).
$$
[双槽 Newton](notes/2026-11-27-original-psi4-double-slot-newton-and-canonical-slope.md)已付全部尾项、坏带、两个 completion 和 $q_\delta$；原 canonical 坏条件因此确实迫这个同源解析斜率零。

**正在解决：**实际参考端点、共同因子的完整 KS/period/阶乘规范及增广阶、指定 derived 几何读数在无穷 $p$ 非零。若两参考全零，只能使用 cross；不能擅除参考，也不能任意插值裸 $p^n$ 或阶乘。已排的权二 $B_6$ 候选全部实际 toric 点为零，不再回到该输入。任何辅助非零必须再付同一 canonical forcing。

## O原矩阵. 正特征完整重数界及第二、第三区块

[三变量 $V$](notes/2026-11-27-original-three-variable-vector-field-prime-d-property.md)已付全次数稳定素簇分类、原奇点 D-property 常数1、真实截断评价及 minimal primary 长度小于 $p$ 的根稳定性。固定低次数通用 Noetherian 链给固定退出指标 $M$，仅为存在性常数。

[正特征截断森林](notes/2026-11-27-original-positive-characteristic-capped-forest-and-cubic-bound.md)进一步支付正规化枝的整数赋值比较、线性加权 cap、短有限流、高次数最小方程退出与三层实际交循环。排固定有限 $p$ 后，同一个原低轴满足
$$
\min\{s,\operatorname{ord}P(t,x(t),\theta(t))\}
 \le D+D(D+A)+D(D+A)^2,\qquad A=3\max\{M,288\}.
$$
所有分量权重与奇点截断误差均保；不制造无限特征 $p$ 轨道。只在 $H=s-13-r_c$ 严格大于已付上界时排原完整 $M$ 的必要低轴核。

同文§§11–14现已给原 $F(t,Y)$ 的真正薄X二次界：固定 $C=576+\max(M_\square,576)$，$U=a+C,W=b+C$，
$
\mathcal B_V(a,b)=48UCW+8(UC+UW+CW)+4(U+C+W).
$
新的 $M_\square$ 专门支付总次数3456的 Laurent 清分母，未沿用较小度数的旧 $M$。完整矩形/Segre嵌入、nef交数、边界和原奇点cap都已付。若原 primitive 低源子格准确返回，则第一块真秩至少 $(9/[176(6C+1)]+o(1))H$；仅当 $H>\mathcal B_V(\lfloor11N/34\rfloor,N)$ 才排该范围的核。原 R467 Theta 补充其实已有更强显式二维界 $a(6b-1)-2c+3$ 和全部因子费用，R637亦已有真实短三块平方根满射范围；本次已在森林§15交叉标明，后续优先复用旧界，二维二次指数不另计新推进。现在继续实际第二/第三块、同一首提升和 Gaussian 读者；低轴单位秩本身不提供所需全位行列式的正收益。原来源维数约 $9N^2/68$，第一块只有 $s$ 行，在临界 $s\sim9N^2/[68(2+\tau)]$ 单独不可能排全部核。新上界即使二次，也必须保真实常数与完整列行预算；不得添导数或乘积的中央零条件。

## O1–O3. 原固定来源的真实中央联合非零

R959/R970–983已经支付固定E65/E65³/E260/E54925/E8125的rank≥2、原全角色/周期/平方与通常全Sha桥r+corankSha≤2ordJ。还需在同一无穷p集合上至少一个固定来源的实际J′非零，才能用有限鸽巢；孤立p、投影、低jet、质量非零和来源秩不替代这一步。

R1015–1034原两frame、全部13字、同c/全4+5 Cartier槽、唯一primitive与严格全位a+2b<3费用保持。R1021两个δ-new固定来源的whole中央确为原canonical倍数，R1022全39支/两顺序回到同窗；R1025六权及末两H的单位组合已付，但坏canonical尚未迫该组合零。R953同parity首Bockstein及R954全混合秩界不自动付指定forcing成员性。完整参数和所有补域均沿归档，不重做。

R1042§§13–14给原S/T/A全精度Hurwitz前缀：push cZp、误差H+1−floorlogp(H+1)、全部Euler/core。实际q13 run46029180230/job140608285958/source dd0da200已付三行6/18/30秩及v13det=3；全差商扩到所有奇r，追加13³ray仍保全Euler。真实前缀前三秩跳≤1/3/5、原线性格Smith费用≤(18+o1)p。三个实际来源仍只在二维角变量上，不能当三自由Hasse变量；有限非零秩也可与同一完整中央收敛零相容。继续同一前缀的两变量反写、三低卷积及完整补域消元。

## O角. 全p-new字与固定角来源

R1040相关模型/固定HJN全平均、Φ126/Ξ0与G126/Ξ1、质量JG0单位均沿归档；仅JG0已付，JG′=0未经授权。R1046原E21609的K/Y角导数和R1047原norm25四even角色的完整一次项均非零，已付BDP2/真实点域/Fuchs–Pham及全尾v=n+ℓp；canonical坏尚不迫这些角值为零。

[完整unitary字](notes/2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md)§§10–13锁g_n的逆Gram、5处12odd Bell、旧2/3/7状态与反变符号；两norm3150/150固定六sigma F±的Y-unit全返回，是β^-n/d_n乘两个K缩放差。只有忘K后才为c_n(JF−−JF+)；K/Y读数另保κ^-n(1−βκ)。p^(1−n)损、mixed cut、全部wild与补域都保留。继续实际F±的完整5-old投影、精确canonical/reference系数及5-new同解约束；不把投影的身份当全来源的零。

## O几何. 原固定图与实际惰性局部normal function

所有原54/27图、η/Cor、最高λ、负9-Weil分量、两cover及Prym保持。R1039全Jac F²=−q和R1041无权q+1/半交身份不付最高加权影子。R1043同一完整J全零才给实际T_a的全p整除；坏Sha尚不迫该条件。Fr−unit核只有p个除点，不能免费全p²。

R1043§§19–22已付原KS/Hasse/Manin和对偶isogeny运输：D_Bμ=cqA、cq≠0，μ/δ=κqXPq(X³)，canonical接触3、有限ss1或2；p除点不提高接触。三权下降的μPQ有限Nq递推及cusp/IV*/O行为皆已付，Pq(−1/4)未判统一非零。CM289原full9负分量图和接触1/2保，空间Manin值不替代实际T_a/p。

R1049把同一原54图逐一降到惰性Kp，η((p))=1，最高H³(2)的φ²=−p^-1；proper FP全Čech/Frobenius同伦给AJ(Yj0)=p/(p+1)I_j,p。全NS饱和/CM Hodge给新增晶体指数1,p、c1D+=upΩ、c1D−=−pΩ−/(3up)，up单位；W₂障碍MW/p→H²(O)为Fp同构。此global障碍不赋原加权AJ非零。

R1049§8进一步给原整局部格：在FL[0,3]中两嵌入filtration3/0，商filtration2，全部扩张参数h=x+puy，Hf¹≅O、logBK=p h/(p+1)、log格=pO，模p^n扩张split iff h≡0。同原积分测试与Artin基严格h_j,p=a_j,p⁻¹I_j,p。下一具体输入是全局transition/Frob cochain在原54图的完整限制，从而计算该h；特殊纤维单点都被p+1杀，其挠提升日志为0，不能拿它们替代一阶normal function。通常全Sha全球连接还必须对应原J′，不套任意syntomic非零。

R984原规范循环Griffiths非零不付各p AJ；R988 level12 K3–E0²实现及R990新CM17图取迹为零排除保持。R979固定7993的Selbal一维/strict核0和R940全双新κ上界不判原端点/增广s=0。原Artin整场fine Selmer排除与已核外部定理范围沿归档，不重做已排输入。

## O厚点. 唯一原完整执行

原q5/q11全影子倒6零、q11完整NS/Br/MW和q11 Manin唯一run46018592834已付，不重跑。native v11 run45978097755的21000s/exit124全终态已消费，非反例、也未到四交/Norm/18×9终门。后继v12 actual run46033409751/job140622660136/source048e20343a5f7ec65db9089d824d0635d6815b2b在21:13 API仍执行；返回日志前段截至19:05显示完整两端身份与首个612厚分解已过，四交/Norm/18×9尚无终回执；完整二次域多项式返回已真实软件PASS，保原两char0 pins、全60源/29/2453/64/minimal及全部原几何门。不存矩阵或可重算日志；不启动相同并行重作业。

## O4、O6、O7及其它原门

O4：原O格Q=δ^a εw需无穷ordinary p有a≤1；E17的a偶、E389的lengthShaA=2(a+1)不删。O6：固定两点饱和λ的全核Np有限且真q_p=1于无穷p；原Tor、整周期与全部p损不能省。O7：同解内/闭盘、同Y余数、全Laurent/非恒Y权及全部216管差仍未迫原闭边界全零。完整模型、数学条件、旧外部文献/负例和各source/run全保于开头的逐字归档。


## 已闭后继与继续时必须保留的条件

上方旧主干的后续完整证明已在整理前 open 逐条登记。当前使用时须同时保留：

- 原 full54 的全部图、Artin、负二 Newton、六条 source 的全精度 cross 已付；一条 $K$ 为单位且满足原好整格范围时才有共同 $F$ 单位、模 $p$ 为 $-432$。没有此范围时不能宣称全精度单位，旧未知 $q_0$ 仍保。
- 同一 signed 因子的绝对整周期亦只在原一 $K$ 单位范围已闭；首层非零等价不能变成跨素数非零。
- $D^2S$、完整 $\zeta$ 补偿、指定热 jet 与实际半周期连接已闭；不对单个 CM 坏条件横向微分。完整 paired Lamé 代数解及零 $p$ 曲率不代原 $p-1$ 或除 $p$ 后的 $p+1$ 读者。
- 原 S3150 的完整450维点载体、有限 point-only 投影及 $K/Y$ 非零已闭；仍缺同一 canonical 坏条件迫相同读者零，不对无限中央 log 尾作有限投影。
- 原 $R1042$ 全 Hurwitz、Euler、Smith 和两角 blow-up 已闭；环境格左逆不是原 scalar kernel 的 Schur 左逆。原线性格费用约 $18p$ 必须保。
- 原 $R1049$ 晶体整格、Manin/cochain、残余 toric 比较均保未知好范围及全54权；全局障碍不直接赋原加权 AJ 非零。具体全部公式、常数和失败链见本页开头逐字归档。
- 唯一完整厚几何 v12 仍待真终态；当前 GET 只给19:05的同一前段，不据缓存尾推停顿，不重复启动。即使其原有限终门通过，仍须接通常全 $\Sha$ 的真实无穷 $p$ 条件。

root 继续审证、消费唯一作业终态、实际两库 pull 和逐条推送；geometry 处理同一新图的参考及指定斜率，central 处理实际共同因子，arithmetic 接薄窗真秩与完整矩阵第二/第三块预算。子问题完成即接下一项，主目标完成前持续研究。
