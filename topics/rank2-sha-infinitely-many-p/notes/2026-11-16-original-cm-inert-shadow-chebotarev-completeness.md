# 原 CM 最高循环的惯性 shadow 检测完备性

日期：2026-11-16。**本注证明：固定系数素数 $\ell>3$ 后，同一个原二维 CM 动机上的有理 étale AJ 非零，当且仅当 R859 的某个惯性约化 shadow 的 $\ell$ 部分非零；若非零，则这些 shadow 的 $\ell$ 阶无界。它不证明原 AJ 非零，也不把变化的约化素数 $r$ 当成主目标中变化的系数素数 $p$。**

本注沿 [R859](../results/R859-original-supersingular-shadow-and-integral-aj-detection.md) 的原循环、真实 $H_{34}$ 平凡化和全部整除子规范。不套 full-GSp 的算法终止定理；这里用原 CM 表示自含证明所需的 Chebotarev 结论。

## 1. 必须先用原来的 Q 下降二维类

固定原一个 $j\in\{4,10,16\}$，取
$$
K=\mathbf Q(\omega),\quad H=H_{34},\quad
\lambda_j=\eta_j^{-1}\psi_0^3.
$$
令 $L/\mathbf Q_\ell$ 为一个含原系数域嵌入的有限扩张，$\mathcal O$ 为其整数环。
令
$$
V=V_{\lambda_j,\ell}(2),\qquad
\rho:G_{\mathbf Q}\longrightarrow\operatorname{GL}_L(V),
\qquad
z=AJ_\ell(Z_{{\rm orig},j})\in H^1(\mathbf Q,V).
\tag{1}
$$
这里是 R832、R858附B中已经下降到 $\mathbf Q$ 的原**两条共轭 CM 线之和**。
只取 $H$ 上一个任意 $\chi$-sector 类，不足以供下面的 $G_{\mathbf Q}$ 稳定性论证。

在 $H$ 上用同一原 Artin–CM 对应平凡化，得到
$$
\theta:V|_{G_H}\xrightarrow{\sim}
 \bigl(H_+^{\otimes3}\oplus H_-^{\otimes3}\bigr)(2).
\tag{2}
$$
这是 R832 的真正 $h^1$ 同构的张量，不替换原类。
R859 的整循环 $\widetilde{\mathcal Z}=D\,\theta_*(Z_{{\rm orig},j}|_H)$
保全部 Hecke 提取、$q_0/q_2$、Artin 系数和清分母整数 $D$。

$H/\mathbf Q$ 是正常扩张。因为有限 $\eta_j$ 在 $H$ 上平凡，(2)是
实际最高块；不是另一个具有同 Frobenius 多项式的任意表示。
以 R859 的几何 Frobenius 约定，
$$
\det V=\chi_\ell,\qquad
\rho(\iota)^2=1,\qquad
\operatorname{Spec}\rho(\iota)=\{1,-1\},
\tag{3}
$$
其中 $\iota$ 是复共轭，$\chi_\ell$ 是圆分特征。
例如 $H^1(E_0)$ 的 determinant 为 $\chi_\ell^{-1}$，
故两条立方 CM 线的 determinant 为 $\chi_\ell^{-3}$；
Tate twist2给 $\chi_\ell^4$，得到(3)。

## 2. 原 CM 表示的两项群论输入

需要的两项事实是
$$
\boxed{V\text{ 绝对不可约； }\ \rho(G_{\mathbf Q})\text{ 含一个 }
uI,\ u\ne1.}
\tag{4}
$$
这里可直接从原 $E_0$ 的 CM reciprocity 支付，不需要非 CM 大像假设。

对 $E_0/K$，CM type 的 reflex norm 是 $K$ 的恒等映射。
在有限 idèle 中取 $\ell$-分量为一个充分接近1的单位，其余分量为1。
CM 主定理使其 Artin 元在全 Tate 模上的作用等于该单位，
至多差一个 $\mathcal O_K^\times=\mu_6$ 因子：
更精确地，主定理的准同源 $\lambda\in K^\times$ 与该有限单位 idèle
的合成保持每个整 Tate 格，故
$\lambda\in K^\times\cap\widehat{\mathcal O}_K^\times
=\mathcal O_K^\times=\mu_6$。不能仅凭其有理 degree 为1就称其为自同构。
取六次幂消去这个有限因子，再取十八次幂使其固定 $H$。
因此有理主单位 $t\in1+\ell^a\mathbf Z_\ell$ 的非零固定幂
给 $G_H$ 在 $H^1(E_0)$ 上的非平凡 scalar。
若该 scalar 为 $v$，cup pairing给 $\chi_\ell=v^{-2}$，
所以在(2)上的 scalar准确为
$$
v^3\chi_\ell^2=v^{-1}\ne1.
\tag{5}
$$
它当然在整个 $\rho(G_{\mathbf Q})$ 中为中心。

同样在 $\mathcal O_K\otimes\mathbf Z_\ell$ 中选一个主单位 $t$
使 $t/\bar t$ 不为根单位。
$\ell$ split 时可在两分量分别取 $1+\ell^a,1$；
$\ell$ inert 时可取充分接近1、非共轭不变的单位。
$\ell>3$ 时主单位群无非平凡有限阶元。
这给 $G_H$ 上两个 CM 角色之比的非平凡无穷像，故两角色不同；
复共轭交换这两条线，得到绝对不可约性。
本段所用 CM 主定理及其有限 idèle 规范见
[Milne, Complex Multiplication, Theorem3.10与Remark3.11](https://www.jmilne.org/math/articles/2007c.pdf)，
不是把系数域自同构计入 point-factor Galois 作用。

## 3. 非零 AJ 在表示核上留下真实平移

设 $\Gamma=\rho(G_{\mathbf Q})$。中心 scalar 的以下作用可直接算出：
对任意连续 cocycle $b:\Gamma\to V$ 及 $uI\in\Gamma$，
$$
b(u\gamma)=b(u)+u\,b(\gamma)
=b(\gamma)+\gamma b(u),
$$
从而
$$
(u-1)b(\gamma)=(\gamma-1)b(u).
\tag{6}
$$
因为 $u-1\ne0$ 在 $L$ 中可逆，$b$ 是 coboundary。
所以
$$
H^1(\Gamma,V)=0.
\tag{7}
$$
这是所需的 Sah 型论证的全部内容，未要求 $u-1$ 为 $\mathcal O$ 单位。

现在假设 $z\ne0$，取其连续 cocycle 代表 $c$。
若 $c$ 在 $\ker\rho$ 上为零，它就下降为 $\Gamma$ 上的 cocycle，
和(7)矛盾。因此其在 $\ker\rho$ 上的同态非零。
置
$$
N=\ker\rho\cap G_H.
\tag{8}
$$
$N$ 在 $\ker\rho$ 中为有限指标。
若 $c|_N=0$，任一 $h\in\ker\rho$ 的某个正整数次幂属于 $N$，
而 $c(h^a)=a\,c(h)$，故特征零中仍会有 $c|_{\ker\rho}=0$。
因此 $c|_N\ne0$。

$N$ 是 $G_{\mathbf Q}$ 的正常子群，且对 $h\in N$，
$$
c(\gamma h\gamma^{-1})=\rho(\gamma)c(h).
\tag{9}
$$
所以 $c(N)$ 的 $L$-线性包是一个非零 $G_{\mathbf Q}$ 子空间。
由(4)，
$$
\boxed{\operatorname{span}_L c(N)=V.}
\tag{10}
$$
这里没有只在 $G_H$ 的一个角色线上偷偷使用全局不可约性。

## 4. 真正惯性 coset 中的平方

所有格与清分母成本都可在此一次性固定。
选一个 $G_{\mathbf Q}$ 稳定 $\mathcal O$ 格 $T_0\subset V$。
连续 cocycle 的像紧，故乘一个固定非零整数后可使 $c$ 取值于 $T_0$。
$\theta(T_0)$ 与 R859 的最高整格 $T_{\rm top}$ 可公度；
这个固定成本与后面的 $r,n$ 无关。

令 $C=\rho(\iota)$。由 $c(\iota^2)=0$，有 $(1+C)c(\iota)=0$。
因2为单位，加上 coboundary $\delta(c(\iota)/2)$ 后可准确令
$$
c(\iota)=0.
\tag{11}
$$
这个改变不影响 $c|_N$。
由(10)，可选 $h\in N$ 使
$$
w=(1+C)c(h)\ne0.
\tag{12}
$$
置 $g=\iota h$。它位于 $G_{\mathbf Q}\setminus G_K$，且
$$
\rho(g)=C,\qquad \rho(g^2)=1,\qquad \chi_\ell(g)=-1.
\tag{13}
$$
最后一式来自 $\rho(h)=1$ 及(3)，不是额外选定的局部角色。
cocycle 的平方公式给
$$
\boxed{c(g^2)=(1+C)c(h)=w\ne0.}
\tag{14}
$$
即使再次改变 cocycle 代表，(14)的值也不变，因为 $\rho(g^2)=1$。

## 5. 在真正联合扩张中使用 Chebotarev

把原表示和实际 cocycle 合成一个连续整表示
$$
\widetilde\rho(\gamma)=
\begin{pmatrix}\rho(\gamma)&c(\gamma)\\0&1\end{pmatrix}.
\tag{15}
$$
对每个正整数 $n$，取由以下有限资料共同截出的有限 Galois 扩张：
$$
\widetilde\rho\bmod\ell^n,\qquad
\chi_\ell\bmod\ell^n,\qquad
G_{\mathbf Q}\longrightarrow\operatorname{Gal}(H/\mathbf Q).
\tag{16}
$$
这些资料来自同一个原 AJ cocycle，不是一个自由加入的平移参数。
Chebotarev 对 $g$ 的像的共轭类给一组正密度有理素数 $r$；
使用几何 Frobenius 时取相应逆共轭类即可，密度不变。
删去原模型的有限坏集、$\ell$、2、3、17后仍有正密度。
于是可以取
$$
r\equiv2\bmod3,\qquad r\equiv-1\bmod\ell^n,
\tag{17}
$$
且某个 Frobenius 代表 $f_r$ 在(16)中与 $g$ 共轭。

必须保留共轭带来的 cocycle 项。
对任意 $\gamma,s$，
$$
c(\gamma s\gamma^{-1})
=\rho(\gamma)c(s)+
  (1-\rho(\gamma s\gamma^{-1}))c(\gamma).
\tag{18}
$$
以 $s=g^2$ 代入，第二项准确为零；对与之模 $\ell^n$ 相同的
$f_r^2$，第二项属于 $\ell^nT_0$。
因此
$$
\rho(f_r^2)\equiv1\pmod{\ell^n},\qquad
c(f_r^2)\equiv\rho(\gamma)w\pmod{\ell^nT_0}
\tag{19}
$$
对某个 $\gamma$ 成立。
$\rho(\gamma)$ 保持 $T_0$，故右侧的有限 $\ell$ 赋值不随 $n,r$ 增大。
这正是本论证不能只看 Frobenius 特征多项式的地方。

令 $a$ 为一个固定整数，使 $w\notin\ell^aT_0$。
当 $n>a$，(19)使 $c(f_r^2)\notin\ell^aT_0$。
其在
$$
T_0/(\rho(f_r^2)-1)T_0
\tag{20}
$$
中的 $\ell$ 阶至少随 $\ell^{n-a}$ 增长：
若 $\ell^{n-a}c(f_r^2)$ 落在
$(\rho(f_r^2)-1)T_0\subseteq\ell^nT_0$，
则在 $V$ 中约去 $\ell^{n-a}$ 就得到
$c(f_r^2)\in\ell^aT_0$，矛盾。
允许 $L/\mathbf Q_\ell$ ramified 不影响这个以 $\ell^n$ 表述的包含论证。

这里的有限余类就是同一个全局 AJ 的 unramified restriction。
好约化、与 $\ell$ 不同的素数处的 specialization 由 R859(17)给出。
因为 $r$ 惯性且 $(r)$ 在原 ring class group 中为主，
$r$ 在 $H/K$ 完全分裂，$f_r^2$ 正是所选
$\mathfrak r\mid r$ 的 $\mathbf F_{r^2}$ Frobenius。
在(2)中更有原准确标量
$$
\theta\rho(f_r^2)\theta^{-1}=-1/r,
\tag{21}
$$
与(17)、(19)一致。

## 6. 传回同一个整 shadow

换用 $T_{\rm top}$ 或乘原固定 $D$，
只会使(20)的阶数界损失一个与 $n,r$ 无关的固定 $\ell$ 幂。
可直接选择 $e$ 使
$$
\ell^eT_{\rm top}\subseteq\theta(T_0)
\subseteq\ell^{-e}T_{\rm top};
$$
用 $\ell^e\theta$ 与 $\ell^e\theta^{-1}$ 得到整格映射，
其双向复合为 $\ell^{2e}$，故有限余群的核与余核均被
$\ell^{2e}$ 杀掉。再乘固定 $D$ 和先前固定清分母整数只增加固定损失。
因此(20)的无界阶在原整格中仍无界。

R859 的实际 cross divisor
$$
D_r=\Gamma_{\varphi_r}-E_0\times O-r\,O\times E_0
$$
在最高块给一个 $\mathcal O$-整同构，行列式 $r$ 为单位。
结合其 Kummer/specialization 相容性，(20)的增长准确传成
$$
\boxed{
\operatorname{ord}_\ell
 \mathscr S_{\mathfrak r}(\widetilde{\mathcal Z})
\text{ 无界。}}
\tag{22}
$$
其中 shadow 保 R859(29)–(30)的原全部 $c_\rho$、
point-factor $\chi$、闭点 trace 和 scheme multiplicity。
不把 $\operatorname{Gal}(H/K)$ 冒作剩余域群。

更强地，对每个固定 $m$，取 $n$ 大到吸收上述固定成本，
(16)的一整个 Chebotarev 共轭类给正密度的 $r$，
使至少一个原所选素理想上的 shadow 具有阶被 $\ell^m$ 整除的元素。
这里每个 $m$ 的密度可以不同，未声称一个与 $m$ 无关的密度下界。

## 7. 准确等价和仍未解决的门

**定理。** 固定原 $j$、$\ell>3$、系数嵌入及 R859 的同一个整代表。
以下三条等价：

1. 原 $AJ_\ell(Z_{{\rm orig},j})\ne0$ 于有理 $\ell$-adic cohomology；
2. 某个好惯性 $r\ne\ell$ 和某个 $\mathfrak r\mid r$ 的原 shadow
   在 $\ell$ 部分非零；
3. 这些好惯性约化 shadow 的 $\ell$ 阶无界。

证明。$1\Rightarrow3$ 是第2–6节；$3\Rightarrow2$ 显然；
$2\Rightarrow1$ 是 R859 的最高块整同构与 $H^1(H,T_{\rm top})$
无挠性。原有理 $h^1$ 对应和固定 $D$ 不改变非零方向。证毕。

因此在实际 Hom/divisor 输入明确以后，遍历惯性好约化的精确
shadow 检测对**非零原 AJ 类**必能终止。
但本注没有提供这样一个非零类的先验输入，没有把 Chow 非零
替成 AJ 非零，也没有宣称零输出能在有限步证原 AJ 为零。
R817 的7993仍是另一个指定 canonical 来源，不能用来启动
本定理的第1条。

特别，(22)变化的是有限域约化素数 $r$，$\ell$ 从头到尾固定。
它不证明无穷多个系数素数上的原 AJ/localization 非零，
更不完成固定 rank至少2 曲线的全 $\Sha[p^\infty]$ 无穷素数目标。

## 8. 证据与接续

- [R832](../results/R832-original-triple-chow-purity-and-rank-zero-contractions.md)、
  [R858附B](../results/R858-original-artin-cm-vertical-vanishing-and-generic-injectivity.md)：
  原 Q 下降二维因子、CM/Artin 方向及真 $h^1$ 平凡化。
- [R859](../results/R859-original-supersingular-shadow-and-integral-aj-detection.md)：
  惯性剩余域、整 cross 同构、5/11无挠性及同一实际 shadow。
- J. S. Milne, [Complex Multiplication](https://www.jmilne.org/math/articles/2007c.pdf)，
  Theorem3.10、Remark3.11：第2节的 CM idèle 作用。本文另付主单位取幂、
  标量、不可约性与全部 cocycle 论证。
- J. S. Milne, [Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf)，
  Chapter V Theorem3.23，Chapter VIII Theorem7.4：
  只在第5节对真实有限扩张(16)使用 Chebotarev。
- 本文没有运行数学程序、素数扫描或新增可重算输出。
  下一实际输入仍是 R839 原映射的明确表达，以及原 AJ/canonical
  或四实际除 p 行的非零，不以本条件等价收尾。
