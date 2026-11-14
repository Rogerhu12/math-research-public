# R268：真实累积量熵预算、弱 $\ell^1$ 带宽与全部重数循环性

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明；原 Haar 模型的中间结论，普通 Hilbert ISP 未完成。

本文给出一个单尺度的排序熵准则，并据此关闭弱 $\ell^1$ 上界加子序列指数下界的全部加权多项式。它不要求全局指数上界，也不要求同幅桶；包含非 $\ell^1$ 的全部对数修正调和幅度。另给一个严格超指数阶梯行的完整新例。规范、临界弱 $\ell^1$、固定 $\sigma>1$ 幂尾及双侧指数的旧范围只作为被包含的特例，不重复计数。

## 1. 三个主结论

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2(\mathbb C),
\quad a_*\in\mathbb C.
$$
令 $\rho_k$ 为非零幅度的非增重排，假设有无穷多个非零系数。
相位与原物理排列任意。固定任意
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2(\mathbb C).
$$

### 1.1 单尺度熵准则

假设存在趋于无穷的整数子序列 $N$ 和固定常数 $D,C_E,C_L$，使
$$
\boxed{
\sup_{k\ge N}k\rho_k\le D N\rho_N,
}
\tag{1.1}
$$
$$
\boxed{
E_N:=\sum_{k=1}^N\log(\rho_k/\rho_N)\le C_E N^2,
\qquad
L_N:=1+\log^+(\rho_N^{-1})\le C_LN^{3/2}.
}
\tag{1.2}
$$

**定理 A。** 对每个非零标量多项式 $q$，根有任意有限重数时仍有
$$
\boxed{q(u)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.3}
$$

### 1.2 弱 $\ell^1$ 上界和仅子序列指数下界

**定理 B。** 若
$$
\boxed{
B:=\sup_{k\ge1}k\rho_k<\infty,\qquad
\liminf_{k\to\infty}\frac{\log^+(\rho_k^{-1})}{k}<\infty,
}
\tag{1.4}
$$
则 (1.3) 成立。

第二条件只要求沿无穷子序列有 $\rho_k\ge c e^{-\beta k}$。
没有要求任何指数型上界、两侧同型、$k\rho_k$ 单调或物理系数和收敛。
特别，任意 $\beta>0$ 的
$$
\rho_k\asymp\frac1{k(\log(e+k))^\beta}
$$
都包括在内；$0<\beta\le1$ 时允许原 first 真正无界。

### 1.3 一个不满足子序列指数下界的超指数例

令 $N_k=2^{4^k}$，在
$N_{k-1}<n\le N_k$ 上取
$$
\rho_n=e^{-N_k^{3/2}},
\tag{1.5}
$$
有限个初项任取正数并保持非增。
这个行满足
$$
\frac{\log(\rho_n^{-1})}{n}\longrightarrow\infty,
$$
但仍满足定理 A，故全部加权多项式含任意重根循环。
该例不同于规则 $e^{-\beta n^\alpha}$；
本文不由此关闭规则 $1<\alpha\le3/2$ 的全部重数。

以下给出完整实际预算和域证明。

## 2. 真实自然域与固定 Bell 算子

沿用 R176 的实际闭 first
$$
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j),\qquad V(z)=(I-z)(I+z)^{-1},
$$
$$
X=X_b=a_*I+\sum_ja_jR_j.
\tag{2.1}
$$
在非 $\ell^1$ 情形，(2.1) 按原有限柱核心及闭算子的意义定义，
不是声称算子范数级数收敛。
其域为原 first 的真实自然域。

固定 $n\ge2$，令
$$
L_n(v)=\left.\frac{d^n}{ds^n}
\log(\cosh s+v\sinh s)\right|_{s=0},
\qquad
G_n=\sum_ja_j^nL_n(R_j)\in\mathcal A.
\tag{2.2}
$$
$L_n$ 为固定多项式且 $L_n(1)=0$；
$a^n\in\ell^1$，故 (2.2) 真正按范数收敛。
全部 $\mathcal A$ 元素保持 $X$ 的每阶自然域并完整交换。

非零常数、一次 $q$ 已由原指数及 first 循环性处理。
设 $q$ 首一、次数 $p\ge2$，置
$$
\mathcal P(z;\kappa)
=\exp\!\left(\sum_{n=2}^p
\frac{\kappa_n}{n!}\partial_z^n\right)q(z),
\qquad T=\mathcal P(X;G).
\tag{2.3}
$$
R176 给出
$$
\operatorname{Dom}T=\operatorname{Dom}X^p,\qquad
T=C_0T^*C_0
$$
以及闭性、准确图核心和
$Te^w=q(u)e^w$。
若 $M=\ker T$，则
$$
\boxed{
M\subseteq\mathcal D_\infty:=
\bigcap_{k\ge0}\operatorname{Dom}X^k,\qquad
X_M=X|_M\in B(M).
}
\tag{2.4}
$$
$X$ 与全部 $\mathcal A$ 系数保持同一个 $M$。
以下反证 $M\ne0$，记 $B_M=\|X_M\|$。

## 3. 任意 $\ell^2$ 行的实际正锥熵半群界

本节不使用 (1.1)--(1.2)。

**引理。** 对每个固定 $n\ge2$，存在 $K_n,C_n,d_n>0$ 使
$$
\boxed{
\|e^{zG_n}\|
\le K_n
\exp[C_n(1+\log(2+|z|))^{4/3}]
\prod_{k\ge1}(1+d_n|z|\rho_k^n).
}
\tag{3.1}
$$
标量乘积收敛。全部实际 carry 均保留，排序只用于这个非负标量乘积。

证明如下。原模型有
$$
\|N_j\|=1,\qquad
N_j^2=\eta_jN_{j+1},\quad
0<\eta_j\le e^{-770\,16^j},
$$
$$
N_j=A^{2^j}/d_j,\quad d_j=e^{-\Lambda_j},\quad
\Lambda_j\le125\,16^j,
$$
$$
\|A^k\|\le
\exp[-(100/15)k^4+105k^3]\le K_Ae^{-c_Ak^4}.
\tag{3.2}
$$

令 $L=\max(1,\sup_j|t_j|)$，写
$$
L_n(1+x)=\sum_{\ell=1}^n c_{n,\ell}x^\ell,\qquad
W_n(z)=\sum_{\ell=1}^n|c_{n,\ell}|
\left(\frac{2Lz}{1-Lz}\right)^\ell.
$$
原 $A$ 是函数非负锥上的正算子，$W_n$ 的 Taylor 系数非负。
实际绝对级数给
$$
|L_n(R_j)f|\le W_n(N_j)|f|.
$$
这里的正性是逐点函数锥，绝非 Hilbert 自伴正性。

$W_n(z)=zW_{n,1}(z)=w_{n,1}z+z^2W_{n,2}(z)$。
实际平方关系给大 $j$ 的 $(I-LN_j)^{-1}$ 一致有界，
有限低位用各自准幂零预解式支付，所以
$\sup_j\|W_{n,i}(N_j)\|<\infty$。
因此
$$
M_n=\sum_j|a_j|^nW_n(N_j)
$$
按范数收敛，且
$$
|G_n^kf|\le M_n^k|f|,\qquad
|e^{zG_n}f|\le e^{|z|M_n}|f|.
\tag{3.3}
$$

偶奇幂分开和 $N_j^2=\eta_jN_{j+1}$ 给
$$
\|e^{\zeta N_j}\|
\le(1+|\zeta|)e^{|\zeta|\sqrt{\eta_j}},
$$
故
$$
\|e^{zvW_n(N_j)}\|
\le(1+d_n|z|v)\exp(C_n'|z|v\sqrt{\eta_j})
\quad(v\ge0).
\tag{3.4}
$$

设 $t=|z|$，取最小物理头 $h\ge1$ 使
$385\,16^h\ge2\log(2+t)$。
真实尾在 (3.4) 的额外 carry 因子有
$$
t\sum_{j\ge h}|a_j|^n\sqrt{\eta_j}
\le2t(\sup_j|a_j|)^n e^{-385\,16^h}\le C_n.
$$
尾的标量乘积可上界为全部排序乘积。

有限物理头则是
$$
M_{n,<h}=A U_{n,h},\qquad
U_{n,h}=\sum_{j<h}
|a_j|^n d_j^{-1}A^{2^j-1}W_{n,1}(N_j)\in\mathcal A,
$$
$$
\|U_{n,h}\|\le C_n
\left(\sum_j|a_j|^n\right)e^{125\,16^{h-1}}.
$$
最小性给
$16^{h-1}\le1+(2/385)\log(2+t)$。
于是
$\log(2+t\|U_{n,h}\|)\le C+2\log(2+t)$。
(3.2) 和实际交换性给
$$
\|e^{zAU_{n,h}}\|
\le K_A\sum_{k\ge0}
e^{-c_Ak^4}\frac{(t\|U_{n,h}\|)^k}{k!}
\le K\exp[C(1+\log(2+t))^{4/3}].
$$
头尾在同一个交换代数内，结合 (3.3)--(3.4) 即证 (3.1)。

因为 $\sum_k\rho_k^n<\infty$，
$$
t^{-1}\sum_k\log(1+d_nt\rho_k^n)\longrightarrow0
$$
由逐项收敛和 $d_n\rho_k^n$ 控制成立。
故 (3.1) 的对数为 $o(t)$；这个事实将在下一节保证所有复方向的实际 Laplace 积分收敛。

## 4. 单尺度联合预解：前段熵只付一次

取满足 (1.1) 的尺度 $N$，记
$$
\delta=\rho_N\le1,\qquad
E=E_N,\qquad L_0=1+\log(\delta^{-1}).
$$
固定 $\varepsilon>0$。
对每个 $2\le n\le p$ 及
$|\lambda|=\varepsilon\delta^n$，实际 Bochner 积分
$$
J_\lambda=\int_0^\infty e^{-s}e^{sG_n/\lambda}\,ds
$$
收敛，由 §3 的 $o(t)$ 界可知边界项趋零。
对有限区间求导再取极限给
$$
J_\lambda=\lambda(\lambda-G_n)^{-1}.
\tag{4.1}
$$
左右逆都由同一积分得到，且所有复方向一致。

将 (3.1) 代入 (4.1)。
排序前 $N$ 项满足 $\rho_k/\delta\ge1$，故
$$
\prod_{k\le N}
\left(1+\frac{d_n s\rho_k^n}{\varepsilon\delta^n}\right)
\le e^{nE}(1+d_ns/\varepsilon)^N.
\tag{4.2}
$$
排序尾由 (1.1) 有 $\rho_k/\delta\le DN/k$，从而
$$
\begin{aligned}
\sum_{k>N}
\log\left(1+\frac{d_n s\rho_k^n}{\varepsilon\delta^n}\right)
&\le\sum_{k\ge1}\log(1+C_ns(N/k)^n)\\
&\le C_n' N s^{1/n}.
\end{aligned}
\tag{4.3}
$$
最后用递减函数积分
$\sum_{k\ge1}\log(1+A/k^n)\le
A^{1/n}\int_0^\infty\log(1+x^{-n})\,dx$；
$n\ge2$ 保证积分有限。

真实物理低头的成本另有
$$
(1+\log(2+s/|\lambda|))^{4/3}
\le C_{p,\varepsilon}
\left[L_0^{4/3}+(1+\log(2+s))^{4/3}\right].
$$
所以 (4.1) 的范数不超过固定常数乘
$$
e^{nE+C L_0^{4/3}}
\int_0^\infty
\exp\!\left[
-s+C(\log(2+s))^{4/3}
+N\log(1+C s)+C N s^{1/n}
\right]ds.
\tag{4.4}
$$
对全部 $N\ge2$，
$$
C(\log(2+s))^{4/3}\le s/8+C',
$$
$$
N\log(1+C s)\le s/8+C'N\log(N+2),
$$
$$
CNs^{1/n}\le s/4+C'N^{n/(n-1)}.
$$
这些分别来自亚线性增长、一次对数最大值和 Young 不等式。
由于 $n/(n-1)\le2$，
(4.4) 的积分不超过 $\exp(C''N^2)$。
因此
$$
\boxed{
\|\lambda(\lambda-G_n)^{-1}\|
\le K_n
\exp[C_n(E_N+L_N^{4/3}+N^2)]
}
\tag{4.5}
$$
在对应圆周上统一成立。

若 $F$ 在闭多圆盘
$|\kappa_n|\le\varepsilon\delta^n$ 的邻域全纯，
边界多圆周上 $|F|\le M_F$，
实际联合 Cauchy 演算的各圆周长度消去预解式前的半径，于是
$$
\boxed{
\|F(G_2,\ldots,G_p)\|
\le K M_F
\exp[C(E_N+L_N^{4/3}+N^2)].
}
\tag{4.6}
$$
常数不依赖 $N,F$。前段熵、真实低头和尾三个成本均已单独支付；
没有对每个选中位的逆重复这个联合成本。

## 5. 非同幅 Hermite 逆及准确输入成本

[R266 §5](R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md) 已证明下述保重数版本；列出完整使用条件。
固定首一 $q$。存在 $\varepsilon,\delta_0,a_0>0$，
使当 $0<\delta\le\delta_0$、$|F|=r$ 且
$$
\delta\le|a_j|\le a_0\quad(j\in F)
\tag{5.1}
$$
时，存在次数小于 $p$、系数在
$|\kappa_n|\le2\varepsilon\delta^n$ 内全纯的 $\mathcal R_F$，
满足
$$
\mathcal R_F\prod_{j\in F}\mathscr L_{a_j}
=1+\mathcal P\mathcal S_F,\qquad
\mathscr L_a(z;\kappa)
=-2[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)],
\tag{5.2}
$$
且系数边界界为
$$
|[z^k]\mathcal R_F|\le
C_q^{r+1}\delta^{-pr-p+1},\qquad 0\le k<p.
\tag{5.3}
$$

其来源是：各原根团保持在半径 $\delta/8$ 内；
$2a_j$ 平移与同一原根团的距离至少 $2\delta$，
不同原根团由固定根距隔开。
在 $|z-\lambda_\nu|=\delta/4$ 上，
$H_F=\prod_{j\in F}[-2\mathcal P(z-2a_j;\kappa)]$
无零，$|H_F^{-1}|\le C_q^r\delta^{-pr}$。
真正 Hermite 余式为
$$
\mathcal R_F(z;\kappa)=
\frac1{2\pi i}\sum_\nu\int_{\Gamma_\nu}
H_F(\zeta;\kappa)^{-1}
\frac{\mathcal P(\zeta;\kappa)-\mathcal P(z;\kappa)}
{(\zeta-z)\mathcal P(\zeta;\kappa)}\,d\zeta.
$$
圈长 $\delta$ 及 $|\mathcal P(\zeta)|\ge c\delta^p$ 给 (5.3)。
Cauchy 除法保留全部重数，给 (5.2)。
不需要同幅比，也不以简单根极限替代。

现在取 $\delta=\rho_N$。
对各系数一次使用 (4.6)，然后在同一 $M$ 上令
$$
\mathfrak R_F=\mathcal R_F(X_M;G|_M):M\to M.
$$
有真实恒等式
$$
\left(\prod_{j\in F}\mathscr L_{a_j}(X;G)\right)
\mathfrak R_Ff=f,\qquad f\in M,
\tag{5.4}
$$
以及
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le K(E_N+L_N^{4/3}+N^2)+K_qrL_N+K_M.
}
\tag{5.5}
$$
$K,K_q$ 不依赖选位、$r,N$ 或之后的平均参数；
$B_M$ 只通过次数小于 $p$ 的代入进入固定 $K_M$。
$\mathfrak R_F$ 是在原核上定义的实际有界算子，不是对未知商作形式除法。

## 6. 不分幅度桶的实际选位

取满足 (1.1)--(1.2) 的 $N$。
从幅度最大的 $N$ 个实际指标中，删去幅度排序最前
$\lfloor N/4\rfloor$ 项，再删去物理位置 $j<\lfloor N/4\rfloor$。
至少留下 $N/2$ 项；从中取恰有
$$
Q_N=\lfloor N/2\rfloor
$$
个指标的集合 $I_N$。
记 $m_N=\lfloor N/4\rfloor$。有
$$
\boxed{
\min I_N\ge m_N,\qquad
\rho_N\le|a_j|\le\frac{2g}{\sqrt N}
\quad(j\in I_N),\qquad g=\|a\|_2.
}
\tag{6.1}
$$
上界只用排序的 $\ell^2$ 估计。
不限制 $\max I_N$。

取一个稍后固定的小 $c>0$，令
$$
r=r_N=\left\lceil\sqrt{N/c}\right\rceil.
\tag{6.2}
$$
充分大 $N$ 时 $r\le Q_N$，而
$$
\frac N{r^2}\to c,\qquad
\frac{Q_N}{r^2}\to c/2.
\tag{6.3}
$$
对于所有 $F\subset I_N$、$|F|=r$，
$$
\sum_{j\in F}|a_j|\le\frac{2gr}{\sqrt N}\le C_c,
\qquad
\sum_{j\in F}|a_j|^n\le
C_c(2g/\sqrt N)^{n-1}\quad(n\ge2).
\tag{6.4}
$$
这里仅需第一式一致有界，完全不要求它趋零。
最大幅度趋零，所以 §5 的 $a_0$ 条件最终成立。

## 7. 全部自然词：不把闭 first 当有界

记 $\delta_XB=[X,B]$，按真实完整域定义。
[R260 的局部壳及其导子 Banach 代数](R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)给
$$
\widehat X_F=X+A_{X,F},\quad
A_{X,F}=\sum_{j\in F}a_j[V(-t_jN_j)-R_j]\in\mathcal A,
$$
$$
\widehat G_{n,F}
=G_n+\sum_{j\in F}a_j^n[L_n(V(-t_jN_j))-L_n(R_j)],
$$
$$
E_{X,F}=\gamma_F(X)-\widehat X_F,\quad
E_{n,F}=\gamma_F(G_n)-\widehat G_{n,F},\quad
\gamma_F=\operatorname{Ad}J_F,\quad
J_F=\prod_{j\in F}M_{\chi_j},
$$
及对所有整数 $s\ge0$ 的统一界
$$
\boxed{
\|\delta_X^sE_{X,F}\|
+\sum_{n=2}^p\|\delta_X^sE_{n,F}\|
\le s!\epsilon_N,\qquad
\epsilon_N\le C e^{-385\,16^{m_N-1}}.
}
\tag{7.1}
$$
这些误差及其全部导数保持 $\mathcal D_\infty$。
$J_F$ 也保持该共同深域：对它的有限实际支撑，完整闭尾交换与有限有界头扰动逐阶给出。
这里只为域使用有限支撑，不用最大物理位估计范数。

(7.1) 不含最大位的理由是原壳的精确消失：
若 $F\cap(j,\ell]=\varnothing$，第 $(j,\ell)$ 差壳为零；
同位 $j=\ell$ 的纯项已准确被符号反转吸收。
故按最高位收集后只从 $\ell\ge m_N$ 起，
壳范数 $\le C\eta_{\ell-1}$，
每阶导数由该局部壳与完整尾交换支付。
这正是 R260 已证的真实任意跨度界。

由 (6.4)，$\|A_{X,F}\|\le C_c$，全部带帽累积量范数也统一有界。
它们是 $\mathcal A$ 元素，故 $\delta_X$ 为零。

### 7.1 明确的正规排序词引理

一个词含 $k$ 个 $X$ 字母、$\ell$ 个有界字母。
有界字母要么在 $\mathcal A$ 中且范数 $\le C$，
要么是 (7.1) 的基本误差；假设至少含一个误差。
若
$$
\|X^jv\|\le H R^j\quad(0\le j\le k),\qquad R\ge1,
$$
则
$$
\|\operatorname{word}(v)\|
\le H\epsilon_N C^\ell(\ell+1)^k k!R^k.
\tag{7.2}
$$
证明：逐个用真正的 $XB=BX+\delta_XB$ 把 $X$ 移向右端。
每个带标签的 $X$ 要么留到最右端，要么消耗为某个有界字母的一次导数，
至多 $\ell+1$ 个去处。
每个非零项保留至少一个误差导数。
各导数阶数 $s_i$ 总和至多 $k$，
故 $\prod_i s_i!\le k!$；多余 $\epsilon_N$ 用 $\epsilon_N\le1$ 控制。
所有字母和导数保 $\mathcal D_\infty$，所以每一步都是实际域等式。

因此 $k\le pr$、$\ell\le C_pr$ 的有限多项式词，
总成本至多 $\epsilon_N e^{C r\log(r+2)}$ 乘输入 jet 常数；
没有最大物理位因子。

### 7.2 反射输入的全部所需 jets

对 $f_F\in M$，
$$
X^kJ_Ff_F
=J_F(X+A_{X,F}+E_{X,F})^kf_F.
$$
不含误差的部分范数 $\le(B_M+C_c)^k\|f_F\|$。
其余部分用 (7.2)，在 $0\le k\le2pr$ 上总和
$\le\epsilon_N e^{C r\log(r+2)}\|f_F\|$。
所以存在固定 $R_{M,c}$，充分大 $N$ 时全部 $F$ 统一满足
$$
\boxed{
\|X^kJ_Ff_F\|\le2R_{M,c}^k\|f_F\|,
\qquad 0\le k\le2pr.
}
\tag{7.3}
$$
没有假设 $J_FM\subset M$。
对任意固定头 $h$，
$Z_h=X-a_*I-\sum_{j<h}a_jR_j$
与 $X$ 相差固定有界交换算子；完整域二项式给同阶
$$
\|Z_h^kJ_Ff_F\|\le2R_{h,M,c}^k\|f_F\|.
\tag{7.4}
$$

## 8. 左反射、Boolean 主项和核内真实逆

置
$$
\widehat T_F=\mathcal P(\widehat X_F;\widehat G_F),\qquad
A_F=\widehat T_F-T.
$$
这些是 $\mathcal A$ 系数的 $X$ 多项式，均保持 $\mathcal D_\infty$；
$A_F$ 与 $T$ 在该域交换并保持 $M$。
把 $\gamma_FX,\gamma_FG_n$ 代入有限多项式，
$(\gamma_FT)^r-\widehat T_F^r$ 展开的每个词含至少一个基本误差，
$X$ 字母总数至多 $pr$，有界字母数 $O_p(r)$。
对 $f_F=\mathfrak R_Ff\in M$，(7.2) 给
$$
\|[(\gamma_FT)^r-\widehat T_F^r]f_F\|
\le\epsilon_N e^{C r\log(r+2)}\|f_F\|.
\tag{8.1}
$$

真实有理差的显式 $N_j^2$ 余项允许在 $M$ 上将 $A_F$ 换成
$$
\widetilde A_F=
\mathcal P\left(
X+4\sum_{j\in F}a_jt_jN_j;\
G_n+4L_n'(1)\sum_{j\in F}a_j^nt_jN_j
\right)-\mathcal P(X;G).
\tag{8.2}
$$
在同一个 $M$ 上，
$\|(A_F-\widetilde A_F)|_M\|\le C_{M,c}\eta_{m_N}$，
而两者的限制范数统一有界。
这是因为 $X_M$ 有界、(6.4) 使全部系数和有界；
不声称 $A_F$ 在全 $H$ 有界。

在交换形式变量 $x_j$ 中，(8.2) 无零次项，
一次项准确为
$$
\sum_{j\in F}t_jx_j\mathscr L_{a_j}(X;G),
$$
因为
$4L_n'(1)=-2(-2)^n$ 和
$\partial_{\kappa_n}\mathcal P=\partial_z^n\mathcal P/n!$。
$r$ 个正次因子而只有 $r$ 个变量，故
$$
\widetilde A_F^r
\equiv
r!t_FN_F\prod_{j\in F}\mathscr L_{a_j}(X;G)
\pmod{(N_j^2:j\in F)}.
\tag{8.3}
$$
每个弃项真含 $N_j^2=\eta_jN_{j+1}$。
原始系数限制到 $M$ 后的范数绝对和至多 $C_{M,c}^r$，
由 (6.4) 和固定 $X_M,G_n$ 范数直接得到。
所以全部重复位余项至多 $\eta_{m_N}C_{M,c}^r$。

采用左反射等式
$$
T^rJ_Ff_F=J_F(\gamma_FT)^rf_F.
$$
因 $Tf_F=0$ 且 $A_F$ 保持 $M$，
$\widehat T_F^rf_F=A_F^rf_F$。
先在 $M$ 内用 (5.4) 消掉完整有限差乘积，再施左侧 $J_F$，
不移动有限差算子过反射。
结合 (8.1)--(8.3) 得
$$
T^rJ_F\mathfrak R_Ff
=r!t_FJ_FN_Ff+\mathcal E_Ff,
$$
$$
\|\mathcal E_Ff\|
\le\epsilon_N e^{C r\log(r+2)}
\|\mathfrak R_F\|\|f\|.
\tag{8.4}
$$
所有等式在真实共同深域上成立。

$J_jE_j=-E_j$，
$\|N_F-\prod_{j\in F}E_j\|\le r\eta_{m_N}$，
所以主项等于
$(-1)^rr!t_F\prod_{j\in F}E_jf$
加上至多 $r!|t_F|r\eta_{m_N}\|f\|$ 的误差。

## 9. 真实对称平均及非零弱极限

令
$$
\mathcal V_N=
(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F:M\to H.
\tag{9.1}
$$
其像在 $\mathcal D_\infty$。
取 $L_b=\max(1,\sup_j|t_j|^{-1})$，并置正的绝对系数界
$$
A_N=\frac{(2L_b)^r}{r!}\sup_F\|\mathfrak R_F\|.
$$
则 $\|\mathcal V_N\|\le A_N$，且 (5.5) 给
$$
\boxed{
\log A_N\le
K(E_N+L_N^{4/3}+N^2)+K_qrL_N+O(r)+K_M.
}
\tag{9.2}
$$

记
$$
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
$$
(8.4) 求和及纯位平方零关系给
$$
\boxed{
\|T^r\mathcal V_Nf-C_{I_N}^rf\|
\le o(1)\|f\|,\qquad f\in M.
}
\tag{9.3}
$$
具体误差上界为
$$
\epsilon_N e^{C r\log(r+2)}A_N
+2^rr\eta_{m_N}.
$$
由 (1.2)、$r\asymp\sqrt N$，$\log A_N=O(N^2)$，
而 $\epsilon_N\le Ce^{-38516^{m_N-1}}$，故确实趋零。

有限位提升矩阵给
$\|C_{I_N}^r\|\le(1+1/Q_N)^r\to1$。
对两个固定有限柱，因 $\min I_N\to\infty$，
其矩阵元准确为 $(Q_N)_r/Q_N^r$ 乘原内积。
(6.3) 给
$$
\frac{(Q_N)_r}{Q_N^r}\to e^{-1/c}.
$$
一致范数界将该极限延到全部 $H$：
$$
\boxed{
C_{I_N}^r\rightharpoonup e^{-1/c}I,\qquad
T^r\mathcal V_Nf\rightharpoonup e^{-1/c}f.
}
\tag{9.4}
$$
$c$ 是固定正数；这里只使用弱极限。
未知核向量的尾速率没有进入证明。

(7.4) 逐项求和还给，任意固定头 $h$ 下
$$
\boxed{
\|Z_h^k\mathcal V_Nf\|
\le2A_N R_{h,M,c}^k\|f\|,
\quad 0\le k\le(p-1)r.
}
\tag{9.5}
$$

## 10. 局部 $p$ 阶交换子和四次闭合

固定支撑在前 $h$ 位的任意局部矩阵 $D_0$。
令
$$
Z_h=X-a_*I-\sum_{j<h}a_jR_j,\qquad
s_h=a_*+\sum_{j<h}a_j.
$$
$D_0$ 与这个真实闭尾及全部尾累积量完整交换。
有限低头准确有有界 $A$ 因子，例如
$$
X-(Z_h+s_hI)
=A\left[
-2\sum_{j<h}a_jt_jd_j^{-1}
A^{2^j-1}(I+t_jN_j)^{-1}
\right],
$$
$L_n(1)=0$ 给累积量差的同类有限式。
有限多项式相减得到
$$
T=T_{\rm tail}+K_h,\qquad
T_{\rm tail}=\mathcal P(Z_h+s_h;G_{\ge h}),\qquad
K_h=A W_h(Z_h),
$$
$$
W_h(z)=\sum_{\ell=0}^{p-1}B_{h,\ell}z^\ell,\qquad
B_{h,\ell}\in\mathcal A.
\tag{10.1}
$$
$K_h$ 通常无界；后面只在 (9.5) 的真实输入上估计。

$D_0$ 与 $T_{\rm tail}$ 完整交换，$K_h$ 与 $T_{\rm tail}$ 在
$\mathcal D_\infty$ 交换，故
$$
\operatorname{ad}_T^rD_0
=\sum_{s=0}^r(-1)^s\binom rsK_h^{r-s}D_0K_h^s
\quad\text{于 }\mathcal D_\infty.
\tag{10.2}
$$
展开后每项是
$$
A^{r-s}B_{\rm left}D_0 A^sB_{\rm right}Z_h^k,
\qquad k\le(p-1)r.
$$
没有把 $A$ 移过 $D_0$。
原 (3.2) 给
$$
\|A^{r-s}\|\|A^s\|
\le e^{-(5/6)r^4+105r^3}.
$$
令 $B_h(R)=\sum_\ell\|B_{h,\ell}\|R^\ell$。
(9.5) 遂给
$$
\boxed{
\|(\operatorname{ad}_T^rD_0)\mathcal V_Nf\|
\le2\|D_0\|A_N[2B_h(R_{h,M,c})]^r
e^{-(5/6)r^4+105r^3}\|f\|.
}
\tag{10.3}
$$
这没有声称高阶交换子在全 $H$ 上有界。

由 (1.2)、(9.2)，固定 $K_0,K_1$ 后
$$
\log A_N\le K_0N^2+K_1rN^{3/2}+O(r)+K_M.
$$
(6.3) 使右端除以 $r^4$ 的上极限至多
$$
K_0c^2+K_1c^{3/2}.
$$
选择一个固定 $c>0$ 使此和小于 $1/4$。
该选择不依赖局部测试 $D_0,h$。
于是 (10.3) 趋零；各固定 $h,M,c$ 的 jet 常数只贡献 $O(r)$。

令 $\mathcal B(x,y)=\langle x,C_0y\rangle$。
$f,g\in M$ 和 $\mathcal V_Nf$ 均处在所需真实深域。
有限 Leibniz 公式、完整 $C_0$ 自伴性及 $Tg=0$ 给
$$
\mathcal B(D_0T^r\mathcal V_Nf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD_0)\mathcal V_Nf,g).
$$
右端趋零，左端由 (9.4) 趋于 $e^{-1/c}\mathcal B(D_0f,g)$。
因此所有固定局部矩阵都有
$\mathcal B(D_0f,g)=0$。
原 Haar 局部全矩阵代数不可约，任意非零 $f$ 的局部轨道稠密。
取 $g=f\ne0$ 即迫 $C_0f=0$，矛盾。
所以 $M=0$。

由 R176 的准确图循环判据，
$$
[q(u)e^w]_A=\overline{\operatorname{Ran}T}.
$$
$T=C_0T^*C_0$ 且核为零，故像稠密，证明定理 A。

## 11. 两个推论的完整验证

### 11.1 定理 B 的未来近极大尺度

假设 (1.4)。
存在 $m\to\infty$、固定 $\beta,C$ 使
$\log(\rho_m^{-1})\le\beta m+C$。
记
$$
V_m=\sup_{k\ge m}k\rho_k,\qquad 0<V_m\le B.
$$
选择某个 $N\ge m$ 使 $N\rho_N\ge V_m/2$。
于是
$$
\sup_{k\ge N}k\rho_k\le2N\rho_N,
$$
且
$$
\rho_N\ge\frac{m\rho_m}{2N},\qquad
\log(\rho_N^{-1})
\le\beta m+C+\log(2N/m)\le C' N.
$$
最后用 $m\le N$、$\log(N/m)\le N$。
所选 $N\to\infty$，必要时取严格增加子序列。
又
$$
E_N\le N\log(\rho_1/\rho_N)\le C''N^2.
$$
因此 (1.1)--(1.2) 成立，证明定理 B。

特别，$\rho_n\asymp[n(\log(e+n))^\beta]^{-1}$ 的
$n\rho_n$ 有界，$\log(\rho_n^{-1})=O(\log n+\log\log n)=o(n)$；
全部 $\beta>0$ 都满足。
同样包括
$\rho_n\asymp n^{-1}e^{-\sqrt{\log(e+n)}}$，
以及许多没有固定幂尾或固定伸缩指数上界的行。
这些例子的相位及物理排列完全任意。

### 11.2 严格超指数阶梯行

对 (1.5)，取尺度 $N=N_k$。
函数 $x e^{-x^{3/2}}$ 在大 $x$ 上递减，
因此未来各平台的最大 $n\rho_n$ 不超过当前平台末端：
$$
\sup_{n\ge N_k}n\rho_n=N_ke^{-N_k^{3/2}}.
$$
所以 (1.1) 可取 $D=1$。
当前平台内的熵项为零；以前至多 $N_{k-1}=N_k^{1/4}$ 项，
每项不超过 $N_k^{3/2}$ 加有限初项常数。故
$$
E_{N_k}\le N_k^{7/4}+O(N_k^{1/4}),\qquad
L_{N_k}=1+N_k^{3/2}.
$$
满足 (1.2)。
另一方面，对 $N_{k-1}<n\le N_k$，
$$
\frac{\log(\rho_n^{-1})}{n}
=\frac{N_k^{3/2}}n\ge N_k^{1/2}\longrightarrow\infty.
$$
所以定理 B 不适用，而定理 A 真正新增此严格超指数例。
行显然属于 $\ell^1$，任意重排及相位仍在定理范围。

## 12. 对数修正族的分阶精细预算

本节另明确支付最初 log-critical 路线的每个对数因素。
假设仅有
$$
\rho_k\le\frac{C}{k(\log(e+k))^\beta},\qquad\beta>0.
$$
对固定 $n\ge2$、$t$ 大，令 $R=t^{1/n}$。
将 (3.1) 的标量和按 $k<\sqrt R$ 与 $k\ge\sqrt R$ 分开。
前段至多 $C\sqrt R\log R$；
后段 $\log(e+k)\ge\frac12\log R$，用积分比较得
$C R/(\log R)^\beta$。
前段被后一个量吸收，真实低头的 $(\log t)^{4/3}$ 也被吸收。
因此
$$
\boxed{
\|e^{zG_n}\|
\le K_n\exp\left[
C_n\frac{|z|^{1/n}}{(\log(2+|z|))^\beta}
\right].
}
\tag{12.1}
$$
小参数由 $K_n$ 吸收。

在实际 Laplace 积分中取 $|\lambda|$ 小、
$L=\log|\lambda|^{-1}$，按
$s<|\lambda|^{1/2}$ 与 $s\ge|\lambda|^{1/2}$ 分开。
前段整增长不超过 $\exp(C|\lambda|^{-1/(2n)})$。
后段 $\log(2+s/|\lambda|)\ge L/2$，故指数至多
$$
-s+C|\lambda|^{-1/n}L^{-\beta}s^{1/n}
\le-s/2+
C'|\lambda|^{-1/(n-1)}L^{-\beta n/(n-1)}.
$$
前段也被此右侧常数项吸收，因为固定对数幂小于任何正幂。
于是
$$
\boxed{
\|\lambda(\lambda-G_n)^{-1}\|
\le K_n
\exp\left[
C_n\frac{|\lambda|^{-1/(n-1)}}
{(\log|\lambda|^{-1})^{\beta n/(n-1)}}
\right].
}
\tag{12.2}
$$
所有复方向统一，仍由真正的积分左右逆得到。

在 Bell 圆周 $|\lambda_n|=\varepsilon\delta^n$ 上，
各阶指数为常数乘
$$
\left(\frac{\delta^{-1}}
{(\log\delta^{-1})^\beta}\right)^{n/(n-1)}.
$$
$n/(n-1)\le2$，所以一次联合求值成本为
$$
\boxed{
\exp\left[
C_\varepsilon
\frac{\delta^{-2}}{(\log\delta^{-1})^{2\beta}}
\right].
}
\tag{12.3}
$$
当双侧幅度 $\delta\asymp[N(\log N)^\beta]^{-1}$ 时，
(12.3) 的对数是 $O(N^2)$。
该细化与 §4 的一般熵预算一致，且没有把高阶坐标的 Bell 半径错误地都按同一个线性半径计算。

## 13. 范围和剩余接口

本稿的全部新量词都在原 Haar 空间和同一个实际闭核上：
自然域、任意跨度、非同幅保重数逆、输入 jets、重复位 carry、
局部高阶交换子和全空间弱平均均已支付。

定理 B 关闭的是“弱 $\ell^1$ 上界且有子序列指数下界”；
定理 A 还允许少数满足熵预算的严格超指数大跳跃行。
规则 $\rho_n\asymp e^{-\beta n^\alpha}$、$1<\alpha\le3/2$ 有
$E_N\asymp N^{\alpha+1}$，超出本稿 $O(N^2)$ 条件，
其全部重数不由本文解决。
无界弱 $\ell^1$ 常数、一般多模式、正常湮灭者、边界 $N=M$
及普通 ISP 仍是独立开放目标。

## 依赖

R109 的原四次幂界；R125/R176 的真实 first 和 Bell 自然域；
R236 临界弱 $\ell^1$ 全重数稿的真实正规排序接口；
R260 的完整域局部壳与导子 Banach 代数；
R264 的平方规模弱平均；
R266 的非同幅 Hermite 余式和左反射顺序。
