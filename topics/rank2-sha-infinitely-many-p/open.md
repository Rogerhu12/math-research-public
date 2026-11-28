# 未解决问题与当前接续

会话：Astra-rank2-Sha-0b097461-20261127；2026-11-28。
**主目标未完成，持续研究，不等用户回复：**固定一条 \(E/\mathbf Q\)，完整证明 \(\operatorname{rank}E(\mathbf Q)\ge2\)，并使无穷不同素数 \(p\) 的通常全 \(\Sha(E/\mathbf Q)[p^\infty]\) 有限。固定有限族的联合无穷非零可用鸽巢，随 \(p\) 换曲线不算完成。

[本次整理前完整 open](notes/2026-11-28-open-before-exact-p-square-characters.md)逐字保留全部旧问题、精确公式、运行与失败、来源及更早归档链；下列只是当前接续，不删除任何未闭门。[results](results.md)、[本卷索引](notes/PROOF-INDEX-R1051-R1100.md)和[HANDOFF](HANDOFF.md)给已证内容与实际执行状态。独立新结论按根规则8放入 results/R编号，旧 notes 路径保转向。

## O新来源：实际 p² 新块、解析运输与同一 canonical 斜率

[R1052](results/R1052-original-unmodified-b2-toric-flat-vanishing.md)已经证明：好点 \(g_2^*F_0\) 的有界性完整成立，但返回原未改动 \(F_0\) 的完整 toric flat 族及实际外权导数恒零。它只杀这个完整和，不能推点级测度支撑、canonical、signed 或 outward 为零；不再重做这条零分支。

[R1054](results/R1054-original-p-square-depleted-source-and-exact-conductor-blocks.md)现给实际通常剔除中剩余的完整来源：
\[
W_p=p^{-4}(g_2^2)^*w_0,\qquad
g_1^*((p\delta)^nA)
=-p^{2n}\delta^nF_0+p^{4n+2}(g_2^2)^*\delta^nF_0 .
\]
真实 cyclic conductor-\(p^2\) 点满足 \(v_p(c_C)=1/p\)、
\(\Omega_2=p^{-2}c_C\Omega_0\)；第二项准确成为
\(p^{-4}(c_C\Omega_0)^{3+2n}r_n^{\rm alg}(E_C)\)。
不能将原点 \(D_{102}\times S_{34}\) 的整性界搬给这个新邻点。

同文§8支付全部有限字。每轴 \(\mathbf Z/p^2\) 的完整 Weil trace 在单位、非平凡主单位和其余元素分别为 \(p^2,-p,1\)，故旧球重数一、非平凡 tame 角色重数零、所有 exact-\(p^2\) 角色重数一。完整矩阵
\(p^{-2}\zeta_{p^2}^{(51/2)(A^2-4AB+B^2)}\)
分成 \(p^{-2}v_0\otimes v_0\) 及全部 wild 逆角色对；旧新混合块为零。每条局部块非零，全局 Hermite/六根/tame 投影仍可能消零。有限环投影保 \(1/[p(p+1)]\)，不能称整幂等元；新 \(p\)-torus 不算入原 full54。

R1054§9现付完整finite intertwiner与真实核/class方向、Tate determinant/cup/KS、三个微分、准确旧项差和全部p+1单位矩阵的正权向量。非平凡wild全和消旧不赋原坏条件给新增ramified字；投回第二输出旧线则新字消失。原惰性2/full9不自动满足AI全局Heegner假设；这里只用同一prime-to-p full-level cover的局部GM/marked构造，classical k=3的局部半径允许p²，不能套two-variable n≥3或直接套全局Thm7.1。

[R1059](results/R1059-original-p-square-source-and-complete-critical-germ.md)现已给同一来源的完整负二germ及斜率：各点裸bounded Q_t输入不变，随权tensor因子j_t留在外权Λ=λj_t；真实Teich逼近与全部Maass尾、v(C)=2的Tate范数收敛支付同一解析恒等。精确保p^-4单位周期及(1−p^-2)旧germ；只有同一full-avatar wild和或R1052原完整germ可去旧。斜率保log、全部Maass、period、det与外权导数。

R1059§8现已付同一Frobenius-rigid primitive和实际有限图的值身份：p^-6Ω_i^-1〈q*G_C−G_i,ω_i〉、全e_i/m_i及旧germ保留；exact-wild完整正交时为−p^-4Σλe_i/(m_iΩ_i)AJ_out。原ψ4十八degree17核、双sign、full9和Artin1/12全部保留，full9中心只在原source本征块平方为1。

[R1060](results/R1060-original-full-gaussian-transpose-and-critical-slope.md)现给A16斜率到原整个双Gaussian来源的真实有限读者：完整逆Maass为指数卷积，有限Newton多项式给B_{i,H,ℓ}和准确槽/period系数精度。保K−old、全source h积分、actual arch与复γ逐槽代数化；图源−6δ/两√6均已付。先冻结Λ(-2)/Λ′(-2)再取全部低槽，不换成Λ(n)或原三个总period产品。

**下一实质门：**给这个完整转置后的h/finite投影、新增ramified covectors及A16全部权导数到原固定canonical斜率的实际未平均关系。有限图的值不代导数；局部单位矩阵可逆不付该关系，也不套AI全局Heegner定理。[R1058](results/R1058-original-cm-principal-unit-mobius-and-centered-root-trace.md)现已付 CM 主单位的完整居中 Möbius、所有系数和det/KS运输及含全部μp闭盘的真实延拓，并逐点证明与root平均互绕；该作用固定每个μp点，不是根平移。实际原g2²第一轴商核已核。R1059已用同源正权式与真实flat逼近比较负二全germ，§8再给整个有限读数的实际图身份；原avatar/Teich/旧项均保。不能由群阶相同认分支，也不将p^n当解析函数。

[R1056](results/R1056-original-flat-amice-critical-slope-and-bol-primitive.md)提供真正可用的同源读者：临界值是单位 inverse-square 矩，斜率保 log、全部 Maass 修正和外权导数；正 KS/正杯积 Bol 与 R997 一致。直接整 Newton 的值读者用至 \(pH-1\) 阶，斜率用 \(O(p(H+\log_p(H+1)+1))\) 阶及准确额外精度；旧 Stirling 路径另付 \(v_p(N!)\)。R1054 的负端点是原 Coleman 的 \(p^{-6}\) 真 \(Q\) 平均；R1059§8通过整个同源germ识别完整有限图读数，仍不逐根认同CM商点。

[连续性审计](notes/2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md)继续优先：完整两 Hermite 的
\(K\zeta^u(( (p^2-1)u)!/((p-1)u)!)^2/((p^2-1)u-1)\)
不能在全部正整数连接两个非零连续函数。旧 full54/六线/新 \(\psi_4\) 的连续几何 cross、\(H_{-2}\)/AJ 与共同几何单位仍条件化；固定幂 period 不修这个障碍。原 \(p=227,u=1,n=51526\) 全槽 run46073583710 已付特征零非零，辅助65537不证明227单位，不再执行同一输入。

独立[纯双槽 Newton](notes/2026-11-27-original-psi4-double-slot-newton-and-canonical-slope.md)、完整 full18/Artin/proper-fp 与
\(\mathcal A_k^{\rm out,new}=(p^2-1)I_k^{\rm new}\)
按原范围保留；参考 \(R_3(0),R_5(0)\) 非零不能单独补上述接合。原坏点
\(O_D=(1-p^{-2})G-\lambda_D^*I_D/p^2\)
仍留原 \(G\) 边界；完整 incoming 范数零不删 outward。所有有限2/3/17、wild两陪集、full9和完整权都保留。

## O原矩阵：同一个高核、全深 Smith 与严格全局收益

[R1051](results/R1051-original-full-depth-gaussian-node-recurrence.md)已付全部物理行的数字折回、完整节点递推、同一 \(P/R\) 的全精度 \(j!C\) 厚核、Hasse–Hermite 等距 PD 代数及全部截断 Smith。回旧基线保准确 \(E(J)\) 损；普通厚理想范围一般至 \((p-3)/2\)，原 S/T 环至 \(p-2\)，不是免费到 \(p-1\)。首 Bockstein 须满足原低核和同一个 \(R\) 的像条件；canonical 的单一加权槽不是乘法理想，不能变成逐节点消失。

**主门仍为**
\[
\sum_p g_{p,D}\log p>3M_D\log D .
\]
当前付出的收益仅 \(O(M_D)\)。需要随来源增长的真实深度、全部块和同一饱和旗标的全 Smith 指数；不把旧低13、来源秩或环境逆矩阵重复计作新收益。

[正特征森林](notes/2026-11-27-original-positive-characteristic-capped-forest-and-cubic-bound.md)的所有 cap、D-property、原奇点、三层循环、薄X二次界、68角帽、两 carry 与第二余核 Xi 均已付。实际三块是 \((t^H,t^Kh^2,h^3)\)，判别式门只在已超过窄窗列数的范围触发，未达全临界预算。旧 R467 显式二维界和 R637 真短三块范围优先复用，不重做更弱指数；保 \(\deg_Y<p\) 和重复因子例外，不新增中央导数或乘积的零条件。

R1042 的全 Hurwitz 前缀、两变量角结构、全 Euler 与原 q13 回执已付；环境左逆不等于 scalar Schur 的 \((18+o(1))p\) 成本。真实前三秩跳至多1/3/5，三个来源仍在二维角上。需同一前缀和补域的全消元，不能将有限非零秩当中央函数非零。

## O1–O3 / O末窗：原 canonical 联合非零与 B12 真实读者

R959/R970–983 与 R1038 已分别支付固定 E65/E65³/E260/E54925/E8125 及 E3969 的 rank≥2、全角色/周期/平方和通常全 Sha 桥。仍须在同一无穷 \(p\) 集合上至少一条固定来源的原 \(J'\ne0\)，才可有限鸽巢。孤立 \(p\)、质量非零、投影或低 jet 不足。

[R1026§9](results/R1026-extended-flat-window-thirteen-saturation-and-full-contiguous-family.md)的原两个39支顺序，全部 \(H\le p-6\) 比较精度是 \(p^{H+1}\)，非零质量、两 Gaussian 及 \(m_0\log q_\alpha\) 全保。末六权 \(H_t=p-6t\) 同样保这一精度。
[R1028§9](results/R1028-terminal-flat-weights-and-complete-thirtynine-primitive.md)的全权差为 \(c_pA^{p^2}T_t^p\)，全39核点从 \(p(H_t+1)\) 起；native 窗后原四阶 cut 逐纤维无留数。一般 \(c<6t\) 仍盲，\(c=6,t=1\) 只有尚未授权非零的端点候选。所有物理 M、高位、GP10、外权、Newton 和及严格 \(a+2b<3\) 费用保留。

[R1053](results/R1053-original-b12-canonical-reader-and-complete-thirtynine-trace.md)现将原390两来源的真正 B12 商、全部324词和完整有限权，写成 E3969 原 degree378 canonical 必要行。二挠第四 Miller、CM 有理比、O增加六零、\(\pm S\) 与二挠全部阶均保；增加的六零抵消表面六极。完整四次 Cartier 和39支 differential trace 返回同一首行；\(\operatorname{Norm}_\alpha(y)=c_\alpha y\) 使对数方向 trace 标量为1，一般微分仍是 \(39/\alpha\)。theta 中间载体为三个 rank13/degree126 稳定项，不能冒390/39得degree10。

R1053§§8–11现已付真实 reader 到原 P10 的完整39字符配对：Gα的全除子、二挠194d_p−8p极帽及全部非齐次连接费用保留。十三维4jet与原39维长12修改均准确，但不是native极帽。source390与target10的p曲率不匹配，排除免费scalar CM/Miller交织，相关水平Hom为零；该事实不推出canonical非零。下一须真正消费完整配对及费用，或回同一个M/R的实际Schur消元。geometry继续common A24与A18行，不重走已排gauge；不能用环境六阶矩填canonical授权。R1021两δ-new来源、R1022全39支、R1025六权和末两H组合、R953/954全混合界继续按已付范围；坏条件尚未迫所需单位组合为零。

## O相对 / O角：common A24、mixed 除 p 与完整 K/Y 方向

[R1055](results/R1055-original-a24-relative-fiber-and-complete-two-trace.md)已付原 \(T=A_{24}H_{48}\) 相对片的全 \(T_2\)、后继 \(T_\delta\)，准确剥出 \(R_{144}\) 的 old 部分。原 \(J_{1,p}/p\) 仍包含 degree12、两个明定 new 余项及低卷积；\(J_{p,1}/p\) 同时保留。要付余项的真实 finite 来源和原算术返回，不能免费交换 trace 与除 \(p\)，或从相乘关系推新的 \(J\) 零行。

R1040 的原模型/全 HJN 平均、\(\Phi_{126}/\Xi_0\)、G126/\(\Xi_1\) 和 \(J_{G,0}\) 单位保留；未授权 \(J'_G=0\)。R1046 的 K/Y 非零、R1047 norm25 的四 even 角色一次项及 Fuchs–Pham/全尾已付，canonical 坏尚不迫同一角读数零。

[原完整 unitary 字](notes/2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md)的全部有限来源、逆Gram、两norm3150/150、六sigma、\(p^{1-n}\) 损、mixed cut、wild与补域均保。原§16已给真正球面 Hecke 反例：完整不读K边际恒零，而同一K/Y读数严格非零；这排“完整Y边际加该球面Hecke就迫K/Y零”。不重算该球面和。下一须真正读K的同解内关系、完整5-old canonical/reference 系数和5-new/p-new补项。

R1055附录现付同一个 \(H_{102}\) 与原四伙伴的全部有理关系：
\(\Phi_{126}^2S^3=\mathscr R\,T^4V\)、\(\Phi_{126}S=\mathscr Q\,A_{24}U\)。
全部有限极、charge、Gaussian和carry保持。实际 E3969 必要零行严格是这个同源唯一平方根的完整 Newton 加权行；下一须在原真实 Schur 行及同一个饱和修正中找到不可消约束，不能将 E 当第五自由高轴，也不由乘积推出新零条件。

## O几何：原54图的全局 normal function 与有权 Manin

原54/27图、η/Cor、最高λ、负9-Weil、两cover及Prym全保。R1039全Jac \(F^2=-q\)、R1041无权 \(q+1\)/半交不付最高加权影子。R1043需原三个完整J全零才给原T_a全p整除；canonical坏尚不迫此条件。Fr−unit核只有p个除点，不可改为全p²。

R1049完整 proper FP/Čech/Frob、全NS与CM Hodge、FL局部格均付：\(AJ(Y_{j0})=pI_{j,p}/(p+1)\)，原 \(h_{j,p}=a_{j,p}^{-1}I_{j,p}\)，log格为pO，模 \(p^n\) split iff \(h\equiv0\)。后继已给完整54有权限制、原weight-p CM来源、全type4 toric平方与 \(h^2\) 残余 canonical 平方，全部p损、period、factorial和Artin/full9保持；几何仍保 \(p>q_0\)。下一是这个真实完整和的无穷非零及原通常全Sha桥，不套任意 syntomic 非零或单点挠提升。

[R1057](results/R1057-original-manin-two-torsion-legendre-wilson-boundary.md)把同一原B的二挠 \(P_q(-1/4)\) 精确返回 Rodrigues 整数卷积；Wilson中央段加两短尾的完整Vandermonde和为零。辅助 \(q=6n+5\) 的所需无穷非零仍开，实正性不付模q非零；q单位倍规范Manin值不读另一个目标 \(p\) 的饱和。下一保原17/η/Cor有权返回或真正canonical除p来源。

R984 Griffiths非零不付逐p AJ；R988 K3–E0²和R990 CM17图零范围保留。R979固定7993 Selbal/strict核与R940全双新κ不判端点，Artin/fine Selmer及已核外部定理负边界沿完整归档，不重做已排输入。

## O厚点：唯一原完整 v13，持续消费真实终门

[v12终态](notes/2026-11-27-v12-terminal-and-captured-return-binding.md)已消费21000s/signal15/exit124，完整六612与下一306/Frob/maximal回返；四交/Norm/18×9无终回执。R1050全非约化scalar支撑证明及三项真软件PASS已付，软件PASS不替数学终门。

[v13生产](notes/2026-11-27-original-scalar-filtration-v13-production.md)为唯一heavy：
run46080875647/job140779301767/source277c55dd2c0d36baf665c65700935ac671faa816，23:09:29UTC创建；最新01:19UTC为in_progress；01:25再次GET与00:37及01:03相同的4203375B日志已给本次完整绑定，末行00:18:25到positive scalar base-prime1第222/306列，数学终门仍未返。保全60旧源+5新、两个char0 pins、29/2453/64/minimal/artinian、4CPU/16GB/21000s及全原数学门。必须消费八条本次T/v全HNF、非约化厚长/残域/边界、四交、一般Norm、18×9和九对；不因日志GET404预报结束，不开第二heavy，不存可重算输出。

旧q5/q11全影子倒6零、q11完整NS/Br/MW和Manin回执已付，不重复输入。即便有限完整影子成功，仍须解决主无穷p非零。

## O4、O6、O7与所有其它原门

- O4：原O格 \(Q=\delta^a\varepsilon w\) 需无穷 ordinary \(p\) 有 \(a\le1\)；E17的a偶、E389的 \(\operatorname{length}\Sha_A=2(a+1)\) 不删。
- O6：固定两点饱和λ的全核 \(N_p\) 有限且真 \(q_p=1\) 于无穷p；原Tor、整周期及全部p损保持。
- O7：同解内/闭盘、同Y余数、全Laurent/非恒Y权及全部216管差仍未迫原闭边界全零。
- 原signed绝对整周期只在已付一K单位范围，不能外推跨p非零。全部热jet、半周期连接、paired Lamé/零p曲率不代原p−1及除p后p+1读者；不横向微分单个CM坏条件。

其余全部模型、来源、例外、数学门与失败记录保于开头逐字归档。子问题完成即接下一真实未闭门，达到课题README的完整标准才收尾。
