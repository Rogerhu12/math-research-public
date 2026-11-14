# R119 续篇：支付额外标签权后的整个实际 connector 精确延拓

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇支付一个明确的更强内部标签范数，把同一精确尾
穿过 R69/R74 **整个已经安装的 connector**，到达 $u=T=2^{24}$ 的真实
径向段末端。它包括 $q=2$ 放大段和准备组，不只包含 R119 的末端组。
额外标签权没有免费加入：下文说明它如何从源 R72 的已证绝对宽度定理
得到，并与 R74 实际线性输入的完整标签费衔接。

本篇没有越过两个 bump 和长径向段到 regular $r=25/8$，没有证明那里
全部 high incoming 的非线性图逆。特别，下面对某个强标签球的前向
延拓，不能反推任意 regular 高度都属于该球的非线性像。

## 1. 实际完整 connector 的长度和轮廓

所有对象取自 [R69 §§4–5](R69-actual-closed-approximate-exterior-and-two-held-disks.md)
和 [R74 §1](R74-actual-full-tail-robin-and-augmented-positive-cap.md)。
R74 的两个 bump 保留右端半径和全部二 jet，只把之后的 connector、
tail 高度作同一常数平移，所以本篇轮廓及方程就是它们的实际轮廓。

仍从 cut128 反向取 $t=\log(r/b)$，$r=a/\rho_*$。现在终时
$L_c$ 为整个 connector 的对数半径长度。R11 的准备组长度小于
$1/3+2\eta$，放大组长度为
$\tfrac12\log(2^{360}/\omega_a)$，$\omega_a>2/3$，末端组长度小于
$1/8$。利用 $\log2<7/10$、$\log(3/2)<1/2$，
$$
 L_c<\frac13+2\eta+126+\frac14+\frac18<127.
 \tag{S.1}
$$
这是 R74 §5 所用同一实际长度上界。全段 $-8\le q\le2$，
$A=q+1\in[-7,3]$。R69 的准确前缀门还给
$$
 \omega>9/10,\qquad 0<a\le a_T<7\cdot10^{-6},\qquad
 w=\frac{a}{4\omega},\qquad 0<w<1,\qquad \frac wa<\frac5{18}.
 \tag{S.2}
$$
因此 R119 (119.8)–(119.16) 的**同一**四分量相对方程及其能源估计
可在整个实际 connector 使用；它们的系数不含参考半径上界。
无需将放大段误称为负曲率或假定其 Cauchy 演化没有角宽费用。

## 2. 额外标签权及其与原 chart 的身份

固定准确数
$$
 \beta=8192=2^{13},\qquad
 \|a\|_{\ell^1_\beta}:=
    \sum_{m\in4\mathbb Z\setminus\{0\}}e^{\beta|m|}|a_m|.
 \tag{S.3}
$$
允许 $\|a\|_{\ell^1_\beta}<1/4$。这里每个 $a_m$ 仍是原实际内部层
$b_m$ 上的同一个标签，不把它换成共同切口 Dirichlet 数据。

源 quantitative-newton-twist-flex 的 R72 §1 已逐项证明：其所有局部
方程、mean、端口 Taylor 常数及固定点对**任意绝对角宽**成立；常数
仅依赖宽度差 $h_j$。因此可以在全部层同时把 $\tau_j$ 换成
$\tau_j+\beta$，输入标签向量为
$a^{[\beta]}=(e^{\beta|m|}a_m)_m$。原内部层编号 $b_m$、
真实矩阵和基 $E_m$ 都不变，因为它们只用 $h_j$，不依赖绝对角宽。

为避免符号混淆，记加权状态为 $X^{[\beta]}$，其标签向量为
$a^{[\beta]}=(e^{\beta|m|}a_m)_m$。则
$$
 \|X^{[\beta]}\|_{\mathcal X}
 <\frac{13}{4}\|a\|_{\ell^1_\beta}<1.
 \tag{S.4}
$$
这确实是原 R115 chart 的限制：去掉每模的 $e^{\beta|m|}$ 后，它满足
原同一物理 PDE、原标签和原单位状态球，固定点唯一性给原 $X(a)$。
完整 mean 由同一 holonomy-one 小根确定，也相同。
等价地，源 R72 §9.1 的卷积证明使用
$e^{\beta|m_1+\cdots+m_k|}\le\prod_i e^{\beta|m_i|}$，故同样的
全频非线性常数在这个加权标签空间有效。

这里付清的是一个更小的标签域。不能将 (S.4) 宣称对所有原无权标签
球自动成立。

## 3. 全组实际角宽和相对小量

仍记 $\tau=5177/400$、$d=9/400$、
$s_* = b^7\delta^{15/4}<2^{-484}$。
在切口先用 R119 的真实状态换算，得到在
$\tau+\beta-d/4$ 上的五项非mean相对范数
$\mathcal R<2^{14}s_*\|X^{[\beta]}\|$。
现在把起始演化宽度选为
$$
 \widehat\sigma_0=\tau+\beta/2.
 \tag{S.5}
$$
所有上述五项都是非零 $4\mathbb Z$ 模，所以限制到此宽度时，实际
因子为
$$
 e^{-4(\beta/2-d/4)}
 =e^{-(2\beta-d)}<2^{-(2\beta-1)}=2^{-16383}.
 \tag{S.6}
$$
零模不能直接乘这个因子。它须重新使用**同一个** mean 小根估计
$|K_0|\le12\mathcal R^2$，从而得到其正确的平方衰减。两种范数下的全纯小根具有同一
幂级数及零值分支，所以这里没有重新指定 mean。
因此完整四状态初值满足
$$
 N_{\widehat\sigma_0}(0)
 <2^{-16367}s_*\|X^{[\beta]}\|.
 \tag{S.7}
$$

取 $\widehat\sigma_1(t)=\widehat\sigma_0-16t$。因为
$e^{32L_c}<2^{8128}$，R119 的全频存在和唯一性证明直接给
$$
 \boxed{\quad
 N_{\widehat\sigma_1(t)}(t)
 <2^{-8239}s_*\|X^{[\beta]}\|
 <2^{-8723}\|X^{[\beta]}\|,
 \qquad 0\le t\le L_c.
 \quad}                                                     \tag{S.8}
$$
它远在完整 $1/64$ 复球内；每段的 same-mean 接合、真实 holonomy 和
完整水平原函数按 R119 §4 传递。全组连续精确解已由此构造。

逐项角宽如下：

| 用途 | 已支付的宽度 |
|---|---:|
| 额外标签权给出的原实际尾状态 | $\tau+8192$ |
| 初始相对物理一阶状态 | $\tau+4096$ |
| 全 connector 最小能源宽度 | $>\tau+2064$ |
| 完整 raw 两迹输出 | $\widehat\sigma_{out}=\tau+2048$ |
| 完整 grounded 两迹输出 | $\widehat\sigma_g=\tau+2047$ |

输出宽度大是由于**明示**限制了标签域，而不是对原无权球凭空增加
角正则性。最后可限制回 R119 的 $\tau-4$ 或有限正帽的物理 $1/512$
条带，范数只减小。这个限制仍不包含 $t=L_c$ 之后的传播。

## 4. 同一外端的全高两迹和 mean

全程采用 cut128 平均高度为0的标签规范及一个独立物理平移 $\lambda$。
在 $t=L_c$ 按 R119 (119.25) 定义完整 raw 两迹，只将 $r_L$ 改为
$r_c=be^{L_c}$，角宽改为 $\widehat\sigma_{out}$。同一 $\zeta$ 不变。

为给完全明确的 norm，粗整数界已足够：
$$
 r<2^{255},\qquad w/w_c<2^{1778},\qquad rw<2^{2033}w_c,
 \qquad L_c<2^7.
 \tag{S.9}
$$
这些仅用 $e<4$、$b<2$、$L_c<127$，不是把它们当作实际采样数据。
初始高度在 (S.5) 上另有非零模因子 $2^{-16384}$，平均高度为0。
积分 $u_t=rwK$ 后，
$$
 \|u\|_{\widehat\sigma_1(t)}<2^{-6198}\zeta\|X^{[\beta]}\|,
 \qquad
 \|u_r\|_{\widehat\sigma_1(t)}<2^{-6461}\zeta\|X^{[\beta]}\|.
 \tag{S.10}
$$
输出还有大于16的角宽余量，二阶和四阶角多项式的乘数均小于1。
所以连同 mean 两行有安全界
$$
 \boxed{\quad
 \|\mathcal B_c(a)\|_{
       \mathfrak C_{\widehat\sigma_{out}}\oplus\mathbb C^2}
 <2^{-6192}\|a\|_{\ell^1_\beta}.
 \quad}                                                     \tag{S.11}
$$
从实际全纯 chart 的方向导数得到的同一输出保留全部 high incoming
标签、全部高输出和真实 mean flux。具体 grounded 接线仍逐字使用
R119 (119.31)–(119.34)，其中 $r,w,Z,R_h$ 现在取**整个 connector 外端**
的真实值。没有把 $(C,C_r)$ 直接当成 $(v,p)$；完整 $\langle\dot G\rangle=0$
来自传到此处的 holonomy。平移列仍准确为 $v=\lambda,p=0$。

由于 $\widehat\sigma_1(L_c)-\widehat\sigma_g>17$，这些公式需要的
有限角导均有实际余宽。它们是给定 chart 的准确两迹公式；本篇不据此
对 regular 端口宣称一个与 R74 同宽的 DN 范数。

## 5. 极小半径没有漏掉物理二阶费用

这里直接用物理半径 $a$，避免把很大的参考 $r$ 与很小的 $\rho_*$
分开估成错误的大费用。相对变量 $P,K,U,V$ 在等比缩放下不变。
在正交极坐标基中，实际高度扰动的 Hessian 准确是
$$
 (\nabla^2u)_{aa}=\frac wa(AK+F_t),\quad
 (\nabla^2u)_{a\theta}=\frac wa(V-P),\quad
 (\nabla^2u)_{\theta\theta}=\frac wa(K+U).
 \tag{S.12}
$$
(S.2)、$\|F_t\|\le15N$ 因而给梯度和 Hessian norm 均小于 $16N$。
初始非mean高度是 $awP$ 的角原函数，平均高度为0；整个物理径向
区间长度小于1，故高度本身小于 $2\sup N$。没有在这里丢掉一个
$a^{-1}$ 或 $\rho_*^{-1}$。

完整水平重建也有相同的取消。用 R119 (119.24) 的物理版本，
在 $N\le1/64$ 的当前分支上可取
$$
 |b_1-1|\le4w^2N,\quad |a_1|\le2w^2N,\quad
 |G-1|\le8w^2N,\quad |\gamma|\le2w^2N,
$$
$$
 |\gamma_a|\le32(w^2/a)N,\qquad
 |(a_1)_a|,|(b_1)_a|\le128(w^2/a)N.
 \tag{S.13}
$$
这些是同一 Wiener 代数估计。最后两项使用
$P_a=(V-(A+1)P)/a$、$K_a=F_t/a$ 以及
$\gamma_a=(a_1G-(b_1)_\theta)/l$，所以没有引入三阶高度。
角二阶重建只用 $l_\theta,G$。由 (S.13)，水平位移的一阶、二阶
Cartesian norm 分别受 $2^8w^2N$、$2^{12}(w^2/a)N$ 控制；
水平位移本身由 $(\partial_\theta+i)^{-1}$ 受 $2^8aw^2N$ 控制。
$w/a<5/18,w<1$ 已在 (S.2) 支付。

因此一个宽松的完整物理界为
$$
 \|F_a-F_0-\lambda e_z\|_{C^2({\rm entire\ connector})}
 <2^{17}\sup N
 <2^{-8690}\|a\|_{\ell^1_\beta}.
 \tag{S.14}
$$
所有内部接缝按同一 PDE 匹配完整二 jet；平尾端还是原 R115 的完整
$C^2$ 零延拓。当前外区的支持正性保持。这里得到的是同一实际 connector
的精确 chart；全局嵌入、与主体的匹配和最终 reach 仍在完整问题内。

## 6. 额外标签权确由 R74 真线性输入支付

R74 (74.34) 对其实际 full-tail 线性解、$B$ 后齐次的 source 合同给
$$
 |a_m^{tail}|\le e^{-T|m|/8}A_m,\qquad
 A_m=h(0)^2|f_m|+|m|^{1/p_*}F_{m,p_*},\quad T=2^{24}.
 \tag{S.15}
$$
$f_m$ 是该公式的 regular 高度输入，$F_{m,p_*}$ 是它定义的完整体源
范数；普通源没有被换成一个切口跳量。
于是**同一真实线性标签**有
$$
 \boxed{\quad
 \|a^{tail}\|_{\ell^1_{8192}}
 \le e^{-4(2^{21}-2^{13})}\sum_m A_m
 =e^{-8355840}\sum_m A_m
 <2^{-8355840}\sum_m A_m.
 \quad}                                                     \tag{S.16}
$$
这里均值按 R74 的独立通量行保留，不把它乘以非零模指数。
所以本篇不是随便指定一个与实际线性输入无关的超强标签域。
若 source 位于两个 bump、connector 或真尾，必须使用 R74
(74.35) 的完整 particular 费用；(S.16) 不对那些 source 免费成立。

本篇的 exact-tail+connector chart 本身在这些区域的 metric defect
恒为0，Newton 中重新评价该 chart 时它们的非线性源也恒为0。
但要把它与外面的有限主体联立，仍须解其**非线性**全部两迹和 mean
matching。线性标签落在 (S.3) 并不证明任意非线性残差也满足同一逆门。

## 7. 可复核入口与当前下一缺口

[准确有理程序](../scripts/fourfold_full_connector_weight_20261113.py)
和 [完整报告](../notes/2026-11-13-R119-full-connector-weight-budget.json)
支付 (S.1)、全部角宽、衰减指数、完整 mean 和 R74 权重差。
输入均来自已注明的实际对象及 R119 已证全频能源估计；未执行一个
虚构的数值 nonlinear connector 求解。

现已得到的真实外端是 $u=T$，其后仍是 R74 两个 bump 及长径向段。
下一数学缺口是把这份非线性完整两迹与那一段的真实 BVP 联立，并对
全部高 incoming、mean 和普通源证明可用于 Newton 的强逆。不能把
有限低图、任意正角宽损失或 (S.16) 的线性小量代替它。
