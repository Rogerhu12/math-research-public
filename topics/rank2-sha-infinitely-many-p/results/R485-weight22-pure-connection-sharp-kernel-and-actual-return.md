# R485 — 二十二权纯角导子、准确特征 p 核与原三源返回

日期：2026-11-14。**状态：已证明。** 在 R473 的实际三来源规范化上，原固定 $\Theta$ 的角导子有一个每轮只增 $22$ 权的齐次多项式乘子。这个 $22$ 在“单齐次乘子乘原导子、无另加零阶连接项”的范围内严格最小。

本篇计算全部特征 $p$ 核，给累计来源除常数后的准确饱和门：$N<\lceil136p/11\rceil$。之后按 R473 的固定 conductor 整地返回原三来源，保其固定权与新增 carry；再给同一原 $\Gamma$ 中的完整物理连接及真实左右提升配对。改进的是实际来源操作和返回成本，未将来源饱和称为物理像饱和或直接赋值给 R418 的算术指数。

## 1. 同一真实规范化与原角导子

沿用 R473 的固定整环
$$
R=\mathbf Z[1/(2\cdot3\cdot7\cdot13\cdot17)],\qquad
a=t(t-1)h_7,\quad h_7=16t^2+4t+7,
$$
$$
\mathcal B_m=\Theta^m a^{c_m}R[t]_{\le e_m},\qquad
c_m=\lceil m/68\rceil,\quad f_m=\lfloor11m/34\rfloor,\quad e_m=f_m-4c_m,
$$
$$
\mathcal B_{\le N}=\bigoplus_{m=0}^N\mathcal B_m.
\tag{1}
$$
负次数界表示零空间；$\mathcal B_0=R$。这些显示基是真正原三来源环的规范化基，不能替换为自由角多项式。

令 $\delta=t\partial_t$ **固定 $\Theta$**。这与旧固定 $\mathscr R=\Theta^{17}(1+8t)$ 的导子相差已知径向项；本篇直接保原 $\Theta$ 坐标，不混用二者。

定义
$$
\boxed{W_{22}=\Theta^{22}\frac{a^2}{t}
=\Theta^{22}t(t-1)^2h_7^2\in\mathcal B_{22},}
$$
$$
\boxed{\mathcal Q_{22}=W_{22}\delta
=\Theta^{22}a^2\partial_t.}
\tag{2}
$$
它是次数增加二十二的真正 Leibniz 导子。角多项式为
$$
\frac{a^2}{t}
=49t-42t^2+177t^3-296t^4+240t^5-384t^6+256t^7.
\tag{3}
$$

## 2. 全部六十八个余类的准确闭合

**定理 1。** 对所有 $m\ge0$，
$$
\boxed{\mathcal Q_{22}:\mathcal B_m\longrightarrow\mathcal B_{m+22}}
\tag{4}
$$
是整映射。在显示基上，它准确为
$$
\boxed{
\mathcal Q_{22}(\Theta^m a^{c_m}F)
=\Theta^{m+22}a^{c_m+1}
\bigl(c_ma'F+aF'\bigr).}
\tag{5}
$$

**证明。** 直接求导得到 (5)。令
$\varepsilon_m=c_{m+22}-c_m\in\{0,1\}$，则返回目标基所用的多项式为
$$
a^{1-\varepsilon_m}(c_ma'F+aF').
$$
其次数至多 $\deg F+7-4\varepsilon_m$。
另一方面，
$$
f_{m+22}-f_m\in\{7,8\},\qquad
e_{m+22}-e_m=f_{m+22}-f_m-4\varepsilon_m
\ge7-4\varepsilon_m.
$$
这证明所有来源次数及全部强迫零均保留。
模六十八的准确数据是：$\varepsilon_m=1$ 恰在余类
$0,47,48,\ldots,67$；$f_{m+22}-f_m=8$ 恰在
$3,6,9,12,37,40,43,46$，其余为七。所有余类均已覆盖。$\square$

证明也有逐点读法：$\delta$ 在 $t=0$ 不降低强迫零阶，在 $a$ 的另外三个简单根最多降低一阶；$a^2/t$ 的零阶分别为一、二、二、二，恰支付新权中可能增加的一次 $a$。本篇未在某个根处使用形式单位逆创造来源。

## 3. 纯乘子范围内二十二严格最小

**定理 2。** 设非零齐次 $W=\Theta^cB(t)\in\mathcal B_c$，且
$W\delta(\mathcal B_m)\subset\mathcal B_{m+c}$ 对每个 $m$ 成立。
则 $c\ge22$。这个结论在特征零及本篇允许的好特征均成立。

**证明。** $c=0$ 时 $B$ 为常数；取实际 $\Theta^{13}a\in\mathcal B_{13}$ 输入，$t a'$ 在三个非零 $a$ 根不消失，故不能保持所需 $a$ 因子。

若 $1\le c\le21$，取 $m=69-c$。此时
$48\le m\le68$、$c_m=1$、$c_{m+c}=2$，且 $\Theta^ma$ 是原 (1) 中的实际列。
闭合要求
$$
a^2\mid B(t)\,t a'(t).
$$
$a$ 的四根简单，只有其中 $t=0$ 被额外的 $t$ 抵消一次，所以
$$
\frac{a^2}{t}\mid B(t),\qquad\deg B\ge7.
$$
但 $W\in\mathcal B_c$ 又要求 $\deg B\le f_c\le6$，矛盾。
定理 1 已达到 $c=22$。$\square$

最小性只针对这里明定的纯乘子原导子。若另加按权分段的零阶角连接，则是不同算子，必须支付它自己的物理项和核，不能把本定理扩张到该情形。

## 4. 每个权的完整特征 p 核

取允许的剩余域 $k$，特征为 $p>83$。令
$$
\kappa_m=p\left\lceil\frac{c_m}{p}\right\rceil.
$$
因为 $W_{22}$ 在原抽象整环约化中非零，$\ker\bar{\mathcal Q}_{22}=\ker\bar\delta$。

**定理 3。** 每个权的准确核是
$$
\boxed{
\ker(\bar{\mathcal Q}_{22}|_{\mathcal B_m/p})
=\Theta^m a^{\kappa_m}
\left\{H(t^p):\ p\deg H+4\kappa_m\le f_m\right\}.}
\tag{6}
$$
其维数为
$$
\boxed{d_m(p)=
\max\left\{0,1+\left\lfloor\frac{f_m-4\kappa_m}{p}\right\rfloor\right\}.}
\tag{7}
$$
不同权在抽象实际来源环中仍独立，所以整个累计核是这些空间的直接和。

**证明。** 写来源角系数 $q(t)=a^{c_m}F(t)$。
$\delta q=0$ 当且仅当 $q\in k[t^p]$，由逐项求导直接得到。
在 $a$ 的每个几何根上，$q$ 的零阶被 $p$ 整除，又至少为 $c_m$，所以至少为 $\kappa_m$。
$a$ 平方自由，故 $a^{\kappa_m}\mid q$；商仍为多项式且导数为零，所以属于 $k[t^p]$。
反向显然成立。最后保完整角次数 $\deg q\le f_m$，得到 (6)–(7)。
这里没有把独立 $\Theta$ 指数在物理评价后产生的关系赋给抽象来源。$\square$

## 5. 累计来源的准确饱和门

特征零中 $\delta$ 的核只有 $1$：对 $m>0$，角系数被 $a$ 整除，不能是非零常数。

**定理 4。** 对整个累计来源，
$$
\boxed{
\mathcal B_{\le N}/\langle1\rangle
\xrightarrow{\mathcal Q_{22}}\mathcal B_{\le N+22}
\text{ 是像为 }p\text{-饱和的整单射}
\iff N<\left\lceil\frac{136p}{11}\right\rceil.}
\tag{8}
$$
等价地，$f_N<4p$。一般 $N$ 下，非零 Smith 因子中被 $p$ 整除的数目准确为
$$
\sum_{m=0}^N d_m(p)-1.
\tag{9}
$$
(9) 不指定更高的 Smith 赋值。

**证明。** 当 $f_N<4p$ 时，每个 $m>0$ 的 $\kappa_m\ge p$，故 (6) 没有非零元素；$m=0$ 恰给常数。
源、目标均有 (1) 的有限自由整基，模 $p$ 秩与特征零秩相同，故像饱和。

令 $m_0=\lceil136p/11\rceil$。有 $f_{m_0}=4p$ 且 $c_{m_0}\le p$，所以
$$
\Theta^{m_0}a^p\in\mathcal B_{m_0}/p
$$
是真正非零核元素。它已经在最早可能的权出现，故反向及准确门成立。一般情形由模 $p$ 核维数与 Smith 形给 (9)。$\square$

例如 $p=101$ 的第一个新核权恰为 $1249$，其
$f_{1249}=404,c_{1249}=19,e_{1249}=328$；实际核是
$\Theta^{1249}a^{101}=\Theta^{1249}a^{19}\cdot a^{82}$。
这是准确来源边界，不是主课题的素数证据。

迭代 $j\ge1$ 次时，充分条件
$$
\boxed{f_{N+22(j-1)}<4p}
\tag{10}
$$
保证 $\mathcal Q_{22}^j$ 在除去 $1$ 后仍为 $p$-饱和单射，目标权至多 $N+22j$。
因为第一次后的来源全在正权，而每一步在 (10) 中对正权均模 $p$ 单射，逐步复合即可。这里保每轮二十二权成本，不把迭代当免费列。

## 6. 固定 conductor 后回到原三个来源

R473 已付
$$
\mathcal A=R[S,T,U],\qquad
\mathfrak c=\Phi_Z(S,U;T)\in\mathcal A_{10980},\qquad
\mathfrak c\mathcal B_m\subset\mathcal A_{m+10980}.
$$
这些返回在同一固定整环上成立，且 $\mathfrak c\mathcal B$ 是原 $\mathcal A$ 中的 $p$-饱和子模。
因此在实际来源子格 $\mathfrak c\mathcal B_{\le N}$ 上定义
$$
\boxed{\mathcal Q_{22}^{\mathfrak c}(\mathfrak c b)
=\mathfrak c\mathcal Q_{22}(b).}
\tag{11}
$$
式 (11) 在显示的整基上定义，不是在原来源环中自由除 $\mathfrak c$。
它按每轮二十二权返回原三生成元，核为 $R\mathfrak c$；(8) 的准确饱和门和 (10) 的迭代充分门原样成立。其目标是实际
$\mathfrak c\mathcal B_{\le N+22j}\subset\mathcal A_{\le N+22j+10980}$。

作为形式连接可写成
$\mathfrak c W_{22}\delta(\mathfrak c^{-1}P)$，但这里的反因子只解释已经限定于该真实子格的 (11)，不增加任何算术观察。

预算也完整保留。每轮在 canonical 多项式基上，由 (5) 得系数范数至多乘 $C(m+1)$；迭代 $j$ 次至多
$$
C^j(N+22j+1)^j.
$$
再经 R473 的固定返回，原三生成元的通常总次数至多
$$
\left\lfloor\frac{N+22j+10980}{17}\right\rfloor,
$$
系数对数范数成本至多
$j\log(N+j+1)+O(N+j)$。
这些成本及固定偏移都计入 R418 的 Cauchy 优化，不能只看每轮的主权增量。

## 7. 原惰性目标中的 carrier 与全部新增 carry

本节仅在原已付的整 $\Gamma$ 窗口工作；不把 raw 惰性 Taylor 级数在所有次数称为整。为与角多项式 $a(t)$ 区分，将原 Gaussian 单位记为 $\alpha=p\kappa$（即 R481 中的 $a$）。写
$$
X=\vartheta_{\rm reg}(w)e^{\alpha\epsilon/17},\qquad
\vartheta_{\rm reg}=(g/d)^{1/17},\qquad d=1+8t,
$$
$$
\mathsf D=w\partial_w+s\epsilon\partial_\epsilon,\qquad
\nu=(\mathsf D\log t)^{-1},\qquad
\mathsf B=\mathsf D\log\vartheta_{\rm reg}+\frac{s\alpha}{17}\epsilon.
\tag{12}
$$
原 $t/w$、$\vartheta_{\rm reg}$ 在所需窗口均整且为单位，故 $\nu$ 为整单位；$\mathsf D$ 保持 $w^s-p\epsilon$ 及全部截断理想。

把 R473 的实际 conductor 写为
$$
\mathfrak c=\Theta^{10980}q_{\mathfrak c}(t),\qquad
r_{\mathfrak c}=\operatorname{ord}_0q_{\mathfrak c},\qquad
162\le r_{\mathfrak c}\le3552.
$$
另删其固定首项分子、分母的素因子后，regularized 的 $\mathfrak c$ 在原窗口准确是
$w^{r_{\mathfrak c}}$ 乘整单位。与整个原 $G_0$ 相乘，令
$$
R_*=13+r_{\mathfrak c},\qquad175\le R_*\le3565.
$$
固定 carrier 的形式是
$$
\boxed{C_{\rm phys}=w^{R_*}U_c(w)
\exp\left(\left(40+\frac{10980}{17}\right)\alpha\epsilon\right),}
\tag{13}
$$
其中 $U_c$ 为包含原 $P_{134}/U_0$ 的完整整单位。

当 $R_*<s$ 且 $\ell+R_*<s$ 时，原限制到 $\mathfrak c\mathcal B$ 的评价必须保
$m_{R_*}$：其有 $R_*$ 个初始自由行和两条各 $R_*$ 行的 $p$ carry。
原来的十三行完整包含其中，另有每带 $r_{\mathfrak c}$ 条固定成本；不能为使用规范化而删掉这些新增行。
这是固定偏移，不随来源预算增长，但其实际整运输必须保留。

## 8. 真物理连接及同一左右提升配对

令
$$
W_{\rm phys}=X^{22}\frac{a(t)^2}{t},\qquad
\mathcal Z_{22}=\nu W_{\rm phys}\mathsf B,
$$
$$
\mathsf C=\mathsf D\log C_{\rm phys}
=R_*+\mathsf D\log U_c+
\left(40+\frac{10980}{17}\right)s\alpha\epsilon.
\tag{14}
$$
这里 $W_{\rm phys}=-49w\cdot\text{整单位}$，故乘 $\nu W_{\rm phys}$ 真正增加一条物理行。所有 Gaussian charge 保留；$\mathsf B$ 的 $s\alpha\epsilon/17$ 项尤其不能删去。

设 $M_-^{\mathfrak c}$ 是来源 $\mathcal B_{\le N}$ 经 $C_{\rm phys}$ 后的实际评价，$M_+^{\mathfrak c}$ 使用来源 $\mathcal B_{\le N+22}$ 及多一条物理目标行。保 $\ell+R_*+1\le s$。令 $E_\Theta=\Theta\partial_\Theta$。

**定理 5。** 整个原有限目标中准确有
$$
\boxed{
M_+^{\mathfrak c}(\mathcal Q_{22}P)
=\nu W_{\rm phys}(\mathsf D-\mathsf C)M_-^{\mathfrak c}(P)
-\mathcal Z_{22}M_-^{\mathfrak c}(E_\Theta P).}
\tag{15}
$$

**证明。** 在同一物理代入上使用链式法则：
$$
\mathsf D(P_{\rm phys})
=\nu^{-1}(\delta P)_{\rm phys}+\mathsf B(E_\Theta P)_{\rm phys}.
$$
先乘 $W_{\rm phys}$，再乘整个 $C_{\rm phys}$，并把其对数导数留在左侧，得到 (15)。由于 $\nu W_{\rm phys}$ 从 $w$ 起，读取多出的目标行只需输入旧目标内已经存在的系数；没有丢失末行。
$\mathsf C$ 保留了原载体和 conductor 的全部普通、Gaussian 及固定零阶项。$\square$

若 $P_2$ 是同一个原 $M_-^{\mathfrak c}$ 的真实模 $p^2$ 右核提升，$\lambda_2$ 是整个 $M_+^{\mathfrak c}$ 的真实模 $p^2$ 左核提升，则 (15) 给
$$
\boxed{\langle\lambda_2,
\mathcal Z_{22}M_-^{\mathfrak c}(E_\Theta P_2)\rangle
=0\pmod{p^2}.}
\tag{16}
$$
所有来源和目标预算都已在 (11)、(13)–(15) 支付。
并未要求 $E_\Theta P_2$ 自身保持右核，也未将这个实际接触对扩成两个环境空间的直和。

在 (8) 的饱和范围，$\mathcal Q_{22}$ 对真正非零右首核方向不会退成零来源：其仅有的常数核在 (13) 的 $w^{R_*}$ 行有单位首项，而所有正权列至少多一个 $w$，所以原首核的常数系数必须为零。
这保留了配对中的实际来源方向，但不证明左核非零或 (16) 强迫某个可见余核类非零。

## 9. 与完整三中央及全局预算的关系

本篇将旧固定 $\mathscr R$ 连接的两径向权成本，换成当前三源规范化上准确的二十二个 $\Theta$ 权；返回原多项式时每轮主增量按 (11) 保留，并加固定 conductor 成本。
它没有取消 (15) 中的 $\mathcal Z_{22}M(E_\Theta P_2)$，没有从来源饱和推出实际 $M$ 的像饱和，也没有把 $J'_S=J'_T=J'_U=0$ 传播给规范化列或 conductor 乘积。

因此 R481 的同一修正及 $d_2^J\to G_2$ 条件仍须在完整原目标中计算；若使用本篇的来源，先保 (13) 的全部固定新增 carry。R418 的严格门仍须由真实算术评价改善证明，不能把 $22/17$ 的来源次数增量直接命名为其惰性指数。

固定多项式、全部六十八个余类及一个准确饱和边界的证书为
[check-r485-weight22-normalized-connection.py](../scripts/check-r485-weight22-normalized-connection.py)。
所有全参数断言由 (4)–(16) 的证明给出；无目标素数扫描，也无新增中央零。
