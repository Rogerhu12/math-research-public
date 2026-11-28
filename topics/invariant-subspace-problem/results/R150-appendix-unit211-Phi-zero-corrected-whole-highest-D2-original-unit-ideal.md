# 正确 Phi：全最高方向的 D2 与 lambda1 原单位理想

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整纸面证明，无新执行。** 在当前正确 $\Phi=0$ 原图的 $(t,f,V)$ 最高齐次代数中，三个真均值和原六次矩条件已经使最高二次量 $D_2$ 为单位；最高 $\lambda_1$ 也为单位。两项结论保留全部权参数，不借原物理 $D\ne0$ 或原 $\lambda\ne0$ 直接排除它们的最高项零面。最高理想本身是否为单位仍未由本文证明。

## 1. 原范围及全部已付系数

使用[全 t 参数真三均值](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)和[整 ell-half 原排除](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)。记
$$
\begin{gathered}
s=u-1,\quad\delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad\ell=L/Q,\quad m=u-\ell,\\
M=\ell(2u-\ell Q)-u^2=\ell^2\delta-m^2,\quad
bc=M/(4\delta),\quad T_0=-K_w,\\
J=2u(1-u)+L,\quad J-Q=-4s^2,\quad
P_{02}=2sL,\quad P_f=T_0(J-Q).
\end{gathered}
$$
在
$$
\mathcal A=\mathbb Q[u,Q,(uQ\delta sK_wLM_n(2\ell-1))^{-1}],
\qquad M_n=QM
\tag{1}
$$
上工作。$M,bc,\ell,T_0,P_{02},P_f$ 都是单位。本证明不需要 $m^{-1}$；没有新权头或谱头分母。

这里只对 $(t,f,V)$ 取原总次数的最高齐次部分，权参数次数为零。沿用同一符号表示这三个齐次坐标。原恢复的线性最高部分为
$$
\lambda_1=\frac{Jf-QV+bcQt}{P_{02}},\qquad
T_1=\frac{T_0(f-V+bct)}{P_{02}}.
\tag{2}
$$
固定 t 时，其对 $(f,V)$ 的行列式为 $-P_f/P_{02}^2$，是 (1) 中的单位。取最高部分没有把原自由变量置成某个物理数值。

## 2. 三个正确均值的最高二次

设 $\rho^2=\delta$，
$$
b=\ell/2+\frac{m}{2\delta}\rho,\qquad
c=\ell/2-\frac{m}{2\delta}\rho,\qquad
\theta=u-\ell Q .
$$
原 X/Y 的线性最高部分为
$$
x_1=\frac{\theta V-2umf}{M},\qquad
y_1=\frac{2u\ell f-uV}{M},\qquad
X_1=x_1+\rho y_1,\quad Y_1=x_1-\rho y_1.
\tag{3}
$$
三个原均值最高二次准确是
$$
\mathcal R_2
=4f(V-f)+bc\,t^2
-\left(\ell+\frac m\delta\right)tV
+\frac{2mu}{\delta}tf,
\tag{4}
$$
以及
$$
E_{B,2}=c\,t^2-2ctY_1-2X_1^2+4fX_1
=E_{B,e,2}+\rho E_{B,o,2}.
\tag{5}
$$
(4) 来自正确 $\mathcal R$；(5) 直接取真原
$E_B=\tau(B^2)-2(D_Kd)_B-2d_B^2+4fd_B$ 的最高二次。特别地，$(D_Kd)_B$ 的二次部分是 $ctY_1$，其含原 p、u 的其它项只为一次。未使用被撤回的 germ 分量平方。

由已刊真三均值头，(4)、(5) 对 $f^2,fV,V^2$ 的系数矩阵行列式为
$$
\det H=\frac{32uQ(2\ell-1)}{M^2}\in\mathcal A^\times .
\tag{6}
$$
在 projective 最高方向的 $t=0$ 图上，三式因而迫
$f^2=fV=V^2=0$。这个 projective 子图为空，包含非约化支也不例外：其无关理想 $(f,V)$ 已幂零。因此全部最高方向都在 $t\ne0$ 图，可齐次归一化 $t=1$。

## 3. 原矩六次的最高部分

[完整原矩来源](R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)给
$$
R_6=MK^2-4m^2D^3,
\quad
D=\ell(2\lambda^2-2\lambda+1)-T^2,
$$
$$
K=\ell^2(4\lambda^3-6\lambda^2+3\lambda-1)
 -3\ell(2\lambda^2-2\lambda+1)T+2T^3 .
$$
它来自两条原 shifted moment，不是假定任何裸三列模自由后得到的式子。其最高齐次部分是
$$
\begin{aligned}
D_2&=2\ell\lambda_1^2-T_1^2,\\
K_3&=4\ell^2\lambda_1^3-6\ell\lambda_1^2T_1+2T_1^3,\\
R_{6,6}&=M K_3^2-4m^2D_2^3 .
\end{aligned}
\tag{7}
$$
以下均在 $t=1$ 的 $\mathcal A[f,V]$ 中。令
$$
J_0=(\mathcal R_2,E_{B,e,2},E_{B,o,2},R_{6,6}).
\tag{8}
$$

## 4. 完整原单位理想 J0 加 D2

断言
$$
\boxed{\quad 1\in J_0+(D_2).\quad}
\tag{9}
$$
为证 (9)，在商环
$$
\mathcal B=\mathcal A[f,V]/(J_0,D_2)
$$
中计算，保全部非约化结构。由 (7) 及 M 单位，$K_3^2=0$。而精确身份
$$
K_3=2\ell\lambda_1^2(2\ell\lambda_1-T_1)-2T_1D_2
$$
在此商中给
$$
K_3^2(2\ell\lambda_1+T_1)^2
=16\ell^4(2\ell-1)^2\lambda_1^8=0 .
\tag{10}
$$
(1) 的单位因此支付 $\lambda_1^8=0$。又 $T_1^2=2\ell\lambda_1^2$，所以 $T_1^8=0$。理想
$$
\mathfrak n=(\lambda_1,T_1)\subset\mathcal B
$$
是幂零的，例如 $\mathfrak n^{15}=0$。

在 $\mathcal B/\mathfrak n$ 中，(2) 及 $T_0,J-Q$ 单位给
$$
f=0,\qquad V=bc.
\tag{11}
$$
代入真正 (4)，有
$$
\mathcal R_2(0,bc,1)
=bc\left(1-\ell-\frac m\delta\right)
=-\frac{bc\,s(2u-3)}{\delta}.
\tag{12}
$$
$bc,s,\delta$ 都是单位，故商中 $u=3/2$。此时
$$
\ell=\frac{2Q+1}{2Q},\qquad
m=-\frac{\delta}{2Q},\qquad
\theta=\delta,\qquad
x_1=\frac14,\quad y_1=-\frac{3}{8\delta}.
\tag{13}
$$
由 (5) 的真正 odd 系数，直接得到
$$
E_{B,o,2}
=\frac{1}{8Q}-\frac{3}{16Q\delta}
=-\frac{2Q+1}{16Q\delta}
=-\frac{\ell}{8\delta}.
\tag{14}
$$
右侧是单位，但左侧在该商为零。因此 $\mathcal B/\mathfrak n=0$。既然 $\mathfrak n$ 幂零，便有 $\mathcal B=0$：否则 $1\in\mathfrak n$ 与 $\mathfrak n^{15}=0$ 矛盾。这证明 (9)。

本证明给整个旧权局部化环上的单位理想，强于仅逐复点排除；没有选择某个权根或丢掉最高重数。

## 5. 最高 lambda1 同样为单位

由 (9)，$D_2$ 在 $\mathcal A[f,V]/J_0$ 中为单位。再商掉 $\lambda_1$，有
$$
D_2=-T_1^2,\qquad K_3=2T_1^3,
$$
$$
R_{6,6}=4(M+m^2)T_1^6=4\ell^2\delta\,T_1^6 .
\tag{15}
$$
$D_2$ 单位使 $T_1$ 为单位，(15) 的系数也是单位，因此这个商为零。故
$$
\boxed{\quad 1\in J_0+(\lambda_1).\quad}
\tag{16}
$$
全部最高方向也可合法取 $\lambda_1=1$。这是最高代数自身的付款；未由原物理 $\lambda\ne0$ 推其最高部分非零。

## 6. 严格保留的范围

(9)、(16) 只把 $D_2$、$\lambda_1$ 付成 **最高共同零代数** 中的单位；没有证明 $J_0=(1)$，也没有宣称所有最高方向消失。加入完整最高 N1、个别 N/P、完整 NV 等原条件可以继续使用此付款，但其单位目标仍需真正来源。

同样，本文没有排除原物理 D 的其它图，没有把旧错误 D2 链恢复为证据，也没有给新有限点数或普通 ISP 结论。原 $2\ell-1$ 的付款来自整个正确 ell-half 原排除；它的使用范围始终是当前正确 Phi 图。

本文只依赖已经刊出的真三均值头、完整原矩身份和原权单位；(4)、(5)、(10)、(12)、(14)、(15) 均在正文逐项给出。没有新脚本、实际运行、重复数值门或系数载荷。
