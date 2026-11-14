# R268 — 原 norm-two 余核的 de Rham 对偶、Cartier 检测与完整幺幂连接

日期：2026-11-13。**状态：下列全局有理微分化简、真实有限余核的 Cartier 判据、完整有理 gauge 和逐素数的准确 $p$-curvature 均已证明。它们描述 R264 的原固定连接；尚未证明原中央零条件迫这里的 Cartier 类消失。**

使用 [R264](R264-normtwo-finite-connection-integral-cm-compensation-and-period.md)
的全部实际规范：$E_0:y^2=x^3-x$、$dz=dx/(2y)$、$U=x^2$、
$D=U^8(U-1)^8$、$F=WD$，以及
$$
\mathscr Kh=h''+\frac{68xy}{U-1}h'+\frac{1088x}{U-1}h,
\qquad F\mathscr K(P/D)=4\frac Wx M(P).
\tag{1}
$$
令 $P_8,A_8,a_*$ 为 R264 的明确多项式和常数，故
$$
h_*:=\frac{P_8}{(U-1)^8},\quad \mathscr Kh_*=0,\qquad
a_*=-\frac{583401555}{2^{32}},
$$
$$
\frac{dz}{(U-1)P_8^2}=a_*dz+dR,
\qquad R=\frac xy\frac{A_8}{P_8}.
\tag{2}
$$
下文的 $\ell$ 始终是 R264 的本原整数余核向量，而非新选的周期归一。

## 1. 与原方程直接相连的 Lagrange 微分

对 $Q\in\mathbb Q(i)[U]_{\le16}$ 定义实际第二类微分
$$
\boxed{\eta_Q=\frac{4P_8(U)(U-1)Q(U)}{xU^8}\,dz.}
\tag{3}
$$
这个分母和次数从 (1) 直接得到。事实上，二阶 Lagrange 恒等式给
$$
\partial_z\left((U-1)^{17}(h_*h'-h_*'h)\right)
=(U-1)^{17}h_*\mathscr Kh.
\tag{4}
$$
取 $h=P/D$，因 $\mathscr Kh=4M(P)/(xD)$，右侧乘 $dz$ 恰为 $\eta_{M(P)}$。
其完整有理原函数也可写成
$$
\boxed{
(U-1)^{17}(h_*h'-h_*'h)
=\frac{4xy(U-1)}{U^9}
\{UP_8P'-(8P_8+UP_8')P\}.
}
\tag{5}
$$
这里 $P',P_8'$ 是 $U$ 微分。式 (4) 由 $\mathscr Kh_*=0$ 和
$68xy/(U-1)=17\partial_z\log(U-1)$ 直接相消；(5) 只使用 $U'=4xy$。
因此这条微分没有离开原有限连接。

## 2. 十七条微分的完整 de Rham 化简

对每个 $Q$ 存在一个明确奇 Laurent 多项式 $R_Q(x)$，使
$$
\boxed{\eta_Q=d(yR_Q(x))+\lambda\ell(Q)x\,dz,
\qquad \lambda=\frac{17179869184}{644658718275}.}
\tag{6}
$$
全部十七个基输入 $Q=U^n$ 的 $R_Q$ 系数随文保存。
式 (6) 可完全通过以下两个递推证明，无需求数值周期。
对任意奇整数 $k$，有
$$
d(yx^k)=\{(2k+3)x^{k+2}-(2k+1)x^k\}\,dz.
\tag{7}
$$
当 $k>1$ 时，
$$
x^kdz=\frac{d(yx^{k-2})}{2k-1}
       +\frac{2k-3}{2k-1}x^{k-2}dz;
\tag{8}
$$
当 $k<1$ 时，
$$
x^kdz=-\frac{d(yx^k)}{2k+1}
       +\frac{2k+3}{2k+1}x^{k+2}dz.
\tag{9}
$$
于是所有奇次幂都唯一归约到一个 $x\,dz$ 项和一个所列有理原函数。
式 (3) 对基输入的系数准确为
$$
4P_8(x^2)(x^2-1)x^{2n-17},\qquad 0\le n\le16,
\tag{10}
$$
其中只出现 $-17\le k\le33$ 的奇数指数。
对 (10) 逐项使用 (8)、(9)，所得 $x\,dz$ 的十七个系数恰为
$$
\lambda(14221350,-46930455,70569499,-58161675,27633375,
-7456625,1057485,-65637,1105,0,\ldots,0).
\tag{11}
$$
这是 R264 的同一个 $\ell$，其尺度由 (10) 的任一非零列唯一确定。
特别，两个相反 $i$ 特征的周期规范满足短等式
$$
\boxed{a_*\lambda=-\frac4{1105}.}
\tag{12}
$$

$x\,dz$ 的 de Rham 类非零：它只在 $O$ 有二阶极。
若它是一个有理函数的微分，则该函数只在 $O$ 有一阶极，
这与椭圆曲线 $L(O)$ 仅含常数矛盾。
因此由 (6)，对本篇十七维实际来源有准确等价
$$
\boxed{\eta_Q\text{ 在 }\mathbb Q(i)(E_0)\text{ 中 exact}
\quad\Longleftrightarrow\quad\ell(Q)=0
\quad\Longleftrightarrow\quad Q\in\operatorname{im}M.}
\tag{13}
$$
最后一步是 R264 的完整有限矩阵结论；前两步现在有了全局微分实现。

### 2.1 实际整性范围

递推 (8)、(9) 的全部固定分母，连同 R264 的 $P_8$ 分母，
可在有限范围 $-17\le k\le33$ 内直接列出。
其大于三十一的素因子全部在 $\mathbb Q(i)$ 中分裂；随文证书保存真实最小公分母的分解。
所以对每个惰性 $p>31$ 和每个 $Q\in\mathcal O_p[U]_{\le16}$，
(6) 的原函数以及系数 $\lambda$ 都在相应原整格中有合法约化，且 $\lambda$ 是单位。
这一步保留原有理原函数的全部分母。

## 3. 两条 de Rham 方向的准确 Cartier 作用

以下在特征 $p>3$ 的 $E_0$ 上，令 $\mathcal C$ 表示 Cartier 算子，
并采用 $\mathcal C(a^p\omega)=a\mathcal C(\omega)$ 的规范。
置 $f(x)=x^3-x$。因为
$$
dz=\left(\frac1{2y}\right)^p f(x)^{(p-1)/2}dx,
$$
而 $\deg f^{(p-1)/2}<2p-1$，只有 $x^{p-1}dx$ 一项可能贡献 Cartier。
同样，$x\,dz$ 只读取 $f^{(p-1)/2}$ 的 $x^{p-2}$ 系数。
逐项展开 $f^{(p-1)/2}=x^{(p-1)/2}(x^2-1)^{(p-1)/2}$，立即得到

| 素数类型 | $\mathcal C(dz)$ | $\mathcal C(x\,dz)$ |
|---|---|---|
| $p=4r+1$ | $(-1)^r\binom{2r}{r}\,dz$ | $0$ |
| $p=4r+3$ | $0$ | $(-1)^{r+1}\binom{2r+1}{r}\,dz$ |

表中的两个二项式系数都为 $p$ 进单位，因为各阶乘参数严格小于 $p$。
这直接证明表中所有零与非零，不以目标素数样本外推。

现在对惰性 $p=4r+3>31$，将 (6) 约化，得到
$$
\boxed{\mathcal C(\overline{\eta_Q})
=(-1)^{r+1}\binom{2r+1}{r}
       \bigl(\overline{\lambda\ell(Q)}\bigr)^{1/p}dz.}
\tag{14}
$$
因而
$$
\boxed{\mathcal C(\overline{\eta_Q})=0
\quad\Longleftrightarrow\quad\ell(Q)\equiv0\pmod p
\quad\Longleftrightarrow\quad\overline Q\in\operatorname{im}\overline M.}
\tag{15}
$$
若 $Q$ 的系数在 $\mathbb F_{p^2}$，(14) 的 $1/p$ 次幂是实际 Frobenius 逆，
不能在 Gaussian 系数上无故省去。
最后一步使用 R264 对所有惰性 $p>19$ 的本原整像结论。

特别，对已付的真实 CM 伴随 $\Gamma_\beta$，R264 的
$\ell(\Gamma_\beta)=5479905460224-3786459611136i$ 在这些素位为单位。
所以 $\mathcal C(\overline{\eta_{\Gamma_\beta}})$ 始终非零。
这给原 CM 余核补偿一个准确、可检测的 Cartier 值。

普通素数处，同一 $x\,dz$ 方向的 Cartier 值为零。
表中保留了这个差别；没有把惰性的 (15) 移用于普通素数。

## 4. 原二阶方程的完整有理 gauge

式 (2) 不只是一个周期值，还给一个全局有理矩阵。设
$$
G=\begin{pmatrix}
h_*&h_*R\\
h_*'&(h_*R)'+a_*h_*
\end{pmatrix},\qquad
N=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\tag{16}
$$
这里 $h_*R=yA_8/(U-1)^9$，故各项都在原函数域 $\mathbb Q(E_0)$ 内。
由 (2) 直接得
$$
\boxed{\det G=h_*^2(R'+a_*)=(U-1)^{-17}.}
\tag{17}
$$
令
$$
A_{\mathscr K}=\begin{pmatrix}
0&1\\-1088x/(U-1)&-68xy/(U-1)
\end{pmatrix}.
$$
准确矩阵恒等式为
$$
\boxed{G'=A_{\mathscr K}G-Ga_*N.}
\tag{18}
$$
其第一列是 $\mathscr Kh_*=0$，第二列由 (2) 的微分及同一齐次方程得到；
随文证书在 $\mathbb Q(x)[y]/(y^2-x^3+x)$ 内核实全部四项。
所以令 $(h,h')^t=G(v,w)^t$，原方程 $\mathscr Kh=0$ 准确变为
$$
\boxed{v'=a_*w,\qquad w'=0.}
\tag{19}
$$
换成连接，右端就是
$$
\boxed{\nabla=d-a_*N\,dz.}
\tag{20}
$$
它在整个椭圆曲线上是正则的秩二幺幂连接。
特征零下它不分裂：分裂将给 $dz$ 一个全局有理原函数，
而非零全纯微分不可能是光滑射影曲线上有理函数的微分。
其沿周期 $\omega\in\Lambda$ 的实际 monodromy 为 $1+a_*\omega N$。
这些周期和 (6) 的对偶周期都来自同一个明确原连接。

## 5. 准确的 $p$-curvature

在好约化处，取不变向量场 $\partial$，满足 $dz(\partial)=1$。
$\partial^p$ 仍是全局正则向量场，故 $\partial^p=H_p\partial$，其中
$$
H_p=\begin{cases}
(-1)^r\binom{2r}{r},&p=4r+1,\\
0,&p=4r+3.
\end{cases}
\tag{21}
$$
这个系数也可从上节的 Cartier 表直接确定：Cartier 对偶恒等式
$$
\bigl(\mathcal C(\omega)(\partial)\bigr)^p
=\omega(\partial^p)-\partial^{p-1}(\omega(\partial))
$$
用于 $\omega=dz$ 时，最后一项为零。
该恒等式在分离坐标的基 $dx,x\,dx,\ldots,x^{p-1}dx$ 上逐项验证，
并对 $p$ 次幂系数线性延拓；其 Cartier 规范与 §3 完全相同。

采用 $\psi_p(\partial)=\nabla_\partial^p-\nabla_{\partial^p}$ 的符号。
由于 $N^2=0$ 且 $a_*$ 为常数，(20) 给
$$
(\partial-a_*N)^p=\partial^p,
$$
从而
$$
\boxed{\psi_p(\partial)=a_*H_pN.}
\tag{22}
$$
在删去 (16) 系数的固定分母后，(18) 将它准确共轭回原二阶方程。
特别对所有 $p>31$，这些分母均合法：
惰性处 $p$-curvature 为零，普通处为秩一的非零幺零矩阵。
所以此方程的幂零曲率和特征零非平凡周期可以同时成立，二者的准确联系已由 (22) 给出。

## 6. 接回原 theta 问题时保留的内容

式 (15) 现在是原有限 $M$ 的真实几何判据，
而 (18) 给出了可逐项运输的原连接矩阵。
与 R264 的整分解合用时，$\Gamma_\beta$ 补偿带有 (14) 的非零 Cartier 值，
不能把它从实际连接图中删除。

要由原 $A,B,H$ 的中央零得到矛盾，仍须支付完整 theta frame 的 Frobenius、
非 $\beta$ 运输交换差以及 Mellin 的全部权移。
原完整中央零目前尚未推出 $\mathcal C(\eta_Q)=0$；
固定 $\mathscr K$ 的曲率也不是原 theta 中央测度的曲率。
本篇提供的是这一步比较所需的明确有限几何对象及准确系数。

## 7. 证书与已发表规范

- [精确脚本](../scripts/check-normtwo-de-rham-duality-and-unipotent-gauge.py) 与
  [十七条全局原函数、gauge 和分母](../scripts/check-normtwo-de-rham-duality-and-unipotent-gauge.json)。
  二十六项检查涵盖全部原微分列、余核尺度、整性及完整矩阵恒等式；没有目标素数扫描。
- N. Katz，*Nilpotent connections and the monodromy theorem: applications of a result of Turrittin*，
  Publ. Math. IHÉS **39** (1970), 175–232，§5 的曲率规范和 Theorem 7.2 的 Cartier 规范；
  [原刊页面](https://www.numdam.org/articles/10.1007/BF02684688/)。
  本文所用两条具体 Cartier 系数及 (22) 已在 §3、§5 直接计算。
