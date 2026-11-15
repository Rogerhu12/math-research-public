# R708 — 原首边界的单模 p 前缀与整 Gaussian 规范的完整返回

日期：2026-11-15。**状态：同一原迹的单模 \(p\) 充要判据、约 \(3p/4\) 的短前缀、整规范变换及无需 LT 坐标的实际有限来源已证明。原中央零到这些全前缀条件的联系仍未证明。**

R699 用高度主系数 \(1\) 得到两位判据。R707 已把同一原代数迹的高度主系数降到 \(3/4\)，其增补将对数次项降到 \(1/4\)。本篇把这个真实收益完整接回原边界和 R614/R647 使用的原首 Gaussian 系数，保留准确的索引、末行、全部高尾和实际整除。

## 1. 原记号及新的严格范数门

固定
\[
p=6s-1>101,\quad d=p+1,\quad e=p-1,\quad q=p^2,\quad
m=34\ \text{或}\ 72.
\]
仍取 R663 的原严格整 LT 坐标、\(W=v^d\) 和
\[
Q(W)=W^e-p,\qquad
\mathcal B_m(W)=\sum_{i\ge0}b_{m,i}W^i\in\mathcal O[[W]],
\quad\mathcal O=\mathcal O_{\mathbf Q_p(\omega)}.
\tag{1}
\]
若 \(\xi^e=p\)，R696 的原迹 \(\mathcal T_{m,T}\) 满足
\[
v_p(\mathcal T_{m,T})
 =\frac1e+v_p(\mathcal B_m(\xi)),
\tag{2}
\]
并且一个原迹为零等价于全部原首边界值为零。

R707 及其 gcd 增补给一个固定常数 \(C_m\)，使非零原迹满足
\[
\boxed{\;
v_p(\mathcal T_{m,T})\le
 \frac34+
 \frac{\frac14\log(1+\log p)+C_m}{\log p}.
\;}
\tag{3}
\]
因此，充分大的 \(p\) 上
\[
\boxed{\;\mathcal T_{m,T}=0
       \iff v_p(\mathcal T_{m,T})\ge1.\;}
\tag{4}
\]
更一般，对任意固定 \(\alpha\in(3/4,1)\)，存在只依 \(\alpha,m\) 的门，使所有门后的非零原迹均有 \(v_p(\mathcal T_{m,T})<\alpha\)。

(3) 是原全共轭平均与固定整数分母给出的界；不要求每个复共轭先有单独最大值节省，也没有预设迹非零。

## 2. 首次完整的单模 p 充要式

R663 的真实余数是
\[
r_{m,i}=\sum_{k\ge0}p^k b_{m,i+ek}\in\mathcal O,\qquad0\le i<e,
\]
且
\[
\mathcal B_m(\xi)=\sum_{i=0}^{e-1}r_{m,i}\xi^i.
\]
因为 \(r_{m,i}\) 的赋值为整数，不同 \(i\) 的有限项赋值具有不同的小数部分，故非零时
\[
v_p(\mathcal B_m(\xi))
 =\min_{0\le i<e}\left(v_p(r_{m,i})+\frac ie\right).
\tag{5}
\]
全高尾已包含在 \(r_{m,i}\) 内，而且
\(r_{m,i}\equiv b_{m,i}\pmod p\)。

结合 (2)、(4)、(5)，充分大 \(p\) 时准确有
\[
\boxed{\;
\mathcal T_{m,T}=0
\iff
b_{m,i}\equiv0\pmod p\quad(0\le i\le e-2).
\;}
\tag{6}
\]
末指标 \(i=e-1\) 在这个判据中完全没有条件：它本身在 (2) 中的最小赋值已为 \(1\)。所以 (6) 是 \(e-1=p-2\) 条真实剩余域行，不是 \(p-1\) 条，更不是一条中央。

一旦 (6) 成立，结论是准确的 \(\mathcal T=0\)，故 R663 又给
\[
Q\mid\mathcal B_m\quad\text{于 }\mathcal O[[W]].
\]
因此被判据省略的行以及全部高尾余数会由原全局高度约束一起被迫为零；并非在初等模 \(p\) 运算中把它们删掉。

## 3. 约三分之四长度的真实前缀

固定 \(\alpha\in(3/4,1)\)，令
\[
J_\alpha(p)=\lceil\alpha e\rceil-1.
\tag{7}
\]
门后的 \(p\) 满足 \(1\le J_\alpha\le e-1\)。若
\[
b_{m,i}\equiv0\pmod p,\qquad0\le i<J_\alpha,
\]
则 (5) 给
\[
v_p(\mathcal T_{m,T})
 \ge\frac{J_\alpha+1}{e}
 =\frac{\lceil\alpha e\rceil}{e}\ge\alpha.
\]
这里早期 \(p\)-整除项的估值至少 \(1+1/e\)，其余项至少达到显示值；全高尾不会降低它。
由 (3) 的严格门，这只可能是准确零。
反向由 \(Q\mid\mathcal B_m\) 得
\(\mathcal B_m\bmod p\) 被 \(W^e\) 整除，当然满足这个前缀。

因此完整结论为
\[
\boxed{\;
\mathcal T_{m,T}=0
\iff
b_{m,i}\equiv0\pmod p\quad(0\le i<J_\alpha(p)).
\;}
\tag{8}
\]
(8) 依赖固定原来源的高度界。它不是对任意整级数都成立的形式命题。
若使用 (3) 的实际固定常数，也可取
\[
J(p)=\left\lfloor e\left\{\frac34+
 \frac{\frac14\log(1+\log p)+C_m}{\log p}\right\}\right\rfloor
 =\frac34p+O_m\!\left(\frac{p\log\log p}{\log p}\right);
\]
此时 \((J+1)/e\) 严格大于 (3) 的右边，同样证明 (8)。

## 4. 原 LT 前缀与完整中央系数逐项相等

保留 R639/R663 的完整中央规范
\[
F_c(X)=\Pi_d\log(\sigma(z)/z),\qquad X=z^d,\qquad
c=[X]F_c,\quad v_p(c)=-1.
\]
令
\[
\Pi_d\!\left(A_m(z)e^{-mF_c(z^d)}\right)
 =G_{m,c,0}(X)=\sum_{h\ge1}g^c_{m,h}X^h,
\quad A_m=\sigma^m\phi_m.
\tag{9}
\]
\(\Pi_d\) 保全部 \(\mu_d\) 平均，不是选一条新 tame 支。

R663 的同一精确身份为
\[
G_{m,c,0}(WH(W)^d)=WH(W)^m\mathcal B_m(W),
\qquad H(W)=1+O(W^e).
\tag{10}
\]
由于 \(G_{m,c,0}\) 的常数为零，(10) 两边中所有 \(H-1\) 修正都从次数 \(e+1\) 开始。所以在特征零中逐项准确有
\[
\boxed{\;
b_{m,h-1}=g^c_{m,h}\qquad(1\le h\le e).
\;}
\tag{11}
\]
这是相等，不只模 \(p\) 相等。\(H\) 的高系数有分母也不影响这个次数断言。
因此 (6)、(8) 已可直接在原完整中央来源上读取，不需要先计算 LT 坐标。

## 5. 整 Gaussian 变换使同一前缀回到 R614 的实际系数

记
\[
U(z)=\frac{\sigma(z)}z e^{-c z^d},\qquad
\mathscr G_m(z)=A_m(z)e^{-mc z^d},\qquad
g_{m,h}=[z^{dh}]\mathscr G_m(z).
\tag{12}
\]
这是 R614/R647 的首 Gaussian 规范。R614 已证明 \(U\) 在全部次数 \(<q-1\) 整，且 \(g_{m,h}\in\mathcal O\) 对 \(1\le h\le p-1=e\) 成立。

本篇还需要把 R647 的前五块整三角变换延到整个首 \(e\) 块，而不是预设更长窗口也整。
定义
\[
E_m(X)=\exp\{-m(F_c(X)-cX)\}
       =\sum_{r\ge0}\epsilon_{m,r}X^r.
\tag{13}
\]
有 \(\epsilon_{m,0}=1,\epsilon_{m,1}=0\)。
精确的范数式是
\[
\boxed{\;
E_m(z^d)
 =\left(\prod_{\zeta\in\mu_d}U(\zeta z)\right)^{-m/d}.
\;}
\tag{14}
\]
它由 \(\Pi_d\log U=F_c-cX\) 得到。

在次数 \(<q-1=de\) 中，括号内是常数一的整级数，并由完整 \(\mu_d\) 不变性只含 \(z^d\) 的幂。又因 \(p\nmid d\)，指数 \(-m/d\in\mathbf Z_p\) 的二项式系数均在 \(\mathbf Z_p\)。故
\[
\boxed{\;\epsilon_{m,r}\in\mathcal O\quad(0\le r<e).\;}
\tag{15}
\]
同样的论证也适用于 \(E_m^{-1}\)。这支付实际整逆，不能把 \(F_c-cX\) 的每个 log 系数直接称为整。

因为 \(E_m\) 只含 \(X\)，(9)、(12) 准确给
\[
g^c_{m,h}=\sum_{r=0}^{h-1}\epsilon_{m,r}g_{m,h-r}.
\tag{16}
\]
由 (15)，对任意 \(J\le e\)，(16) 是原 \(J\) 条系数之间的整单位下三角变换。因此
\[
\boxed{\;
g^c_{m,h}\equiv0\pmod p\ (1\le h\le J)
\iff
g_{m,h}\equiv0\pmod p\ (1\le h\le J).
\;}
\tag{17}
\]
这是同一真实 sigma 来源之间的等价，未引入自由比较 lift。

结合 (8)、(11)、(17)，得到更直接的充要式：
\[
\boxed{\;
\mathcal T_{m,T}=0
\iff
g_{m,h}\equiv0\pmod p\quad
          (1\le h\le J_\alpha(p)).
\;}
\tag{18}
\]
也可在 (18) 中取完整单模 \(p\) 门 \(J=e-1=p-2\)。

## 6. 完全有限的原来源窗口

设
\[
\widetilde X(z)=z^2x(z),\qquad
P_{34}=P_S,\quad P_{72}=P_T
\]
为 R595/R647 的两个完整固定多项式。原来源准确为
\[
\boxed{\;
z^{-6}\mathscr G_m(z)=
U(z)^m\widetilde X(z)^{(m-6)/2}
 P_m\!\left(\frac{17z^6}{\widetilde X(z)^3}\right).
\;}
\tag{19}
\]
\(m=34,72\) 时原每个 \(\widetilde X\) 幂分别至少为 \(2,3\)，所以 (19) 使用完整原有限分子，没有新极点。

要读 \(g_{m,h}\) 的 \(1\le h\le J\)，只需 (19) 到
\[
\boxed{\;L_{p,J}=dJ-6.\;}
\tag{20}
\]
所有 \(U,\widetilde X\) 输入也只需到此实际次数；\(c\) 由同一 \(\sigma\) 的第 \(d\) 次系数取得。
对 (6) 的 \(J=e-1\)，
\[
\boxed{\;L_{p,e-1}=p^2-p-8.\;}
\tag{21}
\]
对 (8)，
\[
L_{p,J_\alpha}=(p+1)(\lceil\alpha(p-1)\rceil-1)-6
             =\alpha p^2+O_\alpha(p).
\tag{22}
\]

这里已不必计算原 LT 坐标或完整 \(T_{\rm g}\)；(10)–(17) 付清了从那些对象返回 (19) 的成本。
但 (20) 仍是 \(O(p^2)\) 的真实窗口。可以先用准确有理数完成 sigma/Gaussian 的实际消去，再读取整系数的模 \(p\)；若使用有限精度实现，仍须逐项支付中间分母与精度损。最终判据只有一位，不等于上游只需一位输入。原高度、位复杂度和固定来源预算也不因此消失。

## 7. 与原中央零的准确关系

原完整 \(j_m\) 并未改变。R614 的完整 Newton 全尾已经给
\[
j_m=\sum_{h\ge1}(-1)^{h-1}(h-1)!
      (p/\gamma_m)^h g_{m,h},\qquad
\gamma_m=pmc\in\mathcal O^\times,
\]
并且
\[
j_m=0\ \Longrightarrow\
L_{m,H}:=\sum_{h=1}^{H}(-1)^{h-1}(h-1)!
      (p/\gamma_m)^h g_{m,h}
 \in p^{H+1}\mathcal O,\quad1\le H\le p-2.
\tag{23}
\]
这是对实际部分和的高精度关系，仍含各低系数的真实除 \(p\) 商。(23) 不能未经证明换成 (18) 的逐行模 \(p\) 零。

例如在 R647 已付的前五个实际 Cartier 行中，(18) 若成立，则必要有
\[
\mathcal T_{m,1}=\cdots=\mathcal T_{m,4}=0,\qquad
\mathcal T_{m,5}=6\kappa_5\ne0.
\tag{24}
\]
最后一个值不是零：它保留原 \(z/Z\) 坐标首差。
原 \(j_m=0\) 的 R647(30)–(32) 则还包含真实低部分和的除商，不能删去后把 (24) 称为矛盾。

本篇支付的是一个实际精度与来源改进：
原首边界准确零已经等价于约 \(3p/4\) 条原首 Gaussian 系数的模 \(p\) 零。
剩下的是 (23) 与 (18) 在这个固定来源上的额外算术联系，或这些同一实际行的指定非退化。
所得零首先只付 \(Q\mid\mathcal B_m\) 和 R663 的同 \(Y\) 闭盘；原 \(X\) 下降仍须 \(j_m=0\)、\(Q^{d-m}\mid\mathcal B_m\) 以及原同解下降条件。

## 依赖

- [R707](R707-original-theta-average-and-three-quarter-trace-height.md)：固定原迹的真实均方收益、全共轭高度及 gcd 增补。
- [R699](R699-original-uniform-two-digit-boundary-criterion.md)：全余数精度及实际来源窗口。
- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：严格整坐标、(10) 与同 \(Y\) 闭盘充要。
- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)：原迹、全部轨道及准确赋值偏移。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：完整 addition 整窗、原首 Gaussian 分子与全部 Newton 尾。
- [R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)：原五 Cartier 行、第五坐标修正及实际部分和除商。

本篇为统一证明和有限算法，不依赖新扫描或新增可重算报告。
