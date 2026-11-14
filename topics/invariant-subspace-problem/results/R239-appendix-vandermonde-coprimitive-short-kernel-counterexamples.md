# R239 附录：原无限尾短核旗上的 Vandermonde 反例与非闭伴随像

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume。
状态：完整显式构造及原无限尾结论已证明；主会话与 central_review 分别独立核验两条 Lagrange 恒等式，主会话补全 $m=0$ 的固定层满射引用。本文否定固定短核阶的全孔层统一环境伴随下界，不声称这些向量来自真实缺陷或最优 Schur 源。

## 1. 被否定的准确断言

原纯尾为
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+1)^{-2},
\qquad
S_J=\sum_{j\ge J}a_j^2.
$$
这里 $E_j$ 删除第 $j$ 位的孔，不同位交换且 $E_j^2=0$。
$\mathcal H_p^{(m)}$ 是恰好 $p$ 个尾孔的原 Hilbert 层。

**定理。** 对每个固定 $m\ge0$ 和每个整数 $p\ge1$，存在显式单位向量
$$
x_{m,p}\in\mathcal H_p^{(m)},\qquad
D_m^2x_{m,p}=0,
$$
使
$$
\boxed{
\|D_m^*x_{m,p}\|^2=S_{m+2p}.
}
\tag{1.1}
$$
故对任何固定 $h\ge2$，
$$
\boxed{
\inf_{\substack{x\in\ker D_m^h\\\|x\|=1}}\|D_m^*x\|=0.
}
\tag{1.2}
$$
按正交孔层写，这亦表明
$$
\inf_{p\ge0}\ \inf_{\substack{x\in\ker D_m^h\cap\mathcal H_p^{(m)}\\\|x\|=1}}
\|D_m^*x\|=0.
$$
因此不存在仅依赖 $m,h$、与孔数 $p$ 无关的正下界，允许常数极小也不能成立。

积分比较给
$$
\frac1{3(J+1)^3}\le S_J\le\frac1{3J^3}\quad(J\ge1),
$$
从而本构造的准确量级为
$$
\|D_m^*x_{m,p}\|
\sim\frac1{\sqrt3\,(m+2p)^{3/2}}
\quad(p\to\infty,\ m\ \text{固定}).
\tag{1.3}
$$
这里只给明确上界族，不声称它是每层最小值或最佳下降速率。

## 2. 任意偶数个互异正权上的有限向量

先处理一般有限块 $I=\{0,\ldots,2p-1\}$，权 $\alpha_i>0$ 且
$$
z_i=\alpha_i^2
$$
两两互异。令
$$
D_I=\sum_{i\in I}\alpha_iE_i.
$$
对有序子集 $S$ 定义
$$
\Delta_S=\prod_{\substack{i<j\\i,j\in S}}(z_j-z_i),
$$
空积为 $1$。对 $|S|=p$，记
$$
\varepsilon(S,S^c)
=(-1)^{\sum_{i\in S}i-p(p-1)/2},
$$
即把顺序列 $S,S^c$ 拼回 $I$ 时的排列符号，并置
$$
y_S=\varepsilon(S,S^c)\Delta_S\Delta_{S^c},
\qquad
X_S=\left(\prod_{i\in S}\alpha_i\right)y_S.
\tag{2.1}
$$
有限块向量为
$$
X=\sum_{\substack{S\subset I\\|S|=p}}X_Se_S.
\tag{2.2}
$$
因为权平方互异，所有 Vandermonde 因子均非零，所以 $X\ne0$。

为方便核对符号，还可写成等价式
$$
\boxed{
y_S=
\frac{\Delta_I}
{\displaystyle\prod_{i\in S,\ j\notin S}(z_j-z_i)}.
}
\tag{2.3}
$$
这是将完整 Vandermonde 分为两块内部差和交叉差的准确恒等式，不是渐近表示。

我们将证明
$$
\boxed{D_I^*X=0,\qquad D_I^2X=0.}
\tag{2.4}
$$
本构造对任意互异正权都成立；不需要原权的具体衰减式。
没有依据有限次数模素数试验推断实秩，也没有声称共同核总是一维。
均权情形使 (2.1) 的 Vandermonde 退化，须另用其已知的普通对称链或原始空间；本稿不通过除零公式处理均权。

## 3. 一阶创建方程：第一条 Lagrange 和

记
$$
P_A(t)=\prod_{i\in A}(t-z_i).
$$
对任意互异节点集 $A$，Lagrange 插值的最高次系数给
$$
\sum_{i\in A}\frac{f(z_i)}{P_A'(z_i)}=0
\quad(\deg f\le |A|-2).
\tag{3.1}
$$
这只须把次数不超过 $|A|-2$ 的 $f$ 展开在次数 $|A|-1$ 的 Lagrange 基，再比较最高次项。

给定 $R\subset I$、$|R|=p+1$，令 $T=I\setminus R$，故 $|T|=p-1$。
第 $R$ 个创建输出系数是
$$
(D_I^*X)_R
=\sum_{i\in R}\alpha_iX_{R\setminus\{i\}}
=\left(\prod_{i\in R}\alpha_i\right)
\sum_{i\in R}y_{R\setminus\{i\}}.
\tag{3.2}
$$
令
$$
C_{R,T}=\prod_{r\in R,\ t\in T}(z_t-z_r).
$$
在 (2.3) 中对 $S=R\setminus\{i\}$ 拆分交叉积，得到
$$
y_{R\setminus\{i\}}
=\frac{(-1)^{p-1}\Delta_I}{C_{R,T}}
\,\frac{P_T(z_i)}{P_R'(z_i)}.
\tag{3.3}
$$
前置因子与 $i$ 无关。因为
$\deg P_T=p-1=|R|-2$，(3.1) 使 (3.2) 中的和准确为零。
因此
$$
D_I^*X=0.
\tag{3.4}
$$

## 4. 顺序二次删除：第二条 Lagrange 和

当 $p=1$ 时，$X$ 只有一孔，故 $D_I^2X=0$ 自动成立。
下设 $p\ge2$。

给定 $T\subset I$、$|T|=p-2$，令 $U=I\setminus T$，则 $|U|=p+2$。
由于不同位删除交换而每位平方为零，顺序算子平方的准确系数为
$$
D_I^2=2\sum_{i<j}\alpha_i\alpha_jE_iE_j.
$$
特别，
$$
(D_I^2X)_T
=2\left(\prod_{t\in T}\alpha_t\right)
\sum_{\substack{i<j\\i,j\in U}}
z_i z_j\,y_{T\cup\{i,j\}}.
\tag{4.1}
$$
这里的因子 $2$ 已完整保留；没有用点态平方替代顺序删除。

置
$$
C_{T,U}=\prod_{t\in T,\ u\in U}(z_u-z_t).
$$
由 (2.3) 逐个拆分交叉差，准确有
$$
y_{T\cup\{i,j\}}
=-\frac{\Delta_I}{C_{T,U}}\,
\frac{P_T(z_i)P_T(z_j)(z_i-z_j)^2}
{P_U'(z_i)P_U'(z_j)}.
\tag{4.2}
$$
定义
$$
\beta_i=\frac{z_iP_T(z_i)}{P_U'(z_i)}\quad(i\in U).
$$
因为
$$
\deg(tP_T(t))=p-1,\qquad
\deg(t^2P_T(t))=p,
\qquad |U|-2=p,
$$
同一个 Lagrange 恒等式给
$$
\sum_{i\in U}\beta_i=0,\qquad
\sum_{i\in U}z_i\beta_i=0.
\tag{4.3}
$$
而有限代数展开给
$$
\boxed{
\sum_{\substack{i<j\\i,j\in U}}
\beta_i\beta_j(z_i-z_j)^2
=
\left(\sum_i\beta_i\right)\left(\sum_i z_i^2\beta_i\right)
-\left(\sum_i z_i\beta_i\right)^2=0.
}
\tag{4.4}
$$
将 (4.2)–(4.4) 代入 (4.1)，每个输出系数都为零。
因此
$$
D_I^2X=0.
\tag{4.5}
$$
这完成 (2.4) 的显式证明。

## 5. 运输到原无限尾，范数恰好是远尾平方和

现在取实际前缀
$$
I_{m,p}=[m,m+2p),\qquad J=m+2p,
$$
并在 §2 中代入
$$
\alpha_i=a_{m+i}=(m+i+1)^{-2}.
$$
这些正权两两互异。令 $X_{m,p}$ 为 (2.2) 的非零有限向量，归一化后张量远尾真空：
$$
x_{m,p}
=\frac{X_{m,p}}{\|X_{m,p}\|}\otimes\Omega_{[J,\infty)}.
\tag{5.1}
$$
它恰有 $p$ 个尾孔，且前缀以外全为空。

由于 $D_m=D_{I_{m,p}}+D_J$ 且 $D_J\Omega=0$，(4.5) 给
$$
D_m^2x_{m,p}=0.
\tag{5.2}
$$
另一方面，(3.4) 使前缀创建项完全消失，所以
$$
D_m^*x_{m,p}
=\frac{X_{m,p}}{\|X_{m,p}\|}\otimes D_J^*\Omega.
\tag{5.3}
$$
远尾的不同单孔向量正交，因而
$$
\|D_J^*\Omega\|^2
=\sum_{j\ge J}a_j^2=S_J.
\tag{5.4}
$$
(5.2)–(5.4) 正是 (1.1)。这不是把有限模型的伴随核直接视为无限伴随核；无限尾创建项明确保留，并准确计算范数。

随着 $p\to\infty$，原无限尾的 $S_{m+2p}\to0$，所以 (1.2) 成立。
不同 $p$ 的 $x_{m,p}$ 位于互相正交的孔层，因而还是一列正交单位向量，特别弱收敛于零。

## 6. 固定层、闭像及真实研究接口的范围

每个固定 $p$ 上，$D_m:\mathcal H_{p+1}^{(m)}\to\mathcal H_p^{(m)}$ 已由
[R254 相容多次原像](R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)
§§1–3 的 $R_1$ 证明有界满射：当 $m\ge1$ 时把原 $(j+1)^{-2}$ 权作 $m'=m-1$ 的既有整数重标。对 $m=0$，另写 $D_0=E_0+D_1$，选取同一个 $D_1$ 相容族 $R_1,R_2$，则
$$
D_0(R_1-E_0R_2)=I
$$
由 $D_1R_1=I$、$D_1R_2=R_1$、$E_0^2=0$ 及头尾交换准确成立。两项均把总孔数增加一，且在每个固定输入层有界。因此 $m=0$ 也已单独支付，不使用负起始位参数或把 $\|D_0\|\le1$ 当成已知。
所以其伴随 $D_m^*|_{\mathcal H_p^{(m)}}$ 在这个固定层有正下界。
由于 $D_m^*$ 分别将不同孔层送入不同孔层，它在整个有限子集 Hilbert 空间上单射。
这与 (1.2) 相容：失去的是跨所有 $p$ 的统一下界。

特别，$D_m^*:\ker D_m^h\to\mathcal H^{(m)}$ 对 $h\ge2$ 是有界单射却没有闭像。
这是闭值域定理与 (1.2) 的直接推论。
若再把输出压缩到任意闭子空间，输出范数只会更小，所以这些序列同样阻止相应压缩的全层统一下界。

[已证环境联合能量](R239-appendix-all-hole-environment-energy-gap-and-actual-tail-stability.md)
在该附录已证明的 $m\ge5$ 范围内仍然成立：$D_m^*D_m+D_mD_m^*\ge c_mI$。
它在本构造上要求 $\|D_mx_{m,p}\|$ 不能同时趋零，并不与
$D_m^2x_{m,p}=0$ 冲突。$h=1$ 的环境创建下界也没有被本稿推翻。

本构造只使用原纯尾和原 Hilbert 范数，没有以真实 carry 近似替代任一等式。
它关闭的是“固定短纯核阶即可取得与孔数无关的环境 $D_m^*$ 下界”这一候选路线。
没有证明 $x_{m,p}$ 来自真实 $w\in M\ominus N$、真实低核 Schur 源或
[完整核合成](R239-appendix-full-l-kernel-completion-and-legal-m-tests.md)
中的 $h_t$。因此不能由此推出无权修复失败、$N\ne M$ 或普通 ISP 的任何完成结论。
后续仍须利用真正源结构或控制 $\widetilde C_{\rm tot}(h(z))$，而不是继续寻找已被 (1.2) 排除的统一环境下界。
