# R151. 两类中央失败的有限行与饱和 jet 的真正目标

日期：2026-11-12。**状态：本文各精确比较与预算已证明；主问题所需的统一整格改进仍开。**

完整证明见[联合中央失败与饱和行](../notes/2026-11-12-joint-central-failure-and-saturated-jet-rows.md)。

## 1. 完整失败确实增加一个明确的局部格条件

若固定目标只有有限多个初级有限素数，则两类实际半因子在固定有限集外均满足
$J_{A,p}'(0)=0$。普通侧用 R40 的充要结论，惰性只取 R54 充分结论的逆否。

对下降阶乘系数前缀 $a_1,\ldots,a_H$，中央行准确为
$$
L_H=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_h
 =\sum_{j=1}^H\frac{(-1)^{j+1}}j\binom HjJ(j).
$$
普通的 $J(j)$ 是带完整 Euler 比值的 $h_{j(p-1)}/h_{j(p-1)+4}$；
惰性的是 $j!(17c)^{-j}\beta_{j(p+1)}$，均是实际固定整数流输入。
准确尾界分别为
$$
M^{\rm o}_{p,H}=\min_{r>H}(r-v_p(r)),\qquad
M^{\rm i}_{p,H}
 =\left\lceil\frac{(H+1)(p-1)+4}{2p}\right\rceil+v_p(H!).
$$
完整失败强迫 $L_H\in p^M\mathbb Z_p$。
在原已证的 Gauss 系数包络中，这个条件准确增加指数 $p^{M-1}$。

令 $K$ 为**自然 $z$ Taylor 阶**上限，$H_p=\lfloor(K-4)/(p-\chi_{-4}(p))\rfloor$。
两类增加的总对数指数为
$$
\sum_p(M_{p,H_p}-1)\log p=\tfrac34K\log K+O(K).
$$
这是系数包络的一个线性条件，不是饱和评价的 arithmeticity 常数。
若以 $w=z^4$ 的阶 $k_w$ 计数，必须代入 $K=4k_w$，主项为
$3k_w\log k_w$。

## 2. 真正需要的条件是所有多项式列的同一行关系

对 R44/R47 的 $F(Z)=\sum e_mZ^m$，标准截面列是 $Z^aF^b$、$a+b\le D$。
记 $r_j$ 为其第 $j$ 系数行，$B$ 为独立前缀行。真实饱和评价满足
$$
\log\|\varphi_D^k\|_p
 =\{\delta_p(B)-\delta_p([B;r_k])\}\log p,
$$
而 $q$ 层整除等价于
$$
r_k\in\operatorname{row}_{\mathbb Q_p}(B)+p^q\mathbb Z_p^{N_D}.
$$
第1节只给选定半因子权的线性行，尚未给所有 $Z^aF^b$ 的这同一个关系。
不能从上述总指数直接扣减 jet 高度。

两类首坏带均可准确化成 value 前缀加 $P_Y$ 的合流矩阵；
若约化满秩，原 Smith 指数是 $q$ 个 $-2$ 和 $r+1$ 个 $0$，
$r=p-1$ 或 $p+1$。改变临界前缀系数 $e_r$ 只给末 value 行增加
一个已有导数行，故该合流行格不变。

## 3. 必须进入无界深带

对原中央图像的 $Z$ 阶 $k$，R44 的系数界给所有 $D$ 的统一估计
$$
\sum_{\substack{p>k/R\\p\notin S}}\log\|\varphi_D^k\|_p
 \le2k\log R+O(k),\qquad2\le R\le k/2.
$$
任意固定数目的坏带只贡献 $O(k)$。取 $R=\log k$，这一大素数部分是
$o(k\log k)$；因此目标 $D\asymp\sqrt k$ 的主要未付范围在
$p\le k/\log k$ 的无界深前缀。

R62 的固定 Euler 图像也有合法的实际规范：所有输出共乘 $G_0^D$
不改变任何饱和 jet 范数，列准确成为
$w^a(4K)^bG_0^{D-b}$。中央失败删除 $K$ 中的 $E_0$ Stokes 项，
但 $K^b$ 的非中央混合余类仍须保留；中央投影不是乘法同态。
这给出可继续攻击的实际混合列，而没有假定整个固定图像半径改善。
