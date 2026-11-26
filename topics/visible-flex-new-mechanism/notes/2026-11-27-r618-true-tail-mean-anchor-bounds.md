# R618 补充：整个真实内尾的同一均值分支与帽口积分界

日期：2026-11-27；会话 Astra-new-mechanism-1f4a61a4-20261127。

这是新 growing-post 模型所需的定量纸证及纯源码接口，未另开科学范围。
它复用 [R587](../results/R587-fixed-metric-mean-height-elimination-at-flat-cap-and-core.md)
的准确均值导数、[R600](../results/R600-same-mild-tail-flat-kernels-through-thirty-two.md)
的已证单谷/无限 DtN 递推，以及
[R618](../results/R618-fixed-metric-core-and-growing-post-response.md) 的同一固定 E 定义。
新内容是覆盖**整个原有限口以下**的显式正域盒、全部旧方向和新增 Gaussian
方向的统一界，以及真实 cap-to-mouth 均值高度积分。它不重做旧数值内口。

准确无限函数与原有限 M/浮点外传之间的误差仍是独立输入。
下面没有把有限口以下改成零，也没有把任意有限 J 的 Darboux 方程宣布为已解。

## 1. 固定对象与全区间假设

保持原温和尾

$$
r_c=11/50,\quad \ell=1/5,\quad A=4/5,\quad
u=\ell/(r-r_c),\quad W=Ae^{-u(2-\sin u)}.
\tag{1}
$$

取原真实口半径 $r_m$，$U=\ell/(r_m-r_c)\ge108$；不移动这个口。
目标 $E_*(r)$ 是已完整冻结的参考 $f_*$ 在 $p_0=-W$ 上的同一连续 turning 根。
记 $H=f-f_*$。以下所有上界均覆盖

$$
r_c<r\le r_m,\quad \theta\in\mathbb R/2\pi\mathbb Z,
\quad f_t=f_*+tH\ (0\le t\le1),\quad |\lambda|\le L,
\qquad p=-W+W\lambda+(f_t)_r.
\tag{2}
$$

假设有真实全区间界

$$
0<W\le W_+,\quad E_-\le E_*\le E_+,\qquad
|(f_t)_r|/W\le A_r,\quad |(f_t)_\theta|/W\le A_q,
\quad |(f_t)_{\theta\theta}|/W\le A_t.
\tag{3}
$$

这里下标 $t$ 在 $A_t$ 中仅表示二阶角导数，路径参数仍由 $f_t$ 标识。
定义

$$
P=1+L+A_r,\qquad
\beta^2=1-(W_+A_q/r_c)^2,
$$
$$
n_-=1-\frac{W_+^2PA_t}{r_c\beta^3},\qquad
n_+=\beta^{-1}+\frac{W_+^2PA_t}{r_c\beta^3},
$$
$$
v_-^2=E_--\frac{W_+^2P^2}{\beta^2},\qquad
C_-=r_c(1-L-A_r)-E_+A_t,
\qquad \kappa=\frac{C_-}{r_mE_+^{3/2}}.
\tag{4}
$$

要求 $L>0$、$L+A_r<1$，且 $\beta^2,n_-,v_-^2,C_->0$。
这些是可拒绝不合格 trial 的具体条件，不能以 $f\in\mathcal I(W)$ 替代。

令 $q=(f_t)_\theta$、$b=(r^2-q^2)^{1/2}$、
$v=(E_*-r^2p^2/b^2)^{1/2}$、
$N=r/b+r^2p(f_t)_{\theta\theta}/b^3$。
直接得到

$$
r\beta\le b\le r,\qquad v_-\le v\le\sqrt{E_+},
\qquad 0<n_-\le N\le n_+.
\tag{5}
$$

此外 $C=E_*(f_t)_{\theta\theta}+rp$ 满足 $C/W\le-C_-$。
用 R587 已证的准确导数（不再展开重证）及
$\omega=r^2/(v^3b^3)\ge1/(r_mE_+^{3/2})$，

$$
\partial_\lambda\frac{\langle N/v\rangle-1}{W^2}
=\frac{\langle\omega C\rangle}{W}\le-\kappa<0.
\tag{6}
$$

所以这里控制的是全盒上的真实连续均值，而非只在根端点或输出节点观察符号。
点态 $C<0$ 只作为这个很小内尾上的充分条件使用；身体中的均值分支仍允许
点态 $C$ 变号，不能把本条件推广成身体上的点除法。

若不另给 $E_\pm$ 的既有证明，可在同一参考盒上额外验证

$$
E_-<n_-^2,\qquad
E_+-W_+^2P^2/\beta^2>n_+^2.
\tag{7}
$$

此时在 $E_-$ 处 $\langle N/v\rangle\ge n_-/\sqrt{E_-}>1$，
在 $E_+$ 处则 $\langle N/v\rangle<1$。
因 $\partial_E\langle N/v\rangle=-\frac12\langle N/v^3\rangle<0$，
参考高度的同一 turning 根在整个尾都唯一地落在 $[E_-,E_+]$。
这里只用它包围冻结参考；不把每个 $f_t$ 的新 E 当成目标。

## 2. 显式响应与真实积分上界

在固定 $E_*,p_0$ 下，对自由高度增量 $K$ 的完整微分为

$$
\delta\mathcal T[K]=\left\langle a_rK_r+a_qK_\theta+a_tK_{\theta\theta}\right\rangle,
$$
$$
a_r=\frac{r^2 f_{\theta\theta}}{vb^3}+\frac{Nr^2p}{v^3b^2},\quad
a_t=\frac{r^2p}{vb^3},\quad
a_q=\frac{rq}{vb^3}+\frac{3r^2pf_{\theta\theta}q}{vb^5}
       +\frac{Nr^2p^2q}{v^3b^4}.
\tag{8}
$$

由(3)--(5)，$|a_i|\le W\ell_i$，其中

$$
\ell_r=\frac{A_t}{v_-r_c\beta^3}+\frac{n_+P}{v_-^3\beta^2},
\qquad \ell_t=\frac{P}{v_-r_c\beta^3},
$$
$$
\ell_q=\frac{A_q}{v_-r_c^2\beta^3}
 +\frac{3W_+^2PA_tA_q}{v_-r_c^3\beta^5}
 +\frac{n_+W_+^2P^2A_q}{v_-^3r_c^2\beta^4}.
\tag{9}
$$

设 $B_r,B_q,B_t$ 分别是整个尾上 $|H_r|/W,|H_\theta|/W,
|H_{\theta\theta}|/W$ 的上界，且

$$
\ell_rB_r+\ell_qB_q+\ell_tB_t<\kappa L.
\tag{10}
$$

参考在 $\lambda=0$ 有准确残差零。沿高度直线积分(8)，再用(6)，
得到新高度在 $\lambda=-L,+L$ 的严格相反符号。
每个 $(r,t)$ 都有这个盒内唯一根；根沿同一参考分支连续，并且

$$
|\lambda(r)|\le
\frac{\ell_r\|H_r(r)\|_\infty+
      \ell_q\|H_\theta(r)\|_\infty+
      \ell_t\|H_{\theta\theta}(r)\|_\infty}{\kappa W(r)}.
\tag{11}
$$

特别地，真实均值斜率修正 $s=W\lambda$ 满足

$$
\left|\int_{r_c}^{r_m}s(r)\,dr\right|
\le\frac{\ell_r I_r(H)+\ell_q I_q(H)+\ell_t I_t(H)}{\kappa},
\quad I_i(H)=\int_{r_c}^{r_m}\|\partial_iH(r,\cdot)\|_\infty\,dr.
\tag{12}
$$

这是**真实 cap 至原有限口**的积分，不是有限口为零的边界约定。
在任何当前真根上，隐式方向 $\delta s$ 同样满足(11)去掉 $W$ 后的式子，
其中 $H$ 换成该实际参数方向 $K$；故(12)也直接控制所有参数积分。
当高度方向属于原快速全平类，R587 的端点光滑结论继续给 $s$ 的真全平延伸。
这里新增的是从端点一直到原口的统一条件，未把局部隐函数结论直接当全区间结论。

允许将(12)的包围区间写成中心 0、严格正半径的积分输入。
这表示真积分被一个已证明区间包围，绝不表示把真函数或均值斜率置零。

## 3. 新 Gaussian 列的全部帽口界

沿已交付模型的同一参数，设 $r_m\le r_a<r_b$，$0<a\le40$，
$u_a=\ell/(r_a-r_c)$，且 $k\ge0$ 为整数。
在整个本节内尾 cut 函数准确为 1，所以新列就是

$$
T_k(r)=\left(\frac{r-r_c}{r_b-r_c}\right)^k
       \exp[-(u^2-u_a^2)/a]
=C_ku^{-k}e^{-u^2/a},\quad
C_k=e^{u_a^2/a}\left(\frac\ell{r_b-r_c}\right)^k.
\tag{13}
$$

它在真帽端准确全平而不在任何正宽尾段恒零。
直接微分给

$$
T_k'=\frac{2u^3/a+ku}{\ell}T_k>0,
$$
$$
|T_k''|\le\frac{4u^6/a^2+(4k+6)u^4/a+(k^2+k)u^2}{\ell^2}T_k.
\tag{14}
$$

第二行来自准确系数 $(4k-6)$、$(k^2-k)$ 的三角上界；没有丢掉多项式微分项。
定义在 $U$ 处的 $F_0=T_k(U)$，$F_1,F_2$ 为(14)右侧。
再把 $F_0$ 换成

$$
K_0=\frac1A\left(\frac\ell{r_b-r_c}\right)^kU^{-k}
       \exp[(u_a^2-U^2)/a+3U],
\tag{15}
$$

并用同一多项式定义 $K_1,K_2$。
则整个 $u\ge U\ge100$ 上

$$
|\partial_r^iT_k|\le F_i,\qquad
|\partial_r^iT_k|/W\le K_i\quad(0\le i\le2).
\tag{16}
$$

证明是逐项的：所有正多项式项均为常数乘
$u^m e^{-u^2/a+3u}$，其中 $m\le6$（负 $m$ 也允许），其对数导数满足
$m/u-2u/a+3\le6/100-5+3<0$。
不用一个只在 $U$ 成立的 $W$ 下界覆盖整段。

对真实 $L_jT=rWT''+rW'T'-j^2W'T$，有

$$
\sup\frac{|L_jT_k|}{W}
\le r_mF_2+\frac{3U^2+U^3}{\ell}(r_mF_1+j^2F_0),
$$
$$
\sup\frac{|L_jT_k|}{W^2}
\le r_mK_2+\frac{3U^2+U^3}{\ell}(r_mK_1+j^2K_0).
\tag{17}
$$

这里再次逐项使用最高次数6的衰减；$|W'/W|$ 本身在整个尾上无界，
不能先把它单独替成 $U$ 处的数值再乘一个无关上界。
这些源项是新列的真实非齐次输入，不是原非线性方程已要求的源项已经消去。

积分还可更尖且更简单：单调性给

$$
\int_{r_c}^{r_m}|T_k'|\,dr=F_0,
\qquad
\int_{r_c}^{r_m}T_k\,dr
\le\frac{a\ell}{2U^3}F_0=:J_k.
\tag{18}
$$

第二式将积分换成 $\ell C_k\int_U^\infty u^{-k-2}e^{-u^2/a}du$，
用 $u^{-k-3}\le U^{-k-3}$ 后准确积分 $u e^{-u^2/a}$。
因此实际系数 $d_{jk}T_k\cos(j\theta)$ 对(12)的贡献不超过

$$
\frac{|d_{jk}|}{\kappa}
\{\ell_rF_0+(j\ell_q+j^2\ell_t)J_k\}.
\tag{19}
$$

所有 $j,k$ 都必须求和；参数方向取其实际系数导数（模型中为原 amp），
不能只界主模或数值未 underflow 的列。

### 原口上的实际策略约束

原共同口的 $U$ 在108附近，不能仅凭 Gaussian 全平就断言 $a=40$ 合格：
(15)的指数在 $U=108$ 含 $-108^2/40+3\cdot108=32.4$。
它可能放大 $T_k/W$，因此(10)需实际核实。
未来若选 $a\le20$ 且原 $r_a\ge.30$，则 $u_a\le2.5$，对 $U\ge100$

$$
(u_a^2-U^2)/a+3U\le-2U+5/16.
\tag{20}
$$

这给真正整个尾的强余量，仍须加上原 germs、真实系数及所有 jet 多项式。
没有修改已发布模型允许 $a\le40$ 的一般定义，也没有在此制造新 q 或新运行。

## 4. 原全部方向的显式加权界

以下只扩充 R588 的归一后幅值估计至已付 R600 的有限集合，
不重复 R600 的 DtN/Green 证明。
对 $2\le j\le32$，$\mu=j^2$，令准确无限解 $y_j(\alpha_{17,j})=1$，
并沿原定义写

$$
S_j(r)=e^{-D_j}r^\mu y_j(u)/c_j,\qquad c_j\ne0.
\tag{21}
$$

其中 $D_j,c_j$ 是同一数学场的明确归一常数或已包围的参数，
不能把未认证的 ODE 输出自动当成精确核心归一。
R600 给 $108<\alpha_{17,j}<109$、$6<\alpha_{n+1}-\alpha_n<7$，
以及 $B=2^{32}$ 和

$$
\mathcal L(a)=Be^{21+2a},\quad
\varepsilon\le870000a^{-4},\quad
Y_{n+1}\le2^{41}e^{42}\alpha_{n+1}^4e^{-3\alpha_{n+1}/2}Y_n
           \le e^{-\alpha_{n+1}/2}Y_n.
\tag{22}
$$

最后一个不等式在100处由
$41\log2+42+4\log100<90<100$ 验证，此后 $a-4\log a$ 递增。
同一 Green 结论给单 cell 内 $|y|\le2Y_n$。
从一个平均值点的 $|y_u|\le Y_n/3$ 积分原方程，
因 $1/3+14\cdot870000/100^4<1$，得 $|y_u|\le\mathcal L(a)Y_n$。

令 $V=a+7$。原方程使
$f_{rr}=-(W'/W)(f_r-\mu f/r)$，$f=r^\mu y$。
用 $\mu/r<5000$、$1/\ell=5$、$|W'/W|\le6V^3$，得到

$$
\max_{i\le2}|\partial_r^if|
\le30V^5\mathcal L(a)Y_n.
\tag{23}
$$

除以 $W\ge Ae^{-3(a+7)}$ 后，右端为
$(30/A)Be^{42}(a+7)^5e^{5a}Y_n$。
相邻 cell 上界之比至多
$\exp[35+35/(a+7)-(a+6)/2]<1$。
因此全部无限 cells 由第一 cell 控制；$a<109,V<116$ 给这个上界小于 $e^{648}$。

余下共同小片 $108\le u\le\alpha_{17,j}$ 长度小于1。
R600 的准确一阶系数满足 $|g|<113,\varepsilon<1$，故一阶二系统
最大行和范数小于114。起点的 $|y|,|y_u|<e^{271}$，全小片上小于 $e^{385}$。
于是 $|f_r|<e^{398}$、$|f_{rr}|<e^{414}$；再除
$W\ge(4/5)e^{-327}$ 后小于 $e^{742}$。
统一取更宽的整数常数，得到

$$
\boxed{\sup_{u\ge108}\max_{0\le i\le2}
 \frac{|\partial_r^iS_j|}{W}
 \le C_j:=e^{750-D_j}/|c_j|.}
\tag{24}
$$

这同时保留节点交替符号、cell 全部内部点与共同口小片。
对任意旧方向系数 $d_jS_j\cos(j\theta)$，其 $B_r,B_q,B_t$ 贡献分别为
$|d_j|C_j,j|d_j|C_j,j^2|d_j|C_j$，而三种积分贡献可分别取

$$
(r_m-r_c)W_+|d_j|C_j\,(1,j,j^2).
\tag{25}
$$

实际模型的旧非均值差 $H$ 在本区间正是 $j=4,6,\ldots,22$ 的这些方向
加上(13)的全部新列：原 body bulk、compact 和 core lift/correction 在这里准确为零。
原固定 pre-tanh 和 forced 则仍属于**参考** $f_*$，不能从参考盒中删除。
core 自由项、tau 与所有仅身体支撑列的这里直接参数方向为零，这来自真实支撑，
并非截断内尾。

## 5. 参考 canonical512、包络与 forced 的完整计入法

记旧 pre-tanh 为 $V=\sum_{j\in\{2,4,6,8\}}v_j(r)\cos(j\theta)$。
其原正包络为

$$
\mathcal B=\frac{\sum_{j\le8}(S_j/m_j)^2+
    e^{-\gamma/(r-r_c)^4}(R-r)^p}{C_*},
\quad\gamma=10^{-4},\ p=2+2\alpha,
\tag{26}
$$

全部 $m_j,C_*$ 保持原定义。
若 $0<R-r_c\le1$、$d_-=R-r_m>0$，且
$5/U-4\gamma U^3/\ell^4+3<0$，逐项单调性给

$$
G_0=A^{-1}\exp[-\gamma U^4/\ell^4+3U],\qquad
G_1=\{4\gamma U^5/\ell^5+p/d_-\}G_0,
$$
$$
\|\mathcal B/W\|_\infty\le
\frac{W_+\sum_j(C_j/m_j)^2+G_0}{C_*}=:B_0,
\qquad
\|\mathcal B'/W\|_\infty\le
\frac{2W_+\sum_j(C_j/m_j)^2+G_1}{C_*}=:B_1.
\tag{27}
$$

这里没有把 quartic 指数的浮点 underflow 当作准确零。
对原每个五次 B 样条 $\psi_i$，使用其真实 $P_i\ge\|\psi_i\|_\infty$、
$Q_i\ge\|\psi_i'\|_\infty$。原非负 clamped 基可以取 $P_i=1$；
导数由两个相邻四次基的准确公式给
$Q_i=5/(t_{i+5}-t_i)+5/(t_{i+6}-t_{i+1})$，
重复端点导致的零分母项按原 B 样条定义省略，不能删任何非零宽 knot 区间。
于是 $v_j=a_jS_j+\mathcal B\sum_i b_{ji}\psi_i$ 有

$$
V_{j,0}=|a_j|C_j+B_0\sum_i|b_{ji}|P_i,\qquad
V_{j,1}=|a_j|C_j+\sum_i|b_{ji}|(B_1P_i+B_0Q_i).
\tag{28}
$$

用 $V_r^+=\sum_jV_{j,1}$、$V_q^+=\sum_jjV_{j,0}$、
$V_t^+=\sum_jj^2V_{j,0}$。
因 $F(x)=\sigma\tanh(x/\sigma)$ 的 $|F'|\le1,|F''|\le2/\sigma$，
且原 canonical512 均值是固定正均值，原非线性项的三种比例界为

$$
2V_r^+,\qquad V_q^+,\qquad V_t^++(2W_+/\sigma)(V_q^+)^2.
\tag{29}
$$

减去 canonical512 均值只在第一项多一个同样的径向导数界；
这里没有改成输出网格的均值，也不要求该固定均值等于连续均值。
最后加入原 literal q 的 $j=4,\ldots,22$ post 项，以及原 forced $j=4$ 项。
后者在此准确为原 `tail_multiplier / scale` 乘未除核心 $c_4$ 的同一个
raw $e^{-D_4}r^{16}y_4$，因此可用(24)取 $c=1$ 后乘其**完整实际系数**。
这些参考贡献加上 H 的三种 B 界，才是(3)的 $A_r,A_q,A_t$。

## 6. 源码消费边界

新 helper `r618_analytic_tail_anchor_bound_20261127.py` 只实现以上正量区间
算式、全部系数求和、参考非线性传递、全盒检查和积分半径；科学调用仍限
后来已声明的公开 Actions 范围。它不求新 DtN、不补造原 ODE 精度。

实际 `tail_anchor` 必须由当前完整 source/response/model 身份下的输入界生产，
特别是 Gaussian 的 a、cutoff、次数、全部旧归一和参数方向都要一致。
该身份要放在输入端，由已交付高度模型强制核对，不可在消费端把异模型结果重新贴标签。
原有限 M、数值 Cauchy/ODE、准确归一、root、roundoff 的未付误差继续明确列出。
只有这些输入都被包围时，(12)才是可传给真帽积分的严格误差半径。
即使如此，它仍只解决均值分支和帽口积分；身体非零角方程、无限角带收敛、
实际位置误差、宏观固定 H/位移以及完整 reach 仍按原 open 主线继续。
