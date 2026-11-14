# R156：有界有限 chaos 的实际指数倾斜与空谱锚多项式

日期：2026-11-12（UTC）。独占作者：critical_kernel；主会话提出梯度—列范数接口。
状态：以下矩阵列估计、实际倾斜乘子、参数整性、空谱锚及全部定义域步骤均已完整证明，经过主会话、l2_moments 与 literature 分段独立审读。
没有假设有限 chaos 的 Walsh 系数绝对可和，也没有假设系数由有限个第一阶模式生成。

## 1. 结论与基本记号

沿用实际模型
$$
N_j=A^{2^j}/d_j,\qquad E_j=e_{10}^{(j)},\qquad
\|N_j-E_j\|=\eta_j,\qquad \eta_j\le e^{-770\,16^j}.
$$
本稿统一记
$$
V_j=(I-N_j)(I+N_j)^{-1}=I-2Y_j,\qquad
Y_j=N_j(I+N_j)^{-1}.
$$
不同 $V_j$ 交换，$\|V_j\|\le6$，且对有限位集 $F$，
$$
V_F1=\chi_F.
$$
因此有限柱 $f=\sum_F\widehat f(F)\chi_F$ 的实际乘子为
$$
X_f=\sum_F\widehat f(F)V_F.
\tag{1.1}
$$
R92 证明每个 $f\in H_{\le d}\cap L^\infty$ 都有唯一连续代表，低位条件期望 $f_m$ 一致趋于该代表，并且
$$
X_f\in\mathcal A,\quad X_f1=f,\quad \chi(X_f)=f(0).
\tag{1.2}
$$
以后 $f(0)$ 一律指这个连续代表在全零物理位处的值，即全部 $\chi_j=1$ 处的值。

给 $c=(c_j)\in\ell^2$，定义局部实际算子
$$
R_j(z)=
(V_j\cosh z+I\sinh z)
(I\cosh z+V_j\sinh z)^{-1}.
\tag{1.3}
$$
下面证明每个有界有限 chaos $f$ 都有规范的
$$
\Phi_c(f)\in\mathcal A,\qquad \chi(\Phi_c(f))=f(0),
\tag{1.4}
$$
且对任意
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,
$$
有真实向量恒等式
$$
\boxed{f e^w=\Phi_b(f)e^w.}
\tag{1.5}
$$
$\Phi_b(f)$ 是一个有界交换子，不是把 $f$ 点乘到任意向量上的乘法算子。
对任意 $a,b\in\ell^2$，$t\mapsto\Phi_{b+ta}(f)$ 为算子范数整函数。

特别地，
$$
\boxed{f(0)\ne0\Longrightarrow f e^w\text{ 循环}.}
\tag{1.6}
$$
这里 $w$ 可为任意复杂 $\ell^2$ 第一阶指数。

进一步，设
$$
u=a_*+\sum_ja_j\chi_j
$$
的实际闭第一阶乘子 $X=X_u$ 为空谱。
例如 R134/R138 的充分且精确谱分类条件是 $a\notin\ell^1$，并存在 $\theta$ 使
$$
\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)<\infty.
\tag{1.7}
$$
设 $p\ge1$，$f_0,\ldots,f_p$ 各为有界有限 chaos，允许不同有限次数，且
$$
f_p(0)\ne0.
\tag{1.8}
$$
则
$$
\boxed{
\left[\sum_{k=0}^p u^k f_k\right]e^w
\text{ 对 }A\text{ 循环}.
}
\tag{1.9}
$$
对每个 $\lambda\in\mathbb C$，同样有
$$
\boxed{
\left[\sum_{k=0}^p u^k f_k-\lambda\right]e^w
\text{ 循环}.
}
\tag{1.10}
$$
这些向量自动非零。指数始终乘在括号外；(1.10) 不声称原加权向量直接减 $\lambda$ 的无条件版本。

## 2. Banach 值端点 Markov 界与离散梯度

本节先只考虑有限柱函数，以便所有和有限。

### 2.1 一个自含的端点 Markov 界

若 $q(t)$ 是次数不超过 $d\ge1$ 的 Banach 空间值多项式，则
$$
\|q'(1)\|\le d^2\sup_{-1\le t\le1}\|q(t)\|.
\tag{2.1}
$$
确切地，在 Chebyshev 节点 $t_\ell=\cos(\ell\pi/d)$，$0\le\ell\le d$，
记 Lagrange 基多项式为 $\ell_\ell(t)$。
对 $\ell\ge1$，$\ell_\ell'(1)$ 的符号是 $(-1)^\ell$，而 $\ell_0'(1)>0$。
Chebyshev 多项式满足 $T_d(t_\ell)=(-1)^\ell$，所以
$$
\sum_{\ell=0}^d|\ell_\ell'(1)|
=\sum_{\ell=0}^d(-1)^\ell\ell_\ell'(1)
=T_d'(1)=d^2.
$$
对向量值 Lagrange 公式逐项取范数即得 (2.1)。$d=0$ 时导数为零。

令 Walsh 噪声算子 $\mathsf T_t$ 在第 $k$ 次 chaos 上乘 $t^k$。
对 $t\in[-1,1]$，它由独立保留/翻转各位的概率平均实现，所以对任何 Banach 值有限柱函数都为 $L^\infty$ 收缩。
令 $\mathcal N$ 为 Walsh 次数算子。
对次数至多 $d$ 的函数 $f$，有 $\left.\partial_t\mathsf T_tf\right|_{t=1}=\mathcal Nf$，从而
$$
\boxed{\|\mathcal Nf\|_\infty\le d^2\|f\|_\infty.}
\tag{2.2}
$$

### 2.2 strip 导数及 carré du champ 恒等式

定义
$$
D_jf=\sum_{F\ni j}\widehat f(F)\chi_{F\setminus\{j\}},
\qquad D_J=\prod_{j\in J}D_j.
\tag{2.3}
$$
$D_j$ 是去掉 $\chi_j$ 的导数，不是直接的翻转差。
若 $\varepsilon^{(j)}$ 表示翻转第 $j$ 位，则
$$
f(\varepsilon)-f(\varepsilon^{(j)})
=2\chi_j(\varepsilon)D_jf(\varepsilon).
$$
因此对 Hilbert 空间值 $f$，逐位直接展开平方得到
$$
\boxed{
\sum_j\|D_jf\|^2
=\operatorname{Re}\langle f,\mathcal Nf\rangle
-\frac12\mathcal N(\|f\|^2).
}
\tag{2.4}
$$
$\chi_j$ 在平方中模长为一，故没有遗漏这个翻转因子。

$f$ 的次数至多 $d$ 时，$\|f\|^2$ 的 Walsh 次数至多 $2d$。用 (2.2)，
$$
\left\|\left(D_jf\right)_j\right\|_{L^\infty(\ell^2)}
\le\sqrt3\,d\,\|f\|_\infty.
\tag{2.5}
$$
这对 Hilbert 值 $f$ 原样成立：第一项由
$\|f\|_\infty\|\mathcal Nf\|_\infty$ 控制，第二项的绝对值不超过 $2d^2\|f\|_\infty^2$。

对有序导数数组反复应用 (2.5)，每次次数降低一。
重复位导数为零，互不相同的 $k$ 个位有 $k!$ 种排列。于是
$$
\boxed{
\left\|\left(D_Jf\right)_{|J|=k}\right\|_{L^\infty(\ell^2)}
\le
G_{d,k}\|f\|_\infty,\quad
G_{d,k}=
\frac{3^{k/2}}{\sqrt{k!}}\frac{d!}{(d-k)!},
\quad 0\le k\le d.
}
\tag{2.6}
$$
$k=0$ 时数组仅含 $f$。

对一般标量 $f\in H_{\le d}\cap L^\infty$，R92 给有限柱 $f_m\to f$ 一致。
把 (2.6) 用于 $f_m-f_n$，得到全部导数数组在 $L^\infty(\ell^2)$ 中一致 Cauchy。
其各个坐标在 $L^2$ 中必为 (2.3) 的 Walsh 导数，所以 (2.6) 延拓到一般这样的 $f$。

这里没有使用或声称“一般 Hilbert 值有界有限 chaos 必连续”；
只使用标量 $f_m$ 的已证一致逼近，和对差的维数无关估计。

## 3. 从 Hilbert 值符号到实际算子列的维数无关界

### 3.1 Hilbert 值复化与纯联合酉膨胀

令 $g=(g_\ell)$ 是有限个次数至多 $q$ 的有限柱函数。
其多仿射符号是一个 Hilbert 值多项式。
R92 的 Lagrange 分齐次与实极化论证，只使用三角不等式和有限线性组合，故给
$$
\sup_{|z_j|\le R}\|(P_{g_\ell}(z))_\ell\|_{\ell^2}
\le K_q(R)\|g\|_{L^\infty(\ell^2)},
\tag{3.1}
$$
其中可取
$$
K_q(R)=A_q\sum_{\nu=0}^q\frac{(2R\nu)^\nu}{\nu!},
\quad A_q=\frac{(2q)^q}{q!}\ (q\ge1),\quad A_0=1,
\tag{3.2}
$$
并约定 $0^0=1$。
具体而言，实立方体内的多仿射值是顶点值的凸组合；
Lagrange 提取每个齐次分量给 $A_q$；
实极化给 $\nu^\nu/\nu!$，复化再给 $(2R)^\nu$。
所有步骤适用于 Hilbert 值，并与列数及位数无关。

记纯算子 $S_j=I-2E_j$，以及
$$
P_g^0=\sum_F\widehat g(F)S_F.
$$
把每个 $E_j$ 膨胀为 $L^2(\mathbb T)$ 上乘坐标酉算子的压缩，其所有非负幂都精确压缩；再取有限张量积。
对于列值多项式，这给从 $H$ 到 $H\otimes\ell^2$ 的精确压缩，而膨胀后的范数是相应列值符号的上确界。
由于 $|1-2z_j|\le3$，得到
$$
\boxed{
\left\|(P_{g_\ell}^0)_\ell\right\|_{B(H,H\otimes\ell^2)}
\le K_q(3)\|g\|_{L^\infty(\ell^2)}.
}
\tag{3.3}
$$
这使用的是实际独立张量膨胀，不是一般多变量收缩元组的不等式。

### 3.2 R88 的矩形放大：逐项证明相同常数

为与本稿的 $V_j$ 区分，把 R88 的未修正实际因子记为
$$
G_j=I-2N_j,\qquad S_j=I-2E_j.
$$
令
$$
\rho=2\sum_{j\ge0}\eta_j10^{j/2}<1,\qquad
W\chi_J=G_J1,\quad \|W-I\|\le\rho.
$$
R88 的低位截取算子 $Q_{j,K}$，$K\subset[0,j)$，满足
$$
\sum_{K\subset[0,j)}Q_{j,K}^*Q_{j,K}\le I.
\tag{3.4}
$$

设 $P:H\otimes\mathbb C^s\to H\otimes\mathbb C^r$ 的每个矩阵项属于纯交换代数。
对其逐项施加 R88 的有界乘法对应，实际公式为
$$
\begin{split}
\mathfrak F_{r,s}(P)
={}&\left[
P+\sum_{j\ge0}\sum_{K\subset[0,j)}
\bigl(G_K(G_j-S_j)\otimes I_r\bigr)
P\bigl(Q_{j,K}\otimes I_s\bigr)
\right](W^{-1}\otimes I_s).
\end{split}
\tag{3.5}
$$
固定 $j$，对任意输入 $h$，其内和的范数不超过
$$
2\eta_j\sum_K3^{|K|}
\|P(Q_{j,K}\otimes I_s)h\|
\le
2\eta_j10^{j/2}\|P\|
\left(\sum_K\|(Q_{j,K}\otimes I_s)h\|^2\right)^{1/2}.
$$
由 (3.4)，最后一项不超过 $2\eta_j10^{j/2}\|P\|\|h\|$。
故 (3.5) 按范数收敛，且
$$
\boxed{
\|\mathfrak F_{r,s}(P)\|
\le C_{\rm model}\|P\|,\qquad
C_{\rm model}=\frac{1+\rho}{1-\rho}.
}
\tag{3.6}
$$
常数与矩形大小 $r,s$ 无关。
这个证明没有在纯与实际混合因子间交换次序；它是原来排序望远镜公式的逐项放大。

取 $s=1$，(3.5) 的各项正是实际乘子 $X_{g_\ell}$，所以 (3.3)—(3.6) 给
$$
\boxed{
\left\|(X_{g_\ell})_\ell\right\|
\le C_{\rm model}K_q(3)\|g\|_{L^\infty(\ell^2)}.
}
\tag{3.7}
$$
无限列通过有限子列的上确界或上述一致逼近延拓；所得算子列仍满足同一界。

将 (2.6) 用于 $g=(D_Jf)_{|J|=k}$，得到关键实际列估计
$$
\boxed{
\left\|(X_{D_Jf})_{|J|=k}\right\|
\le
C_{\rm model}K_{d-k}(3)G_{d,k}\|f\|_\infty.
}
\tag{3.8}
$$
每个单独坐标 $X_{D_Jf}$ 属于 $\mathcal A$。
(3.8) 控制的是共同输入的整列，不是把各项范数作一个可能发散的和。

## 4. 局部莫比乌斯因子及 $\ell^2$ 行界

由唯一字符，(1.3) 分母的字符为 $e^z\ne0$。
因此它对每个 $z\in\mathbb C$ 都是 $\mathcal A$ 的实际单位，其逆为范数整函数。
于是 $R_j$ 整，且
$$
R_j(0)=V_j,\qquad \chi(R_j(z))=1.
\tag{4.1}
$$
直接使用交换因子相减，
$$
\Delta_j(z):=R_j(z)-V_j
=(I-V_j^2)\sinh z\,(\cosh z\,I+V_j\sinh z)^{-1}
=zK_j(z),
\tag{4.2}
$$
其中 $K_j$ 在 $z=0$ 的奇点可去。

固定 $a,b\in\ell^2$ 与 $T<\infty$，置 $c_j(t)=b_j+ta_j$。
高位 $c_j(t)$ 在 $|t|\le T$ 上一致趋于零。
用 $\|V_j\|\le6$，选固定小圆盘使
$$
\|(\cosh z-1)I+V_j\sinh z\|\le1/2.
$$
高位的逆范数因此不超过2，而 $(\sinh z)/z$ 与 $I-V_j^2$ 也一致有界。
余下有限低位只需在相应紧参数集上取实际逆的范数最大值。
由此得到有限常数 $C_T$，使
$$
\boxed{
\|\Delta_j(c_j(t))\|\le C_T|c_j(t)|
\quad(j\ge0,\ |t|\le T).
}
\tag{4.3}
$$
不要求一个对所有复 $z$ 的统一逆界。

对有限位集 $J$ 记
$$
\Delta_J(c)=\prod_{j\in J}\Delta_j(c_j).
$$
所有因子属于交换的 $\mathcal A$。
对应算子行从 $H\otimes\ell^2(\{|J|=k\})$ 到 $H$，满足
$$
\begin{split}
\|(\Delta_J(c))_{|J|=k}\|_{\rm row}
&\le\left(\sum_{|J|=k}\|\Delta_J(c)\|^2\right)^{1/2}\\
&\le C_T^k
\left(\sum_{|J|=k}\prod_{j\in J}|c_j|^2\right)^{1/2}\\
&\le\frac{C_T^k\|c\|_2^k}{\sqrt{k!}}.
\end{split}
\tag{4.4}
$$
这一步只用范数及标量 $\ell^2$，无需行因子彼此正交。

对 $k\ge1$，只保留触及 $j\ge m$ 的集合，则更有
$$
\sum_{\substack{|J|=k\\J\cap[m,\infty)\ne\varnothing}}
\prod_{j\in J}|c_j|^2
\le
\|c_{\ge m}\|_2^2\,
\frac{\|c\|_2^{2k-2}}{(k-1)!}.
\tag{4.5}
$$
所以这些尾行的范数对 $|t|\le T$ 一致趋零，因为
$\|c(t)_{\ge m}\|_2\le\|b_{\ge m}\|_2+T\|a_{\ge m}\|_2$。

## 5. 完整倾斜乘子、范数收敛与字符

定义
$$
\boxed{
\Phi_c(f)=
\sum_{k=0}^d\ \sum_{|J|=k}
\Delta_J(c)X_{D_Jf}.
}
\tag{5.1}
$$
$k=0$ 项为 $X_f$。
对每个 $k$，将 (3.8) 的实际列与 (4.4) 的行相乘，得到规范范数极限；
(4.5) 说明按有限物理位截断的和也收敛到此极限。
每个有限和属于 $\mathcal A$，故 $\Phi_c(f)\in\mathcal A$。
并且对前述紧参数族，
$$
\boxed{
\|\Phi_c(f)\|
\le
C_{\rm model}\|f\|_\infty
\sum_{k=0}^d
\binom dk K_{d-k}(3)(\sqrt3\,C_T\|c\|_2)^k.
}
\tag{5.2}
$$
这里利用了 $G_{d,k}/\sqrt{k!}=3^{k/2}\binom dk$。

有限 $J$ 项都对 $t$ 整。(4.5) 和 (3.8) 给局部一致范数收敛，因此
$$
\boxed{t\longmapsto\Phi_{b+ta}(f)\text{ 为 }\mathcal A\text{ 值整函数}.}
\tag{5.3}
$$
同一估计用于 $f-g$，证明该构造对固定 chaos 次数下的 $L^\infty$ 范数连续。

由 (4.1)，所有非空 $J$ 的 $\Delta_J$ 字符为零。
字符范数连续，所以
$$
\boxed{\chi(\Phi_c(f))=\chi(X_f)=f(0).}
\tag{5.4}
$$

若 $f$ 是有限柱，(5.1) 正是多仿射 Taylor 恒等式
$$
\Phi_c(f)
=\sum_F\widehat f(F)\prod_{j\in F}R_j(c_j).
\tag{5.5}
$$
导数索引只有互不相同的位；没有把普通有重复变量的 Taylor 系数错用到 Boolean 多仿射符号上。
一般 $f$ 的定义由 (5.1) 或有限柱一致极限得到，二者由 (5.2) 相同。

## 6. 指数向量上的真实作用

首先令 $f$ 为有限柱，$w$ 也有限截断，并取一个包含全部相关位的有限集合。
置
$$
T_j(z)=\cosh z\,I+V_j\sinh z.
$$
由 $V_J1=\chi_J$，
$$
e^w=e^{b_*}\prod_jT_j(b_j)1.
\tag{6.1}
$$
对一个位直接计算
$$
R_j(b_j)T_j(b_j)
=V_j\cosh b_j+I\sinh b_j.
$$
将这条等式用于 $f=\chi_F$，其余位因子不变，便得到
$$
\chi_F e^w
=\left(\prod_{j\in F}R_j(b_j)\right)e^w.
$$
线性相加并用 (5.5)，得到 (1.5) 的有限情形。

固定有限柱 $f$，让 $w_N\to w$。
复 Rademacher 指数的标准二次矩计算给 $e^{w_N}\to e^w$ 于 $H$；
这也是 R145/R147 已证的指数整向量结论。
当截断包含 $f$ 的支撑后，$\Phi_b(f)$ 不再随外部截断变化。
所以有界算子作用与有界点乘都允许取 $H$ 极限，得到 $f e^w=\Phi_b(f)e^w$。

对一般有界有限 chaos $f$，取 R92 的一致柱逼近 $f_m$。
(5.2) 给 $\Phi_b(f_m)\to\Phi_b(f)$ 于算子范数，而
$\|(f_m-f)e^w\|_2\le\|f_m-f\|_\infty\|e^w\|_2$。
故 (1.5) 完全成立。

R147 已证明任意这样的 $e^w$ 都循环。
若 $f(0)\ne0$，(5.4) 和 $\mathcal A$ 的单字符谱性质使 $\Phi_b(f)$ 为有界交换单位。
它把循环的 $e^w$ 送为 $f e^w$，证明 (1.6)。

## 7. 与第一阶整真空轨道的定义域衔接

给定第一阶 $u,w$，令
$$
\mathcal B(t)=\prod_jH(b_j+ta_j,V_j),\qquad
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z).
\tag{7.1}
$$
R145/R147 给这个乘积的算子范数整性、可逆性及字符1。
常数项 $a_*,b_*$ 保留在下面的指数向量中，不进入局部乘积。
置
$$
B_w=\mathcal B(0),\qquad
\mathcal V(t)=\mathcal B(t)^{-1}e^{tu+w},
\qquad \xi_w=\mathcal V(0)=B_w^{-1}e^w.
\tag{7.2}
$$
$\xi_w$ 循环。
更重要的是，已经核明真实自然幂域
$$
\mathcal V(t)\in\bigcap_{n\ge0}\operatorname{Dom}X^n,\qquad
X^n\mathcal V(t)=\partial_t^n\mathcal V(t),
\quad X=X_u.
\tag{7.3}
$$
这不是从向量形式级数自行假定的域结论。

定义
$$
M_f(t)=B_w^{-1}\mathcal B(t)\,\Phi_{b+ta}(f).
\tag{7.4}
$$
它是 $\mathcal A$ 值整函数，且
$$
M_f(0)=\Phi_b(f),\qquad \chi(M_f(t))=f(0).
\tag{7.5}
$$
由 §6 应用于指数 $tu+w$，
$$
\boxed{f e^{tu+w}=B_wM_f(t)\mathcal V(t).}
\tag{7.6}
$$
左边是 $H$ 值整函数：$f$ 有界，且 Rademacher 指数有全部局部一致矩界。
右边也是真正的范数解析乘积。

取 $k$ 次导数并用 (7.3)，
$$
\boxed{
u^k f e^w
=B_w\sum_{i=0}^k\binom ki
M_f^{(k-i)}(0)X^i\xi_w.
}
\tag{7.7}
$$
全部 $X^i\xi_w$ 都在真实自然域。
有界系数属于 $\{A\}'$，R125 的全交换子域交换使它们保持每个幂域，故有限重排没有未付清的乘法域。

## 8. 任意有界有限 chaos 系数及空谱逆

取 $f_0,\ldots,f_p$，对每个 (7.7) 求和。
定义有界系数
$$
C_i=\sum_{k=i}^p\binom ki M_{f_k}^{(k-i)}(0)
\in\mathcal A,\qquad 0\le i\le p.
\tag{8.1}
$$
则
$$
\boxed{
\left[\sum_{k=0}^pu^kf_k\right]e^w
=B_wP(X)\xi_w,\qquad
P(X)=\sum_{i=0}^pC_iX^i
\text{ 于 }\operatorname{Dom}X^p.
}
\tag{8.2}
$$
由 (7.5)，
$$
C_p=\Phi_b(f_p),\qquad
\chi(C_i)=f_i(0)\quad(0\le i\le p).
\tag{8.3}
$$
于是 $f_p(0)\ne0$ 时 $C_p$ 是实际有界交换单位。

现在只使用 $X$ 空谱。令 $R=X^{-1}$，则 $R$ 为有界交换子且拟幂零。
为重述后一个事实：对每个 $\lambda$，$X-\lambda$ 都有有界逆，而
$(X-\lambda)R=I-\lambda R$；
相反方向的真实逆关系给 $I-\lambda R$ 在全 $H$ 可逆。
故 $\sigma(R)\subseteq\{0\}$。

因为 $X$ 满射且真逆为 $R$，有限归纳给
$$
\operatorname{Dom}X^p=\operatorname{Ran}R^p,\qquad
X^p=(R^p)^{-1}.
\tag{8.4}
$$
特别 $X^p$ 闭、单射且满射，不是任意闭算子幂的无条件断言。

置 $D_i=C_p^{-1}C_i$，$i<p$，以及
$$
U=I+\sum_{i=0}^{p-1}D_iR^{p-i}.
\tag{8.5}
$$
全部因子属于交換的 $\{A\}'$。
$U-I=RZ$，其中 $Z$ 是有界且与 $R$ 交换的有限和。
因此
$\|(RZ)^n\|^{1/n}\le\|R^n\|^{1/n}\|Z\|\to0$，$U$ 为有界单位。
在 (8.4) 的准确域上，
$$
\boxed{
P(X)=C_pUX^p,\qquad
P(X)^{-1}=R^pU^{-1}C_p^{-1}\in\{A\}'.
}
\tag{8.6}
$$
右边的逆在全 $H$ 有界；$P(X)$ 作为自然 $p$ 次幂域上的算子已经闭。
不需要另行给点态高阶函数构造一个最大闭乘子。

令 $F=\sum_{k=0}^pu^kf_k$。由 (8.2)、(8.6)，
$$
\boxed{
\xi_w=P(X)^{-1}B_w^{-1}[F e^w].
}
\tag{8.7}
$$
右侧左乘算子为有界交换子，因而保持 $\operatorname{cyc}_A(F e^w)$。
该循环空间包含循环向量 $\xi_w$，故是全 $H$。
这证明 (1.9)，并同时证明目标向量不可能为零。

将 $f_0$ 换成 $f_0-\lambda$ 不改变最高 $f_p$，因为 $p\ge1$。
重复同一实际逆论证，得到 (1.10)。
$p=0$ 的对应结论是 §6 的 $f_0(0)\ne0$；此时减去标量必须另外检查字符，没有混入“所有 $\lambda$”的断言。

## 9. 无限秩有界系数的例子

R88 的互不交 Hadamard 块给一个连续有界二阶函数
$$
q=\sum_{n\ge1}\left[q_n-q_n(0)\right],\qquad q(0)=0,
$$
其中两侧各有 $N_n=2^{4n}$ 个位，
$$
q_n=2^{-n}N_n^{-3/2}
\sum_{x,y\in\{0,1\}^{4n}}(-1)^{x\cdot y}
\chi_{i_{n,x}}\chi_{j_{n,y}}.
\tag{9.1}
$$
各块互不相交。
Hadamard 矩阵的算子范数为 $\sqrt{N_n}$，故 $\|q_n\|_\infty\le2^{-n}$，
而 $q_n(0)=2^{-n}/\sqrt{N_n}$。
所以级数一致收敛，$q$ 有界且二阶。
其 Walsh 系数绝对值总和为
$$
\sum_n2^{-n}\sqrt{N_n}=\infty.
$$
因此本稿的列估计确实覆盖绝对系数和法不能处理的函数。

令 $g=1+q$，则 $g(0)=1$。
任取有界有限 chaos $h,k$、任意复杂 $\ell^2$ 第一阶 $w$，并取
$$
u=\sum_{j\ge0}\frac{\chi_j}{j+1}.
$$
系数正、属于 $\ell^2$ 而不属于 $\ell^1$，所以 $X_u$ 空谱。于是
$$
\boxed{
\left[u^2(1+q)+uh+k-\lambda\right]e^w
\text{ 对每个 }\lambda\in\mathbb C\text{ 循环}.
}
\tag{9.2}
$$
所有支撑可以重叠，不需把系数符号拆成独立坐标块后再与 $u,w$ 分离。
Hadamard 块只用于给出一个可检查的有界无限秩系数例。

## 10. 准确边界

本稿构造 $\Phi_c(f)$ 对全部有界有限 chaos 都成立，但 $\chi(\Phi_c(f))=f(0)$。
因此一般 $f(0)=0$ 时不能仅凭其属于 $\mathcal A$ 推出核排除；本稿没有把这一未知情形改写成已解决。

空谱锚结论依赖最高系数 $f_p(0)\ne0$，其作用正是提供真实有界单位。
若最高字符为零，(8.5) 的首一化不能照搬。
一般慢复杂模式的共振、两个无型控制的临界无限行、任意 $H$ 向量和完整 ISP 仍开放。

主要内部依赖：
R88 的排序乘法对应，R92 的标量有界有限 chaos 连续性，
R125 的第一阶闭乘子及全交换子域交换，
R134/R138 的空谱逆，以及 R145/R147 的实际指数整轨道和域。
本稿新增的梯度、矩形放大、行列收敛、一般符号倾斜和空谱多项式系数机制均在正文给出完整证明。
