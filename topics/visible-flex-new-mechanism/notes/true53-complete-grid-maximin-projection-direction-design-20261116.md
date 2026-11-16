# true53 的完整两网 maximin 一阶方向：原物理约束下的半空间投影与全线验收合同

日期：2026-11-16（UTC）。本稿是新的数学子问题、求解机制和源接口设计；没有运行新的数值、人工、Jacobian、投影或标量查询，也未启动 Actions。运行配额由后继唯一 request 单独授权，本稿不重开任何旧额度。

## 1. 唯一基点、已付证据与问题范围

唯一基点是 run43804573954/source ab1ba331a1d376d61e6e9f9b7f29f2bb9221a1e2 的真实接受点 **53**：

- physical SHA256：9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e；
- 两网最大 $\eta=0.26601514422985384$，最大绝对主曲率57.9992694544513；
- 原两网14门及原163维精确物理盒已付通过；目标 $13/50$ 仍 false；
- coarse/fine池4448/4549，versions13/14。新fine软行86919、87033、87303、87417、210297及此前159001都保留；
- $B=1/4000$，body/tail/height半径仍为 $B,B/8,4B$，两streak均0；
- bank512、SHA233b2e81fdd0ab36f3306d2d901e8708bb103ea34c9c20ef006537d371634527；
- gamma coarse/fine为57.187653029922444 / 67.42701956990882，learning62 events/61 commits/pending0，SHA b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76；
- 祖先权威科学总钟 **1406.2512530919998秒**，已付普通values126，旧HiGHS64与cone32永久封存。

源稿为 [p32首次实际与accepted53](paid-p32-line-envelope-first-actual-and-accepted53-20261116.md)。其原研究job133092260804的COMPLETE保存完整checkpoint；后置report job133095041106保语义和原指纹。恢复应由runner只读这一最新原研究日志，提取完整53 checkpoint。report中的池和bank摘要不能代替其原数组。

旧first-jet缓存绑定52、旧 $p_{32}$，不能平移标签成为53的线性化；旧62次查询与53旧门均不再重算。**当前53的完整新方向与其所需参数导数尚未支付**。本任务只为新方向模型计算必要新输入，不把它叫旧门复验。

本轮实际说明：$\alpha=1$ 的完整仿射范数包络不改善，不等于整个候选方向不可用。下一问题据此改成：

> 在真实53、原159维物理族、原提案半径和原hard/curvature guard下，能否得到对完整两网全部谱分支共同下降的一阶方向，再在其合法尺度区间内用完整仿射谱线包络选择真正未试点？

这是新的完整两网线性凸子问题。数学上仍属有限维LP类；实现拟采用半空间投影的对偶坐标算法，不调用HiGHS或Clarabel。**不调用这些backend不等于没有求解**：投影会话、prox步骤、半空间更新、全网分离、行导数和实际评价都须真实计费。

## 2. 与此前两个提案问题的区别

| 层次 | 旧有限row scalar LP | 旧finite exact-affine SOC | 本稿 |
|---|---|---|---|
| 软目标 | 已选行的一阶谱标量模型，加外域常量 | 有限已装行的仿射 $e/f$ 范数精确锥模型 | 完整两网每点两分支的一阶模型，当前gap全保 |
| 覆盖 | 有限原pool及后继切面 | 有限cone tags；完整oracle可能抬高$\rho$ | 每个候选均扫描完整两网的线性化目标，不因近活跃行未入master而忽略 |
| 方向求解 | HiGHS | Clarabel | 新的物理度量投影会话；无旧backend调用 |
| 一阶与范数曲率 | 旧标量提案后真实门 | 范数曲率在有限锥内 | 一阶方向后另用完整仿射谱线包络 |
| 实际接受 | 原两网门 | 原两网门 | 同一原精确盒、14门、严格下降 |
| 资源 | 已封64 | 已封32 | 后继request独立给定；全部祖先费用保留 |

本稿不声称一阶模型比完整仿射范数更准确。相反，$\phi$关于$(e,f)$的凸性说明一阶模型通常是其下界；后置完整线包络正是为了处理这个差别。

新机制的实质是**全部当前gap和近活跃峰参加方向问题，并通过完整分离检验；方向不只在全步$\alpha=1$处决定去留**。它不是把旧32或旧64换一个计数器继续跑。

## 3. 原159→163物理归一化和hard域

沿原 frame_entry_tail_height_blocks.py 的 EntryTailHeight159Subspace.scales/build_primary：

- $q_*$ 为source53的独立159向量；
- $M$ 为原163×159物理映射，九个height系数仍由原exact affine map恢复；
- $x_*$为$q_*$在原exact affine map下的真实163物理系数（保原reference常项），$D$为原163物理盒宽度对角阵；
- $Q$为原physical pivot widths对角阵；
- $r=4B$，$S=rQ$，独立提案步 $p=Sz$；
- $K=D^{-1}MQ$，故 $D^{-1}Mp=rKz$。

原pivot满足 $K_{\rm pivots}=\operatorname{diag}(\pm1)$，不以五个height坐标的范数代替九个物理height系数。原physical weights $w_i$ 分别为body $1/4$、tail $1/32$、height $1$。

原 coupled physical box/trust rows逐项保留：

$$
Kz\le \min\!\left(w,\frac{u_{\rm phys}-x_*}{rD}\right),\qquad
-Kz\le \min\!\left(w,\frac{x_*-\ell_{\rm phys}}{rD}\right).
$$

物理gap仍按原exact affine coefficient计算后走原数值提案路径。另保pivot bounds、原物理无穷范数auxiliary

$$
-Kz\le h{\bf1},\quad Kz\le h{\bf1},\quad 0\le h\le1.
$$

原物理step cost系数保持 $\omega=1/1000$，令

$$
\mu=\omega r=\frac1{1000000}.
$$

于是原norm cost仍为 $\mu h=\omega\|D^{-1}Mp\|_\infty$ 的epigraph形式。它不是独立height tau norm。

### 3.1 原hard行与curvature guard

选取source53两池中全部原hard组2–10，保原整数ID、相对顺序、当前base值、原单位tolerance和新的53参数Jacobian。旧soft池本身不删；只是不再拿其有限子集充当完整软目标。

对原hard值 $v_i$、tolerance $\tau_i$，原 fraction-to-boundary $\theta=1/2$：

$$
t_i^{\rm base}=v_i-\theta(v_i+\tau_i).
$$

原strip组4、5及curvature组7–10按原floor $10^{-7}$ 取max。组8再完全按 frame_metric_curvature_defect_guard.py:apply_primary_guard 使用冻结source gamma：

$$
t_i=\max\{t_i^{\rm base},10^{-7},10^{-7}+\gamma_{\rm grid}B^2\}
\quad(i\text{ 为group8}).
$$

相应硬行是

$$
-J_iSz\le v_i-t_i.
$$

其余原hard目标、外域固定hard原门、常cap原容差都沿原函数保留。in-domain零Jacobian行不能因“没作用”而删除；若字面零导行与guard矛盾，应如实报告阻断。也不能将一个数值下溢的norm当成数学零行。

**此guard域未必含零步。** 若 $t_i>v_i$，零步不满足原提案目标，虽然source53真实门已经通过。后续不能把“当前点真实可行”误当“当前点满足更强提案guard”，也不能因为投影难收敛而删guard或放宽floor。

本稿的完整软目标不冒称“完整hard Jacobian域”：hard线性提案仍沿原两池和固定外域规则，最后实际验收仍在完整两网。未选hard行造成的实际失败仍按原learning处理。

## 4. 完整两网的一阶maximin模型

令 $\mathcal J$ 包括粗160×384和细160×768网格的每点两分支，共368640条真实网格分支；另外加一条原正slack下界对应的常量分支 $T=13/50$。

新53第一jet提供

$$
e_j=U_j\cdot U_j-1,\qquad f_j=U_j\cdot T_j,\qquad
n_j=\sqrt{e_j^2+4f_j^2+\epsilon^2},\quad
\epsilon=10^{-8}.
$$

符号分支 $\sigma_j\in\{+1,-1\}$：

$$
\phi_j^0=\frac{\sigma_je_j+n_j}{2}.
$$

其真实参数一阶作用为

$$
g_jp=
\frac12\left(\sigma_j+\frac{e_j}{n_j}\right)d_e[p]
+\frac{2f_j}{n_j}d_f[p],
$$

其中

$$
d_e[p]=2U\cdot\delta U[p],\qquad
d_f[p]=T\cdot\delta U[p]+U\cdot\delta T[p].
$$

分母只用原正$\epsilon$保证定义，不除以$f$。设

$$
\Phi_*=\max\{T,\max_{j\in\mathcal J}\phi_j^0\},\qquad
\delta_j=\Phi_*-\phi_j^0,\qquad a_j=g_jS.
$$

常量target分支为 $a_*=0,\delta_*=\Phi_*-T$。外support分支同样按原支撑定理保 $a_j=0$；不按“小J”阈值分类。

完整一阶提案的共同净改善是

$$
d(z,h)=
\Phi_*-\left[\max\{T,\max_j(\phi_j^0+a_jz)\}+\mu h\right].
$$

新数学问题为

$$
\max_{z,h,d}\ d
\quad\text{s.t.}\quad
a_jz+\mu h+d\le\delta_j\quad\forall j,
\quad (z,h)\in P_{\rm hard}.
\tag{1}
$$

这正是完整两网的一阶正slack/原物理norm成本模型，非只对已经达到最大值的一条梯度作下降。所有未活跃行的 $\delta_j$ 都在(1)中，近活跃峰无须被武断设为exact active才能参与约束。

采用 $d=\mu s$，变量 $w=(z_{159},h,s)$ 共161维。metric行是

$$
(a_j,\mu,\mu)\,w\le\delta_j.
\tag{2}
$$

所有原hard、box、trust、norm行的$s$系数为0。target常量行保证原$\rho\ge0$的成本下界，不在新模型里悄悄去掉它。

问题(1)的有解性不预授：hard guard可能使$P_{\rm hard}$为空。有限浮点算法未找到可行点不构成不可行或驻点证明。

## 5. 不调用旧backend的投影求解路线

### 5.1 原物理度量

取

$$
G=\operatorname{diag}(K^\top K,1,1).
$$

由原pivot恒等式，

$$
z^\top K^\top Kz=\|Kz\|_2^2\ge\|z\|_2^2.
$$

所以$G$严格正定。原154 tangent块为单位块，只有height五维块需非平凡小矩阵作用；全部九个height物理贡献仍在$K^\top K$中。无需引入大dense metric Jacobian，也不为“可逆”偷偷加jitter。小块若数值分解失败，应报告失败，不能改变物理映射。

令 $\mathcal D$ 为(2)及全部原hard域的闭凸交。方向solver外层使用

$$
y^{(k)}=w^{(k)}+\tau e_s,\qquad
w^{(k+1)}=\operatorname{Proj}_{\mathcal D}^{G}(y^{(k)}),
\quad\tau>0.
\tag{3}
$$

$\tau$只是新算法步长，必须在新request声明；它不修改(1)、原半径或guard。推荐的源接口不提供未声明的默认迭代上限或fallback旧LP。

若当前$w^{(k)}$已可行且投影精确，则投影变分不等式给出

$$
s^{(k+1)}-s^{(k)}
\ge \frac{\|w^{(k+1)}-w^{(k)}\|_G^2}{\tau}\ge0.
$$

第一轮不能用此式，因为guard域可能不含初始零步。更关键的是，精确固定点

$$
w=\operatorname{Proj}_{\mathcal D}^{G}(w+\tau e_s)
$$

等价于 $v_s\le w_s$ 对所有$v\in\mathcal D$成立，即(1)的全局maximin最优点。这是数学模型性质，不授有限浮点运行已到固定点。

### 5.2 每个投影的半空间对偶

对于当前有限master的行 $A_iw\le b_i$，投影问题为

$$
\min_w\frac12\|w-y\|_G^2
\quad\text{s.t. }Aw\le b.
$$

非负对偶变量$\lambda_i$给

$$
v=A^\top\lambda,\qquad
w=y-G^{-1}v,
$$

$$
D_y(\lambda)=
\lambda^\top(Ay-b)-\frac12v^\top G^{-1}v.
\tag{4}
$$

每次仅更新一条半空间：

$$
\kappa_i=A_iG^{-1}A_i^\top,\qquad
\lambda_i^+=\max\left\{0,\lambda_i+\frac{A_iw-b_i}{\kappa_i}\right\},
$$

$$
w^+=w-(\lambda_i^+-\lambda_i)G^{-1}A_i^\top.
\tag{5}
$$

对$\kappa_i>0$，(5)是该对偶坐标的一维二次问题的精确最大化式。它保$\lambda\ge0$且在精确算术下不降低(4)。每条新metric行只需首次计算一次其真实159梯度及$G^{-1}A_i^\top$，后继坐标更新复用。

允许为了浮点安全按显式正二次幂缩放行，但必须保原行/原单位残差和对偶缩放映射；不能裁剪负残差或按小norm丢行。literal零行单独处理。非有限值、下溢到不可用$\kappa$、负gap等原值均保存，不自动归零。

新prox中心改变时，必须从 **新$y$与当前对偶变量重算** $w=y-G^{-1}A^\top\lambda$。不能保旧$w$再假装其属于新中心。旧对偶非负性可温启动，旧投影“完成”标签不能传到新中心。

这些都是新的数值求解工作。必须分别记录projection session、prox步骤、完整/部分sweep、坐标更新、行归一化/小块因子分解及其实际秒数；不得仅因没有backend就写0solver。

## 6. 全网分离、稀疏表示与有限证书

### 6.1 全部gap始终存在

master初始保全部原hard/physical行和target常量行。可用当前四branch maxima作为metric初始行，但这只是计算起点。

对于任意当前$z$，取$p=Sz$，以新53的固定first-jet对象进行一次真实完整方向扫描，计算两网所有

$$
R_j=a_jz+\mu h+\mu s-\delta_j.
$$

一次分离必须覆盖完整61,440/122,880点、两分支及原target常量。不能用已选pool最大值代替，也不能只查看上轮87417。所有当前gap都由同一冻结$\Phi_*,e,f$计算；不是用新候选点的函数值重写旧gap。

完整metric分离使用原 metric_row_tolerance=1e−9；其它原单位门另按原定义。若全网最大残差超过该阈值，则按原grid/group/flatID取真实最大违例行，必要时每branch各取其最大行，计算新行梯度并加入master。已装的hard与metric行不删除。多个相同row出现不能借反复append冒作进展。

如果完整最大行已经在master中而仍违反，说明当前有限投影尚未收敛，或row/JVP链有不一致；应继续原inner工作或报告具体错误，不能授“无新行所以完成”。

每条新row的 $a_jz$ 与已付该方向扫描中的同row导数，必须用原相对容差 $5\times10^{-12}$ 对照并记录，不额外调用一次JVP来制造检查。若不同，不以新policy hash掩盖；当前state/width/map/B/epsilon/grid/row必须一致。

### 6.2 未装行不破坏对偶下界

未装metric行的对偶变量取0，因此任何当前$\lambda\ge0$都仍是**完整**投影问题的合法对偶点。完整原问题的下界(4)不是“有限master下界冒全网”。

但原问题的primal上界必须由候选通过全hard检查和完整metric分离后才能取得。只有已编译行通过，不能授完整primal可行或小gap。

另可从当前metric multipliers $\ell_j\ge0$、hard multipliers $\nu_i\ge0$给(1)的上界。令 $L=\sum_j\ell_j>0$，对$x=(z,h)$定义

$$
v_x=\sum_j\ell_j(a_j,\mu)+C^\top\nu.
$$

以原pivot box和$0\le h\le1$组成易算外域$X$，则每个真实可行点满足

$$
d\le U(\ell,\nu)
=\frac{\sum_j\ell_j\delta_j+\nu^\top b-\min_{x\in X}v_x^\top x}{L}.
\tag{6}
$$

外域的线性最小值按每个原上下界端点求和，不需要LP。这里所有$\delta_j$继续出现；丢掉gap会改变模型及上界。当前有限行的非负multiplier零延拓即可用于(6)。

全网可行候选的实测 $d_{\rm full}$ 与(6)可提供maximin上下界诊断。本文的推导是在精确模型算术中；实际binary64残差/对偶间隙不是自动的严格区间证书。未另做有界舍入/有理证书时，不得用小负gap或finite budget退出宣布精确不可行、全局无下降或真实几何驻点。

### 6.3 原单位门与候选保存

实际数值仍使用原 linear_model_residual_limit=1e−7、原物理精确盒以及明确的新完整分离门；不把投影内部归一化残差当原单位残差。每次对外返回的有限候选保存：

- 原161向量$(z,h,s)$、实际独立159步、源53与新模型绑定；
- 全网当前最大残差、各branch原attainer/当前gap、全部原hard/box/trust residual；
- 原始及修复后的$h,d$、浮点primal/dual值与gap，是否真完成完整分离；
- 完整solver状态、已开始的各类调用数与实际耗时。

最终是否有一阶下降必须读完整扫描重算的$d_{\rm full}$，不能只读投影变量名义值$\mu s$；$d_{\rm full}\le10^{-10}$时不授合格一阶下降。可以在不改$z$的前提下把$h$调整为本次真实物理norm、把$d$调整为已付完整maximin值，但必须重新检查原行/bound残差，保修复前值；不能裁剪到边界伪造可行。原$\rho$/norm丢失的问题不能在新输出重复发生。

候选rounding后若实际$p=\operatorname{apply}(q_*,p_{\rm ideal})-q_*$改变了方向hash，则所有最终分离与线缓存都必须绑定这个真实$p$。不能让理想$p$的缓存证明实际另一个$p$；必要的最终方向重扫要真实计费，不假称cache命中。

## 7. 后置完整仿射谱线包络与合法尺度区间

### 7.1 一阶全网下降为什么有用

如果完整一阶模型在$p$处严格下降，则特别对每个精确当前active分支都有 $g_jp<0$。因此完整平滑仿射谱包络

$$
\Phi_p(\alpha)=
\max\left\{T,\max_j
\frac{\sigma_j(e_j+\alpha d_{e,j})
+\sqrt{(e_j+\alpha d_{e,j})^2+4(f_j+\alpha d_{f,j})^2+\epsilon^2}}2
\right\}
$$

在0处的右导为所有active斜率之最大，并严格为负。在模型算术下存在一个正的小区间下降。每个分支凸，有限最大值凸；前述[完整线包络纸证](paid-p32-complete-grid-line-envelope-convexity-20261116.md)的结论仍适用。

这不保证$\alpha=1$改善，也不保证实际非线性几何通过，更不保证下述guard允许区间必与下降区间相交。

### 7.2 不能默许任意缩小步都保guard

对某原hard行，记当前值$v_i$、冻结目标$t_i$、本方向斜率$b_i=J_ip$。数学合法尺度满足

$$
v_i+\alpha b_i\ge t_i.
\tag{7}
$$

$b_i>0$给下界；$b_i<0$给上界；$b_i=0$时若目标不满足则全线被阻断。因部分$t_i>v_i$，合法$\alpha$可能必须大于正数。

实际实现必须明确保两份记录：原未放宽目标(7)，以及沿原浮点linear_model_residual_limit=1e−7的同一原单位门。若使用其数值允许域，公式把右端换成$t_i-1e−7$，这是原门，不是新加宽容差；原目标和实际残差仍原样报告。exact163 box不会因这个浮点门获得容差。

将所有原hard条件、$[0,1]$和原物理域取交，得到本方向的合法尺度区间$I_p$。物理盒在精确连续仿射线上的凸性仍保，但每个rounded实际试点仍需原精确163盒重新判断。

- $I_p$空：0标量优化、0真实trial，报告具体阻断行；
- $I_p$单点：只收费一次该点完整模型查询，不能冒作已优化区间；
- $I_p$为区间：仅在该区间求完整线包络；基准仍是**真实0处$\Phi_*$**，不是把$I_p$左端改作新基准；
- 原0基准若不在$I_p$中，仍可作为一次单独的已声明模型基准查询；计入新查询总账；
- 不允许在合法区间找不到模型下降后自动越界试小步、减guard、增B或重开SOC。

归一化到原scalar接口时，$t\in[0,1]$映到$\alpha=\alpha_{\min}+t(\alpha_{\max}-\alpha_{\min})$。必须保真实$\alpha$、原0基准和计数，不能重演“新区间0等于物理零步”的身份错误。

### 7.3 实际接受与本任务终止

最终候选必须有完整观测模型下降超过原floor1e−10，才值得进行未试点实际几何。真实接受仍是：

- 原same rounding 159 apply、原exact163 box；
- 原完整粗细两网14门、未改g/b0/锚/height/曲率58；
- 真实$\eta$严格下降，且原最小下降1e−7或两新target均达标的原例外；
- 原value-only学习加入真实新行；失败有新行/容量问题时停止该方向，不删除学习。

本稿不授权新SOC、旧controller重置、gamma再训练或bank上下文改名。最小新实验只输出一个新方向及其一次线会话；具体未试fraction数量由新request声明。源53旧门只读；所有新真实试点完整159/163向量与两网输出都在原stdout保留。

## 8. 具体源接口与最小新计算范围

### 8.1 原函数复用边界

| 原源码/入口 | 复用内容 | 本方法不会调用的旧工作 |
|---|---|---|
| frame_entry_tail_height_blocks.py: scales/_physical_gaps/build_primary | 原M/K/物理box/trust/norm/retention及hard目标 | 不调用旧solve_primary或旧LP ledger |
| frame_metric_curvature_defect_guard.py: apply_primary_guard | 固定gamma、同B、group8原目标/RHS | 不commit_pending、不重新训练旧样本 |
| frame_selected_row_radial_jacobian.py | 原complete theta算子、row顺序与factorized selected J | 不构造旧全163 dense J |
| frame_selected_row_metric_observables.py | 新attainer真实de/df与原159列序 | 不复算旧52已付列 |
| frame_metric_affine_spectral_model.py: phi/phi_gradient | 原epsilon及branch导数原式 | 不调用旧affine inner solver |
| frame_metric_p32_line_envelope.py 的已证底层数据流 | 原U两次加法、direction_frame_jets、complete-grid谱查询公式 | 不把p32专属wrapper/identity假作新53模型 |
| 原direct-reference geometry159/height gate | 新model必要current jets；实际trial全门 | 不另跑53旧门套件/初末审计 |
| 原subspace.apply/exact_box_decision | 原rounding与物理height exact map | 不换reference或自行截断physical向量 |

新模块必须有新policy/evaluation identity，引用原field/config/source SHA；不能假装新完整方向仍是旧affine primary或旧52 cache。实际source53的value-only objective身份也不能替代新模型身份。

### 8.2 建议纯源接口

1. Current53FirstJetBase：一次安装真实source53、原reference163、完整原theta/radial网格；返回冻结$e,f,\phi^0,\Phi_*,\delta$及元数据。原old52缓存不传入此构造。
2. CompleteFirstOrderSeparator.direction(p)：原全theta算子产生$d_e,d_f$并计算所有$R_j$，保四branch最大值、原attainer、完整gap和真实p哈希；完成或异常均收费。最后合格方向的数组可直接转线缓存，不能再做同一方向JVP。
3. MetricRowOracle.row(tag)：只对新master attainer生成159梯度；保原grid/group/flatID、base53、scale、epsilon与链式对照。已装同row同binding复用。
4. OriginalHardDomain：原硬池/原物理映射/guard的不可变行集合，原数组hash、原单位残差与所有zero-J行记录。
5. ProjectedMaximinSession：显式projection ledger、(3)–(5)、全网分离、候选原161保存和(6)诊断。任何终止原因保原收费，不调用fallback LP/cone。
6. GuardCompatibleLine：由真实$p$与冻结hard域得到$I_p$；复用最后完整方向数组完成原谱线查询，另列scalar会话/查询。
7. ActualTrial：只对未试、模型合格、guard允许的尺度调用原真实门。下一点若接受，索引必须明确从53起，不伪造旧accepted arrays。

这些是接口设计，尚未授源码/人工实际通过。

### 8.3 必要的新53导数与旧门禁止重跑并不矛盾

source53原stdout没有完整可直接绑定的新hard-row导数缓存。构造当前53的hard Jacobian可能需要原当前position/two-jet参考数据；它们必须明列为**新模型必要几何/导数建造**并实际收费，不能用旧14门摘要伪造cache。

应只建立新模型实际需要的一份current jets，给选中hard行、metric attainer与全网分离共用；不额外调用一次旧accepted_point/初始审计/独立末审计来“确认53”。若现有原接口只能通过一个完整普通geometry调用得到所需current jets，该调用也必须作为新实际started geometry/费用记录，不能因为用途是J就记成0。

最小scope拟为：新53一份完整两网first-jet base；一份原selected-hard导数域；一个方向优化session（内部次数有明确上限）；一个合格方向的线会话；有限未试actual pairs。全部原对象在同一runner复用，不跨run存数组。若必要current jets仍过贵或原接口不能不重做大量无关值，应先报告具体缺口，不绕计费。

## 9. 生产计数、祖先费用和失败输出

新request必须给独立上限，至少包含：

- total new science seconds，起点在本次输入/准备前，包含新dev、读源、建造、projection、J/JVP、线查询、actual、serialization/stdout；
- new development seconds及准确新增case数；
- base first-jet/two-grid构造次数；
- 必要current geometry started/completed/failed与selected-hard J构造；
- projection solver sessions、prox steps、coordinate updates/sweeps、small-factor solves；
- full-grid direction separation调用与实际两grid计数、cache hits、失败收费；
- new metric-row J次数及真实原ID；
- scalar sessions、全部envelope queries（含0基准、端点、导数、重复值）；
- actual trial points与完整grid geometry调用；
- 新LP/SOC/cone调用上限固定0，旧64/32账永远封存。

旧configuration中64/160/1800/10是历史定义的一部分，不能被新算法拿来重开额度或回填历史。祖先科学1406.2512530919998、values126和已有所有失败费用原样保留；新科学与总累计分别报。旧cone968.6757049859999是已包含的历史分项，不再加第二次。旧资源是否仍有算术“余额”不自动成为本方法授权。

每个昂贵调用开始前登记，异常/提前退出也保已开始数、实际elapsed、最后有限候选/原161和最后真实接受点。预算满、projection未完成、同row持续违反、fullgrid不下降、合法$I_p$空、actual门失败分别保状态；不能一律写“stationary”。

所有大输出后的权威FINAL_CLOCK继续使用当前已验证的做法；较早checkpoint不替代最终累计时钟。Actions UTC job时间与进程科学钟分别报，不擅解释差额。

## 10. 新开发的必要范围与最终判断边界

后继开发只覆盖新逻辑，不能重跑旧3个scalar case、旧9/11/12/6或tiny cone。必要内容限于：

1. 半空间对偶更新/物理度量/原单位残差：有手算答案的小多面体，包括guard域不含0；
2. 全gap分离：一条非当前最大但gap很小的遗漏行会阻断错误方向，补行后不能删除已有hard约束；literal零行矛盾与预算退出保原状态；
3. 非零下端合法区间：变换后的scalar参数0不是物理零步，原基准和所有查询收费保持；空区间不调用scalar或actual。

原row梯度对本方向JVP的对照应放在真实新建行的已有数据上，不再调用几何造一套重复测试。具体case数和预算要在源及request冻结时明确，本文没有执行这些检查。

本方法若给出一个完整分离合格方向并在原14门下接受新点，才算新的实际推进。若只得有限primal/dual残差或未解projection，只能报告该新子问题的已观察边界。即使完整一阶模型最优性有数值支持，也不能直接推出原非线性几何在159维空间驻点，更不能推出全部曲面族不存在更好构造。

本稿解决的是下一方向模型怎样完整、可审地支付当前所有谱分支，以及怎样保原guard接上完整线包络。它不重开旧科学、不预报true54，不为发布制造新的review或执行闸。
