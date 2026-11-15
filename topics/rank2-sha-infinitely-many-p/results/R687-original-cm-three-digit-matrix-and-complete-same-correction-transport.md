# R687 — 原 CM 三位分子到完整旧 M，及同 R 第二类的精确范围

日期：2026-11-15。**状态：已证明。** 本篇把 R676 的实际 CM 分子接入
原旧目标的全部列和第三精度，不增加来源或中央观察。

三位分子给两位 $\Theta^\dagger$ 后，缺少的低前缀第三位由原
非共振精确系数补齐；其余第三位在旧 $\Gamma^+$ 中被真正 carry 杀掉。
因此不需要泛称“还必须知道整个 $B_\alpha\bmod p^4$”。

进一步，只给两位分子、恢复一位 $\Theta^\dagger$，
仍足以在补齐同一原低前缀后确定旧矩阵的第三精度整等价类，
并确定已过首提升的**同一个** $P+pR$ 的第二代表。
未恢复的高处第二位只给显示的目标整单位。
R651 的指定 $Z^+$、两个十三行门及 $\Psi_R$ 都按同一来源输送；
这不证明其实际余类非零。

## 1. 旧坐标、实际 canonical 和完整目标

取
$$
p=6s-1>101,\quad d=p+1,\quad1\le\ell<s-13,\quad f_D<p.
$$
保原同一来源及全部 $P_{134}/U_0$。
完整旧目标为
$$
\boxed{
\Gamma^+=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2).
}
\tag{1}
$$
标准整块为 $f_0(w)+f_1(w)\epsilon+f_2(w)\epsilon^2$，
前两块长度 $s$，第三块长度 $\ell+13$。
两条十三行和最初十三个自由方向始终在这个目标中。

为避免 R676 与旧 $E_1$ 角坐标同名，本文记旧角为 $T$，
R676 的正六次参数仍记为 $t$：
$$
\boxed{
T=-t,\qquad
w=\xi=tH(t)^6,\qquad
H=\sum_{n\ge0}\frac{C_n}{6n+1}t^n,\quad
C=(1+t)^{-1/2}.
}
\tag{2}
$$
这是原 $E_b$ 与 $E_1$ 的同一齐次规范：
$w=bz_b^6=z_1^6$、$t=bu_b^6=u_1^6$。
$\Theta=x\sigma^2$ 的权为零，故两种写法给同一个 $\Theta$。
不需要把 $u$ 与 $z$ 相认，也不需要加入一个新的算术伸缩源。

R676 的 canonical 是
$$
E=\Theta^\dagger=\Theta\exp(-2c_b^\dagger z_b^d),
\qquad
c_b^\dagger=-\frac{b^sC_s}{pd}.
$$
在旧 $E_1$ 的 $w$ 中记
$$
\kappa^\dagger=-\frac{34C_s}{pd},\qquad
\boxed{a^\dagger=p\kappa^\dagger=-\frac{34C_s}{d}\in\mathcal O^\times.}
\tag{3}
$$
那么同一个原径向量准确恢复为
$$
\boxed{
\rho=(1+8T)\Theta^{17}
=(1-8t)E^{17}e_2(a^\dagger\epsilon)
\quad\text{于 }\Gamma^+,
}
\tag{4}
$$
其中 $e_2(x)=1+x+x^2/2$。
这里保首 Gaussian，没有将其正规部分当成原整函数本身。

若继续使用 R651 原先固定的 $a=p\kappa$，
R606 所付的合法整差为
$$
\delta=\kappa^\dagger-\kappa\in\mathcal O.
$$
令 $g^\dagger=(1-8t)E^{17}$，则
$$
\boxed{
g=g^\dagger\exp(\delta w^s),\qquad
a=a^\dagger-p\delta.
}
\tag{5}
$$
因此对每个实际相对 charge $q$，
$$
g^qe_2(aq\epsilon)
=(g^\dagger)^qe_2(a^\dagger q\epsilon)
$$
在原有限目标中准确相同。
(5) 必须整体使用；不能改变 Gaussian 常数而保留不匹配的正规部。
下面恢复原矩阵可用 (4)；读取原 R651 坐标则同时使用 (5)。

## 2. 两位 E 的真实来源

R676 取实际
$$
\alpha=\omega^2+p\omega,\quad
\nu=p^2-p+1,\quad
\delta_{n,p}=(\nu-\alpha^{6n})/p,
$$
并已证所有 $0\le n<p$ 的 $\delta_{n,p}$ 为单位。
其同一个实际 $B_\alpha$ 给
$$
L=\log E
=-\sum_{n=1}^{p-1}
\frac{b_{n,p}-\mathbf1_{n=s}(2C_s\delta_{s,p}/d)}
     {p\delta_{n,p}}\xi^n,
\quad
\log B_\alpha(t(\xi))=\sum b_{n,p}\xi^n.
\tag{6}
$$
全部差先在整环内形成并证明可除 $p$，再除 $p$。
因此，按 R676 的完整输入精度表：

- $B_\alpha,H,C_s$ 和中央 $\delta_{s,p}$ 的三位数据，
  以及其余单位逆的两位数据，恢复 $E\bmod p^2$；
- 相应两位数据恢复 $\bar E$。

(6) 的整个窗口为 $t^{<p}$。
$\xi=tH^6$ 的完整换参必须参加，不能只将三条原中央的十五个系数
当成整个 $E$ 的替代品。

## 3. 所需低前缀第三位已经是原精确有理数据

R434 的原角精确系数为
$$
\log\Theta^{17}
=\sum_{n\ge1}\ell_nT^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}.
$$
Gaussian 从 $t^s$ 才开始，所以
$$
\boxed{
E\bmod t^s
=\exp\left(
\sum_{1\le n<s}\frac{(-1)^n}{3n}
\frac{(1/3)_n}{(5/6)_n}t^n
\right)\bmod t^s.
}
\tag{7}
$$
这是原对象的特征零精确前缀，不是由模 $p$ 微分方程任选的提升。

$n<s$ 时，$n$ 以及 $(5/6)_n$ 中的全部因子在当前素数处为单位；
形成该有限 exp 所需的阶乘也小于 $p$。
故 (7) 可直接按原有理数计算到模 $p^3$，或任何所需更高精度。
这里只读取首共振之前的前缀，未延长原 ODE。

(2) 在原目标中给关键的完整整恒等
$$
\boxed{
t^s=w^sH^{-6s}
=p\epsilon\,H^{-(p+1)}.
}
\tag{8}
$$
尤其
$$
p^2t^s=0\pmod{p^3\Gamma^+}.
\tag{9}
$$
整个 $H^{-(p+1)}$ 保留；
(8) 没有把 $H^{-p}$ 当成一来删除高位。

另外 $w^{3s}=0$，而 $p>3s$。
因此 $t^p$ 也在这个实际有限目标中为零，
R676 的 $t^{<p}$ 窗口确实覆盖旧矩阵的全部所需项，
包括完整 $w^{13}$ 后的第三块。
这只是有限目标的事实，不外推为无限来源的解析半径结论。

## 4. 三位分子已经恢复全原 M 模 p³

取 (6) 恢复的 $E^{[2]}=E\bmod p^2$。
构造任意整混合代表 $\widetilde E^{[3]}$：

1. 其整个 $t^{<p}$ 窗口模 $p^2$ 等于 $E^{[2]}$；
2. 其 $t^{<s}$ 前缀模 $p^3$ 等于 (7)；
3. $t^s$ 以后的第三位可任取整代表。

则
$$
E-\widetilde E^{[3]}
\in p^3R+p^2t^sR,\qquad R=\mathcal O[t]/t^p.
$$
由 (8)–(9)，
$$
\boxed{E=\widetilde E^{[3]}\pmod{p^3\Gamma^+}.}
\tag{10}
$$

**定理 1。** 将 $\widetilde E^{[3]}$ 代入 (4)，
连同同一个原 $t(w)$、全部角因子、$P_{134}$ 及共同 charge 四十，
得到的整个原矩阵准确等于
$$
\boxed{M\pmod{p^3}.}
\tag{11}
$$

**证明。** 原每列只是上述原有限目标中的固定有理角因子
和同一个 $\Theta$ 的实际整数幂，并按 (4) 恢复原首 Gaussian。
所有角单位及其逆都用同一有限整展开；
已付的原来源整性和 $f_D<p$ 范围保持。
(10) 在一个整环内成立，故这些既定的有限乘法、整数幂及整单位逆
全部保持模 $p^3$ 等式。
没有增加源列，也没有对 $m_{13}$ 作非整逆。
整个 $c_*U_0m_{13}$ 仍是原来的完整表示。证毕。

这说明对旧有限矩阵，不需要用 $B_\alpha\bmod p^4$
恢复 $E$ 的整个第三位。
所需第三位只有 (7) 的原低前缀，其余由真实 carry (8) 处理。
这与 R676 中“单独那个 CM 方程的全窗口输入精度”不冲突：
本篇利用了旧目标额外的 $w^s=p\epsilon$ 和已有的原非共振系数。

## 5. 只有一位 E 时，缺失高位仍只给目标整单位

现在只使用 (6) 的一位 $\bar E$，即仅需要相应两位分子。
取一个辅助整代表 $E^{(0)}$，使其整个窗口模 $p$ 等于 $\bar E$，
同时把 $t^{<s}$ 前缀按 (7) 补到模 $p^3$。
高于该前缀的第二、第三位任取。
它只是用于计算的有限代表，不被称为另一条实际算术来源。

因为两个单位在低前缀已经一致，某个真实整 $V(t)$ 满足
$$
\frac{E}{E^{(0)}}=1+pt^sV(t)
\pmod{p^3R}.
$$
其中允许把 $p^2t^s$ 项并入 $V$；
只在目标中读取 $\bar V$。
由 (8)，
$$
\boxed{
\frac{E}{E^{(0)}}
=1+p^2\epsilon H^{-d}V
\pmod{p^3\Gamma^+}.}
\tag{12}
$$
该差的平方已为零于所需精度。

定义原标准整块上的算子
$$
\boxed{
D_\epsilon(f_0,f_1,f_2)=(0,f_1,2f_2).
}
\tag{13}
$$
这是整线性算子，不是未经检验的裸 $\epsilon\partial_\epsilon$
作用在特征零商环上。

原一列的总 sigma degree 为 $34q_i$。
在 canonical $\mathcal W_D$ 中，准确是 $q_i=n+40$；
若使用此前已付的真实扩源，也必须保它们各自的完整总 charge。
模 $p$ 的该列为
$$
\bar F_i=A_i(w)e_2(a^\dagger q_i\epsilon).
$$
普通高尾的 carry 带有额外 $p$，所以在同一标准块中准确有
$$
\boxed{
D_\epsilon\bar F_i
=a^\dagger q_i\,\epsilon\bar F_i.
}
\tag{14}
$$
这包括前面 $w^{13}$ 和第三块的实际截止，不能先删掉它们。

用 $E^{(0)}$ 构造的完整辅助矩阵记为 $M^{(0)}$。
(12) 在第 $i$ 列上的作用为
$1+17q_i p^2\epsilon H^{-d}V$。
结合 (14)，得到整个原目标上的单位恒等
$$
\boxed{
M\equiv(I+p^2K_V)M^{(0)}\pmod{p^3},\qquad
K_V=\frac{17}{a^\dagger}\,m_{H^{-d}V}D_\epsilon.
}
\tag{15}
$$
$m_{H^{-d}V}$ 是同一有限目标中的整乘法；
式中只需选择其模 $p$ 值的任意整提升。
$I+p^2K_V$ 的逆模 $p^3$ 为 $I-p^2K_V$，
不要求这些算子对易。
全 common charge 四十已经包含在 (14)，没有只处理相对 $n$ 后遗漏共同因子。

**定理 2（同一个 R 的准确第二代表）。**
若同一个原源向量 $Q_2=P+pR$ 已满足
$M^{(0)}Q_2\in p^2\Gamma^+$，则也有 $MQ_2\in p^2\Gamma^+$，且
$$
\boxed{
\overline{\frac{M(P+pR)}{p^2}}
=\overline{\frac{M^{(0)}(P+pR)}{p^2}}.
}
\tag{16}
$$
原第一提升、两条十三行要求和真正 $d_2$ 的判定因而一致。

**证明。** (15) 先给两个矩阵模 $p^2$ 完全相同。
对这个同一个 $Q_2$，额外项
$p^2K_VM^{(0)}Q_2$ 属于 $p^4\Gamma^+$，
所以模 $p^3$ 也完全相同。除 $p^2$ 后约化即得 (16)。证毕。

(15) 不声称 $M$ 的逐项第三位已由一位 $E$ 决定；
该具体坐标仍可随真实 $V$ 改变。
它证明的是完整矩阵的整等价及 (16) 的同修正代表。
因此 R676 的分子第三位不能通过这些高系数
单独添加一条旧 $d_2$ 非零证据。

## 6. R651 的实际 Z⁺ 和 Ψ_R 如何读取

现在取 R651 的准确范围
$$
\ell\in\{1,2\},\quad
1\le r\le\nu\le13,\quad \ell\le\nu,
\quad s>\max(3\nu+\ell,\nu+13),
$$
以及该篇的全部原帽。
它的临界基准只使用
$$
T_*=\nu+(\nu-r+\ell+1)<s
$$
的原 $g$ 前缀。
由于 (7) 和 (5) 在 $t^s$ 以下完全固定，
可使用**同一个**原低行右逆、$P^{\rm crit}$ 和临界支 $\psi$。
因而
$$
A=P^{\rm crit}|_\psi,\quad
B=\mathcal E^2P^{\rm crit}|_\psi,\quad
C=\mathcal E^3P^{\rm crit}|_\psi
$$
及同一个修正 $R$ 均不改换。
记
$$
A,B\in w^\nu,\quad C\in w^r,\quad
\eta=\log(g/\psi)=\eta_0+p\xi,\quad
\eta_0\in w^{s-\nu},\quad
\xi\in w^{\nu-r+\ell+1}.
$$
所有取代表和 $p$ 除法继续按 R651 的原顺序。

定理1的混合三位代表直接恢复原完整矩阵，
所以可原样读该篇
$$
\boxed{
Z^+=R_1+B\xi+a^{-1}\mathscr SA+\eta_0R_2+
(2a)^{-1}\mathscr S(B\eta_0^2).
}
\tag{17}
$$
$\mathscr S$ 始终是原 $w$ 中的 $s$ 阶 carry，
不是在新 $t$ 中免费除 $t^s$。
先读两条十三行
$\bar Y^+=0,\ \pi_s\bar Z^+=0$，
再在这些整除已成立后读
$$
\boxed{
\Psi_R=
\left(
\pi_{s-13}\overline{Y^+/p+H_0},\
\pi_{s-13}\overline{aZ^+/p+H_1},\
a\pi_\ell\overline{\mathscr SZ^+}
\right).
}
\tag{18}
$$
其中 $H_0,H_1$ 是 R651 的完整原式，
包括 $\nu\ge7$ 时活的 $\mathscr S(\eta_0^2R_2)/2$。
(11)–(16) 均在完整原目标上成立，
所以没有漏掉该项或其余低行右逆高尾。

对定理2的一位辅助代表，还可以直接核这份正常形。
固定同一个 $\eta_0$，由 (12) 在普通级数中除 $p$ 得
$$
\xi_{\rm actual}-\xi_{(0)}\in w^s\mathcal O[[w]]
\quad\text{于所需精度}.
\tag{19}
$$
其余 $A,B,C,\psi,R$ 相同。
于是 (17) 的差从 $w^{s+\nu}$ 起：
$$
\pi_s(Z^+_{\rm actual}-Z^+_{(0)})=0,\qquad
\pi_\ell\mathscr S(Z^+_{\rm actual}-Z^+_{(0)})=0
$$
于实际读取精度，因为 $\nu\ge\ell$。

$H_0$ 中含 (19) 的差都从 $w^s$ 或更高起。
$H_1$ 中最低的几类阶分别为
$$
s,\qquad
\operatorname{ord}\mathscr S(B\eta_0\Delta\xi)\ge s,\qquad
\operatorname{ord}\mathscr S(C\eta_0^2\Delta\xi)
\ge2s-2\nu+r>s-13.
$$
所有其余项同样高于可见截止。
所以完整 (18) 与 (16) 一致；
没有分别为其前两块或第三尾另选修正。
若直接采用原 $a$ 而非 $a^\dagger$，全程按 (5) 同时返回，
不更改旧 Gaussian 规范。

## 7. 实际输入减少了什么，尚未证明什么

现在有两份准确的有限输入规格：

| 所求对象 | 实际所需资料 |
|---|---|
| 全部原 $M\bmod p^3$ 的具体坐标 | R676 的三位 $B_\alpha$ 等输入，恢复两位 $E$；再用原精确式 (7) 补低前缀第三位 |
| 原第三精度整等价类及已过首提升的同 $P+pR$ 第二代表 | R676 的两位分子输入，恢复一位 $\bar E$；仍必须补 (7) 的原低前缀三位 |

两种规格均保同一个原 $H$、$t/w$ 换参、Gaussian、
共同 charge 四十、全部实际角列、$P_{134}/U_0$ 和两个十三行带。
若丢掉 (7)，则 (12) 的 $t^s$ 因子不再成立，
R649 所指出的低位提升区分仍然存在。
因此本篇没有说“一个模 $p$ theta 模型本身就决定第二类”。

(6) 给的是原 CM 分子的实际高尾，不是新增自由列。
(15) 又表明，未恢复的那部分高位只作目标单位运输；
不能因这些系数都已可计算，便断言 (18) 在真实像外。
还须对原同一个 $\bar E$ 的完整 regular 高尾与
$\mathcal T_\psi(\overline{\mathcal W}_D)$、
$\mathcal D_\psi(\overline{\mathcal K}_{\nu,\ell})$
作真正比较。
本篇不以来源端可逆、CM 单位逆或有限矩阵重建替代这个尚未完成的非零证明。

## 依赖

- [R676](R676-original-unit-cm-numerator-and-three-digit-lift.md)：
  原实际 $B_\alpha$、完整单位逆及输入精度。
- [R434](R434-original-angular-high-coordinates-and-carry-unit-schur-transport.md)：
  原 $\ell_n$ 精确非共振前缀与真实高轴规范。
- [R642](R642-complete-central-remainder-and-original-third-precision-unit.md)：
  原完整标准目标、整块算子而非裸导数、同修正第三精度运输。
- [R651](R651-original-higher-critical-branch-lift-and-complete-second-forcing.md)：
  实际临界基准、全 $Z^+$、两条十三行及同一个 $R$ 的完整 $\Psi_R$。

本篇只保存完整证明；没有新增扫描、证书数据或可重算输出文件。
