# R1002 — 三个 beta27 的 Katz 值在每个好分裂素数非零

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

**已证明。** 对 R991、R994 的三个完整角色
$\beta_{27,j}=\psi_{27}\eta_j$，$j=4,10,16$，以及每个在
$K=\mathbf Q(\sqrt{-3})$ 中分裂的有理素数 $p$，其 primitive
Katz 值在本篇指定的普通 CM 型处非零。结论对每个系数素位成立。
它使用 R994 已付的三个严格完整复中央值，不重新运行该计算。

本篇还给新 weight3 Rankin 输入的两个准确 Katz 角色、保持全部
2/3/17 型的经典权族，以及经典插值处的完整 $p$-Euler 恒等式。
这些角色恒等式不单独声称 R997 的实际 CM 图 trace 已与某个
全球 toric period 相等；该比较中 full9 的 connected component
必须另外落实。

## 1. 角色、素位与周期的固定规范

固定 R991 的

$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,
\qquad \delta=1+2\omega,
\qquad E_{27}:y^2+y=x^3.
\tag{1}
$$

用理想角色规范：$\psi=\psi_{27}$ 的 infinity type 为 $(1,0)$，
且对素于3的主理想

$$
\psi((a))=\epsilon(a)^{-1}a,
\qquad a\equiv\epsilon(a)\pmod3,
\quad\epsilon(a)\in\mu_6.
\tag{2}
$$

原 $\eta_j$ 一律不改；其系数域可取 $\mathbf Q(\zeta_{18})$，
其导子是 $(34)$，且 $\eta_j^c=\eta_j^{-1}$。
由 R991 的完整单位表，

$$
\mathfrak f_{\beta_j}=(34\delta^2),\qquad
\beta_j\beta_j^c=N_K,
\qquad \beta_j:=\psi\eta_j.
\tag{3}
$$

这里 $N_K(\mathfrak a)=\mathrm N\mathfrak a$。上标 $c$ 是在
理想或 idèle 的自变量上作真正的 $K/\mathbf Q$ 共轭；它不是
在 $\mathbf C_p$ 上任取一个所谓复共轭。

设 $p=\mathfrak p\bar{\mathfrak p}$，并固定系数域到
$\overline{\mathbf Q}_p$ 的嵌入，$\mathfrak p$ 是该嵌入在 $K$
上给出的素位。分裂素数都满足 $p\equiv1\pmod3$，所以
$p\nmid2\cdot3\cdot17$。$E_{27}$ 在这些素数有好普通约化，
三个 $\beta_j$ 均在 $p$ 上不分歧。

为明确周期，使用 Castella [C, §2.1.2、Theorem2.2.1] 的规范。
选 $E_{27}$ 的非零代数微分 $\omega_E=dx/(2y+1)$，固定非零
Betti 周期，记 raw CM period 为 $\Omega\in\mathbf C^\times$，
而 $q$-模形式的周期为

$$
\Omega_K=\frac{\Omega}{2\pi i}.
\tag{4}
$$

在普通形式群上选一个 Igusa 平凡化
$\iota_p:\widehat E_{27}\simeq\widehat{\mathbf G}_m$，定义

$$
\omega_E=\Omega_p\,\iota_p^*(du/u).
\tag{5}
$$

这里 $\Omega_p\ne0$；对上述最小整微分可取
$\Omega_p\in\mathcal O_{\mathbf C_p}^{\times}$。
更换微分使 $\Omega$ 与 $\Omega_p$ 同乘一个非零代数数。
不得把(4)中的 $\Omega_K$ 与 $\Omega$ 混成同一个符号后消去
$2\pi i$。以下精确等式以(4)–(5)及 [C] 的 Katz 规范为准。

令 $\mathfrak c=(34\delta^2)$。记
$\mathscr K_{p,\mathfrak c}(\nu)$ 为在理想角色参数 $\nu$ 下的
Katz 函数；它对应 [C, Theorem2.2.1] 的参数
$\xi=\nu^{-1}$。在 $\nu$ 的 infinity type 为
$(a,b)$、$a\ge1,b\le0$，且 $\nu$ 在 $p$ 不分歧时，其规范是

$$
\frac{\mathscr K_{p,\mathfrak c}(\nu)}{\Omega_p^{a-b}}
=\iota_p\left[
\left(\frac{\sqrt3}{2\pi}\right)^b
(a-1)!
\left(1-\frac{\nu(\mathfrak p)}p\right)
\left(1-\nu(\bar{\mathfrak p})^{-1}\right)
\frac{L_{\mathfrak c}(\nu^{-1},0)}{\Omega^{a-b}}
\right].
\tag{6}
$$

方括号是 Katz 插值定理给出的代数数，再经固定嵌入进入
$\mathbf C_p$；不把任意复数直接“代入” $p$-adic 域。
由于参数在 $p$ 不分歧，$p$ 处 Gauss factor 为1。
选择不同的允许周期规范只会同乘明确的非零因子，不改变以下
非零结论。本文不使用 [C] 的高权 Heegner 非零定理。

## 2. 每个分裂素数的非零定理

**定理。** 在(1)–(6)的规范下，对全部 $p\equiv1\pmod3$ 和
$j=4,10,16$，

$$
\boxed{
\mathscr K_{p,\mathfrak c}(\beta_j)
=\Omega_p\,
\iota_p\left[
\left(1-\beta_j(\bar{\mathfrak p})^{-1}\right)^2
\frac{L(\beta_j,1)}{\Omega}
\right]\ne0.}
\tag{7}
$$

**证明。** 先由(3)在每个好理想处逐个核 Euler factor，得到

$$
\beta_j^{-1}=\beta_j^cN_K^{-1},
\qquad
L(\beta_j^{-1},0)=L(\beta_j^c,1)=L(\beta_j,1).
\tag{8}
$$

最后一个等式由 $\mathfrak a\mapsto\bar{\mathfrak a}$ 重排全部
理想得到，不是只比较无穷型。$\mathfrak c$ 正是完整导子；
所有被模数移去的坏 Euler factor 原本就是1，所以这里
$L_{\mathfrak c}=L$。

由 $\beta_j(\mathfrak p)\beta_j(\bar{\mathfrak p})=p$，
两个普通 Euler 因子准确相同：

$$
1-\beta_j(\mathfrak p)/p
=1-\beta_j(\bar{\mathfrak p})^{-1}.
\tag{9}
$$

R994 已严格证明三个完整 $L(\beta_j,1)>0$。
由于 $\Omega\ne0$，(7)中的复代数化值非零。
此外 $\beta_j(\bar{\mathfrak p})$ 是 $\psi$ 的 CM Frobenius
值乘一个有限阶单位，故在每个复嵌入下

$$
\left|\beta_j(\bar{\mathfrak p})\right|=\sqrt p>1.
\tag{10}
$$

所以这个代数数不等于1，其任何 $p$-adic 嵌入也不可能等于1。
因此(9)不为零。将 $(a,b)=(1,0)$ 代入(6)，阶乘及
$\sqrt3/(2\pi)$ 的幂都为1，由(8)–(9)即得(7)。所有代数
嵌入均为单射，且(5)非零，所以结论对每个系数素位成立。
$\square$

此处没有使用 ordinary Selmer 的维数、$p$-adic 高度非退化或
任何 AJ 注入性。也没有声称 Euler factor 在所有 $p$ 都是整单位：
本证明只需要并已经给出其严格非零。

## 3. 新 weight3 输入的两个 Katz 角色仍是原 nu 与 beta27

保持 R991 的 $\psi^3=\psi_0^3$，定义

$$
\chi_{0,j}=\eta_j\psi^{-1}N_K^2
=\eta_j\psi\bar\psi^2.
\tag{11}
$$

其 infinity type 为 $(1,2)$。新形式是
$f_{27}=\theta(\psi^2)$，权为3。Rankin 分解需要的两个 Katz
参数不是两个任意同无穷型角色，而是

$$
\begin{aligned}
\psi^{-2}\chi_{0,j}
&=\eta_j\psi^{-1}\bar\psi^2
=\boxed{\nu_j},\\
\bar\psi^{-2}\chi_{0,j}
&=\boxed{\psi\eta_j=\beta_j}.
\end{aligned}
\tag{12}
$$

第一行恰是 R811、R817 等使用的原 $\nu_j$。确实若
$\psi=\kappa\psi_0$，则 $\bar\kappa=\kappa^{-1}$、
$\kappa^3=1$，所以第一行的有限 twist 额外因子是
$\kappa^{-1}\bar\kappa^2=\kappa^{-3}=1$。
这包括 wild3，不能只因两个无穷型相同就删掉该核验。

原 $\nu_j$ 的 type 为 $(-1,2)$，不在(6)的经典插值区域；
而 $\beta_j$ 的 type 为 $(1,0)$，在其中。因此第2节的证明
没有给出原 $\mathscr K_p(\nu_j)$ 的跨 $p$ 非零。

## 4. 保全部有限型的经典权族

取整数 $m\ge0$ 且 $m\equiv-2\pmod6$，定义

$$
\begin{aligned}
\chi_{m,j}&=\eta_j\psi^{m+3}\bar\psi^{-m},\\
\nu_{1,j}(m)&=\psi^{-2}\chi_{m,j}
=\eta_j\psi^{m+1}\bar\psi^{-m},\\
\nu_{2,j}(m)&=\bar\psi^{-2}\chi_{m,j}
=\eta_j\psi^{m+3}\bar\psi^{-m-2}.
\end{aligned}
\tag{13}
$$

二者的 type 分别为 $(m+1,-m)$ 与 $(m+3,-m-2)$，都在
经典 Katz 区域，并均满足 $\nu_i(m)\nu_i(m)^c=N_K$。
在 $m=-2$ 时，(13)精确成为(11)–(12)。

以下核有限型，不仅核 type。写 $\nu=\psi N_K^{-1/2}$ 为
unitary 角色，并把 Hsieh 的 toric 积分角色取为

$$
\xi_{m,j}=\chi_{m,j}^{-1}N_K^{3/2}
=\eta_j^{-1}\nu^{-(2m+3)}.
\tag{14}
$$

其逆是实际向量所需的 torus 特征。由 R991 的完整表，2、17处
$\nu$ 在单位上平凡，故全部有限 ramified 单位型始终是原
$\eta_j$ 型。3处 $\nu(u)=u$ 对 $u\in\mu_6$，且
$\nu(\delta)=i$、$\eta_j(\delta)=-1$。
若 $m=6r-2$，则 $2m+3=12r-1$，于是

$$
\xi_{m,j}^{-1}|_{K_3^\times}
=\eta_j\nu^{-1}|_{K_3^\times}
=\chi_{27,j,3}.
\tag{15}
$$

式(15)同时核了 $\mu_6$ 与 $\delta$，主单位由导子给出。
2、17的中心 uniformizer 值也保持为 $-1$，因为 $2m+3$ 为奇数。
这正是 R991 的全部有限 toric 角色，而非只保其导子。

两个 Katz 因子在3处的单位指数分别为 $2m+1\equiv3\pmod6$
与 $2m+5\equiv1\pmod6$；故其完整导子分别为

$$
\mathfrak f_{\nu_{1,j}(m)}=(34\delta),
\qquad
\mathfrak f_{\nu_{2,j}(m)}=(34\delta^2).
\tag{16}
$$

在统一模数 $\mathfrak c$ 中使用第一个角色不多丢一个非平凡
Euler factor，因为它已经在 $\delta$ 分歧。

固定一个分裂 $p$ 后，可在更小的权分支
$m\equiv-2\pmod{6(p-1)}$ 上工作。特别

$$
m_n=-2+6(p-1)p^n\quad(n\ge0)
\tag{17}
$$

都是经典非负权且 $p$-adically 趋于 $-2$。所有固定的
prime-to-$p$ 代数单位的这些幂连续变化；(17)不允许把非单位
$p^{m_n}$ 的实整数表达式直接解释成 $p^{-2}$。

## 5. 经典插值中的两个完整 p-Euler 因子

对(13)的任一经典权，令

$$
e_{i,p}(m)=1-\nu_{i,j}(m)(\bar{\mathfrak p})^{-1}.
\tag{18}
$$

由(6)及 $\nu_i\nu_i^c=N_K$，两个 Katz 插值式的乘积准确是

$$
\begin{aligned}
\frac{
\mathscr K_{p,\mathfrak c}(\nu_{1,j}(m))
\mathscr K_{p,\mathfrak c}(\nu_{2,j}(m))
}{\Omega_p^{4m+6}}
={}&\iota_p\left[
\left(\frac{2\pi}{\sqrt3}\right)^{2m+2}
m!(m+2)!\ e_{1,p}(m)^2e_{2,p}(m)^2\right.\\
&\left.\hspace{9mm}\cdot
\frac{
L(\psi^2\chi_{m,j}^{-1},0)
L(\bar\psi^2\chi_{m,j}^{-1},0)
}{\Omega^{4m+6}}
\right].
\end{aligned}
\tag{19}
$$

该式全部是经典插值处的等式；没有先假定 Rankin/几何比较。
在 split $p$ 的 Kirillov 模型中，把第一对角坐标对应
$\bar{\mathfrak p}$，取 $p$-depleted 向量
$W^\flat(d(a))=1_{\mathbf Z_p^\times}(a)$。
它的局部 zeta integral 为1。
Hsieh [H, Lemma3.4、Proposition3.5] 的 split 局部计算于是给

$$
\frac{P_p(W^\flat,W^\flat,\xi_{m,j})}
{L(1/2,\pi_{K,p}\otimes\xi_{m,j})}
=L(1/2,\pi_p\otimes\xi_{m,j,\bar{\mathfrak p}})^{-2}
=e_{1,p}(m)^2e_{2,p}(m)^2.
\tag{20}
$$

这里 $\pi=\mathrm{AI}(\nu^2)$；两个 unramified Satake 值是
$\psi(\bar{\mathfrak p})^2/p$ 与
$\bar\psi(\bar{\mathfrak p})^2/p$。将(14)代入中心 $s=1/2$，
恰得到 $1-\psi^2\chi_m^{-1}(\bar{\mathfrak p})$ 及其共轭
因子，即(18)。加性角色 conductor0、$d_{\mathbf Q_p}=1$，
相关 epsilon 值及单位项为1。

式(20)说明全球比较若沿这个普通方向实行，$p$ 处所有可能含
非单位 $p^m$ 的因子都必须在经典权时与(19)逐项抵消。
只有抵消后的常数才可沿(17)延拓。若交换两个对角坐标，得到的
是另一个 CM/普通方向，不能保留(18)不变。

## 6. 对当前实际图计算的准确意义

Hsieh [H, Proposition2.1] 的一般 Waldspurger 公式允许任意
unitary 中心角色和本题的 CM base change；它不含该文后续
Theorem A 的 $n^-$ square-free 假设。
所以实际3处 conductor27并不排除使用这一**一般**公式。
这不等于可直接使用其 Theorem A 或 BDP 的 cyclic-conductor
全球 Heegner 公式。

从(7)已经得到：在任何随后完整建立且非零常数已付的
“实际最高 AJ 平方 = 原 $\mathscr K_p(\nu_j)$ 乘
$\mathscr K_p(\beta_j)$”公式中，第二个因子在每个分裂 $p$
都不会造成零点。需要解决的原 $\nu_j$ 因子没有被改成另一
个有限角色，也没有被第2节的经典插值结论代替。

对接 R997 时，还须逐项保持 full9 connected component、
$P_+^{\mathrm t}=P_-$、原 $H$ 的 $1/18$ trace、54条真实图及
两处 CM 素位。相关未完成的全球接线在同会话的独占工作笔记
继续推进；本篇已证的是第2节的无条件非零定理及(12)–(20)
的精确角色/Euler 等式。

## 来源

- [C] Francesc Castella，*Tamagawa number conjecture for CM modular
  forms and Rankin–Selberg convolutions*，Proc. London Math. Soc.
  **131** (2025), e70089；本篇调用 §2.1.2 的周期规范与
  Theorem2.2.1 的 Katz 插值。
  [作者公开稿](https://web.math.ucsb.edu/~castella/Katz.pdf)。
- [BDP] M. Bertolini、H. Darmon、K. Prasanna，*p-adic Rankin
  L-series and rational points on CM elliptic curves*，Pacific
  J. Math. **260** (2012), 261–303，§2D、Theorem3.1、
  Proposition3.5；其 Lemma3.14/后续全球分解另有 cyclic
  conductor 假设，本篇不越过该假设。
  [作者公开版](https://www.math.mcgill.ca/darmon/pub/Articles/Research/52.BDP2/bdp-pjm.pdf)。
- [H] Ming-Lun Hsieh，*Special values of anticyclotomic
  Rankin–Selberg L-functions*，Documenta Math. **19** (2014),
  709–767，Proposition2.1、Lemma3.4、Proposition3.5。
  [出版社全文](https://content.ems.press/assets/public/full-texts/serials/dm/19/8965392/online/10.4171-dm-462.pdf)。
- R991：完整 $\psi_{27},\eta_j$、三个 cubic twists 与2/3/17型；
  R994：三个严格完整中央值；R995、R997–R998：最高 Chow 投影、
  实际局部 AJ 公式及混合 full Bloch–Kato 消失。
