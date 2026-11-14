# 固定导子轨道的两生成元与真实 torsion theta 的 Cartier 关系

**状态：已证明。** 日期：2026-11-12。
本文继续 [固定反圆分 theta 对角笔记](2026-11-12-anticyclotomic-theta-diagonal.md)。
所证关系均针对原曲线与其真实 torsion 初值；没有更换原椭圆单位生成元。
它们目前只控制模 $p$ 的第一层，没有证明主问题的无穷素数结论。

## 1. 完整导子 Galois 轨道的显式生成元

仍取
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad f=34(1+i),
\qquad F=K(E[f]),\qquad [F:K]=256.
$$
CM 作用使 $\operatorname{Gal}(F/K)$ 的像是
$(\mathbb Z[i]/f)^\times$ 的子群。该像恰为
$$
\boxed{\quad H=\langle-3,-2+i\rangle\simeq
\mathbb Z/16\mathbb Z\times\mathbb Z/16\mathbb Z.\quad}
\tag{1}
$$

证明如下。素数 $3$ 处良约化，$\#E(\mathbb F_3)=4$，
故 $a_3=0$；$K$ 中 inert 素理想 $(3)$ 的 Frobenius
作用于 prime-to-$3$ torsion 为 $[-3]$。
素数 $5$ 处，逐个 $x\in\mathbb F_5$ 代入，得到 $\#E(\mathbb F_5)=10$，
故 $a_5=-4$。两个 $5$-上方素位的 CM Frobenius 因而分别为
$[-2+i]$、$[-2-i]$。所以 (1) 右边包含在实际 Galois 像中。

模 $17$ 的两个嵌入分别为 $i\mapsto4,-4$，而
$3$ 是 $\mathbb F_{17}^\times$ 的生成元。在这两个因子中，
$$
-3\longmapsto(14,14)=(3^9,3^9),\qquad
-2+i\longmapsto(2,11)=(3^{14},3^7).
$$
两列的离散对数矩阵行列式为
$$
9\cdot7-9\cdot14=-63\equiv1\pmod{16}.
$$
故它们在 $(\mathbb Z[i]/17)^\times\simeq C_{16}^2$ 中已生成全部
$256$ 个元素。实际 Galois 像的阶数恰为 $256$，所以 (1) 成立。
这也证明两生成元在模 $f$ 群中各阶为 $16$，且独立。

因此，对原 $P_f$，正确的 $256$ 点轨道是
$$
\mathcal S=\left\{
[(-3)^a(-2+i)^b]P_f:0\le a,b<16
\right\}.
\tag{2}
$$
这避免了在计算中另行猜测 Gaussian quartic residue symbol 的规范。

整个 $(\mathbb Z[i]/f)^\times$ 有 $1024$ 个元素，且
$$
(\mathbb Z[i]/f)^\times=\mu_4\times H.
\tag{3}
$$
例如可由 $\psi$ 规范生成元的有限字符看出：其在 $\mu_4$ 上是逆字符，
故 $H\cap\mu_4=\{1\}$；再比较阶数即得 (3)。
因此任意 primitive $f$-torsion 点与原 $P_f$ 的 $H$-轨道只差一个
$\epsilon\in\mu_4$ 的整体伸缩。
Kronecker 级数的 CM 齐次性给出
$$
\Theta_{\epsilon z_0,0}(z,w)
=\epsilon^{-1}\Theta_{z_0,0}(\epsilon^{-1}z,\epsilon^{-1}w).
$$
所以其对角 $d_m$ 改变为 $\epsilon^{-(2m+1)}d_m$。
特别在 $m=p-1$ 时，只差一个 $p$-单位，赋值证书不受影响。
若要报告某个精确剩余类，仍须说明所选择的初始轨道。

## 2. Torsion 初值及固定整数 $69$ 的精确分配关系

对 $S\in\mathcal S$，用复均匀化选取 $z_S$，并记
$$
U_S=\zeta(z_S)-\bar z_S/A,
\qquad
F_S(z)=e^{-z\bar z_S/A}\frac{\sigma(z_S+z)}{\sigma(z_S)}.
\tag{4}
$$
因 $[68]S=O$，有 $[69]S=S$。标准 division function 的恒等式
$\sigma(69z)=\Psi_{69}(z)\sigma(z)^{69^2}$，连同 $\sigma$ 的准周期公式，
给出
$$
\boxed{\quad
F_S(69z)=F_S(z)^{69^2}
\frac{\Psi_{69}(S+z)}{\Psi_{69}(S)}.
\quad}
\tag{5}
$$
为核对指数，写 $69z_S-z_S=\lambda\in\Gamma$。
$\sigma(z_S+69z+\lambda)/\sigma(z_S+\lambda)$ 中多出的因子是
$e^{69\eta(\lambda)z}$。
又 $\eta(\lambda)=68\bar z_S/A$，这恰好与
$69^2$ 次幂和 $69$ 次伸缩中指数项的差相消。
两边在 $z=0$ 都为 $1$，所以没有剩余常数。

设 $h=\delta\log\Psi_{69}$ 是曲线上的固定有理函数。
对 (5) 取 $k$ 阶对数导数，得到
$$
(69^k-69^2)\,
\left.\frac{d^k}{dz^k}\log F_S(z)\right|_{z=0}
=(\delta^{k-1}h)(S),\qquad k\ge1.
\tag{6}
$$
当 $k=1$，这就是
$$h(S)=-69\cdot68\,U_S.$$
目标 split 素数不除 $69\cdot68$，且 $\Psi_{69}(S)$ 为局部单位，
故 (6) 可以在每个目标素位还原。

计算初值时也可使用更低的 division function。
原导子轨道满足 $[34]S=T=(0,0)$，且 $E_1^*(T)=0$，所以
$$
U_S=-\frac1{34^2}\frac{\delta\Psi_{34}}{\Psi_{34}}(S).
\tag{7}
$$
这里 $\Psi_{34}(S)\ne0$，因为 $[34]S=T\ne O$。
(7) 仅用于降低计算规模；(5) 仍以 $69$ 为固定乘子。

## 3. 固定代数上的 Cartier 恒等式

令 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，并在 $\mathfrak p$ 处还原。
记 $A_p\in\mathbb F_p^\times$ 为相对于 $\omega=dx/(2y)$ 的 Hasse
不变量，亦即 $a_p(E)\bmod p$。
在曲线函数域上，普通的 invariant derivation 满足
$$
\delta^p=A_p\delta.
\tag{8}
$$
可以先由 invariant vector field 的 restricted $p$-power 是同一条
一维 invariant 线上的常数倍得到 (8)，再由 Cartier/Hasse 计算识别
该常数；这是 R24 使用的同一规范。

考虑固定多项式代数
$$
\overline{\mathcal R}=\mathbb F_p[U,X,Y]/(Y^2-X^3+17X)
$$
及其导子
$$
\mathcal D U=-X,\qquad \mathcal D X=2Y,\qquad
\mathcal D Y=3X^2-17.
\tag{9}
$$
则有较强的整体等式
$$
\boxed{\quad\mathcal D^p=A_p\mathcal D
\quad\text{on }\overline{\mathcal R}.\quad}
\tag{10}
$$

只需证明它也作用在 $U$ 上。令
$$c=\delta^{p-1}X-A_pX\in\mathbb F_p(E).$$
由 (8)，$\delta c=0$，故 $c$ 是函数域中的 $p$ 次幂。
它仅可能在 $O$ 有极点，阶数至多 $p+1$。
所以其 $p$ 次方根仅可能在 $O$ 有至多一阶的极点。
椭圆曲线上不存在仅在一点有一阶极点的非常数函数，故 $c$ 是常数。
再施 $[i]^*$：因为 $p-1\equiv0\pmod4$，
$\delta^{p-1}X$ 与 $X$ 同时变号，而常数固定。
于是 $c=-c$，从 $p\ne2$ 得 $c=0$。
因此
$$
\mathcal D^pU=-\delta^{p-1}X=-A_pX=A_p\mathcal DU,
$$
证明 (10)。

## 4. Theta 导数算子及真实 torsion 初值的额外消去

令 $\mathcal L=\mathcal D+U$，其中 $U$ 表示乘法算子，
并令 $C_n=\mathcal L^n1$，与中央对角笔记的定义相同。
特征 $p$ 的 Bell/Jacobson 公式给出
$$
\mathcal L^p=\mathcal D^p+U^p+\mathcal D^{p-1}U.
\tag{11}
$$
这里可直接看 $C_p$ 的完整 Bell 多项式：除了分拆 $1+\cdots+1$
和单块 $p$ 外，每项的整数系数都被 $p$ 整除。
再用 Leibniz 公式展开 $\mathcal L^p$ 作用在一般函数上，
中间的 $\binom pj$ 均消失，即得到 (11)。

由 (10)，定义
$$
B_p=C_p-A_pU=U^p-\delta^{p-2}X-A_pU,
$$
便有
$$
\mathcal L^p=A_p\mathcal L+B_p,\qquad
\mathcal D B_p=0.
\tag{12}
$$
对于任意形式初值，$B_p$ 不必消失。
对本题的**真实 torsion 初值**，却有
$$
\boxed{\quad
B_p(U_S,x(S),y(S))=0,\qquad S\in\mathcal S.
\quad}
\tag{13}
$$

证明取 (6) 的 $k=1,p$。
在模 $p$ 下，$69^p-69^2\equiv-69\cdot68$，记这个单位为 $-c_0$。
因此
$$
h(S)=-c_0U_S,\qquad
(\delta^{p-1}h)(S)=-c_0(\mathcal D^{p-1}U)(S).
\tag{14}
$$
对任意非零有理函数 $g$，设 $h_g=\delta g/g$。
由 $(\delta+h_g)=g^{-1}\delta g$、(8) 和 (11)，有
$$
\delta^{p-1}h_g=A_ph_g-h_g^p.
\tag{15}
$$
取 $g=\Psi_{69}$；它在 $S$ 附近为单位，所以可以在 $S$ 取值。
将 (14) 代入 (15)，并用 $c_0\in\mathbb F_p^\times$，得到
$$
\mathcal D^{p-1}U(S)=A_pU_S-U_S^p.
$$
再用 (11) 即是 (13)。

一个可直接复算的推论是：对所有 $n\ge1,a\ge0$，
$$
\boxed{\quad
(\mathcal D^a C_{n+p-1})(S)
=A_p(\mathcal D^a C_n)(S)\pmod p.
\quad}
\tag{16}
$$
因为 (12) 中 $B_p$ 与 $\mathcal L$、$\mathcal D$ 都交换，
$C_{n+p-1}=A_pC_n+B_pC_{n-1}$；
施 $\mathcal D^a$ 后，再由 (13) 消去第二项。
同理，对 $a\ge1$，导数指标也满足
$$
(\mathcal D^{a+p-1}C_n)(S)
=A_p(\mathcal D^aC_n)(S)\pmod p.
\tag{17}
$$

## 5. 这些关系还没有越过哪一层

中央对角的精确式是
$$
d_m=\frac1{m!}\sum_{j=0}^{m+1}
\frac{q_j}{(m+1-j)!}
\operatorname{Tr}_{F/K}\operatorname{ev}_f
(\mathcal D^mC_{m+1-j}),
\qquad q_j=[w^j]\frac{w}{\sigma(w)}.
\tag{18}
$$
当 $m=p-1$ 时，$j=0$ 项含 $p!$，其 $p$-赋值为 $1$。
所以即使只计算 $d_{p-1}\bmod p$，不能在 (18) 中先把所有分子
分别模 $p$ 再除以 $p!$。
而目标 $d_{p-1}\bmod p^4$ 至少要求相应 raw numerator 保留到模 $p^5$；
其他 $q_j$ 的分母也必须独立跟踪。

(13)、(16)、(17) 已证明了真实 torsion 对这些首层关系的约束，
但没有提供该五位精度的统一抬升非零项。
例如 (6) 的精确高阶右端仍包含
$$
\delta^{p-1}\big(\delta\log\Psi_{69}\big)(S),
$$
虽然 $\Psi_{69}$ 是固定函数，导数阶数随 $p$ 增长。
不能将它误写成有限个固定代数数的 Fermat quotient。
同样，(16) 的指标周期本身随 $p$ 增长，
尚未给出一个固定阶数、固定系数域的线性 Frobenius 模型来强制
$d_{p-1}\notin p^4$ 对无穷多个 $p$ 成立。

本笔记的作用是把可用的 Cartier 消去具体落实到原 theta 轨道，
并为高精度计算提供独立的第一层校验。

## 来源与接口

- 导子、$[F:K]=256$、$[34]P_f=(0,0)$：R6、R18 及其 CLS 原文输入。
- $\delta^p=A_p\delta$ 的规范及 $A_p\equiv a_p$：R24 的
  Cartier/Hasse 与普通 CM 输入。
- Theta、$F_S$、$d_m$ 的规范：
  [前一笔记](2026-11-12-anticyclotomic-theta-diagonal.md)，
  依据 Bannai–Kobayashi Theorem 1.17 和 §3.3。
  [原文](https://arxiv.org/pdf/math/0610163)。
- (1)、(5)、(10)、(13)、(16) 的证明全部在上文给出，
  不以数值样本代替一般恒等式。
