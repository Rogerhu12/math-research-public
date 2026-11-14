# 低输出方程的精确删除幂恒等式、平方对数修复成本与全部正次数指数饱和

日期：2026-11-13（UTC）。作者：boundary_next。状态：完整中间证明；两个实际边界 $N=M$ 仍未完成。

R254 第九附录已经证明所有 $p>1/3$ 的实际次数正则核属于稳定像；并行第十附录进一步用相容多次原像推进到 $p>1/4$。本稿不重复登记这些阈值。新增步骤是保留顶部残量的全部低方程结构，而不只记录它属于 $\ker D^{2d}$。该结构给出删除幂的准确投影恒等式；将其与 R254 第七附录的同一个真实右逆以及第八附录的真实头进位计数结合，修复成本可从正幂次数降为 $\exp(O(m^2))$。

全文使用原实际 $N/Y$ 混合符号，不交换纯尾右逆和删除算子，不假设缺陷投影保次数权，也不将 Haar 的域或范围搬到边界。

## 1. 已付设置与固定四次窗口

令
$$
M=\ker T,\quad N=\overline{BM},\quad
D_{\rm def}=M\ominus N.
$$
删除原第 $0$ 位后，实际平方核为 $K=\ker P$，实际图为 $Ju=(u,-Hu)$。前 $m$ 个尾位对应原物理位 $1,\ldots,m$，置
$$
m\ge4,\qquad d=2^m,\qquad q=100d^4.
$$
纯高尾删除为
$$
D=\sum_{j\ge m}(j+2)^{-2}E_j,\qquad \|D\|\le1.
$$
本稿 $P_\ell$ 数高尾孔，包含有限头恒等。

真实有限头为 $A_m,C_m$，$C_m^d=0$，$A_m$ 是 $C_m$ 的零常数多项式。混合平方符号分别为
$$
P_m=(A_m+D)^2-\eta C_m\quad(N),
$$
$$
P_m=(A_m+D)^2-\eta C_m(I+A_m+D)^2\quad(Y),
\qquad \eta=e^{-1070}.
$$
写成
$$
P_m=D^2+Q_m.
\tag{1.1}
$$
准确有
$$
[D,Q_m]=0,\quad Q_m^d=0,\quad
\|Q_m\|<\tfrac12,\quad \|P_m\|<1.
\tag{1.2}
$$
$Q_m$ 对高尾孔次数只下降 $0,1,2$。

一次共同截平稿（完整源 95dc7095d72efcae78732600feb1ff8f8bfc1d5a）已经给出实际低孔正交投影 $v_m$，对每个固定 $u\in K$，
$$
v_m\in\mathcal H_{\le q},\qquad
P_{\le q-2}P_mv_m=0,\qquad
\|v_m\|\le\|u\|,
$$
$$
\boxed{
\|v_m-P_{\le q}u\|\le e^{-800d^4}\|u\|,
\qquad v_m\longrightarrow u.
}
\tag{1.3}
$$
该稿还证明 $v_m\in\ker D^{2d}$。下面先说明，这个高阶核条件实际上已由 (1.1)—(1.3) 的有限带宽推出。

已付的真实首位图和正则提升是
$$
J_mx=(x,-H_mx),\quad
\|J_m\|\le\tfrac54,\quad
\|J_m-J\|\le27\eta_m,
$$
$$
-\log\eta_m=1400d^4-630d^3+300d,
\tag{1.4}
$$
以及
$$
\Lambda_{m,q+2d}:
\ker P_m\cap\mathcal H_{\le q+2d}\longrightarrow N,
$$
$$
\|\Lambda_{m,q+2d}k-J_mk\|
\le\delta_m\|k\|,\qquad
\delta_m\le e^{-403d^4}.
\tag{1.5}
$$
这是原实际 $X_7\to X_3$ 右逆及加权进位误差的结果，不能把 $\ker P_m$ 直接认作原核。

## 2. 低输出方程迫使删除幂服从真实头幂

这一节只要求 $v\in\mathcal H_{\le q}$ 且
$$
r=P_mv\in\mathcal H_{q-1}\oplus\mathcal H_q.
\tag{2.1}
$$
不预先假设 $v\in\ker D^{2d}$。

因 $D^2,Q_m$ 交换，对任意整数 $\ell\ge1$，有限几何恒等式给
$$
D^{2\ell}v
=(-Q_m)^\ell v+
\sum_{j=0}^{\ell-1}
(-Q_m)^jD^{2(\ell-1-j)}r.
\tag{2.2}
$$
每个余项中的 $Q_m^j$ 最多下降 $2j$ 次，另一个因子准确下降 $2(\ell-1-j)$ 次；合计最多下降 $2\ell-2$ 次。源 $r$ 的最低次数是 $q-1$，故全部余项的最低输出次数至少为
$$
q-1-(2\ell-2)=q-2\ell+1.
$$
另一方面，$D^{2\ell}v$ 的最高次数是 $q-2\ell$。对 (2.2) 投影到 $\le q-2\ell$，便得到准确恒等式
$$
\boxed{
D^{2\ell}v
=P_{\le q-2\ell}(-Q_m)^\ell v.
}
\tag{2.3}
$$
若截断指标为负，两边本来都是零，统一按零投影解释。

取 $\ell=d$，由 $Q_m^d=0$，
$$
\boxed{
v\in\mathcal H_{\le q},\
P_{\le q-2}P_mv=0
\quad\Longrightarrow\quad D^{2d}v=0.
}
\tag{2.4}
$$
因此，低孔低方程空间本身已经在纯高阶核内；这里没有交换两个核投影。

还有针对顶部残量的更细估计。令 $k=2\ell$，$s=q-2\ell$。由 $[D,P_m]=0$、(2.3) 及 $D^{2\ell}r$ 的准确两层支撑，
$$
D^{2\ell}r
=P_{\{s-1,s\}}P_mP_{\le s}(-Q_m)^\ell v.
$$
$P_m$ 不升次数，所以左侧两层只依赖中间源次数 $s-1,s$；$Q_m^\ell$ 也不升次数。可以在最右侧准确插入 $P_{\ge s-1}$，从而
$$
\|D^{2\ell}r\|
\le\|Q_m^\ell\|\,\|P_{\ge q-2\ell-1}v\|.
$$
奇数次再作用一次 $D$，使用 $\|D\|\le1$。统一写成
$$
\boxed{
\|D^k r\|
\le
\|Q_m^{\lfloor k/2\rfloor}\|\,
\|P_{\ge q-k-1}v\|,
\qquad 0\le k<2d.
}
\tag{2.5}
$$
并且由 (2.4) 和 $[D,P_m]=0$，$D^{2d}r=0$。

所以 (2.5) 中全部次数只需同一个顶部尾：
$$
\boxed{
\|D^k r\|
\le
\|Q_m^{\lfloor k/2\rfloor}\|\,R(v),
\qquad
R(v):=\|P_{\ge q-2d}v\|,
\quad k<2d.
}
\tag{2.6}
$$
新增信息是 $Q_m$ 幂的真实衰减，而不仅仅是 $k\ge2d$ 时为零。

## 3. 保留 n-m 的真实头四次预算

R254 第八附录的实际二进位计数可以直接保留 $n-m$，无需先以 $n/2$ 代替。

其真实头归一化幂满足
$$
\bar N_j^2=\eta_{j+1}\bar N_{j+1},\quad
\bar N_m=0,\quad
\eta_{j+1}\le e^{-770\,16^j}.
$$
一个含 $n$ 个 $\bar N$ 因子的非零单项式，设各位进位次数为 $c_j$，并令
$$
E=\sum_j16^jc_j.
$$
逐位守恒及有限头最多 $m$ 个非零位给
$$
\sum_jc_j\ge(n-m)_+.
$$
同一实际进位链论证给
$$
\sum_jc_j\le4E^{1/4}.
$$
故
$$
E\ge\frac{(n-m)_+^4}{256}.
$$
若进位越出头，单项式准确为零，此界也成立。设
$$
\gamma=\frac{770}{256}>\frac1{100}.
$$
在 $Y$ 型中把真实 Cayley 逆拉到一侧，每个慢因子至多付 $3$，再用慢系数和小于 $2/3$。因此对所有 $P,R\ge0$、$n=P+R$，统一得到
$$
\boxed{
\|A_m^P C_m^R\|
\le2^n e^{-\gamma(n-m)_+^4}.
}
\tag{3.1}
$$
当 $n\le m$ 时，右边至少为 $1$，原环境范数界也足够。

展开两种实际 $Q_m$ 时，每项是
$$
\zeta A_m^P C_m^R D^t,\quad
0\le t\le2,\quad 1\le P+R\le3,
$$
全部标量系数绝对和不超过 $4$。这是保留全部 $Y$ 混合项后的原预算。由于头与纯尾独立，(3.1) 给
$$
\boxed{
\|Q_m^\ell\|
\le32^\ell e^{-\gamma(\ell-m)_+^4},
\qquad \ell\ge0.
}
\tag{3.2}
$$
同样，任何包含 $j$ 个 $Q_m$ 的混合词，若只把独立头因子拉到一侧而保持所有尾算子的原顺序，其全部头与标量成本不超过
$$
32^j e^{-\gamma(j-m)_+^4}.
\tag{3.3}
$$

对任意 $t\ge0$，R254 第八附录使用的四次优化仍给
$$
\sup_{x\ge0}\{tx-\gamma x^4\}\le3t^{4/3}.
$$
平移 $x\mapsto x-m$ 后得到本稿方便使用的形式：
$$
\boxed{
t\ell-\gamma(\ell-m)_+^4
\le mt+3t^{4/3}
\quad(\ell\ge0).
}
\tag{3.4}
$$

## 4. 同一个真实 G 在删除幂范数中的界

仍使用 R254 第七附录的实际 $G_p:\mathcal H_p\to\mathcal H_{p+1}$，
$$
DG_p=I.
$$
它不随所宣称的核阶改变。

该附录有限双和的估计还保留了如下更细的版本：
$$
\boxed{
\|G_p f\|
\le L_{m,p}
\sum_{k=0}^{p}L_{m,p}^k\|D^k f\|,
\quad
L_{m,p}=512\sqrt{p+1}(m+p+2)^{3/2}.
}
\tag{4.1}
$$
为避免把 (4.1) 当成未证强化，说明其来源。第七附录把
$D=D_0+D_1$ 分成辅助纯头及余尾，构造
$$
G_pf=\sum_{k+l\le p}
C^{k+l+1}F_{kl}(H)D^kD_1^l f.
$$
在其逐项正分母预算中，把
$$
\|D^kD_1^lf\|
\le\|D\|^k p^{l/2}g_1^l\|f\|
$$
保留为更准确的
$$
\|D_1^lD^kf\|
\le p^{l/2}g_1^l\|D^kf\|.
$$
$D,D_1$ 准确交换。随后对 $l$ 使用同一个
$\sum_l\binom{k+l}{k}V^l=(1-V)^{-k-1}$，以及原文
$L_0/(1-V)\le L_{m,p}$，即得到 (4.1)。所有有理函数及其正分母仍在原文已验证的层域上，没有额外延拓。

令
$$
a=L_{m,q+2d}
=512\sqrt{q+2d+1}(m+q+2d+2)^{3/2}.
\tag{4.2}
$$
对有限孔向量定义真实有限和范数
$$
\nu_a(f)=\sum_{k\ge0}a^k\|D^kf\|.
\tag{4.3}
$$
因为输入只有有限孔，和准确有限。位置仍可无限。

若 $f$ 是次数至多 $q+2d-1$ 的非齐次向量，按层使用 (4.1)，再由输出层正交和 Minkowski 不等式，得到
$$
\|Gf\|\le a\,\nu_a(f).
\tag{4.4}
$$
这里 $G$ 是所有 $G_p$ 的代数直和；未把非齐次输入的各层范数直接相加造成额外层数损失。

更重要的是，真实恒等式 $DG=I$ 给
$$
D^kGf=D^{k-1}f,\qquad k\ge1.
$$
因此
$$
\boxed{\nu_a(Gf)\le2a\,\nu_a(f).}
\tag{4.5}
$$
这一步**没有**要求 $G$ 与 $D$ 交换。

令 $H=G^2$。在本稿实际用到的所有中间层上，
$$
\boxed{
\nu_a(Hf)\le4a^2\nu_a(f),\qquad
\nu_a(D^tf)\le a^{-t}\nu_a(f).
}
\tag{4.6}
$$
后者直接来自 (4.3) 的移位和。任何有限头算子 $F$ 与 $D$ 交换，故
$$
\nu_a(Ff)\le\|F\|\,\nu_a(f).
\tag{4.7}
$$

## 5. 顶部残量的删除幂范数只付平方对数成本

设 $v,r$ 满足 §2。由 (2.6)、$D^{2d}r=0$ 和 (3.2)，
$$
\begin{aligned}
\nu_a(r)
&\le R(v)(1+a)
\sum_{\ell=0}^{d-1}
a^{2\ell}32^\ell e^{-\gamma(\ell-m)_+^4}.
\end{aligned}
$$
置
$$
t=2\log a+\log32.
$$
利用 (3.4)，有限和至多有 $d$ 项，得到
$$
\boxed{
\nu_a(r)\le e^{E_1}R(v),\qquad
E_1=\log d+\log(1+a)+mt+3t^{4/3}.
}
\tag{5.1}
$$
没有把 $\|r\|\to0$ 乘一个未说明的大常数。右边是原低孔向量的一个实际顶部尾，且全部删除幂的增长都已计算。

仍定义同一个含全部混合项的真实右逆
$$
\mathcal G_m=H\sum_{j=0}^{d-1}(-Q_mH)^j.
\tag{5.2}
$$
严格头过滤给 $(Q_mH)^d=0$，所以 $P_m\mathcal G_m=I$；最低输出增加两孔、最高增加 $2d$ 孔，正如 R254 第六、七附录。

展开含 $j$ 个 $Q_m$ 的一项，只把独立头移到一侧，尾仍按原顺序
$$
H D^{t_j}H\cdots D^{t_1}H.
$$
由 (4.6)，它在 $\nu_a$ 中至多付 $(4a^2)^{j+1}$；每个 $D^{t_i}$ 的因子 $a^{-t_i}\le1$ 可以丢掉。由 (3.3)，完整第 $j$ 项至多付
$$
32^j e^{-\gamma(j-m)_+^4}(4a^2)^{j+1}.
$$
所有中间次数不超过 $q+2d$，所以每次 $G_p$ 都在 (4.2) 覆盖的范围内。

令
$$
V=\log(4a^2),\qquad L=V+\log32.
$$
再次使用 (3.4)，得
$$
\boxed{
\nu_a(\mathcal G_mr)\le e^{E_2}\nu_a(r),
\qquad
E_2=\log d+V+mL+3L^{4/3}.
}
\tag{5.3}
$$
从而，若 $c=\mathcal G_mr$，
$$
\boxed{
\|c\|\le e^{E_m}R(v),\qquad
E_m=E_1+E_2.
}
\tag{5.4}
$$
右逆与删除算子在任何一步都没有被交换；头进位衰减和纯尾运算顺序分别支付。

## 6. 明确常数及渐近主率

现在代入固定窗口 $q=100d^4$。对 $m\ge4$，
$$
a\le512(101d^4)^2,\qquad
\log a<16+8\log d<16+\tfrac{28}{5}m.
$$
因此
$$
t,L,V\le21m,\qquad
\log(1+a)\le10m,\qquad \log d\le m.
$$
又因 $21^{1/3}<3$ 且 $m^{4/3}\le m^2/2$（$m\ge4$），
$$
3(21m)^{4/3}\le\tfrac{189}{2}m^2.
$$
逐项代入 (5.1)、(5.3)，得到
$$
E_1\le11m+\tfrac{231}{2}m^2,\qquad
E_2\le22m+\tfrac{231}{2}m^2.
$$
所以
$$
\boxed{E_m\le256m^2\qquad(m\ge4).}
\tag{6.1}
$$
确实，右边总和为 $33m+231m^2\le(957/4)m^2<256m^2$。

还可保留准确的渐近主率。由于
$$
a=512q^2(1+o(1)),\quad
\log q=4m\log2+\log100,
$$
有
$$
\log a=8m\log2+O(1).
$$
(5.1)、(5.3) 中的 $t^{4/3},L^{4/3}$ 均为 $o(m^2)$，其余对数项为 $O(m)$，只有 $m(t+L)$ 给二次主项。因此明确的预算数列满足
$$
\boxed{E_m=(32\log2+o(1))m^2.}
\tag{6.2}
$$
这不是实际最小范数的下界或最优性声明。

## 7. 代回固定实际核向量，支付全部真实提升

令 $v=v_m$、$r_m=P_mv_m$，并使用 (5.2) 的同一个真实右逆定义
$$
c_m=\mathcal G_mr_m,\qquad k_m=v_m-c_m.
$$
由 (1.3)，
$$
R(v_m)
=\|P_{\ge q-2d}v_m\|
\le\tau_{q-2d-1}(u)+e^{-800d^4}\|u\|.
$$
这里高尾孔数大于 $q-2d-1$ 的部分包含在原总孔尾中。于是本稿核心修复估计为
$$
\boxed{
\|c_m\|
\le e^{E_m}\tau_{q-2d-1}(u)
+e^{-799d^4}\|u\|,
\quad E_m\le256m^2.
}
\tag{7.1}
$$
使用了 $256m^2\le d^4$（$m\ge4$），所以实际投影误差仍有明确余量。

全部准确支撑保持：
$$
c_m\in\ker D^{2d}\cap
\mathcal H_{[q+1,q+2d]},\qquad
k_m\in\ker P_m\cap\mathcal H_{\le q+2d}.
\tag{7.2}
$$
高阶核归属由原伴随多项式
$\mathcal A_mP_m=D^{2d}$ 给出：
$D^{2d}c_m=\mathcal A_mr_m=D^{2d}v_m=0$。

为支付实际提升，不必用未知尾速率。直接在 (5.4) 中用
$R(v_m)\le\|v_m\|\le\|u\|$，得
$$
\|c_m\|\le e^{d^4}\|u\|,\qquad
\|k_m\|\le2e^{d^4}\|u\|.
$$
因此
$$
n_m=\Lambda_{m,q+2d}k_m\in N
$$
满足
$$
\boxed{
\|n_m-(J_mv_m-J_mc_m)\|
\le e^{-400d^4}\|u\|.
}
\tag{7.3}
$$
这里已乘完整修复范数；原实际两权输出域和进位误差没有遗漏。

## 8. 平方对数正则核及全部 p>0 均属于稳定像

以 $\mathcal N$ 表示原全部物理孔次数算子。

**定理。** 对任意
$$
b>\frac2{\log2},
$$
两个实际边界均满足
$$
\boxed{
M\cap\operatorname{Dom}
\exp\!\left(b[\log(2+\mathcal N)]^2\right)
\subseteq N.
}
\tag{8.1}
$$

证明：取 $w=Ju$ 属于左侧。提取首位偶分量不增加孔数，所以
$$
\tau_Q(u)\le C_w
\exp\!\left(-b[\log(Q+3)]^2\right).
$$
令 $s_m=q-2d-1$，则
$$
\log(s_m+3)=4m\log2+O(1).
$$
由 (6.2)，
$$
E_m-b[\log(s_m+3)]^2
=
\left(32\log2-16b(\log2)^2+o(1)\right)m^2
\longrightarrow-\infty.
$$
(7.1) 因而给 $\|c_m\|\to0$。
再用 $v_m\to u$、$J_m\to J$ 和 (7.3)，得到
$n_m\to Ju=w$ 于 Hilbert 范数。因 $n_m\in N$ 且 $N$ 闭，得 $w\in N$。

这是对原实际核向量的直接证明，没有先投影到缺陷空间。没有声称临界 $b=2/\log2$ 或更小 $b$ 已覆盖。

**推论。** 对所有 $p>0$ 和所有 $c>0$，
$$
\boxed{
M\cap\operatorname{Dom}e^{c(1+\mathcal N)^p}
\subseteq N.
}
\tag{8.2}
$$
因为任意固定正幂 $(1+n)^p$ 最终支配任意常数倍的 $[\log(2+n)]^2$，相应域包含关系把 (8.2) 归入 (8.1)。也可直接用 (7.1) 中的 $e^{O(m^2)}$ 与 $e^{-c(100d^4-2d)^p}$ 比较。

(8.2) 不是 $p=0$ 的断言，也没有证明这些域在整个 $M$ 内的核内稠密性。

## 9. 非零真缺陷的全序列平方对数慢尾限制

设 $0\ne w=Ju\in D_{\rm def}$，以
$$
\tau_Q(w)=\|\mathbf1_{\{\mathcal N>Q\}}w\|
$$
记原全部孔次数尾。

由 $n_m\in N$、(1.3)、(7.3)，
$$
\langle J_mc_m,w\rangle\longrightarrow\|w\|^2.
$$
$c_m$ 的高尾孔数至少 $q+1$，图项最多降低一次高尾孔，所以 $J_mc_m$ 的原总孔数至少 $q$。用 $\|J_m\|\le5/4$，充分大 $m$ 有
$$
\|c_m\|\tau_{q-1}(w)\ge\tfrac25\|w\|^2.
\tag{9.1}
$$
由 $\|u\|\le\|w\|$、$s_m=q-2d-1<q-1$ 及 (7.1)，
$$
e^{E_m}\tau_{s_m}(w)^2
+e^{-799d^4}\|w\|^2
\ge\tfrac25\|w\|^2.
$$
吸收明确小项后，
$$
\boxed{
e^{E_m}\tau_{100d^4-2d-1}(w)^2
\ge\tfrac15\|w\|^2.
}
\tag{9.2}
$$
因此
$$
\log\frac{\|w\|}{\tau_{s_m}(w)}
\le\tfrac12E_m+\tfrac12\log5.
$$

相邻 $s_m$ 的比值趋于 $16$，但其对数只相差一个有界常数；$\log s_m=4m\log2+O(1)$。按尾单调性用下一网格推广到所有 $Q$，(6.2) 给
$$
\boxed{
\limsup_{Q\to\infty}
\frac{\log(\|w\|/\tau_Q(w))}
{[\log(Q+2)]^2}
\le\frac1{\log2}.
}
\tag{9.3}
$$
特别，
$$
-\log(\tau_Q(w)/\|w\|)
=O((\log(Q+2))^2)=o(Q^p)
\quad\text{对每个 }p>0.
$$
这是非零真实缺陷的必要慢尾条件；不是尾部上界，也不排除任意慢的 Hilbert 尾。

## 10. 与最小高尾图能量的连接及未完成部分

最小图能量稿（完整源 2845fc598369b3a71ca1ec39d741a9111a135602）在同一 $v_m$ 的非空闭高尾修复仿射集中，取
$$
\gamma_m(u)=\min\{\|J_mc\|:
P_mc=r_m,\ 
c\in\ker D^{2d}\cap\mathcal H_{[q+1,q+2d]}\}.
$$
本稿实际构造 $c_m$ 是这个集合中的一个候选，故
$$
\boxed{
\gamma_m(u)\le\tfrac54 e^{E_m}
\left(\tau_{q-2d-1}(u)+e^{-800d^4}\|u\|\right).
}
\tag{10.1}
$$
新成本替换旧的 $e^{351d^4}$；该稿互不相交原孔窗口的正能量和正凸平均全部保持：
$$
\sum_m(1+\gamma_m(u)^2)^{-1}=\infty
\quad\Longrightarrow\quad Ju\in N.
$$
非零真缺陷仍须满足相反的倒数能量可和性及其 Bessel 尾预算。

一般实际 $u\in K$ 的 Hilbert 尾仍可能慢于平方对数权。(10.1) 没有保证上述级数发散，也没有给任意实际核向量一个有界修复子列。因此 $N=M$ 和普通 ISP 仍未完成。下一步应继续控制这个具体最小正能量，或从真实缺陷条件导出与 (9.3) 相反的尾/能量限制；不能把全部 $p>0$ 正则类已饱和等同于无权核内稠密。

已用完整来源：
- 一次共同截平四次窗口稿，完整源 95dc7095d72efcae78732600feb1ff8f8bfc1d5a；
- 最小高尾图能量与 Bessel 稿，完整源 2845fc598369b3a71ca1ec39d741a9111a135602；
- [R254 第七附录：同一个真实受限 G](../results/R254-appendix-restricted-pure-kernel-right-inverse-and-subexponential-stable-range.md)；
- [R254 第八附录：真实头进位与混合词原序](../results/R254-appendix-quartic-head-budget-and-four-ninths-stable-range.md)；
- [R254 第九附录：已有 p>1/3](../results/R254-appendix-common-plateau-pure-power-inverse-and-one-third-stable-range.md)；
- [R254 第十附录：并行已有 p>1/4](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)；
- [R239 实际混合核正则提升](../results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)。

正式前序：[四次窗口与实际提升](../results/R239-appendix-quartic-hole-window-by-common-flattening-and-exact-repair.md)、[最小图能量](../results/R239-appendix-minimal-tail-repair-energy-and-convex-stable-approximation.md)。
