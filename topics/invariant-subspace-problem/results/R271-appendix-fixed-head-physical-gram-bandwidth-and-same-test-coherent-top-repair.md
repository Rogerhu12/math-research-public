# R271 附录：固定原头的完整物理 Gram 带宽、相干截断封口与同实际测试的一次 MP 小量

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 固定原 N 或 Y 模型的一个真实有限头 $A_m$，本文保留它的非酉 Jordan 相似所产生的全部物理度量。归一后的相干 Gram 按真正的总 grade 有固定带宽，故其完整逆的低源到高 grade 尾可用有限 Neumann 级数直接估计。以 $J=K_m\log x$ 截断相干代表后，同一个实际 $u_f=(P_{V_Q}-P_{K_Q})f$ 完全不变，而原完整 $D_x^\dagger$ 对全部截断残量的一次修正趋于零。

这是**固定 $m$、强位数 $R=x-m\to\infty$** 的结论，常数和衰减率准确依赖原头的物理相似度量。本文没有把这个固定头极限自动放入原 moving-$m$ 母窗口；第 7 节明确列出该运输所需的定量条件。原完整返回、两端 partial 及 $N=M$ 未由此关闭。

依赖：
- [同实际测试的最小相干代表及准确残量](R271-appendix-same-actual-test-minimal-coherent-representative-and-exact-residual.md)；
- [原连续尾相干列的随机池原像与完整 MP 预算](R271-appendix-continuous-tail-coherent-columns-bernoulli-lifts-and-exact-residuals.md)；
- [强位并头的同源源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。

## 1. 原头、原强位与全部物理内积

固定整数 $m\ge1$，令 $d=2^m$，$A_m$ 为原 N 或 Y 的真实 $m$ 位头。其每个第一超对角元素非零，且 $A_m^d=0$。原因是
$$
A_m=F_m(B_m),\qquad F_m(0)=0,\qquad F_m'(0)=d_0^{-1}\ne0,
$$
而 $B_m$ 的实际有限链权全部严格为正。因此 $A_m$ 是一个长度恰为 $d$ 的 Jordan 块，但**原物理内积一般不使它成为单位权移位**。

令 $J_me_j=e_{j-1}$（$j\ge1$），$J_me_0=0$。可先取
$$
S_me_j=A_m^{d-1-j}e_{d-1},\qquad 0\le j<d.
$$
这些列在物理整数旗中的首个非零位置互异，故 $S_m$ 可逆，且
$$
A_mS_m=S_mJ_m.
$$
再把 $S_m$ 乘一个正标量，使
$$
G_m=S_m^*S_m,\qquad
I\preceq G_m\preceq\chi_m I,\qquad
\chi_m=\operatorname{cond}(S_m)^2\ge1.
\tag{1.1}
$$
这个归一化不改变相似恒等式。此后所有 $S_m$、$G_m$、$\chi_m$ 都固定。

给定整数 $R\ge0$，置
$$
x=m+R,\qquad h=d+R,
$$
$$
C=A_m+D_<,\qquad
D_<=\sum_{i=m}^{x-1}(i+1)^{-2}E_i,\qquad
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i.
\tag{1.2}
$$
于是 $C^h=0$，且
$$
\mathcal L_m=C+D=A_m+D_{\ge m}.
$$
令 $\mathcal S=S_m\otimes I$ 作用于全部强头，定义
$$
C_0=J_m+D_<.
$$
原相似准确为
$$
C\mathcal S=\mathcal S C_0,\qquad
\|C_0\|\le1+\frac1m.
\tag{1.3}
$$
后一个界不依赖 $R$。物理度量是 $\mathcal G=G_m\otimes I$，不能省略。

在新坐标上定义 total grade 为
$$
\mathfrak n=j+\#I_<,
$$
其中 $j$ 是 $J_m$ 的头索引，$I_<$ 是强位孔集合。$C_0$ 每次恰降一 grade。这个 grade 只用于保留 $\mathcal G$ 后的证明；原 $C$ 本身一般不齐次。

## 2. 同实际测试的任意相干截断

以下 $g$ 属于原 $d$ 维头，初始强位及远尾均为真空。把强头 forcing 记为
$$
g_0=g\otimes\Omega_<.
$$
沿用
$$
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=\|\omega_j\|^2=(j!)^2e_j((i+1)^{-4}:i\ge x).
$$

对整数 $0\le J<h$ 定义
$$
R_Ja=\sum_{j=0}^J
\frac{(-C)^ja\otimes\omega_j}{\sigma_j^2},
\qquad
H_J=R_J^*R_J
=\sum_{j=0}^J\frac{(C^*)^jC^j}{\sigma_j^2},
$$
$$
a_J=H_J^{-1}g_0,\qquad
f_J=R_Ja_J.
\tag{2.1}
$$
远孔层正交，故这些是原完整物理内积中的准确式。特别，
$$
f_J=P_{\operatorname{Ran}R_J}(g_0\otimes\Omega),\qquad
\|f_J\|^2=\langle H_J^{-1}g_0,g_0\rangle\le\|g\|^2.
\tag{2.2}
$$
没有假设 $H_J^{-1}$ 保强孔或低头。

设 $V_Q,K_Q$ 是同一原有限头模型 $\mathcal L_m$ 的实际左可行空间及真核，cut $Q$ 按第 $m$ 位之后的**全部物理孔数**计。若
$$
Q\ge R+J,
\tag{2.3}
$$
则前引相干代表稿的原低方程积分分部逐列适用，给
$$
P_{V_Q}(D^*)^j i_0
=(-1)^j(P_{V_Q}i_0)(C^*)^j,\qquad 0\le j\le J.
\tag{2.4}
$$
这里 $i_0$ 把完整强头张量远尾真空；强头输入可以占据全部 $R$ 个强位。因此测试中间项至多有 $R+j-1$ 个原尾孔，(2.3) 确实排除了顶 cut。没有把 $C$ 保持 $V_Q$ 当作前提。

$K_Q$ 是真核，同式也成立。对 $R_J$ 的全部列求和再用 $H_Ja_J=g_0$，得到
$$
\boxed{
(P_{V_Q}-P_{K_Q})f_J
=(P_{V_Q}-P_{K_Q})(g_0\otimes\Omega)
=:u_g.
}
\tag{2.5}
$$
这个 $u_g$ 是同一个实际向量，并未重新选 source。

另有一个有用但本身不支付封口的精确式：若 $J<K<h$，则
$$
\langle f_J,f_K\rangle=\langle H_K^{-1}g_0,g_0\rangle
=\|f_K\|^2.
\tag{2.6}
$$
因此差 $f_J-f_{J+1}$ 两两正交，且其平方和不超过 $\|g\|^2$。下面对 top 使用的是完整带宽逆预算，未把 (2.6) 直接当作预测费用界。

## 3. 完整物理 Gram 的归一带宽

在相似坐标中，
$$
\mathsf H_J=\mathcal S^*H_J\mathcal S
=\sum_{j=0}^J\frac{(C_0^*)^j\mathcal G C_0^j}{\sigma_j^2},
$$
$$
H_J^0=\sum_{j=0}^J\frac{(C_0^*)^jC_0^j}{\sigma_j^2}\succeq I.
\tag{3.1}
$$
$H_J^0$ 按 total grade 严格块对角，因为 $C_0$ 恰降一 grade。$\mathcal G$ 只混合旧 $d$ 维头，故其 grade 带宽至多
$$
w=d-1.
$$
同一个带宽也适用于每个 $(C_0^*)^j\mathcal G C_0^j$，于是适用于 $\mathsf H_J$。

定义完整归一矩阵
$$
K_J=(H_J^0)^{-1/2}\mathsf H_J(H_J^0)^{-1/2}.
\tag{3.2}
$$
因两侧的归一因子都保 grade，$K_J$ 的带宽仍至多 $w$。并且
$$
I\preceq K_J\preceq\chi_m I.
\tag{3.3}
$$
这里全 strong-head nuisance 已保留；(3.2) 不是先压到 forcing 再取逆。

写 $a_J=\mathcal S a_J^0$。由 (2.1)，
$$
b_J:=(H_J^0)^{1/2}a_J^0
=K_J^{-1}(H_J^0)^{-1/2}\mathcal S^*g_0.
\tag{3.4}
$$
右侧 forcing
$$
z_J=(H_J^0)^{-1/2}\mathcal S^*g_0
$$
仅支撑于 grade $0,\ldots,w$，且
$$
\|z_J\|\le\sqrt{\chi_m}\|g\|.
\tag{3.5}
$$
这利用的是 $H_J^0$ 保 grade；没有对原 $H_J^{-1}g_0$ 作支撑断言。

## 4. 直接 Neumann 带外估计

先设 $\chi_m>1$，令
$$
c_m=\frac{\chi_m+1}{2},\qquad
\rho_m=\frac{\chi_m-1}{\chi_m+1}\in(0,1).
$$
则
$$
K_J^{-1}
=c_m^{-1}\sum_{n\ge0}(I-K_J/c_m)^n,
\qquad
\|I-K_J/c_m\|\le\rho_m.
\tag{4.1}
$$
这是算子范数收敛的级数，每个第 $n$ 项的 grade 带宽至多 $nw$。

令 $\Pi_{\ge L}$ 为 grade 至少 $L$ 的投影。由 (3.5)，当 $n<(L-w)/w$ 时，第 $n$ 项作用 $z_J$ 后的 $\Pi_{\ge L}$ 部分严格为零。所以
$$
\boxed{
\|\Pi_{\ge L}b_J\|
\le
\rho_m^{\,\lceil(L-w)/w\rceil}
\sqrt{\chi_m}\|g\|,
\qquad L>w.
}
\tag{4.2}
$$
这里使用 $c_m(1-\rho_m)=1$。不需要任何外部矩阵衰减定理，常数也与 $R$、强头维数及 $J$ 无关。

若 $\chi_m=1$，则 $K_J=I$，$b_J$ 仍只支撑于 grade $\le w$；以下所有 high-grade 项在 $J\ge w$ 时严格为零。

## 5. 真实 top 的预测费用

对 $J\ge d-1$，定义
$$
\mathcal E_{J+1}^{(J)}
=\frac{\|C^{J+1}a_J\|^2}{\sigma_{J+1}^2}.
\tag{5.1}
$$
这才是截断后经完整 $D^\dagger$ 读取的 top 预测量；它一般不同于最后一个已观测系数的能量。

$C_0^{J+1}$ 杀掉 grade $\le J$。又由 $H_J^0$ 包含第 $J$ 个正项，
$$
\frac{\|C_0^J\Pi_{\ge J+1}a_J^0\|^2}{\sigma_J^2}
\le\|\Pi_{\ge J+1}b_J\|^2.
$$
因此
$$
\mathcal E_{J+1}^{(J)}
\le
\chi_m\left(1+\frac1m\right)^2
\frac{\sigma_J^2}{\sigma_{J+1}^2}
\|\Pi_{\ge J+1}b_J\|^2.
\tag{5.2}
$$
准确计数给
$$
(J+1)e_{J+1}\ge S_{x+J}e_J,\qquad
\frac{\sigma_J^2}{\sigma_{J+1}^2}
\le\frac1{(J+1)S_{x+J}}
\le\frac{3(x+J+1)^3}{J+1}.
$$
结合 (4.2)，得到
$$
\boxed{
\mathcal E_{J+1}^{(J)}
\le
3\chi_m^2\left(1+\frac1m\right)^2
\frac{(x+J+1)^3}{J+1}\,
\rho_m^{\,2\left\lceil\frac{J-d+2}{d-1}\right\rceil}
\|g\|^2.
}
\tag{5.3}
$$
当 $\chi_m=1$、$J\ge d-1$ 时，左侧为零。

## 6. 同一实际 $u$ 的完整一次 MP 修正

记随机池稿中完整 MP 上界的右侧为
$$
A_{x,k}
=
\frac{S_x}{S_{x+k+1}}
+
12\,512^k(x+k+1)^{3/2}
\sqrt{(k+1)S_x}\,
\exp[-S_{x+k}(x+1)^4].
\tag{6.1}
$$
于是
$$
1\le
\frac{\|D^\dagger\omega_k\|}
{\sigma_k^2/\sigma_{k+1}}
\le A_{x,k}.
$$
对 $J=o(x)$，
$$
\max_{0\le k\le J}(A_{x,k}-1)\longrightarrow0.
\tag{6.2}
$$
这是真正全层 MP，(6.2) 使用同一原无限连续尾。

截断相干代表的全部残量由正交层组成：
$$
[(C+D)f_J]_{j-1}
=\frac{(-C)^ja_J}{\sigma_j^2}\otimes\eta_j,
\quad
1\le j\le J,
$$
$$
[(C+D)f_J]_J
=\frac{(-1)^J C^{J+1}a_J}{\sigma_J^2}\otimes\omega_J,
\tag{6.3}
$$
其中
$$
\eta_j=D\omega_j-\frac{\sigma_j^2}{\sigma_{j-1}^2}\omega_{j-1}.
$$
原随机池稿的准确相消给
$$
\|D^\dagger\eta_j\|^2
\le(A_{x,j-1}^2-1)\sigma_j^2.
$$

令 $\mathcal Q_{x,J}$ 是 $I_{\rm strong}\otimes D^\dagger$ 在远孔 $0,\ldots,J$ 输入上的直和。各完整层都有 R234 有界右逆，故这有限直和是有定义的有界算子；它把每层恰升一孔。它不是全 Fock 上未经证明的有界逆。

由于 (6.3) 的各项经 $\mathcal Q_{x,J}$ 后仍落在不同远孔层，
$$
\boxed{
\begin{aligned}
\|\mathcal Q_{x,J}(C+D)f_J\|^2
\le{}&
\max_{0\le k<J}(A_{x,k}^2-1)\,\|g\|^2\\
&+A_{x,J}^2\mathcal E_{J+1}^{(J)}.
\end{aligned}
}
\tag{6.4}
$$
没有逐层再付 $J$ 次 Cauchy，也没有交换 MP 与物理核投影。

现固定 $m$。若 $\chi_m>1$，定义明确衰减率
$$
\gamma_m=-\frac{2\log\rho_m}{d-1}>0,
\qquad
J_m(x)=d+
\left\lceil\frac6{\gamma_m}\log(x+1)\right\rceil.
\tag{6.5}
$$
当 $\chi_m=1$ 时取 $J_m(x)=d$。对充分大的 $x$，总有
$$
J_m(x)<h,\qquad J_m(x)=o(x).
$$
在 $\chi_m>1$ 的情形，
$$
\rho_m^{\,2\left\lceil\frac{J_m(x)-d+2}{d-1}\right\rceil}
\le(x+1)^{-6},
$$
所以 (5.3) 趋于零。结合 (6.2)、(6.4)，得到

**定理。** 固定原头 $m$，令 $R=x-m\to\infty$，取 (6.5) 的截断，并取任意
$$
Q(x)\ge R+J_m(x).
$$
则 (2.5) 保持同一个真实 $u_g$，且
$$
\boxed{
\sup_{\|g\|\le1}
\|\mathcal Q_{x,J_m(x)}(C+D)f_{J_m(x)}\|
\longrightarrow0.
}
\tag{6.6}
$$
全部 forcing 和完整物理度量保持不变。

若定义一次修正
$$
\widetilde f_J=f_J-\mathcal Q_{x,J}(C+D)f_J,
$$
则 $\|\widetilde f_J-f_J\|\to0$，其两个实际正交投影与 $f_J$ 的差也趋零。头尾交换准确给
$$
(C+D)\widetilde f_J
=-C\,\mathcal Q_{x,J}(C+D)f_J.
\tag{6.7}
$$
因此残量也趋零，因为 $\|C\|\le\|A_m\|+1/m$。但 $\widetilde f_J$ 一般仍不是精确真核；(6.7) 的右侧没有被删去。

## 7. 原 moving-$m$ 母窗口仍需支付什么

(5.3)、(6.4) 是全部参数显式的式子，可以直接用于移动 $m$。一个足够条件是能在同一个原合法窗口内选取整数 $J$，使
$$
J<h,\qquad Q\ge R+J,\qquad J/x\to0,
$$
以及
$$
\chi_m^2\left(1+\frac1m\right)^2
\frac{(x+J+1)^3}{J+1}
\exp[-\gamma_m(J-d+2)]
\longrightarrow0.
\tag{7.1}
$$
不能只保留 $J=O_m(\log x)$ 而省略 $\gamma_m$ 和 $\chi_m$。

特别，若仅用 (1.1) 的原头环境相似条件数，则
$$
\gamma_m\asymp\frac1{(d-1)\chi_m}
$$
在 $\chi_m$ 大时成立；该量可以非常小。本文没有证明其费用能进入已有
$Q\le\exp[(25+1/64)d^3]$ 的同源带权母窗口。固定 $m$ 时让 $x$ 任意大，也不自动保留把 $\mathcal L_m$ 的向量运输到原全局 $T$ 的 carry 与封口预算。

原 $C$ 的多降阶项没有消失：它们全部存于 $G_m$ 和 $K_J$ 的非对角带中。新结论的作用是将截断 top 变成真正完整物理逆上的一个明确可估量，并在固定原头时支付同实际测试的完整一次 MP；进一步的 moving-$m$ 条件改善、精确封口和原 $N=M$ 仍需后继同源估计。
