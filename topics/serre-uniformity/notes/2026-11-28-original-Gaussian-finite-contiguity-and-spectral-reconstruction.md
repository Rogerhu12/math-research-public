# 原 Gaussian 固定权 contiguity 与有限本征重建

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明的范围。** 本文从 R1116 的同一个有限 Kronecker gauge 出发，
先给保持总权 $p+1$ 的完整 contiguity，再把其中的参数导数全部消去为
一个有显式单位逆的有限下降重建。它唯一恢复全部原 centered profile
矩阵；最高 principal 中项作为边界保留，未进入实际 $V$ 的角色仍不补入。
全程只用 $G_4,\ldots,G_{p-3}$。

本征算子的可逆性不等于实际 good 行的子矩阵可逆。
本文没有证明该子矩阵的核避开二根 Hankel 轨迹，也未证明标签注入。
最后给出原矩阵的精确有限形式，供后续做真正的 minor 或余核证明；
不把点值相等沿另一个参数微分。

## 1. 同一个原 centered 总权层

保持 R1116 的原模型、参数和规范：
$$
p=4k+3\ge41,\qquad E_a:y^2=x^3+ax,\qquad
a\in\mathbf F_p^\times,\qquad D\Psi=\delta\in\mathbf F_p^\times,
$$
$$
\mathscr K(T,U)=\frac{\sigma(T+U)}{\sigma(T)\sigma(U)}
=T^{-1}+U^{-1}+\sum_{\ell\ge1}P_\ell(T,U),
\qquad \deg P_\ell=4\ell-1.
\tag{F.1}
$$
每个 $P_\ell$ 对称。这里只使用 $\ell\le k$，
其 Hurwitz 总权至多 $4k=p-3$，所有输入均由 R1116 付清。

置 $\mathscr K_w=e^{wTU}\mathscr K$。
先在原特征零 lift 中取齐次层 $F_n(w)$，再取 centered 差。
本篇使用的 $p$ 次层准确为
$$
\begin{aligned}
M_w(T,U)&=F_p(w)-F_p(0)\\
&=\sum_{h=1}^{k}\frac{w^{2h}}{(2h)!}(TU)^{2h}P_{k+1-h}(T,U)\\
&\quad+\frac{w^{2k+2}}{(2k+2)!}(TU)^{2k+2}(T^{-1}+U^{-1}).
\end{aligned}
\tag{F.2}
$$
这是可约化的真正多项式。未单独约化未知的 $F_p(0)=P_{k+1}$；
后者涉及权 $p+1$，不在本篇安全输入中。

记
$$
A_R(w)=[T^{p-R}U^R]M_w,\qquad A_R=A_{p-R},
\tag{F.3}
$$
越出 $0\le R\le p$ 时记为零。令 $\Delta_0 f=f(w)-f(0)$。
原实际 good 集合及全部尺度仍是
$$
\mathcal G_p=\{R:\ 2\le R\le p-3,\ R\text{ 偶},\
 V_{\omega^R}\ne0,\ p\nmid B_R\},
$$
$$
w=\gamma t_*,\quad
\gamma=\delta\lambda\beta_0^{1-p},\quad
N_R=\frac{(\beta_0^{p+1})^R\delta^{R-1}}{2b_{\omega^R}R!},
\qquad
\Pi_R(t_*^2)=N_R A_R(w).
\tag{F.4}
$$
这里只对实际 good 的 $b_{\omega^R}$ 反除。
特别 $R=(p+1)/2=2k+2$ 不在原实际 $V$ 中。

## 2. 完整固定权 contiguity 与高尾的准确消失

原 sigma 的 logarithmic derivative 给
$$
(\partial_T-\partial_U)\mathscr K_w
=\{\zeta(U)-\zeta(T)+w(U-T)\}\mathscr K_w.
\tag{F.5}
$$
乘以 $TU$，取总次数 $p+1$，再取 centered 差。
$\zeta$ 的两个主极给 $(T-U)M_w$。
对每个 $j\ge1$，其 $G_{4j}$ 项为
$(T^{4j}U-TU^{4j})\Delta_0F_{p-4j}$。
又
$$
\partial_w^{2j}F_p(w)=(TU)^{2j}F_{p-4j}(w).
$$
所以读取 $T^{p-r+1}U^r$ 后，在 $\mathbf F_p$ 中准确得到
$$
\boxed{
\begin{aligned}
(2-r)A_{r-1}-(r+1)A_r
&=w(A'_{r-1}-A'_r)\\
&\quad+\sum_{j=1}^{k}G_{4j}\,
 \Delta_0\partial_w^{2j}
 (A_{r+2j-1}-A_{r-2j}).
\end{aligned}}
\tag{F.6}
$$
约化前左侧第一系数是 $p-r+2$。
将 $\zeta$ 的主极移左，正是从原导数系数得到所示的 $2-r$、
$-(r+1)$。$\Delta_0\partial_w^{2j}$ 必须保留；
对已经 centered 的 $A_R$ 求偶阶导数仍可能产生常数。

潜在的 $j=k+1$ 项涉及 $G_{4k+4}=G_{p+1}$，
但它乘的是
$$
F_{-1}(w)-F_{-1}(0)=0
$$
这一特征零中的恒等零。因此它在约化之前已消失，
不是把一个未付的 $G_{p+1}$ 设为零。
更大的 $j$ 只遇到不存在的低于 $-1$ 的齐次层。
所有存留的 $G$ 权至多 $p-3$，所有参数导数阶至多 $2k<p$。

式 (F.6) 是带完整长尾的微分 contiguity。
在尚未作下面的逐系数重建前，不能把它解释为两个参数点值的三项递推。

## 3. 真正的有限本征算子

以下辅助变量 $X=U/T$ 只表示原两个核变量的比，
与曲线的 Weierstrass $x$ 和实际 coarse 坐标都无关。
置
$$
m_0=(p-1)/2=2k+1,\qquad
\mathscr S_p=\{f\in\mathbf F_p[X]_{\le p}:f(X)=X^p f(X^{-1})\}.
$$
该空间维数为 $m_0+1$。定义
$$
\mathcal L=1+\frac{X(1+X)}{1-X}\frac{d}{dX}.
\tag{F.7}
$$
它确实是 $\mathscr S_p$ 上的多项式算子。
由对称性，
$2f'(1)=pf(1)=0$，故显示分母可除；
对 $X\mapsto X^{-1}$ 微分又说明 $\mathcal Lf$ 仍在 $\mathscr S_p$。

其完整本征基是
$$
E_r(X)=X^r(1+X)^{p-2r},\quad 0\le r\le m_0,
\qquad
\boxed{\mathcal L E_r=(r+1)E_r.}
\tag{F.8}
$$
确实 $E_r'/E_r=r(1-X)/(X(1+X))$ 于特征 $p$。
每个 $E_r$ 的最低次恰为 $X^r$，系数一，
故它们构成所示空间的基，不需要额外行列式假设。

对 $1\le h\le k$，令
$$
\mathscr V_h=\mathscr S_p\cap X^{2h}\mathbf F_p[X]
=\operatorname{span}\{E_{2h},\ldots,E_{m_0}\}.
$$
于是
$$
\boxed{\quad
(\mathcal L-2h)|_{\mathscr V_h}\text{ 可逆，特征值为 }
1,2,\ldots,2(k+1-h).
\quad}
\tag{F.9}
$$
全部数严格小于 $p$。这里从未反除某个 Hurwitz 值、
Bernoulli 值、原 bare 范数或未知 minor。

## 4. 无参数导数的唯一下降重建

写
$$
M_w(1,X)=\sum_{h=1}^{k+1}\frac{w^{2h}}{(2h)!}\,\mathsf B_h(X),
$$
$$
\mathsf B_h=X^{2h}P_{k+1-h}(1,X)\in\mathscr V_h\quad(1\le h\le k),
\qquad
\boxed{\mathsf B_{k+1}=X^{2k+1}(1+X)=E_{m_0}.}
\tag{F.10}
$$
最高项是已付 principal，不属于按 $X^{2h}$ 定义的
$\mathscr V_{k+1}$。它的特征值为 $2k+2$，
正是唯一需另行固定的共振边界。

记对称 Laurent 多项式
$$
\Phi_j(X)=X^{1-2j}(1+X+\cdots+X^{4j-2}).
\tag{F.11}
$$
将 (F.6) 对所有 $r$ 合并，或直接由 (F.5) 换成 $X$，
得到
$$
\mathcal L M_w(1,X)
=w\partial_wM_w(1,X)
-\sum_{j=1}^{k}G_{4j}\Phi_j(X)
 \Delta_0\partial_w^{2j}M_w(1,X).
$$
逐个读取正次的 $w^{2h}/(2h)!$，$1\le h\le k$，即得
$$
\boxed{
\mathsf B_h
=-(\mathcal L-2h)^{-1}
  \sum_{j=1}^{k+1-h}G_{4j}\Phi_j\,\mathsf B_{h+j}.
}
\tag{F.12}
$$
没有剩余的 $w$ 导数。

右侧输入确在 $\mathscr V_h$。
若 $h+j\le k$，最低 $X$ 次至少为 $2h+1$；
若 $h+j=k+1$，principal 的最低次给准确的 $2h$。
各乘积保持对称性，因此其最高次也至多为 $p-2h$。
结合 (F.9)，从唯一的 (F.10) 边界向下，全部
$\mathsf B_k,\ldots,\mathsf B_1$ 被唯一确定。

**$h=0$ 不在 (F.12) 的范围内。**
原 centered 层的 $w^0$ 系数恒零；$\Delta_0$ 正好删除各导数产生的
常数项，故在该层没有一个可外推的下降方程。
若去掉 $\Delta_0$ 后擅取 $h=0$，会错误引入
$G_{p+1}\Phi_{k+1}\mathsf B_{k+1}$；
这个乘积一般不为零，本文既不计算也不删除它。
未约化的原 $F_p(0)$ 整层继续保留为边界之外的对象。

## 5. 标量多项式形式：所有除数都有明确单位界

再置
$$
\xi=\frac{X}{(1+X)^2}.
$$
它仍是核变量的辅助比值，不是实际 Gaussian deformation 参数。
由 (F.8)，$E_r=(1+X)^p\xi^r$，
所以在这个表示中 $\mathcal L=1+\xi\partial_\xi$。

唯一写
$$
P_\ell(1,X)=(1+X)^{4\ell-1}Q_\ell(\xi),
\qquad \deg Q_\ell\le2\ell-1\quad(1\le\ell\le k),
$$
并以 $Q_0(\xi)=\xi^{-1}$ 编码 principal。
这个 $Q_0$ 不是被禁止的 gauge 常数层 $h=0$。
令
$$
H_0=1,\qquad H_\ell(\xi)=\xi Q_\ell(\xi)\quad(\ell\ge1).
$$

定义完全显式的整数多项式
$$
\begin{aligned}
C_j(\xi)&=\xi^{2j-1}\Phi_j(X)\\
&=\sum_{a=0}^{2j-1}(-1)^a
 \binom{4j-2-a}{a}\xi^a.
\end{aligned}
\tag{F.13}
$$
例如 $C_1=1-\xi$；这里只用符号恒等式，不做有限素数测试。
证明可取 $u+v=1,uv=\xi$，则
$C_j=(u^{4j-1}-v^{4j-1})/(u-v)$。

(F.12) 等价于下列有限卷积：
$$
\boxed{
H_\ell'(\xi)
=-\sum_{j=1}^{\ell}G_{4j}C_j(\xi)H_{\ell-j}(\xi),
\qquad H_\ell(0)=0,\quad 1\le\ell\le k.
}
\tag{F.14}
$$
右侧次数至多为 $2\ell-1$，所以积分只除以
$1,\ldots,2\ell$，全部为原 $p$ 单位。
这给另一种完全显式的唯一重建，不会因某个 $G_{4j}=0$ 而失效。

记
$$
J_j(\xi)=\int_0^\xi C_j(t)\,dt
=\frac{1-u^{4j}-v^{4j}}{4j}.
$$
$u,v$ 的对称式保证右侧是 $\xi$ 多项式；
$4j\le p-3$ 也是单位。以形式记账变量 $q$ 表示全部有限层，
$$
\boxed{
\sum_{\ell=0}^{k}H_\ell(\xi)q^\ell
\equiv
\exp\left(-\sum_{j=1}^{k}G_{4j}J_j(\xi)q^j\right)
\pmod{q^{k+1}}.
}
\tag{F.15}
$$
只用到指数展开的阶乘 $0!,\ldots,k!$。
这里 $q$ 不是 Tate 参数、辅助素数或新的数学执行输入。

(F.15) 还有原 sigma 的直接核对：
$\log(\sigma(t)/t)=-\sum G_{4j}t^{4j}/(4j)$，
令 $s=T+U,u=T/s,v=U/s$，则
$$
\xi s\,\mathscr K(T,U)
=\exp\left(-\sum_{j\ge1}G_{4j}J_j(\xi)s^{4j}\right).
$$
只读 $s^{4k}$ 以内，恰给 (F.15)，全部常数由
$\sigma'(0)=1$ 固定。这份核对同样没有读权 $p+1$。

## 6. 原实际 good 矩阵的精确有限形式

若
$$
Q_\ell(\xi)=\sum_{a=0}^{2\ell-1}q_{\ell,a}\xi^a,
\qquad \ell=k+1-h,
$$
则由 (F.8)、(F.10)，原 $w^{2h}$ 列准确为
$$
\boxed{
\mathsf M_{R,h}
=\frac1{(2h)!}\sum_{a=0}^{2\ell-1}q_{\ell,a}
 \binom{p-4h-2a}{R-2h-a},
\qquad 1\le h\le k.
}
\tag{F.16}
$$
下标越出普通二项式范围时该项为零。
所有上标都在 $[1,p-4]$；没有含 $p$ 的阶乘约分。

principal 列另为
$$
\mathsf M_{R,k+1}
=\frac{\mathbf1_{R=2k+1}+\mathbf1_{R=2k+2}}{(2k+2)!}.
\tag{F.17}
$$
它对每个实际偶 good 角色为零，因为 $2k+2$ 实际缺席。
但它仍是 (F.12) 不可删除的重建边界。
因此既不能增添一个观测角色，也不能从原重建中删掉中项。

令实际 coarse 参数为 $z=t_*^2$，则完整原式为
$$
\Pi_R(z)
=N_R\sum_{h=1}^{k}\mathsf M_{R,h}(\gamma^2z)^h,
\qquad R\in\mathcal G_p.
\tag{F.18}
$$
这保留两条实际 Gaussian twist 上各自的原
$\beta_0,\lambda,b_{\omega^R}$，不增加未付的跨 frame 缩放对称性。

为明确余下的有限问题，令 $Z=\gamma^2z$、$Z'=\gamma^2z'$，
且 $Z\ne Z'$。置
$$
S=Z+Z',\quad P=ZZ',\qquad
b_0=1,\quad b_1=S,\quad b_{n+2}=Sb_{n+1}-Pb_n.
$$
则 $b_n=(Z^{n+1}-Z'^{n+1})/(Z-Z')$，原全部观测相等当且仅当
$$
\sum_{h=1}^{k}\mathsf M_{R,h}b_{h-1}=0
\qquad\text{对每个 }R\in\mathcal G_p.
\tag{F.19}
$$
这里的行必须是原实际 mask。除 $S^2-4P\ne0$ 外，
还须保两点所属的实际 coarse 线范围。
$P=0$ 的中心/非中心点对合法，其 Hankel 秩可为一；
不能因通常称“rank-two locus”而删除该边界。

本文新增的是 (F.9)、(F.12)、(F.14)–(F.16) 给出的
完整、唯一、安全权重的有限矩阵重建。
它为后续实际行余核与二根轨迹的交提供确定输入，
没有证明 (F.19) 无解。非恒定行的个数、
$\mathcal L-2h$ 的单位谱、全空间的有限重建，
均不能单独替代指定 masked minor 或共同纤维排除。

## 来源与独立核对

- [R1116](../results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)
  §§1、7–9：原短 carry、完整 good mask、全部 gauge 系数及尺度、
  有限差 (1116.47)–(1116.48)。
- [R1129](../results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)：
  原 sigma heat、逐行准确 degree 与已付非恒定性范围；本文不扩大其结论。
- 式 (F.5) 及 (F.15) 的独立核对均直接来自同一个原 sigma。

o2_high_coefficient 逐式纸推；o1_theta 已独立核准
完整 contiguity、主极移项、centered 高尾边界、本征基与
$1\le h\le k$ 的单位逆和 principal 支撑。无数学程序执行。

root 全文纸核候选 38bc87f87c78410ae8470dfdfdc6962bedb0a612：直接从齐次 (F.5) 再得 (F.6)/(F.12)，逐式核 (F.13)–(F.16) 的指数、次数、积分分母与 sigma 常数；o1_theta 已完成 §§5–6 的 exact 转录核对。全稿明确不外推 h=0，保未约化高常数层、原缺中项及 P=0 点对。


## 7. 原偶角色的 Newton 节点与实际余核

置 $m=(p-1)/2=2k+1$。对 $1\le r\le m$ 以及原偶数
$2\le R\le p-3$，(F.9) 的本征列满足
$$
[X^R]E_r(X)=
\frac{(-1)^rR}{(2r-1)!}
\prod_{a=1}^{r-1}(R^2-a^2).
\tag{F.20}
$$
在 $r\le R\le p-r$ 的范围，这就是
$\binom{p-2r}{R-r}=(-1)^r\binom{R+r-1}{2r-1}$。
若 $R<r$，右侧的 $a=R$ 因子为零；若 $R>p-r$，
则 $a=p-R$ 因子为零。因此 (F.20) 也包括两个越界范围。
$r=0$ 的 $E_0=1+X^p$ 单独处理；其所有内部原偶行均为零。

令 $\mathcal N=X\partial_X$，直接求导给
$$
\mathcal N^2E_r=r^2E_r-2r(2r+1)E_{r+1}.
\tag{F.21}
$$
$r=m$ 时第二项因 $2m+1=p$ 为零，故不需要定义 $E_{m+1}$。
这是真正固定总次数 $p$ 的算子，并未增加横向权重。

原偶数 $R=2,4,\ldots,p-3$ 的平方恰遍历
$\mathbf F_p^{\times 2}\setminus\{1\}$。实际缺席的中间角色
$R=(p+1)/2$ 对应节点 $1/4=m^2$。记
$$
Q_{\mathrm{grid}}(Y)
=\frac{Y^m-1}{(Y-1)(Y-1/4)}.
\tag{F.22}
$$
所有因子不同；这仍只是原可能节点的 ambient grid，
不是把其中每个节点都声明为实际 good 角色。

在 $\mathscr S_p\cap X^2\mathbf F_p[X]=
\langle E_2,\ldots,E_m\rangle$ 上定义
$$
\mathscr E(E_r)
=\frac{(-1)^r}{(2r-1)!}
  \prod_{a=2}^{r-1}(Y-a^2)
\pmod{Q_{\mathrm{grid}}}.
\tag{F.23}
$$
于是原行评价等于 $R(R^2-1)\mathscr E(f)(R^2)$；
这个前因子在全部节点上均为单位。
$\mathscr E(E_m)$ 是非零标量乘 $Q_{\mathrm{grid}}$，
所以 principal 的确映为零。原空间模去这一 principal 后，
(F.23) 给出与 $\mathbf F_p[Y]/(Q_{\mathrm{grid}})$ 的同构；
(F.21) 对应在该商中乘以 $Y$。
这只是确定的同权有限模，不把 $\mathcal L$ 或参数导数
自动加到可观测行中。

取 $\overline{\mathsf B}_h=\mathscr E(\mathsf B_h)$，
并以 (F.19) 中的同一 $S,P,b_n$ 定义
$$
\mathscr D_{S,P}(Y)=
\sum_{h=1}^{k}\frac{b_{h-1}}{(2h)!}\,
       \overline{\mathsf B}_h(Y),\qquad
Q_{\mathrm{good}}(Y)=
\prod_{R\in\mathcal G_p}(Y-R^2).
\tag{F.24}
$$
所有实际观测相等准确等价于
$Q_{\mathrm{good}}\mid\mathscr D_{S,P}$，
其中采用次数小于 $\deg Q_{\mathrm{grid}}$ 的代表。
没有扩大 $\mathcal G_p$。特别，
$$
\mathscr D_{S,P}(4)=-\frac{G_{p-3}}{12}\ne0.
\tag{F.25}
$$
证明是 $[X^2]\mathsf B_1=-G_{p-3}$、
其余 $\mathsf B_h$ 在 $X=0$ 的阶至少四，再除
$2!\,R(R^2-1)=12$。这个值与 $S,P$ 无关。
因此若 $R=2$ 实际出现，直接得到 R1127 的 affine 分离；
当它实际缺席时，不能把 (F.25) 当作一个已观测方程。

## 8. 两个实际低指标把同一 frame 的残余点对固定

本节给出一个有明确 Bernoulli 条件的有限纤维约束，
不声称这些条件对所有素数成立。
[R1128](../results/R1128-all-prime-linear-good-cuspidal-rank.md)
的低指标判据对 $R=4,6$ 给出
$$
\begin{split}
p\mid B_{p-7}&\ \Longrightarrow\ 4\in\mathcal G_p,\\
p\mid B_{p-11}&\ \Longrightarrow\ 6\in\mathcal G_p .
\end{split}
\tag{F.26}
$$
这里“$p\mid B_n$”指这个 $p$ 整有理数为非单位。
$B_4=-1/30$、$B_6=1/42$ 在 $p\ge41$ 时均为单位，
所以两条确是原实际出现且 good 的角色。
这些 Bernoulli 条件与下面的 Gaussian Hurwitz 系数单位性是两回事。

从原 $x''=6x^2+2a$ 逐项得到
$G_8=a^2/525$、$G_{12}=-2a^3/53625$。
再用 R1116 的同一规范反射
$G_{p+1-r}=-(r-1)!\delta^{1-r}G_r$，准确有
$$
G_{p-7}=-\frac{48a^2}{5\delta^7},\qquad
G_{p-11}=\frac{96768a^3}{65\delta^{11}}.
\tag{F.27}
$$
两者对全部原 $p\ge41$ 都是单位。
例如 $96768=2^9\,3^3\,7$；所有分母的素因子均小于 $41$。
反射只用了 $r=8,12\le p-3$，没有高权 carry。

记
$c_s=[T^{p-4-s}U^s]P_k$、
$d_s=[T^{p-8-s}U^s]P_{k-1}$，并写
$\mathcal A_R(Z)=A_R(w)$，$Z=w^2$。
(F.2) 的完整两条低行恰为
$$
\begin{split}
\mathcal A_4(Z)&=\frac{c_2}{2}Z-\frac{G_{p-7}}{24}Z^2,\\
\mathcal A_6(Z)&=\frac{c_4}{2}Z+\frac{d_2}{24}Z^2
                         -\frac{G_{p-11}}{720}Z^3.
\end{split}
\tag{F.28}
$$
这些是整个原 profile 行，不只是其首项：
其余 $h$ 超过原支撑而为零。最高系数由 (F.27) 为单位。

假设 (F.26) 的两个 Bernoulli 条件同时成立。
在一个固定的原 marked Gaussian frame 内，
取实际允许的两个不同点 $Z,Z'$。
若它们的全部实际 good 坐标相等，则 (F.28) 先后强迫
$$
\boxed{
\quad S=Z+Z'=\frac{12c_2}{G_{p-7}},\qquad
P=ZZ'=S^2-\frac{30d_2S+360c_4}{G_{p-11}}.\quad}
\tag{F.29}
$$
证明只需分别把两行差除以 $Z-Z'$：
第一行固定 $S$，第二行使用
$(Z^3-Z'^3)/(Z-Z')=S^2-P$ 固定 $P$。

因此在这个 frame 中，所有非对角共同纤维的无序点对
**至多一个**，且只能是 $X^2-SX+P$ 的两个根。
还必须检查判别式非零、两个根属于原实际 coarse 范围，
以及 (F.24) 的其余实际 good 行。
$P=0$ 的中心/非中心情形仍包含在内。
(F.29) 没有证明这个唯一候选不可行。

这里保留 $N_R$ 与 $\gamma$ 的原单位归一：
实际 profile 为
$\Pi_R(z)=N_R\mathcal A_R(\gamma^2z)$。
在同一 frame 比较时可约去两点共同的 $N_R$。
两个原 Gaussian twist line 各有自己的源尺度，
其合并覆盖的 coarse 范围不能只用单条 fine 平方像替代。
在支付跨 frame 的完整输运前，本节不宣称
“整个原 coarse 空间至多一个共同点对”，也不删除 $S=0$。

## 9. 一个固定的实际二次行 minor

还有一个不同、明确的实际 mask 分支：
$p\mid B_{p-7}$ 且 $p\nmid B_{p-5}$。
此时低 $R=4$ 和 forced $R=p-5$ 都是实际 good 行。
由 $P_\ell$ 的对称性，第二条完整行是
$$
\mathcal A_{p-5}(Z)=\frac{c_3}{2}Z+\frac{d_1}{24}Z^2.
\tag{F.30}
$$
故两行的原 affine 消元为
$$
d_1\,\frac{\Pi_4(z)}{N_4}
+G_{p-7}\,\frac{\Pi_{p-5}(z)}{N_{p-5}}
=\frac{\Delta_{\mathrm{low}}}{2}\gamma^2z,
\qquad
\Delta_{\mathrm{low}}=c_2d_1+G_{p-7}c_3.
\tag{F.31}
$$
原二次行系数矩阵的行列式恰为
$\Delta_{\mathrm{low}}/48$。
因此 $\Delta_{\mathrm{low}}\ne0$ 时，这两条实际行已分离
同一 marked frame 的点。若 $\Delta_{\mathrm{low}}=0$，
则两行确切比例
$\mathcal A_{p-5}=-(d_1/G_{p-7})\mathcal A_4$；
不能因为两条都实际出现就略过这个退化支。

(F.31) 给出一个固定 degree-one 行组合及其准确待付 minor，
但本节未证明该 minor 为单位。
它与 (F.29) 是两个不同 Bernoulli 分支的结论，
均不借未出现的低角色或非 good 的高角色补行。


root 对候选 b39a977ce9f3a9f0af4bb20c4a81b16fa5d500e5 的 F.20–F.31 纸核：Newton 两个越界范围、principal 余核、两个 Hurwitz 反射因子、完整低行及消元均相容。o1_theta 同时核准 mask 与两种 Bernoulli 分支；无数学执行。低行的已证纤维结论另登记为 R1135。


## 10. 被 Newton 商删除的完整 principal 系数

本节确定 (F.23) 删除的整列及其全部低层贡献。
仍只读原 centered 层 (F.2)，不读取未约化的 $P_{k+1}$。
令 $Z=w^2$、$Z'=w'^2$、$Z\ne Z'$，并沿用 (F.19) 的
$b_n=(Z^{n+1}-Z'^{n+1})/(Z-Z')$。在原完整对称空间中置
$$
\mathsf F_{Z,Z'}(X)
=\frac{M_w(1,X)-M_{w'}(1,X)}{Z-Z'}
=\sum_{h=1}^{k+1}\frac{b_{h-1}}{(2h)!}\mathsf B_h(X).
\tag{F.32}
$$
记其本征展开中的 principal 系数为
$C_{\mathrm{pr}}=[E_m]\mathsf F_{Z,Z'}$，$m=2k+1$。
这个系数包括 $h\le k$ 的贡献；它一般不等于
$b_k/(2k+2)!$。

### 10.1 原 sigma 的反对角一阶读取

以 $q$ 表示本小节的形式核变量，定义
$$
a_\ell=[q^{4\ell}]
       \left(\frac{q}{\sigma(q)}\right)^2,\qquad 0\le\ell\le k,
\qquad a_0=1.
$$
由 (F.15) 前的原 sigma 规范，
$$
\left(\frac{q}{\sigma(q)}\right)^2
\equiv
\exp\left(\sum_{j=1}^k\frac{G_{4j}}{2j}q^{4j}\right)
\pmod{q^{4k+1}}.
\tag{F.33}
$$
这里全部 $G$ 的权至多 $p-3$；指数展开最多用 $k!$，
所以每个 $a_\ell$ 都由原安全输入唯一确定。

在原特征零 lift 中置 $s=T+U$、$q=(T-U)/2$。
sigma 的奇性给准确恒等式
$$
\mathscr K_w(T,U)
=-\frac{\sigma(s)e^{\,w(s^2/4-q^2)}}
        {\sigma(q+s/2)\sigma(q-s/2)}.
$$
因此在 $s=0$ 的一阶项是
$-s e^{-wq^2}/\sigma(q)^2$。
先取 centered 差，再读取总次数 $p$，所得一阶系数为
$$
-\mathcal B(w),\qquad
\mathcal B(w)
=[q^{p-1}]
 \frac{\cosh(wq^2)-1}{\sigma(q)^2}.
\tag{F.34}
$$
把指数换成 $\cosh$ 并未删除项：
$q^{-2}(q/\sigma(q))^2$ 只含次数 $4\ell-2$，
而 $p-1=4k+2$，所以所读的指数项必为偶数 $2h$。
减一又排除了本来会涉及 $a_{k+1}$ 的常数层。
因而 (F.34) 在约化前就只含 (F.33) 的安全系数。

对 $r<m$，$E_r(X)$ 在 $X=-1$ 至少三重消失；
而 $m$ 为奇数，$E_m'(-1)=(-1)^m=-1$。
在 $T=q,\ U=-q+s$ 中，
齐次 $p$ 次层的一阶 $s$ 系数是
$q^{p-1}\partial_XM_w(1,-1)$。
结合这两个负号，得到
$$
\boxed{
C_{\mathrm{pr}}
=\frac{\mathcal B(w)-\mathcal B(w')}{Z-Z'}
=\sum_{h=1}^{k+1}
 \frac{a_{k+1-h}\,b_{h-1}}{(2h)!}.}
\tag{F.35}
$$
最后一个求和式来自
$4\ell+4h-2=p-1$，即 $\ell=k+1-h$。
它明确保留所有较低层的原卷积。

还有一个独立的有限核对：在 (F.15) 中，
$J_j(\xi)$ 的最高项是 $-\xi^{2j}/(2j)$。
故 $H_\ell$ 的 $\xi^{2\ell}$ 系数恰为 $a_\ell$。
又
$$
\mathsf B_h=(1+X)^p\xi^{2h-1}H_{k+1-h}(\xi)
\quad(1\le h\le k),
$$
于是 $[E_m]\mathsf B_h=a_{k+1-h}$；
$h=k+1$ 的原 principal 对应 $a_0=1$。
这从 (F.15) 再次给出 (F.35)，没有添加新观测行。

### 10.2 完整 principal 恰是受限 Euler 的边界

暂不对 $Q_{\mathrm{grid}}$ 取商，把 (F.23) 的右侧视为多项式，
记为 $\widehat{\mathscr E}(E_r)$。由于 $m$ 为奇数，
$(p-2)!=1$ 在 $\mathbf F_p$ 中，且
$1^2,\ldots,m^2$ 恰遍历全部非零平方、$m^2=1/4$，所以
$$
\begin{aligned}
&R(R^2-1)(R^2-1/4)\,
       \widehat{\mathscr E}(E_m)(R^2)\\
&\qquad=
\frac{(-1)^m}{(p-2)!}
 R\prod_{a=1}^{m-1}(R^2-a^2)(R^2-1/4)
=-(R^p-R).
\end{aligned}
\tag{F.36}
$$
特别 $\widehat{\mathscr E}(E_m)=-Q_{\mathrm{grid}}$。
若 $\mathscr D_{S,P}$ 仍取 (F.24) 的最低次数代表，
则完整差商在取商之前恰为
$$
\widehat{\mathscr E}(\mathsf F_{Z,Z'})
=\mathscr D_{S,P}-C_{\mathrm{pr}}Q_{\mathrm{grid}}.
\tag{F.37}
$$
这说明原 $h=k+1$ 列以及各 $h\le k$ 的最高本征分量，
都通过同一个完整标量 (F.35) 被删除。

与 [R1154 §12](../results/R1154-original-Gaussian-first-profile-and-joint-finite-Gauss-moments.md)
的有限 Euler 算子比较，令 $\theta=T\partial_T$，把
$R$ 代为 $1-\theta$。在 $\mathbf F_p[T]$ 上
$\theta^p=\theta$，故
$$
(1-\theta)^p-(1-\theta)=0.
\tag{F.38}
$$
于是 (F.37) 中的整项 $C_{\mathrm{pr}}Q_{\mathrm{grid}}$
对该 Euler 读取恒为零。
这是原商映射的准确核边界；它不是由实际 good 行同值推出的
$C_{\mathrm{pr}}=0$，更不能改写成 $b_k=0$。
同样，(F.38) 是这个 Euler 算子的受限幂恒等式，
本文没有把它等同于原超奇异曲线不变导子的受限幂，
也没有据此构造两个形式群之间的映射。

本节新增的是可直接消费的原式 (F.35)–(F.37)：
完整被删列由原安全 sigma 系数和同一二根递推给出，
而它在有限 Euler 变换中的消失有精确的 $R^p-R$ 来源。
实际 good mask、$S=0$ 与 $P=0$ 边界均保持 (F.19)/(F.24) 的范围。
没有新增标签注入或共同纤维排除结论。

o2_high_coefficient 纸推；o1_theta 已独立核准
反对角 Jacobian、两个负号、全部低层卷积及 (F.36) 的单位因子。
无数学程序执行。


## 11. 同一有限对数的首 $p$ 边界与整形式群坐标障碍

本节继续使用同一个实际点对和 (F.32) 的完整本征展开
$\mathsf F_{Z,Z'}=\sum_{r=2}^m c_rE_r$。
它支付有限 Euler 读取在首次特征 $p$ 边界处的完整值；
不把原 good 行的缺项转化成一个未经证明的形式群映射。

### 11.1. 原有限对数的等价双曲正切读取

先在 $\mathbf Q_p[[t]]$ 中置
$$
f(t)=\tanh(t/2)=\frac{e^t-1}{e^t+1},
\qquad
f_{<p}(t)=\sum_{0\le j<p}[t^j]f(t)\,t^j.
$$
$f_{<p}$ 的系数都在 $\mathbf Z_p$，且它是次数至多 $p-2$
的奇多项式。这里只使用其有限约化；没有约化整个
不整的 $f(t)$。

R1154 §12 的原有限多项式 $E(T)$ 准确满足
$$
\boxed{\quad
E(T)=-2T[t^{p-1}]\sinh(Tt)\,\overline{f_{<p}}(t).
\quad}
\tag{F.39}
$$
例如对偶数 $4\le s\le p-1$，令 $R=p+1-s$。
原系数公式
$[t^{R-1}]f=2(2^R-1)B_R/R!$
以及 Wilson 恒等式 $R!(p-R)!\equiv R$，给
$$
-\frac{2[t^{R-1}]f}{(s-1)!}
=\frac{4(1-2^R)B_R}{R},
$$
这正是原 $E_s$。
$s=2$ 的 $B_{p-1}$ 分母由 $2^{p-1}-1$ 消去，准确给
$E_2=-4q_p(2)$；最高 $s=p-1$ 给 $E_{p-1}=-1$。
常数项和奇次项均为零。因此 (F.39) 没有改变实际 Bernoulli
mask 或 primitive 因子。

首次被截掉的系数有准确值
$$
p[t^p]f(t)\equiv-\frac12\pmod p.
$$
可直接从 $e^t$ 证明：到次数 $p$，其唯一可能的 $p$ 分母是
$1/p!$；函数 $(x-1)/(x+1)$ 在 $x=1$ 的导数是 $1/2$，
而 $p/p!=1/(p-1)!\equiv-1$。
结合特征零的 $2f'+f^2=1$，遂得
$$
\boxed{\quad
2\overline{f_{<p}}'
+\overline{f_{<p}}^{\,2}-1
\equiv t^{p-1}\pmod{t^p}.
\quad}
\tag{F.40}
$$
所以不能把这个原有限对数替换成特征 $p$ 中的齐次 Riccati 解。

### 11.2. Newton 算子及完整首 $p$ 系数

为避免与原有限 $E(T)$ 混名，记
$$
q_r(R)=\frac{(-1)^r}{(2r-1)!}
 R\prod_{a=1}^{r-1}(R^2-a^2),\qquad
\widehat Q(R)=(R^2-1/4)\sum_{r=2}^m c_rq_r(R).
\tag{F.41}
$$
这就是 (F.20) 的完整行多项式再乘原中项因子。
由 (F.37)，
$$
\widehat Q(R)=
R(R^2-1)(R^2-1/4)
 \bigl(\mathscr D_{S,P}(R^2)
       -C_{\mathrm{pr}}Q_{\mathrm{grid}}(R^2)\bigr).
$$

任选 $c_r$ 的 $p$ 整 lift，并用 (F.41) 的显示乘积定义
$\widetilde Q\in\mathbf Z_p[R]$。
每个 $(2r-1)!$ 都是单位，且
$\widetilde Q(1)=0$ 是整恒等式。
令
$$
g(t)=\widetilde Q(t\partial_t+1)f(t).
$$
则 $g$ 到次数 $p$ 都是 $p$ 整的：
次数小于 $p$ 已整，而
$\widetilde Q(p+1)\equiv p\widetilde Q'(1)\pmod{p^2}$
消去 $[t^p]f$ 的唯一 $p$ 分母。
这些系数的约化均不依赖所选 $c_r$ 的 lift。

由 (F.39)，R1154 的原算子输出同时为
$$
\mathscr Z_{S,P}(T)
=-2T[t^{p-1}]\sinh(Tt)\,\overline{g_{<p}}(t).
\tag{F.42}
$$
因此全部实际 good 行同值所给的原 gap，准确推出
$\deg\overline{g_{<p}}\le2k-1$。
这是同一完整 mask 的有限系数结论；它没有删除下述第 $p$ 项。

从 $Q_{\mathrm{grid}}(1)=m/(1-1/4)=-2/3$，得到
$$
\widehat Q'(1)=\frac32\mathscr D_{S,P}(1)+C_{\mathrm{pr}}.
$$
故完整边界为
$$
\boxed{\quad
\overline{[t^p]g}
=-\frac12\widehat Q'(1)
=-\frac34\mathscr D_{S,P}(1)-\frac12C_{\mathrm{pr}}.
\quad}
\tag{F.43}
$$
这里 $\mathscr D_{S,P}(1)$ 指 (F.24) 的唯一低次数代表在 $1$
的值；$1$ 不是新增的实际 good 节点。
(F.43) 保留 (F.35) 的全部低层贡献，
没有把 $C_{\mathrm{pr}}$ 换成 $b_k/(2k+2)!$。

这个边界还可完全从原齐次点对核读取。
对多项式的积分仅指逐项反除次数，不涉及实或复路径：
$$
\boxed{\quad
\overline{[t^p]g}
=-\frac38\int_0^1
 \frac{\mathsf F_{Z,Z'}(u,1-u)}{u^2}\,du.
\quad}
\tag{F.44}
$$
其中 $\mathsf F_{Z,Z'}(T,U)$ 是 (F.32) 的齐次次数 $p$ 版本。
确实
$$
q_r'(1)=\frac{r!(r-2)!}{(2r-1)!}
=\int_0^1u^{r-2}(1-u)^r\,du,
$$
而 $E_r(u,1-u)=u^r(1-u)^r$，故
$\widehat Q'(1)$ 是该积分的 $3/4$ 倍。
被积多项式次数至多 $p-3$，只反除
$1,\ldots,p-2$；所以 (F.44) 是安全的原有限泛函。

### 11.3. 这个读取本身不是整形式群坐标变换

(F.25) 给出与点对无关的首项
$$
\overline{g_1}
=\frac{\widehat Q(2)}2
=-\frac{15}{16}G_{p-3}\ne0.
\tag{F.45}
$$
若尝试直接把 $g$ 看成 $f$ 的整坐标变换，
所需的坐标级数只能是
$$
h(x)=g(2\operatorname{arctanh}x),
\qquad
2\operatorname{arctanh}x
=2\sum_{j\ge0}\frac{x^{2j+1}}{2j+1}.
$$
它到次数 $p-1$ 都整，但首次边界准确满足
$$
\boxed{\quad
p[x^p]h(x)\equiv2\overline{g_1}
=-\frac{15}{8}G_{p-3}\ne0\pmod p.
\quad}
\tag{F.46}
$$
证明是第 $p$ 次中的唯一非整来源为
$g_1\cdot2x^p/p$。
对任何 $n\ge3$，若在
$(2\operatorname{arctanh}x)^n$ 中使用 $x^p/p$，
总次数已超过 $p$；其余所用分母均小于 $p$。
$g_p$ 又已由 (F.43) 证明为整，所以没有另一项抵消它。

因此当前 Newton/Euler 操作并不是一个已付的整形式群坐标变换；
这在实际 gap 成立时同样如此。
(F.46) 排除的是把这一个有限读取直接当作整映射的路径，
不是排除原共同纤维。
它也不禁止由其它已经支付来源的算子建立不同的联系。
本节保留真正的待付对象：原二根递推、实际 good mask，
以及 (F.43)/(F.44) 的完整第 $p$ 边界，
不从形式群高度或有限多项式的次数直接推出标签注入。

o2_high_coefficient 纸推；o1_theta 已独立核准
$pf_p=-1/2$、完整 $C_{\mathrm{pr}}$ 对首 $p$ 项的贡献、
首项单位及复合坐标中唯一的 $p$ 分母来源。
无数学程序执行。
