# R457 — 原六 sigma 的完整五输入核心、四伴随与真实同深非零管

日期：2026-11-14。**状态：已证明。**

把原 $H_{33}=S/\sigma$ 的五个 sigma 输入全部保留，作一个行列式
为 $114114$ 的明确正交变换。五个输出的 theta degree 为
$33,84,1596,3458,6006$。在 R454 已经固定的同一个 ray 上，
五条实际核心在这个完整联合来源上依次为
$$
\boxed{\chi\lambda,\ -\lambda,\ -\lambda,\ -\lambda,\ \chi\lambda.}
$$
不增加素数同余条件。第一条核心改变原中央变量 $Y$，同时严格
保留四个真实伴随；其逆变换给出每个原 sigma 输入的准确移动。

用 R455 的同一纯伴随算术测试，并支付 $-1/84$ 与 $-2/3$ 的归一，
得到原六 sigma 表示中的完整中央返回。四个伴随都深 $n$ 的完整
行是 $(-\chi)^n\lambda^{4n}J'_S(0)$；其中五个原 sigma 输入
都深 $n$、第六个输入单位的真实子域，对每个 $n\ge1$ 恰有
赋值 $5n$。这是未展开的原六 sigma 联合，不把残余表示的隐藏
条件当作原输入条件。

该大域中 $Z\notin p^n$ 的补域仍保留；本文没有从局部非零推出
完整中央非零，主目标未完成。

## 1. 同一个原六 sigma 来源及全部常数

使用 R454/R455 的 $b=17$、原 sigma、普通周期 $\Omega$、
固定 ray 及实际符号
$$
\pi_0\equiv1428552127+2161889730\omega
       \pmod{2793510720},
\qquad
\lambda=-\bar\pi_0^{-1},\quad
\lambda_\sigma=-\lambda,\quad
\kappa=p/\bar\pi_0^2,\quad
\chi=\chi_p\in\{1,-1\}.
\tag{1}
$$
$\chi$ 仍是原奇 degree33 trace 的实际符号。当前 $p>19$、
$p\equiv7\bmod64$；特别 $p\ge71$。下文使用 R455 的固定有限
坏集 $\mathcal E$ 时会明确说明。

取
$$
\delta=1+2\omega,\qquad
\gamma_7=3+\omega,\qquad\bar\gamma_7=2-\omega,
$$
$$
(a_1,a_2,a_3,a_4,a_5)
=(2,\delta,2\delta,\gamma_7,\bar\gamma_7),\qquad
(n_1,\ldots,n_5)=(4,3,12,7,7).
\tag{2}
$$
准确有 $\prod_i a_i=-84$。原函数恒等式为
$$
\boxed{
H_{33}(z)=\frac{S(z)}{\sigma(z)}
=-\frac1{84}\prod_{i=1}^5\sigma(a_i z),\qquad
S(z)=-\frac1{84}\sigma(z)\prod_{i=1}^5\sigma(a_i z).
}
\tag{3}
$$
所以 $H_{33}(z)=z^5+O(z^{11})$。

令 $\xi_1,\ldots,\xi_5$ 为五个同一原 sigma 测度的独立物理输入，
写 $t_i=a_i\xi_i$，并记
$$
\nu_5=-\frac1{84}\bigotimes_{i=1}^5[a_i]_*\nu_\sigma,\qquad
\rho_S=\nu_\sigma(c)\otimes\nu_5.
\tag{4}
$$
这里 $\nu_5$ 是五变量联合；只有沿 $Z=\sum_i t_i$ 推前后才是
$\nu_{H_{33}}$。原第六个独立 sigma 输入为 $c$。完整总和
$$
\boxed{Z=\sum_{i=1}^5t_i,\qquad Y=Z+c}
\tag{5}
$$
满足 $Y_*\rho_S=\nu_S$。

每个 $a_i$ 在当前普通处都是单位，所以
$t_i\in p^n$ 与 $\xi_i\in p^n$ 完全等价。下文不忘却这些五个
独立输入后再倒推它们的条件。

## 2. 完整五输入的正交格与半特征

定义四个物理伴随
$$
\begin{aligned}
R_1&=3t_1-4t_2,\\
R_2&=12t_1+12t_2-7t_3,\\
R_3&=7t_1+7t_2+7t_3-19t_4,\\
R_4&=7t_1+7t_2+7t_3+7t_4-26t_5.
\end{aligned}
\tag{6}
$$
令 $D=\operatorname{diag}(4,3,12,7,7)$ 及
$$
C=
\begin{pmatrix}
1&3&12&7&7\\
1&-4&12&7&7\\
1&0&-7&7&7\\
1&0&0&-19&7\\
1&0&0&0&-26
\end{pmatrix}.
$$
生成变量满足 $(z_1,\ldots,z_5)^{\mathsf t}
=C(z,r_1,\ldots,r_4)^{\mathsf t}$；
物理输出则为 $(Z,R_1,\ldots,R_4)^{\mathsf t}
=C^{\mathsf t}(t_1,\ldots,t_5)^{\mathsf t}$。
直接整矩阵计算给
$$
\boxed{
C^{\mathsf t}DC=\operatorname{diag}(33,84,1596,3458,6006),\qquad
\det C=7\cdot19\cdot26\cdot33=114114.
}
\tag{7}
$$
其素因子只有 $2,3,7,11,13,19$，当前均已排除。因此这是同一
$\mathbf Z_p^5$ 上的整可逆变换，所有输入条件均有准确逆像。

完整来源为
$$
\boxed{
\mathcal B(z,\mathbf r)
=-\frac1{84}
 \prod_{i=1}^5
 \sigma\!\left(a_i\left(z+\sum_{j=1}^4C_{ij}r_j\right)\right).
}
\tag{8}
$$
由 (7) 所有交叉 Hermitian 项为零。还需支付半特征，而不能只
用 Gram 对角化。原 sigma 半特征是
$\epsilon(m+n\omega)=(-1)^{m+n+mn}$，在三个非零模二类均为负。

对 $z$ 轴，五个系数模二有三个非零，所以其半特征恰为原
$\sigma^{33}$ 的奇半特征。对四个 $r_j$ 轴，逐列的半特征乘积
均为一：前两列的所有 sigma 系数为偶数，后两列分别恰有两个
非零模二系数。$\omega$ 乘法保持原半特征，故不存在遗漏的
平坦 twist。因此
$$
\boxed{
\mathcal B\in
\mathcal S_{33}^{\rm odd}\boxtimes
\mathcal S_{84}\boxtimes\mathcal S_{1596}
\boxtimes\mathcal S_{3458}\boxtimes\mathcal S_{6006}.
}
\tag{9}
$$
它属于完整张量格，不是只属于若干低阶 jet 的形式空间。
确切地，(8) 是原整测度在 (7) 的整可逆物理变换下的来源；
各 $\sigma^N x^j,\sigma^N yx^j$ 合法基在原形式群坐标中有互异
首阶和单位首系数，依首阶消元即得各轴整系数。有限 Künneth
分解因而位于显示的整张量格。特别
$\mathcal B(z,\mathbf0)=H_{33}(z)\ne0$。

## 3. 当前 ray 上的完整中心及三条绝对锚

所有轴都使用原同一个完整 trace 规范
$$
K_N=\frac{\bar\pi_{17}}p\mathscr M_{\pi_{17}},\qquad
\nu_F|_{p\mathbf Z_p}
=\lambda[\kappa]_*\nu_{K_NF}.
\tag{10}
$$
原 odd degree33 的定义与中心规范见 R454；偶 degree 的完整
Heisenberg lift 见 R413/R431。计算 $g=\pi_0/\bar\pi_0$，当前固定
ray 已经给出下表，包含 $\omega$ 系数和完整 $2N$ 中心模数：

| $N$ | $g\bmod 2N$ | 完整交织的形状 |
|---:|---:|---|
| $33$ | $1$ | 原奇空间的标量 |
| $84$ | $43=1+N/2$ | 二挠平均 |
| $1596$ | $2395=1+3N/2$ | 同一二挠平均 |
| $3458$ | $3459=1+N$ | 标量 |
| $6006$ | $6007=1+N$ | 标量 |

这些都是实整数代表，$\omega$ 系数为零。用
$Xe_j=\zeta_N^je_j,\ Ze_j=e_{j+1}$ 的完整规范，交织为
$X\mapsto X^g,\ Z\mapsto Z^g$，没有被抹去的交叉周期相位。
特别后两条确实与整个 Heisenberg 表示交换，因而是整个空间
上的标量。第一条已由 R454 绝对支付为
$$
\boxed{K_{33}=\chi I,\qquad \chi^2=1.}
\tag{11}
$$

### 3.1 两个完整二挠平均

对 $N=84,1596$，都有 $N\equiv4\bmod8$。
取 $t=(s+r\omega)/2$，$s,r\in\{0,1\}$。原对称 lift 是
$$
T_t^{(N)}e_j=(-1)^{s(r+j)}e_{j+Nr/2}.
\tag{12}
$$
其中 $(-1)^{sr}$ 是 $N/4$ 为奇数所给的中心相位。对 $s$ 求和
只保留 $r\equiv j\bmod2$，故整个空间上
$$
\boxed{
D_N:=\frac12\sum_{t\in E[2]}T_t^{(N)},\qquad
D_Ne_j=e_{(1+N/2)j},\qquad D_N^2=I.
}
\tag{13}
$$
$2395$ 与 $1+1596/2$ 相差一个 $N$，所以在两个 Heisenberg
生成元上给同一个完整交织。

取 $\gamma_{19}=5+2\omega$，$N\gamma_{19}=19$，并设
$$
\alpha_{84}=\delta\gamma_7,\qquad
\alpha_{1596}=\delta\gamma_7\gamma_{19}.
$$
两者范数分别为 $21,399$。实际锚
$$
A_N(z)=\sigma(2\alpha_Nz)\in\mathcal S_N
\tag{14}
$$
对每个非零二挠点的完整 lift 都等于 $-A_N$，因为
$2\alpha_Nt$ 为模二非零的格点。因此 $D_NA_N=-A_N$。
原 sigma 核心是 $-\lambda$，而 $2\alpha_N$ 为当前普通单位，
所以真实 $K_NA_N=-A_N$。完整不可约交织的标量遂被确定：
$$
\boxed{K_{84}=D_{84},\qquad K_{1596}=D_{1596}.}
\tag{15}
$$

### 3.2 整个 degree3458 的绝对标量

令 $\gamma_{13}=4+\omega$，取
$$
\alpha_{3458}=\gamma_7\gamma_{13}\gamma_{19},
\qquad N\alpha_{3458}=7\cdot13\cdot19=1729.
$$
实际非零锚为
$$
A_{3458}(z)=\Theta(\alpha_{3458}z)\in\mathcal S_{3458}.
\tag{16}
$$
R426 用原 $\Theta(3z)$ 支付了 $\Theta$ 的完整核心 $-\lambda$；
$3$ 和 $\alpha_{3458}$ 在当前处都可逆，所以此处的尺度拉回
与限制、推前严格交换。因而真实
$K_{3458}A_{3458}=-A_{3458}$。结合表中的完整标量交织，得到
$$
\boxed{K_{3458}=-I\quad\text{于整个 }\mathcal S_{3458}.}
\tag{17}
$$
这里没有从质量或未知中央导数确定符号。

## 4. 同一完整五 sigma 来源上的五个核心

先看 (15) 在完整联合 $\mathcal B$ 上的作用。
$r_1$ 平移 $t=\ell/2$ 时，发生周期移动的两个 sigma 系数为
$6t=3\ell$ 与 $-4\delta t=-2\delta\ell$。完整半特征乘积为
$\epsilon(\ell)$，所以对每个非零 $t\in E[2]$，
$$
T_{t,r_1}^{(84)}\mathcal B=-\mathcal B.
$$
$r_2$ 平移的三个系数为 $24t=12\ell$、
$12\delta t=6\delta\ell$、$-14\delta t=-7\delta\ell$，
同样恰有一个负半特征。所有额外变量的指数项都因 (7) 的
正交性消掉。因此这些是完整联合身份，保留 $z$ 和其余所有
$r_j$，并非只在原点或边际成立。代入 (13)：
$$
\boxed{
K_{84,r_1}\mathcal B=-\mathcal B,\qquad
K_{1596,r_2}\mathcal B=-\mathcal B,\qquad
K_{3458,r_3}\mathcal B=-\mathcal B.
}
\tag{18}
$$

最后一个完整算子先写成 $K_{6006}=\zeta_pI$；其标量尚未选择。
五个原 sigma 输入同时深一层的实际系数为
$\lambda_\sigma^5=-\lambda^5$。
由 (7)，同一个域恰是 $Z,R_1,\ldots,R_4$ 同时深一层。
五个完整轴核心可交换，(11)、(18) 给它的系数为
$$
\lambda^5\chi(-1)^3\zeta_p=-\lambda^5\chi\zeta_p.
$$
同一个非零联合 $\mathcal B$ 在全部坐标同时缩放后仍非零，
所以可准确比较并消去，得到 $\chi\zeta_p=1$。由 $\chi^2=1$：
$$
\boxed{K_{6006}=\chi I\quad\text{于整个 }\mathcal S_{6006}.}
\tag{19}
$$
这是一个保留全部五输入的实际非零锚，未用五个边际相互替代。

合并起来，同一原五 sigma 联合在五轴上的特征值准确为
$$
\boxed{(K_{33},K_{84},K_{1596},K_{3458},K_{6006})\mathcal B
=(\chi,-1,-1,-1,\chi)\mathcal B.}
\tag{20}
$$
这里 (20) 的五个等式分别指对应轴的作用。

## 5. 真实输入的完整运输，而不只总和边际

记 $v_j$ 为 $C$ 的第 $j$ 列，$j=0,\ldots,4$；
$L_j=(33,84,1596,3458,6006)_j$。令
$$
E_j=\frac{Dv_jv_j^{\mathsf t}}{L_j},\qquad
P_j=I+(\kappa-1)E_j.
\tag{21}
$$
(7) 严格给
$$
E_j^2=E_j,\quad E_iE_j=0\ (i\ne j),\quad
\sum_jE_j=I.
$$
所以 $P_j$ 恰将第 $j$ 个物理输出乘 $\kappa$，保留其余四个
输出。它的行列式为 $\kappa$，像恰为第 $j$ 个输出深一层的整域。
由 (10)、(20) 得完整联合测度式
$$
\boxed{
\nu_5|_{Z\in p}=\chi\lambda(P_0)_*\nu_5,\quad
\nu_5|_{R_j\in p}=-\lambda(P_j)_*\nu_5\ (1\le j\le3),\quad
\nu_5|_{R_4\in p}=\chi\lambda(P_4)_*\nu_5.
}
\tag{22}
$$
每式保任意完整五输入测试，外部独立 $c$ 也原样保留。

特别第一式的真实输入变化十分明确：
$$
\boxed{
t_i\longmapsto t_i+\frac{\kappa-1}{33}n_iZ,\qquad
\xi_i\longmapsto \xi_i+\frac{\kappa-1}{33}\bar a_iZ,\qquad
c\longmapsto c.
}
\tag{23}
$$
它保全部 $R_j$，将 $Z$ 变为 $\kappa Z$，从而将
$Y=c+Z$ 真正变成 $c+\kappa Z$。此式不保持原中央测试；
使用它时，$\log\langle Y\rangle$ 及任何附加域都必须按 (23)
完整转置。迭代 $n$ 次只需将 $\kappa-1$ 换成 $\kappa^n-1$。

对任意非负深度 $(r_0,\ldots,r_4)$，可交换的完整式准确给
$$
\boxed{
\nu_5|_{Z\in p^{r_0},\,R_j\in p^{r_j}}
=\chi^{r_0+r_4}(-1)^{r_1+r_2+r_3}
 \lambda^{r_0+\cdots+r_4}
 \left(\prod_{j=0}^4P_j^{r_j}\right)_*\nu_5.
}
\tag{24}
$$
所有原 $t_i$ 条件都要按显示的矩阵保留；没有将每个输出深度
和每个原输入深度分别相认。唯一准确的共同深度等价是
$$
\boxed{
t_1,\ldots,t_5\in p^n
\iff Z,R_1,\ldots,R_4\in p^n.
}
\tag{25}
$$

## 6. R455 算术测试的原六 sigma 归一

沿用 R455 的完整纯伴随
$$
T_c=Z-33c
$$
及其固定多项式 $\mathfrak h_b$、单位修正
$\mathfrak h_{b,p}^{\times}$。其六个系数、原周期和固定有限坏集
$\mathcal E=\{p:p\mid17LN_\alpha\}$ 都直接采用 R455
(17)–(20)、(24)、(35)–(36)，不改换来源。

必须区别两个整体归一：R455 忘却残余 $T$ 后的来源是
$$
F(y,t)=-\frac23\sigma(y-33t)H_{33}(y+t),
$$
而 (4) 的原六 sigma 联合没有这个 $-2/3$。因此在原
$\rho_S$ 上定义准确测试
$$
\boxed{
\mathfrak h_b^{S}=-\frac23\mathfrak h_b,\qquad
\mathfrak h_{b,p}^{S,\times}
=-\frac23\mathfrak h_{b,p}^{\times}.
}
\tag{26}
$$
由 R455 已付的整个来源身份，而非只一个中央值，
$$
\boxed{
Y_*\{\mathfrak h_b^S(T_c/\Omega)\rho_S\}=\nu_S,\qquad
Y_*\{\mathbf1_{T_c\ {\rm unit}}\,
       \mathfrak h_{b,p}^{S,\times}(T_c/\Omega)\rho_S\}=\nu_S.
}
\tag{27}
$$
(3)、(4)、(26) 一起支付所有 $-1/84$、$-2/3$ 常数。

四个 $R_j$ 核心都保 $Z,c,Y,T_c$。因此 (24)、(27) 给对整个
principal 参数 $u$ 的身份
$$
\boxed{
\int_{\substack{R_1,\ldots,R_4\in p^n\\Y,T_c\ {\rm unit}}}
 \langle Y\rangle^{du}
 \mathfrak h_{b,p}^{S,\times}(T_c/\Omega)\,d\rho_S
=(-\chi)^n\lambda^{4n}J_S(u),\qquad d=p-1.
}
\tag{28}
$$
更一般的四个独立伴随深度由 (24) 同样给出准确系数。
所以 $J'_S(0)=0$ 确实使 (28) 的完整中央为零。这里已经保住
原五 sigma 隐藏输入，而不是仅将 $H_{33}$ 边际的结论反向宣称
为完整联合式。

## 7. 未展开原六 sigma 中的每层真实非零域

取真正的原输入域
$$
\boxed{
\mathscr D_n^{(6)}
=\{\xi_1,\ldots,\xi_5\in p^n,\ c\ {\rm unit}\}
=\{Z,R_1,\ldots,R_4\in p^n,\ c\ {\rm unit}\},
\quad n\ge1.
}
\tag{29}
$$
这个域已有 $Y,T_c$ 单位，故位于 (28) 的大域中。

记其在 (26) 的同一实际测试下的中央值为
$$
\mathcal C_n^{(6)}
=\int_{\mathscr D_n^{(6)}}
 d\log_p\langle Y\rangle\,
 \mathfrak h_{b,p}^{S,\times}(T_c/\Omega)\,d\rho_S.
\tag{30}
$$
令 $\mathcal A_p^\times(T_0)$ 为 R455 (28) 的完整函数，只将测试
换为其 (24) 的单位修正。按五个独立原 sigma 核心，(26) 中的
归一准确给
$$
\boxed{
\mathcal C_n^{(6)}
=(-\lambda)^{5n}\mathcal A_p^\times(\kappa^n).
}
\tag{31}
$$
这个式子保留所有 log 加权正矩。没有使用固定负五次矩非零。

R455 的同深残余管值为
$\mathcal C_n^\times=(-\eta)^n\lambda^{2n}
\mathcal A_p^\times(\kappa^n)$，所以两个实际来源表示的值有明确关系
$$
\boxed{
\mathcal C_n^{(6)}
=(\eta\lambda^3)^n\mathcal C_n^\times.
}
\tag{32}
$$
它是计算后的值关系；不声称两个表示的隐藏域是同一个集合。

R455 已完整支付 $\mathcal A_p^\times$ 的首五阶、高尾及所有
六个正 sigma 矩、log 矩。删去同一个固定有限坏集
$\mathcal E$ 后，其第五系数为单位、此前全部为零。
由 (31)，得到
$$
\boxed{
v_p(\mathcal C_n^{(6)})=5n
\quad\text{对当前 ray 上每个 }p\notin\mathcal E,\quad n\ge1.
}
\tag{33}
$$
这里是真正的未展开原六 sigma 表示 $m=0$，固定次数三十六
的算术测试。没有把 R429 的 $m>0$ 带二次权 Theta 展开与这个
五输入格混同；若改动那五个 sigma 的尺度或保留新增原输入，
必须重新运输其完整来源。

## 8. 精确保留的一个补域与可继续使用的混合 Y 接口

定义同一个原联合中的补域
$$
\boxed{
\mathscr E_n^{(6)}
=\{R_1,\ldots,R_4\in p^n,\ Y,T_c\ {\rm unit},\
Z\notin p^n\}.
}
\tag{34}
$$
由 (25)，(28) 的大域准确不交分拆为
$\mathscr D_n^{(6)}\sqcup\mathscr E_n^{(6)}$。因此
$$
\boxed{
(-\chi)^n\lambda^{4n}J'_S(0)
=\mathcal C_n^{(6)}
+\int_{\mathscr E_n^{(6)}}d\log_p\langle Y\rangle\,
       \mathfrak h_{b,p}^{S,\times}(T_c/\Omega)\,d\rho_S.
}
\tag{35}
$$
原中央为零只使第二项准确抵消第一项，本文未排除这种抵消。

新的可用内容是 (22)–(24) 在原五个独立 sigma 输入上的完整
运输。特别 (23) 真的改变 $Y$，而且不丢任何 $R_j$ 或原输入
条件；与原独立 $c$ 的核心、反射或四 sigma 恒等式组合时可以
从这个同一联合出发。只在 $Z,c$ 边际成立的等式，若未保这些
$R_j$，仍不能反向作用于 (29)、(34)。

## 精确证书与依赖

[精确脚本](../scripts/check-r457-five-sigma-full-companion-core.py)
逐项计算整个 Gram、行列式、原半特征、两个二挠 lift、当前
$2N$ 中心代表、三条实际锚的范数及五个完整投影矩阵。
[完整有理数据](../scripts/check-r457-five-sigma-full-companion-core.json)
保留所有这些量。它是固定代数身份的证书，不是目标素数扫描；
完整 trace 与非零结论的证明在正文。

- [R454：原 odd33 完整核心和实际符号](R454-original-odd33-core-and-exact-residual-slope-transport.md)。
- [R455：同一个纯伴随算术测试及全部首五阶](R455-original-pure-companion-test-and-slope-core-arithmetic-return.md)。
- [R431：完整偶 degree 二挠 lift 与绝对 sigma 锚](R431-original-degree52-full-core-and-fixed-thirteen-ray.md)。
- [R426：原 Theta 核心与 degree18 完整规范](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R429：原六 sigma 表示及更高 Theta 展开的准确边界](R429-original-two-depth-grid-and-reciprocal-sigma-nonvanishing.md)。

