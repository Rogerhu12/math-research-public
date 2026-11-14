# R230 工作稿：固定正常正态可同时压低全部实际交换子右测试的多行整函数增长

日期：2026-11-13 UTC。作者：normal_complex / Astra-ISP-0c017065；central_review 提出并独核固定数目窗与软窗，root 提供实际逐位近交换投影；AI 辅助：GPT-6 Astra Pro；根全文核验，central_review 独核全篇。

状态：下文给完整实际模型证明。它审计一条拟用的增长下界：仅凭正常性、正秩一，甚至有界且几乎处处严格正的原函数，并不能迫慢 first 的正常泛函增长超过快类的 $\log^{4/3}$ 尺度。原联合慢行的准确零式仍是额外条件；本文没有构造湮灭者或未知不变空间。

## 1. 同一个固定正态与主定理

固定
$$
\frac32<\alpha<3,\qquad s=\frac{\alpha}{3}\in\left(\frac12,1\right).
\tag{1.1}
$$
在原 Haar 空间 $H=L^2(\mathbb Z_2,\mu)$ 中，存在一个下文明确构造的固定向量 $h=h_\alpha$，满足
$$
\boxed{
\|h\|_2=1,\qquad h\in L^\infty,\qquad h>0\ \text{a.e.},
\qquad Ch=h.
}
\tag{1.2}
$$
这里不声称 $h$ 有统一严格正下界或连续。

沿用原实际
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
N_j^2=\eta_jI_j\otimes N_{j+1},\qquad
\|N_j\|\le1,
$$
$$
0<\eta_j\le e^{-770\,16^j},\qquad
V_j=(I-N_j)(I+N_j)^{-1},\qquad Q_j=V_j-I.
\tag{1.3}
$$
每个 $N_j,V_j$ 都属于 $\mathcal A$ 并相互交换；全部实际 $\mathfrak C=A'$ 右测试与它们交换。

给定任意有限个实际行
$$
T_\nu=\sum_{j\ge0}
\left(u_{\nu j}N_j+v_{\nu j}Q_j+w_{\nu j}Q_j^2\right),
\quad1\le\nu\le d,
\tag{1.4}
$$
假设对某个 $\beta>0$ 和有限 $C_\nu\ge0$，
$$
|u_{\nu j}|+6|v_{\nu j}|+36|w_{\nu j}|
\le C_\nu e^{-\beta j^\alpha}.
\tag{1.5}
$$
这些级数在算子范数中绝对收敛，故各 $T_\nu\in\mathcal A$。
其系数可以为复数。

令 $\phi_h(F)=\langle Fh,h\rangle$，这是迹一正秩一正常态。
则存在只依当前有限族、$\alpha,\beta$ 的常数 $C<\infty$，使
$$
\boxed{
\left\|
F\longmapsto
\phi_h\!\left(e^{\sum_{\nu=1}^d z_\nu T_\nu}F\right)
\right\|_{\mathfrak C_*}
\le
\exp\!\left[
C\left(\log\!\left(2+\sum_{\nu=1}^d|z_\nu|\right)\right)^{4/3}
\right]
}
\tag{1.6}
$$
对所有复 $z_1,\ldots,z_d$ 成立。

范数中的上确界针对原完整 $\mathfrak C$ 单位球，不只为有限多项式或纯比较代数。
同一个 $h_\alpha$ 适用于全部满足 (1.5) 的有限族；常数不要求对族统一。

特别，可同时取
$$
a_j=e^{-\beta j^\alpha},\qquad
c_j=a_j^\kappa\mathbf1_{j>j_0},\quad\kappa>0,
$$
$$
P_a=\sum_ja_jN_j,\qquad
X=\sum_ja_jQ_j,\qquad
Y=\sum_jc_jQ_j,\qquad
B_0=\sum_ja_j^2Q_j^2.
\tag{1.7}
$$
若 $\kappa<1$，把公共包络中的 $\beta$ 换成 $\kappa\beta$ 即可。
因此两条慢行及其实际局部二阶修正可以在同一个正正常态中同时具有 (1.6)。

证明分开支付：固定正常向量、纯窗压缩、任意实际右测试的全尾比较、实际 head 和所有 carry。纯窗从未被称为原 $A$ 的不变旗。

## 2. 一个实际四次幂预算

若 $n\ge2$，取整数 $\ell\ge1$ 使 $2^\ell\le n<2^{\ell+1}$。
反复使用 (1.3)，有准确等式
$$
N_j^{2^\ell}
=
\left(\prod_{r=0}^{\ell-1}
\eta_{j+r}^{\,2^{\ell-1-r}}\right)
I_{[j,j+\ell)}\otimes N_{j+\ell}.
\tag{2.1}
$$
所以
$$
\begin{aligned}
\|N_j^n\|
&\le\|N_j^{2^\ell}\|\\
&\le
\exp\!\left[
-\frac{770}{14}\,16^j(16^\ell-2^\ell)
\right]\\
&\le \exp(-3\,16^j n^4).
\end{aligned}
\tag{2.2}
$$
最后使用 $16^\ell-2^\ell\ge(7/8)16^\ell$、
$n^4<16\cdot16^\ell$，且 $(770/14)(7/8)/16>3$。
不对 $n=1$ 使用该界。

由
$$
(I+N_j)^{-1}=(I-N_j)(I-N_j^2)^{-1}
$$
可取 $\|(I+N_j)^{-1}\|\le3$。
于是
$$
Q_j=-2N_j(I+N_j)^{-1},\qquad
\|Q_j^2\|\le36\eta_j,
$$
$$
\|N_j-E_j\|\le\eta_j,\qquad
\|Q_j+2E_j\|\le8\eta_j.
\tag{2.3}
$$
后一式可直接由
$Q_j=-2N_j+2N_j^2(I+N_j)^{-1}$ 得到。

对于 $z=(z_1,\ldots,z_d)$，置
$$
q=\sum_\nu C_\nu|z_\nu|,\qquad
x=\log(2+q),\qquad a_j=e^{-\beta j^\alpha},
$$
$$
Z_j=\sum_\nu z_\nu
\left(u_{\nu j}N_j+v_{\nu j}Q_j+w_{\nu j}Q_j^2\right).
\tag{2.4}
$$
可准确写成 $Z_j=N_jB_j$，其中 $B_j$ 与 $N_j$ 交换，且
$$
\|B_j\|\le q a_j.
\tag{2.5}
$$
其纯一次比较为
$$
D_j=\xi_jE_j,\qquad
\xi_j=\sum_\nu z_\nu(u_{\nu j}-2v_{\nu j}),
$$
满足
$$
|\xi_j|\le q a_j,\qquad
\|Z_j-D_j\|\le2q a_j\eta_j.
\tag{2.6}
$$
$Z_i,Z_j$ 两两交换，$D_i,D_j$ 也两两交换；不要求混合的 $Z_i,D_j$ 交换。

### 2.1 实际指数的全域与有限头界

记 $r_j=q a_j$、$L_j=\max(0,\log r_j)$。
(2.2)--(2.5) 给
$$
\|e^{Z_j}\|
\le1+r_j+\sum_{n\ge2}r_j^ne^{-3\,16^jn^4}.
$$
对 $n,L\ge0$，
$$
nL-3\,16^jn^4
\le16^{-j/3}L^{4/3}-\frac32\,16^jn^4.
$$
且
$$
\sum_{n\ge2}e^{-(3/2)16^jn^4}
\le2e^{-24\,16^j}.
$$
因而
$$
\boxed{
\log\|e^{Z_j}\|
\le\log(1+r_j)+16^{-j/3}L_j^{4/3}
+2e^{-24\,16^j}.
}
\tag{2.7}
$$
由于 $\sum_{j\ge0}16^{-j/3}<2$，对任意有限头长 $m$，
$$
\boxed{
\left\|e^{\sum_{j<m}Z_j}\right\|
\le\exp(mx+2x^{4/3}+1).
}
\tag{2.8}
$$

令
$$
p=1+\frac1\alpha\in\left(\frac43,\frac53\right).
$$
将 $j$ 按 $j\le(2x/\beta)^{1/\alpha}$ 及其补集分开，可得
$$
\sum_{j\ge0}\log(1+q e^{-\beta j^\alpha})
\le C_{\alpha,\beta}x^p.
$$
低部每项至多 $x$，高部使用
$q e^{-\beta j^\alpha}\le e^{-\beta j^\alpha/2}$。
所以 (2.7) 给全域实际界
$$
\boxed{
\max\left\{
\left\|e^{\sum_{j\in J}Z_j}\right\|,
\left\|e^{\sum_{j\in J}D_j}\right\|
\right\}
\le e^{C_{\alpha,\beta}x^p}
}
\tag{2.9}
$$
对任意指标子集 $J$ 成立。
把全部 $z_\nu$ 同乘 $t\in[0,1]$ 时仍可用右侧同一常数。

实际与纯尾生成元之差满足
$$
\left\|\sum_{j\ge m}(Z_j-D_j)\right\|
\le4q e^{-770\,16^m}.
$$
两者均为有界算子，故有界 Duhamel 恒等式和 (2.9) 给
$$
\boxed{
\left\|
e^{\sum_{j\ge m}Z_j}
-e^{\sum_{j\ge m}D_j}
\right\|
\le4q\exp[-770\,16^m+2C_{\alpha,\beta}x^p].
}
\tag{2.10}
$$
这里完整保留实际 carry，也支付了指数增长；没有只用生成元差就认定指数差小。

## 3. 固定软数目窗：有界且 a.e. 严格正的单个向量

按原物理二进位分块
$$
I_\ell=[2^\ell,2^{\ell+1})\cap\mathbb N_0,\qquad
N_\ell=|I_\ell|=2^\ell,\qquad \ell=0,1,\ldots .
\tag{3.1}
$$
第0物理位不在这些块内，始终取原真空。
每块原真空为物理 $|0\rangle,|1\rangle$ 的均匀正张量，
其数目 $K_\ell$ 服从 $\operatorname{Bin}(N_\ell,1/2)$。

选择 $\ell_0$ 足够大，使对所有 $\ell\ge\ell_0$：
$N_\ell^s\le N_\ell/4$、$N_\ell^s\ge2$，
且 $2e^{-N_\ell^{2s-1}/2}\le1/2$。
对这些块置
$$
w_\ell=\lfloor N_\ell^s\rfloor,\qquad
L_\ell=N_\ell/2-w_\ell,\quad
U_\ell=N_\ell/2+w_\ell.
$$
对其余有限多个块取全窗 $[L_\ell,U_\ell]=[0,N_\ell]$。
记
$$
k_\ell=U_\ell-L_\ell,\qquad
P_\ell=\mathbf1_{\{L_\ell\le K_\ell\le U_\ell\}},\qquad
p_\ell=\|P_\ell\Omega_\ell\|^2.
\tag{3.2}
$$
全部窗口关于 $N_\ell/2$ 对称，且
$$
k_\ell\le C_sN_\ell^s,\qquad p_\ell\ge\frac12.
\tag{3.3}
$$

二项分布的基本指数估计给
$$
1-p_\ell\le2e^{-2w_\ell^2/N_\ell}
\le2e^{-N_\ell^{2s-1}/2}
\quad(\ell\ge\ell_0).
\tag{3.4}
$$
可直接由
$\mathbb E e^{t(K_\ell-N_\ell/2)}
=(\cosh(t/2))^{N_\ell}\le e^{N_\ell t^2/8}$
优化 Markov 界得到。
因为 $2s-1>0$，$\sum_\ell(1-p_\ell)<\infty$。

取固定软化参数
$$
\varepsilon_\ell=\exp[-16^{\,2N_\ell}],\qquad
f_\ell=\mathbf1_{\mathrm{win}_\ell}
+\varepsilon_\ell\mathbf1_{\mathrm{win}_\ell^c},
$$
$$
s_\ell=\|f_\ell\|_2^2
=p_\ell+\varepsilon_\ell^2(1-p_\ell).
\tag{3.5}
$$
令
$$
\boxed{
h(y)=
\frac{\prod_{\ell\ge0}f_\ell(y)}
{\prod_{\ell\ge0}\sqrt{s_\ell}}.
}
\tag{3.6}
$$
分母严格正，因为 $\sum(1-s_\ell)\le\sum(1-p_\ell)<\infty$。
又由 (3.4)，几乎每个点只落在有限多个窗口外：
发生无穷多个窗口外事件的概率不超过
$\lim_L\sum_{\ell\ge L}(1-p_\ell)=0$。
因此分子的无限乘积几乎处处是有限个严格正 $\varepsilon_\ell$ 的乘积。
所以 $h>0$ a.e.，且
$$
\|h\|_\infty\le\left(\prod_\ell s_\ell\right)^{-1/2}<\infty.
$$
有限部分乘积一致有界且逐点收敛，故在 $L^2$ 中收敛。
每个有限规范乘积的 $L^2$ 范数是1，遂得 $\|h\|_2=1$。
数目窗关于二进位翻转对称，所有系数实，故原 $C$ 满足 $Ch=h$。

### 3.1 只作比较的硬尾替换

若 $m=2^L$ 是块边界，把 $\ell<L$ 的软块保留，$\ell\ge L$ 改成规范硬窗
$$
g_\ell=P_\ell\Omega_\ell/\sqrt{p_\ell}.
$$
所得向量记为 $h^{[m]}$，仍有范数1。
单块直接计算给
$$
\left\|\frac{f_\ell\Omega_\ell}{\sqrt{s_\ell}}-g_\ell\right\|
\le4\varepsilon_\ell\sqrt{1-p_\ell}\le4\varepsilon_\ell.
$$
用有限规范张量乘积的望远镜，再取 $L^2$ 极限，得到
$$
\boxed{
\|h-h^{[m]}\|
\le4\sum_{\ell\ge L}\varepsilon_\ell
\le8e^{-16^{\,2m}}.
}
\tag{3.7}
$$
$h$ 本身固定不随指数参数变化；$h^{[m]}$ 仅为带明确误差的辅助向量。

## 4. 任意实际交换子的全尾近交换投影

这里给一条对整个原 $\mathfrak C$ 单位球统一的实际比较。

在第 $j$ 位物理分解中，写
$$
E_j=\begin{pmatrix}0&0\\I&0\end{pmatrix},\qquad
R=\begin{pmatrix}a&b\\c&d\end{pmatrix},
$$
其中各块都是其余全部位上的有界算子。
定义有界线性投影
$$
\mathcal P_j(R)=
\begin{pmatrix}(a+d)/2&0\\c&(a+d)/2\end{pmatrix}.
\tag{4.1}
$$
其像准确为与 $E_j$ 交换的算子，且
$$
\|\mathcal P_j\|\le2,\qquad
\|R-\mathcal P_j(R)\|
\le\frac32\|[R,E_j]\|.
\tag{4.2}
$$
后一式使用
$$
[R,E_j]=
\begin{pmatrix}b&0\\d-a&-b\end{pmatrix},
$$
其中 $\|b\|,\|d-a\|\le\|[R,E_j]\|$。

不同位上的 $\mathcal P_j$ 彼此交换；
对 $i\ne j$，还满足
$$
[\mathcal P_i(R),E_j]=\mathcal P_i([R,E_j]).
\tag{4.3}
$$
若 $R\in\mathfrak C$，则 $[R,N_j]=0$，所以 (1.3) 给
$$
\|[R,E_j]\|\le2\eta_j\|R\|.
\tag{4.4}
$$

固定 $m$，按 $j=m,m+1,\ldots$ 依次施加 $\mathcal P_j$。
第 $j$ 步增量的范数至多
$$
3\cdot2^{j-m}\eta_j\|R\|.
$$
由原真实 carry 包络，这些增量绝对可和，且
$$
3\sum_{j\ge m}2^{j-m}\eta_j
\le6e^{-770\,16^m}=:\epsilon_m^{\mathrm{com}}.
$$
因此范数极限
$$
\mathcal Q_m(R)
=\lim_{n\to\infty}\mathcal P_n\cdots\mathcal P_m(R)
\tag{4.5}
$$
存在，并满足
$$
\boxed{
[\mathcal Q_m(R),E_j]=0\ (j\ge m),\quad
\|\mathcal Q_m(R)-R\|
\le\epsilon_m^{\mathrm{com}}\|R\|,\quad
\|\mathcal Q_m(R)\|\le(1+\epsilon_m^{\mathrm{com}})\|R\|.
}
\tag{4.6}
$$
这定义在实际 $\mathfrak C$ 上；不声称无限投影乘积在全部 $B(H)$ 上一致有界。

$\mathcal Q_m(R)$ 是比较算子，未被假设属于原 $\mathfrak C$。
该构造不要求混合实际因子与纯因子交换，也不把一般右因子换成有限次数多项式。

## 5. 纯尾数目旗与完整压缩

取块边界 $m=2^L$。
令 $M_m^0$ 为全部尾块同时满足 $K_\ell\ge L_\ell$ 的闭支持空间。
在其中，令 $N_m^0$ 为“至少一个尾块满足 $K_\ell>U_\ell$”的闭支持空间。
于是
$$
Q_m^0=M_m^0\ominus N_m^0
$$
准确为全部尾块均处于其窗口中的支持空间，头部自由；
$h^{[m]}\in Q_m^0$。

若有界 $R^0$ 与全部尾 $E_j$ 交换，则它保持此旗。
具体地，对每个有限尾块 $I_\ell$，
逐位使用单个位的交换矩阵式，可写
$$
R^0=\sum_{F\subseteq I_\ell}E_F\otimes B_F
\tag{5.1}
$$
其中 $B_F$ 为块外有界算子。
这些纯产生项只能提高该块的物理数目，所以保持每个阈值空间 $K_\ell\ge r$。
于是它保持 $M_m^0$ 的无限交；
也保持 $M_m^0\cap\{K_\ell>U_\ell\}$ 的各项及其闭线性张成 $N_m^0$。

因此
$$
\pi_m^0(R^0)=P_{Q_m^0}R^0|_{Q_m^0}
\tag{5.2}
$$
在这个纯尾交换子族上是契约代数表示。
这些算子保持下阈值空间 $M_m^0$；在 $M_m^0$ 内，上窗外的 $N_m^0$ 分量不能返回窗口，因此商压缩的乘法关系准确。
低于下阈值的向量可以被产生算子送入窗口，但它们不属于此商的原空间 $M_m^0$。
这里的 $M_m^0,N_m^0$ 只是比较旗；不宣称它们被原 $A$ 或一般实际 $R$ 保持。

对 (2.6) 的纯块
$$
D_{I_\ell}=\sum_{j\in I_\ell}\xi_jE_j
$$
有
$$
(\pi_m^0D_{I_\ell})^{k_\ell+1}=0,\qquad
\|\pi_m^0D_{I_\ell}\|
\le t_\ell:=\sum_{j\in I_\ell}|\xi_j|
\le qN_\ell e^{-\beta N_\ell^\alpha}.
\tag{5.3}
$$
所以
$$
\boxed{
\log\|e^{\pi_m^0D_{I_\ell}}\|
\le\min\{t_\ell,\ k_\ell\log(1+t_\ell)\}.
}
\tag{5.4}
$$
当 $k_\ell=0$ 时两边均为0；
其余情形使用
$\sum_{r=0}^{k_\ell}t_\ell^r/r!\le(1+t_\ell)^{k_\ell}$
及完整指数上界。

取常数 $D$ 使 $\beta D^\alpha\ge2$，按
$N_\ell\le D x^{1/\alpha}$ 和其补集分开。
低部满足
$$
\sum_{N_\ell\le D x^{1/\alpha}}k_\ell=O(x^{s/\alpha})=O(x^{1/3}),
\qquad
\log(1+t_\ell)=O(x).
$$
高部则满足 $t_\ell\le N_\ell e^{-\beta N_\ell^\alpha/2}$，其和一致有限。
因而 (5.4) 给
$$
\boxed{
\left\|
e^{\,\pi_m^0(\sum_{j\ge m}D_j)}
\right\|
\le e^{C_{\alpha,\beta}x^{4/3}},
}
\tag{5.5}
$$
常数与剥头边界 $m$ 无关。
无穷块的指数乘积由生成元的绝对范数收敛取得，未交换未控级数。

## 6. 原实际全右测试的整函数界

固定 $z$，仍用 (2.4) 的 $q,x$。
选一个足够大的常数 $M_0$，再令 $m$ 为不小于
$$
M_0+\frac{2}{\log16}\log(1+x)
\tag{6.1}
$$
的最小二的整数幂，并取 $M_0\ge2^{\ell_0}$。
于是
$$
m=O(1+\log(1+x)),\qquad
16^m\ge16^{M_0}(1+x)^2,\qquad
mx=O(x^{4/3}).
\tag{6.2}
$$
因为 $p<2$，可一次性选 $M_0$，使以下全部误差在所有 $x\ge\log2$ 上至多1：
$$
4q e^{-770\,16^m+2C_{\alpha,\beta}x^p},\qquad
6e^{-770\,16^m+C_{\alpha,\beta}x^p},\qquad
16e^{-16^{2m}+C_{\alpha,\beta}x^p}.
\tag{6.3}
$$
常数 $M_0$ 可依固定包络及窗口选择，不依 $z$ 或右测试。

令 $F\in\mathfrak C$，并置
$$
F'=e^{\sum_{j<m}Z_j}F\in\mathfrak C.
$$
实际各项交换，且由 (2.8)、(6.2)，
$$
\|F'\|\le e^{C_1x^{4/3}}\|F\|.
\tag{6.4}
$$
先把固定 $h$ 换成 $h^{[m]}$。
由 (3.7)、(2.9)，所得标量误差至多
$$
2\|h-h^{[m]}\|
\left\|e^{\sum_jZ_j}\right\|\|F\|
\le16e^{-16^{2m}+C_{\alpha,\beta}x^p}\|F\|.
\tag{6.5}
$$
这是固定原态的有界误差比较，不是随参数更换见证。

在硬尾辅助向量上，再用 (2.10) 将实际尾指数替换为纯尾指数，误差至多 (6.3) 第一项乘 $\|F'\|$。
然后用 (4.6) 将 $F'$ 换成 $\mathcal Q_m(F')$，误差至多 (6.3) 第二项乘 $\|F'\|$。

两步后的主项是
$$
\left\langle
e^{\sum_{j\ge m}D_j}\mathcal Q_m(F')h^{[m]},
h^{[m]}
\right\rangle.
$$
它可在 §5 的纯比较旗中准确压缩：
$$
\left\langle
e^{\pi_m^0(\sum_{j\ge m}D_j)}
\pi_m^0(\mathcal Q_m(F'))h^{[m]},
h^{[m]}
\right\rangle.
$$
由 (4.6)、(5.5)，其绝对值至多
$$
e^{C_2x^{4/3}}
(1+\epsilon_m^{\mathrm{com}})\|F'\|.
$$
结合 (6.3)--(6.5)，吸收固定常数，得到
$$
|\phi_h(e^{\sum_\nu z_\nu T_\nu}F)|
\le e^{C_3x^{4/3}}\|F\|.
\tag{6.6}
$$
$q=\sum C_\nu|z_\nu|$ 与参数模和只差固定常数，故 (6.6) 就是 (1.6)。
全部界对原实际 $\mathfrak C$ 单位球同时成立。

## 7. 固定零常数多项式也保持该尺度

令
$$
\mathcal F(z)=
\left[F\mapsto
\phi_h(e^{\sum_\nu z_\nu T_\nu}F)\right]
\in\mathfrak C_*.
$$
由于各 $T_\nu$ 有界，这是 Banach 空间值整函数。
(1.6) 与多变量 Cauchy 估计给常数 $c,C>0$，使对每个多重指标 $\gamma$，
$$
\boxed{
\|\phi_h(T_1^{\gamma_1}\cdots T_d^{\gamma_d}\,\cdot)\|_{\mathfrak C_*}
\le C\,\gamma!\,e^{-c|\gamma|^4}.
}
\tag{7.1}
$$
对于 $|\gamma|\ge1$，可取共同 Cauchy 半径
$R=\exp(a|\gamma|^3)$，其中固定 $a>0$ 足够小。
此时增长上界中的正四次项小于分母贡献
$|\gamma|\log R$ 的一半；有限小指标由 $C$ 吸收。

设 $P$ 为任意固定复多项式且 $P(0)=0$，次数为 $d_0$，系数绝对值和为 $L$。
$P(T)^n$ 的各单项次数在 $[n,d_0n]$，系数绝对值和不超过 $L^n$。
故 (7.1) 给
$$
\|\phi_h(P(T)^n\,\cdot)\|_{\mathfrak C_*}
\le C L^n(d_0n)!\,e^{-cn^4}.
$$
把阶乘及 $L^n$ 吸收进一半负四次指数，再求指数级数，得到
$$
\boxed{
\|\phi_h(e^{tP(T)}\,\cdot)\|_{\mathfrak C_*}
\le
\exp[C_P(\log(2+|t|))^{4/3}]
\quad(t\in\mathbb C).
}
\tag{7.2}
$$
$P=0$ 时显然。
若 $P$ 有非零常数项，则须另外保留其准确标量指数，不将其称为 (7.2)。

例如 (1.7) 中的实际二次组合
$X^2-B_0+Y$ 也满足 (7.2)。
这是增长上界，远弱于该二次组合真正湮灭同一正常泛函的准确零式。

## 8. 与同一正见证增长路线的准确关系

真实联合见证若满足
$$
\phi((X+H)F)=0\qquad(F\in\mathfrak C),
$$
其中 $H$ 为快实际元，那么确实有
$$
\phi(e^{tX}F)=\phi(e^{-tH}F)
$$
并可对整个 $\mathfrak C$ 单位球给快型上界。
这个有用的准确身份未被否定。

本稿表明：不能再只凭“$\phi$ 正、正常、有限秩”推出左侧必有更大的慢行增长。
同一个固定正秩一态 $h_\alpha\otimes h_\alpha$，
甚至具有原有界 a.e. 正且 $C$ 实的向量，
已经对全部合法实际右因子及多行联合指数满足快型上界。
允许右测试随指数参数变化也不能突破 (1.6)。

该构造没有证明任何联合零式。
事实上，对于任意非零非负可和行 $a$，
原 $h>0$ a.e. 与正核算子 $N_j\ge E_j$ 给
$$
\phi_h\!\left(\sum_ja_jN_j\right)>0.
$$
这里 $N_j\ge E_j$ 只表示保持原函数正锥的逐项核差，不是自伴算子序。
本稿不从增长上界构造未知实际核或不变空间。

后续若要排同一联合正见证，必须使用它的准确理想关系、真正核或商结构，
或者给该见证专属且已经付费的源上界。
本文的纯窗口旗不被自动运输为实际不变旗，
软窗比较也不改变这一边界。
普通 Hilbert ISP 的完成标准仍未达到。
