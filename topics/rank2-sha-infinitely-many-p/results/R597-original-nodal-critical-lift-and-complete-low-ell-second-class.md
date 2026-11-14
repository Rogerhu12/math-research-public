# R597 — 原结点临界支的同格整提升与完整低 ell 第二类

日期：2026-11-14。**状态：已证明。**

本篇支付 R577/R593 明确未包含的 $r=1,\nu=2$ 情形。
原 Euler 临界曲线在 $(t,Y)=(0,1)$ 是分裂普通结点。
三个固定原列对结点三条件给出行列式 $-2$ 的整单位块；
再用一个原常权列固定临界值的最低项，
得到同一 $\mathcal W_D$ 中的真正整基准和原非垂直临界支。

新基准满足 $A,B\in w^2$、$B/w^2$ 为单位，但 $C$ 一般只在 $w$ 中。
因此原完整 $p^3$ 展开及两条十三行仍可付清，
第三块却必须保留 $C/B$ 的一阶 Laurent 极。
正文给这一极对全部一至两条可见行的准确贡献，
并将同一个修正送入全来源的第二像判据。
还可用同一原权帽中的固定列整选 $\xi\in w^7$、$A\in w^5$，
使整个第三块只读同一 $Z^+$ 的一至两条真实续段。

没有证明最后指定余类非零，也没有发现一个新的低预算实际候选。
原主目标、R561 非零接口及完整中央条件与真实像的比较仍未完成。

## 1. 原范围及唯一遗漏情形

保原有限自由来源
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad \mathcal E=Y\partial_Y,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
\quad
h_7=16t^2+4t+7,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor .
\tag{1}
$$
取
$$
p=6s-1>101,\quad \ell\in\{1,2\},\quad
n_0=s-13>2,\quad f_D=\lfloor9D/2\rfloor+4<p .
\tag{2}
$$
$\mathcal O$ 为原有限非分歧系数环，$k$ 为剩余域。
$t=-w+O(w^2)$、$g(0)=1$、$a\in\mathcal O^\times$，
以及全部 $P_{134}/U_0$、charge 四十均保持原规范：
$$
M=c_*U_0m_{13}J,\qquad
Y_{\rm phys}=g(w)e_2(a\epsilon),\qquad w^s=p\epsilon .
\tag{3}
$$
仍保 $\epsilon^3=0$ 和 $w^\ell\epsilon^2=0$，
不先删去 raw $\bar\Gamma$ 的高 normal 项。

本篇取同一个实际非零
$$
\bar P\in\ker\bar J,\qquad
d^{C_D}\bar P=tF(t,Y),\quad t\nmid F,
\qquad
\operatorname{ord}_w(\mathcal E^2\bar P)(t(w),\bar g(w))=2 .
\tag{4}
$$
所以全局角含量是 $r=1$，物理第二 Euler 值的阶是 $\nu=2$。
两者不能在论证中互换。
(4) 对 $\ell=1,2$ 均有意义。

最低角层只有 $n\le6$ 可出现。
原首两块和第三低块给
$$
F(0,1)=F_Y(0,1)=F_{YY}(0,1)=0 .
\tag{5}
$$
因 $F(0,Y)\ne0$，其在 $Y=1$ 的重数 $c$ 满足
$$
3\le c\le6,\qquad D\ge3 .
\tag{6}
$$
特别本篇将用的 $n=0,1,2$ 原列确实存在。

以下形式函数只在 R481 已付的原有限普通系数窗口中与物理轴比较；
临界支本身则由实际整多项式定义。
不将无限长 raw sigma 级数约化为普通 $k[[w]]$。

## 2. 原临界曲线是可分普通结点

置
$$
\bar H(t,Y)=\frac{d^{C_D}}t\,\mathcal E\bar P\in k[t,Y] .
\tag{7}
$$
由 (4)，沿原低轴
$$
\bar H(t,\bar g)\in t^{s-1}k[[t]],\qquad
\operatorname{ord}_t\bar H_Y(t,\bar g)=1 .
\tag{8}
$$
这里第二式也可直接从
$\bar H_Y=d^{C_D}(\mathcal E^2\bar P)/(tY)$ 读取。
强 Hensel/Newton 递推给唯一很近分支
$$
\bar H(t,\bar\psi(t))=0,\qquad
\bar\psi-\bar g\in t^{s-2}k[[t]],\qquad
\bar\psi(0)=1,
$$
$$
\bar H_Y(t,\bar\psi)=t\,u(t),\qquad u(0)\ne0 .
\tag{9}
$$
准确地，(8) 的函数阶严格大于导数阶的两倍；
逐次 Newton 修正从 $t^{s-2}$ 开始，
后续阶严格增长。原有限低轴的任一形式延拓给出同一近分支
及这个接触下界，不使用第一个未付共振以后的 ODE。

写 $\lambda=\bar\psi'(0)$，在支坐标
$Z'=Y-\bar\psi(t)$ 中，
$$
\bar H(t,\bar\psi+Z')
=t\,u(t)Z'+v(t,Z')Z'^2 .
\tag{10}
$$
因此其二次切锥为
$$
Z'\{u(0)t+v(0,0)Z'\}.
\tag{11}
$$
两条切线定义于原 $k$ 且不同，因 $u(0)\ne0$。
一条是原非垂直近支；若 $v(0,0)=0$，
另一条就是 $t=0$，仍是普通结点。
故
$$
\bar H(0,1)=\bar H_Y(0,1)=\bar H_t(0,1)=0 .
\tag{12}
$$

这里不是把 $F=0$ 的最近两根误认为临界分支。
所提升的是同一实际 $\mathcal E\bar P$ 的结点，
(9) 是其中指定的非垂直分支。

## 3. 三条原列同时整解结点条件

先在原显示格中逐系数提升 $\bar P$，
保持全局 $t$ 含量，得到
$P^{\rm base}\in\mathcal W_D^{(1)}$。
令
$$
H_P=\frac{d^{C_D}}t\,\mathcal EP .
$$
对同一个来源考虑三条整线性条件
$$
\mathcal N(P)=\bigl(H_P(0,1),(H_P)_Y(0,1),(H_P)_t(0,1)\bigr).
\tag{13}
$$
使用原实际列
$$
L_1=tY,\qquad L_2=tY^2q_2(t),\qquad L_3=t^2Y,
\qquad q_2=(t-1)/(1+8t).
\tag{14}
$$
这些列逐条保全部原帽：
$n=1$ 的自由多项式次数帽为 $e_2=8$，
故 $tY,t^2Y$ 都在其中；
$n=2$ 的帽为 $e_3=13$，故 $tY^2q_2$ 也在其中。
全部角因子仍是原 $q_n$，且三列均有全局 $t$ 因子。
这已经支付全部十九角，不是仅在原点造出的局部列。

因 $q_2(0)=-1,q_2'(0)=9$，三列在 (13) 上的准确矩阵为
$$
\boxed{
\begin{pmatrix}
1&-2&0\\
1&-4&0\\
8C_D&18-16C_D&1
\end{pmatrix},
\qquad\det=-2 .}
\tag{15}
$$
由 (12)，$\mathcal N(P^{\rm base})\in p\mathcal O^3$。
用 (15) 的整逆一次求出 $c_i\in p\mathcal O$，令
$$
P^{\rm node}=P^{\rm base}-c_1L_1-c_2L_2-c_3L_3 .
\tag{16}
$$
于是同一个真实整来源满足
$$
\mathcal N(P^{\rm node})=0,\qquad
P^{\rm node}\equiv\bar P\pmod p,\qquad
P^{\rm node}\in\mathcal W_D^{(1)} .
\tag{17}
$$
没有分别求三条条件后再假设它们兼容。

由 (17)，
$$
H_{P^{\rm node}}(t,1+tZ)=t^2K(t,Z),
\qquad K\in\mathcal O[t,Z].
\tag{18}
$$
模 $p$ 时 $K(0,\lambda)=0$ 且 $K_Z(0,\lambda)=u(0)\ne0$。
先在 $\mathcal O$ 中提升这一个简单切线根，
再用形式隐函数定理得 $Z(t)\in\mathcal O[[t]]$。
置
$$
\boxed{\psi(t)=1+tZ(t),\qquad
\mathcal EP^{\rm node}(t,\psi(t))=0,\qquad
\psi\bmod p=\bar\psi.}
\tag{19}
$$
这是原系数环内的支，不需要常量域的二次扩张；
指定的切线根原本已在 $k$ 中且为简单根。

还可支付以后低行所需的实际规范。
令
$$
c_A=[t]P^{\rm node}(t,\psi(t))
=[t]P^{\rm node}(t,1)\in p\mathcal O .
$$
最后取
$$
\boxed{P^{\rm crit}=P^{\rm node}-c_A t.}
\tag{20}
$$
$t$ 是原常权列，次数一不超过 $e_1=4$。
它的 Euler 导数为零，所以 (17)–(19) 完全不变。
(20) 仍是同一 $\bar P$ 的实际整提升。

换用 (20) 只改变基准的 $p\mathcal W_D$ 项，
相应差除以 $p$ 可并入同一个第一次修正 $R$。
因此没有丢弃原 $p^3$ 提升候选，也没有改变物理 $g$。

## 4. 准确的 A、B、C 阶与原接触

在同一 $w$ 中定义
$$
A=P^{\rm crit}|_\psi,\qquad
B=\mathcal E^2P^{\rm crit}|_\psi,\qquad
C=\mathcal E^3P^{\rm crit}|_\psi .
$$
由 (18)–(20)，
$$
\boxed{
A\in w^2\mathcal O[[w]],\quad
B=w^2b,\ b(0)\in\mathcal O^\times,\quad
C\in w\mathcal O[[w]],\quad
\mathcal EP^{\rm crit}|_\psi=0.}
\tag{21}
$$
确实，在 $t$ 中有准确式
$$
B=t^2d^{-C_D}\psi K_Z(t,Z(t)),
$$
$$
C=B+t\,d^{-C_D}\psi^2K_{ZZ}(t,Z(t)).
\tag{22}
$$
这里第二项一般只有一个 $t$ 因子，不能删掉。

原有限窗口内取
$$
\eta=\log(g/\psi)=\eta_0+p\xi,\qquad
\eta_0\in w^{s-2}\mathcal O[w],\qquad
\xi\in w\mathcal O[[w]].
\tag{23}
$$
$\xi(0)=0$ 来自 $g(0)=\psi(0)=1$；
(9) 给 $\eta_0$ 的阶。
由原第一块及临界 Taylor 展开，
$$
\bar A\in w^s k[[w]] .
\tag{24}
$$
因为 $B\eta_0^2$ 从 $2s-2$ 开始，
$C\eta_0^3$ 从 $3s-5$ 开始，均超出首块。

(21) 还说明，沿整个原正规化轴 $g$，
$$
(\mathcal E^2P^{\rm crit})(t,g)\in w^2\mathcal O[[w]] .
\tag{25}
$$
证明用
$B+C\eta+(\mathcal E^4P)|_\psi\,\eta^2/2+\cdots$：
$B$ 含 $w^2$，全部更高 Euler 值含全局 $t$，
而 $\eta(0)=0$。故 (25) 是整系数恒等，
对 $\ell=1,2$ 的低第三块均足够。

## 5. 原完整 J 到 p³：极项没有被隐去

令 $\mathscr S$ 始终表示原 $w$ 中的真正 $s$ 阶移位。
按 R481 完整公式，原三个输出为
$$
J(P)=\left(
\pi_sP_0,\quad
\pi_s(aP_1+p\mathscr SP_0),\quad
\pi_\ell\left(\frac{a^2}{2}P_2+
pa\mathscr SP_1+p^2\mathscr S^2P_0\right)\right).
\tag{26}
$$
对 (20)，准确得到
$$
J_0(P^{\rm crit})
=\pi_s(A+p^2B\xi^2/2)\pmod{p^3},
$$
$$
\begin{aligned}
J_1(P^{\rm crit})={}&
p\pi_s\left(aB\xi+\mathscr SA+
\frac12\mathscr S(B\eta_0^2)\right)\\
&+p^2\pi_s\left(
\frac a2C\xi^2+\mathscr S(B\eta_0\xi)
+\frac12\mathscr S(C\eta_0^2\xi)\right)
\pmod{p^3},
\end{aligned}
$$
$$
\begin{aligned}
J_2(P^{\rm crit})={}&
pa\,\pi_\ell\mathscr S(B\eta_0)\\
&+p^2\pi_\ell\left[
a\mathscr S(B\xi+C\eta_0\xi)+\mathscr S^2A+
\frac12\mathscr S^2(B\eta_0^2)\right]\pmod{p^3}.
\end{aligned}
\tag{27}
$$

这些形式与 R577 的显示式相同，但所需阶数证明不同。
第一块中 $B\eta_0\xi$ 的阶至少 $s+1$，
$C\eta_0\xi^2$ 的阶也至少 $s+1$。
第二块中未经移位的 $C\eta_0\xi$ 从 $s$ 起，
故超出 $\pi_s$；移位后的
$C\eta_0^2\xi$ 则从 $s-2$ 起，必须保留。
第三块的直接 $P_2$ 项由 (25) 整消失，
但 $\mathscr S(C\eta_0\xi)$ 现在可有非零常数项。
所有含三个 $\eta_0$ 的剩余项在两次移位后仍从
$s-5>\ell$ 起；更高项也超出原窗口。
这些估计同时保留全部 $p$ 次数，未先把高 normal 项置零。

整个可见首像仍为同一来源上的
$$
\mathcal T_\psi(R)=
\left(\pi_{n_0}R_0,\ a\pi_{n_0}R_1,\
\frac{a^2}{2}\pi_\ell R_2\right),
\qquad R_j=(\mathcal E^jR)|_\psi ,
\tag{28}
$$
因为 $\bar g-\bar\psi$ 的阶 $s-2$ 严格大于 $n_0$。
原首 forcing 完整为
$$
\boxed{\mathcal F_P=
\left(\overline{\pi_{n_0}A/p},\
\pi_{n_0}\overline{aB\xi+\mathscr SA},\
a\pi_\ell\overline{\mathscr S(B\eta_0)}\right).}
\tag{29}
$$
第一项先截断再除 $p$；其整性由 (24) 给出。

## 6. 全低行、同一修正及两条十三行

由于 (21)，首 forcing 的前两块低两行仍只来自真实 carry。
取整的
$$
\alpha=\pi_2\mathscr SA,\qquad
\beta=\pi_\ell\mathscr S(B\eta_0),
$$
并将 $\beta$ 零延拓到长度二，记为 $\beta^\sharp$。
用 R593 的同一实际三列定义
$$
x_0=(3\alpha-2\beta^\sharp)/(2a),\quad
x_1=2(\beta^\sharp-\alpha)/a,\quad
x_2=(\alpha-2\beta^\sharp)/(2a),
$$
$$
R_{\rm bd}=\sum_{i=0}^2Y^iq_i\,
\pi_2^t\left(\frac{x_i(w(t))}{\psi^iq_i}\right).
\tag{30}
$$
于是整系数上
$$
(R_{\rm bd})_0=0\bmod w^2,\quad
(R_{\rm bd})_1=-\alpha/a\bmod w^2,\quad
(R_{\rm bd})_2=-2\beta^\sharp/a\bmod w^2 .
$$

这里的核按**物理两低行**定义，不假定候选全局含 $t^2$：
$$
\mathcal K_{2,\ell}
=\{S\in\mathcal W_D:S_0,S_1\in w^2,\ S_2\in w^\ell\}.
\tag{31}
$$
其完整实际分解正是 R578/R593 已付的
$$
\mathcal K_{2,2}
=\mathcal W_D^{(2)}
\oplus\bigoplus_{n=3}^{\min(D,6)}\mathcal OQ_n,
\qquad
\mathcal K_{2,1}=\mathcal K_{2,2}\oplus\mathcal OQ_{\rm quad},
$$
$$
Q_{\rm quad}=t(1-2Y-Y^2q_2),\qquad
(Q_{\rm quad})_2=-2w+O(w^2).
\tag{32}
$$
全部 $Q_n$ 是原真实列，前三个支上 jet 在 $w^2$ 中；
(31) 的每条显示来源都含全局 $t$。
这份核分解只用原 $q_n$ 和 $\psi(0)=1$，
所以在新结点基准上仍准确。

任何有希望到 $p^3$ 的首次修正可取同一个
$$
R=R_{\rm bd}+S,\qquad S\in\mathcal K_{2,\ell}.
\tag{33}
$$
改变该模 $p$ 低行整提升的差在 $p\mathcal W_D$，
由下一次同格 $p^2T$ 吸收。

剥下整个原 $c_*U_0$ 后，准确整表示仍是
$$
M=(J_A,pJ_B)^t
\tag{34}
$$
加十三条自由零行；
$A$ 读前两块 $<n_0$ 及第三块 $<\ell$，
$B$ 是前两块各末十三行。
因此原 $p^3$ 提升首先迫使同一个
$Q_2=P^{\rm crit}+pR$ 满足
$$
\boxed{JQ_2\in p^2.}
\tag{35}
$$
原 $B$ 行不能被下一次 $p^2T$ 改掉：
$pJ_B(Q_2+p^2T)\in p^3$ 正给 $J_BQ_2\in p^2$。

令 $A_1=\pi_sA/p$。
由 (27)，(35) 的前两块准确为
$$
R_0+\eta_0R_1=-A_1\bmod(p,w^s),
$$
$$
R_1+\eta_0R_2=
-B\xi-a^{-1}\mathscr SA-
(2a)^{-1}\mathscr S(B\eta_0^2)\bmod(p,w^s).
\tag{36}
$$
第三块的一次商由 (30) 在整系数上恰为零。

所以定义
$$
\mathcal D_\psi^+(S)=
\left(w^{-2}S_0,\ w^{-2}(S_1+\eta_0S_2)\right)
\bmod w^{s-2},\qquad S\in\mathcal K_{2,\ell},
$$
$$
f_0^+=A_1-a^{-1}\eta_0\alpha,\qquad
f_1^+=B\xi+a^{-1}\mathscr SA+
(2a)^{-1}\mathscr S(B\eta_0^2)-2a^{-1}\eta_0\beta^\sharp ,
$$
$$
\boxed{\mathcal G_P^+
=-w^{-2}\left(f_0^++(R_{\rm bd})_0,\
f_1^++(R_{\rm bd})_1\right)\bmod(p,w^{s-2}).}
\tag{37}
$$
所有除法由 (30)–(31) 保证；
(35) 等价于
$\bar{\mathcal D}_\psi^+(\bar S)=\mathcal G_P^+$。

$\ell=2$ 时 (37) 是完整纯两 jet。
$\ell=1$ 时写同一 $S=S'+\gamma Q_{\rm quad}$，
它与纯两 jet 只差第二目标最高一行
$$
-2\lambda\bar\gamma w^{s-3},
\qquad \lambda=[w^{s-2}]\bar\eta_0 .
\tag{38}
$$
$\gamma$ 仍是同一个实际来源系数，不是独立可选高尾。

## 7. 同一 Z 的增强及整个第二 forcing

对 (33) 的同一个解置
$$
Z=R_1+B\xi+a^{-1}\mathscr SA,\qquad
Z^+=Z+\eta_0R_2+(2a)^{-1}\mathscr S(B\eta_0^2).
\tag{39}
$$
(36) 给
$$
\bar Z^+\in w^s k[[w]],\qquad
\bar Z\in w^{s-2}k[[w]],\qquad
\pi_{n_0}\mathscr S(\bar\eta_0\bar Z)=0 .
\tag{40}
$$
最后一项的移位后阶至少 $s-4>n_0$。
这是已付二十六条真实 carry 后的消项，
不是只在短首提升中使用的估计。

先在原精度形成
$$
L_0=\overline{\frac{\pi_{n_0}(A+pR_0)}{p^2}},\qquad
L_1=\overline{\frac{\pi_{n_0}(aB\xi+\mathscr SA+aR_1)}p}.
\tag{41}
$$
它们整，低两行在整系数上为零。
$\xi$ 在带一个外部 $p$ 的项中保所需两位，
不能先约化后形成 (41)。

原完整第二代表
$\Psi=\overline{J_AQ_2/p^2}$ 准确为
$$
\boxed{\Psi_0=L_0+
\pi_{n_0}\left(-\frac12B\xi^2-\frac{\xi}{a}\mathscr SA\right),}
$$
$$
\boxed{\Psi_1=L_1+\pi_{n_0}\left(
\frac a2C\xi^2+a\xi R_2+\mathscr SR_0
-a^{-1}\mathscr S(\eta_0\mathscr SA)\right),}
$$
$$
\boxed{\Psi_2=
a\pi_\ell\mathscr SZ^+
+\frac{a^2}{2}\pi_\ell(\xi R_3)
+a\pi_\ell\mathscr S(\eta_0C\xi).}
\tag{42}
$$
证明直接将 (27) 与同一 $pR$ 的完整三个 Euler 展开代入 (26)。
第一块用 (36) 消去 $R_1$；
第二块中
$\mathscr S(\eta_0(B\xi+R_1))$
等于
$\mathscr S(\eta_0Z)-a^{-1}\mathscr S(\eta_0\mathscr SA)$，
第一项恰由 (40) 消失。
第三块将全部
$\mathscr S^2A,\mathscr S^2(B\eta_0^2)/2$ 及高 $R_1,R_2$
合回 (39)，得到 (42)。
由于 $C\in w$ 而 $\xi\in w$，
这里所需其余消项仍满足 (27) 已列的阶数门；
没有额外假定 $C\in w^2$。

## 8. 一阶 Laurent 极对一至两条第三行的准确贡献

令
$$
B=w^2b,\quad C=wc,\quad \eta_0=w^{s-2}v,\qquad
\beta_{\rm full}=\mathscr S(B\eta_0)=bv,
$$
$$
\kappa=C/B=\kappa_{-1}w^{-1}+\kappa_0+O(w),\quad
\xi=\xi_1w+\xi_2w^2+O(w^3),\quad
z_j=[w^{s+j}]\bar Z^+ .
\tag{43}
$$
以下系数在 $k$ 中读取。
$\kappa$ 只允许一个极，而 $\kappa\xi$ 正规。
准确恒等为
$$
\boxed{\mathscr S(\eta_0C\xi)=\beta_{\rm full}\kappa\xi.}
\tag{44}
$$
它保原 $w$ 移位，不是在来源中除 $t^s$。

因 (32) 每条核列含 $t$，
$R_3(0)$ 仍仅由三列右逆给出：
$$
\boxed{R_3(0)=(2\alpha_0-6\beta_0)/a .}
\tag{45}
$$
使用其上 $\mathcal E^3=3\mathcal E^2-2\mathcal E$，
(42) 的整个第三块就是
$$
\boxed{\Psi_2=a(z_0+\beta_0\kappa_{-1}\xi_1)
\qquad(\ell=1),}
\tag{46}
$$
以及
$$
\boxed{
\begin{aligned}
\Psi_2={}&a(z_0+\beta_0\kappa_{-1}\xi_1)\\
&+a\Bigl[
z_1+\xi_1(\alpha_0-3\beta_0)
+\beta_0(\kappa_{-1}\xi_2+\kappa_0\xi_1)
+\beta_1\kappa_{-1}\xi_1
\Bigr]w
\qquad(\ell=2).
\end{aligned}}
\tag{47}
$$
$\ell=1$ 不读取 $\beta_1$；
$\ell=2$ 的 $\beta_1$ 是同一个 $\beta_{\rm full}$ 的一次系数，
已经包含在原低右逆中。
$z_0,z_1$ 均是同一 $R$ 的真实续段，不能由
$\pi_sZ^+=0$ 另设为零。

该极的首系数还由原结点给出：
$$
\boxed{
\bar\kappa_{-1}
=-\,\frac{\bar K_{ZZ}(0,\lambda)}{\bar K_Z(0,\lambda)}.}
\tag{48}
$$
符号来自原 $t/w=-1+O(w)$。
分母是 (18) 的单位。
若原 $F(0,Y)$ 在 $1$ 恰有三重根，
分子是 $F_{YYY}(0,1)$ 的同一非零单位，
所以 $\bar\kappa_{-1}\ne0$；
若其重数 $c>3$，则 $\bar\kappa_{-1}=0$。
这只计算真实形状系数，未把它或 $\xi_1$ 认成余核单位。

当 $\bar\kappa_{-1}=0$ 时，(46)–(47) 正恢复 R593 的正规形状式。
恰三重最低角层则必须保新增的
$\beta_0\kappa_{-1}\xi_1$、
$\beta_0\kappa_{-1}\xi_2$ 和
$\beta_1\kappa_{-1}\xi_1$；
它们不是另一个自由高轴参数。


### 8.1. 同一原帽内还能把 xi 的前六项整归零

可以进一步选择上述实际基准，使
$
\boxed{\xi\in w^7\mathcal O[[w]],\qquad
A\in w^5\mathcal O[[w]].}
\tag{48a}
$
这是用原来源作有限三角消元，不是给 $\xi$ 自由指定系数。

在 (16) 的结点三条件已整满足之后，
使用同一 $n=1$ 权内的六条列
$
t^jY,\qquad j=3,\ldots,8 .
\tag{48b}
$
它们的自由多项式次数均不超过原 $e_2=8$，
全部十九角仍由原 $q_1=1$ 支付。
对应 $H_P$ 的改变量是
$t^{j-1}d^{C_D}Y$，沿原 $g(t)$ 的首项准确为 $t^{j-1}$。
所以逐阶整消去
$H_P(t,g(t))$ 的 $t^2,\ldots,t^7$ 六个系数，
是一份单位三角系统。
这些所需系数本来全在 $p\mathcal O$：
约化仍是 (8) 的 $\bar H(t,\bar g)\in t^{s-1}$，
且每次修正仍是 $p$ 倍实际列。
它们也不动 $H_P$ 在 $(0,1)$ 的常数和一次项，
故结点三条件保持。

这里只需原 $g(t)$ 的固定有限前缀，
该前缀在 (2) 的范围中已整；
任意整形式延拓均给同一个计算。
所得 $H_P(t,g)\in t^8$，
且 $H_Y(t,g)=t$ 乘整单位。
沿原指定非垂直切线的同一 Hensel 论证遂给
$\psi-g\in t^7$。
因 $\eta_0\in w^{s-2}$、$s-2>7$，
准确有 $\xi=(\log(g/\psi)-\eta_0)/p\in w^7$。

最后用原常权的四列 $t,t^2,t^3,t^4$
消去 $A(t)$ 的前四个系数。
这些系数均在 $p\mathcal O$，因为 (24) 保持；
原常权帽恰为四，所以没有增加预算。
此步不改变任何 Euler 导数和临界支，故得到 (48a)。

对这种完整的同格基准，(42) 的整个第三块进一步化为
$
\boxed{
\Psi_2=
\begin{cases}
a z_0,&\ell=1,\\
a(z_0+z_1w),&\ell=2 .
\end{cases}}
\tag{48c}
$
确实 $\xi R_3$ 从 $w^7$ 起，
而 $\beta_{\rm full}\kappa\xi$ 至少从 $w^6$ 起，
都超出长度 $\ell\le2$。
同时首 forcing 中 $A/p$ 从 $w^5$ 起，
$B\xi$ 从 $w^9$ 起。

(48c) 不把 $z_0,z_1$ 变成自由行，也不证明其真实余类消失。
若从旧基准改到 (48a)，
必须把两实际基准的差除 $p$ 吸入同一个 $R$，
并继续用改变后的 (41)–(42) 计算前两块。
所有 $D^+$ 和 $D^{\rm short}$ 的来源仍是 (31)；
(52) 的完整判据保持。
因此一般基准的 Laurent 项 (46)–(47) 与规范基准 (48c) 相容：
前者不能在不改整个修正的情况下直接删去。

## 9. 原全 p³ 的同一第二像判据

(35) 成立后，原 $p^3$ 提升余下的条件准确为
$$
\bar J_A(T)=-\Psi,\qquad T\in\mathcal W_D .
\tag{49}
$$
不是要求完整 $J(Q_2+p^2T)\in p^3$；
全部 $B$ 行已经由 (35) 处于原 $p^3$ 中。

令
$$
h_0=\pi_2\Psi_0,\quad h_1=\pi_2\Psi_1,\quad
h_2^\sharp=\text{将 }\Psi_2\text{ 零延拓到长度二},
$$
$$
y_0=-h_0+3h_1/(2a)-h_2^\sharp/a^2,\quad
y_1=-2h_1/a+2h_2^\sharp/a^2,\quad
y_2=h_1/(2a)-h_2^\sharp/a^2 .
$$
按 (30) 同一原三列构造
$$
T_{\rm bd}=\sum_{i=0}^2Y^iq_i\,
\pi_2^t\left(\frac{y_i(w(t))}{\psi^iq_i}\right).
\tag{50}
$$
则它整支付 (49) 的全部低行，剩余来源准确为 (31)。

置
$$
\mathcal D_\psi^{\rm short}(H)=
(w^{-2}H_0,w^{-2}H_1)\bmod w^{n_0-2},
\qquad H\in\mathcal K_{2,\ell},
$$
$$
\boxed{\mathcal H_P(R)=
-w^{-2}\bigl(\Psi_0+(\bar T_{\rm bd})_0,\
a^{-1}\Psi_1+(\bar T_{\rm bd})_1\bigr)
\bmod w^{n_0-2}.}
\tag{51}
$$
它是原同预算、全部剩余列的矩阵，
没有把临界曲线上的任意截面算作来源。

**定理。** 原 (4) 的 $\bar P$ 可提升到 $M(P^{(3)})\in p^3$，
当且仅当存在同一个 $\bar S\in\bar{\mathcal K}_{2,\ell}$，
使
$$
\boxed{
\bar{\mathcal D}_\psi^+(\bar S)=\mathcal G_P^+,\qquad
\mathcal H_P(R_{\rm bd}+S)
\in\operatorname{im}\bar{\mathcal D}_\psi^{\rm short}.}
\tag{52}
$$
其中 (42)、(46)–(47) 必须使用同一个实际 $R=R_{\rm bd}+S$，
$\ell=1$ 的 $\gamma$ 也保持 (38) 的同一来源系数。

必要性由 (34)–(37)、(49) 和实际低行右逆 (50) 得到。
反向以第二项选 $T=T_{\rm bd}+H$，则 (49) 成立；
全部原 $B$ 行由第一项保证，故恢复原 $M$ 模 $p^3$。
若 $S$ 换为 $S+pV$、$V\in\mathcal K_{2,\ell}$，
$\Psi$ 只加 $\bar J_A(V)$，
所以 (51) 只改变一个实际 $\bar{\mathcal D}_\psi^{\rm short}(V)$ 像。
这证明判据保同一个整提升，且不依赖其代表。

## 10. 覆盖范围与仍未付的非零

原低角分类已经证明：
对 $1\le\ell\le2$，
若相对首核的第二 Euler 值在原缺失 carry 中可见，
则 $1\le r\le\nu\le2$。
R593 处理 $r=\nu$；
本篇的同格结点构造与 (52) 处理唯一余下的 $r=1,\nu=2$。
因此这一低 ell 相对首核范围不再缺一个实际整临界基准。

新增内容是固定原列的结点整求解、非垂直整支、
不同 $r/\nu$ 下完整原 $p^3$ 阶数核定，
以及一般基准必须保留的一阶 Laurent 形状项 (46)–(48)。
同预算有限规范 (48a)–(48c) 进一步支付这些项的实际基准消去，
保全前两块和同一修正。
它们没有证明 (52) 的第一指定类不可达，
也没有在第一解空间上证明第二指定类非零。

所有三条完整中央条件仍是原固定来源的条件。
本篇未给 $H,K,\psi$、临界值或任意乘积新增中央零，
未由源端单位块推出物理像饱和，
也未将形状系数的单位等同于实际 $C_2(M)$ 中的单位。
下一步仍须在 (52) 的同一个来源、同一个解和全前两块上
判定显示的指定余类。

## 依赖

- [R577](R577-original-critical-factor-euler-lift-and-complete-first-forcing.md)：
  原三块公式、原有限窗口、实际首 forcing 与整提升范围。
- [R578](R578-complete-critical-boundary-elimination-and-fixed-polar-carry.md)：
  原固定低行右逆及 $\mathcal K_{2,\ell}$ 的全部显示列。
- [R593](R593-original-critical-carry-completion-and-actual-second-normal-tail.md)：
  两条十三行的原整运输、同一两 jet 延长与原第二像判据；
  本篇对新增结点情形重新支付阶数和 Laurent 项。
- [原低 ell 最近二分支记录](../notes/2026-11-14-deep-low-ell-visible-kernel-and-two-nearest-branches.md)：
  $r=1,\nu=2$ 的原近临界支与光滑外支范围。
- [R481](R481-full-third-precision-normal-form-and-common-correction.md)、
  [R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)：
  全部普通系数、真实移位、原 $U_0$ 与完整 carry。

本篇为全参数证明；没有新增素数扫描或未执行的数值证书。
