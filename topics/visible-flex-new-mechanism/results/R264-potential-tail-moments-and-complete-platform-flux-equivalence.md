# R264：全第三核的真实势尾矩与平台—总通量联合判据

日期：2026-11-15。**完整纸面证明；没有新的研究计算或人工执行。** 本文把 R260 的准确 Green 边界式进一步化成原右锚的势尾矩，并在 R225 的有限活动区间类上给出“全部平台加全部总通量”的必要充分条件。适用对象现在是 R261 已支付的完整十八维第三对角核。

来源：[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md)、[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R260](R260-actual-activity-flux-green-boundary-and-step-baseline.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)。

## 1. 完整算子、真实右锚与输入范围

固定共同区间 $I=[\ell,r]$。seed $f$ 在两个外 collar 全平为零；输入 $w$ 在整个 $I$ 光滑，允许其原式带真实左多项式尾，不要求它紧支撑。令

$$
\tau\in Z=\mathfrak H_7\oplus\mathfrak J_3\oplus
\operatorname{span}\{\chi_{30},\chi_{32},\chi_{34},\chi_{37},
\chi_{40},\chi_{100},\chi_{104},\chi_{109}\},\qquad
G=K_f^\tau(w).
$$

R258 与 R261 给出完整原函数身份

$$
G'''=\mathscr A w,\qquad
\mathscr A=D^2(aD^2)+D(bD)+c,\qquad
\mathscr A^*=\mathscr A,\qquad \mathscr A f=0.
\tag{1}
$$

$a,b,c$ 是关于 $f$ 的有限 jets 的二次齐次局部系数，允许显含 $x$。原恢复为

$$
G=-\mathcal J^3\mathscr A w,\qquad
\mathcal J h(x)=\int_x^r h(\xi)\,d\xi.
\tag{2}
$$

共同右 collar 上 $G,G',G''$ 全零。全部 $a,b,c$ 也在那里为零。下文不改变这个锚，不在每个活动区间重新选择积分常数。

对 (1) 从右端积分一次，得到

$$
\boxed{G''=(aw'')'+bw'-\mathcal J(cw).}
\tag{3}
$$

这里 $D\mathcal J=-1$。式 (3) 的符号及积分常数都由原右 collar 唯一确定；仅知道 $G'''$ 而随意附加一个二次多项式不能代替 (3)。

## 2. 种子湮灭决定一个真实尾恒等式

置

$$
d=(af'')'+bf'.
\tag{4}
$$

由 $\mathscr A f=0$，有 $d'=-cf$；而 $d$ 在右 collar 为零。所以

$$
\boxed{d=\mathcal J(cf).}
\tag{5}
$$

这不是对各个平台独立选择的 primitive。特别地，若 $f$ 在某个平台为常数，则所有正阶导数为零，(4) 给 $d=0$，因此该平台上真实的 $\mathcal J(cf)$ 也准确为零。

R260 的完整 concomitant 是

$$
\mathfrak B(v,w)=v(aw'')'-v'aw''
-w(av'')'+w'av''+b(vw'-wv'),
\qquad
D\mathfrak B(v,w)=v\mathscr Aw-w\mathscr Av.
\tag{6}
$$

代入 $v=f$，再用 (3)–(5)，原通量势可准确化成

$$
\begin{aligned}
\Lambda
&=fG''-\mathfrak B(f,w)\\
&=\boxed{a(f'w''-f''w')+
w\mathcal J(cf)-f\mathcal J(cw).}
\end{aligned}
\tag{7}
$$

其导数为

$$
\Lambda'=f'G''.
\tag{8}
$$

因此每个活动区间 $(a_j,b_j)$ 的真实截左通量满足

$$
\mathcal F_j(x;G)=\int_{a_j}^x f'G''
=\Lambda(x)-\Lambda(a_j).
\tag{9}
$$

式 (7) 保留输入 $w$ 的真尾；式 (9) 保留活动左端的真实常数。两者均不把全带积分与逐活动积分混同。

## 3. 常平台上的尾值与活动总通量

现在明确采用有限活动分解

$$
P_0,\ I_1=(a_1,b_1),\ P_1,\ldots,
I_N=(a_N,b_N),\ P_N,
\tag{10}
$$

其中平台按原次序排列、具有正长度，$f|_{P_j}=F_j$ 为常数，活动端全平接合；外平台 $F_0=F_N=0$。不宣称任意光滑 $f$ 都自动有这样的有限分解。内部 Laurent 应用另按 R225 的解析、有限阶退化假设。

每个平台上 $c=0$：当 $F_j\ne0$，由 (1) 得 $cF_j=0$；当 $F_j=0$，$f$ 的全部 jets 为零，局部二次齐次性给 $a=b=c=0$。故

$$
T_j:=\left.\mathcal J(cw)\right|_{P_j}
\tag{11}
$$

是该平台上真实的常数。再由 (5)、(7)，

$$
\boxed{\left.\Lambda\right|_{P_j}=-F_jT_j.}
\tag{12}
$$

由连续性，同一式子也给活动端值。第 $j$ 个活动区间的总通量因此准确为

$$
\boxed{
\mathcal F_j(b_j;G)=F_{j-1}T_{j-1}-F_jT_j.}
\tag{13}
$$

若全部总通量为零，沿有序平台从 $F_0=0$ 递推，得

$$
F_jT_j=0\quad(0\le j\le N).
\tag{14}
$$

反过来 (14) 立即给全部 (13) 为零。因此

$$
\boxed{\text{全部活动总通量为零}
\ \Longleftrightarrow\
F_jT_j=0\ \text{对所有平台成立}.}
\tag{15}
$$

在非零常平台，(15) 强迫 $T_j=0$；在零平台，单靠通量并不强迫它为零。这一差别正是不能用整包零端通量替代内部 step 条件的原因。

定义各活动区间的真实势矩

$$
M_j=\int_{a_j}^{b_j}c(x)w(x)\,dx.
\tag{16}
$$

由于平台上 $c=0$，原同锚尾满足

$$
T_N=0,\qquad T_{j-1}-T_j=M_j,\qquad
T_j=\sum_{k=j+1}^{N}M_k.
\tag{17}
$$

这些是原有序尾的有限表示，不是互相独立的新变量。也没有据其条数宣称观测秩。

## 4. 平台与总通量的准确联合 iff

**定理。** 对 (1)–(10) 的同一 $f,\tau,w,G$，下列两组条件等价。

第一组：

1. 每个平台，包括两个外 collar，都有 $G''=0$；
2. 每个活动区间的真实总通量 $\int_{a_j}^{b_j}f'G''=0$。

第二组：

1. 每个活动势矩 $M_j=0$；
2. 在每个非零常平台 $F_j\ne0$ 上，
   $$
   \boxed{(aw'')'+bw'=0.}
   \tag{18}
   $$

右 collar 的 $G=G'=0$ 已由完整原函数 (2) 给出，不是删去的额外门。

**第一组推出第二组。** 全部总通量由 (15) 强迫每个非零平台 $T_j=0$。零平台上 $a=b=0$，所以 (3) 与 $G''=0$ 也强迫 $T_j=0$。于是所有 $T_j$ 都为零，(17) 给全部 $M_j=0$；再把 $T_j=0$ 代入非零平台的 (3)，得到 (18)。

**第二组推出第一组。** 全部 $M_j=0$ 与真实 $T_N=0$ 由 (17) 给所有 $T_j=0$。在非零平台，(18) 与 (3) 给 $G''=0$；在零平台，$a=b=0$ 同样给 $G''=0$。式 (13) 随即给全部总通量为零。证毕。

这里每一个平台条件都是整个开放平台上的函数恒等式，并非若干采样点为零。非零常平台仍有真实微分条件 (18)，不能把它从“$\mathscr A f=0$”推成对任意 $w$ 自动成立。

对一个零端整 profile 包，(13) 的整包总通量确实自动为零；但若包内存在非零常平台，它的各子活动通量仍有内容。即使包内没有常平台，外零平台 $G''=0$ 仍会要求相应的势尾条件。总通量自动不等于完整 period 自动。

## 5. 通过联合条件后的内部通量分子

假设第 4 节的条件已经支付。在 $I_j$ 内，右方所有完整活动的势矩为零，且 $\Lambda(a_j)=0$，故 (7)、(9) 给

$$
\boxed{
\mathcal F_j(x;G)=a(pw''-p'w')
+d\,w-f(x)\int_x^{b_j}c(\xi)w(\xi)\,d\xi,
\qquad p=f'.}
\tag{19}
$$

$d=(af'')'+bf'$ 仍是同一个局部函数，也等于原 $\mathcal J(cf)$。式 (19) 内从 $x$ 到 $b_j$ 的积分，是由已经证明的右侧势矩零推出来的简化；没有先行重置右锚。

这可直接代入 R225 的原算子求解。令

$$
A_H=6pp''-2(p')^2,\qquad
q_j=\frac{\mathcal F_j(x;G)}{A_Hp^2}.
\tag{20}
$$

为避免混同，本稿 $w$ 是已给定的 $K_f^\tau$ 输入；现在用 $v$ 表示待求的二阶校正，$\mathcal L_fv=G$。在正则子区间，

$$
v'=p\left(C+\int q_j\right).
\tag{21}
$$

若 $p(\zeta)\ne0$ 而 $A_H$ 在 $\zeta$ 为简单零点，内部条件准确为 $F_j(\zeta;G)=0$。其他退化点仍须保全部 R225 Laurent 条件：若 $n_\zeta=\operatorname{ord}_\zeta p$，须消去 $q_j$ 中全部幂 $k\le -n_\zeta-2$ 及 residue $k=-1$。允许的负幂不能因公式看起来有极点就额外排除。

两个真实平端的 $p\int q_j$ 光滑 germ、全 I 双 collar 拼接、以及同一个 $v$ 的第四 ruling 仍须另外支付。第 4 节只完成 R225 四类 iff 中的平台与总通量两类，没有证明另外两类自动。

## 6. 有限控制组合与完整 mixed 历史

若实际响应是有限和 $G=\sum_\alpha K_f^{\tau_\alpha}(w_\alpha)$，所有上述恒等式逐项相加。第 4 节中的势矩应为

$$
M_j^{\rm total}=\sum_\alpha\int_{I_j}c_\alpha w_\alpha,
$$

平台微分项为 $\sum_\alpha\{(a_\alpha w_\alpha'')'+b_\alpha w_\alpha'\}$。联合 iff 对这些总和成立；不能把总和应为零错误加强成每个控制方向分别为零。

R255 的完整两个 mixed 响应仍为

$$
u_d=\Phi_E(f^2-g^2),\quad u_e=\Phi_E(fg),\quad
\zeta=K_f^\tau(g),
$$

$$
D_{E,\tau}=2K_f^\tau(u_d)+4\Phi_E(g,\zeta),\qquad
E_{E,\tau}=-4K_f^\tau(u_e)+4\Phi_E(f,\zeta).
\tag{22}
$$

本文定理直接处理 (22) 中的 $K$ 部分。其余 $\Phi_E$ 历史有自己的平台函数和活动通量，必须与 $K$ 的贡献一起相加；除非先从完整原式证明 $\zeta=0$，不能删除。整 profile 逐包比例类可以使用 R258 的 $\zeta=0$，而“某段 $g$ 常、$f$ 在变”的旧 step 描述本身不能替代该条件。

若采用 $\sin^2\theta\,V_d+2\cos\theta\sin\theta\,V_e$ 规范，E 列贡献为 $E_{E,\tau}/2$。真实规范、同一原锚、全部 history 均保持。

## 7. 结论的范围

本稿给出了全 $Z$ 的准确尾矩表，以及这些 $K$ 输出的平台和总通量联合必要充分条件；没有新 rank 结论。R261 已支付八个额外方向，所以本文的十八维范围是已证明的，不是把 R260 的十维结果未经检查外推。

它没有证明 $B(E,Z)$ 覆盖完整 $\mathcal R_{p0}$；尤其 $\mathcal R_{71}\cap\ker\pi$ 的其余部分不能删除。完整 period 障碍商、内部 Laurent 与平端 germ、真实带符号成本实现、同一二阶校正的 ruling，以及最终固定度量有限族仍未完成。

原临时稿在终端环境断连后不可读取；本文件按已经核清的完整数学关系重新编辑。没有声称恢复原临时文件的字节或摘要，没有以新编辑稿替代任何已发布科学数据。
