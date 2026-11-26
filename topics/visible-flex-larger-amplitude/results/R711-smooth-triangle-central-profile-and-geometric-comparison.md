# R711 — 平滑三角型中央相位：全部正均值半径、近最优转角斜率与完整几何比较界

2026-11-26。**已证明：在 R709 的同一准确均值根条件下，一个明确的平滑三角型中央 profile 覆盖全部 $0<r<1$，保持单位长度、准确三分量闭合和全部原端口，并在所列 scalar 相位类中给任意接近最优的最大一阶转角。** 本文给出准确场位置、握持预算和真正曲率上界的比较公式；这些公式不自动证明实际新场有更小曲率、已嵌入或已满足 README。

本结果不改已排的五段 seed、其工作缓存或原求解目标。它是独立下一输入机制的完整解析基础。当前没有本地数值实验或本方案科学执行。

本文使用已登记的 [R708：支撑内单位 meridian seed](R708-supported-unit-meridian-seed-contraction.md)、[R709：无需收缩的全局凸均值闭合](R709-global-convex-mean-closure-without-contraction.md)、[R710：完整两角 jet 费用链](R710-supported-unit-seed-complete-angular-jet-error-bounds.md)，以及 [R707：固定 normal 链误差传播](R707-fixed-normal-chain-root-jet-error-propagation.md)。这些引用只提供明确列出的输入与费用责任，不继承另一场的数值或几何证书。

## 1. 固定不变的均值对象

保持 R708/R709 的原准确 $g$、符号域、原核心与高度、两段支撑、四个端层及其 $\chi$。三均值方程
$$
L_cv+B(Nv)=K
$$
完全不变。因此，只要该准确方程的假设已付，$v(\phi)$、$r=|v|$、$d=v/r$ 和同一个极向量投影架
$$
w={e_r(\theta_0)-(e_r(\theta_0)\cdot d)d\over
 |e_r(\theta_0)-(e_r(\theta_0)\cdot d)d|}
$$
都与中央 profile 的选择无关。

改变的仅是每个中央物理区间 $I_i$ 中的相位形状。设其准确长度为 $\ell_i>0$，用归一化坐标 $t\in[0,1]$ 写
$$
T(t,\phi)=\cos\alpha(t,\phi)d(\phi)+\sin\alpha(t,\phi)w(\phi).
$$
本文的 $\delta$ 只指这个归一化中央 profile 的参数，不是外部四端层的物理宽度。外部支撑、端层和全部原自由变量没有缩小。

## 2. 明确的平滑三角 profile

记 $a=1/4$，固定 $0<\delta<a/2=1/8$，并设
$$
S_5(x)=10x^3-15x^4+6x^5,\qquad
I_5(x)=\frac52x^4-3x^5+x^6.
$$
$I_5'=S_5$，$I_5(1)=1/2$。在一个 quarter 上定义速度
$$
g_\delta(t)=
\begin{cases}
S_5(t/\delta),&0\le t\le\delta,\\
1,&\delta\le t\le a-\delta,\\
S_5((a-t)/\delta),&a-\delta\le t\le a.
\end{cases}
$$
这是非负 $C^2$ 函数，内点严格正，端点的值、一二导均为零，并且关于 $a/2$ 对称。两 ramp 各积分 $\delta/2$，故
$$
\int_0^a g_\delta(t)\,dt=a-\delta=:c>0.
$$
令 $H_\delta(t)=c^{-1}\int_0^t g_\delta(u)\,du$。完整可复现的分段公式为
$$
H_\delta(t)=
\begin{cases}
\delta I_5(t/\delta)/c,&0\le t\le\delta,\\
(t-\delta/2)/c,&\delta\le t\le a-\delta,\\
1-\delta I_5((a-t)/\delta)/c,&a-\delta\le t\le a.
\end{cases}
$$
特别
$$
H_\delta(0)=0,\quad H_\delta(a)=1,\quad
H_\delta(a-t)=1-H_\delta(t),\quad
\max H_\delta'=1/c.
$$
在整个单位区间定义
$$
h_\delta(t)=
\begin{cases}
 H_\delta(t),&0\le t\le a,\\
 H_\delta(2a-t),&a\le t\le2a,\\
-H_\delta(t-2a),&2a\le t\le3a,\\
-H_\delta(4a-t),&3a\le t\le4a=1.
\end{cases}
\tag{1}
$$
各段连接的值为 $0,1,0,-1,0$，一二导数均为零。事实上 $h_\delta\in C^3$，而且可在两端以零作 $C^3$ 延拓。它满足
$$
|h_\delta|\le1,\qquad h_\delta(1-t)=-h_\delta(t),
\qquad h_\delta(0)=h_\delta'(0)=h_\delta''(0)=0,
$$
以及 $t=1$ 的同样三条端口，且
$$
\boxed{\ \max_{[0,1]}|h_\delta'|={1\over a-\delta}
={4\over1-4\delta}.\ }
\tag{2}
$$
没有忽略任何小 ramp；若数值求积，完整 profile 有十二个正长度多项式 piece。

## 3. 与三角波的顺序关系

记 $\tau(t)$ 为同样四 quarter 上的连续三角波，首 quarter 为 $t/a$。先证明
$$
H_\delta(t)\le t/a\quad(0\le t\le a/2).
\tag{3}
$$
令 $\ell(t)=t-\int_0^t g_\delta$。当 $t\le\delta$，由于 $S_5$ 单调，其在 $[0,t/\delta]$ 上的平均不超过其在 $[0,1]$ 的平均 $1/2$，故 $\ell(t)\ge t/2\ge\delta t/a$。当 $\delta\le t\le a/2$，$\ell(t)=\delta/2\ge\delta t/a$。于是
$$
H_\delta(t)-t/a={\delta t/a-\ell(t)\over a-\delta}\le0.
$$
对称性给后半 quarter 的反向不等式。也有完整一致差界
$$
\boxed{\quad
\|h_\delta-\tau\|_\infty
\le{\delta\over2(a-\delta)}
={2\delta\over1-4\delta}.
\quad}
\tag{4}
$$
证明只需在前半 quarter 用 $0\le\ell(t)\le\delta/2$ 与 $0\le\delta t/a\le\delta/2$，再反射到全区间。

对 $0<\lambda<\pi$，$H_\delta(t)\le t/a\le1/2$ 给
$$
\begin{aligned}
&\cos(\lambda H_\delta(t))
+\cos(\lambda(1-H_\delta(t)))\\
&\qquad=2\cos(\lambda/2)
 \cos(\lambda(1/2-H_\delta(t)))\\
&\qquad\le
2\cos(\lambda/2)\cos(\lambda(1/2-t/a)).
\end{aligned}
$$
这里两项 cosine 的参数都落在其正确单调区间，且 $\cos(\lambda/2)>0$。将前半 quarter 配对积分，得到完整余弦矩
$$
A_\delta(\lambda):=\int_0^1\cos(\lambda h_\delta(t))\,dt
=4\int_0^a\cos(\lambda H_\delta(t))\,dt
$$
满足
$$
\boxed{\qquad
\cos\lambda\le A_\delta(\lambda)\le{\sin\lambda\over\lambda},
\qquad 0<\lambda<\pi.
\qquad}
\tag{5}
$$
同样的配对对平方函数给
$$
\boxed{\quad\int_0^1h_\delta(t)^2\,dt\ge\int_0^1\tau(t)^2\,dt={1\over3}.\quad}
\tag{6}
$$
因为 $x^2+(1-x)^2$ 在 $0\le x\le1/2$ 随 $x$ 减小而增加。以上是完整 profile 积分，不是有限工作权和的替代。

## 4. 全部正均值半径和准确角 jet

对称 $H_\delta(a-t)=1-H_\delta(t)$ 在 $\lambda=\pi$ 时逐对抵消 cosine，所以
$$
A_\delta(0)=1,\qquad A_\delta(\pi)=0.
$$
在 $0<\lambda<\pi$，
$$
-A_\delta'(\lambda)=\int_0^1h_\delta\sin(\lambda h_\delta)\,dt>0,
$$
因为被积函数非负且在正测度集合严格正。因此，对于每个 $0<r<1$，有唯一
$$
\lambda_\delta(r)\in(0,\pi),\qquad A_\delta(\lambda_\delta)=r.
\tag{7}
$$
这覆盖 R709 的全部正均值半径。它不需要旧五段 profile 的 $4\epsilon<r$ 条件；该变化来自一个新的完整中央输入，不是把旧求根失败标成成功。

由反对称性，完整正弦矩为零。于是每个中央段的准确积分仍为
$$
\int_{I_i}T\,ds=\ell_i\,r\,d=\ell_i v.
$$
所有中央段之和仍是 $L_cv$，原准确三分量闭合完全保留。

更具体地，
$$
A_\delta(\lambda)=8\cos(\lambda/2)
 \int_0^{a/2}\cos(\lambda(1/2-H_\delta(t)))\,dt
\le\cos(\lambda/2).
$$
若 $0<r_-\le r\le r_+<1$，则
$$
\arccos r_+\le\lambda_\delta\le2\arccos r_-<\pi.
\tag{8}
$$
sin 在 $[0,\lambda]$ 的凹性和(6)还给
$$
-A_\delta'(\lambda)\ge
\sin\lambda\int_0^1h_\delta^2\,dt
\ge{\sin\lambda\over3}>0.
\tag{9}
$$
因此同一全角根分支继承原 $r(\phi)$ 的正则性和周期/反射。准确一二角 jet 为
$$
\lambda_\phi={r_\phi\over A_\delta'(\lambda)},\qquad
\lambda_{\phi\phi}
={r_{\phi\phi}-A_\delta''(\lambda)\lambda_\phi^2\over A_\delta'(\lambda)}.
\tag{10}
$$
$|A_\delta''|,|A_\delta'''|\le1$ 仍成立。

R710 的三套 scalar 费用链可沿原证明消费这个新 profile，但必须明确替换存在范围和 derivative floor。若实际候选 $0<\widehat\lambda<\pi$，连接候选与真实根的有效下界可取
$$
m_\delta={1\over3}\min\{\sin\widehat\lambda,\,
 \sqrt{1-r_+^2},\,2r_-\sqrt{1-r_-^2}\}>0.
\tag{11}
$$
各项都须向外支付。不能沿用旧 $(1-4\epsilon)\sin\lambda$ 平台界，也不能保留旧 $\widehat\lambda<\pi/2$ 的来源标签。工作求积还须保自己完整权、真实根区间和实际组合闭合容差；$A_\delta(\pi)=0$ 是准确恒等式，不自动把浮点端点矩设置为零。

## 5. 在准确 scalar 相位类中的近最优斜率

对给定 $r\in(0,1)$，令 $\lambda_\triangle(r)\in(0,\pi)$ 是唯一 sinc 根
$$
{\sin\lambda_\triangle\over\lambda_\triangle}=r.
$$
sinc 在 $(0,\pi)$ 严格下降，证明来自
$\sin x-x\cos x=\int_0^x t\sin t\,dt>0$。由(5)，
$$
\lambda_\delta(r)\le\lambda_\triangle(r).
\tag{12}
$$

考虑任何 Lipschitz 相位 $\alpha:[0,1]\to\mathbb R$，满足
$$
\alpha(0)=\alpha(1/2)=\alpha(1)=0,\qquad
\int_0^1\cos\alpha(t)\,dt=r.
$$
记 $M=\|\alpha'\|_\infty$。若 $M<4\pi$，在每个半段上，零端点给
$|\alpha(t)|\le M$ 乘其到最近半段端点的距离；该包络最高 $M/4<\pi$。cos 在 $[0,\pi]$ 递减，因此
$$
r\ge4\int_0^{1/4}\cos(Mt)\,dt
={\sin(M/4)\over M/4}.
$$
由 sinc 的单调性，$M\ge4\lambda_\triangle(r)$。若 $M\ge4\pi$，同一下界自动成立。因此对整个此类都有
$$
\boxed{\quad M\ge4\lambda_\triangle(r).\quad}
\tag{13}
$$
本 profile 的 $\alpha_\delta=\lambda_\delta h_\delta$ 则满足
$$
\boxed{\quad
\|\alpha_\delta'\|_\infty
={4\lambda_\delta\over1-4\delta}
\le {4\lambda_\triangle\over1-4\delta}.
\quad}
\tag{14}
$$
故它在该完整 scalar 类中距离最优下界至多因子 $1/(1-4\delta)$。取明确参数 $\delta=1/128$，因子是 $32/31$；令 $\delta\to0$，下界可由光滑端口 profile 任意逼近。

这是最大一阶相位斜率的近最优结论，不是整张曲面的 principal curvature、reach、度量残差或嵌入最优结论。

## 6. 与当前五段输入的一个严格径向二阶比较

只在同一个 $r>2/\pi$ 下比较当前五段 $\epsilon=1/10$ 和本 profile $\delta=1/128$。两者都存在 $\lambda\in(0,\pi/2)$ 的准确幅度根。记旧根为 $\lambda_{\rm old}$。旧 profile 的准确最大斜率是 $15/(8\epsilon)=75/4$，所以同一个中央物理段上
$$
\max_{s\in I_i}|F_{ss,\rm old}|={75\,\lambda_{\rm old}\over4\ell_i},
\qquad
\max_{s\in I_i}|F_{ss,\rm new}|={128\,\lambda_\delta\over31\ell_i}.
$$
这里比较的是两个准确、零外层旋转、已闭合的单位 seed，故 $F_s=T$、$|T_s|=|\alpha_s|$；没有将工作 normal 误差设零。

由 $A_{\rm old}(\lambda)\ge\cos\lambda\ge1-\lambda^2/2$，
$$
\lambda_{\rm old}\ge\sqrt{2(1-r)}.
$$
对 $0\le x\le\pi/2$，$\sin(x/2)/(x/2)$ 的单调性给
$1-\cos x\ge4x^2/\pi^2$。积分后，
$$
1-r=1-\operatorname{sinc}\lambda_\triangle
\ge{4\lambda_\triangle^2\over3\pi^2}.
$$
结合(12)，得到完整的统一上界比较
$$
\boxed{\quad
\max_{s\in I_i}|F_{ss,\rm new}|
\le {128\pi\sqrt6\over2325}
 \max_{s\in I_i}|F_{ss,\rm old}|
<\frac12\max_{s\in I_i}|F_{ss,\rm old}|.
\quad}
\tag{15}
$$
最后一个严格不等式甚至只需 $\pi<16/5,\sqrt6<5/2$，给常数
$<1024/2325<1/2$。

该结论只在同一准确均值数据、该半径范围、相同中央长度和所列两个 profile 之间成立。它降低了径向二阶向量的全段上界，**不能**直接改写成真正 principal curvature 减半：混合与角向二阶项、法向投影以及 Gram 行列式也会变化。

## 7. 所有原端口、全角选择和局部化

因为 $h_\delta,h_\delta',h_\delta''$ 在中央两端为零，中央 $T=d$、$T_s=0$，并与原端层末端的同样 jet 相接。固定 $d,w$ 的两套角 jet、$\lambda$ 的同一唯一全角分支，以及所有 $\lambda_\phi,\lambda_{\phi\phi}$ 乘积项均保留。对每个中央段，准确总积分及其两角导数都与原 profile 相同：
$$
\int T\,ds=\ell_i v,\quad
\int T_\phi\,ds=\ell_i v_\phi,\quad
\int T_{\phi\phi}\,ds=\ell_i v_{\phi\phi}.
\tag{16}
$$
从帽端积分定义 $F$ 时，上方已完成中央段的差全部为零。因此两个准确 seed 的 $F,F_\phi,F_{\phi\phi}$ 在全部中央段之外**逐点相同**，包括原补集、四端层、核心和帽区。原中圈反射和帽端六 jet 端口由此原样保留。

在一个中央段 $[a_i,b_i]$ 内，令
$$
A_j\ge\sup_{I_i,\phi}
 |\partial_\phi^j(T_{\rm new}-T_{\rm old})|,\qquad j=0,1,2.
$$
利用(16)可从任一端点积分，得到
$$
|\partial_\phi^j(F_{\rm new}-F_{\rm old})(s,\phi)|
\le\min(s-a_i,b_i-s)A_j
\le{\ell_i A_j\over2}.
\tag{17}
$$
各中央段互不相交，故全域误差是各段上界的最大值，不必把两个互不同时发生的内部差相加。零阶还可用
$$
|T_{\rm new}-T_{\rm old}|
=2|\sin((\alpha_{\rm new}-\alpha_{\rm old})/2)|
\le|\alpha_{\rm new}-\alpha_{\rm old}|.
$$
完整两角差按下一节真实公式包围，不能只对零阶相位差积分后冒其导数也一样小。

新范围允许 $\lambda$ 超过 $\pi/2$，可能使 $T_z$ 反向。旧强单调高度条件、避免反向结论和已有嵌入证据不能自动迁移。保留的是单位、闭合、全角对称/周期和端口，实际几何仍由完整新场支付。

## 8. 完整角向 jet 与真正曲率上界

为给出可直接消费的真实曲率界，令 $n=d\times w$，并定义固定架的准确角连接
$$
A=w\cdot d_\phi,\qquad B=n\cdot d_\phi,\qquad C=n\cdot w_\phi.
$$
于是
$d_\phi=Aw+Bn$、$w_\phi=-Ad+Cn$、$n_\phi=-Bd-Cw$。
记
$$
V=-\sin\alpha\,d+\cos\alpha\,w,\quad
q=A+\alpha_\phi,\quad
\beta=B\cos\alpha+C\sin\alpha,\quad
\gamma=-B\sin\alpha+C\cos\alpha.
$$
全部一二角式准确为
$$
T_\phi=qV+\beta n,
$$
$$
T_{\phi\phi}=-(q^2+\beta^2)T
 +(A_\phi+\alpha_{\phi\phi}-\beta\gamma)V
 +((A+2\alpha_\phi)\gamma+B_\phi\cos\alpha+C_\phi\sin\alpha)n.
\tag{18}
$$
由于 $(T,V,n)$ 正交，平方范数就是三个所列系数平方之和，没有三角不等式遗漏。特别可取
$$
U_1^2=(|A|+|\lambda_\phi|)^2+B^2+C^2
$$
作为 $|T_\phi|^2$ 的上界。对二角范数，分别以
$$
u_0=(|A|+|\lambda_\phi|)^2+B^2+C^2,
$$
$$
u_1=|A_\phi|+|\lambda_{\phi\phi}|+(B^2+C^2)/2,
$$
$$
u_2=(|A|+2|\lambda_\phi|)\sqrt{B^2+C^2}
+\sqrt{B_\phi^2+C_\phi^2}
$$
包围三个系数的绝对值，便得 $|T_{\phi\phi}|\le\sqrt{u_0^2+u_1^2+u_2^2}$。这些公式保新 $\lambda_\phi,\lambda_{\phi\phi}$，不能只换一个较小 $h'$ 就沿用旧角 jet 常数。

下面不要求 seed 已等距。准确 $F_s=T$ 单位，令
$$
b_g=T\cdot F_\phi,\qquad
\sigma=|T\times F_\phi|>0.
$$
若实际同场有完整界
$$
|F_{ss}|\le U,\quad |F_{s\phi}|\le V_0,\quad
|F_{\phi\phi}|\le W_0,\quad |b_g|\le B_g,\quad \sigma\ge\sigma_0>0,
$$
则在正交切基 $T,(F_\phi-b_gT)/\sigma$ 中，第二基本形式的绝对矩阵逐项不超过
$$
\begin{pmatrix}
U & V\\V&W
\end{pmatrix},\quad
V={V_0+B_gU\over\sigma_0},\quad
W={W_0+2B_gV_0+B_g^2U\over\sigma_0^2}.
$$
因此真正 principal curvature 的绝对最大值满足
$$
\boxed{\quad
K_{\rm new}\le{U+W+\sqrt{(U-W)^2+4V^2}\over2}.
\quad}
\tag{19}
$$
证明来自上述正交基中的准确二次型变换和绝对值 Rayleigh 界，不把 $|F_{ss}|$ 单独冒完整曲率。

(15)可以降低(19)中的 $U$；$V_0,W_0,B_g,\sigma_0$ 必须由新完整场或下面的已付比较给出。它们可能抵消径向改进，所以没有无条件的 $K_{\rm new}<K_{\rm old}$ 结论。

## 9. 位置、握持和 Gram 正性比较的明确预算

设(17)已给准确全域
$$
\|F_{\rm new}-F_{\rm old}\|_\infty\le e_0,\quad
\|F_{\phi,\rm new}-F_{\phi,\rm old}\|_\infty\le e_1,\quad
\|F_{\phi\phi,\rm new}-F_{\phi\phi,\rm old}\|_\infty\le e_2.
$$
核心、帽和握持对象不变。则
$$
D_{\rm new}\le D_{\rm old}+2e_0,\qquad
\inf|F_{\rm new}\mp p|\ge\inf|F_{\rm old}\mp p|-e_0.
\tag{20}
$$
原两个见证分支都保留。任何非局部点对的距离下界也最多下降 $2e_0$。若握持区本身直径下界为 $G$，则它保持不变，新的 $G/D$ 比值须用 $D_{\rm old}+2e_0$ 重新核算。

例如沿现有明确预算，若同一个准确旧 seed 已证
$D_{\rm old}\le4.2-2e_0$、两支见证下界至少 $.9+e_0$，则新 seed 支付 $4.2/.9$ 这两条预算；否则不能暗改 budget 或借另一场的旧界。本文没有声称目前那个旧 seed 的这些真实连续数值已返回。

再设旧场有 $|F_{\phi,\rm old}|\le Q_{\rm old}$、
$|T_{\rm old}\times F_{\phi,\rm old}|\ge\sigma_{\rm old}$ 和混合量界 $|T_{\rm old}\cdot F_{\phi,\rm old}|\le B_{\rm old}$。若 $|T_{\rm new}-T_{\rm old}|\le A_0$，则
$$
\Delta_c=A_0Q_{\rm old}+e_1,
$$
$$
\sigma_{\rm new}\ge\sigma_{\rm old}-\Delta_c,\qquad
|b_{g,\rm new}|\le B_{\rm old}+\Delta_c,\qquad
|F_{\phi\phi,\rm new}|\le |F_{\phi\phi,\rm old}|+e_2.
\tag{21}
$$
当第一下界确实为正时，可将这些量及(18)直接送入(19)。这给出完整可检验的曲率上界比较，而非仅说 profile 更平缓。嵌入、近点/远点分离和 reach 仍须原同场连续准则；(20)(21)是其输入，不独自替代它们。

上述局部化和预算只直接比较两个准确初始 seed。若当前外层 $\omega$ 已非零，或 normal 校正非零，换参考场会改变所有相应积分/隐式根，必须对完整新场重读。不能把初始 seed 的局部化关系迁给一个未比较的优化末场。工作 seed 与准确 seed 的差则还须 R710 及 R707 的全部费用。

## 10. 完整独立实现的范围

下一独立实现可用(1)的十二个完整正权 piece 计算 $A_\delta,A_\delta',A_\delta''$，使用原实际组合三分量闭合容差，在 $(0,\pi)$ 内真实求根。R709 的均值 Newton、原固定 $K,d,w$、全部原外层 Exp 变量、自由核心/H、完整 normal 分段、原 Gram 行/母范数、全部历史地址、192+幅度行与真实 Phase I 均继续保留。

新的 profile 定义、$\delta$、求积、lambda 区间、源码和完整模型必须有独立身份。原缓存不可跨模型冒用。中央 point evaluator 使用准确分段公式及其完整 $h,h_s$，两角链继续使用(10)和完整(18)，不把新 profile 的参数当物理 flex 时间。

若同时采用已独立核过的最窄 normal 成本省工，只有在已有 enabled=torch.is_grad_enabled() 的 _normal_frame_jets 内，将 autograd.grad 的 create_graph=True 改成 create_graph=enabled；临时 enable_grad、active 全 J/J* 和全部数学方法不删。那仍是独立新源身份，不修改已锁旧源或声称已发生实际加速。

当前尚未形成或执行上述新数值入口，也未以此替换在跑的原 seed。本文完成的是新的准确中央机制、完整正半径范围、scalar 近最优性、严格径向比较和可用几何预算公式；最终 $10^{-6}$、全相位闭面/握持/Euclidean 商/reach 及固定问题加密仍保持原标准。
