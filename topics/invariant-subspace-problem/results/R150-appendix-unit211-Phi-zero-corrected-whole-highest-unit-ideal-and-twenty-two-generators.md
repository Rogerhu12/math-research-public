# 正确 Phi：全部原最高方向消失与全权二十二生成

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整纸面证明，无新执行。** 在当前正确 $\Phi=0$、distinct singleton、物理 $D\ne0$ 原图的已付权参数环上，三个真均值、加权 NS/PS 和原六次矩条件的最高齐次系统没有任何 projective 方向。证明在整系数环内保留幂零结构；没有把原物理 $D$ 或 $\lambda$ 的非零性移到最高项。

其直接结果是：在反演任何几何量之前，必要代数
$$
\mathcal B=\mathcal A[t,f,V]/(I_6,R_6)
$$
是全权有限 $\mathcal A$ 模，而且由以下 **22 个明确单项式**生成：
$$
\boxed{\quad
1,t,\ldots,t^7;\qquad
f,tf,\ldots,t^6f;\qquad
V,tV,\ldots,t^6V .
\quad}
\tag{1}
$$
不要求这 22 元自由或独立。所有原权首项为零的纤维均包括在内；原物理开集的几何局部化另行解释，本文不宣布全 Phi 为空。

## 1. 系数环、原来源与次数

采用[全 t 参数真均值](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)的原恢复，并记
$$
\begin{gathered}
s=u-1,\qquad \delta=1-Q,\qquad K_w=Q+4s,\\
L=Q-2s(u-2),\qquad \ell=L/Q,\qquad m=u-\ell,\\
M=\ell^2\delta-m^2,\qquad M_n=QM,\qquad
bc=M/(4\delta),\\
T_0=-K_w,\qquad J=2u(1-u)+L,\qquad
J-Q=-4s^2,\\
P_{02}=2sL,\qquad P_f=T_0(J-Q).
\end{gathered}
\tag{2}
$$
在
$$
\mathcal A=
\mathbb Q[u,Q,(uQ\delta sK_wLM_n(2\ell-1))^{-1}]
\tag{3}
$$
上工作，括号内的有理写法等价于先反演 $Q$ 再反演其分子。于是 $M,bc,\ell,T_0,P_{02},P_f$ 均为单位。

这里 $u$ 的支付来自[独立真原零 base-mean 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)，$2\ell-1$ 来自[正确 Phi 整个 ell-half 原排除](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)。其余为当前原恢复图的既有权单位。本证明甚至不需要 $m^{-1}$，也不反演 $\theta=u-\ell Q$、任何原斜率头或新的权多项式。它不是对 $h=k$、任意 $D=0$ 图或 W 图的单位付款。

$\deg(t)=\deg(f)=\deg(V)=1$，$\mathcal A$ 的元素次数为零。原恢复为
$$
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},
\qquad
T=-\ell+\frac{T_0(f-V+bct)}{P_{02}},
\qquad z=Qt .
\tag{4}
$$
这是已付权环上的仿射双向变换；固定 $t$ 的线性行列式是 $-P_f/P_{02}^2$。其最高一次部分为
$$
\lambda_1=\frac{Jf-QV+bcQt}{P_{02}},
\qquad
T_1=\frac{T_0(f-V+bct)}{P_{02}}.
\tag{5}
$$

$I_6$ 指六条真正原式
$$
I_6=(\mathcal R,E_{B,e},E_{B,o},N_1,NS,PS).
\tag{6}
$$
前三式与原 $E_1,E_B,E_C$ 的完整身份使用双点乘法 $(d^2)_1=2d_0d_1$。其固定 $t$ 二次头和原三生成规则由上述 t 参数论文逐式给出。完整 NS/PS 来源另见[中心化 t 的原十行表示](R150-appendix-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-and-sextic.md)与[全图六原乘子](R150-appendix-unit211-Phi-zero-corrected-whole-t-sextic-six-original-multipliers-and-H28.md)；本文只使用这些原式本身，不重跑其表示或标量门。

[完整原矩来源](R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)给必要式
$$
R_6=MK^2-4m^2D^3,
\tag{7}
$$
其中
$$
\begin{aligned}
A_2&=2\lambda^2-2\lambda+1,\\
B_3&=4\lambda^3-6\lambda^2+3\lambda-1,\\
D&=\ell A_2-T^2,\\
K&=\ell^2B_3-3\ell A_2T+2T^3.
\end{aligned}
$$
(7) 是两个原 shifted moment 的多项式后果，未倒 $D$ 或其范数。本文研究必要代数 $(I_6,R_6)$，不声称这七式已充分刻画全部物理解。

## 2. 真均值的最高二次与 t=0 图

在首一、有限自由、忠实平坦的扩张
$$
\mathcal A'=\mathcal A[\rho]/(\rho^2-\delta)
$$
中置
$$
b=\frac{\ell}{2}+\frac{m\rho}{2\delta},\qquad
c=\frac{\ell}{2}-\frac{m\rho}{2\delta},\qquad
p=1+\rho,\quad q=1-\rho.
$$
$b,c,p,q,\rho$ 都是单位：其乘积分别由 $bc,Q,\delta$ 支付。保留两根与整个扩张，不选某个复根。

令 $X,Y$ 表示原 $X,Y$ 的最高一次部分：
$$
x=\frac{(u-\ell Q)V-2umf}{M},\qquad
y=\frac{2u\ell f-uV}{M},\qquad
X=x+\rho y,\quad Y=x-\rho y.
\tag{8}
$$
于是
$$
bX+cY=V,\qquad bpX+cqY=2uf.
\tag{9}
$$
$x,y$ 到 $f,V$ 的线性行列式为 $-M/(2u)$，也是旧单位。以下用 $X,Y$ 只是同一原线性图的写法。

三个真均值的最高二次准确是
$$
\begin{aligned}
R&=4f(V-f)+bc\bigl(t^2-2t(X+Y)\bigr),\\
E_B^{(2)}&=ct^2-2ctY-2X^2+4fX,\\
E_C^{(2)}&=bt^2-2btX-2Y^2+4fY.
\end{aligned}
\tag{10}
$$
其中 $R=\mathcal R^{(2)}$。偶奇两行是
$$
E_{B,e}^{(2)}=(E_B^{(2)}+E_C^{(2)})/2,\qquad
E_{B,o}^{(2)}=(E_B^{(2)}-E_C^{(2)})/(2\rho).
$$
这是一项可逆行变换。

对列 $(f^2,fV,V^2)$，三个偶奇原均值的共同头矩阵 $H$ 满足已经显示证明的身份
$$
\det H=\frac{32uQ(2\ell-1)}{M^2}\in\mathcal A^\times.
\tag{11}
$$
因此在 $t=0$ 上，三式恰生成 $(f^2,fV,V^2)$。该 projective 子图为空，连同其非约化结构也保留。齐次均值商同时由 $1,f,V$ 生成为 $\mathcal A[t]$ 模，所以它在每个剩余域上的 projective 支持至多有限。

## 3. 完整加权 N/P 给出的新最高三次

从原 rowB 直接取最高三次，有
$$
N_{B,3}=2c(Y-f)t^2-4cXYt+4fX^2,
\qquad
P_{B,3}=ct^3-3cXt^2+2X^3.
\tag{12}
$$
C 行是交换 $b,c$ 与 $X,Y$ 的共轭式。原 $N_4$ 中 $\tau(vD_Kv)$ 在此至多二次，故不漏掉三次项。

完整加权两式的最高部分为
$$
\begin{aligned}
NS_3&=bN_{B,3}+cN_{C,3}-4P_{02}\lambda_1^3,\\
PS_3&=bP_{B,3}+cP_{C,3}-4P_{02}\lambda_1^3.
\end{aligned}
\tag{13}
$$
两条最高 $\lambda_1^3$ 校正恰相同。由 (10)、(12) 逐项相减，
$$
N_{B,3}-P_{B,3}-X E_B^{(2)}
=c\bigl(2(X+Y-f)t^2-2XYt-t^3\bigr).
$$
加上其共轭并按原权加权，得到完整身份
$$
\boxed{
NS_3-PS_3-bX E_B^{(2)}-cY E_C^{(2)}
=-2bc\,t\bigl[t^2-2(X+Y)t+2XY+2ft\bigr].
}
\tag{14}
$$
左侧正是完整 Loww 的最高组合。这个身份没有倒任何原 N/P 首项，且没有用原 $N_1$ 或完整 NV 来替代 NS/PS。

在齐次图 $t=1$ 上，由 $bc$ 单位，(14) 支付
$$
L_0=1-2(X+Y)+2XY+2f=0.
\tag{15}
$$

## 4. 保留幂零结构的中心计算

下面在 $\mathcal A'$ 上，由 (10)、(13)、$R_{6,6}$ 在 $t=1$ 所定义的商环中计算。$L_0=0$ 已由 (14) 给出。记
$$
\xi=1-2X,\qquad \eta=1-2Y,\qquad
P=\xi\eta,\qquad S=\xi+\eta.
$$
(15) 等价于
$$
4f=1-\xi-\eta-\xi\eta.
\tag{16}
$$
此处的 $P$ 只是局部计算记号，不是 $P_{02}$ 或原三次值。

将 (16) 代入真均值 (10)，有
$$
2E_B^{(2)}=\eta(\xi^2+2c-1),\qquad
2E_C^{(2)}=\xi(\eta^2+2b-1).
\tag{17}
$$
由原线性身份 (9)，同时有
$$
cq\,\xi+bp\,\eta+uP=0.
\tag{18}
$$

为明确保留全部幂零，置
$$
F_b=\eta^2+2b-1,\qquad F_c=\xi^2+2c-1.
$$
在 (16) 下直接展开 $R$，给
$$
R+P^2=-2X^2 E_C^{(2)}-2Y^2 E_B^{(2)}
+\frac{S-1}{4}F_bF_c.
$$
例如取 $b_0=(1-\eta^2)/2,c_0=(1-\xi^2)/2$，此时 $R=-P^2$；把 $b=b_0+F_b/2,c=c_0+F_c/2$ 代回，两个一次括号分别为 $-\xi X^2$、$-\eta Y^2$，即得上式。再用 (17) 乘 $P$：
$$
\boxed{
P R+P^3
=-2PX^2 E_C^{(2)}-2PY^2 E_B^{(2)}
+(S-1)E_B^{(2)}E_C^{(2)} .
}
\tag{19}
$$
所以 $P^3=0$。分别用 $\xi,\eta$ 乘 (18)，得到
$$
cq\,\xi^2=-P(bp+u\xi),\qquad
bp\,\eta^2=-P(cq+u\eta).
\tag{20}
$$
$bp,cq$ 是单位，故
$$
\xi^6=\eta^6=0,\qquad
\mathfrak n=(\xi,\eta),\qquad \mathfrak n^{11}=0.
\tag{21}
$$
这不是先把商约化后遗漏其重数。

## 5. 模幂零理想后的原六次矛盾

在上述商再模掉 $\mathfrak n$，由 (16) 得
$$
X=Y=\frac12,\qquad f=\frac14,\qquad V=\frac{\ell}{2}.
\tag{22}
$$
原 $R=0$ 此时给
$$
bc=\frac{2\ell-1}{4}.
\tag{23}
$$
完整权身份为
$$
4\delta R\big|_{(22)}
=m^2-\delta(\ell-1)^2=s^2(3-2\ell).
\tag{24}
$$
最后一个等号只用正确 Phi 的 $\ell=L/Q$。$s$ 单位，所以
$$
\ell=\frac32,\qquad bc=\frac12.
\tag{25}
$$

由 (5)、(22)、(23)，
$$
T_1=0,\qquad
\lambda_1=\frac{J-Q}{4P_{02}}=-\frac{s^2}{P_{02}}\in\mathcal A^\times.
\tag{26}
$$
这里最高 $\lambda_1$ 的单位是新等式 (26) 的结果，未从原 $\lambda\ne0$ 推出。

原六次 (7) 的最高齐次部分是
$$
\begin{aligned}
D_2&=2\ell\lambda_1^2-T_1^2,\\
K_3&=4\ell^2\lambda_1^3-6\ell\lambda_1^2T_1+2T_1^3,\\
R_{6,6}&=M K_3^2-4m^2D_2^3.
\end{aligned}
\tag{27}
$$
在 (23)、(26) 下直接算得
$$
R_{6,6}
=16\ell^3\delta(3\ell-2)\lambda_1^6
=40\ell^3\delta\lambda_1^6.
\tag{28}
$$
(28) 是单位，却应为零，故模 $\mathfrak n$ 的商为零。由于 $\mathfrak n^{11}=0$，原商自身也为零。

$\mathcal A'/\mathcal A$ 有限自由且忠实平坦，因此单位理想结论下降到原偶奇系数环。令
$$
\mathcal J_{\rm top}
=(R,E_{B,e}^{(2)},E_{B,o}^{(2)},NS_3,PS_3,R_{6,6})
\subset\mathcal A[t,f,V].
\tag{29}
$$
我们已在整个 $\mathcal A$ 上证明
$$
\boxed{\quad
1\in \mathcal J_{\rm top}\big|_{t=1}.
\quad}
\tag{30}
$$
结合 §2 的 $t=0$ 图，$\mathcal J_{\rm top}$ 没有任何 projective 共同零方向。注意齐次理想本身仍包含于 $(t,f,V)$；这里所谓最高单位理想是其 $t=1$ 仿射图的单位理想，而不是声称 $1$ 属于正次数齐次理想。

## 6. 每个剩余域中的统一八次降阶

给出明确的统一次数界，而不依赖一个未计算的齐次化指数。

取 $\mathcal A$ 的任意极大理想，剩余域记作 $k$。它是特征零的无限域。由 (11)，三个真均值二次生成的 projective 零集是有限的，因而其齐次理想高度至少二。可在这三个二次式的 $k$ 线性空间中选取两式 $q_1,q_2$，使它们无共同曲线因子。具体地，先取非零 $q_1$，再避开它有限个不可约因子所给的真线性子空间选择 $q_2$；三式的高度保证每个待避子空间确是真子空间。

$q_1,q_2$ 构成正则序列，$V(q_1,q_2)\subset\mathbb P^2_{\overline k}$ 是有限 complete intersection。由 (30) 及 $t=0$ 的结论，$\mathcal J_{\rm top}$ 的次数六部分在这个有限集合上无公共零点：每个点已有某个次数至多六的生成元不为零，再乘不在该点消失的单项式即可补到六次。无限域中的有限线性避让于是给一条
$$
q_3\in (\mathcal J_{\rm top}\otimes k)_6
$$
避开全部这些点。因此 $q_1,q_2,q_3$ 是次数 $(2,2,6)$ 的齐次正则序列。

其 Artin 商的 Hilbert 级数为
$$
\frac{(1-x^2)^2(1-x^6)}{(1-x)^3}
=(1+x)^2(1+x+x^2+x^3+x^4+x^5).
\tag{31}
$$
最高非零次数至多七。所以
$$
(\mathcal J_{\rm top}\otimes k)_8
=k[t,f,V]_8
\tag{32}
$$
对每个极大剩余域都成立。这里每个 $k$ 可以选不同的 $q_i$；不把局部选取的分母当作新的全局权单位。

## 7. 八次满射拼回整个系数环

令 $\Psi_8$ 为固定的有限矩阵映射：对 (29) 中每个次数 $d_i$ 的原最高生成元，取全部次数 $8-d_i$ 的普通单项式倍，映到 $\mathcal A[t,f,V]_8$。右端是秩
$$
\binom{10}{2}=45
$$
的自由 $\mathcal A$ 模。这个矩阵完全由原最高式定义，不使用 §6 逐剩余域挑选的正则序列作为参数。

$\operatorname{coker}\Psi_8$ 有限生成，且 (32) 使它在每个极大剩余域上都为零。局部 Nakayama 引理及有限模支持给
$$
\boxed{\quad
(\mathcal J_{\rm top})_8=\mathcal A[t,f,V]_8 .
\quad}
\tag{33}
$$
因为右端自由，(33) 还表示每个八次单项式都存在一个真正的 $\mathcal A$ 系数原齐次组合；无需再反演任何权多项式。未显式展开这个右逆不会损失该存在性身份，也没有把模素数的满秩当作全局空性。

把每个最高生成元换回其完整原式 $\mathcal R,E_{B,e},E_{B,o},NS,PS,R_6$，相应差的总次数严格较低。于是 (33) 使每个八次单项式在原必要商中都可降为总次数至多七。更高单项式由此逐次严格降总次数，所以
$$
\mathcal A[t,f,V]/(\mathcal R,E_{B,e},E_{B,o},NS,PS,R_6)
$$
已是有限 $\mathcal A$ 模。再加入完整 $N_1$ 取商，当然保留这个结论。

最后使用已刊的真三均值规则
$$
f^2,\ fV,\ V^2
\equiv a_0(t)+a_f(t)f+a_V(t)V,
\qquad
\deg_ta_0\le2,\quad \deg_ta_f,\deg_ta_V\le1.
\tag{34}
$$
它们严格降低 $(f,V)$ 次数，并且不增加 $(t,f,V)$ 总次数。故所有总次数至多七的单项式进一步落入 (1) 的 22 元张成。这完成全权有限二十二生成证明。

## 8. 已付结论与保留范围

对每个权参数点，未反演几何量的 $(t,f,V)$ 必要代数纤维的向量空间维数至多 22。该上界保留幂零；不表示纤维恰有 22 个点、模自由或各纤维维数相同。

有限生成的行列式技巧还给原 $t$ 的一个全权首一至多 22 次关系：对 (1) 选择同点乘 $t$ 的真实作用提升，再用其 $22\times22$ 特征多项式并返回生成映射。原 $\lambda,T$ 由 (4) 恢复，类似积分性也成立。本文没有计算这些新多项式的系数，不把存在性当作一个已执行的系数证书。

[既有非零纯权支持](R150-appendix-unit211-Phi-zero-corrected-nonzero-weight-support-and-whole-dimension-one.md)仍给正确原 $I_6$ 内的非零 $F(u,Q)$。本条把原必要代数的投影进一步提升为对该权支持的有限模型；尚未把这一权曲线排成有限点集或排空。

随后取物理 $D\ne0$ 及其它几何单位开集，只能直接断言各权纤维仍有限、维数不会增加。这样的几何局部化不一定仍是有限 $\mathcal A$ 模；本文的二十二生成明确先于这一步。

本文没有计入恢复 $\rho$、singleton 谱值或独立尺度 $U_0$ 的额外坐标。因此不以 22 直接宣称完整规范原点数或长度。尤其 p 规范并不等于 $U_0$ 规范；若将 $U_0$ 也列为独立坐标，需要另保其原三次关系。

[最高 $D_2$ 与 $\lambda_1$ 前导引理](R150-appendix-unit211-Phi-zero-corrected-whole-highest-D2-original-unit-ideal.md)仍是独立正确结论；本条新增了完整 NS/PS 的最高 Loww 来源，才把全部最高方向排空。全篇无新脚本、数值运行、重复门或系数载荷，也不恢复任何被撤回的 wrong-Rbar 后继。
