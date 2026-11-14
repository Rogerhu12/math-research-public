# R168：Tate Frobenius 的非齐次约束、支撑单位斜率与 Weil 平方类

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的全参数必要条件。**
本文把 [R161](R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md)
的惯性正交进一步接到实际乘法约化表示的 Frobenius 迹。
允许支撑素数本身出现在 $S$-单位中，得到一个由固定 $A,p,R$
确定的有限分量矩阵。它与实际整数 $(q+1)/p^n$ 满足非齐次方程，
并与判别式指数 $pv_q(Z)$ 的 Weil 配对平方类相容。

特别地，若最小 Tate 支撑只有一个在 $\mathbb Q(i)$ 惰性的素数 $q$，
且原始 Robert 对偶线在 $q$ 为零，则存在一个与 $E$ 无关的
$q$-单位斜率 $\lambda_q$。实际曲线必满足
$$
x_q\lambda_q=\frac{q+1}{2p^n}\pmod p,\qquad x_q\ne0.
\tag{168.1}
$$
因此 $\lambda_q=0$ 当且仅当 $v_p(q+1)>n$。当 $\lambda_q\ne0$
时，原始判别式指数还给一个明确的非零平方条件。
本文给出斜率的真实 $S$-单位构造和剩余符号公式，但尚未计算
任何新的 $\lambda_q$ 数值，也没有得到变化 $p,R$ 的统一矛盾。

## 1. 设定与局部规范

固定
$$
A:y^2=x^3-x,\qquad K=\mathbb Q(i),\qquad
p>37,\quad p\equiv3\pmod4.
$$
写 $V=A[p]$、$J=[i]$，沿用 R161 的正交分解
$$
\operatorname{ad}^0V=\mathbb F_p(\chi_{-4})J\oplus W,\qquad
W=\{D:\operatorname{tr}D=\operatorname{tr}(JD)=0\}.
\tag{168.2}
$$
$W$ 的对偶经迹配对识别为 $W$，其 Tate 对偶为 $W(1)$。

先取一个素数
$$
q\ne2,p,\qquad q\equiv-1\pmod{4p},
$$
并在 $\overline{\mathbb Q}$ 中固定 $q$ 上方的一个素点。
所有 Frobenius 均用算术规范。令
$$
F_q=\bar\rho_A(\operatorname{Frob}_q),\qquad K_q=JF_q.
$$
$A$ 在 $q$ 好约化且 $a_q(A)=0$，所以
$$
F_q^2=1,\quad \operatorname{tr}F_q=0,\quad
F_qJ=-JF_q,\quad
K_q^2=1,\quad
\operatorname{tr}(F_qK_q)=0.
\tag{168.3}
$$
在 $W$ 上，$\operatorname{Ad}(F_q)$ 的正、负特征线分别为
$\mathbb F_pF_q$ 和 $\mathbb F_pK_q$。
在 $W(1)$ 上，圆分值 $q=-1$ 交换这两个符号。

取 $0\ne v_q\in V^{F_q=1}$。因为 $J$ 没有 $\mathbb F_p$ 本征线，
$(v_q,Jv_q)$ 为基；令
$$
\zeta_q=e_{p,A}(v_q,Jv_q).
\tag{168.4}
$$
选择兼容的 $p$ 幂单位根提升，并以 $\zeta_q$ 归一化 tame
生成元 $\tau_q$，即
$$
\tau_q(q^{1/p})/q^{1/p}=\zeta_q.
$$
这里 $q^{1/p}$ 可换为任意相容选择，惯性比值不变。
可以取算术 Frobenius 提升 $\varphi_q$ 固定各个 $q^{1/p^r}$；
后文的有限坐标实际上也不依赖这个提升。

采用 Tate 曲线的 Weil 配对规范
$$
e_{p,\operatorname{Tate}(t)}(\zeta,t^{1/p})=\zeta.
\tag{168.5}
$$
这与 Nekovář–Plater，*On the parity of ranks of Selmer groups*，
§1.2.7 的明确规范相同。本文固定这一规范；采用相反定义时，
必须同时改写 tame 根与 Tate 基中的符号，不能只反转某个局部基。
在所有曲线上同时反转配对并不改变配对乘数本身。

## 2. 两侧有限与奇异坐标及杯积的相对负号

对 $c\in H^1(\mathbb Q_q,W)$，定义标量 $a_q(c),b_q(c)$：
$$
\begin{split}
c(\varphi_q)&\equiv a_q(c)F_q
       \pmod{(\operatorname{Ad}(F_q)-1)W},\\
c(\tau_q)&=b_q(c)K_q.
\end{split}
\tag{168.6}
$$
第二式在忽略对 $p$ 上同调无贡献的 wild inertia 后成立。
这两个坐标给 $H^1(\mathbb Q_q,W)\simeq\mathbb F_p^2$。
对 $d\in H^1(\mathbb Q_q,W(1))$，用 $\zeta_q$ 写出系数的
$(1)$，定义
$$
\begin{split}
d(\varphi_q)&\equiv c_q(d)K_q
       \pmod{(F_q|_{W(1)}-1)W(1)},\\
d(\tau_q)&=d_q(d)F_q.
\end{split}
\tag{168.7}
$$
字母 $d_q(d)$ 仅是这个局部奇异坐标，不表示下文的全局类。

这些定义与 cocycle 代表无关：coboundary 的 Frobenius 值落在
相应负特征线，惯性值为零。改变 Frobenius 提升只加入惯性方向；
该方向同样是对应表示的负特征线，所以不改变有限坐标。
因此，即使原类在 $q$ 分歧，(168.6)–(168.7) 的有限坐标仍然
真实定义。不是先任意选择一个不分歧补空间再计算。

在迹配对和标准 Brauer invariant 下，局部 Tate 配对为
$$
\boxed{\langle c,d\rangle_q
=2\bigl(a_q(c)d_q(d)-b_q(c)c_q(d)\bigr).}
\tag{168.8}
$$
这里将 $(1/p)\mathbb Z/\mathbb Z$ 按 $r/p\mapsto r$ 识别为
$\mathbb F_p$；算术 reciprocity 把均匀化元送到算术 Frobenius。

以下推导同时核准因子与相对负号。
令 $k_q/\mathbb Q_q$ 为未分歧二次扩张。$W$ 和 $\mu_p$ 在
$G_{k_q}$ 上都平凡。取 $u\in\mathcal O_{k_q}^{\times}$，使
其 Kummer 类在 $\operatorname{Frob}_{k_q}$ 的
$\zeta_q$ 对数为 $1$；记对应的 $\mathbb F_p$ 值类为 $U$。
均匀化元 $q$ 的 Kummer 类则记为 $T$。于是
$$
U(\varphi_q^2)=1,\quad U(\tau_q)=0,\qquad
T(\varphi_q^2)=0,\quad T(\tau_q)=1.
$$
限制后的两类为
$$
c|_{k_q}=2aF_qU+bK_qT,\qquad
d|_{k_q}=2c'K_q(U\otimes\zeta_q)
                  +d'F_q(T\otimes\zeta_q).
$$
$\operatorname{tr}(F_q^2)=\operatorname{tr}(K_q^2)=2$，
两个交叉迹为零，而且一次上同调杯积反交换，故限制后的配对为
$$
4(ad'-bc')\,[U\cup(T\otimes\zeta_q)].
$$
均匀化元 reciprocity 给最后的杯积 invariant 为 $1/p$。
Brauer invariant 在次数二的限制下乘 $2$，即得 (168.8)。
即使用相反的全局 reciprocity 规范，所有局部项同时反号，
后文的 $a=b\lambda$ 和全部矩阵等式保持不变。

这里只使用标准 Kummer 与局部杯积规范；可直接核对
Milne，*Class Field Theory* v4.03，III Proposition 3.6、
Lemma 3.7，以及 III §4 的 Steps 2–3 和 Theorem 4.4(b)。

## 3. 支撑素数的真实 $S$-单位类与局部计算公式

令 $Q=\{q_1,\ldots,q_r\}$ 为满足 §1 条件的有限素数集。
沿用 R163 的数域
$$
T=\mathbb Q(A[p]),\qquad
\mathscr F=T^{\mathbb F_p^\times},\qquad
G=\operatorname{Gal}(\mathscr F/\mathbb Q).
$$
$|G|=2(p+1)$ 与 $p$ 互素，且 $W$ 经 $G$ 作用。
记
$$
\mathcal D_{p,Q}
=\{d\in H^1(\mathbb Q,W(1)):
 d\text{ 在 }2,p,Q\text{ 外不分歧}\},
\tag{168.9}
$$
在 $p$ 不加限制，$2$ 处整个局部上同调为零。

R161 的严格 $p$ 条件最小 Selmer 为零；进一步在 $Q$ 要求
primal 局部为零仍为零。Poitou–Tate 比较与 R164 §3 完全相同，
给准确序列
$$
0\longrightarrow\mathcal D_p
\longrightarrow\mathcal D_{p,Q}
\xrightarrow{(d_{q_i})_i}\mathbb F_p^r
\longrightarrow0.
\tag{168.10}
$$
因此 $\dim\mathcal D_{p,Q}=r+1$。此处每个 $q_i$ 的奇异方向
是一维；不是把整个二维局部空间误当成新增一维。

R163 已证明 $\operatorname{Cl}(\mathscr F)[p]$ 的 $W$ 型为零。
$2,p$ 上方的赋值置换模没有 $W$ 型不变量。因此真正的 Kummer
序列给
$$
\mathcal D_{p,Q}
\simeq
\left(
\mathcal O_{\mathscr F,Q}^{\times}/
        (\mathcal O_{\mathscr F,Q}^{\times})^p
\otimes_{\mathbb F_p}W\right)^G.
\tag{168.11}
$$
这里 $(1)$ 已由 Kummer 提供；张量因子是 $W$，不是 $W(1)$。
没有假设 $\mathscr F$ 包含 $\mu_p$；在所选 $q_i$ 的完成处
却确实包含 $\mu_p$，因为该完成是未分歧二次扩张。

固定 R163 的非零原始 Robert 类 $d_0\in\mathcal D_p$。
由 (168.10)，对每个 $j$ 可取真实 $Q$-单位类 $d_j$，使
$$
d_{q_i}(d_j)=\delta_{ij}.
\tag{168.12}
$$
固定这些奇异值后，$d_j$ 的全部歧义准确是加上 $d_0$ 的倍数。
这与选取未经全局主化的局部 Kummer 元素不同。

R164 §4 给出有限构造程序：在
$\bigoplus_{\lambda\mid Q}\mathbb Z[\lambda]$ 中作 $W$ 型整投影，
利用已消失的 $W$ 型 $p$ 类群把指定模 $p$ 赋值主化；
剩余素于 $p$ 的理想类阶可取倍数后在模 $p$ 中反转。
所得主生成元与全局单位给出 (168.11) 的实际元素。
该算法对每个固定 $p,Q$ 是有限的；本文没有把此有限性声称为
变化 $p,Q$ 的复杂度界或已经完成的数值实算。

还可把所有有限坐标写成通常的剩余幂符号。
将 $d_j$ 的 Kummer 张量代表写为有限和
$$
\xi_j=\sum_\nu [u_{j,\nu}]\otimes D_{j,\nu},
\qquad
u_{j,\nu}\in\mathcal O_{\mathscr F,Q}^{\times},\quad
D_{j,\nu}\in W.
\tag{168.13}
$$
在 $q_i$ 上方固定素点 $\lambda_i$，写
$e_{j,\nu,i}=v_{\lambda_i}(u_{j,\nu})$，并先除去均匀化元：
$$
\widetilde u_{j,\nu,i}
=u_{j,\nu}/q_i^{\,e_{j,\nu,i}}.
$$
它在 $\lambda_i$ 为单位。定义
$$
\ell_i(u)=
\log_{\zeta_{q_i}}
\left(\overline u^{\,(q_i^2-1)/p}\right)\in\mathbb F_p.
\tag{168.14}
$$
则
$$
\sum_\nu e_{j,\nu,i}D_{j,\nu}=\delta_{ij}F_{q_i},
\qquad
L_{j,i}:=\sum_\nu
 \ell_i(\widetilde u_{j,\nu,i})D_{j,\nu}
=2c_{q_i}(d_j)K_{q_i}.
\tag{168.15}
$$
第二式的 $2$ 来自
$\operatorname{Frob}_{k_{q_i}}=\varphi_{q_i}^2$；
它不能省略。因而定义
$$
\boxed{
C_{ji}=c_{q_i}(d_j)
      =\frac14\operatorname{tr}(K_{q_i}L_{j,i}),\qquad
\gamma_i=c_{q_i}(d_0).
}
\tag{168.16}
$$
这些量只需实际 $Q$-单位及有限域幂符号。
未经除去 $q_i$ 赋值就把 $u_{j,\nu}$ 约化，会失去定义；
也不能在尚未证明下降的扩域内直接读取剩余符号。
(168.11) 和未分歧二次限制已保证这里的下降与精确因子。

## 4. 全局互反确定完整首差的有限分量

记 $H_Q$ 为 $W$ 上的全局空间：在 $p$ 局部为零，
在 $2$ 自动为零，在 $2,p,Q$ 外不分歧，在 $Q$ 不加限制。
R161 的最小严格 Selmer 为零，故奇异映射是单射，且其像准确为
$$
H_Q\xrightarrow{\sim}
\{(b_i)\in\mathbb F_p^r:\ \sum_i\gamma_i b_i=0\}.
\tag{168.17}
$$
若 $c\in H_Q$ 在 $q_i$ 的坐标为 $(a_i,b_i)$，
则将它与各个 $d_j$ 作全局杯积，只有 $Q$ 项可能非零。
由 (168.8)、(168.12) 得
$$
0=2\left(a_j-\sum_i C_{ji}b_i\right).
$$
因此
$$
\boxed{\gamma\mathbf b=0,\qquad
       \mathbf a=C\mathbf b.}
\tag{168.18}
$$
这是真正完整全局类的有限分量，不只是奇异向量维数计数。
反过来，给定 $\gamma\mathbf b=0$，(168.17) 给唯一全局类，
其有限分量必为 $C\mathbf b$。

若换 $d_j$ 为 $d_j+t_jd_0$，则
$$
C_{ji}\longmapsto C_{ji}+t_j\gamma_i.
\tag{168.19}
$$
故第二个等式只有在同时保留第一个齐次等式时才与选择无关。
不能丢掉旧 Robert 行后把任意一个 $C$ 当成独立规范矩阵。
R164 的小惰性单位行与 Gaussian 行也应继续保留；
它们是同一实际惯性权重的额外约束。

## 5. 实际 Tate Frobenius 给非齐次右端

现在令 $E$ 为 R19 的任一实际原始解对应的曲线，定义
$$
n=\min_{q\mid Z}v_p(pv_q(Z)),\qquad
R=\prod_{\substack{q\mid Z\\v_p(pv_q(Z))=n}}q.
\tag{168.20}
$$
本节假设 $R$ 的全部素因子在 $K$ 惰性，取 $Q=\{q:q\mid R\}$。
$Z$ 允许另外含有更高 $p$ 深度的分母素数。

R114、R128 给一个全局同构 $E[p^n]\simeq A[p^n]$。
选择整基把它写为
$\rho_E\equiv\rho_A\bmod p^n$，首差 cocycle 为
$$
c_E(\sigma)=
\frac{\rho_E(\sigma)\rho_A(\sigma)^{-1}-1}{p^n}\bmod p
=x_E(\sigma)J+c_W(\sigma).
\tag{168.21}
$$
R161 已证明 $c_W\in H_Q$，且对每个 $q_i\mid R$，
$$
b_{q_i}(c_W)=\epsilon_i x_i,\qquad x_i\ne0,
\tag{168.22}
$$
其中 $\epsilon_i=+1$ 表示 $E$ 在 $q_i$ 分裂乘法，
$\epsilon_i=-1$ 表示非分裂乘法。
$x_i=x_E(\tau_{q_i})$ 使用 §1 的同一 tame 规范。

这里还必须使用完整 Tate 表示的 Frobenius 迹。
对任意算术 Frobenius 提升，$E$ 的两个对角角色为
$\epsilon_i\chi_p$ 和 $\epsilon_i$，因而
$$
\operatorname{tr}\rho_E(\varphi_{q_i})
     =\epsilon_i(q_i+1).
\tag{168.23}
$$
它不是坏约化 Euler 因子中的 $a_{q_i}(E)=\epsilon_i$。
另一方面 $A$ 的实际迹为零。模 $p^n$ 同构首先给
$$
p^n\mid q_i+1.
\tag{168.24}
$$
因此下式确实先在整数中相除，再约化：
$$
z_i=\frac{q_i+1}{2p^n}\pmod p.
$$
将 (168.21) 取迹，得到
$$
\operatorname{tr}\bigl(c_E(\varphi_{q_i})F_{q_i}\bigr)
=\epsilon_i\frac{q_i+1}{p^n}\pmod p.
$$
$J$ 分量与 $K_{q_i}$ 分量对 $F_{q_i}$ 的迹均为零，
$\operatorname{tr}(F_{q_i}^2)=2$，所以
$$
\boxed{a_{q_i}(c_W)=\epsilon_i z_i.}
\tag{168.25}
$$
这是本文加入的实际 Frobenius 输入。

合并 (168.18)、(168.22)、(168.25)，令
$D_\epsilon=\operatorname{diag}(\epsilon_i)$，得到
$$
\boxed{
\gamma D_\epsilon\mathbf x=0,\qquad
C D_\epsilon\mathbf x=D_\epsilon\mathbf z,\qquad
x_i\in\mathbb F_p^\times.
}
\tag{168.26}
$$
R164 的联合矩阵仍作用在同一 $\mathbf x$ 上：
若其 Gaussian 行为 $A_{\rm G}$、惰性单位行为 $B$，还必须
$$
A_{\rm G}\mathbf x=0,\qquad B D_\epsilon\mathbf x=0.
\tag{168.27}
$$
这里包含原始第零行，故 (168.19) 不改变实际条件。
不能为 (168.26) 与 (168.27) 分别选不同的核向量。

## 6. 单个最小支撑的内在斜率

设 $R=q$。R161 已先迫
$\operatorname{loc}_q(d_0)=0$，即 $\gamma_q=0$。
此时 (168.10) 允许选择一个仅在 $q$ 具有单位奇异坐标的
真实 $q$-单位类 $d_q^\ast$，定义
$$
\lambda_q=c_q(d_q^\ast).
\tag{168.28}
$$
因为任意另一个选择只加 $d_0$，而 $d_0$ 在 $q$ 为零，
$\lambda_q$ 与 $d_q^\ast$ 的选择无关。
它由固定 $A,p,q$ 和 §1 的局部规范确定，与 $E$、
$\epsilon_q$、$v_q(Z)$ 无关。

更内在地，(168.17) 给 $H_{\{q\}}$ 一维，
其奇异坐标非零；按奇异坐标为 $1$ 归一化后，
有限坐标恰为 $\lambda_q$。
这个识别由 (168.8) 的全局互反证明，不是定义一个待选的
自由局部参数。

实际两种 Tate 符号在 (168.26) 中消去，给 (168.1)。
由于 $x_q\ne0$，准确有
$$
\boxed{
\begin{array}{c|c}
\lambda_q=0 & v_p(q+1)>n,\\
\lambda_q\ne0 & v_p(q+1)=n,\quad
x_q=\dfrac{q+1}{2p^n\lambda_q}\bmod p .
\end{array}}
\tag{168.29}
$$
这比只检查 $\operatorname{loc}_q(d_0)=0$ 多出实际限制。
尚未计算 $\lambda_q$ 时，不能据此宣布某个给定 $q$ 已被排除。

## 7. 惯性权重与真实判别式指数的 Weil 平方类

令
$$
m\in\mathbb F_p^\times
$$
为给定全局同构 $\phi:E[p]\to A[p]$ 的 Weil 配对乘数：
$$
e_{p,A}(\phi P,\phi Q)=e_{p,E}(P,Q)^m.
$$
残余绝对不可约使全局同构仅可再乘标量，因此 $m$ 的平方类固定。
对每个 $q_i\mid R$ 记
$$
\mu_i=\frac{pv_{q_i}(Z)}{p^n}\pmod p\in\mathbb F_p^\times.
\tag{168.30}
$$
该整数来自实际极小判别式
$v_{q_i}(\Delta_E)=pv_{q_i}(Z)$；不是任意替代的惯性系数。

**引理 168.1。** 在 §1 的 tame 规范下，
$$
\boxed{-\frac{2mx_i}{\mu_i}\in\mathbb F_p^{\times2}}
\tag{168.31}
$$
对每个最小惰性支撑素数成立，且不依赖 $\epsilon_i$ 的正负。

**证明。** 在 $(v_i,Jv_i)$ 基下写
$$
F_i=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
K_i=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
在 Tate 基 $(e_{\rm tor},e_{\rm quo})$ 中，用 (168.5) 使
配对为同一个 $\zeta_{q_i}$。
非分裂二次扭曲在惯性平凡且保持 Weil 配对。
首个非零惯性项为
$$
\mu_i\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$
环面线的残余 Frobenius 特征值是
$\epsilon_iq_i=-\epsilon_i$，不是 $\epsilon_i$。
由于两个 Frobenius 特征值不同，可将商向量加上环面向量的
倍数而取为另一个本征向量；此操作既不改变配对也不改变惯性矩阵。

若 $\epsilon_i=+1$，$\phi$ 在这两组配对基中的矩阵为
$$
M=\begin{pmatrix}0&b\\a&0\end{pmatrix},
\qquad a,b\ne0,\qquad \det M=-ab=m.
$$
共轭惯性矩阵得到
$\mu_i(a/b)E_{21}=x_i(J+K_i)=2x_iE_{21}$，故
$$
x_i=-\frac{\mu_i a^2}{2m}.
$$
若 $\epsilon_i=-1$，则
$M=\operatorname{diag}(a,b)$、$ab=m$，
而共轭惯性为
$\mu_i(a/b)E_{12}=x_i(J-K_i)=-2x_iE_{12}$。
再次得到同一公式，证明 (168.31)。证毕。

将 $v_i$ 换为 $tv_i$，$t\in\mathbb F_p^\times$，
使 $\zeta_{q_i}$ 变为 $\zeta_{q_i}^{t^2}$。
于是 tame 生成元及 $x_i$ 乘 $t^2$，
所有相应有限 Kummer 坐标除以 $t^2$，
所以 (168.26)、(168.29)、(168.31) 同时保持。
只选择 Frobenius 本征基而不追踪其 Weil 根，可能错误地引入
任意非平方比例；(168.4) 正是为避免该问题。

R22 已给本三族的固定平方类
$\sigma_E=(m/p)$：
$$
\begin{array}{c|c|c}
&p\equiv7\bmod8&p\equiv3\bmod8\\ \hline
\text{族 I}&+1&+1\\
\text{族 II}&+1&-1\\
\text{族 III，}X\text{ 奇}&+1&-1\\
\text{族 III，}X\text{ 偶}&+1&+1
\end{array}
\tag{168.32}
$$
这些是实际全局同构的乘数，不可针对每个支撑素数重新选择。
相应地，多素数矩阵问题除 $x_i\ne0$ 外还必须满足
$$
\left(\frac{-2x_i/\mu_i}{p}\right)=\sigma_E
\quad\text{对所有 }i.
\tag{168.33}
$$

## 8. 单支撑的明确指数判据

在 §6 的单最小支撑条件下，如果 $\lambda_q\ne0$，
(168.29) 与 (168.31) 合并为
$$
\boxed{
-\,m\,
\frac{(q+1)/p^n}{\lambda_q\,\mu_q}
\in\mathbb F_p^{\times2},\qquad
\mu_q=\frac{pv_q(Z)}{p^n}.
}
\tag{168.34}
$$
等价地，消去未知的平方倍乘数，
$$
\boxed{
\left(\frac{-\,((q+1)/p^n)/(\lambda_q\mu_q)}p\right)
=\sigma_E.
}
\tag{168.35}
$$
分子在整数中先除 $p^n$；(168.29) 保证其约化非零。
若 $\lambda_q=0$，只能保留 $v_p(q+1)>n$ 与 (168.31)，
不能在 (168.34) 中除以零。

例如在真正的单素数分母 $Z=\pm q^e$ 中，
$n=1+v_p(e)$、$\mu_q=e/p^{n-1}$，因此 (168.35) 直接约束
原始三族的整数指数 $e$。当 $g=\gcd_{\ell\mid Z}v_\ell(Z)$
为 $1$ 或 $3$ 且分母单素数时，$e$ 就分别为 $1$ 或 $3$；
这时右端及 $\mu_q$ 已固定，不是任意可调的局部量。
若只是最小支撑 $R=q$ 而 $Z$ 还含其他高深度素数，
则仍须使用实际 $v_q(Z)$，不能擅自把它改为 $g$。

本文没有声称 (168.35) 对全部 $q$ 都不相容。
其额外性在于：旧 Robert 零列仅允许任意非零的奇异权重，
而实际 Frobenius 将该权重确定为 (168.29)，
Weil 配对再判断它是否可能来自给定整数判别式指数。

## 9. 与有限零列及高阶可积性的边界

R164 的真复共轭论证只对预先固定的有限组不分歧类给无限零列。
这里的 $d_q^\ast$ 随新支撑 $q$ 变化，并且在 $q$ 本身分歧；
其自局部值 $\lambda_q$ 不受那个固定有限合成域的零列结论控制。
所以不能从 R164 推出 (168.1) 或 (168.34) 自动相容。

反过来，即使这些新等式在第一层相容，也没有得到实际椭圆曲线，
更没有得到原始三族的整数解。一个固定正素数 $q$ 的整数 $q+1$
非零，故它不可能在所有 $p$ 幂层都等于零。
各个有限层分别使用 Chebotarev 找到的新素数，不能拼成同一个
固定 $q$ 的无限层可积 Tate 表示。
本文只确定第一非零差异层的必要条件；后续层还必须保留真正的
变形相容性、完整 Tate 结构及 R19 的原始整数方程。

当前仍未得到某个 $\lambda_q$ 的新数值、矩阵 $C$ 的统一非退化性，
或变化支撑的全局不可积定理。这些缺口与本文已经证明的
非齐次方程及 Weil 平方类限制严格分开。

## 10. 引用定位

- R161 §§2–6：最小 $R=T$、严格 $p$ 条件、唯一对偶线、
  实际 Tate 首差和局部维数。
- R163 §§1–3：$\operatorname{Cl}(\mathscr F)[p]$ 的 $W$ 型消失；
  §§4–6：全 $p$ 原始 Robert 生成元。
- R164 §§3–5：放松对偶条件的精确序列、真实 $S$-单位主化、
  以及共同权重的 Gaussian / 惰性单位矩阵。
- R22 §§1–4：好超奇异局部 Weil 乘数与三族的固定平方类。
- J. S. Milne，*Class Field Theory*，v4.03，
  [作者全文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)，
  III Proposition 3.6、Lemma 3.7（正文页 109–110），
  III §4 Steps 2–3、Theorem 4.4(b)（正文页 112–113）：
  arithmetic Artin、Kummer 杯积与反交换规范。
- J. Nekovář、A. Plater，*On the parity of ranks of Selmer groups*，
  Asian J. Math. **4** (2000), 437–498，
  [作者全文](https://webusers.imj-prg.fr/~jan.nekovar/pu/parity.pdf)，
  [出版商全文](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806253860626862081-1806253860626862081-42879e7fcf2dc137962fe36b5f0f30b6.pdf)，
  §1.2.7（发表页 443）给 (168.5) 的明确 Weil 配对规范。
  本文只引用这一规范，不调用该文的 ordinary、Hida 或秩结论。
