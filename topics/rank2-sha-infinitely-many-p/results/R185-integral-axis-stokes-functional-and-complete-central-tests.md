# R185. 原中央导数的完整整轴泛函与显式高精度阶乘行

日期：2026-11-12。**状态：本文的完整收敛公式、准确赋值、规范
改换和有限精度检验均已证明。** 本篇是单份完整结果，不另设重复
工作笔记。原两个中央导数在无穷多个素数上的非零仍未证明。

## 1. 原对象、同一整截面与本篇结论

固定惰性素数
$$
 p=4r-1\ge7,\qquad R=r(p-1),\qquad
 w=z^4,\qquad \rho=p^{-1/(2p)}.
 \tag{1}
$$
沿用实际平面
$$
 a(w)=\vartheta(z)^4,\qquad b(w)=\sigma(z)^4,
 \qquad s_0(w)=b(w)/a(w)=x_E(z)^{-2}.
$$
R174 的整 Cartan 坐标为
$$
 U=X-Y/3+O((X,Y)^2),\qquad V=Y+O((X,Y)^2),
 \qquad X=a-1,\quad Y=b.
$$
二者及其环境形式逆均在 $\mathbb Z_p$ 上。沿原曲线，
$$
 U(w)=u_0w^r+O(w^{pr}),\qquad
 V(w)=w+O(w^{R+1}),\qquad v_p(u_0)=-1.
 \tag{2}
$$
这里的高阶曲线系数未被假定为整。

R179 §6.1 已在同一个环境中构造唯一整截面
$$
 U(a_{\rm sec}(s)-1,s a_{\rm sec}(s))=0,\qquad
 a_{\rm sec}\in1+s\mathbb Z_p[[s]],
$$
以及
$$
 \nu(s)=V(a_{\rm sec}(s)-1,s a_{\rm sec}(s))
       \in s+s^2\mathbb Z_p[[s]].
$$
置
$$
 \Gamma=\frac{a}{a_{\rm sec}(b/a)},\qquad
 \zeta=\nu(b/a).
 \tag{3}
$$
于是 $(\Gamma-1,\zeta)$ 是同一环境的整形式坐标，并满足
$\Gamma(0,V)=1,\ \zeta(0,V)=V$。

令 $F(a,b)\in\mathbb Z_p[a,b]$ 为正齐次次数
$d\in\mathbb Z_{>0}$ 的多项式，且
$$
 p\nmid d,\qquad F(1,0)=0.
 \tag{4}
$$
定义其真实轴级数
$$
 g_F(V)=F(a(0,V),b(0,V))
       =\sum_{\ell\ge1}g_\ell(F)V^\ell\in V\mathbb Z_p[[V]].
$$
齐次性准确给
$$
 F=\Gamma^d g_F(\zeta).
 \tag{5}
$$
特别，原 $A_2,B$ 都满足 (4)，且同有 $d=17$；二者使用下文
**完全相同**的权 $\lambda_{17,s}$。

令 $c$ 为 R54 的准确 sigma 常数，$v_p(c)=-1$。本篇证明
$$
 \boxed{\quad
 J_F'(0)=\sum_{s\ge1}g_{rs}(F)\lambda_{d,s},\qquad
 v_p(\lambda_{d,s})=s+v_p((s-1)!).
 \quad}
 \tag{6}
$$
这里 $J_F$ 是原加法参数 $w=z^4$、指数规范 $4dc$ 下的实际
Mahler 半因子；没有先把原高中央系数换到 $v=V(w)$。

更强地，令
$$
 b_d=d u_0,\qquad q_p=(p-1)/2.
 \tag{7}
$$
则 $v_p(b_d)=-1$，并且对**全部** $s\ge1$，
$$
 \boxed{\quad
 \lambda_{d,s}
 =(-1)^{s-1}(s-1)!\,b_d^{-s}
                  \bigl(1+p^{q_p}\mathbb Z_p\bigr).
 \quad}
 \tag{8}
$$
这里的记法表示其比值属于所示单位群，不是允许任意选择的误差。
每个 $\lambda_{d,s}$ 都由下文 (15) 的同一真实系数定义。

## 2. 较大圆盘上保留完整前因子

先说明为何 (5) 允许在 R54 的较大余项盘上逐轴展开。R54 给
$$
 a(w)=e^{4cw^r}A_{\rm res}(w),\qquad
 A_{\rm res}(0)=1,\qquad \|A_{\rm res}\|_\rho\le1.
 \tag{9}
$$
指数分离是形式恒等式；单独的 $e^{4cw^r}$ 不必在闭 $\rho$ 盘
上收敛。具体地，R54 的秩零参考
$S=(x_E^2+1)\sigma^4$ 满足相同指数分离，而
$a/S=x_E^2/(x_E^2+1)=(1+s_0)^{-1}$ 是此盘上的解析单位。

写 $W_x=z^2x_E(z)$。R54 的系数界给
$$
 v_p([w^m](W_x-1))\ge-\frac{4m}{p^2-1}\qquad(m\ge1).
$$
在 $|z|\le\rho$ 上，每项的加权赋值至少
$4m(1/(2p)-1/(p^2-1))>0$。所以 $W_x$ 及其逆是范数一的
解析单位，且
$$
 s_0=wW_x^{-2},\qquad \|s_0\|_\rho=\rho^4.
 \tag{10}
$$
由 $a_{\rm sec},\nu$ 的整性，
$a_{\rm sec}(s_0)$、$\nu(s_0)/s_0$、$s_0/w$ 也都是范数一的
解析单位。因此对任意整数 $\ell\ge1$，定义实际形式级数
$$
 F_{d,\ell}(w)
 =\Gamma(\gamma(w))^d\zeta(\gamma(w))^\ell
 =a(w)^d a_{\rm sec}(s_0(w))^{-d}\nu(s_0(w))^\ell.
 \tag{11}
$$
取 $a_d=4dc$，则
$$
 F_{d,\ell}=e^{a_dw^r}G_{d,\ell},\qquad
 \boxed{\quad
 \|G_{d,\ell}\|_\rho\le\rho^{4\ell},\qquad
 G_{d,\ell}=w^\ell+O(w^{\ell+1}).
 \quad}
 \tag{12}
$$
所有正、负整次单位幂在这里均保留，故 (12) 对所有 $\ell$
成立，不是只对有限初始截断成立。

一般 (5) 去指数后的级数也在该盘收敛。因为 $\|\zeta\|_\rho
=\rho^4<1$，整级数 $g_F(\zeta)$ 在闭盘上一致收敛。这一步没有
要求 $\Gamma$ 本身在整个较大盘上解析，也没有把 $\Gamma,\zeta$
添加为原有限多项式源的自由列。

## 3. 原中央投影与每条轴的准确 Stokes 权

范数为一的真实 Teich 群除去 $\mu_4$ 后阶为 $r$。它在原曲线
上作用为 $w\mapsto\epsilon w$，在 (3) 上作用为
$$
 \Gamma\mapsto\Gamma,\qquad \zeta\mapsto\epsilon\zeta,
 \qquad \epsilon\in\mu_r.
 \tag{13}
$$
指数 $e^{a_dw^r}$ 也不变。因此 $G_{d,\ell}$ 只有
$w^{\ell\bmod r}$ 项；当 $r\nmid\ell$ 时，其全部 $w^{rh}$ 项
准确为零，中央 Mahler 半因子也恒为零。这里只杀掉非 $r$ 倍
的轴，不会杀掉 $g_{2r},g_{3r},\ldots$。

对 $\ell=rs$，写
$$
 c_{s,h}=[w^{rh}]G_{d,rs}.
$$
由 (12)，$c_{s,h}=0$ 对 $h<s$ 成立，$c_{s,s}=1$，且
$$
 v_p(c_{s,s+t})
 \ge-\left\lfloor\frac{(p+1)t}{2p}\right\rfloor
 \qquad(t\ge0).
 \tag{14}
$$
以 $(u)_h=u(u-1)\cdots(u-h+1)$ 表示下降阶乘。定义
$$
 J_{d,rs}(u)=
   \sum_{h\ge s}c_{s,h}a_d^{-h}(u)_h,\qquad
 \boxed{\quad
 \lambda_{d,s}=J_{d,rs}'(0)
 =\sum_{h\ge s}(-1)^{h-1}(h-1)!\,a_d^{-h}c_{s,h}.
 \quad}
 \tag{15}
$$
(14) 使系数赋值至少线性趋于无穷，因此第一式属于
$\mathbb Z_p\langle u\rangle$，可以逐项微分。在每个整数 $k\ge0$，
有限下降阶乘和还给准确插值
$$
 J_{d,rs}(k)=k!a_d^{-k}[w^{rk}]F_{d,rs}.
 \tag{16}
$$
这与原 R54 规范一致。

(15) 中 $h=s$ 的项准确为
$(-1)^{s-1}(s-1)!a_d^{-s}$。其后 $h=s+t$ 项相对这一项的
赋值至少为
$$
 t-\left\lfloor\frac{(p+1)t}{2p}\right\rfloor
 +v_p\!\left(\frac{(s+t-1)!}{(s-1)!}\right).
 \tag{17}
$$
对 $t\ge1$，(17) 至少一，并且随 $t$ 趋于无穷。因此
$$
 \lambda_{d,s}
 =(-1)^{s-1}(s-1)!a_d^{-s}(1+p\mathbb Z_p),
 \qquad
 v_p(\lambda_{d,s})=s+v_p((s-1)!).
 \tag{18}
$$
尤其每条中央轴的权都非零。其非零不等于原两个指定加权和非零。

## 4. 无限轴交换、准确尾界与完整零性检验

由 (5)，先对有限多个 $\ell$ 求和，(13) 与线性性给
$$
 J_{\Gamma^d\sum_{\ell\le M}g_\ell\zeta^\ell}'(0)
 =\sum_{rs\le M}g_{rs}\lambda_{d,s}.
$$
要把 $M$ 送往无穷，不能只诉诸形式代入。对中央轴取到 $s=N$ 后，
剩余准确写成
$$
 \Gamma^d\zeta^{r(N+1)}h_N(\zeta^r),
 \qquad h_N\in\mathbb Z_p[[T]].
$$
去指数后在闭 $\rho$ 盘的范数至多
$\rho^{4r(N+1)}$。重复 (14)–(17)，其 Stokes 导数赋值至少为
$$
 N+1+v_p(N!).
$$
这个下界趋于无穷。非中央轴的每个中央系数本来为零，有限
$\mu_r$ 平均与上述收敛也交换。因此得到 (6)，并有完整余项界
$$
 \boxed{\quad
 v_p\!\left(J_F'(0)-\sum_{s=1}^{N}g_{rs}(F)\lambda_{d,s}\right)
 \ge N+1+v_p(N!).
 \quad}
 \tag{19}
$$
这也逐项证明 (6) 的双重求和可交换，而不依赖未经指定的
逐点或形式连续性。

以 $\lambda_{d,1}\ne0$ 归一，令
$$
 \omega_{d,s}=\lambda_{d,s}/\lambda_{d,1},\qquad
 \mathscr L_d(g)=\sum_{s\ge1}\omega_{d,s}g_{rs}.
$$
则
$$
 \omega_{d,1}=1,\qquad
 v_p(\omega_{d,s})=s-1+v_p((s-1)!),\qquad
 J_F'(0)=\lambda_{d,1}\mathscr L_d(g_F).
 \tag{20}
$$
这是整轴空间 $V\mathbb Z_p[[V]]$ 上一条原始、连续的
$\mathbb Z_p$ 线性泛函，其连续性按 (19) 给出的逐轴尾界理解。
在原有限次数源上只取它的实际限制。

因此以下条件完全等价：
$$
 \begin{aligned}
 J_F'(0)=0
 &\quad\Longleftrightarrow\quad
 \sum_{s\ge1}\omega_{d,s}g_{rs}(F)=0\\
 &\quad\Longleftrightarrow\quad
 \sum_{s=1}^{N}\omega_{d,s}g_{rs}(F)
       \in p^{\,N+v_p(N!)}\mathbb Z_p
       \quad\text{对全部 }N\ge1.
 \end{aligned}
 \tag{21}
$$
正向用 (19)，反向令 $N\to\infty$。这给原完整中央零性的一组
线性、全精度整检验，而非只给首权必要条件。

## 5. 真 Teich 支撑使规范余项推迟到第 p 带

下面加强 (18) 的单位精度。仅为本节的正式计算，用径向坐标
$(\eta,w)$ 表示
$$
 (a_{\rm env},b_{\rm env})=(e^\eta a(w),e^\eta b(w)).
$$
在这个计算中 $w$ 由 $s=b/a$ 决定，故径向缩放不改变 $w$。
令
$$
 u(\eta)=\sum_{n\equiv1\;(\mathrm{mod}\;p-1)}\frac{\eta^n}{n!},
 \qquad
 \xi(w)=a(w)-b(w)/3=\sum_{n\ge0}\xi_nw^n,\quad \xi_0=1.
$$
R174 的原有限 Teich 平均逐系数给出完整形式恒等式
$$
 \begin{aligned}
 U(\eta,w)
 &=\sum_{j\ge0}\xi_{rj}\,u^{(j)}(\eta)w^{rj},\\
 V(\eta,w)
 &=\sum_{j\ge0}b_{1+rj}\,u^{(j+1)}(\eta)w^{1+rj},
 \qquad b_n=[w^n]b(w).
 \end{aligned}
 \tag{22}
$$
这里 $u^{(j)}$ 是普通第 $j$ 次导数，相关阶乘已经在定义中；
没有在对称幂与除幂之间省掉因子。

可直接检验 (22) 的角色。第一行的 $\eta^h w^{rj}$ 必满足
$h+j\equiv1\bmod p-1$；第二行除以 $w$ 后必须满足
$h+j\equiv0\bmod p-1$。赋予 $\eta$ 和 $w^r$ 权一，则
$$
 U=\eta+u_0w^r+O_{\rm wt}(p),\qquad
 V=w\{1+O_{\rm wt}(p-1)\}.
 \tag{23}
$$
式中所有 $w$ 指数和径向导数都来自实际曲线；并非另选一个
具有相同首项的形式群模型。

令 $\eta_{\rm sec}(w)$ 为同一个 $U=0$ 截面的径向参数。由
(23) 的整阶隐函数计算，在 $\mathbb Q_p[[w]]$ 中准确有
$$
 \eta_{\rm sec}(w)=-u_0w^r+O(w^{pr}),\qquad
 \zeta(\gamma(w))=w+O(w^{R+1}).
 \tag{24}
$$
因为 $a_{\rm sec}(s_0(w))=e^{\eta_{\rm sec}(w)}a(w)$，由 (3)
又有
$$
 \Gamma(\gamma(w))=e^{-\eta_{\rm sec}(w)}.
$$
于是对全部 $s\ge1$，
$$
 \boxed{\quad
 e^{-d u_0w^r}F_{d,rs}(w)
       =w^{rs}\{1+O(w^R)\}.
 \quad}
 \tag{25}
$$
(24)–(25) 只是准确的消失阶断言；没有把个别
$\eta_{\rm sec}$ 系数额外假定为整。

## 6. 规范改换不改变原导数，且给出全部 s 的高精度权

由 (9)、(2) 与 $[w^r]b\in\mathbb Z_p$，
$$
 u_0-4c\in\mathbb Z_p.
 \tag{26}
$$
具体地，$[w^r]A_{\rm res}$ 由闭 $\rho$ 盘估计为整，
$u_0=[w^r](a-1-b/3)$，故 (26) 直接成立。对于 (4) 的 $d$，
$$
 b_d=d u_0,\qquad
 b_d/a_d\in1+p\mathbb Z_p,\qquad b_d-a_d\in\mathbb Z_p.
$$
因此改用指数 $b_d$ 后，余项仍在闭 $\rho$ 盘解析，并保持 (12)
的范数界：额外因子 $e^{(a_d-b_d)w^r}$ 的范数为一，因为
$$
 v_p(w^r)\ge\frac{p+1}{2p}>\frac1{p-1}.
$$
记两种规范的解析插值为 $J_F^{(a_d)}$、$J_F^{(b_d)}$。在全部
非负整数 $k$，实际插值给
$$
 J_F^{(b_d)}(k)=(a_d/b_d)^kJ_F^{(a_d)}(k).
$$
两端均在零附近解析，非负整数包含趋于零的 $p^n$，故解析
恒等定理给
$$
 J_F^{(b_d)}(u)=(a_d/b_d)^uJ_F^{(a_d)}(u).
$$
质量 $F(1,0)=J_F(0)=0$ 使
$$
 \boxed{\quad
 (J_F^{(b_d)})'(0)=(J_F^{(a_d)})'(0).
 \quad}
 \tag{27}
$$
所以这里是同一个原中央导数，而不是只保留其赋值或零性。

对每条 $F_{d,rs}$ 也有质量零，故同一 $\lambda_{d,s}$ 可在
$b_d$ 规范计算。(25) 表明首项之后 $h=s+1,\ldots,s+p-2$
的残余中央系数全部准确为零。因此 (17) 的尾只从 $t=p-1$
开始。而
$$
 t-\left\lfloor\frac{(p+1)t}{2p}\right\rfloor
 \ge\frac{p-1}{2}\qquad(t\ge p-1).
$$
该式在 $t=p-1$ 取等，随后非减；阶乘比只会增加赋值。
这就对所有 $s$ 证明了 (8)，没有对 $s<p$ 的附加限制。

## 7. 原两中央条件的显式多层轴约束

由 (8)，对 $s\ge2$，
$$
 \omega_{d,s}
 =(-1)^{s-1}(s-1)!\,b_d^{\,1-s}
       (1+p^{q_p}\mathbb Z_p),\qquad \omega_{d,1}=1.
 \tag{28}
$$
第 $s\ge2$ 项中，替换此单位所产生的误差赋值至少
$q_p+s-1+v_p((s-1)!)\ge q_p+1$。另一方面，
$s\ge q_p+2$ 的权本来就有赋值至少 $q_p+1$。因此 (20)
有一个无需未知单位修正的明确截断：
$$
 \boxed{\quad
 \frac{J_F'(0)}{\lambda_{d,1}}
 \equiv
 \sum_{s=1}^{(p+1)/2}
 (-1)^{s-1}(s-1)!\,b_d^{\,1-s}g_{rs}(F)
             \pmod {p^{(p+1)/2}}.
 \quad}
 \tag{29}
$$
所有系数均为 $p$ 进整数。它是原完整泛函的有限精度公式，
不是把中央投影替换成乘法。

特别，当 $J_F'(0)=0$ 时，依次有
$$
 \begin{aligned}
 g_r(F)&\equiv0\pmod p,\\
 g_r(F)-b_d^{-1}g_{2r}(F)&\equiv0\pmod {p^2},\\
 g_r(F)-b_d^{-1}g_{2r}(F)
                 +2b_d^{-2}g_{3r}(F)&\equiv0\pmod {p^3}.
 \end{aligned}
 \tag{30}
$$
第三式对所有本篇 $p\ge7$ 合法；更高到 (29) 指定的精度亦同。
第二式与 R182 的
$g_{2r}\equiv d(pu_0)\,g_r/p\bmod p$ 完全相符。

应用于原两个坐标时，取同一个 $d=17$、同一个 $b_{17}=17u_0$，
得到两条完整等式
$$
 \sum_{s\ge1}\omega_{17,s}g_{rs}(A_2)=0,\qquad
 \sum_{s\ge1}\omega_{17,s}g_{rs}(B)=0
 \tag{31}
$$
当且仅当原两个 $J'$ 同时为零。它们也对两截面的任意整线性
组合成立。一般乘积具有不同的齐次次数，既不能沿用同一个
$d$，也不能从 (31) 推出其中央导数为零。

式 (21) 与 R182 原 $w$ 参数中全部稀疏行的检验
$\mathcal B^w_{t_n,1,0}\in p^{2n+2}$ 表述同一个完整零性。
本篇的优势是将所有精度写在同一个整轴、保留准确尾界，并把
前 $(p+1)/2$ 位的权变成显式阶乘系数。它没有证明两个
指定加权和之一必非零，也没有证明 (31) 已使 R159 的全部
混合前缀预算严格改善。

## 8. 范围及依赖

本篇只对 $p\nmid d$ 使用 $v_p(4dc)=-1$。在原次数至多 $D$
的源中，齐次部分的 $ab$ 次数为 $17m$；若 $p\mid m$，不能
不改规范地把本篇的赋值、半径和权公式套到该部分。

轴的整形式展开与 (11) 是证明原多项式取值的工具。没有把
任意 $g(V)\in V\mathbb Z_p[[V]]$ 当成原有限次数源中的一列，
也没有省略写回原 $a,b$ 或 $A_2,B$ 时的次数成本。

- [R54：准确 sigma 常数、闭余项盘与 Mahler 插值](R54-inert-analytic-half-factor-and-central-slope.md)；
  [较大余项盘的完整证明](../notes/2026-11-12-inert-half-factor-first-layer.md)。
- [R174：原 CM 整 Cartan 坐标及真实稀疏性](../notes/2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)。
- [R175：完整径向轴、首两带与实际中央矩](../notes/2026-11-12-euler-cartan-rows-and-joint-central-prefix-gain.md)。
- [R179 §6.1：同一整截面与任意带的齐次分解](../notes/2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R182：原 w 的完整中央检验及下一轴条件](../notes/2026-11-12-actual-first-as-carry-and-complete-central-rows.md)。
