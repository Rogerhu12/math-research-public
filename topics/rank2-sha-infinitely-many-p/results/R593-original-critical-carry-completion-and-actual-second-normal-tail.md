# R593 — 原临界 carry 的完整延拓与同一修正的第二 normal 高尾

日期：2026-11-14。**状态：已证明。**

本篇继续 R577/R578 的同一个低 $\ell$ 临界来源。
要把原 $M$ 的一次提升再升到模 $p^3$，
同一个修正必须先支付两条十三行 carry。
这把 R578 的两个短 jet 延长恰好十三行；
在 $r=\ell$ 时仍是完整代数支上的两 jet，
唯一 $(r,\ell)=(2,1)$ 例外是一条由实际 $Q_{\rm quad}$ 给出的最高行。

这次真实 carry 相容使原 $Z$ 消失阶从 $s-13$ 提高到 $s-r$，
把第二块此前余下的末 $r$ 项全部消掉。
随后给全部三块的下一位。
在同格正规化 $\psi(0)=1$ 后，
第三块只读同一个完成后 $Z^+$ 的一至两条真实续段，
以及一个固定临界形状常数；
没有额外自由的第三 normal jet。

最后把整个模 $p^3$ 提升写成两个确定的实际像判据，
第二个仍是 R578 的同一短 $\mathcal D_\psi$。
本文没有证明其指定余核类非零，
也没有把两个十三行或未知高续段自由指定。
原主目标及 R561 的非零接口未完成。

## 1. 原对象与合法的同格临界正规化

保 R577/R578 全部范围：
$$
p=6s-1>101,\quad
\ell\in\{1,2\},\quad
\ell\le r=\nu\le2,\quad n_0=s-13>r,\quad
f_D<p.
\tag{1}
$$
同一个 $\bar P\in\ker\bar J$、实际来源
$\mathcal W_D$、十九角、次数帽、相对
$\mathcal E=Y\partial_Y$ 及原物理评价均不变。
特别
$$
M=c_*U_0m_{13}J.
\tag{2}
$$
沿用原 $w,t(w)$，其中 $t=-w+O(w^2)$；
$\pi_j$ 始终是原 $w$ 次数 $<j$。
所有 $\mathscr S$ 都先在这个 $w$ 中作真正 $s$ 阶移位，
不能先改成来源中的除 $t^s$。

R577 已付 $P^{\rm crit}\in\mathcal W_D$、
整临界分支 $\psi$ 和
$$
A=P^{\rm crit}|_\psi,\quad
B=\mathcal E^2P^{\rm crit}|_\psi=w^r b,\quad b(0)\in\mathcal O^\times,
\quad C=\mathcal E^3P^{\rm crit}|_\psi\in w^r\mathcal O[[w]],
$$
$$
\mathcal EP^{\rm crit}|_\psi=0,\qquad
\eta=\log(g/\psi)=\eta_0+p\xi,\qquad
\eta_0\in w^{s-r}\mathcal O[w].
\tag{3}
$$
这些式子仅在 R577 已付的原有限普通系数窗口中使用。

可以并将取
$$
\boxed{\psi(0)=1,\qquad \eta_0(0)=\xi(0)=0.}
\tag{4}
$$
准确理由如下。若原 $\psi(0)=u\equiv1\pmod p$，
把基准换成 $P^{\rm crit}(t,uY)$。
各原权分量只乘整单位 $u^n$，
故全部角整除、次数帽、全局 $t^r$ 和同一 $\mathcal W_D$ 保持，
且模 $p$ 仍是原 $\bar P$。
新的临界支是 $\psi/u$；$A,B,C$ 的支上值完全不变。
两个实际基准之差在 $p\mathcal W_D$ 中，
把它除 $p$ 加入同一个修正 $R$，
就保持 $P^{\rm crit}+pR$ 这个实际提升不变。
这只是原候选的整基准选择，没有改变物理 $g$、Gaussian 或 $M$。
因 $g(0)=1$，新的实际 log 比常数为零，
可取 (4)。

以下所有
$$
R_j=(\mathcal E^jR)|_\psi
\tag{5}
$$
都在临界支上读取。
原 $g$ 与 $\psi$ 的区别在全部 carry 中仍按 (3) 展开保留。

## 2. 规范低行右逆与全部真实核

这次把 R578 的低 carry 提升选成实际整系数本身：
$$
\boxed{\alpha=\pi_r\mathscr SA,\qquad
\beta=\pi_\ell\mathscr S(B\eta_0).}
\tag{6}
$$
令 $\beta^\sharp$ 为次数 $<r$ 的零延拓；
当 $(r,\ell)=(2,1)$ 时它就是常数 $\beta_0$。
这不是把其它原列的第三 jet 额外置零，
只是固定低行右逆。

仍用真实 $q_0=q_1=1,q_2=(t-1)/(1+8t)$，置
$$
x_0=(3\alpha-2\beta^\sharp)/(2a),\quad
x_1=2(\beta^\sharp-\alpha)/a,\quad
x_2=(\alpha-2\beta^\sharp)/(2a),
$$
$$
R_{\rm bd}
=\sum_{i=0}^2Y^iq_i(t)\,
\pi_r^t\left(\frac{x_i(w(t))}{\psi(t)^iq_i(t)}\right).
\tag{7}
$$
三个有限多项式都在原次数帽内。
与 R578 完全相同的单位 Vandermonde 给整恒等
$$
(R_{\rm bd})_0=0\bmod w^r,\quad
(R_{\rm bd})_1=-\alpha/a\bmod w^r,\quad
(R_{\rm bd})_2=-2\beta^\sharp/a\bmod w^r.
\tag{8}
$$

记原有限自由核为
$$
\mathcal K_{r,\ell}
=\{R\in\mathcal W_D:
R_0,R_1\in w^r\mathcal O[[w]],\
R_2\in w^\ell\mathcal O[[w]]\}.
\tag{9}
$$
R578 的完整实际分解仍为
$$
\begin{aligned}
\mathcal K_{1,1}&=\mathcal W_D^{(1)},\\
\mathcal K_{2,2}&=\mathcal W_D^{(2)}
 \oplus\bigoplus_{n=3}^{\min(D,6)}\mathcal OQ_n,\\
\mathcal K_{2,1}&=\mathcal W_D^{(2)}
 \oplus\bigoplus_{n=3}^{\min(D,6)}\mathcal OQ_n
 \oplus\mathcal OQ_{\rm quad},
\end{aligned}
\tag{10}
$$
其中全部 $Q_n$ 是同一原格的列，其前三个 Euler jet 都在 $w^2$ 中，
而
$$
\boxed{Q_{\rm quad}=t(1-2Y-Y^2q_2(t)),\qquad
(Q_{\rm quad})_2=-2w+O(w^2).}
\tag{11}
$$
每一条 (10) 的来源列都含全局 $t$ 因子；
这最后一点也对 $Q_n,Q_{\rm quad}$ 成立。

任何有希望延伸的第一次修正都可以取成
$$
\boxed{R=R_{\rm bd}+S,\qquad S\in\mathcal K_{r,\ell}.}
\tag{12}
$$
确实，其模 $p$ 的低行已经被原首提升强迫为 (8)。
R578 的整分裂允许把该模 $p$ 核向量提升到 (9)。
换到 (12) 只改变 $R$ 的 $p$ 倍，
相应差可吸收到下一次实际 $p^2T$ 修正中。
所以 (12) 不丢弃原模 $p^3$ 提升候选。

## 3. 为什么两条十三行先强迫整个 J 窗口

剥下整个原 $c_*U_0$，并只作 R449 已付的整基变换后，
(2) 准确成为
$$
\boxed{M=(J_A,pJ_B)^t}
\tag{13}
$$
加原十三条自由零行。
这里 $A$ 是前两块的 $<n_0$ 行及第三块的 $<\ell$ 行，
$B$ 是前两块各自 $[n_0,s)$ 的十三行。
(13) 没有在目标格中除 $p$；
它保留了真实 $w^{13}$ 的两个非单位行带。

设同一个 $Q_2=P^{\rm crit}+pR$ 已满足 $M Q_2\in p^2$。
若存在原 $T\in\mathcal W_D$ 使
$$
M(Q_2+p^2T)\in p^3,
\tag{14}
$$
则 (13) 的 $B$ 分量给
$$
pJ_BQ_2+p^3J_BT\in p^3,
\quad\text{即 }J_BQ_2\in p^2.
$$
$A$ 分量在第一次提升时已经给 $J_AQ_2\in p^2$。
因此同一个 $R$ 必须先满足
$$
\boxed{J(P^{\rm crit}+pR)\in p^2.}
\tag{15}
$$
反过来，一旦 (15) 成立，(14) 中的所有 $B$ 分量本来就在
$p^3$ 中；剩余条件只有
$$
\boxed{\bar J_A(T)=
-\overline{J_A(P^{\rm crit}+pR)/p^2}.}
\tag{16}
$$
这没有声称 $J(Q_2+p^2T)\in p^3$。
整个 $U_0$、十三自由行和两条真实行缩放均已由 (13) 保留。

## 4. 真二 jet 延长十三行及唯一最高行例外

从 R577 的完整三块展开，
(15) 对 (12) 准确等价于
$$
R_0+\eta_0R_1=-A_1\bmod(p,w^s),
\qquad
A_1=\frac{\pi_sA}{p}\in\mathcal O[w],
\tag{17}
$$
$$
R_1+\eta_0R_2
=-B\xi-a^{-1}\mathscr SA
-\frac1{2a}\mathscr S(B\eta_0^2)
\bmod(p,w^s).
\tag{18}
$$
第三块的一次商因 (6)、(8)、(9) 在整系数上严格为零：
$$
\boxed{\pi_\ell\left(
a\mathscr S(B\eta_0)+\frac{a^2}{2}R_2
\right)=0.}
\tag{19}
$$
(17) 中 $A_1$ 的整性来自原 $\bar A\in w^s$；
不能把 $A/p$ 扩展为未付的无限整级数。

由 (8) 及 $\eta_0\in w^{s-r}$，
(17) 的全部修正可替为
$R_0=-A_1+\eta_0\alpha/a\bmod(p,w^s)$。
对 (18) 保实际 $\eta_0R_2$，得到整有限来源映射
$$
\boxed{
\mathcal D_\psi^+:\mathcal K_{r,\ell}\longrightarrow
(\mathcal O[w]/w^{s-r})^2,\quad
S\longmapsto
\left(w^{-r}S_0,\ w^{-r}(S_1+\eta_0S_2)\right).
}
\tag{20}
$$
两个目标除法都由原低行核实际保证。
定义同一个原目标
$$
f_0^+=A_1-a^{-1}\eta_0\alpha,
$$
$$
f_1^+=B\xi+a^{-1}\mathscr SA
+\frac1{2a}\mathscr S(B\eta_0^2)
-\frac2a\eta_0\beta^\sharp .
$$
则 (15) 的准确判据是
$$
\boxed{
\bar{\mathcal D}_\psi^+(\bar S)=\mathcal G_P^+,\qquad
\mathcal G_P^+=
-w^{-r}\left(f_0^++(R_{\rm bd})_0,\
f_1^++(R_{\rm bd})_1\right)\bmod(p,w^{s-r}).
}
\tag{21}
$$
低 $r$ 行由 (8) 消掉，故 (21) 中除法合法。

当 $r=\ell$ 时，$S_2\in w^r$，
所以 $\eta_0S_2\in w^s$，(20) 恰为完整支上的两 jet。
当 $(r,\ell)=(2,1)$，按 (10) 唯一写
$$
S=S'+\gamma Q_{\rm quad},
\qquad
S'\in\mathcal W_D^{(2)}\oplus\bigoplus\mathcal OQ_n.
$$
记 $\lambda=[w^{s-2}]\bar\eta_0$。
于是模 $p$ 的 (20) 与纯两 jet 矩阵只差
$$
\boxed{
-2\lambda\bar\gamma\,w^{s-3}
\quad\text{加在第二目标的最高一行。}
}
\tag{22}
$$
因为所有 $S'$ 的第二 Euler jet 在 $w^2$ 中，
(11) 支付了该例外的完整系数。
$\lambda\ne0$ 时，这个来源到环境目标的更新确实秩一；
$\gamma$ 是同一个实际 $Q_{\rm quad}$ 的系数，
不是可以与其它 jet 分开另选的变量。
取真实像商之后的秩仍须按 (20) 计算。

(20) 约化到长度 $n_0-r$ 时恰为 R578 的
$\mathcal D_\psi$，只作已付的 $t/w$ 单位换参。
所以 (21) 是同一首提升后新增的恰好二十六条实际行条件，
没有删除其它列或把核交与来源直和交换。

## 5. 原 Z 的新增消失阶与固定的末 r 项

对同一个 (12) 定义实际函数
$$
Z=R_1+B\xi+a^{-1}\mathscr SA,
$$
$$
\boxed{
Z^+=Z+\eta_0R_2+\frac1{2a}\mathscr S(B\eta_0^2).
}
\tag{23}
$$
(18) 准确给
$$
\boxed{\bar Z^+\in w^s k[[w]],\qquad
\bar Z\in w^{s-r}k[[w]].}
\tag{24}
$$
第二项由 (23) 中两个已知项的阶至少为 $s-r$ 得到。
这比只用原首提升得到的 $\bar Z\in w^{s-13}$ 更强。

因此
$$
\boxed{\pi_{n_0}\mathscr S(\bar\eta_0\bar Z)=0.}
\tag{25}
$$
因为移位后的阶至少是 $s-2r>s-13=n_0$。
它消掉的是整个第二可见块的余项，
不只是将该余项改名或在来源中除 $w^s$。

还可给末 $r$ 项的准确值。写
$$
B=w^r b,\qquad \eta_0=w^{s-r}v.
$$
若 $r=\ell$，$\beta=\pi_r(bv)$；
用 (8)、(18) 逐项得到
$$
\boxed{
\bar Z=\frac3{2a}\mathscr S(B\eta_0^2)\bmod(p,w^s).
}
\tag{26}
$$
这里用了
$\eta_0\beta=\mathscr S(B\eta_0^2)\bmod w^s$。
若 $(r,\ell)=(2,1)$，记
$\beta_1^*=[w](bv)$，则唯一修正为
$$
\boxed{
\bar Z=\frac3{2a}\mathscr S(B\eta_0^2)
+2\lambda\left(\bar\gamma-\frac{\beta_1^*}{a}\right)w^{s-1}
\bmod(p,w^s).
}
\tag{27}
$$
(27) 保同一 $\gamma$，未将缺失的第二低第三行免费补入。

特别，在全部三个允许情形中，
若接触准确为 $s-r$，即 $\lambda=v(0)\ne0$，
则
$$
\boxed{[w^{s-r}]\bar Z=\frac{3b(0)\lambda^2}{2a}\ne0.}
\tag{28}
$$
这个实际非零项处于第二块完成式内部；
它恰被 (23) 的其它完整项抵消。
因此 (28) 本身不被误认作原 $C_2(M)$ 的非零左行。

(24) 也只说 $\bar Z^+$ 的初始段为零。
$\mathscr SZ^+$ 读取的是 $[s,s+\ell)$ 的真正续段，
仍由同一个原 $R$ 决定，不可设成零。

## 6. 全部三块的第二 forcing

现在假定 (21) 已由同一个 (12) 解出。
按原整精度先形成
$$
L_0=\overline{
\frac{\pi_{n_0}(A+pR_0)}{p^2}},
\qquad
L_1=\overline{
\frac{\pi_{n_0}(aB\xi+\mathscr SA+aR_1)}p}.
\tag{29}
$$
这些除法的整性来自第一次提升。
尤其 $\xi$ 在第二式中保原两位；
不能先模 $p$ 再形成 (29)。
(6)–(9) 还给 $L_0,L_1$ 的低 $r$ 行为零，
而第三块的一次商已经在 (19) 严格为零。

令
$$
\Psi=\overline{J_A(P^{\rm crit}+pR)/p^2}.
$$
对 (29) 以外的普通项在所示截断后约化。
准确有
$$
\boxed{
\Psi_0=L_0+
\pi_{n_0}\left(-\frac12B\xi^2-\frac{\xi}{a}\mathscr SA\right),
}
\tag{30}
$$
$$
\boxed{
\Psi_1=L_1+\pi_{n_0}\left(
\frac a2C\xi^2+a\xi R_2+\mathscr SR_0
-\frac1a\mathscr S(\eta_0\mathscr SA)
\right),
}
\tag{31}
$$
$$
\boxed{
\Psi_2=
a\pi_\ell\mathscr SZ^+
+\frac{a^2}{2}\pi_\ell(\xi R_3)
+a\pi_\ell\mathscr S(\eta_0 C\xi).
}
\tag{32}
$$

证明保持 R577 的原 $p^3$ 展开。
第一可见块除 $p^2$ 后为
$L_0+B\xi^2/2+\xi R_1$。
原首提升给 $R_1=-B\xi-\mathscr SA/a\bmod(p,w^{n_0})$，
即得 (30)。

第二块在消元前完整为
$$
L_1+\pi_{n_0}\left(
\frac a2C\xi^2+a\xi R_2+\mathscr SR_0
+\mathscr S\{\eta_0(B\xi+R_1)\}\right).
$$
最后一项是
$\mathscr S(\eta_0Z)-a^{-1}\mathscr S(\eta_0\mathscr SA)$。
(25) 恰好把第一项全部杀掉，得 (31)。
这正是必须先付两条十三行才能完成的加强。

第三块在 (19) 后完整剩下
$$
\pi_\ell\left[
\frac{a^2}{2}\xi R_3+
a\mathscr S(B\xi+C\eta_0\xi)+\mathscr S^2A+
\frac12\mathscr S^2(B\eta_0^2)
+a\mathscr S(R_1+\eta_0R_2)\right].
$$
使用实际 (23) 合并即为 (32)。
没有删除二次 $\eta_0$ 项、高 $\mathscr S^2A$，
也没有把 $R_1,R_2$ 的高值分别另选。
所有丢弃项均由 R577 的
$\operatorname{ord}\eta_0\ge s-r$、
$B,C\in w^r$ 及当前低 $\ell$ 窗超出相应目标；
没有将 raw $\bar\Gamma$ 中的高 normal 项直接置零。证毕。

## 7. 整个第三块只剩实际续段及固定形状项

定义同一个候选的临界形状常数
$$
\kappa_{\rm crit}=(C/B)(0)\in\mathcal O,\qquad
\xi_1=[w]\bar\xi,\qquad
z_j=[w^{s+j}]\bar Z^+.
\tag{33}
$$
$C/B$ 在原点正规，因为两者含相同已付 $w^r$ 因子，
且 $B/w^r$ 是单位。
这里的 $\kappa_{\rm crit}$ 不是 Gaussian 常数。

整个核 (10) 的每条来源都含 $t$，
所以所有其 Euler 值的常数均为零。
而 $R_{\rm bd}$ 只使用 $Y$ 次数 $0,1,2$，
其上有准确算子恒等
$\mathcal E^3=3\mathcal E^2-2\mathcal E$。
故由 (8)，对全部同一实际解都有
$$
\boxed{R_3(0)=\frac{2\alpha_0-6\beta_0}{a}.}
\tag{34}
$$
这不是令较高来源的第三 jet 全部消失；
这里只读取它们由真实 $t$ 因子强迫为零的常数。

由 (4)，$\xi=\xi_1w+O(w^2)$。
又写 $B=w^rb$、$C=w^rc$、$\eta_0=w^{s-r}v$，
则
$$
\beta_0=b(0)v(0),\qquad
c(0)v(0)=\kappa_{\rm crit}\beta_0.
$$
将这些实际等式代入 (32)，得到
$$
\boxed{
\Psi_2=
\begin{cases}
a z_0,&\ell=1,\\[1mm]
a z_0+
a\left[z_1+\xi_1\{
\alpha_0+(\kappa_{\rm crit}-3)\beta_0\}\right]w,
&\ell=2\quad(r=2).
\end{cases}}
\tag{35}
$$
其中 $a,\alpha_0,\beta_0,\kappa_{\rm crit}$ 在剩余域读取。

(35) 是全部第三块，不是只取其一个示意系数。
它准确说明：在原 $\ell=1$ 窗，
第三块只读完成后 $Z^+$ 的下一条真实行；
在 $\ell=2$ 窗，只再加一个已显示的固定形状修正。
所有更高的自由 $R_3$ jet 均因 $\xi(0)=0$ 和长度 $\ell\le2$
超出窗口，但 $z_0,z_1$ 仍是同一个 $R$ 的真实高延拓。
尤其不能因 $\pi_sZ^+=0$ 就把它们也置零。

## 8. 第二次仍是同一个短 Dpsi 的完整像

最后支付 (16) 的全部原列，而不只列必要系数。
在剩余域取
$$
h_0=\pi_r\Psi_0,\qquad h_1=\pi_r\Psi_1,\qquad
h_2^\sharp=\text{将 }\Psi_2\text{ 从长度 }\ell\text{ 零延拓到 }r.
$$
令
$$
y_0=-h_0+\frac{3h_1}{2a}-\frac{h_2^\sharp}{a^2},\quad
y_1=-\frac{2h_1}{a}+\frac{2h_2^\sharp}{a^2},\quad
y_2=\frac{h_1}{2a}-\frac{h_2^\sharp}{a^2}.
$$
按 (7) 的同一实际三列及任意整系数提升，构造
$$
T_{\rm bd}
=\sum_{i=0}^2Y^iq_i
\pi_r^t\left(
\frac{y_i(w(t))}{\psi^iq_i}\right).
\tag{36}
$$
于是
$$
(T_{\rm bd})_0=-\Psi_0\bmod(p,w^r),\quad
a(T_{\rm bd})_1=-\Psi_1\bmod(p,w^r),
$$
$$
\frac{a^2}{2}(T_{\rm bd})_2=-\Psi_2\bmod(p,w^\ell).
\tag{37}
$$
低行之外的全部第二修正恰为 (9) 的同一个核。

用 $w$ frame 写原短矩阵
$$
\mathcal D_\psi^{\rm short}(H)=
(w^{-r}H_0,w^{-r}H_1)\bmod w^{n_0-r},
\qquad H\in\mathcal K_{r,\ell}.
$$
它和 R578 原 $\mathcal D_\psi$ 只差整目标单位与换参。
定义
$$
\boxed{
\mathcal H_P(R)=
-w^{-r}\left(
\Psi_0+(\bar T_{\rm bd})_0,\
a^{-1}\Psi_1+(\bar T_{\rm bd})_1
\right)\bmod w^{n_0-r}.
}
\tag{38}
$$
两个除法由 (37) 保证。

**完整原判据。**
原 $\bar P$ 可提升到 $M(P^{(3)})\in p^3$，
当且仅当存在同一个 $\bar S\in\bar{\mathcal K}_{r,\ell}$ 使
$$
\boxed{
\bar{\mathcal D}_\psi^+(\bar S)=\mathcal G_P^+,
\qquad
\mathcal H_P(R_{\rm bd}+S)
\in\operatorname{im}\bar{\mathcal D}_\psi^{\rm short}.
}
\tag{39}
$$
第一项的 $\gamma$ 按 (10)–(22) 读取；
第二项的 $R$ 必须是同一个解，
全部 $\Psi$ 按 (29)–(35) 计算。

必要性由 (15)、(21)、(16)、(37) 逐步得到。
反向取第一项的实际整提升，
再用第二项选 $T=T_{\rm bd}+H$。
(37) 与 (38) 正给 (16)，而全部 $B$ 行由 (15) 已在 $p^3$ 中，
故得到原完整提升。
放回整个 $c_*U_0$、原行缩放及十三自由行即恢复 (14)。

(39) 不依赖第一解的整提升选择：
若 $S$ 换成 $S+pV$、$V\in\mathcal K_{r,\ell}$，
$Q_2$ 只改变 $p^2V$，
所以 $\Psi$ 加上同一个 $\bar J_A(V)$。
它的低行在 (9) 已为零，
(38) 因而只改变一个
$\bar{\mathcal D}_\psi^{\rm short}(V)$ 像。
这个论证保来源与目标中的同一个修正，
没有在不同精度分别选择互不相容的高尾。

## 9. 新增限制与仍缺的实际非零

本篇的新增输入是：

- 原两条十三行强迫 (15)，使同一两 jet 真正延长十三行，
  并保唯一实际 $Q_{\rm quad}$ 的秩一最高行；
- 对已经相容的同一个 $R$，(24)–(28) 给更高的 $Z$ 消失阶
  及其准确非零末项，从而完整消去第二可见块的旧余尾；
- (32)–(35) 将整个第三块压成同一 $Z^+$ 的一至两条真实续段，
  保固定形状修正，消掉所有未付的自由第三 normal jet；
- (39) 使用两个明确的全来源矩阵给整个原模 $p^3$ 的充要条件。

尚未证明 (39) 的第一指定类不可达，
也未证明在它的实际解空间上第二指定类非零。
(28) 的系数单位没有被冒称为这些真实余核中的单位。
原三条完整中央失败、全部高轴和全局实际范数仍按既有结果保留；
本篇不把同一来源中的有限消元换成新增中央零或全次数容量收益。

下一实际问题已经是 (39) 的这个指定续段与像，
尤其 $\ell=1$ 的 $z_0$ 或 $\ell=2$ 的两行 (35)，
同时满足前两块 (30)–(31) 的相容性。
不能分别满足它们后再把同一个 $R$ 拆开。

## 依赖

- [R577](R577-original-critical-factor-euler-lift-and-complete-first-forcing.md)：
  同格临界整提升、完整原 $p^3$ 三块和真正 $d_2$。
- [R578](R578-complete-critical-boundary-elimination-and-fixed-polar-carry.md)：
  全低行右逆、实际核 (10) 和原短两 jet。
- [R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)：
  原 $w^{13}$ 的完整行带与相对/原 Bockstein 的范围；
  本篇 (13)–(16) 直接保这些整行缩放。
- [R481](R481-full-third-precision-normal-form-and-common-correction.md)：
  全部普通 Euler 值与真正 $s$ 阶移位的第三精度公式。

本篇使用全参数恒等式与实际有限自由来源，没有新增素数扫描。
