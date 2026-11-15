# 原双侧 θ-lift、第二障碍与实际除 T² 杯积

日期：2026-11-15。接续
[实际 Shapiro 二阶类](2026-11-15-original-Robert-Shapiro-second-class.md)。
本文在同一原支持内构造另一侧到 $T^2$ 的 lift，保留其真正的
第二障碍及 $p$ 条件。随后使用原 $c_s$ 的 $T^3$ 数据作实际
除 $T^2$，说明所得一次互反恰恢复 R779 已登记的 $I_0$ 比较。
没有新的 $\Theta$、$b$、$a_q$ 数值，也没有把形式存在当成可执行
Robert 产品算法。

## 1. 同一个 k-linear exact dual

保留前稿的 $K=\mathbf Q(i)$、$p=43$、$k=\mathbf F_{43}[i]$、
$\Sigma_K$、$D=W(1)|_{G_K}$ 和
$$
\ell=\kappa_q+i\kappa_S,\qquad
\ell_{\rm cyc}=2\kappa_S,\qquad
\theta_n=(1+T)^\ell\bmod T^n .
$$
这里 $\kappa_q(\gamma)=1$，没有反转原 $\gamma$。
记
$$
V=D^\vee_k(1),\qquad
V_n=V\otimes_k\Lambda_n(\theta_n),\qquad
D_n=D\otimes_k\Lambda_n^\# .
\tag{1}
$$
相同 $J$ 结构下的原 trace pairing 为 Hermitian，所以 $V$ 使用
原 $W$ 的共轭 $k$ 结构。以下 $\bar w$ 表示原 $w$ 在该结构中的
同一个类，不是另选一个 primal 全局类。

取 R200/R743 的原 $w$，保 $w_p=0$ 的完整 cochain gauge。置
$$
P_0=\bar w,\qquad
x_0=-\ell_{\rm cyc}-2i\kappa_q=-2i\bar\ell .
\tag{2}
$$
R752 给真正 $\Sigma$ 支持的 $D_0$，满足
$$
\delta D_0=x_0\cup w .
\tag{3}
$$
其 differential、$q$ regularization、$p$ flat correction 始终
按原 rational 标架，不把它称为一个已计算的 cochain。

令
$$
P_1=\frac i2\,\overline{D_0}.
\tag{4}
$$
由 (2)–(3)，
$$
\delta P_1=-\ell\cup P_0.
\tag{5}
$$
所以 $P_0+TP_1$ 是实际 $V_2$ cocycle，保持原支持。
本节并未令 $P_{1,p}=0$。

## 2. q 的 rational 平衡局部 lift

在 $K_q$ 的原标架中，记
$$
v=\kappa_S+i\kappa_q,\qquad \ell=i\bar v .
$$
原 $V$ 坐标为 $F_q\mapsto1,\ K_q\mapsto-i$，所以
$$
P_{0,q}=i\varepsilon\ell.
\tag{6}
$$
不带 rational 对称规范的局部 lift 可以写成
$i\varepsilon(\theta_{n+1}-1)/T$。
为了与 R752 的原 quadratic primitive 逐字对齐，使用
$$
P^{\rm loc}
 =i\varepsilon(1+T)^{1/2}
       \frac{\theta_{n+1}-1}{T}\pmod {T^n}.
\tag{7}
$$
所有二项式只取需要的有限阶，分母 $2,3$ 在 $k$ 中可逆。
乘号前的系数与 Galois 元无关；因此
$(\theta(gh)-1)=(\theta(g)-1)+\theta(g)(\theta(h)-1)$
证明 (7) 是真实局部 cocycle。

这个半次因子还保留原 rational 对称性。在原 semilinear 对合
$T\mapsto(1+T)^{-1}-1$ 下，未平衡的 quotient 变成其
$(1+T)$ 倍，而 $(1+T)^{1/2}$ 变成 $(1+T)^{-1/2}$；
两者合起来不变。只在此局部陈述这一对称性，不用它代替全局
支持或 $p$ 型条件。

(7) 的一次、二次系数分别为
$$
Q_1=\frac{i\varepsilon}{2}\ell^2,
\qquad
Q_2=i\varepsilon\left\{
 \binom\ell3+\frac12\binom\ell2-\frac18\ell\right\}.
\tag{8}
$$
因 $\bar\ell=-iv$，
$$
2i\,\overline{Q_1}=-\varepsilon v^2=\mathfrak q ,
\tag{9}
$$
恰是 R752 (752.8) 的原 rational quadratic cochain。
这里没有额外加减一个未标记的 $i w$。

## 3. 真正的第二障碍由原 L_q 精确检测

设
$$
z_q=P_{1,q}-Q_1.
$$
在 $K_q$ 上系数 $V$ 平凡，故 (5)、(8) 使 $z_q$ 为真正
$1$-cocycle。取原算术 $f=\varphi_q^2$ 和 tame generator $x$，
$$
\ell(f)=32i,\qquad \ell(x)=1.
$$
写
$$
e_q=32i\,z_q(x)-z_q(f).
\tag{10}
$$
以原 Weil 根识别局部 $k(1)$，原算术 invariant 给
$e_q=\operatorname{inv}_{K_q}(\ell\cup z_q)$。
等价地只用 R168 的 finite/singular alternating determinant
即可得到同一个式子。

从 (4)、(9)，$D_0-\mathfrak q=2i\bar z_q$。
R752 (752.12) 允许直接在 quadratic restriction 上读其 affine
functional，且已证明任意局部杀零 correction 在此 functional
中抵消。因此
$$
\boxed{
\mathscr L_q(D_0)
 =2i\,\overline{z_q(f)}-64\,\overline{z_q(x)}
 =-2i\,\overline{e_q}.}
\tag{11}
$$
这里不再除一次 $2$；finite 坐标限制到 $K_q$ 的那个 $2$
已经在 R752 的公式中。

要将 $P_0+TP_1$ 延到 $V_3$，第二 obstruction 是
$$
\mathcal O_2
 =\ell\cup P_1+\binom\ell2\cup P_0 .
\tag{12}
$$
它确为 $2$-cocycle：$\delta\binom\ell2=-\ell\cup\ell$，
再用 (5) 和 Leibniz，两个三次项正好抵消。
(7) 的实际局部二次系数满足
$$
\delta Q_2=-\ell\cup Q_1-\binom\ell2\cup P_0.
$$
所以 $q$ 处 (12) 的类恰为 $\ell\cup z_q$。结合 (11)，
$$
[\mathcal O_2]_q=0
\quad\Longleftrightarrow\quad
\mathscr L_q(D_0)=0 .
\tag{13}
$$
这保留了第二 obstruction，没有仅由第一 primitive 的存在
宣布完整 lift 存在。

## 4. 同支持的全局 lift 与实际 flat 缺陷

原 Shapiro 笔记 §4 已从 R743 得
$H^1(G_{K,\Sigma_K},D)\to H^1(K_p,D)$ 单射。
因此 $\Sha^1_{\Sigma_K}(D)=0$，Poitou–Tate 对偶给
$$
\Sha^2_{\Sigma_K}(V)=0 .
\tag{14}
$$
这是需要的对偶方向。

在 $p$，原非平凡 tame type 给 $H^2(K_p,V)=0$；在 $2$，
原 R743/R746 的局部 inertia 计算同样给零。
$K$ 的无穷位为复位；其余地方均不分歧。
因此 (12) 是同一个支持问题中的零全局类，当且仅当其 $q$ 类为零。
没有使用一个可在新素数任意分歧的 global lift。

R752 (752.14) 已准确计算
$$
\begin{array}{c|cc}
 &\mathscr L_q\text{ 的改变量}&
     \langle\,\cdot\,,d_{{\rm fl},p}\rangle_p\\ \hline
c_p^{\rm Rob}&20&23\\
w&0&0 .
\end{array}
\tag{15}
$$
故可在原支持内选择
$$
\boxed{
D_0^\circ=D_0-\frac{\mathscr L_q(D_0)}{20}c_p^{\rm Rob}.
}
\tag{16}
$$
$20\ne0$，此选择在原有理下降的 $D_0$ primitive ambiguity 中唯一到
$\mathbf F_{43}w$；若不限制 $\mathbf Q$ 下降，则相应 ambiguity 是 $k w$。以它定义 (4) 的 $P_1^\circ$，(13)–(14)
给真正 $\Sigma_K$ 支持的 $P_2$，使
$$
\boxed{
P=P_0+TP_1^\circ+T^2P_2\in Z^1(G_{K,\Sigma_K},V_3).
}
\tag{17}
$$
$P_2$ 不唯一，也没有被数值求出。这是一个实际存在的受支撑
exact-dual lift，不是指定了其 $p$ 型的 lift。

原定义
$$
I_0=\mathscr L_q(D_0)
 -\frac{20}{23}\langle D_{0,p},d_{{\rm fl},p}\rangle_p
$$
和 (16) 给
$$
\boxed{
\langle D_{0,p}^\circ,d_{{\rm fl},p}\rangle_p
 =-\frac{23}{20}I_0=I_0 .
}
\tag{18}
$$
最后一等号用原 $23=-20$ 模 $43$，不改 pairing 规范。
因此可以同时使**第二 lift 障碍消失**和**第一原 coefficient
finite-flat**，当且仅当 $I_0=0$。

严格 $p$ 要另外保留 R746 的实际条件：
任意一阶 $\theta_2$ lift 的 $P_{1,p}$ 可设为零，当且仅当
$b=0$。对已满足第二 lift 条件的 (16)，两个原测试值为
$$
\langle D_{0,p}^\circ,d_{0,p}\rangle_p=26\varepsilon b,
\qquad
\langle D_{0,p}^\circ,d_{{\rm fl},p}\rangle_p=I_0 .
\tag{19}
$$
两条 dual 局部向量独立，故这时 $P_{1,p}^\circ=0$ 当且仅当
$b=I_0=0$。这仍只控制第一 coefficient；
没有证明 $P_{2,p}=0$，也没有将 finite-flat 的首阶条件替换成
原完整晶体型。

## 5. 原 Robert 类多取一阶，并作真正的除 T²

只使用前稿的 $D_3$ 类作未 shift 的二阶 cup，会得到旧的
$w\cup\mathcal K_{\rm glob}$。它不能读取 $a_q$。
这里明确使用同一个原 $c_s$ 的 Shapiro 类多取一阶：
$$
\mathscr C_4\in H^1(G_{K,\Sigma_K},D_4).
$$
它仍是原有限群环的映射，$4<43$，不引入新的 Robert 单位或新的
Euler Norm。其模 $T^2$ 的类在 $p$ 为零，前稿逐层单射使它
在全局也为零。

精确序列
$$
0\longrightarrow T^2D_2\longrightarrow D_4
 \longrightarrow D_2\longrightarrow0
$$
及 $H^0(G_{K,\Sigma_K},D_2)=0$ 给唯一类
$$
\boxed{
\widetilde{\mathcal K}\in H^1(G_{K,\Sigma_K},D_2),\qquad
T^2\widetilde{\mathcal K}=\mathscr C_4.
}
\tag{20}
$$
它的零阶是前稿 $\mathcal K_{\rm glob}$。
这一次除 $T^2$ 是通过真正的 exact sequence 定义；
并未对一个已丢弃的 Taylor coefficient 形式作除法。

原 $c_s$ 在 $V_q$ 的 Kummer 类为零，所以
$\mathscr C_{4,q}=0$。局部
$H^0(K_q,D_2)=Tk$，connecting map 把 $T a$ 送到
$$
a\,\frac{\theta^{-1}-1}{T}\pmod {T^2}.
$$
因而
$$
\boxed{
\widetilde{\mathcal K}_q
 =a_q\,\frac{\theta^{-1}-1}{T}
 \quad\hbox{在 }H^1(K_q,D_2),
}
\tag{21}
$$
其中正是前稿唯一的 $a_q$，满足 $K_q=-a_q$、$\Theta=i a_q$。
本节没有求出这个标量。

另一方面，(13)、(16) 说明 (17) 降到 $V_2$ 后在 $q$ 的类
等于 $i\varepsilon(\theta-1)/T$ 的类。半次平衡与它之差，
以及所有沿 $\ell$ 的一次 correction，都是本地 coboundaries。

## 6. 这条实际 shifted cup 的 q 项为零

在 $K_q$ 上定义
$$
A(g)=\frac{\theta(g)-1}{T},\qquad
B(g)=\frac{\theta(g)^{-1}-1}{T}.
$$
为了写下面的 ordinary $0$- and $1$-cochain 多项式，将同一
$\theta$ 按二项式暂取到模 $T^4$；没有改变任何源类。
exact-dual cup 满足
$$
(A\cup B)(g,h)
 =A(g)\theta(g)^{-1}B(h)=-B(g)B(h).
$$
显式取未变形输出系数中的 $1$-cochain
$$
F(g)=\frac{\theta(g)^{-1}-1+T\ell(g)}{T^2}\pmod {T^2}.
$$
其分子严格被 $T^2$ 整除，且 $\ell$ 是加性角色。
直接用 character 的乘法律得
$$
\boxed{\delta F=-B(g)B(h)=A\cup B\pmod {T^2}.}
\tag{22}
$$
所以 (21) 与 (17) 的实际 cup 在 $q$ 的零阶和一次 invariant
都为零。这是完整局部 coboundary，不是从两个一阶 finite
坐标猜二阶项消失。

在 $p$，$P_{0,p}=0$ 是原完整 cochain 恒等式。因此 cup 的一次
系数仅有
$$
P_{1,p}^\circ\cup\mathcal K_{{\rm glob},p}.
$$
其余 action/交叉项全都乘 $P_{0,p}$；它们是在这个 gauge 中
严格为零。$2$ 与其它地方由原局部 cohomology/支持消失。
全局 reciprocity 遂给
$$
\operatorname{inv}_{K_p}
 \bigl(P_{1,p}^\circ\cup\mathcal K_{{\rm glob},p}\bigr)=0 .
\tag{23}
$$

置 $d^\sharp=d_R+(11/2)d_0$。前稿的准确等式为
$\mathcal K_{\rm glob}=i\,\operatorname{res}_K d^\sharp$，
而 $P_1^\circ=(i/2)\overline{D_0^\circ}$。
点值的 $k$-linear pairing 因子就是
$-\overline{D_0^\circ}d^\sharp/2$。
取原 trace，并用 quadratic restriction 对 Brauer invariant
乘 $2$，(23) 等价地给
$$
\boxed{\langle D_{0,p}^\circ,d^\sharp_p\rangle_p=0.}
\tag{24}
$$
这里所需结论为零；两个明确的可逆因子都没有被当成新未知尺度。

## 7. 与已登记 I₀ 公式完全相合，没有新增数值

R779 的实际全局分解为
$$
d_R=13b\,d_q+B_Rd_0,\qquad
d_q=d_{\rm fl}+8d_0.
$$
将 (18)、(19) 代入 (24)，得到对所有 $b$ 成立的
$$
\boxed{
13b I_0+26\varepsilon b
       \left(18b+B_R+\frac{11}{2}\right)=0.
}
\tag{25}
$$
若 $b\ne0$，这精确是
$$
I_0/\varepsilon=32+7b-2B_R=32+25B_1,
\tag{26}
$$
因为 R779 的 $B_1=2b+24B_R$。这恢复原 R779/R776 已登记的
数值系数和其非零 $b$ 使用范围，而不提供新的 $b$。
若 $b=0$，(25) 是零等式，不能由此除以 $b$。

所以本稿具体完成的是：另一侧原支持 lift、真正的第二
obstruction/$p$-flat 分离，以及多一阶实际 Shapiro 数据作
除 $T^2$ 后的原互反连接。即使使用这条 shifted cup，
$a_q$、$B_R$ 和 $I_0$ 仍未被实际求值；(26) 不能再次作为
一条独立方程来解已有的同一个未知量。

## 引用

- [原 Shapiro 二阶类](2026-11-15-original-Robert-Shapiro-second-class.md)：原 $\Lambda^\#$、支持、局部自由性/全局单射、$\mathcal K_{\rm glob}$ 与 $a_q$。
- [R168](../results/R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md)，§2：原 local pairing、有限/奇异坐标及 quadratic restriction。
- [R200](../results/R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md)：原 $w_p=0$ cochain gauge、exact dual 与完整支持。
- [R743](../results/R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md)，§§1–2：支持空间、Poitou–Tate 与原 flat line。
- [R746](../results/R746-original-ordinary-coefficient-as-a-strict-p-bockstein-condition.md)，§§1–4：strict-$p$ iff $b=0$ 及 $26\varepsilon b$。
- [R752](../results/R752-exact-Gamma-scalar-exchange-with-the-retained-second-coefficient.md)，§§2–3：原 rational quadratic primitive、$\mathscr L_q$、$I_0$ 与 $20/23$。
- [R773](../results/R773-complete-ordinary-scalar-lattice-and-original-mixed-Robert-phase.md)，§2：同一原混合单位的全 residue。
- [R776](../results/R776-original-cochain-p-division-and-the-remaining-scalar-unit-coordinate.md)、[R779](../results/R779-original-real-Robert-class-and-two-p-local-obstruction-coordinates.md)：被 (25)–(26) 恢复的原比较与真实数值边界。
