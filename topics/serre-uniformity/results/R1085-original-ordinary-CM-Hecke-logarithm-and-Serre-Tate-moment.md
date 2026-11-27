# R1085 — 原 full-47 普通 CM 点的完整 $B_q$ 对数与 Serre–Tate 矩

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
作者：global_route；独立纸审：root、o2_high_coefficient。本文不执行数学程序。

本篇为原
$X=X_{\rm ns}^{+}(47)$、$J=\operatorname{Jac}(X)$
构造一个可实际求值的整对数来源。它不借用旧 tame-six 曲线
$X_1$ 的局部形式，也不把尚未公认的 Jaswal 预印本结论作为定理输入。

## 1. 原对象、条件与结论

令 $C_\infty$ 是原全部 $23$ 个 cusps 的和。这是次数 $23$ 的有理 divisor。
令 $y=c_J\in X(\mathbf Q)$ 是
[R1074](R1074-certified-original-p47-eight-CM-disks.md)
中的一个实际有理 CM 点。其 CM 阶记为 $\mathcal O$，二次域为 $K$；
$\mathcal O$ 的类数为一，$47$ 在 $K$ 惰性，且
$\mathcal O/47\mathcal O=\mathbf F_{47^2}$。
$y$ 的原 necklace 就是这个 CM Cartan。

本篇所用辅助素 $q$ 满足：

1. $q>3$，$q\ne47$，$q\equiv1\pmod {47}$；
2. $q$ 不整除 $\mathcal O$ 的 conductor，且在 $K$ 分裂；
3. 采用该 CM 点的一个在 $q$ 好约化的实际椭圆曲线模型。

在本轮已选择的 $q=4513$ 上，以上条件成立的六点是
$$
J=0,\ 1728,\ 8000,\ 54000,\ 287496,\ -12288000.
\tag{1085.1}
$$
这六点的普通性及其原 level 来源见
[R1083](R1083-original-level47-auxiliary-Hecke-fields-and-scalar-fibers.md)。
另外两个 $J=-3375,16581375$ 在 $4513$ 超奇异，不在本篇定理范围内。

定义原有理点及实际 Hecke 算子
$$
u_y=[23y-C_\infty]\in J(\mathbf Q),\qquad
B_q=q+1-T_q,\qquad z_y=B_q u_y.
\tag{1085.2}
$$
$T_q$ 采用次数 $q+1$ 的通常原同源对应；不除以 $q+1$。

令 $\mathcal J/\mathbf Z_q$ 为 $J$ 的好约化模型。取任意原整微分
$$
\omega\in H^0(\mathcal J,\Omega^1)
       =H^0(X_{\mathbf Z_q},\Omega^1).
$$
在 $\overline y$ 的一个有标记普通细变形圆盘上，取真正的
Serre–Tate 参数 $s$，使原 CM lift 为 $s=1$。
其系数环可取 $W=W(\overline{\mathbf F}_q)$，不要求这些 Tate bases
在 $\mathbf Z_q$ 上有理。把实际 coarse 微分拉回，写成
$$
\omega=f_\omega(s)\frac{ds}{s},\qquad
 f_\omega(s)\in W[[s-1]].
\tag{1085.3}
$$
只为提取形式 Taylor 系数，置
$$
g_\omega(t)=f_\omega(e^t).
$$
这里 $t$ 是形式变量；不在 $q$ 次单位根处使用
$t=\log s$ 作为一个可逆解析坐标。

本篇的结论是
$$
z_y\in\ker\bigl(J(\mathbf Z_q)\longrightarrow J(\mathbf F_q)\bigr),
\qquad \log_J z_y\in q\,\operatorname{Lie}(\mathcal J)(\mathbf Z_q),
\tag{1085.4}
$$
及准确的整首层恒等式
$$
\boxed{\quad
 q^{-1}\log_J(z_y)(\omega)
   \equiv 23\,[t^{\,q-2}]\,g_\omega(t)\pmod q.
 \quad}
\tag{1085.5}
$$
右侧由真 Serre–Tate 标记定义，且其模 $q$ 值与所有这类基变更无关；
若 $\omega$ 在 $\mathbf Z_q$ 上定义，其值属于 $\mathbf F_q$。
公式没有未确定的 period unit 或 stabilizer 除数。

(1085.5) 是原 $u_y$ 的对数公式，不宣称某个给定 Hecke block 上该值为零、
为单位或给出高度 valuation one。它也没有替代原 Mordell–Weil 格的饱和检验。

## 2. 原 CM lift、全部 $q+1$ 个目标与 level-47 运输

### 2.1 采用的已发表 Serre–Tate 来源

Katz, *Serre–Tate local moduli*, Lecture Notes in Mathematics **868**
(1981), pp. 138–202，作者
[完整扫描](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)，
Theorem 2.1，印刷 pp. 148–149，给出普通变形的双线性参数及同源提升条件
$$
q(A;\alpha,f^t\beta)=q(B;f\alpha,\beta).
\tag{1085.6}
$$
global_route 与 root 已亲读该定理及其构造，o2 已全文独核本篇。以下使用它对当前一维 split
$q$-divisible group 逐条计算，不引用其它未付款的普通 CM 对数定理。

因为 $\mathcal O\otimes\mathbf Z_q\simeq\mathbf Z_q\times\mathbf Z_q$，
两个幂等作用在原 CM lift 上，使其 $q$-divisible group 分裂。
选择 physical Tate bases 和相容的 torus 标记之后，
$$
G_y=\mu_{q^\infty}\times(\mathbf Q_q/\mathbf Z_q),\qquad s(y)=1.
\tag{1085.7}
$$
在 $W$ 上原 ordinary special fiber 的 connected 和 étale 两部分都得到
这种标记。无需、也不声称这些标记在有限层 $\mathbf Z_q$ 上恒定。

### 2.2 两个水平 CM 同源的原目标均为 $y$

$q$ 的两个素理想在类数一的阶 $\mathcal O$ 中主化；其生成元
$\alpha,\bar\alpha$ 的 norm 为 $q$。
相应两个 $q$-同源目标作为 CM 椭圆曲线均与原 $E_y$ 同构。

还必须核原 necklace。因 $q\ne47$，$\alpha$、$\bar\alpha$ 在
$\mathcal O/47\mathcal O=\mathbf F_{47^2}$ 中可逆；
它们在 $E_y[47]$ 上属于原 CM Cartan，并正规化同一个 necklace。
所以这两个目标作为原 $X$ 上的点都确为 $y$，不只具有相同 $j$。

一个水平 kernel 是 $\mu_q$；另一个是 (1085.7) 中的 split étale
$\mathbf Z/q$。前者的商仍是 split ordinary lift。
后者作为下面 $a=0$ 的情形也给 $s=1$。
这些断言包含原 level-47 数据。

### 2.3 其它所有 kernel 的参数

在 $W[\zeta_q]$ 上，除 $\mu_q$ 外的 $q$ 个 kernel 可准确写成
$$
C_a=\bigl\langle(\zeta_q^a,1/q)\bigr\rangle,\qquad
 a\in\mathbf F_q.
\tag{1085.8}
$$
这列出了 $G_y[q]$ 的全部其它 order-$q$ cyclic subgroups。

先采用商的直接标记。商 $G_y/C_a$ 的 étale 坐标相对原坐标乘 $q$。
将其 étale 的 $1/q^n$ 提升为原 split group 中的 $1/q^{n+1}$，
乘 $q^n$ 后所得 $(1,1/q)$ 在商中等于 $(\zeta_q^{-a},0)$。
因此其 Kummer extension 参数准确为 $\zeta_q^{-a}$。
这是 (1085.6) 的一维 extension 形式。

为了把所有目标送到原 $\overline y$ 的同一个细变形圆盘，
用 $a=0$ 的水平 CM 同源固定一次 special-fiber identification。
全部 $C_a$ 的 special fiber kernel 相同，故此 identification 对所有 $a$
相容。更改由它传输的 physical Tate bases，只把参数同时变为
$$
s_a=\zeta_q^{\beta a},\qquad \beta\in\mathbf Z_q^\times.
\tag{1085.9}
$$
同一个 $\beta$ 独立于 $a$；故全部参数的集合准确是全部 $q$ 次单位根。
不能在各分支另选互不相关的 period。

原 prime-to-$q$ level structure在无穷小变形上唯一提升；
水平 CM endomorphism 的 level-47 作用已在 §2.2 证明属于原 Cartan。
因此这些目标全部约化到原 coarse 点 $\overline y$。
选择 full level cover消去 automorphisms时，只是对同一个原
$q$-同源目标选有标记的表示，不更换原 necklace 或原对应。

### 2.4 原 Hecke cycle 与 cusp 项

$C_\infty$ 是单个次数 $23$ 的 Galois 轨道，$T_q$ 定义在 $\mathbf Q$ 上、
将 cusps 送至 cusps，并具有次数 $q+1$。
所以 $T_q C_\infty$ 中所有 cusp 的系数相同；比较总次数给
$$
T_q C_\infty=(q+1)C_\infty.
\tag{1085.10}
$$
这一步保留全部 $23$ 个 cusps，不以任取有理基点替换它们。

用 §2.2–2.3 的真实目标表示原 cycle，得到
$$
\begin{aligned}
z_y
 &=23\bigl((q+1)[y]-T_q[y]\bigr)\\
 &=23\left(q[1]-\sum_{a\in\mathbf F_q}[\zeta_q^a]\right)
  =23\left((q-1)[1]-\sum_{a\ne0}[\zeta_q^a]\right).
\end{aligned}
\tag{1085.11}
$$
此等式是在原 Jacobian 中，右侧通过实际细圆盘到 coarse $X$ 的映射读取。
重复目标按原 Hecke 对应的重数保留。

所有目标都在 $\overline y$ 的 tube，且原 cycle 次数零，故其 reduction 为零。
$z_y$ 本来定义在 $\mathbf Q_q$ 上，$J$ 在 $q$ 好约化，
因而第一条 (1085.4) 成立。对好模型的形式群，积分参数属于
$q\mathbf Z_q$；形式对数的各次分母至多该次数，
$q>3$ 时 $n-v_q(n)\ge1$，故第二条 (1085.4) 也成立。
下节还直接给出这个 $q$ 整除。

## 3. 一个自足的有界测度引理

本节说明为什么 (1085.11) 中的对数首层可以完整求出，
而不截掉可能通过积分分母下降的高项。

令 $W$ 为任意完备不分歧 $q$-adic valuation ring，
$f(s)=\sum_{n\ge0}c_n(s-1)^n\in W[[s-1]]$。
则存在唯一的有界 $W$ 值测度 $\mu$，使
$$
f(s)=\int_{\mathbf Z_q}s^x\,d\mu(x).
\tag{1085.12}
$$

这里“测度”是连续函数上的有界线性泛函，或等价的 clopen 集合上
有界有限可加分布；本证明不需要实分析式的可数可加性。
以下短证也固定需要的所有收敛约定。

对连续 $h:\mathbf Z_q\to W$，令
$a_n=\Delta^n h(0)$，$\Delta h(x)=h(x+1)-h(x)$。
有 $|a_n|\le\|h\|_\infty$。若 $h$ 的周期为 $q^r$，在这一有限周期空间上
$$
\Delta^{q^r}\equiv0\pmod q,
$$
因为 characteristic $q$ 下 $(T-1)^{q^r}=T^{q^r}-1$。
于是 $a_n\to0$。一般连续 $h$ 可一致逼近为局部常值的周期函数；
$\Delta^n$ 的算子范数至多一，所以仍有 $a_n\to0$。
Newton 恒等式先在非负整数上成立，再由稠密性和一致收敛得到
$$
h(x)=\sum_{n\ge0}a_n\binom xn.
\tag{1085.13}
$$
这也证明所需的 Mahler 展开，而不需要假定 $W$ 局部紧。

定义
$$
\int h\,d\mu=\sum_{n\ge0}a_n c_n.
$$
其级数收敛且范数至多 $\|h\|_\infty$。
取 $h(x)=\binom xn$ 得唯一性；
对任意固定 $|s-1|<1$，
$s^x=\sum_n\binom xn(s-1)^n$ 在 $x\in\mathbf Z_q$ 上一致收敛，
故可逐项积分，得到 (1085.12)。
这个证明允许把 $W$ 扩到包含 $\zeta_q$ 的有限分歧扩张再作同样积分。

若需经典来源，这正是 Mahler 连续展开的有界测度版本：
K. Mahler, “An interpolation series for continuous functions of a
$p$-adic variable”, *J. reine angew. Math.* **199** (1958), 23–34，
[原文扫描](https://carmamaths.org/resources/mahler/docs/139.pdf)。
本篇只使用上面已经重证的连续展开，不使用其它微分阶数结论。

## 4. 全部尾项的准确消去与首矩

把 $\mu$ 限制到 $\mathbf Z_q^\times$ 和 $q\mathbf Z_q$，分别记作
$\mu_\times$、$\mu_q$。

### 4.1 unit 部分

对 $|s-1|<1$，定义
$$
I_\times(s)=
 \int_{\mathbf Z_q^\times}\frac{s^x-1}{x}\,d\mu(x).
\tag{1085.14}
$$
$x^{-1}$ 在 units 上有界；二项展开和导数展开在每个
$|s-1|\le\rho<1$ 上一致收敛。因此
$$
dI_\times=f_\times(s)\frac{ds}{s},\qquad I_\times(1)=0.
$$
在 $s=\zeta_q^a$ 处，$s^x$ 是由 $x\bmod q$ 决定的连续角色。
故准确地有
$$
\sum_{a=0}^{q-1}\zeta_q^{ax}=0\quad(x\in\mathbf Z_q^\times),
$$
从而
$$
qI_\times(1)-\sum_{a=0}^{q-1}I_\times(\zeta_q^a)
   =q\int_{\mathbf Z_q^\times}x^{-1}\,d\mu(x).
\tag{1085.15}
$$
这是有界积分与有限和的交换，不是未经控制的高次 Taylor 截断。

### 4.2 $q\mathbf Z_q$ 部分

把 $\mu_q$ 通过 $x=qz$ 推至 $\mathbf Z_q$，得到有界测度 $\nu$，
并令 $h(r)=\int r^z\,d\nu(z)$。于是
$$
f_q(s)=h(s^q).
$$
取从 $r=1$ 出发的解析原函数
$H(r)=\int_1^r h(v)\,dv/v$。
这个原函数在开单位圆盘收敛：$h(v)/v$ 在 $v-1$ 中的系数有界，
逐项积分只引入正整数分母，其赋值仅以对数速度增长。
则
$$
I_q(s)=q^{-1}H(s^q),\qquad
dI_q=f_q(s)\frac{ds}{s},\qquad
I_q(\zeta_q^a)=0.
\tag{1085.16}
$$
其中可能出现的 $\log r$ 项同样在 $r=1$ 为零。
所以这一整部分的全部高项，在原根和中准确消失。

令 $I=I_\times+I_q$。
它是从 $s=1$ 出发的实际微分原函数。
形式 Abel–Jacobi 对数在同一个好约化 tube 内由这个原函数读取，
没有路径或额外 Coleman 常数。由 (1085.11)、(1085.15)–(1085.16)，
$$
q^{-1}\log_J(z_y)(\omega)
 =23\int_{\mathbf Z_q^\times}x^{-1}\,d\mu_\omega(x).
\tag{1085.17}
$$
这是 $W$ 中的**整等式**，比所需模 $q$ 公式更强。
它已包含全部积分尾项。

### 4.3 模 $q$ 的唯一首矩

作为 $\mathbf Z_q$ 上的连续函数，
$$
\mathbf1_{\mathbf Z_q^\times}(x)x^{-1}
 \equiv x^{q-2}\pmod q.
$$
在 $q\mathbf Z_q$ 上两边模 $q$ 都为零。
有界测度保这个整同余，所以
$$
\int_{\mathbf Z_q^\times}x^{-1}d\mu
 \equiv\int_{\mathbf Z_q}x^{q-2}d\mu\pmod q.
$$
将 (1085.12) 形式代入 $s=e^t$，对次数 $q-2<q$ 提取系数：
$$
[t^{q-2}]f(e^t)
 =\frac1{(q-2)!}\int_{\mathbf Z_q}x^{q-2}\,d\mu(x).
\tag{1085.18}
$$
这里只有小于 $q$ 的 factorial，均为整单位。
Wilson 给 $(q-2)!\equiv1\bmod q$。
(1085.17)–(1085.18) 正好证明 (1085.5)。

## 5. 标记、算术下降与两个特殊 CM coarse 点

### 5.1 不分歧标记与 $\mathbf F_q$ 下降

更换两个 physical Tate bases或其相容标记，使 $s_{\rm new}=s^a$，
其中 $a\in\mathbf Z_q^\times$。
于是 $t_{\rm new}=at$，实际微分的系数变换为
$$
[t_{\rm new}^{q-2}]g_{\rm new}(t_{\rm new})
 =a^{-(q-1)}[t^{q-2}]g(t)
 \equiv[t^{q-2}]g(t)\pmod q.
\tag{1085.19}
$$
同时 $\{\zeta_q^{ab}:b\in\mathbf F_q\}$ 仍是同一完整根集。
故 (1085.5) 不依赖任何这类选择。

由于 $\overline y$ 在 $\mathbf F_q$ 上定义，
算术 Frobenius 只把上述 Tate bases 变成其它 $\mathbf Z_q$-bases。
对在 $\mathbf Z_q$ 上定义的 $\omega$，
(1085.19) 说明首矩的 reduction 被 Frobenius 固定，因而属于 $\mathbf F_q$。
也可直接由 (1085.17) 左侧的原有理点及原整微分得到相同下降。
这里没有把一般 ST 标记假定为在有限不分歧层已有完整 Tate basis。

若以后改用代数 CM 参数、Weierstrass 参数或复 period 归一化，
必须另付它与 $s$ 的真实尺度。
(1085.19) 只支付 Serre–Tate Tate-base 变更，不准把任意形式参数的
tangent unit 当成全部高阶坐标变换。

### 5.2 $j=0,1728$ 的实际重数

令 $e=3$ 或 $2$，分别对应 $j=0$、$1728$。
在当前普通情形 $q$ 分裂于 CM 域，且 $q\nmid e$。
有效自同构群 $\mu_e$ 对细 ST 形式变量的作用为
$$
t\longmapsto \xi t,\qquad \xi^e=1,\quad\operatorname{ord}(\xi)=e.
\tag{1085.20}
$$
例如由 (1085.6)，CM unit 的两个 $q$-adic 分量之比给这个角色；
其阶分别为三或二。这不是任意指定的 coarse 参数。

coarse 整微分的拉回满足
$g(\xi t)\xi=g(t)$，故其可能的幂次为
$$
n+1\equiv0\pmod e.
$$
因 $q$ 在该 CM 域分裂，$e\mid q-1$，所以
$n=q-2$ 正是允许的幂次；不能由特殊自同构把 (1085.5) 误判为零。

$\mu_e$ 将非零的 $q$ 次根分成长度 $e$ 的 orbit。
原 Hecke 对应在 coarse curve 上，同一个目标确有相应重数 $e$：
它是对 $E_y$ 的全部 order-$q$ 子群推下所得 cycle，
而不是对子群的自同构轨道再赋重数一。
(1085.11) 已保每个子群一次，(1085.3) 又保原 coarse 微分的拉回。
因此无需、也不允许在 (1085.5) 额外除以二或三。
两个水平 CM 子群各给一次 $[y]$，同样已经保留。

## 6. 可消费的实际高度输入与仍未支付的量

定义原整线性泛函
$$
\lambda_{q,y}:
H^0(\mathcal J,\Omega^1)\longrightarrow\mathbf F_q,\qquad
\omega\longmapsto23[t^{q-2}]f_\omega(e^t)\bmod q.
\tag{1085.21}
$$
它准确等于 $q^{-1}\log_J(B_q u_y)$ 的 reduction。
故对已付款的原整 Hecke 幂等 $e_{\mathfrak m}$，可在实际 Hodge 格上限制
$\lambda_{q,y}$，检测这个**具体原有理点**在该块的对数是否更深入一层。
这里不需要预先除去 $23$ 个 cusp 常数，或先选择非有理的基点。

[R1081](R1081-certified-original-level47-Cartan-trace-and-integral-Hecke-algebra.md)
已经在 $4513$ 认证真实整 Hecke 代数及一次块；
[R1083](R1083-original-level47-auxiliary-Hecke-fields-and-scalar-fibers.md)
支付其原 Hodge/Lie 自由 rank-one 接口；
[R1080](R1080-certified-full-level47-Jacobian-rank.md)
支付完整 $J$ 的 Mordell–Weil rank $73$。
本篇补的是另一项独立输入：原普通 CM 有理点的整首对数来源。

下列问题仍须对同一个原来源分别完成：

- 六个普通点在所选整 Hecke blocks 上的 (1085.21) 实际值；
- 原 Mordell–Weil 格、其余 blocks 的饱和性及完整高度 pairing；
- $4513$ 处两个超奇异 CM 点的替代实际来源；
- 所需 Chow–Heegner divisor、对应的完整高度首项与 valuation one；
- 原八个 $47$-adic CM 圆盘内部的有理唯一性。

原坏 $47$ 项的同盘支撑避让已有 R1074 §9；
它不代替本节任何一个尚缺的好辅助素首项。
本篇不把对数公式、普通性或真一次 Hecke 块本身称为盘内排点，
更不将固定 $47$ 的进展当作全部 $p$ 的 Serre 一致性结论。
