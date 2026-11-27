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
