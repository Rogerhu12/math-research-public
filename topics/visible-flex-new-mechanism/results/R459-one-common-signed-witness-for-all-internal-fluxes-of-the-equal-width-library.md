# R459：同权零全 current 补偿与同宽全角色内部通量的一个共同正字符核见证

日期：2026-11-16。完整原式纸面证明；没有执行新的 forcing、符号化简、profile 积分、矩阵求秩、人工检查或研究程序。

本稿把 [R457](R457-natural-seven-current-quotient-complete-normalization-and-weight-zero-witness.md) 的
$\widehat H=H_*+J_4$
推进到同一个成本上的全部内部 $A_f$ 点。先在**完整**响应空间中将整个有序 current 清零，并用真实权零投影保住完整 self 的八次平移界；再用 R448 的一个原成本右逆，同时清除所有微包角色和全部对应副本的 self partial。

结论适用于从起点选定共同物理宽度、具有 R455 唯一共同镜对的完整新母库，包括已经从起点纳入的 R450 八宏复制。它不把原已冻结的多宽库改成同宽，也不把这个有号成员当成实际正时间路径。

直接来源：
[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、
[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、
[R356](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md)、
[R407](R407-connected-moment-fibers-fix-self-caps-and-retain-the-actual-total-fluxes.md)、
[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md)、
[R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md)、
[R448](R448-nineteen-real-mirror-fluxes-and-the-complete-thirty-dimensional-self-remainder.md)、
[R451](R451-weight-zero-positive-representative-on-complete-real-mirror-copy-families.md)、
[R454](R454-complete-response-self-principal-trace-and-seven-ordered-current-invariants.md)、
[R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md)、
R457。

## 1. 固定新库与完整目标

沿 R455 §§7—9，先选共同物理宽度 $w_0>0$，再固定全部有限布局、正幅、整块 $g$ 翻号及允许的共同支持窗口。最终母形 $U_i$ 与参考母 $U_0$ 具有：

- 四个完整 natural 约束 $q(U_i)=q(U_0)=0$；
- 相同的三矩 $\mu$，以及原 $F^\star=(F_{\rm rat},D,E_5)$；
- 共同的两个简单 $A_U$ 根及其整个外邻域；
- 沿固定严格内区变化、保持全部三矩的实际光滑连通路径。

将 $w_0$ 收入物理母 $u_i(x)=U_i(x/w_0)$、$u(x)=U_0(x/w_0)$。共同镜点写为 $\pm b$，其真实 jets 为
$$
u(-b)=u(b)=u_*,\qquad
u'(-b)=p_*,\quad u'(b)=-p_*,
\qquad u''(\pm b)=r_*,
\tag{1}
$$
其中 R455 给 $p_*\ne0$、$r_*>0$。记
$$
s=p_*/r_*,\qquad h_{\rm jet}=u_*/r_*.
$$
这里 $h_{\rm jet}$ 是 profile 比值，不是几何标量 $h$。

为避免幅度重复，以下将每个完整复制的共同实幅收入两个实际系数 $a_i,b_i$，写
$$
f=\sum_i a_i u_i(\,\cdot-\xi_i),\qquad
g=\sum_i b_i u_i(\,\cdot-\xi_i).
$$
所有微包值支撑严格不交。令
$$
R_i=a_i^2-b_i^2,\qquad T_i=a_i b_i,
$$
$$
n_{R,i}=\sum_{j>i}R_j\mu_j,\qquad
n_{T,i}=\sum_{j>i}T_j\mu_j.
\tag{2}
$$
$\mu_j$ 是已平移到真实位置 $\xi_j$ 的三个矩；(2)包含全部 high/low、五块、八/十二包装和八宏复制，不重置任何后缀。

固定原共同查询
$$
J^+=(E,A,O_{\rm all}).
\tag{3}
$$
$E$ 是 whole pure 与 whole self-$Q$；$A$ 是当前实际母和所需有序查询的有限共同仿射闭包；$O_{\rm all}$ 是 universal ordered $3+2$ natural 查询。它不包含所有母的 universal self natural 函数。

对 $E(V)=O_{\rm all}(V)=0$，R433 给完整有序输出
$\mathcal U_{V,n}=4Q_{V,n}$
及其原左锚累计
$$
\mathcal K_{V,n}(x;v)
=\int_{\ell}^{x}v'\,\mathcal U_{V,n}(v)''.
\tag{4}
$$
在 $A_v=6v'v'''-2(v'')^2=0$ 处，$\mathcal K/4$ 是 R433 的完整 39 坐标形式。记此映射为 $\mathscr C(V)$。本文的
$\mathscr C(V)=0$
始终指**对任意真实三矩 $n$ 和全部允许的 Af jets，整个形式 current 为零**，比只在某些实际后缀上令
$R_iH_e+T_iH_d=0$
更强。

self partial 则另记
$$
\mathfrak h_{\alpha,v}(V)
=\int_\ell^\alpha v'\,\Sigma_V(v)'',
\qquad \Sigma_V(v)=V(v^2,0).
\tag{5}
$$
(5)没有除以4；不能将它与(4)的 39 坐标归一混用。

## 2. 原初选构造确实允许共同物理宽度

此处需要原构造支持，不能只从镜对线性代数倒推布局可改。

R280 §§1、3 以共同 even 母的平移起步，将共同包宽收入母内；其三矩写为
$m(1,t_i,t_i^2+\nu)$。
R280 §4 的两个正、负布局使用同一个格距，交换的是17进制与二进制的有限索引层。它们没有对不同微包施加不同宽度。§§6—8 的五块面积支付只使用完整 block 的平移及正四次幅；共同母宽不变。

[R324 §§6、9](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md)
的十九个 principal 经所有完整复制，仍由
$\sum_\nu w_\nu P(X+d_\nu)$
这个正权三角可逆算子输运。它不要求不同的 profile 宽度。
[R447 §§3—4](R447-twenty-common-profile-targets-and-a-nonzero-highest-P-gauge-direction.md)
更明确证明：对任意固定正 $w_0$，真实偶点对
$X\pm w_0b$ 和可逆 jet 缩放
$(u,p,r)\mapsto(u,p/w_0,r/w_0^2)$
仍给原二十行独立性及各十二交替列的严格正核。

[R450 §11](R450-seventeen-degree-true-inverse-and-exact-second-period-macro-cancellation.md)
新增的八宏复制同样只是完整 base 的平移、实幅及整块 $g$ 翻号。其全部新低阶/cross 基准先收入原完整 $b_{\rm new}$，二十目标的主输运仍是正权平移平均。R450 §11.1 已逐类支付旧 $F^\star$ 精确身份与连续 $C^2$ 基准，不需要在这里另加形状观察。

因此可在 R455 的四约束图册、限制最大 $F^\star$ minor 及二十目标求根之前，统一选定 $w_0$，再取所需有限间距与合法窗口；原全部复制、面积、三矩、十九门及非零最高 $d_P$ 构造仍可进行。最后有限根以后，不再改变宽度、布局、幅度或冻结纤维。

本稿只使用这种**新初选的共同宽度库**。对于预先固定的多宽库，下面单个镜对右逆并不自动适用。

## 3. 完整 current 的真实仿射输运

先给成本层面的等变式，以便后面的权零投影作用于完整 current，而不是仅作用于某个点值。

令
$$
(C_{H,c}v)(y)=v((y-c)/H),\qquad H>0,
$$
并沿 R89 取原成本作用
$P_{H,c}V=C_{H,c}^{-1}V(C_{H,c}\,\cdot)$。
三个矩的真实输运是
$$
\mu(C_{H,c}w)=H^{-3}T_{H,c}\mu(w),
$$
$$
T_{H,c}(n_0,n_1,n_2)
=(n_0,\ c n_0+Hn_1,\ c^2n_0+2cHn_1+H^2n_2).
\tag{6}
$$
第三矩中的 $2(w')^2$ 与 $x^2(w'')^2$ 共同给(6)，没有单独丢弃第一导数项。

原同锚恢复与成本协变给
$$
\mathcal U_{P_{H,c}V,n}(v)(x)
=\mathcal U_{V,H^{-3}T_{H,c}n}(C_{H,c}v)(Hx+c).
\tag{7}
$$
在(4)中令 $y=Hx+c$。输入一次导数、输出二次导数及积分测度分别产生 $H,H^2,H^{-1}$，所以先得 $H^2$；再用(7)对矩的线性性，得到
$$
\boxed{
\mathcal K_{P_{H,c}V,n}(x;v)
=H^{-1}\mathcal K_{V,T_{H,c}n}(Hx+c;C_{H,c}v).
}
\tag{8}
$$
左右端随同一真实仿射作用输运；没有新增原始积分常数。

若 $F_V=\mathcal K_V/4$ 表示 Af 上的完整 jet 多项式，则(8)等价于
$$
\boxed{
F_{P_{H,c}V}(x,u,p,r;n)
=H^{-1}F_V(Hx+c,u,p/H,r/H^2;T_{H,c}n).
}
\tag{9}
$$
$A_v$ 本身乘 $H^{-4}$，故 Af 条件也准确输运。先在所有相关输入及原型共用的合法 collar 参数域内证明(7)—(9)，再使用有限多项式身份；不以形式平移取代窗口条件。

完整响应的稳定性也可从原生成式逐项看出。R105/R109 的
$\mathcal R=\operatorname{span}\{\mathcal B_E\tau:E\in E_8,\tau\in W\}$
满足
$$
P_{H,c}(\mathcal B_E\tau)
=\mathcal B_{P_{H,c}E}(P_{H,c}\tau).
$$
原二阶空间 $E_8$ 与完整第三空间 $W$ 在 R89 的同锚作用下稳定，故整个 $\mathcal R$ 稳定。
[R323 §6.1](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)
由 pure 协变和 whole-$Q$ 左二次尾的准确变换，另已证明 $\ker E$ 稳定。
所有 $\mathcal R$ 的完整 natural 函数为零，所以其成本也杀当前 $A$ 与 $O_{\rm all}$。这里没有断言固定查询 $A$ 对任意输入自动仿射稳定，也没有断言原144标签的有限子空间本身稳定。

## 4. 同一个真权零响应清除整个有序 current

R457 已给
$$
\widehat H=H_*+J_4\in U_0\cap\ker J^+,\qquad
\lambda_+(\widehat H)=1,\qquad
\mathfrak d(\widehat H)=0.
\tag{10}
$$
又因 $E=O_{\rm all}=0$，该文自然修正与原 current 对角一致：
$$
D(\mathscr C(\widehat H))=\mathfrak d(\widehat H)=0.
$$

R454 的完整响应像定理是
$$
\mathscr C(\mathcal R\cap\ker E)=\ker D
\subset\mathscr F_{39}.
\tag{11}
$$
它使用 R434 已付32个完整 lifts 给满像，随后用全 $\mathcal R$ 的 trace 身份给上界。不是仅从原144列猜整个响应空间。

固定这些已付 lifts 在 $\ker D$ 上的一个线性右逆 $\iota$，置
$$
R=\iota\bigl(\mathscr C(\widehat H)\bigr)
\in\mathcal R\cap\ker E.
\tag{12}
$$
(12)是同一个完整成本；它同时支付三后缀、全部形式 jets 和全部位置，没有为各角色另选响应。

任意加入一个混权 $R$ 会破坏后面的八次 self 界。因此必须在这里取真正的权零分量。原 $U$ 的真权支撑为 $[-9,3]$。取13个不同且足够接近1的正数 $H_\nu$，令 $c_\nu$ 为准确插值系数
$$
\sum_{\nu=1}^{13}c_\nu H_\nu^\sigma
=\begin{cases}1,&\sigma=0,\\0,&-9\le\sigma\le3,\ \sigma\ne0.\end{cases}
\tag{13}
$$
乘回 $H_\nu^9$ 后是普通 Vandermonde，故此有限实系数表存在；特别 $\sum c_\nu=1$。定义
$$
\Pi_0=\sum_{\nu=1}^{13}c_\nu P_{H_\nu,0},
\qquad R_C=\Pi_0R .
\tag{14}
$$
这是**有号线性谱投影**，不将 $c_\nu$ 当成正时间或复制次数。

由完整 $\mathcal R\cap\ker E$ 的稳定性，
$R_C\in\mathcal R_0\cap\ker E$。
由(9)、(12)及 $P_{H,0}\widehat H=\widehat H$，
$$
\mathscr C(P_{H,0}R)=
\mathscr C(P_{H,0}\widehat H)=\mathscr C(\widehat H).
$$
再用 $\sum c_\nu=1$，得到
$$
\boxed{\mathscr C(R_C)=\mathscr C(\widehat H).}
\tag{15}
$$
这一步不需要证明144标签在正伸缩下闭合。

置
$$
V_0=\widehat H-R_C.
$$
原响应杀 $\lambda_+$ 和全部 natural 函数，所以
$$
\boxed{
V_0\in U_0\cap\ker J^+,\qquad
\mathscr C(V_0)=0,\qquad
\lambda_+(V_0)=1,\qquad
\Lambda(V_0)=n_2 .
}
\tag{16}
$$
$n_2=\Lambda(H_*)$ 是 R406 的完整非零局部五次函数。它在当前每个母及全部允许正仿射输运上为零；(16)不声称 universal $\Lambda_{\rm all}(V_0)=0$。

## 5. formal current 零准确清除所有角色的后缀项

在 $E=0$ 及当前整包 natural 查询零的范围，R389/R397/R407 的原逐包公式给
$$
H_{d,i,\alpha}(V)
=a_i^3\left\{R_i\,\mathfrak h_{i,\alpha}(V)
+\mathcal K_{V,n_{R,i}}(x_{i,\alpha};u_i(\cdot-\xi_i))\right\},
$$
$$
H_{e,i,\alpha}(V)
=-a_i^3\left\{T_i\,\mathfrak h_{i,\alpha}(V)
+\mathcal K_{V,n_{T,i}}(x_{i,\alpha};u_i(\cdot-\xi_i))\right\}.
\tag{17}
$$
whole-$Q$ 使真实平台的二次部分为零；其它包左尾的剩余仿射部分二导为零。式(17)中仍保留所有右包的三矩，不假它们逐包为零。

对(16)，由**形式**身份(15)而非某个特殊后缀消去，任意 $n$ 都有
$$
\mathcal K_{V_0,n}(x_{i,\alpha};u_i(\cdot-\xi_i))=0.
$$
因此全部包、全部角色、全部实际复制一并满足
$$
\boxed{
H_{d,i,\alpha}(V_0)=a_i^3R_i\mathfrak h_{i,\alpha}(V_0),
\qquad
H_{e,i,\alpha}(V_0)=-a_i^3T_i\mathfrak h_{i,\alpha}(V_0).
}
\tag{18}
$$
这正是从 R451 的同角色结果跨到全角色所需的步骤。两次独立给各角色选择 self 校正并不能代替(15)—(18)。

## 6. 任意真权零 V0 的完整 self 八次项

下面使用的是完整 $\Sigma$，不是只读总自然通量或左二次尾。

令 $N$ 为原平移导子。R356 已证明
$$
\Sigma(U_{-9})=0,\qquad
\Sigma(U_{-8})\subset\operatorname{span}\{\mathcal T_R,r^4\},
$$
$$
\mathcal T_R=4J^2(r^2t^2)-4J(prt^2)-r^4,
\qquad p=u',\quad r=u'',\quad t=u''' .
\tag{19}
$$
这些原两层身份适用于(16)的整个 $V_0$，包括新增 $R_C$ 的 self。由于
$N^9V_0\in U_{-9}$、$N^{10}V_0=0$，真实共同平移的完整 self 与每个原 partial 都是次数至多8的多项式。

存在两个共同实常数 $\alpha,\beta$，使
$$
\Sigma_{N^8V_0}=\alpha\mathcal T_R+\beta r^4.
\tag{20}
$$
它们来自原成本，与根、包位置、幅度及宽度无关。无需新运行求其数值。

R330/R451 的完整同锚身份为
$$
2\mathcal T_R=-r^4/3-\frac23 L_u\{P(u,u)\},
\qquad P(u,u)=J(r^2).
\tag{21}
$$
$P(u,u)$ 有真实左常数。原通量身份
$$
pL_u(w)''=\partial_x\{A_u(pw''-rw')\}
\tag{22}
$$
对这个非紧 $w$ 仍成立。左平端和外 Af 点分别使两端通量为零；没有把 $P$ 改成紧 profile。

另由完整分部积分，在 Af 点
$$
\int_\ell^\alpha p(r^4)''
=4pr^3t-\frac45r^5=\frac8{15}r(\alpha)^5.
\tag{23}
$$
所以 $\mathcal T_R$ 的 partial 为 $-4r^5/45$。由(20)，两个共同镜点的 self 八次系数除回 $r_*^5$ 后准确相同。

若需要先显式删去该项，原
$K_n=\delta^nK_0$、
$\Sigma_{K_0}=-r^4/3$
满足
$$
N^8K_8=8!\frac{10!}{2}K_0.
$$
因此同一个系数
$$
\gamma=\frac{\alpha-6\beta}{8!\,10!}
\tag{24}
$$
给
$$
\Sigma_{N^8(V_0-\gamma K_8)}
=-\frac{\alpha}{3}L_u\{P(u,u)\}.
\tag{25}
$$
(22)使(25)在每个 Af 点的 partial 为零。这个结论不仅限于一对根，但本稿随后只在当前唯一共同镜对上使用一个完整右逆。

## 7. 同矩内区路径把完整 self 目标移到同一个参考母

这里不能仅用最终母的 jets 相同来替代完整 self history。

沿第1节的同三矩路径 $u_{i,t}$，原二阶极化场
$Z(u_{i,t},\dot u_{i,t})$
在变化内区的两侧完整为零。R407(7)—(11)由此得到
$$
\partial_t\Sigma_{V,u_{i,t}}
=-4\mathscr K\bigl(Z_{u_{i,t}},Z(u_{i,t},\dot u_{i,t})\bigr).
$$
左外区是一个真实二次多项式，右外区为零；whole-$Q(V)=0$ 再使左二次系数为零，遂有
$$
\Sigma_{V,u_i}''=\Sigma_{V,u}''\quad\text{在共同两个外 cap}.
\tag{26}
$$
这是沿已构造连通路径的完整身份，不是假定整个同矩纤维连通。它对原实际成本的有限实组合线性延拓，因而适用于 $V_0$ 和以下全部响应。

左根的(5)只经过左 cap，所以(26)直接转移该 partial。右根还须保整个包的真实总通量：
$$
\int_\ell^{r_*}v'\Sigma_V(v)''
=\int_\ell^{r_*}v'''\Sigma_V(v)=\Omega_v(V).
\tag{27}
$$
两次分部的边项由输入端 jets 为零支付；没有要求 $\Sigma_V$ 左紧。

对 $V_0$，pure 为零，故 $\Omega_v(V_0)=\Lambda_v(V_0)=n_2(v)$。
参考母与所有最终母都满足四个 $q$ 约束，因此它们的全部允许平移/正伸缩输入都使(27)为零。右根的左累计等于负的右 cap 积分，故(26)也给右根 partial 完全相同。

于是，在每个实际中心 $\xi_i$，
$$
\boxed{
\mathfrak h_{\xi_i\pm b,u_i(\cdot-\xi_i)}(V_0)
=\mathfrak h_{\xi_i\pm b,u(\cdot-\xi_i)}(V_0).
}
\tag{28}
$$
共同内区可以有许多个简单 $p$ 零点；本证明既不删除它们，也不从(28)宣告其 Laurent/range 条件已满足。

## 8. 一个原响应 W 同时清除全角色、全复制的 self

定义参考母的真实平移 partial
$$
h_\pm(c)=\mathfrak h_{c\pm b,u(\cdot-c)}(V_0).
$$
按实际根坐标 $x$ 归一为
$$
P_-(x)=r_*^{-5}h_-(x+b),\qquad
P_+(x)=r_*^{-5}h_+(x-b).
\tag{29}
$$
第6节证明 $P_\pm\in\operatorname{Pol}_{\le8}$，且二者八次系数相同。

R448 在这个固定物理镜对上的原49维成本模块 $\mathscr M$ 满足
$$
\operatorname{ev}_{s,h_{\rm jet}}\mathscr M
=\{(P,\mathsf T P+Q):P\in\operatorname{Pol}_{\le10},
\ Q\in\operatorname{Pol}_{\le7}\}.
\tag{30}
$$
$\mathsf T$ 由完整 $K_0,\ldots,K_{10}$ 左镜多项式的三角逆定义，保次数与最高系数；不能把它换成只凭奇偶猜得的反射算子。全部 $\mathscr M$ 成本都满足
$$
E=0,\qquad \Lambda_{\rm all}=0,\qquad \mathscr C=0.
\tag{31}
$$
(31)来自 R443 的同一 whole-$Q$/三尾完整 current 核证书及原 K 轨道，不是只在十九个采样点成立。

由(29)—(30)，
$$
Q_*(x)=P_+(x)-\mathsf T P_-(x)\in\operatorname{Pol}_{\le7}.
\tag{32}
$$
使用 R448(12)、(19)的**原成本**右逆 $\mathscr K[P]$ 与 $L_0,\ldots,L_7$，置
$$
\boxed{
W=\mathscr K[P_-]+\sum_{j=0}^{7}[x^j]Q_*\,L_j .
}
\tag{33}
$$
每个系数由同一个固定 $s,h_{\rm jet}$、整个 $V_0$ 和原 right-inverse 决定。原
$\mathscr K[P_-]$
使用完整 $\kappa_n^\pm$，所有 lower terms 与真实常数都保留。没有对不同角色、中心或宏块分别选 $W$。

式(30)—(33)准确匹配两个**完整多项式**，故在每个允许的实际中心，
$$
\mathfrak h_{\xi\pm b,u(\cdot-\xi)}(V_0-W)=0.
\tag{34}
$$
这不是先看十九个值再假定未知目标次数；次数已由(19)—(29)证明。事实上 $K_9,K_{10}$ 系数为零，$K_8$ 系数恰为(24)。

$W$ 同样可用第7节的 cap 身份；其 universal natural 函数为零，故参考与最终母的右根总通量条件自动成立。由(28)、(31)、(34)，最终一个成本
$$
\boxed{V_\#=H_*+J_4-R_C-W}
\tag{35}
$$
满足
$$
\boxed{
J^+(V_\#)=0,\qquad
\mathscr C(V_\#)=0,\qquad
\Lambda(V_\#)=n_2,\qquad
\lambda_+(V_\#)=1,
}
\tag{36}
$$
以及每个最终微包的两个真实 partial
$$
\boxed{\mathfrak h_{i,-}(V_\#)=\mathfrak h_{i,+}(V_\#)=0.}
\tag{37}
$$

若改用显式 profile 幅 $\rho_i u_i(\cdot-\xi_i)$，(5)准确乘 $\rho_i^5$；(34)—(37)因此仍成立。不得把第五次幅替换成 natural 或布局中的另一差分权。本文的(2)、(17)已把所有共同复制幅收入真实 $a_i,b_i$，故实际 $a_i^3R_i$、$a_i^3T_i$ 本身具有所需五次齐次性。

将(36)—(37)代入(17)，得到本稿的新全角色结论：
$$
\boxed{
H_{d,i,-}(V_\#)=H_{d,i,+}(V_\#)
=H_{e,i,-}(V_\#)=H_{e,i,+}(V_\#)=0
\quad\text{对全部 }i .
}
\tag{38}
$$
所有 high/low、五块及8×12宏复制使用同一个 $V_\#$。各自真实后缀可以不同；它们已由整个形式 current 核一次消去。

## 9. 新增有限查询仍不能使 λ+ 下降

令 $\mathcal P_{\rm int}$ 收集当前整个有限库的全部原 $d/e$ 内部 Af 累计门，并定义
$$
J_{\rm int}=(J^+,\mathcal P_{\rm int}).
$$
由(35)—(38)，
$$
\boxed{
V_\#\in\ker J_{\rm int},\qquad \lambda_+(V_\#)=1.
}
\tag{39}
$$
所以 $\lambda_+$ 不能经这个**同一个完整**有限查询映射下降。它不只是对一个角色、一个镜点或19个特别选点的核见证。

有限谱投影(14)的作用是让 $V_0$ 保真权零，从而先得到严格八次上界。之后的完整 $W$ 可以混权；最终 $V_\#$ 不必属于 $U_0$。不能再拿最终成本自动套用只对权零输入成立的次数结论。需要的每个门已在(33)—(38)中先准确匹配。

仍明确保留以下边界：

- (39)是原成本空间中的有号成员，不是一条实际正时间闭路径；原型完整成本、整数复制、桥、真倒行、Klein 基准和同一有限 IFT 尚须在新增联合映射上支付。
- 不由 $\lambda_+$ 不下降宣布其余正字符都已排除，也不把两个独立 actual 截面相加。
- 同宽假设在第2节从起点落实；固定多宽库需要额外的共同 self 右逆，不能分别用不同 $W$ 后相加。
- (38)支付全部真实 Af 点累计必要门，但不等于整个 $L_f$ range：各简单 $p$ 点的允许极性、gap/collar、真实端 germ、两个周期特解仍须完整检查。
- 同一个独立二阶规范的十三行、最高 $d/e$ 基准及其余端口行没有由(38)自动支付。R450 的条件性最高 $e$ 复制身份仍保其真 range 前提。
- $\Lambda(V_\#)=n_2$ 是非零 universal 函数；只有当前共同母的实际自然查询为零。因此本稿不违反 R406 的 universal natural 正字符障碍。

本稿新增的是一个全角色的共同原成本核见证，及其所需的完整 current 等变、真权零补偿和 self 次数证明。所有 source lifts 均来自已付原响应，未重做旧像、旧秩或旧 forcing。
