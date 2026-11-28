# 正确 Phi：原 N1 最高极化排除与完整六式全权十三生成

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整纸面证明，无新执行。** 在当前正确 $\Phi=0$、distinct singleton、物理 $D\ne0$ 原图的已付权环上，三个真均值、完整原 $N_1$ 和加权 NS/PS 的最高齐次系统已没有任何 projective 共同方向。因此，在反演几何量之前，完整六式必要代数
$$
\mathcal B_6=\mathcal A[t,f,V]/I_6
$$
由以下 **13 个明确单项式**生成为 $\mathcal A$ 模：
$$
\boxed{
1,t,t^2,t^3,t^4;\qquad
f,tf,t^2f,t^3f;\qquad
V,tV,t^2V,t^3V .
}
\tag{1}
$$
这些生成元不要求独立或自由；所有尚未支付的权首项零纤维都包括在内。本文新增的关键是完整原 $N_1$ 的二次最高极化。它在已控制的幂零商中直接成为单位，所以本条不需要再加入原六次矩条件 $R_6$。

[先前的全权二十二生成证明](R150-appendix-unit211-Phi-zero-corrected-whole-highest-unit-ideal-and-twenty-two-generators.md)仍是独立正确结论。本条用此前未用于最高矛盾的原 $N_1$，对更大的六式必要代数给出更强生成界；没有重跑任何计算门。

## 1. 系数环与六条原式

记
$$
\begin{gathered}
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\\
\ell=L/Q,\quad m=u-\ell,\quad
M=\ell^2\delta-m^2,\quad M_n=QM,\quad bc=M/(4\delta),\\
T_0=-K_w,\quad J=2u(1-u)+L,\quad
J-Q=-4s^2,\quad P_{02}=2sL,\quad P_f=T_0(J-Q).
\end{gathered}
\tag{2}
$$
在
$$
\mathcal A=\mathbb Q[u,Q,(uQ\delta sK_wLM_n(2\ell-1))^{-1}]
\tag{3}
$$
上工作；含 $\ell=L/Q$ 的写法等价于先反演 $Q$ 再反演相应分子。于是 $M,bc,\ell,T_0,P_{02},P_f$ 都是单位。

$u$ 来自[独立真原零 base-mean 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)，$2\ell-1$ 来自[正确 Phi 整个 ell-half 排除](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)。其余是原恢复图的既有权单位。本文不需要反演 $m$、任何新斜率或几何首项；不把这些付款移到 $h=k$、任意 $D=0$ 或 W 图。

[全 t 参数真均值模型](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)给原恢复
$$
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},
\qquad
T=-\ell+\frac{T_0(f-V+bct)}{P_{02}},
\qquad z=Qt .
\tag{4}
$$
固定 $t$ 时，这是行列式 $-P_f/P_{02}^2$ 为单位的仿射双向变换。

令
$$
I_6=(\mathcal R,E_{B,e},E_{B,o},N_1,NS,PS).
\tag{5}
$$
前三式是使用真双点乘法 $(d^2)_1=2d_0d_1$ 的均值系统。完整 $N_1$ 的来源见[正确 t 参数 N1](R150-appendix-unit211-Phi-zero-corrected-t-parameter-N1-two-slope-curves-and-six-by-two-model.md)，完整 NS/PS 见[原十行表示](R150-appendix-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-and-sextic.md)。这里引用原式及身份，不调用其斜率补图来支付新的全图单位。

给 $t,f,V$ 总次数一，权量次数零。$\mathcal R,E_{B,e},E_{B,o},N_1$ 的次数至多二，NS、PS 的次数至多三。原 $\lambda,T$ 的最高一次部分为
$$
\lambda_1=\frac{Jf-QV+bcQt}{P_{02}},
\qquad
T_1=\frac{T_0(f-V+bct)}{P_{02}},
\qquad w_1=\lambda_1-T_1 .
\tag{6}
$$

## 2. 真实最高均值与 t=0 图

在有限自由、忠实平坦的首一扩张
$$
\mathcal A'=\mathcal A[\rho]/(\rho^2-\delta)
$$
中，置
$$
b=\frac{\ell}{2}+\frac{m\rho}{2\delta},\quad
c=\frac{\ell}{2}-\frac{m\rho}{2\delta},\quad
p=1+\rho,\quad q=1-\rho .
$$
$b,c,p,q,\rho$ 均为单位，分别由 $bc,Q,\delta$ 支付。这个扩张保留两根和全部非约化结构，不选择单个复根。

用 $X,Y$ 表示原 $X,Y$ 的最高一次部分：
$$
\begin{aligned}
x&=\frac{(u-\ell Q)V-2umf}{M},&
y&=\frac{2u\ell f-uV}{M},\\
X&=x+\rho y,&Y&=x-\rho y.
\end{aligned}
$$
完整原线性关系给
$$
bX+cY=V,\qquad bpX+cqY=2uf.
\tag{7}
$$
三个原均值的最高二次为
$$
\begin{aligned}
R&=4f(V-f)+bc\{t^2-2t(X+Y)\},\\
E_B^{(2)}&=ct^2-2ctY-2X^2+4fX,\\
E_C^{(2)}&=bt^2-2btX-2Y^2+4fY.
\end{aligned}
\tag{8}
$$
其中 $R=\mathcal R^{(2)}$，并且
$$
E_{B,e}^{(2)}=(E_B^{(2)}+E_C^{(2)})/2,\qquad
E_{B,o}^{(2)}=(E_B^{(2)}-E_C^{(2)})/(2\rho).
$$
这是可逆行变换。

已刊的显示头计算给
$$
\det H_{f,V}=\frac{32uQ(2\ell-1)}{M^2}\in\mathcal A^\times.
\tag{9}
$$
所以 $t=0$ 时三均值恰生成 $(f^2,fV,V^2)$，没有 projective 共同点。其齐次商由 $1,f,V$ 生成为 $\mathcal A[t]$ 模；每个剩余域上的三个最高均值因而有有限 projective 支持。

## 3. 原 NS/PS 的最高 Loww 与完整幂零控制

直接从原 rowB 取最高三次，有
$$
N_{B,3}=2c(Y-f)t^2-4cXYt+4fX^2,\qquad
P_{B,3}=ct^3-3cXt^2+2X^3.
$$
C 行由交换 $b,c$ 和 $X,Y$ 得到。加权 NS/PS 的最高校正同为 $4P_{02}\lambda_1^3$，故两者相减时严格取消。完整原身份为
$$
\boxed{
NS_3-PS_3-bX E_B^{(2)}-cY E_C^{(2)}
=-2bc\,t\{t^2-2(X+Y)t+2XY+2ft\}.
}
\tag{10}
$$
它来自真 $N_4/P_2$ 和均值，不倒任一个个别 N/P 首项。

现在在 $t=1$ 图上，取 (8)、$N_{1,2}$、$NS_3,PS_3$ 所定义的商环。由 (10) 和 $bc$ 单位，
$$
1-2(X+Y)+2XY+2f=0.
\tag{11}
$$
设
$$
\xi=1-2X,\quad \eta=1-2Y,\quad P=\xi\eta,\quad S=\xi+\eta.
$$
此处 $P$ 只是中心计算记号。则
$$
4f=1-\xi-\eta-\xi\eta,
\tag{12}
$$
$$
2E_B^{(2)}=\eta(\xi^2+2c-1),\qquad
2E_C^{(2)}=\xi(\eta^2+2b-1),
\tag{13}
$$
且 (7) 给
$$
cq\,\xi+bp\,\eta+uP=0.
\tag{14}
$$

为保留全部重数，使用以下完整原多项式身份，而不先把商约化：
$$
\boxed{
P R+P^3
=-2PX^2E_C^{(2)}-2PY^2E_B^{(2)}
+(S-1)E_B^{(2)}E_C^{(2)}.
}
\tag{15}
$$
(15) 在 (12) 下逐项成立；其展开与来源见[二十二生成证明](R150-appendix-unit211-Phi-zero-corrected-whole-highest-unit-ideal-and-twenty-two-generators.md) §4。具体地，先展开
$$
R+P^2=-2X^2E_C^{(2)}-2Y^2E_B^{(2)}
+\frac{S-1}{4}(\eta^2+2b-1)(\xi^2+2c-1),
$$
再乘 $P$ 并用 (13)，即得 (15)。

因此 $P^3=0$。分别用 $\xi,\eta$ 乘 (14)，有
$$
cq\,\xi^2=-P(bp+u\xi),\qquad
bp\,\eta^2=-P(cq+u\eta).
$$
$bp,cq$ 都为单位，所以
$$
\xi^6=\eta^6=0,\qquad
\mathfrak n=(\xi,\eta),\qquad \mathfrak n^{11}=0.
\tag{16}
$$

模掉这一已证明幂零的理想后，
$$
X=Y=\frac12,\qquad f=\frac14,\qquad V=\frac{\ell}{2},
\tag{17}
$$
而 $R=0$ 给
$$
bc=\frac{2\ell-1}{4}.
\tag{18}
$$
接下来直接使用原 $N_1$，不需要由额外权关系先求出 $\ell$，也不加入 $R_6$。

## 4. 新输入：完整原 N1 最高极化的六项计算

记 $a=1-\ell$。原 Gram 行为
$$
g_0=(0,0,p,q),\qquad
g_1=(0,A_1,r,\sigma),
$$
$$
g_B=(p,r,0,t),\qquad g_C=(q,\sigma,t,0),
$$
其中
$$
A_1=2f-2V+2bct,\qquad
r=X_{\rm full}-ap-ct,\qquad
\sigma=Y_{\rm full}-aq-bt.
$$
写 $\tau(v)=av_0+v_1+bv_B+cv_C$；原乘法的双点分量为
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0,
$$
其余两分量逐点相乘。$D_Kv$ 的第 $i$ 分量是 $\tau(g_i v)$，$d=D_K1$，$F_2=\tau(d)=2f$。

原二次式和原 germ 极化是
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)
 -4\tau(v)\tau(dv)+2F_2\tau(v)^2+\tau(vD_Kv),
$$
$$
N_{\rm pol}=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1),
\qquad
N_1=N_{\rm pol}-4\lambda wP_{02},
\quad w=\lambda-1-T.
\tag{19}
$$
所有这些都是实际 dual Gram 定义，不是已撤回的 compact 均值。

在 (17)、(18)、$t=1$ 下，原 $A_1$ 的最高一次部分为
$$
A_1^{(1)}=\frac12-\ell+2bc=0.
$$
令
$$
r_1=\frac12-c,\qquad \sigma_1=\frac12-b,\qquad
v_0=g_0,\qquad v_1=g_1^{(1)}=(0,0,r_1,\sigma_1).
$$
原 $d,F_2$ 的最高部分为
$$
d^{(1)}=(0,a/2,1/2,1/2),\qquad F_2^{(1)}=1/2.
\tag{20}
$$
实际最高 Gram 矩阵为
$$
K^{(1)}=
\begin{pmatrix}
0&0&0&0\\
0&0&r_1&\sigma_1\\
0&r_1&0&1\\
0&\sigma_1&1&0
\end{pmatrix}.
\tag{21}
$$
特别地，第零行的最高部分确实为零。

这里 $g_0$ 的次数为零，$g_1,d,F_2,K$ 的次数至多一。极化 (19) 中每个次数二的项，因而恰由 $v_0,v_1$ 与 (20)、(21) 取得；$g_1$ 的常数部分只产生次数至多一的项，没有遗漏更高项。

置
$$
W_{r\sigma}=bp\,r_1+cq\,\sigma_1=\frac u2-2bc.
$$
由 (18)，
$$
\begin{gathered}
\tau(v_0)=u,\qquad \tau(v_1)=\ell/2-2bc=a/2,\\
\tau(d^{(1)}v_0)=u/2,\qquad
\tau(d^{(1)}v_1)=a/4,\\
\tau(v_0v_1)=W_{r\sigma},\qquad
p\sigma_1+qr_1=1-u .
\end{gathered}
\tag{22}
$$
把 (19) 的真实极化逐项分为六组，其最高二次依次为：

| 原极化项 | 在 (17)、(18) 下的值 |
|---|---:|
| $4\tau(d^{(1)}v_0v_1)$ | $2W_{r\sigma}$ |
| $-2F_2^{(1)}\tau(v_0v_1)$ | $-W_{r\sigma}$ |
| $-4\tau(v_0)\tau(d^{(1)}v_1)$ | $-ua$ |
| $-4\tau(v_1)\tau(d^{(1)}v_0)$ | $-ua$ |
| $4F_2^{(1)}\tau(v_0)\tau(v_1)$ | $+ua$ |
| $\tau(v_0D_{K^{(1)}}v_1)+\tau(v_1D_{K^{(1)}}v_0)$ | $2bc(1-u)$ |

最后一行由 (21) 直接给出：两个交叉项各为 $bc(p\sigma_1+qr_1)$。于是
$$
\begin{aligned}
N_{{\rm pol},2}
&=W_{r\sigma}-ua+2bc(1-u)\\
&=u\left(\ell-\frac12-2bc\right)=0.
\end{aligned}
\tag{23}
$$

另一方面，(6)、(17)、(18) 给
$$
T_1=0,\qquad
\lambda_1=\frac{J-Q}{4P_{02}}
=-\frac{s^2}{P_{02}}\in\mathcal A^\times,
\qquad w_1=\lambda_1.
\tag{24}
$$
因此原 $N_1$ 的最高二次在模 $\mathfrak n$ 的商中为
$$
\boxed{
N_{1,2}=-4P_{02}\lambda_1^2
=-\frac{4s^4}{P_{02}}\in\mathcal A^\times .
}
\tag{25}
$$
它又必须为零，所以该商为零。由 $\mathfrak n^{11}=0$，模掉 $\mathfrak n$ 之前的整个商也为零。这一步保留所有幂零，不只是排除约化点。

## 5. 完整 I6 最高理想的全图结论

令
$$
\mathcal J_6=
(R,E_{B,e}^{(2)},E_{B,o}^{(2)},N_{1,2},NS_3,PS_3)
\subset \mathcal A[t,f,V].
\tag{26}
$$
§3–4 在整个 $\mathcal A'$ 上证明 $t=1$ 图为单位理想。由忠实平坦性，结论下降到原偶奇系数环：
$$
1\in\mathcal J_6\big|_{t=1}.
\tag{27}
$$
与 §2 的 $t=0$ 图合并，$\mathcal J_6$ 在任意权剩余域上均无 projective 共同零方向。

(27) 是 $t=1$ 图的单位理想；正次数齐次理想 $\mathcal J_6$ 自身仍包含于 $(t,f,V)$。本证明没有把最高 $D_2$ 当作物理 $D$，也没有把原 $\lambda\ne0$ 直接移到最高 $\lambda_1$；(24) 是新的完整原等式所得。

## 6. 次数五的统一满射

取 $\mathcal A$ 的任意极大剩余域 $k$。这是特征零的无限域。由 (9)，三个均值二次的齐次理想高度至少二，所以能在它们的 $k$ 线性空间中选出两条没有共同曲线的二次式 $q_1,q_2$。

它们的 projective complete intersection 是有限集。由 §5，$\mathcal J_6$ 的次数三部分在该有限集上没有共同零点：每个点已有某个次数二或三的原生成元不为零，次数二时再乘一个在该点非零的一次单项式。有限个真线性子空间不能覆盖这个 $k$ 向量空间，因此能选出
$$
q_3\in(\mathcal J_6\otimes k)_3
$$
避开全部这些点。于是 $q_1,q_2,q_3$ 构成次数 $(2,2,3)$ 的齐次正则序列。

其 Artin 商的 Hilbert 级数为
$$
\frac{(1-x^2)^2(1-x^3)}{(1-x)^3}
=(1+x)^2(1+x+x^2),
\tag{28}
$$
最高非零次数为四。因此
$$
(\mathcal J_6\otimes k)_5=k[t,f,V]_5
\tag{29}
$$
在每个极大剩余域都成立。这些正则序列只用于证明统一上界，不把逐点选择的主元或分母付成全局单位。

现在直接由 (26) 的六个固定原最高式定义有限矩阵：次数二的生成元取全部次数三单项式倍，次数三的生成元取全部次数二单项式倍。其目标是
$$
\mathcal A[t,f,V]_5\simeq\mathcal A^{21}.
$$
(29) 说明该固定矩阵的有限 cokernel 在每个极大剩余域上为零。局部 Nakayama 引理与有限模支持给
$$
\boxed{(\mathcal J_6)_5=\mathcal A[t,f,V]_5.}
\tag{30}
$$
右端自由，所以每个五次单项式都有真正的 $\mathcal A$ 系数最高原组合。这里得到的是全环中的存在性身份，不需要再反演任何未付权因子，也没有把一个模素数秩计算当作特征零全局结论。

## 7. 原完整代数的十三生成

将 (30) 的六个最高生成元替换为完整原式 $\mathcal R,E_{B,e},E_{B,o},N_1,NS,PS$，每个五次单项式在 $\mathcal B_6$ 中都降为总次数至多四。乘适当单项式后反复使用，总次数严格下降，所以所有原单项式都落入总次数至多四的张成。

再使用原三均值的完整规则
$$
f^2,\ fV,\ V^2
\equiv a_0(t)+a_f(t)f+a_V(t)V,
$$
$$
\deg_t a_0\le2,\qquad
\deg_t a_f,\deg_t a_V\le1.
\tag{31}
$$
每步严格降低 $(f,V)$ 次数，并且不增加 $(t,f,V)$ 总次数。因而总次数至多四的所有单项式最终由 (1) 的 $5+4+4=13$ 元生成。

这证明完整六式必要代数是全权有限 $\mathcal A$ 模。任何再加入完整个别 N/P、矩条件或完整 NV 的必要商都保留此生成界。证明没有假设裸三坐标矩阵自由、交换或无关系；所有降次都在真实原多项式商中进行。

## 8. 结论范围与尚未完成的目标

每个权点的未几何局部化必要代数纤维，其向量空间维数至多 13，保留全部重数。有限生成的行列式技巧还给原 $t$ 一个全权首一至多十三次关系：先为 (1) 的每个生成元选择同点乘 $t$ 的真实表示，再对这个 $13\times13$ 提升矩阵使用 Cayley–Hamilton，返回生成映射。无需生成元独立；本文未展开其系数或声称已经执行新的乘法表计算。

[既有非零纯权支持](R150-appendix-unit211-Phi-zero-corrected-nonzero-weight-support-and-whole-dimension-one.md)仍给 $I_6$ 内的非零 $F(u,Q)$。本条把完整六式必要代数变成该权支持上的有限模型；尚未证明权曲线只有有限多个点，更未宣布全 Phi 为空。

随后取物理 $D\ne0$ 等几何单位开集，各权纤维仍然有限、维数不增加；这样的几何局部化未必仍是有限 $\mathcal A$ 模。十三生成明确在该步之前成立。

本文不把恢复 $\rho$、singleton 谱值或独立尺度 $U_0$ 的额外坐标计入 13。p 规范与 $U_0$ 规范不同；任何完整规范点数或长度须另保其原有限关系。先前二十二生成与最高 $D_2$ 前导仍独立正确；被撤回的 wrong-Rbar 链继续撤回。全篇没有新执行、重复门、系数载荷或未付首项的隐含反演。
