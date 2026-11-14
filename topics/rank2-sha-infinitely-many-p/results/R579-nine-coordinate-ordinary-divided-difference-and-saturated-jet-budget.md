# R579 — 九个真实 w 坐标在全部普通位的差商范数与饱和 jet 成本

日期：2026-11-14。**状态：已证明。**

对 R575 的正幂规整七塔与原 $S,T$，本文支付同一个九坐标单项式格、
全部次数和全部饱和前缀的普通局部估计。
关键是使用实际有限阶分布的连续差商范数，
并证明其卷积及下降阶乘差商的完整界；
不把一般有限阶分布误写成“有限和有界测度的导数”。

结论不要求 $I_4=I_1=0$，也不删去原 Dirac 缺陷。
所有好普通素数都计入，不仅原用于核心运输的固定射线。

## 1. 同一个真实九坐标和饱和格

先在 R418/R540 的共同 $E_0:y^2=x^3+1$ frame 工作。
令 $w=z^6$，采用 R575 已证明的七个整坐标
$$
V_{4,r}=z^{2-r}U_{4,r}\quad(r=1,2),\qquad
V_{1,r}=z^{5-r}U_{1,r}\quad(r=1,\ldots,5).
$$
整个坐标向量为
$$
\boxed{\mathbf G=(S,T,V_{4,1},V_{4,2},
                    V_{1,1},\ldots,V_{1,5}).}
\tag{1}
$$
它们全部是有理系数的整 $w$ 函数，均在 $w=0$ 至少一阶零。
R418/R575 已付其真实超越次数九及统一有限型增长界。
本篇不另换成九个仅有相同初始 jet 的来源。

对所有 $D,k\ge1$，保持原单项式格
$$
E_D^{(9)}=\bigoplus_{|\mathbf a|\le D}\mathbf Z\,\mathbf X^{\mathbf a},
\qquad N_D=\binom{D+9}{9},
$$
$$
r_h(P)=[w^h]P(\mathbf G(w)),\qquad
K_{D,k}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_D^{(9)}.
\tag{2}
$$
$\varphi_D^k$ 是 $r_k$ 在该真实饱和前缀上的限制。
局部范数使用 (2) 的单项式最大系数范数。
如果这一层不增加秩，算子为零；下面的界仍成立。

## 2. 全部普通 p 的原来源，而非仅固定射线

除去固定有限坏集，取任意 $p\equiv1\bmod6$。
R418 的原 $S,T$ 在同一单位周期 $\Omega_{p,0}$ 下给范数至多一的有界测度。

对 $f_{4,0}=x\sigma^6$、$f_{1,0}=-xy\sigma^6$，
R540 §7.1–7.3 已独立支付整个 degree $6$ 迹及所有普通 $p$ 的准确公式
$$
\boxed{
\nu_{j,0}|_{p\mathbf Z_p}
=\beta_p[\kappa_p]_*\nu_{j,0},\quad
\beta_p=\frac{\xi(\mathfrak p)}{\bar\pi_0},\quad
\kappa_p=\frac p{\bar\pi_0^2},\quad j=4,1.
}
\tag{3}
$$
$\xi$ 是原已付的完整有限角色；$|\beta_p|_p=1$、
$v_p(\kappa_p)=1$，且 $\|\nu_{j,0}\|\le1$。
在原固定射线上 (3) 退化成 R575 使用的 $\beta$，但本篇不作该限制，
也不把射线外的根单位猜成一。
下面仅使用其真实单位性质。

因此 R575 的同一构造在每个这样的普通 $p$ 都有效。
对 $f_\ell$ 的 $r$ 次原函数，记
$$
\tau=1_{\mathbf Z_p^\times}(t)t^{-r}\nu_{\ell,0},
\quad I=\tau(1),\quad \tau^\circ=\tau-I\delta_0,
$$
$$
\rho_{\ell,r}
=\sum_{n\ge0}\beta_p^n\kappa_p^{-rn}
 [\kappa_p^n]_*\tau^\circ.
\tag{4}
$$
$\|\tau^\circ\|\le1$，且其 $0,\ldots,r$ 次矩全零。
这些事实对两个可能非零的 $I$ 仍成立，不能以省略 $I\delta_0$ 代替。

## 3. 差商范数和原正则化系列的统一单位界

对一个 $\mathbf C_p$ 系数多项式 $\phi$，用连续延拓到重合节点的对称差商
$\phi^{[j]}(t_0,\ldots,t_j)$，定义
$$
\boxed{
\|\phi\|_{r,p}
=\max_{0\le j\le r}\sup_{t_0,\ldots,t_j\in\mathbf Z_p}
 |\phi^{[j]}(t_0,\ldots,t_j)|_p.
}
\tag{5}
$$
这是真正包含所有节点的差商范数，不只是普通导数范数。
以下论证对多项式及其相应 $C^r$ 完备化都适用；
饱和 jet 的应用只需多项式测试。

在原点的精确 Newton 余项是
$$
\phi(t)=\sum_{j=0}^{r-1}\phi^{[j]}(0,\ldots,0)t^j
+t^r\phi^{[r]}(t,0,\ldots,0).
$$
再减去 $r$ 次项。因为 $\tau^\circ$ 的前 $r+1$ 个矩全零，
(4) 第 $n$ 项在 $\phi$ 上的值等于
$$
\beta_p^n\int t^r
 \left[
 \phi^{[r]}(\kappa_p^nt,0,\ldots,0)
 -\phi^{[r]}(0,\ldots,0)
 \right]\,d\tau^\circ(t).
\tag{6}
$$
所有 $\kappa_p^{rn}$ 都准确约去。
式 (6) 的范数至多 $\|\phi\|_{r,p}$，
并因连续性趋于零。
所以完整系列给
$$
\boxed{|\rho_{\ell,r}(\phi)|_p\le\|\phi\|_{r,p}.}
\tag{7}
$$
这是范数常数一、对 $p$ 和来源深度都统一的实际泛函界。
它不是仅说明“存在某个有限 distribution order”。

正幂规整用分布导数。
连续差商有完整整数恒等式
$$
\boxed{
(\phi')^{[j]}(t_0,\ldots,t_j)
=\sum_{i=0}^j
 \phi^{[j+1]}(t_0,\ldots,t_i,t_i,\ldots,t_j).
}
\tag{8}
$$
例如可先对 $(Z-t)^{-1}$ 验证，再比较 $Z^{-1}$ 系数；
重合节点由连续延拓给出。
因此
$\|\phi'\|_{r,p}\le\|\phi\|_{r+1,p}$，
没有隐藏的阶乘分母。

令 $R=2$ 或 $5$、$a=R-r$。
R575 的实际正幂分布是
$(-\partial_t)^a\rho_{\ell,r}$。
由 (7)–(8)，其对 (5) 的 $R$ 阶范数仍至多一。
再乘同一单位 $\Omega_{p,0}^{R}$，得到原坐标 $V_{\ell,r}$ 的准确呈示
$$
\boxed{
\mathcal A_{\mu_{V_{\ell,r}}}(Z)
=V_{\ell,r}(\Omega_{p,0}\log(1+Z)),\quad
|\mu_{V_{\ell,r}}(\phi)|_p\le\|\phi\|_{R,p}.
}
\tag{9}
$$
这里导数作用在真实有限阶分布上，未把它称作有界测度的导数。

## 4. 卷积的完整 lattice-path 证明

下面支付全部乘积所需的统一范数，不能只对单个坐标给 (9)。

对节点 $x_0,\ldots,x_r$、$y_0,\ldots,y_s$，
令 $\mathcal P_{r,s}$ 是从 $(0,0)$ 到 $(r,s)$ 的单调格路。
每步只把一个坐标加一。
对路径 $P=((i_0,j_0),\ldots,(i_{r+s},j_{r+s}))$，有
$$
\boxed{
[x_0,\ldots,x_r]_x[y_0,\ldots,y_s]_y\,\phi(x+y)
=\sum_{P\in\mathcal P_{r,s}}
 \phi^{[r+s]}(x_{i_0}+y_{j_0},\ldots,
              x_{i_{r+s}}+y_{j_{r+s}}).
}
\tag{10}
$$
所有系数为整数一。

为完整证明 (10)，先取 $\phi(t)=(Z-t)^{-1}$。
第一次 $x$ 差商恰为
$\prod_{i=0}^r(Z-x_i-y)^{-1}$。
对这个乘积作 $s$ 阶 $y$ 差商，差商乘积律按
$$
0=j_0\le j_1\le\cdots\le j_{r+1}=s
$$
求和；第 $i$ 因子的差商是
$\prod_{j=j_i}^{j_{i+1}}(Z-x_i-y_j)^{-1}$。
这恰逐一枚举全部格路的节点乘积，也就是右边的 $(r+s)$ 阶差商。
比较形式 Laurent 展开中 $Z^{-m-1}$ 系数即得到所有单项式 $t^m$，
线性组合给所有多项式；重合节点再由连续性得到。
这样没有在卷积时把不同输入的节点误合成一个普通导数。

若 $L_1,L_2$ 分别对 (5) 的 $r,s$ 阶范数有单位界，
(10) 先控制每个混合差商，再逐变量作用两个泛函，给
$$
\boxed{|(L_1*L_2)(\phi)|_p\le\|\phi\|_{r+s,p}.}
\tag{11}
$$
这个结论在多项式上已完整成立，足以评价下文真正的下降阶乘。

所以 (2) 中任意单项式的实际分布范数由其真实总阶控制：
两个 $S,T$ 坐标贡献零；
两个 $V_{4,r}$ 各贡献二；
五个 $V_{1,r}$ 各贡献五。
对所有系数整、总次至多 $D$ 的 $P$，因此得到一个**实际**
$\mu_P$，满足
$$
\mathcal A_{\mu_P}(Z)=P(\mathbf G(\Omega_{p,0}\log(1+Z))),
\qquad
|\mu_P(\phi)|_p\le\|\phi\|_{5D,p}.
\tag{12}
$$
系数整和非 Archimedean 三角不等式保证这里没有单项式个数的额外损失。

## 5. 下降阶乘的所有差商，不只普通导数

令
$$
\mathcal F_n(t)=\prod_{v=0}^{n-1}(t-v).
$$
对 $0\le j\le n$ 使用差商乘积律。
每个非零项选恰好 $j$ 个一次因子作一阶差商，值都是一；
剩余因子被这些位置分成 $j+1$ 个连续整数根段，长度
$$
l_0,\ldots,l_j\ge0,\qquad \sum l_i=n-j.
$$
每一段都在其中一个真实节点 $t_i$ 取值，
是某个平移后的下降阶乘 $\mathcal F_{l_i}(t_i-a_i)$。
故该项的赋值至少
$$
\sum_i v_p(l_i!).
$$

对任意 $q=p^a$，写 $l_i=qk_i+r_i$、$0\le r_i<q$。
由
$$
n-q\sum k_i=j+\sum r_i\le(j+1)q-1
$$
严格得到
$$
\sum_i\left\lfloor\frac{l_i}{p^a}\right\rfloor
\ge\max\left(0,\left\lfloor\frac n{p^a}\right\rfloor-j\right).
$$
逐 $a$ 相加，再对各整数项求和，不会降低这个赋值。
所以对整个节点空间，
$$
\boxed{
v_p\!\left(\mathcal F_n^{[j]}(t_0,\ldots,t_j)\right)
\ge v_p(n!)-\sum_{a\ge1}
 \min\left(j,\left\lfloor\frac n{p^a}\right\rfloor\right).
}
\tag{13}
$$
当 $j>n$ 时差商为零。
定义
$$
\Lambda_p(n,R)=\sum_{a\ge1}
 \min\left(R,\left\lfloor\frac n{p^a}\right\rfloor\right).
$$
由 (13)，有真正的 $C^R$ 范数界
$$
\boxed{\|\mathcal F_n\|_{R,p}
\le p^{-v_p(n!)+\Lambda_p(n,R)}.}
\tag{14}
$$
这就是一般有限阶分布所需的完整替代证明，
没有调用“有限和 measure derivatives”的未付假设。

## 6. 真饱和前缀中的最高阶乘抵消

取 (2) 中系数最大范数至多一、所有前 $k$ 行为零的真实 $P$。
由于全部九坐标属于 $w=z^6$，(12) 的原矩准确为
$$
\mu_P(t^{6h})=\Omega_{p,0}^{6h}(6h)!\,r_h(P),
\qquad
\mu_P(t^m)=0\quad(6\nmid m).
\tag{15}
$$
因此全部低于 $n=6k$ 的矩为零。
这同时保留整个原前缀和所有角型，没有只保几个选出的低行。

又因九坐标全部从 $w$ 起，次数大于 $k$ 的单项式不影响
$r_0,\ldots,r_k$。
直接删去这些列的系数，不改变当前评价及前缀零，也不增系数范数。
故在 (12) 可准确使用
$$
R=5\min(D,k).
$$
同一个 monic $\mathcal F_n$ 于是给
$$
\Omega_{p,0}^{6k}(6k)!\,r_k(P)
=\mu_P(\mathcal F_{6k}).
$$
把 (12)、(14) 代入并约去原最高阶乘和单位周期，得到
$$
\boxed{
\log\|\varphi_D^k\|_p
\le \Lambda_p(6k,5\min(D,k))\log p.
}
\tag{16}
$$
(16) 对全部好普通 $p$、全部 $D,k\ge1$、
以及 (2) 的全部真实饱和层同时成立。

证明实际上覆盖所有 $\mathbf Z_p$ 系数、满足原前缀的多项式。
所以从 $\ker_{\mathbf Q}\cap E_D$ 张到局部饱和格时没有额外指标损失。
未把全函数恒等式代替某个不同的受限 mixed 事件。

## 7. 全部普通位求和和固定坏集

设 $n=6k$、$1\le R\le5k<n$。
对 $a\ge2$，有统一上界
$$
\sum_p\sum_{a\ge2}
 \min(R,\lfloor n/p^a\rfloor)\log p
\le n\sum_p\frac{\log p}{p(p-1)}
=O(n).
$$
对一次素数幂，将范围在 $p=n/R$ 处分开：
$$
\sum_{p\equiv1(6)}\min(R,\lfloor n/p\rfloor)\log p
\le R\,\vartheta(n/R)
+n\sum_{\substack{p\equiv1(6)\\n/R<p\le n}}\frac{\log p}{p}.
$$
第一项为 $O(n)$。
固定模六的 Mertens 公式给第二项为
$(n/2)\log R+O(n)$，包括 $n/R$ 有界的情形。
于是
$$
\boxed{
\sum_{\substack{p\ {\rm good}\\p\equiv1(6)}}
\log\|\varphi_D^k\|_p
\le 3k\log D+O(k).
}
\tag{17}
$$
常数与 $D,k$ 无关。

固定坏位的九个坐标都有同一个正的局部收敛半径。
固定次原函数仅带多项式增长的积分分母，不会把一个正半径降为零。
在较小固定闭盘上逐系数 Cauchy 给坏位成本 $O(k+D)$。
因此允许包括全部固定坏位后，右端是
$$
\boxed{3k\log D+O(k+D).}
\tag{18}
$$
没有删除尚未估计的无限普通素数集合。

## 8. 原 b=17 的同一格运输

R540 的固定同构保持
$\Omega_{p,0}=\theta\Omega_{p,17}$、$\theta^6=17$。
其真实来源式给
$$
U_{\ell,r,17}(z)=\theta^{-(\ell+r)}
 U_{\ell,r,0}(\theta z).
$$
正幂规整后，七者恰有共同权六：
$$
\boxed{V_{\ell,r,17}(z)=\theta^{-6}
 V_{\ell,r,0}(\theta z)
 =17^{-1}V_{\ell,r,0}(17w).}
\tag{19}
$$
把原 $S,T$ 同时运输到该共同 sigma frame，
它们的首 $w$ 归一也有同一个式子。
所以整个九坐标在两 frame 间是
$\mathbf G_{17}(w)=17^{-1}\mathbf G_0(17w)$。

在每个 $p\ne17$，
其单项式变换是对次数 $|\mathbf a|$ 列乘 $17^{-|\mathbf a|}$，
第 $h$ 个评价行再乘 $17^h$。
这些全是单位，因而完整前缀核、饱和格和 (16) 的局部范数完全对应。
$p=17$ 已在固定坏集内。

这不是把任意代数数 $\theta$ 当作 $\mathbf Z_p$ 输入的乘法；
同一普通变量上的测度比较使用原两个单位周期及完整固定同构。

## 9. 已付与仍未付的范围

R575 的复侧及真正九维已经成立；
本篇支付其同一 (2) 上普通侧全部次数、全部乘积、全部饱和前缀的
真实成本 (16)–(18)。
该结论无条件，不要求两个负矩或任何原中央导数为零。

本篇的局部证明不将新的固定原函数当作有界测度。
惰性侧使用
[R574](R574-nine-coordinate-inert-envelope-and-primitive-denominator-cost.md)
已经在同一九坐标和同一前缀上支付的真实界，
不能自动抄用旧 $S,T$ 格的包络。

### 9.1 同一九坐标的严格门

复侧的有限型与完整九维，加上本篇 (18)，使 R159 的同一旗标估计适用。
若在整个 (2) 的全部非零层上，原实际算术条件能够给
$$
\sum_{p\equiv5(6)}\log\|\varphi_D^k\|_p
\le a_I k\log D+b_I k\log k+O(k+D),
\quad a_I,b_I\ge0,
$$
那么 $b_I<3$ 时必有
$$
9\le\frac{a_I+6}{3-b_I}.
$$
所以严格的充分门是
$$
\boxed{a_I+9b_I<21.}
\tag{20}
$$
这已使用真实普通成本三，未将九坐标普通成本写成零。

R574 当前无条件包络是 $(a_I,b_I)=(3,3)$：
其额外三来自固定原函数短分母段的实际全部乘积成本。
它不满足 (20)。
若暂只改善 Gaussian 的 $b_I$ 而仍保 $a_I=3$，
则须得到 $b_I<2$，而非把原积分成本删除。

另一个完全条件性的读法是：
如果将来在同一全部饱和格上证明
$p>C D^\vartheta$ 的惰性 jet 全整，
保留 $p\le C D^\vartheta$ 时，R574 的 Gaussian 项至多
$3\vartheta k\log D+O(k)$，
其 primitive 分母项仍可保完整 $3k\log D+O(k)$。
故可用 $(a_I,b_I)=(3\vartheta+3,0)$，
并在 $\vartheta<6$ 时严格进入 (20)。
这里没有证明该 cutoff 整性；显示的额外 $+3$ 不能省略。

原算术总行到 $I_4/I_1$ 或单位来源的合法比较也仍需另付；
本文没有删去 $u$ 单位补域或其他原 mixed 条件。

## 10. 精确证书

[check-r579-nine-coordinate-divided-difference-budget.mjs](../scripts/check-r579-nine-coordinate-divided-difference-budget.mjs)
用 12,220 项精确整数检查验证完整 lattice-path shuffle、
重合节点的导数恒等式、下降阶乘的全部连续根段乘积式，
以及逐 $p^a$ 的组合估值界。
其中 11,890 项是小整数分段的完整枚举，不是负矩非消失的素数扫描。

所有一般 $D,k,p$ 量词来自正文证明；
证书没有将有限范围检查代替饱和前缀或全部普通位的估计。
