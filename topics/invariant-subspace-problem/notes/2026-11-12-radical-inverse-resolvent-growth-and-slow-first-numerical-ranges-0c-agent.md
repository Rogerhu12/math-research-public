# R190：根理想分母之闭逆的超多项式预解增长与慢第一阶的完整数值域

日期：2026-11-12（UTC）。作者：l2_moments。根代理预留 R190。

状态：完整证明。主结论适用于实际范数代数中的任意非零根理想 quasiaffinity，不限于慢系数。后半给 R185、R188 两个具体慢算子的有限物理头见证。结果明确 R189 准增生预解方法的适用边界；不否定这些算子的未知限制稠密像。

## 1. 一般实际代数分母与主定理

记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
I_1=\ker\chi.
$$
使用 R32 的忠实形式嵌入与连续归一化系数抽取：
$$
\iota:\mathcal A\longrightarrow\mathbb C[[z]],\qquad
\kappa_n(T)=W_n[z^n]\iota(T),\qquad
|\kappa_n(T)|\le\|T\|.
\tag{1.1}
$$
最后的范数界来自实际单边表示的对应矩阵元，不是仅由形式唯一性推出。

取任意
$$
0\ne S\in I_1,\qquad \ker S=0,\qquad
\overline{\operatorname{Ran}S}=H.
\tag{1.2}
$$
因为 $\mathcal A$ 只有字符 $\chi$，$S$ 拟幂零。设
$$
\iota(S)(z)=c_rz^r+c_{r+1}z^{r+1}+\cdots,
\qquad r\ge1,\quad c_r\ne0.
\tag{1.3}
$$

定义真实最大闭逆
$$
Y=S^{-1},\qquad \operatorname{Dom}Y=\operatorname{Ran}S,
\qquad Y(Sx)=x.
\tag{1.4}
$$

本文证明：

1. $Y$ 闭、稠密定义、无界且空谱。
2. 对任意相位 $\phi\in\mathbb R$ 和 $s>0$，
   $$
   R_s^\phi=(I+s e^{-i\phi}Y)^{-1}
   =S(S+s e^{-i\phi}I)^{-1}\in\mathcal A.
   $$
   有精确一阶下界
   $$
   \boxed{\|R_s^\phi\|\ge W_r|c_r|\,s^{-1}.}
   \tag{1.5}
   $$
   更强：对每个固定整数 $k\ge1$，存在与 $\phi$ 无关的 $s_k>0$，使
   $$
   \boxed{
   \|R_s^\phi\|\ge
   \frac{W_{kr}|c_r|^k}{2}\,s^{-k}
   \quad(0<s<s_k).
   }
   \tag{1.6}
   $$
3. 任意旋转 $e^{-i\phi}Y$ 都不准增生；任意有界扰动也不能修复这一点。
4. 标准 $R_s^\phi$ 不可能在全 $H$ 上强趋于 $I$，也不可能强收敛到其他有界算子。
5. 任意旋转的 $-Y$ 都不是 $C_0$ 半群的生成元。
6. 对 R185 的 $S=\sum_j(j+1)^{-2}N_j$ 和 R188 的
   $S=\sum_j(j+1)^{-2}N_j(I+N_j)^{-1}$，
   还给出显式有限柱 $x_{j,\theta}$，使 $y_{j,\theta}=Sx_{j,\theta}$ 满足
   $$
   \frac{\langle Yy_{j,\theta},y_{j,\theta}\rangle}
        {\|y_{j,\theta}\|^2}
   =\frac{e^{i\theta}}{a_j}+o(a_j^{-1}),
   \qquad a_j=(j+1)^{-2},
   \tag{1.7}
   $$
   且误差对 $\theta$ 一致。这两个闭逆的数值域均为整个 $\mathbb C$。

本稿内积约定对第一变量线性。

## 2. 闭逆的准确域与空谱

若 $Sx_n\to u$ 且 $x_n\to v$，有界性给 $Sv=u$。
所以 (1.4) 的图闭；单射性使它是单值算子，稠密像假设使定义域稠密。

对每个 $\lambda\in\mathbb C$，$I-\lambda S$ 是 $\mathcal A$ 中的有界单位。
它及逆与 $S$ 交换，故保持 $\operatorname{Ran}S$。准确地，
$$
\boxed{
(Y-\lambda I)^{-1}=S(I-\lambda S)^{-1}.
}
\tag{2.1}
$$
右侧为有界全域算子，像属于 $\operatorname{Ran}S$。
在全 $H$ 上乘到 $Y-\lambda$ 的右侧得到恒等；
在 $u=Sx\in\operatorname{Dom}Y$ 上乘到左侧也得到 $u$。
因此 $\sigma(Y)=\varnothing$。

$Y$ 不可能有界。否则稠密定义且闭的有界算子必须定义于全 $H$，
从而 $S$ 具有有界全域逆，与 $S$ 拟幂零矛盾。

对 $\lambda=-s^{-1}e^{i\phi}$ 改写 (2.1)，即得
$$
R_s^\phi
=S(S+s e^{-i\phi}I)^{-1}.
\tag{2.2}
$$
此处 $S+s e^{-i\phi}I$ 的可逆性是在实际范数代数中成立。

## 3. 实际归一化系数给统一相位的超多项式增长

因 $S$ 拟幂零，对每个固定 $s>0$，
$$
R_s^\phi
=\sum_{m\ge1}(-1)^{m-1}s^{-m}e^{im\phi}S^m
\tag{3.1}
$$
按算子范数绝对收敛。确实，$r(S/s)=0$，
所以级数的项范数最终被任意固定几何级数控制。
这里不要求 $\|S\|<s$。

对 $z^r$ 系数，只有 $m=1$ 存活：
$$
[z^r]\iota(R_s^\phi)=s^{-1}e^{i\phi}c_r.
$$
由 (1.1) 立刻得到 (1.5)。

现在固定 $k\ge1$。由于 $\operatorname{ord}S^m=mr$，
$z^{kr}$ 系数只含 $m\le k$ 的有限和：
$$
[z^{kr}]\iota(R_s^\phi)
=(-1)^{k-1}s^{-k}e^{ik\phi}c_r^k
+\sum_{m=1}^{k-1}
 (-1)^{m-1}s^{-m}e^{im\phi}[z^{kr}]\iota(S^m).
\tag{3.2}
$$
记
$$
A_k=\sum_{m=1}^{k-1}|[z^{kr}]\iota(S^m)|.
$$
对 $0<s\le1$，余项绝对值不超过
$A_ks^{-(k-1)}$。
当 $A_k=0$ 时无需缩小 $s$；否则取
$$
s_k=\min\left(1,\frac{|c_r|^k}{2A_k}\right).
$$
则对全部相位 $\phi$ 和 $0<s<s_k$，
$$
|[z^{kr}]\iota(R_s^\phi)|
\ge\tfrac12|c_r|^k s^{-k}.
$$
再用 (1.1)，得到 (1.6)。

特别，对每个固定实数 $N\ge0$，
$$
\boxed{
s^N\|R_s^\phi\|\longrightarrow\infty
\quad(s\downarrow0),
}
\tag{3.3}
$$
且该结论可在全部相位上统一。证明只需选整数 $k>N$。

这不是只从“预解范数无界”作定性推断：
每个固定阶都有具体的实际系数证书，
$W_{kr}|c_r|^k/2$ 虽可很小，但对该阶固定且严格为正。

## 4. 准增生性与全空间强预解近似均不成立

### 4.1. 任意旋转都不准增生

假设某个 $\phi$ 及 $\kappa\ge0$ 使
$$
\operatorname{Re}\langle e^{-i\phi}Yx,x\rangle
\ge-\kappa\|x\|^2
\quad(x\in\operatorname{Dom}Y).
\tag{4.1}
$$
当 $s\kappa<1$ 时，Cauchy–Schwarz 给
$$
\|(I+s e^{-i\phi}Y)x\|\,\|x\|
\ge(1-\kappa s)\|x\|^2.
$$
(2.2) 已保证这个算子实际满射，所以
$$
\|R_s^\phi\|\le(1-\kappa s)^{-1}.
$$
这与 (1.5) 矛盾。

故不存在 (4.1)。如果对某个有界 $K\in B(H)$，
$e^{-i\phi}(Y+K)$ 准增生，则减去有界项只把下界常数增加 $\|K\|$，
又会给 (4.1)。所以任意有界扰动都不能修复准增生性；
这一附带结论不要求 $K$ 交换。

### 4.2. 标准预解族不可能全空间强收敛

固定 $\phi$，若 $R_s^\phi$ 在 $s\downarrow0$ 时对每个向量强收敛，
则沿任意序列 $s_n\downarrow0$，
一致有界原理给
$$
\sup_n\|R_{s_n}^\phi\|<\infty.
$$
(1.5) 已排除这种可能。
因此该标准族不能强趋于 $I$，也不能在全空间强趋于其他算子。

这不排除其他强主理想近似。
例如 R23 仍给原 $A$ 的有界强近似 $A p_\nu(A)\to I$；
该事实与 $A(A+sI)^{-1}$ 的范数爆炸完全相容。
本稿也没有由标准预解族失败否定任何特定不变限制上的稠密像。

## 5. 自含的 C0 半群障碍

设某个旋转
$$
G=-e^{-i\phi}Y
$$
是一个 $C_0$ 半群 $(T(t))_{t\ge0}$ 的生成元。

先由强连续性和一致有界原理，在某个固定紧时间区间上得到统一范数界；
再用半群律逐区间相乘，存在 $M\ge1$、$\omega\in\mathbb R$ 使
$$
\|T(t)\|\le M e^{\omega t}\quad(t\ge0).
\tag{5.1}
$$

对 $\lambda>\max(\omega,0)$ 定义 Bochner 积分
$$
J_\lambda x=\int_0^\infty e^{-\lambda t}T(t)x\,dt.
$$
它有界，且
$$
\|J_\lambda\|\le\frac{M}{\lambda-\omega}.
\tag{5.2}
$$

说明这是实际预解而非形式 Laplace 记号。
对有限 $R>0$，半群差商直接给
$$
\int_0^R T(t)x\,dt\in\operatorname{Dom}G,\qquad
G\int_0^R T(t)x\,dt=T(R)x-x.
$$
对指数加权积分作 Riemann 和或分部积分，得
$$
G\int_0^R e^{-\lambda t}T(t)x\,dt
=e^{-\lambda R}T(R)x-x
+\lambda\int_0^R e^{-\lambda t}T(t)x\,dt.
$$
由 (5.1) 令 $R\to\infty$，再用 $G$ 闭，得到
$$
(\lambda I-G)J_\lambda x=x.
$$
对 $x\in\operatorname{Dom}G$，
$t\mapsto T(t)x$ 可微、导数为 $T(t)Gx$，
同样分部积分给
$J_\lambda(\lambda I-G)x=x$。
所以 $J_\lambda=(\lambda I-G)^{-1}$。

取 $s=1/\lambda$，得到
$$
R_s^\phi=\lambda J_\lambda,\qquad
\|R_s^\phi\|\le\frac{M\lambda}{\lambda-\omega}.
$$
右侧在 $\lambda\to\infty$ 时有界，与 §3 矛盾。
因此所有旋转的 $-Y$ 都不是 $C_0$ 半群生成元；
正负号可吸收到相位中。

这个证明没有仅引用一个未展开的生成元判据。

## 6. 两个具体慢算子与有限物理头

取
$$
a_j=(j+1)^{-2},\qquad
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jY_j,\qquad
Y_j=N_j(I+N_j)^{-1}.
\tag{6.1}
$$
R185、R188 给二者单射、稠密像；它们属于 $I_1$。
所以 §1–5 全部适用。

为给出数值域的显式见证，使用 Haar 张量空间每一位的正交物理基
$$
e_0=\sqrt2\,1_{\{b=0\}},\qquad
e_1=\sqrt2\,1_{\{b=1\}},
$$
及 Haar 参考向量 $\Omega=(e_0+e_1)/\sqrt2$。
纯位算子满足 $E e_0=e_1$、$E e_1=0$。

固定 $j\ge2$、$M>j+1$、$\theta\in\mathbb R$，令
$$
z_\theta=(e_0+e^{i\theta}e_1)/\sqrt2
$$
并取有限柱单位向量 $x=x_{j,M,\theta}$：
前 $M$ 位全部为 $e_1$，唯第 $j$ 位换成 $z_\theta$；
从第 $M$ 位起保留参考 $\Omega$。
于是
$$
\|E_jx\|=1/\sqrt2,\qquad
\langle x,E_jx\rangle=e^{i\theta}/2.
\tag{6.2}
$$

以下逐段控制真实进位，不对固定低位粗用全局 $\eta_i$ 界。

### 6.1. 低于 j 的位

由
$$
N_i=E_i+\eta_iE_i^*N_{i+1}
$$
和 $i,\ldots,j-1$ 位全为物理 $e_1$，递推准确给
$$
N_ix=\frac{\alpha_j}{\alpha_i}
 E_i^*\cdots E_{j-1}^*N_jx
\quad(i<j).
$$
所以
$$
\|N_ix\|\le\alpha_j/\alpha_i\le\eta_{j-1}.
\tag{6.3}
$$
对 Cayley 项把真逆置左：
$$
Y_ix=(I+N_i)^{-1}N_ix,\qquad
\|Y_ix\|\le3\alpha_j/\alpha_i.
\tag{6.4}
$$
这里没有假设完整逆保持物理头。

### 6.2. j 以上但仍在有限头内的位

对 $j<i<M$，相同递推越过全部物理 $e_1$ 位，给
$$
N_ix=\frac{\alpha_M}{\alpha_i}
 E_i^*\cdots E_{M-1}^*N_Mx.
$$
故
$$
\|N_ix\|\le\alpha_M/\alpha_i\le\eta_{M-1},\qquad
\|Y_ix\|\le3\alpha_M/\alpha_i.
\tag{6.5}
$$

### 6.3. 第 j 位自身

第 $j+1,\ldots,M-1$ 位全为 $e_1$，因此
$$
\|(N_j-E_j)x\|\le\alpha_M/\alpha_j.
\tag{6.6}
$$
同样估计必须在已经作用 $E_j$ 的向量上再检查。
$N_{j+1}$ 与 $E_j$ 交换，且 $E_jx$ 不改变上方物理头，
所以
$$
\|(N_j-E_j)E_jx\|\le\alpha_M/\alpha_j.
\tag{6.7}
$$

实际非交换逆差恒等式是
$$
Y_j-E_j
=(I+N_j)^{-1}(N_j-E_j)(I-E_j).
$$
结合 (6.6)—(6.7) 及逆范数不超过3，
$$
\boxed{\|(Y_j-E_j)x\|\le6\alpha_M/\alpha_j.}
\tag{6.8}
$$

### 6.4. 头外全部高位

只使用算子范数
$\|N_i\|=1$、$\|Y_i\|\le3$。
由于
$$
\sum_{i\ge M}a_i\le1/M,
$$
头外总贡献不超过 $3/M$。不要求尾参考向量有任何新的衰减性质。

### 6.5. 汇总及正确的尺度

记 $A_0=\sum_ia_i<2$。
两种 $S\in\{S_N,S_Y\}$ 均满足对所有 $\theta$ 一致的估计
$$
\boxed{
\|Sx_{j,M,\theta}-a_jE_jx_{j,M,\theta}\|
\le
3A_0\eta_{j-1}
+6a_j\frac{\alpha_M}{\alpha_j}
+3A_0\eta_{M-1}
+\frac3M.
}
\tag{6.9}
$$
取
$$
M=M_j=j^4.
$$
由 $\eta_j\le e^{-77016^j}$、$a_j=(j+1)^{-2}$，
右侧除以 $a_j$ 趋于0。
因此，令 $x_{j,\theta}=x_{j,M_j,\theta}$，有
$$
\boxed{
Sx_{j,\theta}=a_jE_jx_{j,\theta}+o(a_j),
}
\tag{6.10}
$$
误差对 $\theta$ 一致。
这里先固定慢系数的明确尺度，再选 $M_j$；
没有假设未知核向量的任何尾速率。

## 7. 显式数值域圆圈与全复平面

令 $Y=S^{-1}$，
$$
y_{j,\theta}=Sx_{j,\theta}\in\operatorname{Dom}Y.
$$
$S$ 单射，故这些向量非零，且 $Yy_{j,\theta}=x_{j,\theta}$。
由 (6.2)、(6.10)，
$$
\|y_{j,\theta}\|^2=\tfrac12a_j^2+o(a_j^2),
$$
$$
\langle Yy_{j,\theta},y_{j,\theta}\rangle
=\langle x_{j,\theta},Sx_{j,\theta}\rangle
=\tfrac12a_je^{i\theta}+o(a_j).
$$
所以 (1.7) 成立，误差对相位一致。

固定任意旋转 $\phi$，取 $\theta=\phi+\pi$，
立刻得到
$$
\operatorname{Re}
\frac{\langle e^{-i\phi}Yy_{j,\theta},y_{j,\theta}\rangle}
     {\|y_{j,\theta}\|^2}
=-a_j^{-1}+o(a_j^{-1})\to-\infty.
\tag{7.1}
$$
这是 §4 准增生障碍的显式向量证明。

还可得到完整数值域。取四个相位
$0,\pi/2,\pi,3\pi/2$，其数值域点分别为半径
$a_j^{-1}$ 的四个坐标方向加 $o(a_j^{-1})$ 误差。
它们的凸包包含半径趋于无穷的圆盘。
线性定义域算子的数值域是凸的：任意有限个域向量张成的空间仍在域内，
压缩为有限维矩阵后应用数值域凸性，再取这些有限维空间的并即可。
于是
$$
\boxed{W(S_N^{-1})=W(S_Y^{-1})=\mathbb C.}
\tag{7.2}
$$

因此这些实际闭逆虽为空谱，数值域却覆盖全平面。
没有从“空谱”推断任何未成立的半平面控制。

## 8. 与 R189 及原不变子空间问题的界线

R189 的正机制使用空谱闭第一阶加有界交换扰动，并额外拥有一个旋转后的准增生下界。
该下界给标准预解在小正参数上的一致范数界，
继而在每个子商上以 $O(n\log n)$ 输入放大获得精确混合型。

本稿表明：任何满足 (1.2) 的 $\mathcal A$ 内根理想分母，
其闭逆都不能拥有这一准增生接口。
这包括原 $A$ 自身及 R185、R188 的具体慢符号。
这些逆的范数代数分母与 R189 的有界逆交换子不能无区别替换。

结论仅排除了这一种标准预解、半群及半平面方法。
它不排除另一个共同正则器，
不排除某个具体 $S$ 在所有原不变限制上仍稠密，
也不把边界的非标准闭理想或无限核传回原 Haar 空间。
一般慢核与完整 Hilbert 不变子空间问题仍未解决。
