# R1167 — 原第一层 CM 挠点的完整整 PD 系数与实际 Miller 定标

**状态：已证明。** 日期：2026-11-28 Asia/Taipei。会话：Astra-serre-24b8836b-20261126。

本篇实际计算 R1164–R1166 的第一槽 Weil/Miller 系数，而不重新选择一个只差单位的 Fontaine–Laffaille 基。结果同时保留未取值的 PD 法向项 $\gamma_p(g)$ 和原 $\omega,x\omega$ 两列。它是第一层 $p$ 系数的完整公式；原中央 $F_0$ 仍须以同一 theta、ordered primitives 和 Cor 继续读取。

## 1. 同一曲线、坐标与系数格

固定原 good supersingular CM 模型之一：

- cubic 情形 $\mathcal E:y^2=x^3-1$，$p\equiv5\pmod6$；
- Gaussian 情形 $\mathcal E:y^2=x^3+a_{\rm G}x$，$a_{\rm G}\in\mathbb Z_p^\times$，$p\equiv3\pmod4$。

始终 $p>37$。令 $F=\mathbb Q_{p^2}$、$\mathcal O=W(\mathbb F_{p^2})$，$\sigma$ 是其实际 Frobenius。所需进一步未分歧底变换逐系数作原作用即可，不改变本篇定标。

沿 R712、R978、R1166 的同一 strict Lubin–Tate 坐标 $z$：
$$
[p]z=pz-z^{p^2},\qquad [\xi]z=\xi z\quad(\xi\in\mu_e),
\qquad e=p^2-1.
\tag{1167.1}
$$
令
$$
t=-x/y,\qquad \omega=\frac{dx}{2y},\qquad \eta=x\omega,
\qquad z/t\longrightarrow1.
$$
这是实际 $\omega$ 的 strict normalization。置
$$
L=F(\varpi),\quad\varpi^e=p,\quad z(P_0)=\varpi,\quad
g=z^e-p,\quad
S=\mathcal O[z,\gamma_n(g):n\ge1]^\wedge_p.
\tag{1167.2}
$$
本篇先不令 $g=0$。$\psi$ 在系数上为 $\sigma$，$\psi z=z^p$，
$N=z\partial_z$。记
$$
D=S\otimes_{\mathcal O}
       \bigl(\mathcal O\omega\oplus\mathcal O\eta\bigr).
$$

由 R1163 的第一层整比较及 R1166 的 actual ambient/residue map，
原 pointed inverse-Miller 类给唯一 degree-zero coefficient cycle
$$
x_P\in\operatorname{Fil}^1D/p,\qquad
Nx_P=0,\qquad \Phi_1x_P=x_P,\qquad \Phi_1=\Phi/p.
\tag{1167.3}
$$
这里是 divided-Frobenius 方程，不把它弱化为 $\Phi x_P=px_P$。
该 degree 没有负一次项，故原自然性给字面的 coefficient 等式。

## 2. 原 Cartier 常数及实际 crystalline 两列

定义原非零常数
$$
b_E=[x^{p-1}]\,
       x f(x)^{(p-1)/2}\pmod p,\qquad y^2=f(x).
\tag{1167.4}
$$
直接展开即得
$$
b_E=
\begin{cases}
(-1)^{(p-1)/2-(p-2)/3}
 \displaystyle\binom{(p-1)/2}{(p-2)/3},
       & f=x^3-1,\\[6pt]
\displaystyle\binom{(p-1)/2}{(p-3)/4}
 a_{\rm G}^{(p+1)/4},
       & f=x^3+a_{\rm G}x .
\end{cases}
\tag{1167.5}
$$
所有阶乘指标均小于 $p$，且 $a_{\rm G}$ 为单位，
所以 $b_E\in\mathbb F_p^\times$。

为锁定符号，直接在特殊纤维写
$$
\eta=\frac{x f(x)^{(p-1)/2}\,dx}{(2y)^p}.
$$
分子次数小于 $2p-1$，Cartier 只读取 $x^{p-1}dx$。
相同计算给 $\omega$ 的系数为零。因此
$$
C_{\rm rel}(\eta)=b_E\omega',\qquad
C_{\rm rel}(\omega)=0 .
\tag{1167.6}
$$
cubic 的同一值已在 R589/R683 登记；本篇使用其原值，
并显示 Gaussian 的相同有限系数。

CM 的 $\mu_6$ 或 $\mu_4$ 两特征线为 $\mathcal O\omega$ 和
$\mathcal O\eta$；$\sigma$ 交换它们。原 crystalline Frobenius
遂有精确形式
$$
\Phi_M\omega=p\alpha\eta,\qquad
\Phi_M\eta=\beta\omega,\qquad \alpha,\beta\in\mathcal O^\times.
\tag{1167.7}
$$
特殊纤维的平方 Frobenius 为 $[-p]$，故
$$
\beta\sigma(\alpha)=-1,\qquad
\alpha\sigma(\beta)=-1.
\tag{1167.8}
$$

再使用 R1165 §10 的实际 chain Frobenius，而不另选基。
$\iota\eta=(\eta,\eta_V,t^{-1})$，其中 $\eta_V=\eta-t^{-2}dt$。
模 $p$ 后，两 local Frobenius forms 及 overlap homotopy $I$ 均为零，
而 overlap 剩 $t^{-p}$。R1165 的原 residue projection 因而给
$$
\beta\equiv-\operatorname{Res}(t^{-p}\eta_V)
       =-[t^{p-1}]\eta_V=-b_E,\qquad
\alpha\equiv b_E^{-1}\pmod p.
\tag{1167.9}
$$
最后一个 residue 由 (1167.6) 和 $\omega/dt=1+O(t^4)$ 锁定。
第二个 projection 是 $\operatorname{Res}(t^{-p}\omega)=0$。
因此 (1167.9) 的负号来自原两开集投影，不是后加的选择。

## 3. 完整 PD 固定方程只剩一个待定常数

令 $\tau_\xi z=\xi z$。原 first-slot Weil 归一满足
$$
e_p([\xi]P,T)=e_p(P,[\bar\xi]T).
$$
对局部 $\xi$，取全局 CM 整数在 $\mathcal O$ 中逼近至模 $p^2$；
其在 $E[p]$ 上的作用和在实际 de Rham 格模 $p$ 的作用均固定。
$\bar\xi=\xi^p$。由 R1164 的 isogeny 自然性，写
$x_{P_0}=A\omega+B\eta$ 后有
$$
A(\xi z)=\xi^pA(z),\qquad
B(\xi z)=\xi B(z).
\tag{1167.10}
$$
唯一 $z^j\gamma_n(g)$ normal 展开及 $\operatorname{Fil}^1$ 遂给
$$
A=z^p\sum_{n\ge0}a_n\gamma_n(g),\qquad
B=z\sum_{n\ge1}b_n\gamma_n(g),\qquad a_n,b_n\in\mathbb F_{p^2}.
\tag{1167.11}
$$

完整 Frobenius carry 是
$$
c=\frac{\psi(g)}p\equiv-1-\gamma_p(g)\pmod p.
\tag{1167.12}
$$
确实，$(g+p)^p/p-1$ 中只有 $g^p/p=(p-1)!\gamma_p(g)$
和常数 $-1$ 留下。$\gamma_p(g)^p\equiv0$，因为其
divided-power 乘法系数的 $p$-赋值为一，所以 $c$ 为单位。

对 $n\ge1$，$\psi(\gamma_n(g))=p^nc^n/n!$ 被 $p$ 整除；
对 $n\ge2$，$\psi(\gamma_n(g))/p$ 仍被 $p$ 整除。
这里使用完整的
$n-1-v_p(n!)\ge1$，并未把 $n\ge p$ 的 normal 项直接删去。
因此 $\Phi_1$ 只读 (1167.11) 的 $a_0,b_1$，
但其输出仍含 (1167.12) 的高 normal 项。

置 $\kappa=a_0$。由 (1167.7)–(1167.12) 和
$z^{p^2}=z(g+p)$ 得
$$
b_1=b_E^{-1}\kappa^p,\qquad
\boxed{\quad
x_{P_0}=
 \kappa z^p(1+\gamma_p(g))\omega
 +b_E^{-1}\kappa^pzg\,\eta .
\quad}
\tag{1167.13}
$$
(1167.8) 保证第一列的常数恰为 $\kappa$。
这是完整 normal 等式，尚待原 Miller 来源确定 $\kappa$。

也可直接核 connection：
$$
N\gamma_p(g)=ep\gamma_p(g)+ep\gamma_{p-1}(g)\equiv0,\qquad
N(zg)=z(p^2g+ep)\equiv0\pmod p.
\tag{1167.14}
$$
故 (1167.13) 确为 (1167.3) 的 cycle，未遗漏底 log 条件。

## 4. 原 Miller 函数的外环 residue

令 $f=f_{P_0,p}$ 为 R1164 的同一个 Miller 函数：
$$
\operatorname{div}(f)=p(P_0)-p(O),\qquad
t^pf=1+c_1t+\cdots\quad\text{at }O.
\tag{1167.15}
$$
R1164 §13 的 actual formal $U$ frame 给
$u_U=f\,t(-P_0)^p$；后一个因子对几何微分为常数。
R1166 的 $A$ projection 在 $g=0$ 时遂为
$$
\operatorname{ev}(A)
   =-\operatorname{Res}_{\rm outer}\frac{d\log f}{t}.
\tag{1167.16}
$$
overlap PD logarithm 在实际 specialization 后为零。

此 residue 在原特殊纤维 $O$ 的外环上取。
在一般纤维，它同时包住 $O$ 和 $P_0$。
不能只读 (1167.15) 的 Laurent 系数。
取 $|t(P_0)|<|t|<1$，原 residue theorem 给
$$
\operatorname{Res}_{\rm outer}\frac{d\log f}{t}
   =c_1+\frac p{t(P_0)}.
\tag{1167.17}
$$
第二项来自 $f$ 在 $P_0$ 的 $p$ 重零。
这也可直接由
$(t-a)^{-1}=\sum_{n\ge0}a^nt^{-n-1}$ 的外环展开核实；
$a=t(P_0)$ topologically nilpotent，展开与原 completed
两开集的 residue 相容。$t$ 在选定的 $V$ 上仅于 $O$ 为零，
故没有其它贡献。

特别 $v_p(p/t(P_0))=1-1/e<1$：
这个项绝不能以“含因子 $p$”为由先删掉。

## 5. 由同一个 Miller translation norm 锁定 $c_1$

令 $\mathcal E(z)$ 为原 odd completed-zeta primitive，
$$
d\mathcal E=-\eta,\qquad
\mathcal E(z)=z^{-1}+\sum_{k\ge1}e_kz^k.
\tag{1167.18}
$$
常数项固定为零。它与 R589 的原 completed-zeta 值使用相同
$\omega$、$t$ 和点；以下由原 Miller 函数直接定标，
不依赖一个另外选取的解析 period。

对任意非零形式点 $P$，定义实际有理函数
$$
r_P(T)=\frac{y(T)+y(P)}{x(T)-x(P)}.
$$
其 residues 在 $P,O$ 分别为 $1,-1$，在 $-P$ 可去；
$O$ 处展开为 $-t^{-1}+O(t)$。
椭圆加法公式直接给
$$
D r_P=x(T)-x(T-P),\qquad D=d/\omega.
$$
结合 (1167.18)，并在 $O$ 比较常数项，得到精确加法式
$$
r_P(T)=\mathcal E(T-P)-\mathcal E(T)+\mathcal E(P).
\tag{1167.19}
$$
这些形式级数在所有非零形式点收敛：
$\eta$ 的整 Laurent 系数使 $v_p(e_k)\ge-v_p(k)$。
因此 (1167.19) 在避开其极点的共同形式环域上成立。

$D\log f-pr_{P_0}$ 无极点，是常数；
由 (1167.15) 在 $O$ 的展开，该常数恰为 $c_1$：
$$
D\log f=pr_{P_0}+c_1.
$$
另一方面，
$\prod_{j=0}^{p-1}f(T-jP_0)$ 的 divisor 逐项 telescopes 为零，
故该有理函数为常数。对其取 $D\log$，再用 (1167.19)，得
$$
0=p\sum_{j=0}^{p-1}r_{P_0}(T-jP_0)+pc_1
  =p^2\mathcal E(P_0)+pc_1.
$$
所以准确有
$$
\boxed{\qquad c_1=-p\mathcal E(P_0),\qquad
\operatorname{ev}(A)
 =p\left(\mathcal E(P_0)-\frac1{t(P_0)}\right).\qquad}
\tag{1167.20}
$$
这里只在特征零的函数恒等式中除 $p$；
没有对整 trace、cochain 或 lattice 作不合法的 $p$ 除法。

## 6. 包含全部高次项的模 $p$ 取值

令 $m=6$（cubic）或 $m=4$（Gaussian）。
原 CM automorphisms 及 strict 坐标给
$$
\mathcal E(z)=z^{-1}
 +\sum_{\substack{k\ge1\\k\equiv-1\ (m)}}e_kz^k,\qquad
v_p(e_k)\ge-v_p(k).
\tag{1167.21}
$$
确实 $\eta$ 的 character 为 $\xi^{-1}$，
故其正次项积分的指数正是 $k\equiv-1\pmod m$。
另外，完整 $\mu_e$ 作用于 invariant differential 给
$$
\omega=(1+O(z^e))\,dz.
\tag{1167.22}
$$

写 $\eta=(z^{-2}+\sum_{k\ge1}a_{k-1}z^{k-1})\,dz$。
则 $e_k=-a_{k-1}/k$。
由 (1167.6)、(1167.22)，对 $1\le r<p$，
$$
a_{pr-1}\equiv
\begin{cases}
b_E,&r=1,\\
0,&2\le r<p
\end{cases}
\pmod p .
\tag{1167.23}
$$
因此对 $0<k<e$：
若 $p\nmid k$，$p e_k\varpi^k\in p\mathcal O_L$；
若 $k=pr$，由 $p e_{pr}=-a_{pr-1}/r$，
只有 $r=1$ 留下 $-b_E\varpi^p$。

必须另付 $k\ge e$ 的整个无限尾。
置 $a=v_p(k)$，一般界为
$$
v_p(p e_k\varpi^k)\ge1-a+\frac{k}{e}.
\tag{1167.24}
$$

- $a=0$ 时右侧至少 $2$。
- $a=1$ 时右侧至少 $1$。
- $a=2$ 时写 $k=p^2r$。由 $p^2\equiv1\pmod m$ 和
  $k\equiv-1\pmod m$，$r\ge m-1\ge3$，
  故右侧严格大于 $2$。
- $a\ge3$ 时 $p^a/(p^2-1)>p^{a-2}\ge a$，
  故右侧至少 $1$。

这也证明尾项一致收敛至 $p\mathcal O_L$。
其中 $a=2$ 必须用原 CM character：
若不保该 character，$k=p^2$ 本来会是不能忽略的危险项。

最后 $t=z+O(z^2)$ 为整 strict 改参，
故 $z^{-1}-t(z)^{-1}\in\mathcal O[[z]]$。
将它乘 $p$ 后取值为零模 $p\mathcal O_L$。
综上
$$
\boxed{\quad
p\left(\mathcal E(P_0)-\frac1{t(P_0)}\right)
       \equiv-b_E\varpi^p\pmod{p\mathcal O_L}.
\quad}
\tag{1167.25}
$$
这里消去的是 (1167.20) 的完整极项差，
并未单独丢掉 $p/z(P_0)$。

由 (1167.13) 的 specialization，
$\operatorname{ev}(A)=\kappa\varpi^p$。
$\varpi^p$ 在 $\mathcal O_L/p$ 中非零，
而 $\kappa+b_E$ 属于常数域 $\mathbb F_{p^2}$；
因此
$$
\kappa=-b_E .
\tag{1167.26}
$$

## 7. 原完整系数及所有 pure powers 的 normal 表

把 (1167.26) 代回，得到本篇主结论：
$$
\boxed{\quad
x_{P_0}
 =-b_Ez^p(1+\gamma_p(g))\omega-zg\,\eta
       \quad\text{in }\operatorname{Fil}^1D/p .
\quad}
\tag{1167.27}
$$
对 $P_\xi=[\xi]P_0$，保同一 $z,\varpi$ 及原 Weil 槽：
$$
\boxed{\quad
x_{P_\xi}
 =-b_E\xi^pz^p(1+\gamma_p(g))\omega
    -\xi zg\,\eta .
\quad}
\tag{1167.28}
$$
这不是“至多差一个单位”的公式。
$b_E$、两负号、$\xi^p/\xi$ 以及 normal $\gamma_p$ 均已实际锁定。

令 $d\in\{4,8,12\}$。R1163/R1164 的 normalized signed
projector 把原 $P_\xi^d$ 送到普通 pure power $x_{P_\xi}^d$，
不额外插入 $d!$。
记 $j_k=p(d-k)+k$。
原 $\omega^{d-k}\eta^k$ 系数准确是
$$
(-1)^d\binom dk b_E^{d-k}\xi^{j_k}z^{j_k}
       (1+\gamma_p(g))^{d-k}g^k .
\tag{1167.29}
$$
所有 $0<j_k\le12p<e$。
进一步用
$$
g^k=k!\gamma_k(g),\qquad
\gamma_p(g)^h\equiv h!\gamma_{hp}(g),\qquad
\gamma_{hp}(g)\gamma_k(g)\equiv\gamma_{hp+k}(g)\pmod p
$$
（$k,h<p$），得到完整有限 normal 展开
$$
\boxed{
x_{P_\xi}^d=
 (-1)^d
 \sum_{k=0}^d\sum_{h=0}^{d-k}
 \frac{d!}{(d-k-h)!}\,
 b_E^{d-k}\xi^{j_k}z^{j_k}\gamma_{hp+k}(g)\,
 \omega^{d-k}\eta^k .
}
\tag{1167.30}
$$
这里出现的 $d!/(d-k-h)!$ 是 (1167.29) 的 ordinary
binomial 与 PD 乘法系数；
它不是把原 moment 再乘一次 $d!$。

每个 $j_k$ 都是非平凡 tame character，
所以 (1167.30) 与 R1166 的 $\operatorname{Tr}(x_P^{[d]})=0$
完全吻合。乘原 theta 的函数输入后仍须先收集实际第零
$e$-block，不能据这个 coefficient trace-zero 删除 moment。

## 8. 与原 theta 及后继中央输入的直接连接

R1166 §§11–12 已锁原 $d=4,8$ 第一层的实际同一个单位
$$
V_2(z)=-\frac1{z^3y(P(z))},
\qquad k_4(2)=63/16,\quad k_8(2)=1023/256 .
$$
将 (1167.30) 逐项乘
$$
\frac{N_zV_2}{V_2}\,d\log z,\qquad
\frac1p\log\frac{V_2^p}{\psi V_2},
$$
然后使用 R1166 的实际 trace：
无 base-log 槽取 $e$ 倍第零块，
base-log 槽取第零块并写成 $d\log u$。
这给完整原输入的明确函数与明确 coefficient，
没有任意的系数基、额外根、未知 period 常数或待定 scalar。

所有 $\gamma_p(g)$ 及 (1167.30) 的高 normal 项须保留到
实际乘法、trace 和 divided Frobenius 完成。
R1155 的取值窗口不允许预先删去它们。
本篇没有把原 function 展开截到 degree $12$，
没有把后继两个 moments 的乘积改成两个独立 trace 的乘积，
也没有删除 R1159/R1166 的 same-coset 和 ordered corrections。

本篇只断言上述第一层实际系数与输入公式。
全部 $p^r$ 根塔、原三中央指定 primitives 的逐项值和 $F_0$
仍按已登记的同源比较继续计算；
(1167.27) 本身不代替全局 canonical primitive，
也不证明本课题的主完成标准。

## 已登记来源

- [R589](R589-specified-type-three-coefficient-and-actual-CM-unit-criterion.md)
  与 [R683](R683-even-weight-Cartier-channel-and-actual-r3.md)：
  原 cubic completed-zeta、Cartier 常数及 character。
- [R712](R712-actual-M2-second-digit-and-Lubin-Tate-two-block-reduction.md)
  与 [R978](R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md)：
  同一 strict LT/Robert 坐标及整改参；本篇不重做已登记的来源窗口。
- [R1163](R1163-original-highest-moment-integral-syntomic-comparison.md)：
  原 finite integral coefficient comparison 与 projectors。
- [R1164](R1164-original-pointed-Miller-coefficients-and-Cech-symbols.md)：
  第一槽 inverse-Miller、实际 SS frames、pointed 同根归一和 CM 自然性。
- [R1165](R1165-original-integral-residue-contraction-and-log-PD-cone.md)：
  同一 $\omega,\eta$ 留数投影及 actual chain Frobenius。
- [R1166](R1166-original-ambient-PD-and-ordered-coefficient-comparison.md)：
  actual ambient/source 比较、$H^0$ 两 residue、tame Cor 和原 theta 输入。

全部为纸面证明，无数学程序执行。
