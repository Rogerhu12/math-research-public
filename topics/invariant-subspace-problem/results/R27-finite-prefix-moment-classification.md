# R27：全部有限柱平方矩匹配的谱符号分类与精确最小范数

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94，子任务 `centered_literature`。

**状态：已证明的中间结论。** 固定比较目标 $h=1$，将[复对称矩笔记](R24-complex-symmetric-moments-and-escape.md) 的单一高位构造推广到全部有限柱函数。本条完整分类了前 $2^m$ 个平方矩精确相等的 $2^{2^m}$ 个解，并证明非平凡解的最小 $L^2$ 范数恰由单一最高位构造取得，必趋于无穷。它不覆盖一般目标 $h$、一般 $L^2$ 匹配向量或只有近似矩相等的柱逼近；没有解决普通 ISP，不主张文献新颖性。

## 1. 定义与结论

在 R9 的 $H=L^2(\mathbb Z_2,\mu)$ 上，

$$
(Af)(y)=a_{v_2(y)}f(y-1),\qquad a_j=e^{-b_j},
$$

$$
b_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.1}
$$

零点处的权仍定义为零。令

$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y),\qquad Q_n(f)=B(A^nf,f).
\tag{1.2}
$$

固定 $m\ge1$，$N=2^m$，令 $V_m$ 为只依赖最低 $m$ 位的柱函数空间。用函数值坐标 $v=(v_0,\dots,v_{N-1})$ 表示它，于是

$$
\|v\|_{L^2}^2=\frac1N\sum_{j=0}^{N-1}|v_j|^2,
\qquad B_m(v,u)=\frac1N\sum_{j=0}^{N-1}v_j u_{N-1-j}.
\tag{1.3}
$$

定义

$$
\theta_m=\sum_{s=0}^{\infty}2^{-s-1}a_{m+s},
\qquad \rho_m=\frac{\theta_m}{a_{m-1}}\in(0,1).
\tag{1.4}
$$

这与前一笔记的记号满足 $\theta_m=c_{m-1}$、$\rho_m=\rho_{m-1}^{\rm previous}$；本文下标 $m$ 表示整个柱空间深度。

**定理 1.1。** 集合

$$
\mathcal S_m=\{g\in V_m:Q_n(g)=Q_n(1)\text{ 对所有 }0\le n<N\}
\tag{1.5}
$$

恰有 $2^N$ 个元素，其谱符号表达在 §3 给出。除去 $g=1,-1$ 后，有精确极小值

$$
\boxed{
\min_{g\in\mathcal S_m\setminus\{1,-1\}}\|g\|_{L^2}
=\sqrt{\frac{\rho_m+\rho_m^{-1}}2}.
}
\tag{1.6}
$$

等号只在以下两个向量取得：

$$
g=\pm g_m^{\min},\qquad
g_m^{\min}(y)=\sqrt{\rho_m}\,\mathbf1_{\{b_{m-1}(y)=0\}}
+\rho_m^{-1/2}\,\mathbf1_{\{b_{m-1}(y)=1\}}.
\tag{1.7}
$$

特别地

$$
\min_{g\in\mathcal S_m\setminus\{1,-1\}}\|g\|
\ge\sqrt{\frac{a_{m-1}}{2a_m}}\longrightarrow\infty.
\tag{1.8}
$$

因此，若 $g_m\in V_m$ 精确匹配前 $2^m$ 个平方矩且范数一致有界，则充分大 $m$ 时必有 $g_m\in\{1,-1\}$。所有 $\mathcal S_m$ 中的解还自动匹配第 $N$ 阶矩；(1.7) 的两个非平凡极小解在第 $N+1$ 阶首先失败，公式见前一笔记定理 4.1。

## 2. 前 $N$ 阶矩由有限加权循环精确给出

定义 $N\times N$ 加权循环矩阵 $J_m$：

$$
J_m e_j=a_{v_2(j+1)}e_{j+1}\quad(0\le j<N-1),
\qquad J_m e_{N-1}=\theta_m e_0.
\tag{2.1}
$$

这里 $e_j$ 是函数值坐标中的标准基。令

$$
C_m=\prod_{j=1}^{N-1}a_{v_2(j)}
=\prod_{s=0}^{m-1}a_s^{2^{m-s-1}}.
\tag{2.2}
$$

**引理 2.1。** 对每个 $v\in V_m$ 和 $0\le n\le N$，

$$
Q_n(v)=B_m(J_m^n v,v).
\tag{2.3}
$$

**证明。** 写 $y=r+Nz$，$0\le r<N$。长度不超过 $N$ 的整数段 $y,y-1,\dots,y-n+1$ 至多包含一个 $N$ 的倍数。没有这个倍数时，其所有权只由低位 $r$ 决定；有这个倍数时，对高位尾部 $z$ 积分得到

$$
\int a_{m+v_2(z)}\,d\mu(z)=\theta_m.
$$

其他权仍只由低位决定。$v(y-n)$ 与 $v(-1-y)$ 只依赖低位，因此逐个 $r$ 的条件积分，恰等于有限循环中跨零边权为 $\theta_m$ 的矩阵幂。这给出 (2.3)。证毕。

这里不能声称 $\mathbb E_m A^n|_{V_m}=J_m^n$ 对所有 $n$ 成立：超过一个周期后，会出现相邻尾权的相关乘积，其均值一般不等于 $\theta_m$ 的相应幂。

显然

$$
J_m^N=C_m\theta_m I.
\tag{2.4}
$$

此外 $a_{v_2(j)}=a_{v_2(N-j)}$ 对 $1\le j<N$ 成立，所以 $J_m$ 关于 $B_m$ 对称。跨零边是它自己的反射边，任意正值 $\theta_m$ 都保留这一对称性。

## 3. 所有解的谱符号分类

记

$$
r_m=(C_m\theta_m)^{1/N},\qquad
W_0=1,\quad W_j=\prod_{i=1}^j a_{v_2(i)}\ (1\le j<N),
$$

$$
d_j=W_j/r_m^j,\qquad D=\operatorname{diag}(d_0,\dots,d_{N-1}).
\tag{3.1}
$$

若 $S$ 是无权循环移位 $Se_j=e_{j+1\bmod N}$，直接核验每条边可得

$$
J_m=D(r_mS)D^{-1}.
\tag{3.2}
$$

令 $\zeta=e^{2\pi i/N}$。取酉 Fourier 矩阵 $\mathcal F$，其列为 $S$ 的单位特征向量 $\phi_\ell$，对应特征值 $\zeta^\ell$。因此 $J_m$ 有互异特征值 $\lambda_\ell=r_m\zeta^\ell$，特征向量为 $\psi_\ell=D\phi_\ell$。

因为 $J_m$ 关于 $B_m$ 对称，互异特征向量之间 $B_m$-正交；又这是一组基，$B_m$ 非退化，所以每个 $B_m(\psi_\ell,\psi_\ell)$ 都非零。

写 $1=\sum\alpha_\ell\psi_\ell$、$g=\sum\beta_\ell\psi_\ell$。由 (2.3)，前 $N$ 个矩相等当且仅当

$$
\sum_{\ell=0}^{N-1}\lambda_\ell^n
(\beta_\ell^2-\alpha_\ell^2)B_m(\psi_\ell,\psi_\ell)=0,
\quad 0\le n<N.
$$

Vandermonde 矩阵可逆，故这等价于 $\beta_\ell^2=\alpha_\ell^2$ 对每个 $\ell$ 成立。

下面证明所有 $\alpha_\ell$ 非零，从而得到**恰好** $2^N$ 个不同解。令

$$
x=D^{-1}1=(d_0^{-1},\dots,d_{N-1}^{-1})^t.
$$

一旦知道 $\sum_{j=1}^{N-1}d_j^{-1}<1$，每个 Fourier 系数 $\alpha_\ell=(\mathcal F^*x)_\ell$ 都非零，因为其首项为 $1/\sqrt N$，其余项绝对值总和严格小于该首项。这个估计在 §4 给出。

于是全部解为

$$
\boxed{
g=D U_\varepsilon x,\qquad
U_\varepsilon=\mathcal F\operatorname{diag}(\varepsilon_0,\dots,\varepsilon_{N-1})\mathcal F^*,
\quad \varepsilon_\ell\in\{1,-1\}.
}
\tag{3.3}
$$

$U_\varepsilon$ 是 Euclidean 范数下的酉自伴循环矩阵。全正号及全负号分别给 $g=1,-1$；其他符号选择均非平凡。由 (2.4)、(2.3)，前 $N$ 个矩相等也自动推出第 $N$ 阶矩相等。

## 4. 对角相似变换的两个定量恒等式

置 $\bar b_m=-\log\theta_m$，并令

$$
\gamma_m=\frac{\bar b_m-b_{m-1}}N>0.
\tag{4.1}
$$

对 $j<N$，按各个 $2$ 的幂的倍数计数，有

$$
-\log W_j=jb_0+\sum_{s=1}^{m-1}\left\lfloor\frac j{2^s}\right\rfloor(b_s-b_{s-1}).
\tag{4.2}
$$

另一方面，一整个有限循环的平均对数权给

$$
-\log r_m
=b_0+\sum_{s=1}^{m-1}2^{-s}(b_s-b_{s-1})+\gamma_m.
\tag{4.3}
$$

由于 $b_s$ 严格递增，将 (4.2) 中的取整改为上界 $j/2^s$，得到

$$
\boxed{d_j\ge e^{j\gamma_m}\qquad(1\le j<N).}
\tag{4.4}
$$

由 $\theta_m\le a_m$，以及 (1.1) 的精确差分

$$
b_m-b_{m-1}=1400\,16^{m-1}-630\,8^{m-1}+300\,2^{m-1}
\ge770\,16^{m-1},
$$

可得

$$
\gamma_m\ge385\,8^{m-1}.
\tag{4.5}
$$

所以 $\sum_{j\ge1}d_j^{-1}\le e^{-\gamma_m}/(1-e^{-\gamma_m})<1$，补足 §3 所需非零性。并且以标准 Euclidean 范数计，

$$
\delta_m:=\|x-e_0\|_2
\le\frac{e^{-\gamma_m}}{\sqrt{1-e^{-2\gamma_m}}}
\le2e^{-\gamma_m}.
\tag{4.6}
$$

第二个恒等式来自低位权的反射对称性。对 $1\le j<N$，

$$
W_jW_{N-j}=C_m a_{v_2(j)},
$$

因为 $W_{N-j}=C_m/W_{j-1}$。除以 $r_m^N=C_m\theta_m$ 得

$$
\boxed{d_jd_{N-j}=\frac{a_{v_2(j)}}{\theta_m}.}
\tag{4.7}
$$

特别地

$$
d_{N/2}=\sqrt{\frac{a_{m-1}}{\theta_m}}=\rho_m^{-1/2}=:D_m.
\tag{4.8}
$$

若 $j\notin\{0,N/2\}$，则 $v_2(j)\le m-2$，因此

$$
\max\{d_j,d_{N-j}\}\ge D_m
\sqrt{\frac{a_{m-2}}{a_{m-1}}}
\qquad(m\ge2).
\tag{4.9}
$$

## 5. 非恒定谱符号必产生大坐标

设

$$
u=U_\varepsilon e_0,\qquad
u_j=\frac1N\sum_{\ell=0}^{N-1}\varepsilon_\ell\zeta^{-j\ell}.
\tag{5.1}
$$

因为 $\varepsilon_\ell$ 实，$u_{N-j}=\overline{u_j}$。酉性及 (4.6) 还给每个坐标的误差界

$$
|(U_\varepsilon x)_j-u_j|\le\delta_m.
\tag{5.2}
$$

先记录一个不使用代数数论的粗界。非恒定符号序列中，若正号个数为 $p\in\{1,\dots,N-1\}$，则

$$
\sum_{j=1}^{N-1}|u_j|^2
=1-u_0^2=\frac{4p(N-p)}{N^2}
\ge\frac{4(N-1)}{N^2}.
$$

故某个 $j\ne0$ 有 $|u_j|\ge2/N$，其共轭位置也满足同一界。由 (4.7)，这两个位置中至少一个的 $d$ 值不小于 $D_m$。由 (4.5)—(4.6) 可取 $\delta_m\le1/N$，所以任意非平凡解满足

$$
\|g\|_{L^2}\ge N^{-3/2}D_m.
\tag{5.3}
$$

这已证明所有非平凡解的范数一致发散。要找**精确极小值**，需比较交替符号与其余符号。

### 5.1 非零 Fourier 系数的离散下界

若 $u_j\ne0$，则 $Nu_j$ 是域 $\mathbb Q(\zeta)$ 中的非零代数整数。该域次数为 $\varphi(N)=N/2$；每个共轭都是 $N$ 个符号与单位根的和，其绝对值至多 $N$。非零代数整数的域范数是非零整数，绝对值至少 $1$。将其他 $N/2-1$ 个共轭用 $N$ 控制，得到

$$
\boxed{|u_j|\ge N^{-N/2}=:q_N.}
\tag{5.4}
$$

这是所需的全部代数数论事实；若该元素位于更小子域，使用整个 $\mathbb Q(\zeta)$ 的域范数仍给相同有效下界。

由 (4.5)—(4.6)，

$$
\delta_m\le\tfrac12 q_N.
\tag{5.5}
$$

具体只需验证 $\gamma_m\ge\log4+(N/2)\log N$。因 $4^{m-1}\ge m$，(4.5) 的右端至少为 $385m2^{m-1}$，显然足以满足该不等式（包括 $m=1$）。

### 5.2 非交替符号的范数严格超过 $D_m$

若 $u$ 的支集包含于 $\{0,N/2\}$，Fourier 反演给

$$
\varepsilon_\ell=u_0+u_{N/2}(-1)^\ell.
$$

因为每个值都为 $\pm1$，这种符号序列只能是全同号，或交替号 $\varepsilon_\ell=\pm(-1)^\ell$。因此，任何既非恒定又非交替的符号序列，都存在某个 $j\notin\{0,N/2\}$ 使 $u_j\ne0$。

取这个 $j$ 及 $N-j$ 中 $d$ 较大的位置。由 (4.9)、(5.2)、(5.4)—(5.5)，

$$
\|g\|_{L^2}
\ge\frac{D_m}{2\sqrt N}\sqrt{\frac{a_{m-2}}{a_{m-1}}}\,N^{-N/2}.
\tag{5.6}
$$

对 $m\ge2$，这个下界严格大于 $D_m$。为核实常数，注意

$$
\log\sqrt{\frac{a_{m-2}}{a_{m-1}}}
=\frac{b_{m-1}-b_{m-2}}2\ge385\,16^{m-2},
$$

而

$$
\log(2\sqrt N\,N^{N/2})
=\log2+\frac{N+1}{2}\log N
\le N\log N=m2^m\log2.
$$

简单归纳给 $m2^m\le8\cdot16^{m-2}$（$m\ge2$），所以前一个指数严格大于后一个指数。因此

$$
\boxed{\|g\|_{L^2}>D_m\quad
\text{对所有非恒定、非交替的谱符号解。}}
\tag{5.7}
$$

$m=1$ 时只有两类符号，不存在需要考虑的第三类。

## 6. 交替符号恰给单一最高位极小解

取 $\varepsilon_\ell=(-1)^\ell$，则 $U_\varepsilon=S^{N/2}$，所以

$$
g=D S^{N/2}D^{-1}1
=r_m^{-N/2}J_m^{N/2}1.
\tag{6.1}
$$

记 $C_{m-1}=\prod_{j=1}^{N/2-1}a_{v_2(j)}$。对低位坐标 $0\le r<N/2$，半圈路径跨越零边，其权积为 $C_{m-1}\theta_m$；对 $N/2\le r<N$，半圈路径跨越中间边，其权积为 $C_{m-1}a_{m-1}$。又

$$
C_m=C_{m-1}^2a_{m-1},\qquad
r_m^{N/2}=C_{m-1}\sqrt{a_{m-1}\theta_m}.
$$

代入 (6.1)，得到前半坐标为 $\sqrt{\rho_m}$、后半坐标为 $\rho_m^{-1/2}$，恰是 (1.7)。反号符号给它的负值。因此

$$
\|g_m^{\min}\|_{L^2}^2
=\frac{\rho_m+\rho_m^{-1}}2
<\rho_m^{-1}=D_m^2.
\tag{6.2}
$$

结合 (5.7)，这是全部非平凡解中的严格极小值，且只由正负这两个解取得。这证明 (1.6)—(1.7)。由 $\theta_m\le a_m$ 立即得到 (1.8)，而权比趋零保证其发散。定理证毕。

## 7. 这个有限层结论留下的实际缺口

若一般 $g\in L^2$ 的全部平方矩与 $1$ 相等，其条件期望 $g_m=\mathbb E_mg$ 虽然强趋 $g$，却通常只满足**近似**矩匹配，而不是 (1.5)。对每个固定 $n$，确有

$$
|Q_n(g_m)-Q_n(g)|
\le\|A^n\|\,\|g_m-g\|\,(\|g_m\|+\|g\|).
\tag{7.1}
$$

但将这些近似矩还原成 §3 的谱坐标，要逆转高度病态的 Vandermonde/对角相似变换；任意 $L^2$ 向量没有提供足够快的柱逼近速度。因此不能据此推出一般匹配只剩 $g=\pm1$。后者一旦证明，将只排除固定目标 $h=1$ 的这类匹配；要解决本模型仍须处理一般 $h,g$ 的等价存在性问题。
