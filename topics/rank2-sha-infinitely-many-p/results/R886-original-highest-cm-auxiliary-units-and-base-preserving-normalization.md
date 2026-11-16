# R886. 原最高 CM 分量的共同辅助元、三 Euler 单位与同底归一

日期：2026-11-16。**状态：下列原角色计算、实际 Galois 元、每个深度的辅助素数集合、群环单位和有界归一引理已证明。** 归一引理只作用于已经付清同来源完整范数关系的系统；它不凭 R885 的 n=1 提升制造其它 tame 层。本文也不把一组正密度辅助素数自动替成所有分裂素数，更不由秩一表示的假设直接推出原普通局部化单射。

## 1. 保留原三个端点的四条角色

沿 [R885](R885-original-endpoint-bounded-anticyclotomic-lift-and-unit-specialization.md)，取
$K=\mathbf Q(\omega)$、$\omega^2+\omega+1=0$，
原 $\eta=\eta_{10}$，$(a_4,a_{10},a_{16})=(13,1,7)$，
$\eta_j=\eta^{a_j}$，以及原 $E_0:y^2=x^3+1$ 的 CM 角色
$\psi_0,\bar\psi_0$。其 p-adic 表示角色仍用同名，且
$\mathbf N=\psi_0\bar\psi_0=\varepsilon_{\rm cyc}$。
固定原普通 ray 中一个 $p>211$，选择同一系数整数环 $\mathcal O$ 包含全部原有限角色及 $\omega$。

对于原两槽 $(j,k)=(10,16),(16,4),(4,10)$，
四维表示在 $K$ 上的四个指定分量为
$$
\begin{aligned}
\chi_{jk,0}&=\eta^{3-2a_j-2a_k}\psi_0^3\mathbf N^{-1},\\
\chi_{jk,1}&=\eta^{3+2a_j+2a_k}\bar\psi_0,\\
\chi_{jk,2}&=\eta^{3-2a_j+2a_k}\psi_0,\\
\chi_{jk,3}&=\eta^{3+2a_j-2a_k}\psi_0 .
\end{aligned}
\tag{1}
$$
第一条正是原 $V_\ell=\lambda_\ell/\mathbf N
=\varepsilon_{\rm cyc}\widehat\nu_\ell^{-1}$。
四条有限 $\eta$ 指数准确是
$$
(5,1,15,9),\qquad(17,7,15,9),\qquad(11,13,9,15).
\tag{2}
$$
每个指数都是奇数。后三条仍是原三个 mixed 分量，没有在作范数前删掉。

## 2. 一个真实共同辅助元

存在 $\tau\in G_K$，使
$$
\boxed{\eta(\tau)=-1,\qquad
\psi_0(\tau)=-\omega,\qquad
\bar\psi_0(\tau)=-\omega^2,\qquad
\mathbf N(\tau)=1.}
\tag{3}
$$

证明如下。原 R804 已付 $\eta$ 在十七处惯性上的像为 $\mu_{18}$；
$E_0$ 在十七处良好，所以两条 CM Tate 角色在该惯性上均平凡。
可取 $\tau_{17}$ 使其三值为 $(-1,1,1)$。

$p$ 在 $K$ 中分裂，且 $E_0$ 在这两个 p 位均良好普通。
CM 分裂将 Tate 模分成形式部分与 étale 部分。在 $\mathfrak p$ 的惯性上，两条角色依原选定符号分别为
$(\varepsilon_{\rm cyc},1)$；在 $\bar{\mathfrak p}$ 上为
$(1,\varepsilon_{\rm cyc})$。
每个完备域都是 $\mathbf Q_p$，所以其惯性的 cyclotomic 像为全部
$\mathbf Z_p^\times$。
$\eta$ 的导子与 $p$ 互素，故可分别取这两个惯性中的元，
使三值为 $(1,-\omega,1)$ 和 $(1,1,-\omega^2)$。
它们与 $\tau_{17}$ 的乘积给 (3)。
这里只使用角色像的交换性，不声称三个惯性子群本身交换。

将 (3) 代入全部三个 (1)，统一得到
$$
\boxed{(\chi_{jk,0},\chi_{jk,1},\chi_{jk,2},\chi_{jk,3})(\tau)
=(1,\omega^2,\omega,\omega).}
\tag{4}
$$
例如第一条为 $(-1)(-\omega)^3=1$，不是一个形式指定而未证明存在的 Frobenius 数据。
因 $p\equiv1\pmod3$，上述 $\omega$ 已在 $\mathbf Z_p$ 中；
**不需**再加 $p\equiv1\pmod{54}$ 一类额外条件。

$\mathbf N(\tau)=1$ 还表明 $\tau$ 固定 $K(\mu_{p^\infty})$。
$K$ 的类数为一，单位群为 $\mu_6$，且 $p>3$，所以
$$
K(1)^\circ=K,\qquad
K\bigl(\mu_{p^\infty},(\mathcal O_K^\times)^{1/p^\infty}\bigr)
=K(\mu_{p^\infty}).
\tag{5}
$$
因此 (3) 也固定 (5) 中所需的整个扩张。

## 3. 所有深度的真实辅助素数

令 $H/K$ 为原 $\eta$ 的十八阶扩张。对每个整数 $m\ge1$，
在有限 Galois 扩张
$$
L_m=H\,K(E_0[p^m])
$$
中取 $\tau$ 的像。$H$ 在复共轭下稳定，$E_0$ 定义在 $\mathbf Q$，
所以 $L_m/\mathbf Q$ 也是 Galois。
Chebotarev 定理给正密度的有理素数 $q$，
它们在 $K$ 中分裂，且某个 $\mathfrak q\mid q$ 的 Frobenius 为此像。
删除有限坏素数 $2,3,17,p$ 后仍为正密度。
这些素数满足
$$
q\equiv1\pmod{p^m},\qquad
\eta(\operatorname{Fr}_{\mathfrak q})=-1,\qquad
\psi_0(\operatorname{Fr}_{\mathfrak q})\equiv-\omega,\quad
\bar\psi_0(\operatorname{Fr}_{\mathfrak q})\equiv-\omega^2
\pmod{p^m\mathcal O}.
\tag{6}
$$
固定 Frobenius 方向与原表示；若整体采用相反方向，全部角色同时取逆。
其对群环单位性的结论不变。
选择另一共轭素点只交换两条 CM 根，第一条仍为一，后三条仍为非一的三次单位根。

记 $\mathcal L_m$ 为这样选定、带有 $\mathfrak q$ 的素数集合。
可由同一个 $\tau$ 的各有限像取嵌套的 $\mathcal L_m$。
特别每个深度均有无穷多个合适的辅助素数。
这是对**固定目标 p** 的辅助 q 结论，不能把这句话误读成已解主目标的无穷目标 p。

## 4. 原 p 环类群及兼容 Frobenius lift

对平方自由整数 $n$，其素因子分裂且避开 $6p$，
记 $K[n]$ 为导子 $n$ 环类域的最大 p 子扩张，
$G_n=\operatorname{Gal}(K[n]/K)$。
由类数一、$\#\mathcal O_K^\times=6$ 与 CRT，环类精确序列的 p 部分给
$$
\boxed{G_n\simeq\prod_{q\mid n}G_q,\qquad
G_q\simeq\bigl((\mathcal O_K/q)^\times/(\mathbf Z/q)^\times\bigr)^{(p)},
\quad \#G_q=p^{v_p(q-1)}.}
\tag{7}
$$
因此所有这些有限扩张确实线性不交。
反循环 $\mathbf Z_p$ 扩张 $K_\infty/K$ 只在 p 处分歧，
而 $K[n]/K$ 在 p 处不分歧。
其交域处处不分歧，仍因类数一为 $K$。
故同时有
$$
\operatorname{Gal}(K[n]K_\infty/K)\simeq G_n\times\Gamma.
\tag{8}
$$

在由这些扩张组成的直积塔中，对每个 $q\in\mathcal L_1$ 一次选定
$\sigma_q$：其在 $G_q$ 上的分量为一；
在每个 $G_l$、$l\ne q$ 上取真实的 $\operatorname{Fr}_{\mathfrak q}^{-1}$；
在 $\Gamma$ 上也取真实的未分歧 $\operatorname{Fr}_{\mathfrak q}^{-1}$。
(7)–(8) 证明此选择存在且在所有投影下兼容。
当 $q\nmid n$ 时，它在 $G_n\times\Gamma$ 上就是范数式中的真实 Frobenius；
当 $q\mid n$ 时，其 q 分量只是已经明确固定的 lift。
没有在一个分歧层把未定义的 Frobenius 当成天然元。

## 5. 三个额外 Euler 因子是实际群环单位

按原范数约定定义
$$
P_{jk,\mathfrak q}(X)
=\det\bigl(1-\operatorname{Fr}_{\mathfrak q}^{-1}X
       \mid T_{jk}^{\vee}(1)\bigr)
=P_{0,\mathfrak q}(X)\,Q_{jk,\mathfrak q}(X),
\tag{9}
$$
其中 $P_0$ 是 (1) 第一条的线性因子，$Q$ 包含原后三个因子。
若使用算术 Frobenius，四个内部特征值可写为
$\chi_{jk,i}(\operatorname{Fr}_{\mathfrak q})/q$；
也可直接坚持 (9) 的定义避免混用互反规范。

对 (6) 的 $q$，(4) 与 $q\equiv1\pmod p$ 给
$$
\boxed{Q_{jk,\mathfrak q}(1)\in\mathcal O^\times.}
\tag{10}
$$
模极大理想，三个因子为 $1-\omega^2,1-\omega,1-\omega$，
或同时交换 $\omega,\omega^2$。
它们都是单位，因为 $\omega\ne1\bmod p$，$p>3$。

现在对任一 $n$，
$\mathcal O[G_n]$ 是完备局部环，其极大理想由 $\mathcal O$ 的极大理想与 augmentation ideal 生成。
同样，$\Lambda[G_n]=\mathcal O[[\Gamma]][G_n]$ 的极大理想还包含 $\gamma-1$。
所以 (10) 准确推出
$$
\boxed{
Q_{jk,\mathfrak q}(\sigma_q|_{G_n})\in\mathcal O[G_n]^\times,\qquad
Q_{jk,\mathfrak q}(\sigma_q|_{G_n\times\Gamma})\in\Lambda[G_n]^\times .
}
\tag{11}
$$
这是完整群环及 Iwasawa 群环中的单位结论，不仅是某一个数值特化。
全部非平凡原有限角色已在 (1) 中处理。

## 6. 同底、有界的降因子引理

设已经给出同来源的一族类 $z_n$，其中 $n$ 的每个素因子均属于 $\mathcal L_1$，
且这族类在某一固定格上整，或只需要一个与 $n$ 无关的固定分母。
假定它们的完整原范数关系已经证为
$$
\operatorname{cor}_{K[nq]/K[n]}z_{nq}
=P_{0,\mathfrak q}(\operatorname{Fr}_{\mathfrak q}^{-1})
 Q_{jk,\mathfrak q}(\operatorname{Fr}_{\mathfrak q}^{-1})z_n.
\tag{12}
$$
这里 $z_n$ 是投向原最高分量后的**同一个**类，
仍带四维来源的全四因子。
可同样在 wild 塔写 (12)；但必须先有真实同源 wild 系统。

令
$$
u_n=\prod_{q\mid n}Q_{jk,\mathfrak q}(\sigma_q|_{G_n}),
\qquad
c_n=u_n^{-1}z_n.
\tag{13}
$$
wild 情形改用 $G_n\times\Gamma$。
(11) 保证 (13) 在原格上合法，完全不产生随层数增长的 p 分母。
空乘积为一，所以
$$
\boxed{c_1=z_1.}
\tag{14}
$$

对 $q\nmid n$，群环投影准确给
$$
\operatorname{pr}_{nq,n}(u_{nq})
=u_nQ_{jk,\mathfrak q}(\operatorname{Fr}_{\mathfrak q}^{-1}).
$$
corestriction 对这些投影等变；将 (12) 代入，合法消去的都是 (11) 的真单位，
从而得到
$$
\boxed{\operatorname{cor}_{K[nq]/K[n]}c_{nq}
=P_{0,\mathfrak q}(\operatorname{Fr}_{\mathfrak q}^{-1})c_n.}
\tag{15}
$$
此证明保留整个原最低层类，包括它原有的 q/q⁴、系数、Artin 和旧副本归一；
不只保留“某个非零比例”。
固定的 Galois 稳定局部条件也被 (13) 保持，
因为它们是闭的群环子模，单位的逆仍在同一个整群环或完备群环中。

(15) 目前是一族在明确辅助集合 $\mathcal L_1$ 上的秩一范数关系。
若要引用只对所有良好分裂素数陈述的 Euler-system 定理，
仍须核实其允许的辅助集合假设；
不能把“正密度”本身当作该核验。
也没有证明任意别的 q 上的三个因子都是单位。

## 7. 原秩一表示自己的 HW、HS、HO 与有限层替代元

原四维表示可约，不能直接套用 ACR 的绝对不可约假设。
对 (1) 指定的秩一 $T_\ell=\mathcal O(\chi_{jk,0})$，
这些**表示和局部条件假设本身**却可逐项支付：

- $T_\ell$ 及其残余均一维，故绝对不可约。
- ACR §8.1 的 HW(2)、HS(2') 对秩一格可取恒等元：
  $T_\ell/(1-1)T_\ell=T_\ell$ 为秩一自由模，且该元固定要求的全部扩张。
- 取上面 $\tau_{17}$；(1)–(2) 给 $\chi_{jk,0}(\tau_{17})=-1$，
  因此作用标量及其减一都是单位，满足 HS(3')。
- 原 $\eta^c=\eta^{-1}$、$\psi_0^c=\bar\psi_0$ 准确给
  $\chi_{jk,0}\chi_{jk,0}^c=\mathbf N$。
  在 rank-one 标准格上乘法定义完美对称配对
  $T_\ell\times T_\ell\to\mathcal O(1)$，
  第二输入按共轭作用；这支付 HS(4')。
- 最高原符号在 $\mathfrak p$ 的 balanced 条件为全局部群，
  在 $\bar{\mathfrak p}$ 为零。
  这两个条件在共轭局部 Tate 配对下互为正交补，在所有有限塔层仍如此，
  支付 HO。

此外 $\tau_{17}$ 在十七处惯性，而 (5) 的扩张在十七处不分歧；
故它固定 (5)，在 $V_\ell$ 上减一可逆。
这正支付 ACR Remark 8.4 所列的**表示端替代门**，
可在满足其其余 Euler-system 条件时替代要求 wild 延拓的门。
本段没有把尚未建立的系统、底类非零或允许辅助集合一并当作已知。

即使未来由合法秩一 Euler-system 定理得到一个 balanced Selmer 群为秩一，
它本身也不等于“原 ordinary localization 在该群上单射”。
原底类非零、原 $\mathscr D_{\ell,p}(0)$ 非零以及通常全 Sha 的结论仍须分别证明。

## 8. 当前接口与引用

[R885](R885-original-endpoint-bounded-anticyclotomic-lift-and-unit-specialization.md)
已构造原底类的真实有界 wild 提升及准确单位特殊化。
本文不擅自为它填入未证明的 tame 系统。
另一条直接从 ACR 权 (2,2,2) small diagonal 构造原有限层系统的路线，
也必须先付同 $C_{02,\ell}$ 的 n=1 来源、所有层的范数和统一分母，
之后才可使用 (13)–(15)。

表示条件和局部条件的原文位置：
Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL₂×GL₂*，
[正式刊本](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)，
§8.1 的 HW、HS、HO，Definition 8.1，Theorems 8.3、8.5 及 Remark 8.4。
原角色、十七惯性和 CM 局部符号来自本仓库 R804、R806、R826、R832、R885。
上面共同辅助元、全部三个原输入的单位计算、兼容 lift 与同底归一均已在本文直接证明。

没有数学程序执行、目标素数扫描或新的数值证书。
