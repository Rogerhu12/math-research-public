# 两个实际最大除法域的零前缀与占满前缀图正则性

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下无条件最大图域估计、加权图嵌入及图核心正交余空间的准确方程已证明；没有支付真实 $\alpha_q^{-1/8}$ 输出逆权、同 $W$ 的 $\Gamma$ 或两道完整范围核心。**

使用[实际除法闭关系](R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)中的
$$
G=G_0^*,\qquad SGy=T^*y,\qquad
A_{\max}=J_BT,\qquad BA_{\max}v=Tv,
$$
其中 $S=B^*$，$J_B$ 的值域在 $e_0^\perp$。两种 $T=T_N,T_Y$ 均保原全部 carry。

[全张量指数稿](R271-appendix-full-tensor-exponential-bound-and-improved-occupied-prefix-decay.md)已对 $M=\ker T$ 给占满前缀估计。本文的新增范围是整个 $\mathcal D(G)$ 和 $\mathcal D(A_{\max})$，并且前者控制的是相反的全零低前缀。因而这里不是把旧核结论重新标为一般图域结论。

## 1. 两个相反的实际前缀

记
$$
V_n e_k=\mathbf1_{\{2^n\mid k\}}e_k,\qquad
Q_n e_k=\mathbf1_{\{2^n\mid k+1\}}e_k,
\qquad V_0=Q_0=I.
\tag{1.1}
$$
$V_n$ 要求低 $n$ 位全零，包含真空；$Q_n$ 要求低 $n$ 位全一，保留全部高位。不能将二者混用。

沿用
$$
a_j=(j+1)^{-2},\qquad
\eta_j=\alpha_{j+1}/\alpha_j,\qquad
D_r=\sum_{j\ge r}a_jE_j.
$$
原实际估计为
$$
\|N_j-E_j\|\le\eta_j,\qquad
\|Y_j-E_j\|\le4\eta_j,\qquad
\|(I+N_j)^{-1}\|\le3,
\tag{1.2}
$$
以及 $\eta_{j+1}\le\eta_j/4$、$\eta_j\le e^{-770\,16^j}$、$\alpha_j<1$。

**引理 1.1（两条实际边界行）。** 若 $0\le i<r$，则
$$
\boxed{
\|V_rN_i^*\|\le\frac{\alpha_r}{\alpha_i},\qquad
\|Q_rN_i\|\le\frac{\alpha_r}{\alpha_i}.
}
\tag{1.3}
$$
相应 Y 行分别至多为右边的三倍。

核对第一式可取伴随，考察 $N_iV_r$。对 $k\ge1$，准确 ruler 权乘积给
$$
N_i e_{2^r k}
=\frac{\alpha_{r+v_2(k)}}{\alpha_i}
 e_{2^r k-2^i};
$$
对 $k=0$ 输出为零。这些列正交，且 $\alpha_{r+v_2(k)}\le\alpha_r$。第二式考察 $N_i^*Q_r$：
$$
N_i^* e_{2^r k+2^r-1}
=\frac{\alpha_{r+v_2(k+1)}}{\alpha_i}
 e_{2^r k+2^r-1+2^i},
$$
同样为正交列。Y 型直接保留
$Y_i=N_i(I+N_i)^{-1}$ 及其完整伴随逆，使用 (1.2) 即得；不需要把低头截断后的逆替换成原逆。

对 $j\ge r$，$N_j,E_j,Y_j$ 都在低 $r$ 位上为恒等张量，故与 $V_r,Q_r$ 交换。由 (1.2)--(1.3) 和 $\sum_j a_j<2$，得到
$$
\boxed{
\|V_rT^*-D_r^*V_r\|\le8\eta_{r-1},\qquad
\|Q_rT-D_rQ_r\|\le8\eta_{r-1}.
}
\tag{1.4}
$$
这里将 $D_r$ 自然视为全空间上的纯高尾算子。统一 Y 界的低项小于
$6\eta_{r-1}$，高项小于 $8\eta_r\le2\eta_{r-1}$；N 型更小。所有高位差也保留在 (1.4) 中。

原移位还准确满足
$$
\boxed{
\|V_rS\|\le\alpha_r,\qquad
\|Q_rB\|\le\alpha_r.
}
\tag{1.5}
$$
它们分别只从低头全一列跨入全零行、以及从全零列跨入全一行；跨界权为某个 $\alpha_{r+j}$。

## 2. 最大伴随除法域的全零前缀

取任意实际最大图对
$$
y\in\mathcal D(G),\qquad f=Gy,\qquad T^*y=Sf.
\tag{2.1}
$$
写 $V_ry=e_0\otimes g_r$。由 (1.4)--(1.5)，
$$
\|D_r^*g_r\|
\le8\eta_{r-1}\|y\|+\alpha_r\|f\|
\le26\eta_{r-1}(\|y\|+\|f\|),
\qquad \|g_r\|\le\|y\|.
\tag{2.2}
$$
最后只用了 $\alpha_r=\eta_{r-1}\alpha_{r-1}\le\eta_{r-1}$，没有给形式来源使用未付范数。

定义
$$
\gamma_{\rm ex}
=\log2+\operatorname{arsinh}1+
\frac25\left(1-\frac1{\sqrt2}\right)>\frac53,
$$
$$
a(n)=e^{-\gamma_{\rm ex}n+4(\log n+1)^2},\qquad
b(n)=e^{-47n^4}\quad(n\ge2).
\tag{2.3}
$$

**定理 2.1。** 两种原模型对每个 $n\ge2$ 均有
$$
\boxed{
\|V_ny\|
\le a(n)\|y\|+b(n)(\|y\|+\|Gy\|).
}
\tag{2.4}
$$

给出与旧核证明相同的实际参数，以核清伴随方向。置
$$
r=\lceil\log_2n\rceil,\qquad m=n-r\ge1,
\qquad H=\sum_{j=r}^{n-1}a_jE_j^*,\qquad R=D_n^*.
$$
这些创建算子相互交换，而且
$$
H^m=m!\left(\frac{r!}{n!}\right)^2 E_r^*\cdots E_{n-1}^*.
$$
所以 $H^mg_r$ 的范数准确等于
$m!(r!/n!)^2\|V_ny\|$；创建乘积读取的是这些位全空的来源。另一方面
$$
H^m-(-R)^m=\sum_{k=0}^{m-1}H^{m-1-k}(-R)^kD_r^*,
\qquad \|H\|,\|R\|\le1/r.
$$
原完整张量恒等式及其伴随给
$$
\|e^{zD_n^*}\|
=\exp\sum_{j\ge n}\operatorname{arsinh}\frac{|z|a_j}{2}.
$$
在共同 Cauchy 半径 $2n^2$ 取 $m$ 阶系数，结合 (2.2)，得到
$$
\|V_ny\|\le A_n\|y\|+
B_n(\|y\|+\|f\|),
\tag{2.5}
$$
其中
$$
A_n=\left(\frac{n!}{r!}\right)^2(2n^2)^{-m}e^{n\mathcal I},
\quad
\mathcal I=\int_1^\infty\operatorname{arsinh}(u^{-2})\,du,
$$
$$
B_n=26\eta_{r-1}
\frac{m r^{-(m-1)}}{m!}\left(\frac{n!}{r!}\right)^2.
$$
全张量指数稿的准确阶乘与积分界给
$A_n\le a(n)$、$B_n\le b(n)$。其证明只使用上述 $26$、$\eta_{r-1}\le e^{-770\,16^{r-1}}$ 及两个算子的范数，全部与 (2.2) 一致。因此 (2.5) 证明 (2.4)。

顺带，$V_ny\to y_0e_0$，而 (2.4) 右边趋零，再次确认 $y_0=0$。这与原多值部 $\mathbb Ce_0$ 已给出的域结论相容，不作为新的真空结论重复登记。

## 3. 最大正向除法域的占满前缀

取
$$
v\in\mathcal D(A_{\max}),\qquad
z=A_{\max}v,\qquad Tv=Bz.
\tag{3.1}
$$
写 $Q_rv=e_{2^r-1}\otimes k_r$。由 (1.4)--(1.5)，
$$
\|D_rk_r\|
\le8\eta_{r-1}\|v\|+\alpha_r\|z\|
\le26\eta_{r-1}(\|v\|+\|z\|).
\tag{3.2}
$$
删除乘积 $E_r\cdots E_{n-1}$ 读取占满位，故 §2 的同一计算、这次不取伴随，给出
$$
\boxed{
\|Q_nv\|
\le a(n)\|v\|+b(n)(\|v\|+\|A_{\max}v\|)
\qquad(n\ge2).
}
\tag{3.3}
$$
$v\in M$ 时 $A_{\max}v=0$，恢复已付核估计；新增的是没有要求 $Tv=0$ 的整个最大图域范围。

## 4. 实际图范数中的指数位权

定义精确位块
$$
P_q^+=V_q-V_{q+1},\qquad P_q^-=Q_q-Q_{q+1}.
$$
前者是正整数指标 $v_2(k)=q$，后者是首缺位 $q$；二者不同。

对每个 $0<\gamma<\gamma_{\rm ex}$，存在明确有限常数 $K_\gamma$，使
$$
\boxed{
\sum_{q\ge0}e^{2\gamma q}\|P_q^+y\|^2
\le K_\gamma(\|y\|+\|Gy\|)^2
\qquad(y\in\mathcal D(G)),
}
\tag{4.1}
$$
$$
\boxed{
\sum_{q\ge0}e^{2\gamma q}\|P_q^-v\|^2
\le K_\gamma(\|v\|+\|A_{\max}v\|)^2
\qquad(v\in\mathcal D(A_{\max})).
}
\tag{4.2}
$$

具体地，取 $\gamma'=(\gamma+\gamma_{\rm ex})/2$，
$N_{\gamma'}=\lceil256/(\gamma_{\rm ex}-\gamma')^2\rceil$、
$C_{\gamma'}=2e^{\gamma'N_{\gamma'}}$，则 (2.4)、(3.3) 与同一个有限小尺度吸收给
$$
\|V_ny\|\le C_{\gamma'}e^{-\gamma'n}(\|y\|+\|Gy\|),
$$
以及 $Q_n,v,A_{\max}$ 的对应式。用
$\|P_q^+y\|\le\|V_qy\|$ 和 $\|P_q^-v\|\le\|Q_qv\|$ 求几何级数，可取
$$
K_\gamma=\frac{C_{\gamma'}^2}{1-e^{-2(\gamma'-\gamma)}}.
$$
(4.1) 中没有漏掉 $q=0$；真空系数已为零。两个最大图域本身都是实际 Hilbert 域，以上没有对未属于这些域的规范形式 $h(w)$ 作延拓。

## 5. 第一图核心正交余空间的两条原方程

令
$$
\mathcal C=
\overline{\{(Sh,T^*h):h\in\mathcal H\}}
\subset\operatorname{Graph}G,
\qquad
\mathcal E=\operatorname{Graph}G\ominus\mathcal C
$$
（正交补在 $\mathcal H\oplus\mathcal H$ 的实际图范数中取）。由有界列算子的伴随，对 $(y,f)\in\mathcal H\oplus\mathcal H$ 准确有
$$
\boxed{
(y,f)\in\mathcal E
\iff T^*y=Sf,\quad By+Tf=0.
}
\tag{5.1}
$$
第一式本身保证 $y\in\mathcal D(G)$、$Gy=f$；第二式准确表达与所有 $(Sh,T^*h)$ 正交。由于 $y_0=0$，第二式也给
$$
f\in\mathcal D(A_{\max}),\qquad A_{\max}f=-y.
\tag{5.2}
$$
这里使用 $J_BB=I-e_0\otimes e_0$，没有把 $A_{\max}$ 替换为 $A_{\min}$。

于是任意真正图核心缺陷对同时满足
$$
\boxed{
\begin{aligned}
\|V_ny\|&\le a(n)\|y\|+b(n)(\|y\|+\|f\|),\\
\|Q_nf\|&\le a(n)\|f\|+b(n)(\|y\|+\|f\|).
\end{aligned}
}
\tag{5.3}
$$
这些是相反两端的实际图正则性；本文未证明 $\mathcal E=0$。若 $\mathcal E=0$，则第一道图核心成立；第二道精确可除值域在全部闭包可除源中的稠密性仍是另一个问题。

## 6. 对真实 $W$ 的范围与剩余费用

如果已经对同一 $w=Ju\in W$ 支付 $\Gamma(u)<\infty$，则
$y=Sh(w)\in\mathcal D(G)$、$Gy=w$，故 (2.4)、(4.1) 无条件适用于这个真实 $y$。这是原 dyadic 尾量 $\|y_r\|\to0$ 的统一图范数指数改进。

但 $e^{2\gamma q}$ 只是位号的指数权；原
$-\log\alpha_q=\Theta(16^q)$。因此 (4.1) 不能代替
$$
\sum_q\alpha_q^{-1/8}\|P_q^+y\|^2<\infty,
$$
也不能支付 $\lambda_r\|y_r\|$ 中
$\lambda_r\asymp a_{r-1}/\alpha_{r-1}$ 的实际增长。没有先证明 $\Gamma(u)<\infty$ 时，更不能把 (2.4) 用在尚不属于 Hilbert 空间的形式 $Sh(w)$ 上。

下一步仍须利用同一 $W$ 来源或 (5.1) 的两条联合方程，支付真正图/范围核心；本稿不以这些指数位权替换它们。
