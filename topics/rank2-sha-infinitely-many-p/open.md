# 未解决问题与当前接续

主目标：固定一条 $E/\mathbf Q$，完整证明 $\operatorname{rank}E(\mathbf Q)\ge2$ 且无穷不同 $p$ 的通常全 $\Sha(E/\mathbf Q)[p^\infty]$ 有限。**未完成；持续研究。**

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。
[本次整理前完整 open](notes/2026-11-27-open-before-positive-characteristic-forest.md)逐字保全部旧问题、公式、source/run、失败、未付条件与更早归档链；下列整理不删除未闭门或改变既有结论。证明见 [results](results.md)、[R1001–1050 索引](notes/PROOF-INDEX-R1001-R1050.md) 、[R1051–1100 索引](notes/PROOF-INDEX-R1051-R1100.md) 和 [HANDOFF](HANDOFF.md)。

## O新来源. 同一个 canonical 斜率的实际几何非零

[完整 $\psi_4$ 来源](notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)已把正槽严格换回原 $S/H_3/H_5$，负槽为全部三挠 Gaussian Weyl 词的 $\delta$ 拉回，三条 degree102 首4规范1与 raw 分子 $(-7,624,1224)$ 全固定。有限2/3/17角色、wild两陪集、$\delta^{-n}$、完整 Yang 范数均保；复 $n=4$ 非零锚不是增广单位。

[实际 sign 曲面及图](notes/2026-11-27-original-psi4-sign-surface-fulllevel-graphs-and-fp.md)给 $C:s^6=t(1-27t)$、全 $f_{\Omega_4}=-\delta f_4(\tau/6)$、严格有限 Chow 投影、正确 full9 列基和 $+34$ 分量。全18核先重标、$Q_\tau$ 先于 sign，完整两个取向和 proper fp 已闭；没有借旧 full54 的未知 $q_0$。

[新十八图](notes/2026-11-27-original-psi4-full-graphs-artin-and-geometric-newton-cross.md)的 Artin 全 trace、同一 fulllevel fixed-base $p^2$ 全和与直接 proper-fp 返回独立已付，特别
$$
\mathcal A^{\rm out,new}_k=(p^2-1)I_k^{\rm new}.
$$
[21:55连续性审计](notes/2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md)已将后继连续几何 cross、Kriz $H_{-2}$ 到此 AJ 的识别和共同几何单位改为条件陈述：需要同一个连通延拓或原 flat/usual-depletion 交织、换点后正确的定义域，以及负端点的实际微分/Frobenius归一。7.20 的两个不交区域与7.21的good点连续性均不自动给这些条件。

审计还给精确离散障碍：$A=p^2-1,B=p-1$ 时，任何固定非零 $K,\zeta$ 的
$$
g(u)=K\zeta^u\frac{((Au)!/(Bu)!)^2}{Au-1}
$$
都不可能满足两个非零连续函数之间的 $L(u)=g(u)R(u)$（所有正整数）。双Hermite完整阶乘保持，不能添未证Gamma修正。同一当前未除幂张量的实际toric比较已在§7逐项锁定为固定幂；它与真实flat族的识别仍未成立。本审计不声称原书定理假。

[纯双槽 Newton](notes/2026-11-27-original-psi4-double-slot-newton-and-canonical-slope.md)仍独立给
$$
R_k(v)=-3q_\delta^{-v}K_{-,k}(v)J_{+,k}(v),\qquad
R'_{\rm can}(0)=-3K_{-,1}(0)J'_S(0).
$$
原 canonical 坏条件确迫这个纯 Newton 斜率零。即使参考 $R_3(0)$ 或 $R_5(0)$非零，仍须先支付几何接合，才可定义实际几何共同因子及读取其端点；正权消因子自身不填连续性缺格。

**固定正权证书已付：**公开run46073583710/job140756005342实际成功，固定 $p=227,u=1$、$n=51526$ 的两个原完整槽系数均非零，整窗身份全PASS，故 $R_{{\rm can},227}(226)\ne0$。辅助65537只证明特征零非零；离散障碍的非零前提现在不是空条件。**正在做：**当前literal序列已确定不连续，继续寻找从真实flat算子本身导出的规范及其proper端点，而不是在旧比较上补无来源因子；原bad点更深根与完整 $p^2$ source已保下述费用。未能接合就继续同一 S3150 forcing/原矩阵方向，不停止研究。参考端点、真正 derived 读数及无穷 $p$ 非零仍须解决。已排权二 $B_6$ 的全部toric点零不再重算。

[原bad CM点的真实b2读者与p²边界](notes/2026-11-27-original-bad-cm-b2-source-and-p-square-boundary.md)：$g_1^*Q_1=Q_2$、$g_1^*\omega_{\rm can}=\omega_{\rm can}$、$g_1^*dz_{\rm dR}=p^{-1}dz_{\rm dR}$，故好点 $(p\theta)^j$ 的连续读者实际运输成坏点 $(p^2\theta)^j$，但source是 $g_1^*F$。回原source仍须好点 $g_2^*F_0$ 的完整有界性。对同一实际cyclic $p^2$分支，严格有
$
O_D=(1-p^{-2})G(E)-\lambda_D^*I_D/p^2.
$
完整incoming范数为零而outward为 $p(p+1)(1-p^{-2})G$，所以对偶/Fricke换点仍留下原 $G(E)$ 边界；不能靠相同Euler因子恢复原图。直接proper图身份保留，未与Newton或flat负端点相认。

下一须在这个真实outward source上证明完整flat/微分比较；好点incoming连续性单独不读该边界。

[连续性审计§7](notes/2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md)现锁定同一已完成的未除幂 raised 张量 $\omega^3\otimes(\Omega^1)^n$：固定CM基/KS/level比较只有 $q_{p,n}=q_{p,4}Q_p^{n-4}$，完整两Hermite仍为 $c_n=n!(n+2)!\xi^{n-4}/(4!6!)$。真实Hecke等变KS保 $\det H_{\rm dR}^{-n}$，7.19的实际基乘 $p^{3+n}$；书7.22的 $p^{3+2n}$ 尚缺同一线性化比较，但任何这种固定幂都不修digit障碍。由实际 $R_{{\rm can},227}(226)\ne0$，当前明定的 full18图/通常depletion/未除幂正整数序列**不存在连续延拓到 $\mathbf Z_{227}$**。这是本题literal数列的严格结论，不把它与真实flat族无条件相认，也不据此称书定理假。后继须真正给不同算子或权归一并重证proper端点，参考非零或period单位不能补此门。

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

[原森林§§16–18.1](notes/2026-11-27-original-positive-characteristic-capped-forest-and-cubic-bound.md)把同一三块实际化为 $(t^H,t^Kh^2,h^3)$，只剥显示 $t^rY^{m_0}$，保Euler电荷。通用判别式的一次项严格为 $-4c_0c_2^3\operatorname{Disc}Q_2$，故原点阶至少 $\min(2H',H'+3K')$。原全部68角帽给 $W=(b-1)(b+2m_0)$，若剩余判别式非零则
$
\min(2H',H'+3K')+3\lceil W/68\rceil
\le \lfloor11W/34\rfloor-r(2b-2).
$
失败只强迫实际非边界重复因子，未排所有核；同一R的两carry、完整首次提升和真正第二余核Xi全部保留。低b例外明确，未以独立三次秩或新中央导数代替原三块。

[森林§19的准确范围](notes/2026-11-27-original-positive-characteristic-capped-forest-and-cubic-bound.md)：原profile $m_0/N\to\mu,b/N\to\beta,r/N\to\rho,K/H\to\tau$ 必须保 $\mu/68\le\rho\le19\mu/68$；判别式严格失败门是 $\beta[19(\beta+2\mu)-136\rho]<9\min(2,1+3\tau)/(2+\tau)$。真实逐charge列数(68)表明，有固定裕量时已经 $H>n_{\rm win}+cN^2$，所以此门仍在第一块行数超过窄窗列数的范围，**未触全临界或主严格预算**。泛型不可分被 $\deg_Y<p$ 排除后可得核子空间共同平方因子，但Theta的68格不能未付返回就接成rho的19角格；同R/carry/Xi保。后继转增长块数与同一饱和旗标的全Smith指数，不再把固定三块小改进充作全局正收益。

按原固定深度预算，下一实质方向为深度随来源增大时的原高尾、全部块和同一全Smith指数；严格目标仍为 $\sum_p g_{p,D}\log p>3M_D\log D$。

## O1–O3. 原固定来源的真实中央联合非零

R959/R970–983已经支付固定E65/E65³/E260/E54925/E8125的rank≥2、原全角色/周期/平方与通常全Sha桥r+corankSha≤2ordJ。还需在同一无穷p集合上至少一个固定来源的实际J′非零，才能用有限鸽巢；孤立p、投影、低jet、质量非零和来源秩不替代这一步。

R1015–1034原两frame、全部13字、同c/全4+5 Cartier槽、唯一primitive与严格全位a+2b<3费用保持。R1021两个δ-new固定来源的whole中央确为原canonical倍数，R1022全39支/两顺序回到同窗；R1025六权及末两H的单位组合已付，但坏canonical尚未迫该组合零。R953同parity首Bockstein及R954全混合秩界不自动付指定forcing成员性。完整参数和所有补域均沿归档，不重做。

R1042§§13–14给原S/T/A全精度Hurwitz前缀：push cZp、误差H+1−floorlogp(H+1)、全部Euler/core。实际q13 run46029180230/job140608285958/source dd0da200已付三行6/18/30秩及v13det=3；全差商扩到所有奇r，追加13³ray仍保全Euler。真实前缀前三秩跳≤1/3/5、原线性格Smith费用≤(18+o1)p。三个实际来源仍只在二维角变量上，不能当三自由Hasse变量；有限非零秩也可与同一完整中央收敛零相容。继续同一前缀的两变量反写、三低卷积及完整补域消元。

## O角. 全p-new字与固定角来源

R1040相关模型/固定HJN全平均、Φ126/Ξ0与G126/Ξ1、质量JG0单位均沿归档；仅JG0已付，JG′=0未经授权。R1046原E21609的K/Y角导数和R1047原norm25四even角色的完整一次项均非零，已付BDP2/真实点域/Fuchs–Pham及全尾v=n+ℓp；canonical坏尚不迫这些角值为零。

[完整unitary字](notes/2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md)§§10–13锁g_n的逆Gram、5处12odd Bell、旧2/3/7状态与反变符号；两norm3150/150固定六sigma F±的Y-unit全返回，是β^-n/d_n乘两个K缩放差。只有忘K后才为c_n(JF−−JF+)；K/Y读数另保κ^-n(1−βκ)。p^(1−n)损、mixed cut、全部wild与补域都保留。继续实际F±的完整5-old投影、精确canonical/reference系数及5-new同解约束；不把投影的身份当全来源的零。

[原Y/K完整球面Hecke§16](notes/2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md)：全部 $p(p+1)$ 格逐支计数给 $\mathcal H_p(B_0\otimes B_0)=p^2B_1\otimes B_1+(p-1)B_0\otimes B_0+B_{-1}\otimes B_{-1}$。保同一自然/标准交织、正负division/Haar、完整六输出及物理Y-unit后，真实返回为 $\nu_{\mathcal H_p}^{\times}=(p-1)\nu^\times+\beta^{-1}(D_{K,\kappa^{-1}})_*\nu^\times$。因此有限字 $\mathcal Z_p=\mathcal H_p-(p-1+\beta^{-1})$ 的整个不读K边际恒零，而同一 $K/Y$ 读数严格为 $\beta^{-1}(\kappa^{-1}-1)(10\delta/7)\Omega I_{D,p}\ne0$，用原R1046同一固定非挠点。该实际反例排除“完整Y边际加这个球面Hecke就迫K/Y零”的替代；不排另有真实读K的来源关系，也不声称原坏中央实际存在。

后继必须使用真正读K的同解内关系；不再重做这个球面和或以其完整Y-Mellin身份代canonical forcing。原5-new/p-new补项仍保。

## O几何. 原固定图与实际惰性局部normal function

所有原54/27图、η/Cor、最高λ、负9-Weil分量、两cover及Prym保持。R1039全Jac F²=−q和R1041无权q+1/半交身份不付最高加权影子。R1043同一完整J全零才给实际T_a的全p整除；坏Sha尚不迫该条件。Fr−unit核只有p个除点，不能免费全p²。

R1043§§19–22已付原KS/Hasse/Manin和对偶isogeny运输：D_Bμ=cqA、cq≠0，μ/δ=κqXPq(X³)，canonical接触3、有限ss1或2；p除点不提高接触。三权下降的μPQ有限Nq递推及cusp/IV*/O行为皆已付，Pq(−1/4)未判统一非零。CM289原full9负分量图和接触1/2保，空间Manin值不替代实际T_a/p。

R1049把同一原54图逐一降到惰性Kp，η((p))=1，最高H³(2)的φ²=−p^-1；proper FP全Čech/Frobenius同伦给AJ(Yj0)=p/(p+1)I_j,p。全NS饱和/CM Hodge给新增晶体指数1,p、c1D+=upΩ、c1D−=−pΩ−/(3up)，up单位；W₂障碍MW/p→H²(O)为Fp同构。此global障碍不赋原加权AJ非零。

R1049§8进一步给原整局部格：在FL[0,3]中两嵌入filtration3/0，商filtration2，全部扩张参数h=x+puy，Hf¹≅O、logBK=p h/(p+1)、log格=pO，模p^n扩张split iff h≡0。同原积分测试与Artin基严格h_j,p=a_j,p⁻¹I_j,p。下一具体输入是全局transition/Frob cochain在原54图的完整限制，从而计算该h；特殊纤维单点都被p+1杀，其挠提升日志为0，不能拿它们替代一阶normal function。通常全Sha全球连接还必须对应原J′，不套任意syntomic非零。

R984原规范循环Griffiths非零不付各p AJ；R988 level12 K3–E0²实现及R990新CM17图取迹为零排除保持。R979固定7993的Selbal一维/strict核0和R940全双新κ上界不判原端点/增广s=0。原Artin整场fine Selmer排除与已核外部定理范围沿归档，不重做已排输入。

## O厚点. 唯一原完整执行

原q5/q11全影子倒6零、q11完整NS/Br/MW和q11 Manin唯一run46018592834已付，不重跑。v11真时限终态沿原归档。[v12真终态](notes/2026-11-27-v12-terminal-and-captured-return-binding.md)：原run46033409751于22:15:38被真实21000s门限中止，signal15/exit124；完整日志5694056B/hash80552d07f846435ca65e372cba161a4c0240e820abec053c3589d969239ce907已消费。30次完整native回返、六条612尖点分解及下一306块已返，四交/Norm/$18\times9$仍无终回执。源核查证明v12的后置module绑定没有更新先生成native函数的独立globals；这一个别名的保全部原门软件核验已于run46076504365真PASS，原primary局部平方重复已公开软件PASS（run46077929103）。[R1050：原标量厚纤维及T/v准确返回](results/R1050-original-scalar-thick-fibers-and-exact-cusp-transfer.md)（已证明）：完整自由代数中 $\pi^jA/\pi^{j+1}A\simeq A/\pi A$，故原 $\pi^mA$ 每个局部分量全长为 $m\deg(\pi)d_i$、重数为 $md_i/f_i$；$d_i$ 是整个非约化分量维数。原T/v在两图的完整scalar HNF逐式固定，finite v同T负点取有号重数−1/2，∞取同原重数。专用geometry支撑只消费point+m，因而可用全滤过回执保所有厚度而不重做其不消费的local projector；通用需完整ideal的接口不变。原四交/Norm/$18\times9$及主无穷$p$目标仍未付，软件实现已真PASS；不将时限退出作反例，不重复相同生产输入。

保原两char0 pins、全60源/29/2453/64/minimal及全部原几何门；即使有限影子通过，真正无穷p主门仍须另付。

## O4、O6、O7及其它原门

O4：原O格Q=δ^a εw需无穷ordinary p有a≤1；E17的a偶、E389的lengthShaA=2(a+1)不删。O6：固定两点饱和λ的全核Np有限且真q_p=1于无穷p；原Tor、整周期与全部p损不能省。O7：同解内/闭盘、同Y余数、全Laurent/非恒Y权及全部216管差仍未迫原闭边界全零。完整模型、数学条件、旧外部文献/负例和各source/run全保于开头的逐字归档。


## 已闭后继与继续时必须保留的条件

上方旧主干的后续完整证明已在整理前 open 逐条登记。当前使用时须同时保留：

- 原 full54 的全部图、Artin、负二 Newton 与六条来源保留；连续几何 cross 及共同几何 $F$ 单位现额外需要上述审计接合。即便一条 $K$ 单位、原好整格范围成立，也不独自支付该连续性门。独立残余比较按原范围保留，旧未知 $q_0$ 仍保。
- 同一 signed 因子的绝对整周期亦只在原一 $K$ 单位范围已闭；首层非零等价不能变成跨素数非零。
- $D^2S$、完整 $\zeta$ 补偿、指定热 jet 与实际半周期连接已闭；不对单个 CM 坏条件横向微分。完整 paired Lamé 代数解及零 $p$ 曲率不代原 $p-1$ 或除 $p$ 后的 $p+1$ 读者。
- 原 S3150 的完整450维点载体、有限 point-only 投影及 $K/Y$ 非零已闭；仍缺同一 canonical 坏条件迫相同读者零，不对无限中央 log 尾作有限投影。
- 原 $R1042$ 全 Hurwitz、Euler、Smith 和两角 blow-up 已闭；环境格左逆不是原 scalar kernel 的 Schur 左逆。原线性格费用约 $18p$ 必须保。
- 原 $R1049$ 晶体整格、Manin/cochain、残余 toric 比较均保未知好范围及全54权；全局障碍不直接赋原加权 AJ 非零。具体全部公式、常数和失败链见本页开头逐字归档。
- 唯一完整厚几何 v12 的真实21000s/exit124终态已消费；四交/Norm/18×9未返。捕获别名和同商局部平方软件均已真实通过；下一受核修改是R1050的原scalar支撑入口，保完整非约化纤维、maximal/registry及所有一般返回和几何门。有限终门也不替通常全 $\Sha$ 的真实无穷 $p$ 条件。

root 继续审证、实际两库 pull 和逐条推送；geometry 处理原 $P_q(-1/4)$ 的准确二挠读数，central 处理原theta的真实flat/Amice与合法Newton reader，arithmetic 处理真正高前缀核中的同源节点 jets 和全部 Smith 主项。子问题完成即接下一项，主目标完成前持续研究。


## 原全深矩阵的已付递推与下一未闭项（R1051）

[R1051：原完整 Gaussian 的全深折回与全部精度节点递推](results/R1051-original-full-depth-gaussian-node-recurrence.md)（已证明）：基线所有物理行模 $p$ 按数字和 $s_p(q)$ 精确折回原首窗，保 Gaussian 单位与 factorial 单位；同一原来源的全行 $\mathcal Y_{r,q}=p^q q![w^{r+sq}]\Phi$ 具有完整节点系数 $C_{\rho,j,r}$，其赋值至少 $\lceil\eta j-\vartheta\rceil$。任意 $H$ 由真正首一 $\prod_{\rho=0}^{p-1}(T-a\rho)^{\lfloor H/\eta\rfloor}$ 给全部后行递推。连续前缀和适配整旗标保全部 Smith 精度及实际对角 $\epsilon$，但已付加权收益仍仅 $O(M_D)$，未达 $3M_D\log D$ 主门；坏 canonical 条件仍是含全部 $k\gamma_m^k$ 分母的同源加权行，不能免费变成逐节点消失。

下一步使用上述完整 $C_{\rho,j,r}$ 和坏条件，在真正高前缀核/同一首提升中支付新增 Smith 主项。整个来源有许多节点并不能推出该核仍有同样节点；也不以高物理深度本身替代全局预算。


原完整几何当前软件接续见[scalar全厚支撑核验](notes/2026-11-27-original-scalar-support-software-and-production.md)。这项检查已获真实PASS；不以静态审阅、夹具结果或方法计数替原所有终门。


## 原Manin二挠特殊值的具体整数条件

[原Manin二挠特殊值的完整Legendre返回](notes/2026-11-27-original-manin-two-torsion-legendre-boundary.md)已证明：同一原 $B$ 上 $U=-1/4$ 恰为三个非零二挠点，原Hasse严格等于 $\mathcal L_{2n+1}(V)$。次数 $<q$ 的原函数固定全部积分常数；Rodrigues完整边界给 $P_q(-1/4)=(-1)^n C_n/[3\cdot2^{2n+1}(2n+1)!]$，并准确返回原规范 $\mu_{\min}(P_Q)(O)=(-1)^{n+1}c_QC_n/(2n+1)!$。这里 $q=6n+5$ 是辅助特征；整数和 $C_n$ 的无穷模q非零仍开，所有17/η/Cor后继仍保，未以实正性或半单角色取消充作非零。

下一步仅能消费这个同源整数条件或换入真正新几何输入；不能从全局Manin多项式非零直接推指定纤维非零。第一scalar软件检查真实失败于矩阵复制接口，最小修正后第二次实际PASS；未出现原几何反例。


### 全深递推的真实首提升已付范围

[R1051§8](results/R1051-original-full-depth-gaussian-node-recurrence.md)把全深递推除以 $p$ 准确返原首提升：$\mathfrak D=Q_1(E_q)\mathcal Y/p$ 对全部同源整，模p不随同一个 $P+pR$ 的 $R$ 改变；全部 $R_p(E_q)$、下一regular带及整数charge进位均保。原基线到 $p^2$ 的实际可读范围为r0时 $q\le p-3$、r>0时 $q\le p-2-6r$，逐行支付ε损失。较强 $\mathscr B_d$ 中的全首Bockstein须同时满足真实 $B_{\rho,r}=0$ 和同一个原 $R$ 的实际像条件，不能外推给旧短矩阵。原canonical坏只直接支付S/T的r0槽；旧R530 divided算子及R631/633低13成本不重复记新收益，主预算仍开。

继续联立原坏条件、真实高前缀核和这些同源下一regular带；新必要行本身不证明核降到所需维数，不把强目标的首提升等价式迁给旧基线。


原scalar软件第二次执行已真实通过（run46079484704），完整来源和第一失败见[§§4–5](notes/2026-11-27-original-scalar-support-software-and-production.md)。继续处理真实生产导入顺序及8条实际filtration回执，不将软件PASS替原几何终门。


## 原完整 v13 生产请求

[v13原完整生产接入](notes/2026-11-27-original-scalar-filtration-v13-production.md)：三项真实软件PASS后，保原60源和全部参数/数学终门，明确修正捕获别名、同商平方及原scalar支撑；八条本次实际filtration回执替原方法使用断言，通用full-local接口不变。新65源和workflow已逐项pin并请求唯一公开生产，实际run与终态待消费，不预付四交/Norm/$18\times9$。

本次只替换已证明且软件全核验的实现成本。必须实际完成原四交、一般 Artinian Norm、全部 $18\times9$ 和九对；若失败，只按真实错误修改，不重复相同输入，也不把 finite PASS 升格为无穷 $p$ 主结论。
