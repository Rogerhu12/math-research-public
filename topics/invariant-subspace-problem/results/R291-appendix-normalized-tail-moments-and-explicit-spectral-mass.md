# R291 附录：固定次数归一化矩阵与实际尾谱质量

2026-11-14，normal-annihilator / 789f。**状态：以下固定次数界及一位谱质量公式已证明。一般有限秩正常湮灭者仍未排除。**

本稿继续 [R291](R291-normal-moment-module-independence-and-exponential-support-rank-growth.md)及[固定头距离证书](R291-appendix-fixed-head-finite-moment-distance-and-spectral-mass.md)。新增步骤是把后者依赖原态高次矩的可逆矩阵，改成明确的归一化实际幂与有限 Cayley 右测试矩阵。固定次数下，它在同一正常尾链上有统一最小奇异值下界；全部真实 carry 与换基逆费用仍保留。

## 1. 原归一化二进制幂与实际右测试

在真实尾 $H_m$ 上记原归一化算子为 $N_m,N_{m+1},\ldots$，省略尾限制的帽号。使用原递推

$$
N_i^2=\eta_iN_{i+1},\qquad
\|N_i\|=1,\qquad
N_i=E_i+\eta_iE_i^*N_{i+1},
\tag{1.1}
$$

$$
0<\eta_i\le e^{-770\,16^i},\qquad
\gamma_m:=e^{-770\,16^m}.
\tag{1.2}
$$

故对每个 $i\ge m$ 有 $\eta_i\le\gamma_m$；不要求实际序列 $\eta_i$ 单调。

对整数 $r\ge0$，记其非零二进制位集合为 $B(r)$。原递推给准确身份

$$
\frac{N_m^r}{\|N_m^r\|}
=\prod_{\ell\in B(r)}N_{m+\ell}.
\tag{1.3}
$$

特别，右端的范数恰为一。上界来自各因子范数一；下界可在 $B(r)$ 中各物理位取 $e_0$、其余位任取单位向量，再按指标递减顺序作用。每一步都沿原 $N_i$ 的左下单位块把本位 $e_0$ 送到 $e_1$，不触进位，故乘积保持这个单位向量的范数。

更明确地，对所有整数 $n\ge1$，

$$
\boxed{
\|N_j^n\|=
\prod_{s\ge0}\eta_{j+s}^{\lfloor n/2^{s+1}\rfloor}.
}
\tag{1.4}
$$

乘积只有有限个非零指数。证明是先迭代
$N_j^{2^\ell}=d_{j,\ell}N_{j+\ell}$，其中
$d_{j,\ell}=\prod_{s<\ell}\eta_{j+s}^{2^{\ell-1-s}}$，再按 $n$ 的二进制位相乘，并用 (1.3) 的范数等于一。第 $s$ 个 $\eta$ 的总指数正是 $\lfloor n/2^{s+1}\rfloor$。

记同一个真实尾范数代数

$$
\mathcal B_m=\overline{\mathbb C[I,N_m]}^{\|\cdot\|}.
$$

对每个 $i\ge m$，$N_i$ 是 $N_m$ 的一个正标量归一化幂，故属于 $\mathcal B_m$。拟幂零性保证 $(I+N_i)^{-1}\in\mathcal B_m$，所以

$$
W_i=(I-N_i)(I+N_i)^{-1}\in\mathcal B_m.
\tag{1.5}
$$

这些是原有界右源，不是以纯 $E_i$ 代替后的外来乘子。原局部界可取

$$
\|W_i\|\le3,\qquad
\|W_i-(I-2E_i)\|\le18\eta_i.
\tag{1.6}
$$

例如 $(I+N_i)^{-1}=(I-N_i)(I-N_i^2)^{-1}$ 的范数小于 $3$，$(I+E_i)^{-1}=I-E_i$ 的范数小于 $2$；预解式身份实际已给误差小于 $12\eta_i$。又 $\|I-2E_i\|=1+\sqrt2$，结合 (1.2) 得 $\|W_i\|<3$。使用较宽的 $18$ 与已有原局部界一致。

## 2. 固定次数的有限真实矩阵

固定 $D\ge1$，令

$$
K=D+1,\qquad L=\lceil\log_2(D+1)\rceil.
$$

对 $0\le r,i\le D$，定义

$$
Z_{m,r}=\prod_{\ell\in B(r)}N_{m+\ell}
=\frac{N_m^r}{\|N_m^r\|},
$$

$$
F_{m,i}=3^{-|B(i)|}\prod_{\ell\in B(i)}W_{m+\ell}\in\mathcal B_m,
\qquad\|F_{m,i}\|\le1.
\tag{2.1}
$$

空乘积均为 $I$。取任意迹为一的正常正尾态 $\nu$，并记

$$
\delta=1-\langle\nu\Omega_m,\Omega_m\rangle,
\qquad
H^{(m,\nu)}_{ir}=\operatorname{Tr}(\nu Z_{m,r}F_{m,i}).
\tag{2.2}
$$

在纯局部比较对象中，用 $E_{m+\ell}$ 代替 $N_{m+\ell}$、$D_{m+\ell}=I-2E_{m+\ell}$ 代替 $W_{m+\ell}$，并取真空态。相应矩阵准确为

$$
H^0_{ir}=3^{-|B(i)|}2^{-|B(r)|}
1_{\{B(i)\subseteq B(r)\}}.
\tag{2.3}
$$

逐位验证只用
$\omega(I)=1$、$\omega(E)=1/2$、$\omega(I-2E)=0$、$E(I-2E)=E$。因此完整 $2^L\times2^L$ 矩阵是

$$
B^{\otimes L},\qquad
B=\begin{pmatrix}1&1/2\\0&1/6\end{pmatrix}.
\tag{2.4}
$$

按二进制整数的自然次序排列，$B(i)\subseteq B(r)$ 蕴含 $i\le r$，所以完整矩阵是上三角矩阵。(2.3) 正是它的前 $K$ 行列首主块，允许 $D+1$ 不是二次幂。

因为

$$
B^{-1}=\begin{pmatrix}1&-3\\0&6\end{pmatrix},
\qquad \|B^{-1}\|\le\|B^{-1}\|_{\mathrm{HS}}=\sqrt{46}<7,
$$

完整逆的范数小于 $7^L$。上三角分块矩阵的首主块逆正是完整逆的相应首主块，故

$$
\boxed{\|(H^0)^{-1}\|\le7^L,
\qquad\sigma_{\min}(H^0)\ge7^{-L}.}
\tag{2.5}
$$

这一步明确控制非二次幂大小的块，没有把它当作另一个完整 Kronecker 矩阵。

## 3. 全部 carry 误差与统一正常阈值

令 $Z^0_{m,r}$、$F^0_{m,i}$ 表示上述纯比较积。由有限积逐项相减、(1.1)、(1.6)，

$$
\|Z_{m,r}-Z^0_{m,r}\|\le |B(r)|\gamma_m,
$$

$$
\|F_{m,i}-F^0_{m,i}\|
\le 3^{-|B(i)|}|B(i)|18\gamma_m3^{|B(i)|-1}
\le6|B(i)|\gamma_m.
\tag{3.1}
$$

两个归一化右积的范数都不超过一，因此

$$
\|Z_{m,r}F_{m,i}-Z^0_{m,r}F^0_{m,i}\|
\le (|B(r)|+6|B(i)|)\gamma_m\le7L\gamma_m.
\tag{3.2}
$$

正态的真空 fidelity 给

$$
\|\nu-|\Omega_m\rangle\langle\Omega_m|\|_1\le2\sqrt\delta.
\tag{3.3}
$$

这可以直接由正态的谱分解、纯态迹距离公式及 Cauchy–Schwarz 得到。对每个实际 $\|Z_{m,r}F_{m,i}\|\le1$ 的输出应用 (3.3)，再用 (3.2)，得到

$$
|H^{(m,\nu)}_{ir}-H^0_{ir}|
\le2\sqrt\delta+7L\gamma_m,
$$

$$
\boxed{
\|H^{(m,\nu)}-H^0\|
\le K(2\sqrt\delta+7L\gamma_m).
}
\tag{3.4}
$$

所以只要

$$
\boxed{
\delta\le(8K7^L)^{-2},\qquad
\gamma_m\le(28KL7^L)^{-1},
}
\tag{3.5}
$$

就有

$$
\boxed{\sigma_{\min}(H^{(m,\nu)})\ge\frac1{2\,7^L}.}
\tag{3.6}
$$

常数只在固定 $D$ 下统一。对于 R253 的同一正常尾链 $\nu_m$，$\delta_m\to0$ 且 $\gamma_m\to0$，故每个固定 $D$ 存在一个阈值之后 (3.5) 一直成立。阈值依赖原态的正常尾收敛；没有宣称可任取增长的 $D=D(m)$。

重要的是，(3.3) 作用于真实且一致有界的输出。因此这里允许 $m$ 及来源随尾移动，不用将 WOT 收敛错误地作用于无控制的移动向量。

## 4. 代入 R291 固定头证书：全部损失写成真实 carry 与 U 的逆

取同一原正常正湮灭链，在当前真实尾 $H_j$ 上记

$$
\rho=\nu_j,\qquad T=N_j,\qquad q=2^M,\ M\ge1,
$$

$$
T^q=I_q\otimes z,
\qquad R=\overline{\mathbb C[I,z]}^{\|\cdot\|}=\mathcal B_{j+M}.
\tag{4.1}
$$

选一个当前实际首阶一符号 $S_j$，使同一 $\nu_j$ 满足

$$
\operatorname{Tr}(\nu_j S_jG)=0\qquad(G\in\mathcal B_j).
\tag{4.2}
$$

例如可用 R253 的 $Q_j$ 或一个明确已除去真实单位的同理想符号。令 $U_{j,M}$ 为 $1,S_j,\ldots,S_j^{q-1}$ 相对于 $1,N_j,\ldots,N_j^{q-1}$ 的真实余数换基矩阵。仍保留其实际 $\|U_{j,M}^{-1}\|$。

固定 $1\le k<q$，置

$$
D=qk+q-1,\qquad K=D+1,\qquad L=\lceil\log_2(D+1)\rceil.
\tag{4.3}
$$

此处远尾边缘正是同一链的 $\nu_{j+M}$。$z$ 是 $N_{j+M}$ 的正标量倍数，所以

$$
\frac{z^r}{\|z^r\|}=Z_{j+M,r}.
$$

使用第 2 节的实际 $F_{j+M,i}\in R$。未归一化列的矩阵

$$
\widetilde H_{ir}=\operatorname{Tr}(\nu_{j+M}z^rF_{j+M,i})
$$

等于 $H^{(j+M,\nu_{j+M})}\operatorname{diag}(\|z^r\|)_{r=0}^{D}$。因 $\|z\|\le1$，这些幂范数不增。因此，只要 (3.5) 对 $m=j+M$、$\delta=\delta_{j+M}$ 成立，

$$
\boxed{
\sigma_{\min}(\widetilde H)
\ge\frac{\|z^D\|}{2\,7^L}
=\frac{\|N_j^{qD}\|}{2\,7^L}.
}
\tag{4.4}
$$

R291 固定头距离证书对任意原 $F_i\in R$、$\|F_i\|\le1$ 的可逆有限矩阵适用，不要求这些测试本身是普通幂。其多项式度数界、Mahler 系数下界、真实伴随矩阵恒等式均保持。

由于 $\|T\|=1$，而对应 companion 矩阵满足 $\|C_q\|=\max(1,\|z\|)=1$，该证书的两个有限幂和常数都不超过 $\sqrt{D+1}$。于是每个算子 Schmidt 秩至多 $k$ 的比较迹类 $\sigma$ 都满足

$$
\boxed{
\|\nu_j-\sigma\|_1\ge\widehat\Gamma_{j,M,k}:=
\frac{\|N_j^{qD}\|\binom{2D}{D}^{-q/2}}
{2\,7^L\,q!\,(D+1)^{(q+1)/2}\|U_{j,M}^{-1}\|}>0.
}
\tag{4.5}
$$

所有实际 carry 现由 (1.4) 明确列出：

$$
\|N_j^{qD}\|
=\prod_{s\ge0}\eta_{j+s}^{\lfloor qD/2^{s+1}\rfloor}.
\tag{4.6}
$$

取 $k=d^2<q$，将 $\nu_j$ 压到其远尾边缘 $\nu_{j+M}$ 的前 $d$ 个特征向量，再用正压缩的 $2\sqrt\epsilon$ 迹范数界，得到

$$
\boxed{
\sum_{r>d}\lambda_r(\nu_{j+M})
\ge\frac14\widehat\Gamma_{j,M,d^2}^{\,2}.
}
\tag{4.7}
$$

同一个界也适用于当前连续头块的边缘谱尾。对每个固定 $M,d$，(4.7) 在所有充分深 $j$ 成立；阈值已完全分成 (3.5) 的正常尾条件和原模型条件。

这比仅保留一个待寻找的原态矩最小奇异值更具体：有限原来源和固定次数的稳定矩阵已全部给出。剩余损失是 (4.6) 的真实进位乘积与实际 $\|U_{j,M}^{-1}\|$，两者均未被换成形式系数的符号。

## 5. 一位非纯谱质量：准确的 η 指数

取 $M=1$、$q=2$、$k=d=1$。则

$$
D=3,\quad K=4,\quad L=2,\quad\binom{2D}{D}=20,
$$

$$
\|N_j^{qD}\|=\|N_j^6\|=\eta_j^3\eta_{j+1}.
\tag{5.1}
$$

把原一位符号准确写为 $C_j+N_jD_j$，其中 $D_j$ 是真实尾单位；在右测试中除掉它后，可用同一理想的

$$
\widetilde S_j=N_j+Z_j,\qquad Z_j=D_j^{-1}C_j\in\mathcal B_{j+1}.
$$

其真实换基矩阵与逆为

$$
U_{j,1}=\begin{pmatrix}I&0\\Z_j&I\end{pmatrix},
\qquad
U_{j,1}^{-1}=\begin{pmatrix}I&0\\-Z_j&I\end{pmatrix},
\qquad
\|U_{j,1}^{-1}\|\le1+\|Z_j\|.
\tag{5.2}
$$

这里只在每个固定层使用真实有界的 $D_j^{-1}$；其费用全部留在 $Z_j$ 中。若采用旧真实递推的规范化 $S_j$，这正是该递推的真实商，不能改成初始慢行的简单尾比。

条件 (3.5) 此时可以写成

$$
\delta_{j+1}\le1568^{-2},\qquad
\gamma_{j+1}\le10976^{-1}.
\tag{5.3}
$$

第二条由原 (1.2) 对所有 $j\ge0$ 自动满足；第一条在同一正常链上最终满足。由 (4.5)、(5.1)、(5.2)，

$$
\|\nu_j-\sigma\|_1\ge
\frac{\eta_j^3\eta_{j+1}}
{31360(1+\|Z_j\|)}
\quad\text{对每个算子 Schmidt 秩至多一的 }\sigma.
\tag{5.4}
$$

于是实际下一个尾边缘的非纯谱质量满足

$$
\boxed{
1-\lambda_{\max}(\nu_{j+1})
\ge
\left[\frac{\eta_j^3\eta_{j+1}}
{62720(1+\|Z_j\|)}\right]^2>0.
}
\tag{5.5}
$$

这是关于最大特征值之外的真实谱质量，不只是关于它在指定真空方向之外的质量。其精确指数来自 $N_j^6$ 的真实进位，而不是有限截断的猜测。

## 6. 与现有正常尾必要界的关系

(4.7)、(5.5) 均使用真实湮灭方程，同时保留同一个正常态的相容边缘；它们不是任意正常态的谱结论。

另一方面，(5.5) 的分子已经含极小的 $\eta_j^6\eta_{j+1}^2$。对原正 $S_N$，旧[真实递推商增长](R236-appendix-positive-slow-row-true-recursive-quotient-growth.md)（该稿将此商记为 $G_j$）还给 $\|Z_j\|\ge\exp[(55-o(1))16^j]$，使这一指定证书的可用下界进一步变小。这不否定别的优化来源，但不能把本式读成多项式大小的谱质量。

由于 $1-\lambda_{\max}(\nu_{j+1})\le\delta_{j+1}$，本稿也不给比已有多项式柱尾更强的 $\delta$ 速率；它新增控制的是谱非纯质量而非指定方向泄漏。没有由这个极小的质量下界推出熵正密度，也没有与 R289 的 $o(m)$ 熵上界形成矛盾。

下一实质问题仍是能否在保留真实符号和同一链的前提下，利用完整尾理想修正或正完成方程去掉 (4.6) 与 $\|U^{-1}\|$ 中足够多的损失。固定次数矩阵这一部分现已付清，不再需要把未知正常高幂阈值隐藏在矩搜索里。
