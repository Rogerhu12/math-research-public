# 有限物理块 Cayley 正则器：真空小量、全块 Walsh 增益与真实进位预算

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：本稿全部有限块和实际扰动结论完整证明。** 本稿只提供全局正则器构造所需的有限块估计，不声称无穷乘积收敛，不构造慢主理想的分母或见证专属配对正则器。

## 1. 有限块与结论

在 $Q$ 个物理位的 Haar 空间
$$
H_Q=\bigotimes_{j=1}^Q(\mathbb C^2,\Omega_+),
\qquad \Omega_+=(e_0+e_1)/\sqrt2,
$$
置
$$
S_Q=\sum_{j=1}^QE_j,\qquad E_j=e_{10}^{(j)},\qquad
K_Q=\frac{2S_Q}{Q+1},\qquad
F_Q=(I-K_Q)(I+K_Q)^{-1}.
\tag{1.1}
$$
令 $\Omega$ 为常数函数 $1$，令 $\chi$ 为这 $Q$ 位的完整 Walsh 积。二者都是单位向量。

**定理 1.1。** 对每个整数 $Q\ge1$，$K_Q$ 是幂零收缩，$F_Q$ 增生，并有
$$
\boxed{\|F_Q\Omega\|\le\frac{10}{\sqrt{Q+1}},}
\tag{1.2}
$$
$$
\boxed{
0\le\langle F_Q\Omega,\Omega\rangle
\le\frac4{Q+1},
}
\tag{1.3}
$$
以及
$$
\boxed{
\|F_Q\chi\|\ge c_0\sqrt Q,
\qquad c_0=\frac{\sqrt3}{8e}.
}
\tag{1.4}
$$
(1.3) 的均值本身为实数。另有
$$
\|(I+K_Q)^{-1}\|\le Q+1,\qquad
\|F_Q\|\le2Q+1.
\tag{1.5}
$$

## 2. 收缩性和增生性

物理占据数为 $k$ 的层以 $k$ 元子集为正交基。$S_Q$ 把它送入 $k+1$ 层；对应矩阵的每个输出行有 $k+1$ 个 $1$，每个输入列有 $Q-k$ 个 $1$。对输入系数 $v_A$，
$$
\begin{aligned}
\|S_Qv\|^2
&=\sum_{|B|=k+1}\left|\sum_{j\in B}v_{B\setminus\{j\}}\right|^2\\
&\le(k+1)\sum_{|B|=k+1}\sum_{j\in B}|v_{B\setminus\{j\}}|^2\\
&=(k+1)(Q-k)\|v\|^2.
\end{aligned}
$$
在该层的常系数向量上等号成立，所以
$$
\|S_Q\|=\max_{0\le k<Q}\sqrt{(k+1)(Q-k)}
\le\frac{Q+1}{2}.
\tag{2.1}
$$
因此 $\|K_Q\|\le1$，且 $K_Q^{Q+1}=0$。

有限 Neumann 和给
$$
(I+K_Q)^{-1}=\sum_{r=0}^Q(-K_Q)^r,
\qquad
F_Q=I+2\sum_{r=1}^Q(-K_Q)^r,
$$
立即得到 (1.5)。准确 Cayley 恒等式为
$$
\operatorname{Re}F_Q
=(I+K_Q^*)^{-1}(I-K_Q^*K_Q)(I+K_Q)^{-1}\ge0.
\tag{2.2}
$$
这证明增生性，不要求 $\|K_Q\|<1$。尤其奇数 $Q$ 时可能发生的 $\|K_Q\|=1$ 不造成定义域或可逆性问题。

## 3. 两个准确占据数积分

记
$$
a=\frac2{Q+1}.
$$
在物理点 $y$ 上令 $k=k(y)$ 为其中 $1$ 的数量。因为
$$
S_Q^r\Omega(y)=(k)_r,\qquad
S_Q^r\chi(y)=(-1)^r(k)_r\chi(y),
$$
有限 Neumann 和准确给
$$
\begin{aligned}
((I+K_Q)^{-1}\Omega)(y)
&=I_k^-:=\int_0^\infty e^{-t}(1-at)^k\,dt,\\
((I+K_Q)^{-1}\chi)(y)
&=\chi(y)I_k^+,\qquad
I_k^+:=\int_0^\infty e^{-t}(1+at)^k\,dt.
\end{aligned}
\tag{3.1}
$$
这些积分只涉及有限多项式，逐项积分完全合法。它们不来自未经证明的无限级数或收敛半群替换。

由于 $F_Q=2(I+K_Q)^{-1}-I$，
$$
F_Q\Omega(y)=2I_k^--1,
\qquad
F_Q\chi(y)=\chi(y)(2I_k^+-1).
\tag{3.2}
$$
Haar 测度下 $k$ 服从 $\operatorname{Bin}(Q,1/2)$。

## 4. 负号积分的统一误差

以下估计同时用于范数和均值。设 $0<b\le2/(Q+1)$，$0\le k\le Q$，并记
$$
J_k(b)=\int_0^\infty e^{-t}(1-bt)^k\,dt.
$$
$k=0$ 时 $J_0(b)=1$。对 $k\ge1$，在 $0\le u\le1$ 上，
$$
0\le e^{-ku}-(1-u)^k
\le\frac{k}{2}u^2e^{-(k-1)u}.
\tag{4.1}
$$
事实上 $e^{-u}\ge1-u$，
$e^{-u}-(1-u)\le u^2/2$，再对两个数的 $k$ 次幂作望远镜差即可。

将 $u=bt$ 代入 (4.1)，在 $[0,1/b]$ 上积分并向上延伸非负上界，得到主段误差至多
$$
\frac{k b^2}{[1+(k-1)b]^3}.
\tag{4.2}
$$
负号尾也可准确计算：
$$
\int_{1/b}^\infty e^{-t}|1-bt|^k\,dt
=e^{-1/b}b^k k!.
$$
由 AM--GM，
$$
k!\le\left(\frac{k+1}{2}\right)^k,
\qquad
b^kk!\le\left(\frac{k+1}{Q+1}\right)^k\le1.
\tag{4.3}
$$
相应指数尾满足
$\int_{1/b}^\infty e^{-(1+kb)t}dt\le e^{-1/b}$。所以
$$
\boxed{
\left|J_k(b)-\frac1{1+kb}\right|
\le\frac{k b^2}{[1+(k-1)b]^3}+2e^{-1/b}.
}
\tag{4.4}
$$
这已包括 $1-bt$ 变负后的整个积分，不舍去该部分。

## 5. 真空范数和均值

令 $n=Q+1\ge2$。在 (4.4) 中取 $b=a=2/n$，得对所有 $k$
$$
\left|2I_k^--1-\frac{1-ak}{1+ak}\right|
\le\frac8n+4e^{-n/2}.
\tag{5.1}
$$
其中 $k=0$ 的左端实际为零，故统一界也成立。

因为 $1+ak\ge1$，
$$
\mathbb E\left|\frac{1-ak}{1+ak}\right|^2
\le\mathbb E|1-ak|^2
=\frac{\mathbb E(Q+1-2k)^2}{(Q+1)^2}
=\frac1{Q+1}.
\tag{5.2}
$$
最后一步使用 $\mathbb E k=Q/2$、$\operatorname{Var}k=Q/4$。于是
$$
\|F_Q\Omega\|
\le n^{-1/2}+8n^{-1}+4e^{-n/2}
\le10n^{-1/2}.
$$
对最后常数，可用 $n\ge2$ 及
$\sqrt n\,e^{-n/2}\le\sqrt2/e$，得到系数
$1+4\sqrt2+4\sqrt2/e<10$。这证明 (1.2)。

均值应先对占据数平均，不能用 (1.2) 的 $Q^{-1/2}$ 上界替代所需 $Q^{-1}$ 精度。有限二项式恒等式给
$$
\mathbb E(1-at)^k=(1-at/2)^Q.
$$
因此
$$
\langle F_Q\Omega,\Omega\rangle
=2J_Q(1/n)-1.
\tag{5.3}
$$
在 (4.4) 中取 $b=1/n$、$k=Q=n-1$，得到
$$
2J_Q(1/n)-1
\le\frac1{2n-1}+\frac2n+4e^{-n}.
$$
对 $n\ge2$，
$$
\frac n{2n-1}\le\frac23,\qquad
4ne^{-n}\le8e^{-2},
\qquad
\frac23+2+8e^{-2}<4.
$$
故均值至多 $4/n$。它是实数，而 (2.2) 保证其非负，证明 (1.3)。

## 6. 全块 Walsh 向量的平方根增益

由 (3.1)，$I_k^+\ge1$，所以
$$
2I_k^+-1\ge I_k^+.
\tag{6.1}
$$
Chebyshev 不等式给
$$
\mathbb P\{k\ge Q/2-\sqrt Q\}\ge3/4.
\tag{6.2}
$$
这对小 $Q$ 也成立，若阈值为负则事件就是整个空间。

在 (6.2) 的事件上，取 $0\le t\le\sqrt Q/4$。对 $u\ge0$，
$\log(1+u)\ge u-u^2/2$，于是
$$
-t+k\log(1+at)
\ge(ak-1)t-\frac{k a^2t^2}{2}.
$$
此处
$$
ak-1\ge-\frac{1+2\sqrt Q}{Q+1},
$$
故线性负项的绝对值不超过
$$
\frac{2Q+\sqrt Q}{4(Q+1)}\le\frac34.
$$
而二次项至多
$$
\frac{Q a^2}{2}\frac{Q}{16}
=\frac{Q^2}{8(Q+1)^2}\le\frac18.
$$
所以整个指数至少为 $-7/8\ge-1$，从而
$$
I_k^+\ge\int_0^{\sqrt Q/4}e^{-1}dt
=\frac{\sqrt Q}{4e}.
$$
结合 (6.1)—(6.2)，
$$
\|F_Q\chi\|^2
\ge\frac34\frac{Q}{16e^2},
$$
即 (1.4)。这里的增长来自正号积分的真实中心窗口；不把负号积分的估计移用于正号情形。

## 7. 有界增生因子的直接推论

对 $\lambda>0$，令
$$
R_Q=I+\lambda F_Q.
$$
$F_Q$ 的谱为 $\{1\}$，故 $R_Q$ 可逆。由增生性，
$$
\|R_Qx\|^2
=\|x\|^2+2\lambda\operatorname{Re}\langle F_Qx,x\rangle
+\lambda^2\|F_Qx\|^2
\ge\|x\|^2+\lambda^2\|F_Qx\|^2.
\tag{7.1}
$$
因此 $R_Q$ 扩张且 $\|R_Q^{-1}\|\le1$。特别
$$
\|R_Q\Omega-\Omega\|\le10\lambda/\sqrt{Q+1},
$$
$$
0\le\mu_Q:=\langle R_Q\Omega-\Omega,\Omega\rangle
\le4\lambda/(Q+1),
$$
以及
$$
\|R_Q\chi\|\ge c_0\lambda\sqrt Q.
\tag{7.2}
$$
均值零部分满足
$$
\|R_Q\Omega-(1+\mu_Q)\Omega\|^2
\le100\lambda^2/(Q+1).
\tag{7.3}
$$
此外 $\|R_Q\|\le1+\lambda(2Q+1)$，便于有限柱逼近预算。

## 8. 实际远物理块的微增分母和完整 carry 预算

现将纯块移到原 Haar 模型的连续物理位
$$
J=\{r,\ldots,r+Q-1\}.
$$
令
$$
S^0=\sum_{j\in J}E_j,\qquad
S^{\rm act}=\sum_{j\in J}N_j,
\qquad
0<\eta_j\le e^{-770\,16^j}.
$$
取一个已知上界 $\varepsilon\ge\max_{j\in J}\eta_j$，例如
$\varepsilon=e^{-770\,16^r}$。真实局部递推给
$$
\|S^{\rm act}-S^0\|\le Q\varepsilon.
$$
定义
$$
d=Q+1+2Q\varepsilon,\qquad
K^{\rm act}=\frac{2S^{\rm act}}d,\qquad
K^0=\frac{2S^0}{Q+1}.
\tag{8.1}
$$
由 (2.1)，
$$
\|K^{\rm act}\|\le1,\qquad
\|K^{\rm act}-K^0\|
\le\frac{4Q\varepsilon}{d}\le4\varepsilon.
\tag{8.2}
$$
所有 $N_j$ 都是真实归一化幂，所以 $K^{\rm act}\in\mathcal A$ 且谱为 $\{0\}$；$I+K^{\rm act}$ 可逆。这里没有把尾上真实算子截断成幂零算子。

若
$$
4\varepsilon(Q+1)\le1/2,
\tag{8.3}
$$
用 (1.5) 及预解恒等式得到
$$
\|(I+K^{\rm act})^{-1}\|\le2(Q+1).
$$
令
$$
F^{\rm act}=2(I+K^{\rm act})^{-1}-I,\qquad
F^0=2(I+K^0)^{-1}-I.
$$
则
$$
\boxed{
\|F^{\rm act}-F^0\|
\le16(Q+1)^2\varepsilon=:\Delta.
}
\tag{8.4}
$$
$F^{\rm act}$ 仍增生，因为 $K^{\rm act}$ 是收缩。它的系数及实际权为实，因此 $\langle F^{\rm act}1,1\rangle$ 为实数。

对原全空间常数 $1$ 及块 Walsh 积 $\chi_J$，(1.2)—(1.4) 与 (8.4) 给
$$
\|F^{\rm act}1\|\le10/\sqrt{Q+1}+\Delta,
$$
$$
0\le\langle F^{\rm act}1,1\rangle\le4/(Q+1)+\Delta,
$$
$$
\|F^{\rm act}\chi_J\|\ge c_0\sqrt Q-\Delta.
\tag{8.5}
$$
例如取
$$
\varepsilon\le\frac{c_0}{32(Q+1)^3},
$$
便同时保证 (8.3)，并得到安全常数
$$
\|F^{\rm act}1\|\le11/\sqrt{Q+1},\qquad
0\le\langle F^{\rm act}1,1\rangle\le5/(Q+1),
\qquad
\|F^{\rm act}\chi_J\|\ge(c_0/2)\sqrt Q.
\tag{8.6}
$$

最后对 $R^{\rm act}=I+\lambda F^{\rm act}$、$R^0=I+\lambda F^0$，
$$
\boxed{
\|R^{\rm act}-R^0\|\le16\lambda(Q+1)^2\varepsilon.
}
\tag{8.7}
$$
$R^{\rm act}$ 可逆、扩张且其逆为实际 $\mathcal A$ 中的收缩。通过将块起点 $r$ 取得足够远，(8.7) 可满足任意事先给定的正误差预算；不需要改变原权。这个选择可同时把新块置于任何已经给定的有限柱之后。

## 9. 范围

本稿准确支付了三个有限块尺度及将其送回真实模型所需的全部算子范数成本。由这些局部估计构造无穷乘积，还须另证有限柱自适应选择、向量乘积的收敛、收缩逆积的强收敛、非零性及任何增长下界。本文未把这些全局结论当成有限块估计的自动推论。
