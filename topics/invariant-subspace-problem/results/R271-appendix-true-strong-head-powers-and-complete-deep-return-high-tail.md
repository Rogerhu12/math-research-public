# R271 附录：原强头真实幂支付全部深返回的高段，且不依赖幂零高度

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对原 $C=A_m+D_{[m,x)}$，真正的旧头借位幂界与强位的有限幂零阶共同给出
$$
\|C^j\|\le7^j\exp\{-\gamma(j-x)_+^4\},\qquad \gamma=770/256.
$$
将它与原连续尾各固定层的完整右逆界合并，可以支付 canonical 全深修复在
$$
j\ge J_*(x):=\left\lceil x+2\sqrt{x}(\log x)^{1/4}\right\rceil
$$
的**整个正交高段**，平方费用至多 $e^{-x^2\log x}\|a\|^2$。这个界保所有顺次 MP 的真实域，不把 $(D^\dagger)^j$ 换成 $(D^j)^\dagger$，不要求 $h\le2x$，也不以无速率的源能量 $\epsilon_m$ 乘增长常数。

因此，前稿相容塔线性下界所在的 $j\ge3x/2$ 区间，对原 $R=d$ 模型已被真实幂支付。尚未付清的是 $j<J_*(x)$ 的中段及其同源完整最小化；本稿不证明全修复小或 $N=M$。

依据：

- [低物理孔借位幂与完整 Gram 压缩](R271-appendix-low-physical-hole-borrow-powers-and-complete-gram-compression.md)，原 N/Y 两型共同的 $\gamma=770/256$ 幂界；
- [原连续尾完整固定层右逆](R234-appendix-quartic-head-powers-and-super-four-thirds-hole-weights.md)，§1(1.1)；
- [真实强前缀与原大头完整 Gram 比较](R271-appendix-actual-strong-head-gram-comparison-and-true-far-variance-source-limit.md)；
- [相容塔精确边际与同源全深返回平方](R271-appendix-continuous-compatible-vacuum-tower-marginals-and-linear-deep-return-barrier.md)，尤其 §5。

## 1. 真强头的四次高幂衰减

取原 N 或 Y 模型，$m\ge10$、$d=2^m$。令
$$
R\ge0,\qquad x=m+R,\qquad
E=D_{[m,x)}=\sum_{i=m}^{x-1}(i+1)^{-2}E_i,
$$
$$
C=A_m+E,\qquad h=d+R,\qquad C^h=0.
\tag{1.1}
$$
旧头和强位作用于不同张量因子，因而严格对易。所有强位状态保留，没有压到真空或某一个对称扇区。

原低物理孔定理对完整 $m$ 位头直接给
$$
\|A_m^k\|\le6^k e^{-\gamma(k-m)_+^4},
\qquad \gamma=\frac{770}{256}.
\tag{1.2}
$$
另一方面，
$$
E^{R+1}=0,\qquad
\|E\|\le\sum_{i=m}^{x-1}(i+1)^{-2}\le\frac1m\le1.
\tag{1.3}
$$
在 $C^j$ 的二项式展开中，非零项 $A_m^kE^{j-k}$ 必有 $k\ge j-R$。所以
$$
(k-m)_+\ge(j-x)_+.
$$
逐项使用 (1.2)--(1.3)，得到全部 $j\ge0$ 的真实算子界
$$
\begin{aligned}
\|C^j\|
&\le e^{-\gamma(j-x)_+^4}
\sum_{k=0}^j\binom jk6^k\\
&=\boxed{7^j e^{-\gamma(j-x)_+^4}.}
\end{aligned}
\tag{1.4}
$$
$j\ge h$ 时左侧本来为零。证明保留 N 型全部加权幂及 Y 型全部 Cayley 项；其唯一旧输入正是已经分别适用于两型的 (1.2)。

## 2. 完整顺次真空塔的合法粗上界

在真正远尾 $D=D_x$ 上定义
$$
v_0=\Omega,\qquad v_j=(D^\dagger)^j\Omega.
\tag{2.1}
$$
原完整固定层右逆定理给
$$
D:\mathcal H_r\longrightarrow\mathcal H_{r-1}\quad\hbox{满射},
$$
$$
\|D^\dagger:\mathcal H_{r-1}\to\mathcal H_r\|
\le[10000(x+r)^2]^r,\qquad r\ge1.
\tag{2.2}
$$
这里是以已付右逆范数控制真正最小右逆；不要求全孔直和的 $D^\dagger$ 有界。

每一个固定有限 $j$ 因而都在全部顺次 MP 的自然域，且
$$
Dv_j=v_{j-1}.
$$
乘 (2.2) 并保 $r\le j$，得到
$$
\boxed{
\|v_j\|^2
\le[10000(x+j)^2]^{j(j+1)}.
}
\tag{2.3}
$$
(2.3) 本身十分粗；它仅在 (1.4) 已给四次负指数的高段使用。本文不把它带回中低段作有效预算。

同时
$$
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=(j!)^2e_j(b^2)\le j!S_x^j,
$$
$$
\frac1{3(x+1)^3}\le S_x.
\tag{2.4}
$$

## 3. 同一个任意头源，完整真核与相干截断

给定任意强头向量 $a$、$s\ge S_x$，并取整数
$$
0\le J\le h-1.
$$
定义
$$
F_{s,J}(a)=
\sum_{j=0}^J\frac{(-C)^ja\otimes\omega_j}{s^jj!},
\qquad
z(a)=\sum_{j=0}^{h-1}(-C)^ja\otimes v_j.
\tag{3.1}
$$
相容性和 $C^h=0$ 给
$$
(C+D_x)z(a)=0.
\tag{3.2}
$$
$z(a)$ 在原第 $m$ 位以后的总孔数不超过 $R+h-1$；因此
$$
z(a)\in K_{m,Q}\qquad\text{若 }Q\ge R+h-1.
\tag{3.3}
$$
两列都是有限个固定远孔层的原物理 Hilbert 向量。其位置支撑可无限，但全部删除、创建及顺次 MP 均具有 §2 所述真实域。

令 $\mathsf P_{\ge k}^{>x}$ 表示远孔数至少 $k$ 的正交投影。由于不同 $j$ 层正交，
$$
\begin{aligned}
\|\mathsf P_{\ge k}^{>x}(F_{s,J}(a)-z(a))\|^2
=\sum_{j=k}^{h-1}
\|C^ja\|^2
\left\|
\mathbf1_{\{j\le J\}}\frac{\omega_j}{s^jj!}-v_j
\right\|^2.
\end{aligned}
\tag{3.4}
$$
不需要在 $h$ 个修复项之间作三角估计。特别，本稿高段界对截断 $J$ 一致，包含完整 $J=h-1$。

## 4. 整个高段的显式预算

### 定理 4.1

在 (1.1)--(3.1) 下，若 $x\ge1024$，置
$$
J_*(x)=
\left\lceil x+2\sqrt{x}(\log x)^{1/4}\right\rceil.
\tag{4.1}
$$
则对任意幂零高度 $h=d+R$、任意 $J<h$、任意 $a$ 和 $s\ge S_x$，
$$
\boxed{
\|\mathsf P_{\ge J_*(x)}^{>x}
(F_{s,J}(a)-z(a))\|^2
\le e^{-x^2\log x}\|a\|^2.
}
\tag{4.2}
$$
若 $J_*(x)\ge h$，左侧为零。无需 $h\le2x$。

**证明。** 分两段，所有对数为自然对数。

先设 $J_*(x)\le j<2x$。由 (2.3)，
$$
\log\|v_j\|^2
\le j(j+1)\log(90000x^2)
\le20x^2\log x,
$$
因为 $j(j+1)\le5x^2$、$\log(90000x^2)\le4\log x$ 对 $x\ge1024$ 成立。结合 (1.4) 与 $4x\log7\le x^2\log x$，
$$
\|C^ja\|^2\|v_j\|^2
\le
\exp\{21x^2\log x-2\gamma(j-x)^4\}\|a\|^2.
\tag{4.3}
$$
而 $j-x\ge2\sqrt{x}(\log x)^{1/4}$，所以
$$
2\gamma(j-x)^4\ge32\gamma x^2\log x
=\frac{385}{4}x^2\log x.
$$
于是 (4.3) 不超过 $e^{-75x^2\log x}\|a\|^2$。

相干项用 (2.4) 和 $s\ge S_x$：
$$
\left\|\frac{C^ja\otimes\omega_j}{s^jj!}\right\|^2
\le
7^{2j}[3(x+1)^3]^j
e^{-2\gamma(j-x)^4}\|a\|^2.
\tag{4.4}
$$
对 $j<2x$，
$$
2j\log7+j\log[3(x+1)^3]\le x^2\log x
\qquad(x\ge1024),
$$
所以 (4.4) 也小于同一个 $e^{-75x^2\log x}\|a\|^2$。
使用 $\|v-w\|^2\le2\|v\|^2+2\|w\|^2$，并对不足 $2x$ 个正交层求和，这一段总量不超过
$$
8x e^{-75x^2\log x}\|a\|^2
\le e^{-2x^2\log x}\|a\|^2.
\tag{4.5}
$$

再设 $j\ge2x$。这段不依赖 $h$ 的上界。此时 $j-x\ge j/2$、$j\ge2048$，
$$
\log[10000(x+j)^2]\le4\log j.
$$
由 (1.4)、(2.3)，
$$
\begin{aligned}
\log\frac{\|C^ja\|^2\|v_j\|^2}{\|a\|^2}
&\le9j^2\log j-\frac{\gamma}{8}j^4\\
&\le-\frac14j^4.
\end{aligned}
\tag{4.6}
$$
最后一步用 $9\log j\le j^2/8$ 及 $\gamma>3$。相干项 (4.4) 的正对数在此段更小，同样至多 $9j^2\log j$，故也满足 (4.6)。

因此全部 $j\ge2x$ 的差平方总量至多
$$
4\sum_{j\ge2x}e^{-j^4/4}\|a\|^2
\le8e^{-4x^4}\|a\|^2
\le e^{-2x^2\log x}\|a\|^2.
\tag{4.7}
$$
中间不等式由
$j^4\ge(2x)^4+4(2x)^3(j-2x)$ 的几何和直接得到。
合并 (4.5)、(4.7)，再用
$2e^{-2x^2\log x}\le e^{-x^2\log x}$，即得 (4.2)。证毕。

同一证明还分别支付 $F_{s,J}(a)$ 和 $z(a)$ 的这些高层范数；没有依赖二者互相抵消。

## 5. 原完整最小源、实际窗口与仍剩的中段

取完整或截断最小源
$$
a=H_{C,J}(s)^{-1}g,\qquad
H_{C,J}(s)=\sum_{j=0}^J\frac{(C^*)^jC^j}{s^jj!}.
$$
因 $H_{C,J}\succeq I$，(4.2) 的右侧可直接换成
$e^{-x^2\log x}\|g\|^2$；不需假定 $a$ 的强孔支持，也不需 $\epsilon=\sum_{j\ge1}\|C^ja\|^2/(s^jj!)$ 的收敛率。

特别取原
$$
m\ge10,\qquad R=d=2^m,\qquad x=m+d,\qquad h=2d.
$$
则 $x\ge1024$，真核列 (3.2) 的总孔数至多 $3d-1$。所以对原任意
$$
4d\le Q\le e^{26d^3}
$$
该列属于同一个 $K_{m,Q}$，而 $F_{s,J}$ 的原 $V_Q/K_Q/u_f$ 同源身份也成立，因为 $Q\ge R+J$。这些是两条分别核过的包含；未将原高出生商免费识别为真核。

又
$$
J_*(x)\le\lceil3x/2\rceil
$$
对 $x\ge1024$ 成立。因此相容塔前稿对 $j\ge3x/2$ 的线性必要代价，在原 $C$ 上已由 (4.2) 支付。该必要条件不是这个实际源的新障碍。

更一般，若 $R=0$ 且 $m=x\ge1024$，同一结论把 canonical 全修复的全部 $j\ge m+O(\sqrt m\log^{1/4}m)$ 也支付掉，尽管完整 nilpotency 仍为 $2^m$。这只是原模型中的高段预算，不取消其他路线曾要求的 $R=d$ 强块门，也不改变原 cut/carry 规则。

尚需控制的准确剩余量是
$$
\sum_{1\le j<J_*(x)}
\|C^ja\|^2
\left\|
\mathbf1_{\{j\le J\}}\frac{\omega_j}{s^jj!}-v_j
\right\|^2,
$$
或能替代它的更小完整源依赖真核距离。这里 $j$ 可与 $x$ 同阶；(1.4) 的四次负指数在 $j\le x$ 为零，不能继续向下套用。现有一次／二次 MP 与同源正能量仍可在其原范围内使用，但本稿没有由已付高段推出整个 deep return 或 $N=M$。
