# R77：迭代 Frobenius 与短输入的完整惰性证书

日期：2026-11-12。状态：实际恢复公式、锐整除界及有限精度均已证明。
完整证明见[迭代矩阵和完整 jets](../notes/2026-11-12-iterated-gm-frobenius-and-complete-inert-jets.md)。

固定惰性 $p\ge7$，令 $k=p^n,m=(p+1)p^n$。所有对象来自 R66/R68 的实际晶体和固定 $M_1$。

## 1. 有理二次 Frobenius 完全恢复高权

行约定 $F=Y(t^p)F_0Y^{-1}$、$F_0^2=-pI$ 给

$$
F_{[h]}=Y(t^{p^h})F_0^hY^{-1},\qquad
Q_h=F_0^{-h}F_{[h]}=Y^{-1}+O(t^{p^h}).
$$

取 $h=n+2$，$\mathcal K=(Q_h)_{22}$、$\mathcal L=-(Q_h)_{12}/t$，则

$$
C_m=[t^m]M_1\frac{\mathcal K^m}{\mathcal L^{m+1}}
$$

在特征零完全相等。实际所需周期次数仅到 $m-3$。
还可完全消去未知中心周期单位：

$$
G_p=F_{[2]}=-pY(t^{p^2})Y^{-1}
\in M_2(\mathbb Q[[t]])\cap M_2(\mathbb Z_p[[t]]).
$$

取足够多次 $G_p$ 的偶数迭代后除 $(-p)^a$ 即恢复所需 $Y^{-1}$。
归一一般非整，不能忽略其代价。

## 2. 真实 Hodge 整除的锐界

对 $1\le b\le\lfloor h/2\rfloor$，置 $d=h-2b+1$、$\tau=p+\cdots+p^d$。
则 $F_{[h]}/p^b$ 在次数严格小于 $\tau$ 时整，而

$$
v_p([t^\tau](F_{[h]})_{21})=b-1.
$$

证明使用真实四个条目的单位首项和唯一最低次数路径。
在恢复 $m=(p+1)p^n$ 所需的周期窗口中，整个矩阵最多共除一个 $p$；
CM 点上的 $p^{\lfloor h/2\rfloor}$ 整除不能移到整个 jet。

## 3. 完整中央导数的加强判据

R54 的实际半因子满足
$J_p(u)-J_p'(0)u\in p^2u^2\mathbb Z_p\langle u\rangle$，故
$J_p(p^n)/p^n\equiv J_p'(0)\pmod{p^{n+2}}$。
定义实际有理数

$$
S_{p,n}=p^{p^n}C_{(p+1)p^n}.
$$

保留全部阶乘与比较因子，准确有

$$
S_{p,n}\in\mathbb Z_p,\qquad
v_pS_{p,n}=2v_pJ_p(p^n),\qquad
J_p'(0)\ne0\iff\exists n\ge0:
S_{p,n}\not\equiv0\pmod{p^{4n+4}}.
$$

首层正是 $\beta_{p+1}$ 为单位；若 $j=v_pJ_p'(0)<\infty$，最迟在 $n=j-1$ 检出。
这覆盖完整导数，且只充分推出惰性初级有限，没有假定其反向。

## 4. 证书只需线性长度的实际输入

真实周期在 $\rho=p^{-1/(p+1)}$ 的范数满足
$\|K\|_\rho\le1$、$\|J-1\|_\rho\le\rho^2<1$、$\|M_1\|_\rho\le\rho^4$。
这些界由显式系数的逐 $p^a$ 计数证明。

置 $P=4n+4$、$L=P-1$、$D=\min\{m,2(p+1)L+4\}$。
把 $M_1$ 截到 $D$、$K,J$ 截到 $D-4$ 后，仍准确确定 $S_{p,n}\bmod p^P$。
取最小 $a\ge1$ 使 $p^{2a}>D-3$，足够的实际整输入为

- $G_p$ 到次数 $D-3$，模 $p^{L+a}$；
- 固定 $M_1$ 到次数 $D$，模 $p^L$。

[R81](R81-weighted-frobenius-precision-and-actual-kummer-iterate.md)进一步把 $G_p$ 的输入精度统一降到 $p^{4n+4}$。

故输入长度 $O(p(n+1))$、精度 $O(n+1)$、二次 Frobenius 迭代数
$O(1+\log_p(n+1))$。目标系数次数仍为 $m$，不声称全部运算复杂度线性。

**剩余任务：** 用实际固定单位或整数流的全局关系证明此完整证书无穷次成功。
