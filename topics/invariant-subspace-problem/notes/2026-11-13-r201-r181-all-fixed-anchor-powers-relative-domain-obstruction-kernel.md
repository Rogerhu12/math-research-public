# R201/R181 范围补记：任意固定空谱锚幂仍不能正则化横向 first

日期：2026-11-13（UTC）。kernel_resume_1cf；Astra-ISP-1cf8c51d 已独立回读 R181 §§2–3 的任意乘积态统一真实高幂估计，并核域不包含及全部有界交换扰动。
性质：两篇已证稿的直接推论，不登记新定理编号。
用途：排除把实系数支配误用为剪切多项式的全域降次。

## 1. 原有真实输入

取 [R201](../results/R201-positive-first-ratio-domain-obstruction-and-full-plane-spectrum.md) §1
的两两不交正非 $\ell^1$ 行 $b^{(i)}$。
令
$$
T=X_{\sum_i c_i b^{(i)}},\qquad
S=X_{\sum_i d_i b^{(i)}},
$$
其中 $c_i\ge0$、$c\ne0$，且 $d\notin\mathbb Cc$。
$T$ 空谱，$L=T^{-1}\in A'$ 有界且拟幂零。

R201 §§2–3 取实向量 $t$ 满足
$c\cdot t=0$、$d\cdot t\ne0$，
构造单位有限柱乘积向量 $x_R$。
每条正行的纯局部中心为 $1+iRt_i$，
全部实际 carry 误差由固定常数控制。
因此
$$
\|Sx_R\|\longrightarrow\infty.
\tag{1.1}
$$
对于总锚 $T$，同一乘积态的纯局部中心准确是
$$
\beta=\sum_i c_i+iR\sum_i c_it_i=\sum_i c_i,
\tag{1.2}
$$
与 $R$ 无关。

[R181](../results/R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md)
§§2–3，特别 (3.6)，适用于任意有限乘积参考态；
常数不依赖改变的位数、所选总质量或中心。
在尾起点 $m=0$ 使用它，得每个固定 $j\ge0$：
$$
x_R\in\operatorname{Dom}T^j,\qquad
\|(T-\beta I)^j x_R\|
\le C_j\Bigl\|\sum_i c_i b^{(i)}\Bigr\|_2^j.
\tag{1.3}
$$
这是全部真实自然幂估计，不是从一次近特征关系形式升幂。

## 2. 任意固定自然幂的域障碍

固定整数 $N\ge1$。
从 (1.2)–(1.3) 及有限二项式，
$$
\sup_R\|T^j x_R\|<\infty\qquad(0\le j\le N).
\tag{2.1}
$$
令
$$
y_R=T^Nx_R.
$$
于是 $y_R$ 有界，$L^Ny_R=x_R$，并且
$$
SL^Ny_R=Sx_R
$$
范数发散。因此真正自然乘积
$$
Z_N=SL^N,\qquad
\operatorname{Dom}Z_N=\{y:L^Ny\in\operatorname{Dom}S\}
$$
无界。

$Z_N$ 闭：$L^N$ 有界，直接使用 $S$ 的闭性。
它的域稠密：有限柱是 $T^N$ 的真实图核心，
$T^N$ 满射且逆为 $L^N$，
所以 $T^N$ 的有限柱像在 $H$ 稠密；
这些像全部在 $\operatorname{Dom}Z_N$ 中。
闭图定理遂给
$$
\boxed{
SL^N\text{ 闭、稠密定义、无界且非全域},\qquad
\operatorname{Dom}T^N\not\subseteq\operatorname{Dom}S.
}
\tag{2.2}
$$

## 3. 有界交换扰动及一般固定多项式分母

取任意 $H_1,H_2\in A'$，令
$$
\widetilde T=T+H_1,\qquad \widetilde S=S+H_2.
$$
R201 §3.3 已证 $\widetilde T$ 仍空谱。
有界交换子的真实域交换给
$$
\widetilde T^j x_R
=\sum_{\ell=0}^j\binom j\ell H_1^{j-\ell}T^\ell x_R.
$$
由 (2.1)，每个固定 $j$ 的范数仍统一有界；
而 $\|\widetilde Sx_R\|\to\infty$。
完全相同的论证给
$$
\boxed{
\widetilde S\,\widetilde T^{-N}\text{ 闭、稠定、无界、非全域}
}
\tag{3.1}
$$
及相应的全部固定幂域不包含。
这包括任意复 $\ell^2$ 指数倾斜。

更一般，若
$$
P(\widetilde T)=\sum_{j=0}^N E_j\widetilde T^j,
\qquad E_j\in A',\quad E_N\in(A')^\times,
$$
则旧空谱锚定理给真实闭的最高单位多项式及有界全域逆。
(2.1) 仍给
$\sup_R\|P(\widetilde T)x_R\|<\infty$。
于是
$$
\widetilde S\,P(\widetilde T)^{-1}
$$
无界，且由闭图定理不是全域。
其自然域稠密仍由有限柱图核心及满射得到。
此处保留自然算子多项式；适用于旧 Bell 闭实现时，
须使用该实现已经支付的最高单位系数和真实域。

## 4. 当前交替例

若
$$
u=\sum_j a_j\chi_j,\quad a_j>0,\qquad
v=\sum_j(-1)^j a_j\chi_j,
$$
且偶、奇两侧系数和都发散，
把两侧分别作为不交正行即可。
此时 $|c_j|=a_j$，仍有对每个固定 $N$：
$$
\boxed{
\operatorname{Dom}X_u^N\not\subseteq\operatorname{Dom}X_v,
\qquad X_vX_u^{-N}\text{ 非全域无界}.}
$$
特别规则幂 $\frac12<\sigma\le1$ 的当前实例完全满足输入。

所以不能凭系数逐项支配，
把 $Y X^{-1}$ 或更高固定 $Y X^{-N}$ 当作有界算子，
再声称实切向剪切的多项式由 $L$ 降次成为单位。
这与 R150 已证的循环性没有冲突：
其证明使用实际有限消元和共同深域，
没有提出这里被排除的全空间相对域包含。
