# 原跨两条 p-扭点直线的 chord 单位方程与完整角色投影

日期：2026-11-28（Asia/Taipei）  
会话：Astra-serre-24b8836b-20261126  
状态：完整纸面证明；没有数学程序执行。一般 $p$ 主目标仍为 OPEN。

## 1. 范围、原标记及两个不同的共轭

固定 $p>37$，沿用 R1064/R1070/R1133 的
$$
K_0=\mathbf Q(\zeta_p),\quad F=K_0^+,\quad
m=(p-1)/2,\quad X=X_{\rm ns}^+(p).
$$
取原非平方 $\delta\in\mathbf F_p^\times$，以
$\mathbf F_{p^2}=\mathbf F_p[\mathsf i]$、
$\mathsf i^2=\delta$ 书写原 level 索引。
对同一个 Weil pairing 为 $\zeta_p$ 的有序基 $(P_0,Q_0)$，定义
$$
P_{u+v\mathsf i}=uP_0+vQ_0.
\tag{L.1}
$$
$\mathsf i$ 只作用于这个 $p$-torsion 标记；
本文从不把它当成通用椭圆曲线的 CM 端同态，
也没有向常数域另添一个数域中的 $\sqrt\delta$。

索引共轭为 $z\mapsto\bar z=z^p$，故
$\overline{\mathsf i}=-\mathsf i$。
原算术 $\sigma_{-1}$ 在 full-level 标记上是
$(u,v)\mapsto(u,-v)$，并同时送
$\zeta_p\mapsto\zeta_p^{-1}$。下面的算术 bar 范数保持这两个实际作用。

固定完整实际 cusp 模块中的非零角色
$\chi=\omega^r$，取其偶数代表 $2\le r\le p-3$。
保原整数提升
$$
n_{\chi,h}\equiv m^{-1}\chi(h)^{-1}\pmod p,\qquad
\sum_h n_{\chi,h}=0.
\tag{L.2}
$$
每个范数类在 $I=\mathbf F_{p^2}^\times/\{\pm1\}$ 中有 $p+1$ 个元素，
故 $\sum_{z/\pm}n_{\chi,[Nz]}=0$。
本文的 $F_\chi$ 始终是原 $u_\chi^m/A(u_\chi)$ 规范函数，
不新选一个仅具有相同 divisor 的函数。

本节构造的两个 primitive 单位在原 full-level 开曲线上严格满足和为一；
其真实 bar 范数可以逐槽恢复原 $F_\chi$。
这不意味着取范数后的两个函数仍和为一，也不意味着原两个不同角色的 cup 已消失。

## 2. 原 chord 源：两槽都是全局权零单位

在局部非零 Hodge 标架上写短 Weierstrass 方程
$y^2=x^3+Ax+B$。取
$$
a\in\mathbf F_p\setminus\{0,1,-1\},\qquad
P=P_z,\quad Q=P_{az},\quad S=P_{\mathsf iz}.
$$
因 $\mathsf i\notin\mathbf F_p$，$S$ 与 $P,Q,-Q$ 分属两条
不同的 $\mathbf F_p$ 直线。

对非垂直的两个点定义同一首项规范的 chord：
$$
m_{P,Q}=\frac{y(P)-y(Q)}{x(P)-x(Q)},\qquad
\ell_{P,Q}(T)=y(T)-y(P)-m_{P,Q}(x(T)-x(P)).
\tag{L.3}
$$
置
$$
\begin{aligned}
U_a(z)&=\frac{\ell_{P,Q}(S)}{\ell_{P,-Q}(S)},\\
V_a(z)&=\frac{(m_{P,Q}-m_{P,-Q})(x(S)-x(P))}
                 {\ell_{P,-Q}(S)}.
\end{aligned}
\tag{L.4}
$$
直接相减给
$$
\boxed{\quad U_a(z)+V_a(z)=1.\quad}
\tag{L.5}
$$
这里的正号来自
$\ell_{P,-Q}(S)-\ell_{P,Q}(S)
=(m_{P,Q}-m_{P,-Q})(x(S)-x(P))$。

所有除法都在原 full-level 非退化开部合法。
确实，$a\ne\pm1$ 保 $x(P)-x(Q)\ne0$，而
$$
m_{P,Q}-m_{P,-Q}=-\frac{2y(Q)}{x(P)-x(Q)}\ne0
\tag{L.6}
$$
因为非零奇数阶点 $Q$ 不是二扭点。
两个 chord 的零点 divisor 分别是
$[P]+[Q]+[-P-Q]$ 与 $[P]+[-Q]+[-P+Q]$，
全部在第一条 $\mathbf F_p$ 直线上；
第二条直线上的 $S$ 不会落在其中。
即使 $a=2$ 或 $a=m$ 使某个 chord 的第三个交点与端点重合，
只会出现已有同直线零点的重数，不影响这项避让。
同理 $x(S)-x(P)\ne0$。

个别 chord、斜率、坐标差仍有 Hodge 权；
但 (L.4) 的分子、分母各有同样的权 $3$，
所以 $U_a,V_a$ 是全局权零 modular units。
这在特征零成立，并可在原 fine 开模空间的
$\mathbf Z[1/6p]$ 模型上逐局部标架检查。
本文不额外宣称这套短 Weierstrass 公式已支付 $2,3$ 处的特殊化。

同时把所有点取负时，chord 与斜率各变号、坐标差不变，
故
$$
U_a(-z)=U_a(z),\qquad V_a(-z)=V_a(z).
\tag{L.7}
$$
所以原半向量乘积没有未跟踪的 $\pm z$ 相位。

## 3. 真正的 bar 范数与精确的两槽代数恒等式

定义
$$
\mathcal U_{\chi,a}
 =\prod_{z/\pm}U_a(z)^{n_{\chi,[Nz]}},\qquad
\mathcal V_{\chi,a}
 =\prod_{z/\pm}V_a(z)^{n_{\chi,[Nz]}}.
\tag{L.8}
$$
norm-one Cartan 的几何作用只重排这些因子。
determinant 为一的 anti-Cartan 元为
$z\mapsto b\bar z$、$N(b)=-1$；
重指标后，它把 $S=P_{\mathsf iz}$ 送到 $-S$，
并保持 $[Nz]$ 的指数。
算术 $\sigma_{-1}$ 也把 (L.8) 送到同一个 $S\mapsto-S$ 乘积。

因此下列是同时具有原几何 normalizer 不变性和实下降的函数：
$$
\mathcal N^U_{\chi,a}
=\mathcal U_{\chi,a}\overline{\mathcal U_{\chi,a}},
\qquad
\mathcal N^V_{\chi,a}
=\mathcal V_{\chi,a}\overline{\mathcal V_{\chi,a}}
\quad\in F(X)^\times.
\tag{L.9}
$$
这里取了一次实际二次范数；
不能把几何与算术的两种相同乘积读法再乘一次而引入额外 $2$。

写 $d(T,T')=x(T)-x(T')$。
对同一首项规范的 chord，曲线方程给
$$
\ell_{P,Q}(S)\ell_{P,Q}(-S)
=-d(S,P)d(S,Q)d(S,P+Q).
\tag{L.10}
$$
分母 chord 有同样的首项，故逐点相除后准确得到
$$
U_a(z)\,U_a(z)\big|_{S\mapsto-S}
=\frac{d(P_{\mathsf iz},P_{(1+a)z})}
       {d(P_{\mathsf iz},P_{(1-a)z})}.
\tag{L.11}
$$
没有留下斜率常数或模型标量。

同样由 (L.6)、(L.10)，第二槽的完整公式是
$$
V_a(z)\,V_a(z)\big|_{S\mapsto-S}
=-\frac{\psi_2(P_{az})^2\,d(P_{\mathsf iz},P_z)}
 {d(P_z,P_{az})^2
  d(P_{\mathsf iz},P_{az})
  d(P_{\mathsf iz},P_{(1-a)z})},
\qquad \psi_2=2y.
\tag{L.12}
$$
共同的 $-1$ 在原半权乘积中由 $\sum n=0$ 消失。
式 (L.12) 仍保 $\psi_2^2$，不把可能为零的 $\kappa_\chi(2)$ 反除。

## 4. 任意两索引的原坐标差投影，包含全部相位与 leading

本节给 (L.11)–(L.12) 所需的精确通用接口。
对 $\alpha,\beta\in\mathbf F_{p^2}^\times$、$\alpha\ne\pm\beta$，定义
$$
\mathcal E_\chi(\alpha,\beta)
=\prod_{z/\pm}
 d(P_{\alpha z},P_{\beta z})^{n_{\chi,[Nz]}}
\tag{L.13}
$$
以及
$$
D_\chi(\alpha,\beta)=
 \chi(N(\alpha+\beta))+\chi(N(\alpha-\beta))
 -2\chi(N\alpha)-2\chi(N\beta).
\tag{L.14}
$$
每个因子的权由 augmentation 消去，故 (L.13) 已是 full-level 权零单位。
它在 anti-Cartan 与算术 bar 下都变成
$\mathcal E_\chi(\bar\alpha,\bar\beta)$。

使用 R1070 (1070.19) 的同一个 $\Theta$。
椭圆函数的 divisor 和在 $u=0$ 的首项比较给
$$
x(u)-x(v)=\lambda(E)\,
 \frac{\Theta(u+v)\Theta(u-v)}
      {\Theta(u)^2\Theta(v)^2},
\tag{L.15}
$$
其中 $\lambda(E)$ 仅依赖共同模型/Hodge 标架。
例如在同一个解析参数中，它是
$-\Theta'(0)^2$ 乘相应的 $x$ 切向尺度。
其准确值不被猜定，而是因 (L.2) 在 (L.13) 中严格消去。

R1070 (1070.21) 的二次指数在 (L.15) 中也严格消去：
$$
(r+r')(u+v)+(r-r')(u-v)-2ru-2r'v=0.
$$
将所有索引改回原固定代表只产生根单位。
写
$f_\chi^{[\gamma]}=\prod_{z/\pm}g_{\gamma z}^{n_{\chi,[Nz]}}$，
并在这一定义中总使用原固定代表。
于是得到实际函数恒等式
$$
\mathcal E_\chi(\alpha,\beta)
=\varepsilon
 \frac{f_\chi^{[\alpha+\beta]}f_\chi^{[\alpha-\beta]}}
 {(f_\chi^{[\alpha]})^2(f_\chi^{[\beta]})^2}.
\tag{L.16}
$$
右侧的每个重指标乘积仍为原 augmentation-zero 的范数指数乘积。
两侧都在原 $K_0(X(p))$ 中，该函数域的常数域是 $K_0$；
因此根单位 $\varepsilon$ 真在 $K_0$。

取同一个算术 bar 范数，$\varepsilon\bar\varepsilon=1$ 严格成立：
$$
\mathcal E_\chi(\alpha,\beta)
\mathcal E_\chi(\bar\alpha,\bar\beta)
=
\frac{w_\chi^{[\alpha+\beta]}w_\chi^{[\alpha-\beta]}}
 {(w_\chi^{[\alpha]})^2(w_\chi^{[\beta]})^2},
\quad
w_\chi^{[\gamma]}=f_\chi^{[\gamma]}\overline{f_\chi^{[\gamma]}}.
\tag{L.17}
$$
这一步没有取 $12p$ 次幂，也没有丢掉原 $p$-相位。

重指标 $z\mapsto\gamma z$ 给
$n'_h=n_{h/N\gamma}\equiv\chi(N\gamma)n_h\pmod p$。
差是 $p$ 倍的 augmentation-zero 整数向量；
R1064/R1070 保证除以 $p$ 后仍是实际 modular unit。
此外 R1070 (1070.5)、(1070.29) 的全 cusp leading 和为零
适用于这些全部重指标向量，不能只凭相同 $V$ 类省去这一步。
故
$$
[w_\chi^{[\gamma]}]
=\frac{2\chi(N\gamma)}m[F_\chi],
\qquad
[\mathcal E_\chi(\alpha,\beta)
 \mathcal E_\chi(\bar\alpha,\bar\beta)]
=\frac{2D_\chi(\alpha,\beta)}m[F_\chi].
\tag{L.18}
$$
特别是 $\alpha,\beta$ 均在 $\mathbf F_p$，或
$\alpha=\mathsf i$、$\beta=t\in\mathbf F_p^\times$ 时，
(L.13) 本身严格固定于 bar 和原几何 normalizer。
后一种情形用的是 $x(P_{-\mathsf iz})=x(P_{\mathsf iz})$。
因此在这两种实际输入上可除以 $2$：
$$
[\mathcal E_\chi(\alpha,\beta)]
=\frac{D_\chi(\alpha,\beta)}m[F_\chi].
\tag{L.19}
$$
所有规范 leading 常数均已由 (L.17)–(L.18) 支付。

## 5. 两个原角色系数

置 $f_\chi(t)=\chi(t^2)$、$\kappa_\chi(2)=4-f_\chi(2)$。
由 (L.11)、(L.19)，
$$
[\mathcal N^U_{\chi,a}]
=\frac{u_\chi(a)}m[F_\chi],\qquad
u_\chi(a)=D_\chi(\mathsf i,1+a)-D_\chi(\mathsf i,1-a).
\tag{L.20}
$$
对第二槽，原 all-vector $M_{2,\chi}$ 的逆正是
$\prod_{z/\pm}\psi_2(P_z)^{2n_{\chi,[Nz]}}$：
偶数除法多项式的负号由 augmentation 消失。
所以 R1070 §9 给出
$$
\left[\prod_{z/\pm}\psi_2(P_{az})^{2n_{\chi,[Nz]}}\right]
=-\frac{2f_\chi(a)\kappa_\chi(2)}m[F_\chi].
$$
结合 (L.12) 的其余四项，
$$
\begin{aligned}
[\mathcal N^V_{\chi,a}]&=\frac{v_\chi(a)}m[F_\chi],\\
v_\chi(a)&=-2f_\chi(a)\kappa_\chi(2)
 -2D_\chi(1,a)+D_\chi(\mathsf i,1)\\
&\hspace{16mm}-D_\chi(\mathsf i,a)-D_\chi(\mathsf i,1-a).
\end{aligned}
\tag{L.21}
$$
这些是实际原规范的函数域 Kummer 类，不只是 divisor 系数。
公式也容许 $\kappa_\chi(2)=0$；没有对它作反除。

改变 $a$ 为 $-a$ 时，
$U_{-a}=U_a^{-1}$、$V_{-a}=-V_a/U_a$，
与
$u_\chi(-a)=-u_\chi(a)$、
$v_\chi(-a)=v_\chi(a)-u_\chi(a)$ 相符。
这同时核准两槽的符号和真实范数方向。

## 6. 每个完整实际角色都有可逆的第一槽

将 $\chi=\omega^r$ 的值在 $\mathbf F_p$ 中读取，定义偶函数
$$
g_r(t)=(t^2-\delta)^r-t^{2r}.
$$
因 $\delta$ 非平方，第一项的底数从不为零。
式 (L.14)、(L.20) 化为
$$
u_\chi(a)=2\bigl(g_r(a+1)-g_r(a-1)\bigr).
\tag{L.22}
$$

假设对所有 $a\ne0,\pm1$ 都有 $u_\chi(a)=0$。
$a=0$ 的差由 $g_r$ 偶性自动为零，
故 $g_r(t)=g_r(t-2)$ 除了 $t=0,2$ 之外都成立。
在步长为 $2$ 的 $\mathbf F_p$ 循环中删去顶点 $0$，
余下 $p-1$ 个非零顶点仍为一条连通路径。
所以 $g_r$ 在 $\mathbf F_p^\times$ 上为常数。

令 $X=t^2$。于是
$(X-\delta)^r-X^r$ 在全部 $m$ 个非零平方上为常数。
若 $2\le r\le m$，该多项式次数为 $r-1<m$，
首项 $-r\delta X^{r-1}$ 非零，矛盾。

若 $m<r\le p-3$，在
$\mathbf F_p[X]/(X^m-1)$ 中看 $X^{m-1}$ 系数。
它准确是
$$
\binom r{m-1}(-\delta)^{r-m+1}\ne0.
\tag{L.23}
$$
唯一可能折回同次数的高项是 $X^{2m-1}$，
但 $2m-1=p-2>r-1$，该项不存在。
余式因而也不可能为常数，仍为矛盾。

因此至少有一个允许的 $a$ 使 $u_\chi(a)\ne0$。
又 $u_\chi(-a)=-u_\chi(a)$，可取准确范围
$$
\boxed{\quad
2\le a\le m,\qquad u_\chi(a)\in\mathbf F_p^\times.
\quad}
\tag{L.24}
$$
端点 $a=2$ 合法，$a=m$ 也不等于 $0,\pm1$。
这覆盖完整实际非零 $V_\chi$，无需额外 Bernoulli-good 假设。

由 (L.20)，每个原 $F_\chi$ 因此都可由这个
真正跨两条 $\mathbf F_p$ 直线的 primitive 源恢复：
$[F_\chi]=m\,u_\chi(a)^{-1}[\mathcal N^U_{\chi,a}]$。
本文只保证每个角色各自有可用 $a$；
没有未经证明地保证不同角色共用同一个 $a$，或 $v_\psi(a)$ 同时为单位。

## 7. 实际低 cochain 输入与仍须保留的 Norm 交叉项

(L.5) 是原 full-level 开曲线上的严格单位方程。
所以 R1133 §§8–10 已付的显式 Heisenberg、
单位 norm witness 以及兼容的 class-four 塔都可直接取
$U=U_a(z)$、$W=V_a(z)$。
其局部因子、根单位和交换同构使用同一实际模型，
不需要把 level-$p$ theta 先取 $p$ 次幂。

但 (L.9) 后的两个范数不满足自动的和一关系。
例如把两个原范数 cup 拉回同一个 full-level 域，
必须保
$$
\sum_{i,j}n_{\chi,i}n_{\psi,j}
 \bigl(
 \{U_i,V_j\}+\{U_i,\bar V_j\}
 +\{\bar U_i,V_j\}+\{\bar U_i,\bar V_j\}
 \bigr).
\tag{L.25}
$$
只有真正相同输入的 $\{U_i,V_i\}$ 及其 bar 共轭可直接用 (L.5)。
其余项及下降时的完整 Cor 仍须处理。
式 (L.24) 付款的是第一阶段的实际角色恢复，
不是原 coarse 曲线上的四阶覆盖，也不是一般 $p$ 同点排除。

## 8. 为何需要真实椭圆关系：泛坐标三角关系的准确边界

这里仅记录一个形式范围，不能误读为原 cup 非零。

把 $I=E[p]^\times/\{\pm1\}$ 按 $p+1$ 条 $\mathbf F_p$ 直线
分成互不交顶点块 $I_L$。
R1133 原 primitive
$\mathcal B_{a,\chi}=\prod B_a(P_i)^{-n_{\chi,i}}$
的形式 log 向量 $w_\chi$ 只用同一个块内的
$x(P_i)-x(2P_i)$ 与 $x(P_i)-x(aP_i)$ 两条边，
且每块的总边系数为零。

以 $i=\lambda z_L$ 重指标时，
每块向量只是同一个向量乘非零标量 $\chi(Nz_L)^{-1}$。
R1133 可选的 $\delta_\chi(a)$ 为单位，且原 $F_\chi$ 非零；
所以每个块向量均非零。
两个不同实际角色的形式向量不能比例，
否则其原函数域 Kummer 类也比例，与不同原 Galois 角色矛盾。
这里 full-level 拉回的单射由其 prime-to-$p$ 次数和 norm 支付。

若 $w_\chi\wedge w_\psi$ 在所有不同块的边对上系数为零，
则对所有 $L\ne M$，
$w_{\chi,L}\otimes w_{\psi,M}
=w_{\psi,L}\otimes w_{\chi,M}$。
全块非零的简单张量等式迫每块同比例、且比例在所有块相同，
矛盾。因此有一对四个端点互异的边，wedge 系数非零。

通用坐标差的 triangle/Arnold 关系每个 wedge 项都共享顶点，
故不能消掉该系数。更直接地，在独立变量 $X_i$ 的配置函数域中，
先沿这两条互不交的 collision divisors 连续取 tame，
精确读出这个系数（总号依次序），故对应的通用 $K_2/p$ 类非零。

这没有任何向实际椭圆 specialization 的单射断言。
实际上椭圆加法提供额外的真关系：
$$
d(P+Q,P-Q)\,d(P,Q)^2=-4y(P)y(Q).
\tag{L.26}
$$
它由两个 chord 斜率的平方相减直接得到。
四对 $(P,Q),(R,S),(P,R),(Q,S)$ 取比会消掉全部
$y$ 与 $-4$，给原 $p$ 点之间的权零乘法关系；
所用 pairs 只须非 $\pm$。
这样的关系不是独立坐标配置里的 triangle 关系。
本稿的 chord 单位方程正是利用真实椭圆加法，
仍不宣称这些新增关系已经消去指定原 cup。

## 原来源与审核

- [R1070](../results/R1070-original-cuspidal-labels-by-division-polynomial-values.md)
  §§1、4–7、9–10：原整数范数权、全部 cusp leading、
  $\Theta/g$ 规范、真正 bar 范数、$\psi_2$ 及完整实际角色范围。
- [R1133](../results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)
  §§1–8 的原 primitive 恢复与完整 crossed Cor，
  §§9–10 的实际 unit-norm cochain 塔。
- 椭圆曲线 chord 的 divisor、同一首项及 (L.10)、(L.26)
  均已在本文从短 Weierstrass 方程直接推导；不假设通用曲线具有 CM。

global_route 推导。o2_high_coefficient 已独立纸核
两槽单位、真实 bar 范数、$D_\chi/m$ 的相位和 $2$ 因子、
$u_\chi,v_\chi$ 全式、(L.24) 两个次数范围，
以及 §8 的准确 universal/actual 边界。

root 对候选 6862e89aa64bfae3df3b1930d62fd89bf3434aa9 全文独立纸审通过；o2_high_coefficient 已再核 exact 转录。所有 chord 退化重数、两种 bar 的一次范数、R1070 全部 augmentation/leading、(L.23) 的高次回折和 §8 的实际 specialization 边界均保留。
