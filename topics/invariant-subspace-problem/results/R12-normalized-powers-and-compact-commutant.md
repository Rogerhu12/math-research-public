# R12：归一化 dyadic 幂、无紧交换子与不变限制的稠密值域

日期：2026-11-12（北京时间）。状态：**已证明的中间结论**。分工：`universal_model`。

内部依赖：[R9](R9-radial-odometer-and-nilpotent-approximants.md) 的径向标量 odometer 及其精确 dyadic 幂公式。本文件给出自含推导，不对文献新颖性作判断；没有构造普通不变子空间，也没有排除其存在。

## 1. 设定与结论

在 $H=L^2(\mathbb Z_2,\mu)$ 上，$\mu$ 是 Haar 概率测度，令

$$
(Af)(y)=w(y)f(y-1),\qquad
w(y)=a_{v_2(y)}\quad(y\ne0),\qquad w(0)=0.
\tag{1.1}
$$

R9 的权 $a_r=e^{-10-B_r}$ 严格递减、正且趋于零，并满足

$$
\eta_k:=\frac{a_{k+1}}{a_k}
=\exp\bigl(-1400\,16^k+630\,8^k-300\,2^k\bigr)
\longrightarrow0.
\tag{1.2}
$$

以下结论实际上只需要 $a_r>0$ 递减且 $a_{k+1}/a_k\to0$。记

$$
C_k=\prod_{s=0}^{k-1}a_s^{\,2^{k-s-1}},\qquad
F_k=\frac{A^{2^k}}{\|A^{2^k}\|}\quad(k\ge1).
\tag{1.3}
$$

**定理 1.1。** 有

$$
\|F_k\|=1,\qquad
\|F_k^2\|=\eta_k\longrightarrow0,\qquad
F_k\xrightarrow{\mathrm{WOT}}\frac12I.
\tag{1.4}
$$

而且对每个 $f\in H$，

$$
\lim_{k\to\infty}\left\|\left(F_k-\frac12I\right)f\right\|
=\frac12\|f\|.
\tag{1.5}
$$

由此得到：

1. 与 $A$ 交换的紧算子只有零算子。
2. 对每个闭 $A$-不变子空间 $M$ 及每个整数 $j\ge1$，都有 $\overline{A^jM}=M$。
3. 对每个非零闭 $A$-不变子空间 $M$，限制 $A|_M$ 的交换子中也没有非零紧算子。特别地，$A|_M$ 本身不紧。

$F_k$ 是归一化幂，**不是投影**。(1.4) 没有矛盾：两个同时变化的算子的乘积不保持 WOT 收敛。

## 2. 归一化幂逼近移动到高位的矩阵单位

把 $y$ 写为 $y=r+2^kz$，其中 $0\le r<2^k$。R9 §4 已证明

$$
A^{2^k}=I_{2^k}\otimes(C_kA^{(k)}),\qquad
(A^{(k)}g)(z)=a_{k+v_2(z)}g(z-1).
\tag{2.1}
$$

平移是酉算子，而 $\{z:v_2(z)=0\}$ 的测度为 $1/2$，所以

$$
\|A^{(k)}\|=a_k,\qquad
\|A^{2^k}\|=C_ka_k>0.
\tag{2.2}
$$

再按 $z$ 的最低位分解 $L^2(\mathbb Z_2)\cong\mathbb C^2\otimes L^2(\mathbb Z_2)$。删去由奇数 $z-1$ 进位到偶数 $z$ 的边后，$A^{(k)}/a_k$ 只剩

$$
e_{10}\otimes I,\qquad e_{10}e_0=e_1,\quad e_{10}e_1=0.
$$

被删去部分的权的本质上确界为 $a_{k+1}/a_k$。故若 $E_k$ 表示在第 $k$ 个二进位上作用 $e_{10}$、在其他位上作用恒等算子的算子，则

$$
\boxed{\|F_k-E_k\|=\eta_k\longrightarrow0.}
\tag{2.3}
$$

这里位编号从 $0$ 开始。具体地，$E_k$ 把第 $k$ 位为 $0$ 的输入移到第 $k$ 位为 $1$，其余位不变；在第 $k$ 位为 $1$ 的输入上为零。若 $b_k(y)\in\{0,1\}$ 是第 $k$ 位，则

$$
E_k^*E_k=M_{\mathbf1_{\{b_k=0\}}},\qquad
E_kE_k^*=M_{\mathbf1_{\{b_k=1\}}},\qquad E_k^2=0.
\tag{2.4}
$$

特别地 $\|E_k\|=1$。注意这里使用的是 Haar 乘积表示：每一位的参考向量是 $(e_0+e_1)/\sqrt2$。

## 3. 范数、弱极限和逐向量缺口

由定义及 (2.2)，$\|F_k\|=1$。又

$$
C_{k+1}=C_k^2a_k,
$$

所以

$$
\|F_k^2\|
=\frac{\|A^{2^{k+1}}\|}{\|A^{2^k}\|^2}
=\frac{C_k^2a_ka_{k+1}}{C_k^2a_k^2}
=\eta_k.
\tag{3.1}
$$

若 $f,g$ 都只依赖前 $m$ 位，且 $k\ge m$，则第 $k$ 位与 $f,g$ 独立。该位参考向量上 $e_{10}$ 的矩阵系数为 $1/2$，故

$$
\langle E_kf,g\rangle=\frac12\langle f,g\rangle.
\tag{3.2}
$$

柱函数稠密，且 $\|E_k\|=1$，从而 $E_k\to I/2$ 于 WOT。结合 (2.3)，得到 $F_k\to I/2$ 于 WOT。同理，(2.4) 中两个位投影都 WOT 收敛到 $I/2$。

对任意 $f\in H$，因此

$$
\begin{aligned}
\left\|\left(E_k-\tfrac12I\right)f\right\|^2
&=\langle E_k^*E_kf,f\rangle
  -\operatorname{Re}\langle E_kf,f\rangle+\tfrac14\|f\|^2\\
&\longrightarrow
\tfrac12\|f\|^2-\tfrac12\|f\|^2+\tfrac14\|f\|^2
=\tfrac14\|f\|^2.
\end{aligned}
\tag{3.3}
$$

(2.3) 给出

$$
\left|\left\|(F_k-\tfrac12I)f\right\|
-\left\|(E_k-\tfrac12I)f\right\|\right|
\le\eta_k\|f\|,
$$

证明 (1.5)。所以当 $f\ne0$ 时，$F_kf$ 没有范数收敛子列：任何这样的子列的强极限都必须等于其弱极限 $f/2$，与 (1.5) 冲突。

## 4. 交换子不含非零紧算子

设紧算子 $K$ 满足 $KA=AK$。则 $KF_k=F_kK$。固定 $f\in H$，由 $F_kf\rightharpoonup f/2$ 及紧性，

$$
KF_kf\longrightarrow\tfrac12Kf\qquad\text{于范数}.
\tag{4.1}
$$

故交换关系推出 $F_kKf\to Kf/2$ 于范数。但 (1.5) 应用于向量 $Kf$，给出

$$
\lim_k\|(F_k-\tfrac12I)Kf\|=\tfrac12\|Kf\|.
$$

于是 $Kf=0$。$f$ 任意，得到 $K=0$。

这排除了直接在 $\{A\}'$ 中寻找非零紧算子来套用 Lomonosov 定理的路线；它不排除其他方式构造普通不变子空间。

## 5. 每个不变限制都有稠密值域

设 $M$ 是闭 $A$-不变子空间，$x\in M$，并固定 $j\ge1$。当 $2^k\ge j$ 时，

$$
2F_kx
=A^j\left(\frac{2A^{2^k-j}x}{\|A^{2^k}\|}\right)
\in A^jM.
\tag{5.1}
$$

另一方面，$2F_kx\rightharpoonup x$。线性子空间 $A^jM$ 的范数闭包也是弱闭的，因此 $x\in\overline{A^jM}$。反向包含由 $A$-不变性给出，故

$$
\boxed{\overline{A^jM}=M\qquad(j\ge1).}
\tag{5.2}
$$

R9 已证明 $A$ 单射，所以 $A|_M$ 同样单射；(5.2) 表明其值域在 $M$ 中稠密。此处没有证明 $A|_M$ 满射，更没有证明 $M=H$。

## 6. 结论在非零不变限制中继续成立

仍令 $M\ne\{0\}$ 为闭 $A$-不变子空间。$F_k|_M$ 是 $A|_M$ 的标量倍幂，范数不超过 $1$。由 §3，

$$
F_k|_M\xrightarrow{\mathrm{WOT}}\tfrac12I_M,
\qquad
\|(F_k|_M-\tfrac12I_M)x\|\longrightarrow\tfrac12\|x\|
\quad(x\in M).
\tag{6.1}
$$

若 $K\in\mathcal B(M)$ 紧且与 $A|_M$ 交换，则 §4 的同一论证在 $M$ 内逐字成立，给出 $K=0$。

由于 $A$ 单射且 $M\ne\{0\}$，$A|_M\ne0$，而它当然与自身交换。因此 $A|_M$ 不是紧算子。由此也可看出 $M$ 必为无限维。

这些性质给可能存在的普通不变子空间施加了限制，但没有否定这类子空间的存在性。特别地，“每个限制的值域稠密”与“每个非零向量对整个 $H$ 循环”是不同命题。
