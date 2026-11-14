# R88 后续：全族四次 Frobenius 条件与实际 Mordell–Weil 筛

**状态：下列必要条件和维数断言已证明；尚无变化参数的统一排除。**
R88 已排除 R53 原来的三次域，不再继续把它的三条射线类关系当作必须先解决的门槛。

## 1. 固定 CM 三族的准确模 4p 条件

设 $p>37$、$p\equiv3\pmod4$，存在一条 R19 的实际原始曲线 $E$，相应数据为 $(X,W,Z)$。取
$$
\ell\equiv1\pmod8,\qquad \ell\nmid pZ,
$$
并假定 $E[2]$ 的三次多项式在 $\mathbb F_\ell$ 上不可约，即相应 $S_3$ Frobenius 为 $3$ 循环。

记
$$
b_\ell=a_\ell(A),\qquad A:y^2=x^3-x,
$$
$$
\varepsilon=
\begin{cases}
1,&\text{族 I、III},\\
2,&\text{族 II}.
\end{cases}
$$
此时 $\varepsilon Z$ 模 $\ell$ 为平方，定义
$$
s_\ell=(\varepsilon Z)^{(\ell-1)/4}\in\{1,-1\}.
\tag{Q1}
$$
则
$$
\boxed{a_\ell(E)\equiv b_\ell-p s_\ell\pmod{4p}.}
\tag{Q2}
$$

**证明。** R19 的精确极小判别式分别为
$2^6Z^p,2^9Z^p,2^{12}Z^p$。不可约三次式的判别式为平方，而 $2$ 在 $\ell\equiv1\pmod8$ 时也是平方，故 (Q1) 有定义。四次符号在平方上只有 $\pm1$；因为 $p$ 奇，
$$
\chi_4(2^6Z^p)=\chi_4(Z),\qquad
\chi_4(2^9Z^p)=\chi_4(2Z),\qquad
\chi_4(2^{12}Z^p)=\chi_4(Z).
$$
R88 引理 88.1 给 $a_\ell(E)\equiv-s_\ell\pmod4$。

另一方面，$A$ 在奇素数的好约化有全部有理 $2$ 挠点，所以
$b_\ell\equiv\ell+1\equiv2\pmod4$。由全局挠点同构写
$$a_\ell(E)=b_\ell+k p.$$
模 $4$ 给 $2-k\equiv-s_\ell$，等价于 $k\equiv-s_\ell\pmod4$（$s_\ell=\pm1$）。这正是 (Q2)。

注意这里保留的是完整的 $Z$。若 $Z=d z_0^2$，则在 $\varepsilon d$ 为平方的地方
$$
\chi_4(\varepsilon Z)=\chi_4(\varepsilon d)
\left(\frac{z_0}{\ell}\right).
$$
不能只用平方自由部分或三次域判别式替代 (Q1)。

### 1.1 小窗口内确实只允许指定的一支

若进一步 $\ell<p^2/4$，Hasse 界给
$|a_\ell(E)|,|b_\ell|<p$。由于前者为奇数、后者为偶数，$k$ 为奇数，且 $|k|<2$。因此 (Q2) 迫使
$$
\boxed{a_\ell(E)=b_\ell-p s_\ell.}
\tag{Q3}
$$
$A$ 在 $\ell\equiv1\pmod4$ 处普通，$b_\ell\ne0$；也可由
$b_\ell\equiv2\pmod4$ 直接看出非零。结合 Hasse 界，(Q3) 必须满足
$$
s_\ell=\operatorname{sgn}(b_\ell),\qquad
p\le |b_\ell|+2\sqrt\ell.
\tag{Q4}
$$
若符号相反，$|b_\ell-p s_\ell|=p+|b_\ell|>2\sqrt\ell$；符号相同后则得到第二个不等式。这严格选定 $a_A+p$ 和 $a_A-p$ 中的一支。

一般不必限定 $\ell<p^2/4$：计算同余类 $b_\ell-p s_\ell\bmod4p$ 的最小绝对值 $d_\ell$，若
$$d_\ell^2>4\ell,$$
就排除该处的 $3$ 循环。R88 的 $521$ 正是 $d_{521}=65$ 的实例。

但这个单独的同余—Hasse 筛有一个准确的有限范围：$d_\ell\le2p$，所以当 $\ell\ge p^2$ 时，必有 $d_\ell^2\le4\ell$。不能把这项条件本身说成对任意大辅助素数持续排除的障碍。

## 2. 接到 R46 的真实全局字符空间

固定 $Z,p$ 和分支，令 $F$ 为 R46 的二次预解式域，$V$ 为带原有分歧、指定分裂条件的三次字符空间。取满足 (Q1) 的辅助素数 $\ell$，并假设模 $4p$—Hasse 筛排除了 $3$ 循环。

因为判别式在 $\ell$ 为平方，Frobenius 只能是单位元或 $3$ 循环。故每个实际候选字符必满足
$$
\kappa(\mathfrak l)=0\qquad(\mathfrak l\mid\ell\text{ 于 }F).
\tag{Q5}
$$
两个上方素理想的字符值互为相反数，取核与选择无关。因而可把实际允许的全局空间替换为
$$
V^{\rm new}=V\cap\bigcap_{\ell\text{ 被筛定}}
\ker\operatorname{ev}_{\mathfrak l},
$$
$$
W^{\rm new}=W\cap\bigcap_{\ell\text{ 被筛定}}
\ker\operatorname{ev}_{\mathfrak l},
\qquad W=V\cap\delta(D_Z(\mathbb Q)).
\tag{Q6}
$$
这是对真正类群字符及真正有理点像的线性筛，不能将它的核自动认作零。

### 2.1 R53 原来的 Z：恰好切去一个真实有理点方向

仍取 R53 的完整 $Z=-q$ 和 $c=1$ 普通分支，但此处允许该分支的其他候选三次域。$521$ 在
$F=\mathbb Q(\sqrt{-q})$ 中分裂，而且 R88 的迹矛盾排除了任何实际候选的 $3$ 循环。因此所有实际字符都必须落在
$$W_1^{\rm new}=W_1\cap\ker\operatorname{ev}_{\mathfrak l_{521}}.$$

R53 已知点
$$P=(3,108n)\in D_Z(\mathbb Q),\qquad
D_Z:y^2=x^3+27q$$
满足 $\delta(P)=\pm\kappa\ne0$。其三次代数在 $521$ 不可约，所以
$\operatorname{ev}_{\mathfrak l_{521}}(\kappa)\ne0$。由此严格得到
$$
\boxed{\dim W_1^{\rm new}=\dim W_1-1.}
\tag{Q7}
$$
不需要计算 Mordell–Weil 基，也不需要知道 $\dim W_1$ 的具体值。若 $d=\dim W_1$，原有 $(3^d-1)/2$ 个非零射影字符，经这一个新条件后只剩
$\bigl(3^{d-1}-1\bigr)/2$ 个。$d=1$ 时这已经排除该 $Z$ 的全部 $c=1$ 普通候选；目前没有证明 $d=1$。

### 2.2 如果同一个 Z 还有实际解，辅助曲线的有理秩至少为二

**必要条件。** 若 R19 的 $c=1$ 分支对这个 $p=43,Z=-q$ 仍有实际原始解（来自其他三次域），则
$$\operatorname{rank}D_Z(\mathbb Q)\ge2.$$

**证明。** 相应有理点 $Q\in D_Z(\mathbb Q)$ 的非零三次类属于
$W_1^{\rm new}$。非零性是 R37 的实际三次多项式不可约性；不能用三次类为零的可约代数代替候选域。由于 $\delta(P)$ 在 $521$ 评价非零而 $\delta(Q)$ 评价为零，这两个类在
$D_Z(\mathbb Q)/\phi B_Z(\mathbb Q)$ 中线性独立。

两条曲线 $B_Z:y^2=x^3-q$ 和 $D_Z$ 都没有有理 $3$ 挠点。可直接使用
$\psi_3=3x(x^3+4b)$：$x=0$ 所需的 $b$ 不是有理平方，而另一支的 $x^3$ 在素数 $q$ 处赋值为 $1$，不可能为有理立方。任意非 $3$ 阶挠点部分在 $\phi$ 下同构。

在秩同为 $r$ 的自由部分上，$\widehat\phi\phi=[3]$ 说明 $\phi$ 的余核为一个维数不超过 $r$ 的 $\mathbb F_3$ 空间。因此两个独立的实际有理点类迫使 $r\ge2$。证毕。

这个结论没有把 Selmer 维数认作 Mordell–Weil 秩。它只使用两个真正有理点类的独立性；也没有假设 $P$ 是生成元或原始点。反之，当前没有辅助曲线秩至多一的已证上界，故不能据此宣称该分支已排除。族 II 的 $c=8$ 对应另一条辅助曲线 $D_{8Z}:y^2=x^3+216q$，即这里的二次扭曲；已知点 $P$ 不能自动移到那条曲线，本段不对其宣称同样的秩下界。

## 3. 全局四次互反接口尚未补上的部分

四次符号来自实际 $4$ 挠点的二进层，可在
$$K_4=\mathbb Q(i,\sqrt[4]{\Delta_E})$$
中解释。它包含 $F=\mathbb Q(\sqrt{\Delta_E})$，而 $K_4/F$ 是二幂次数扩张。候选分裂域 $H/F$ 则为循环三次扩张。因此
$$H\cap K_4=F.$$
这仅由次数互素即成立；不能把四次互反本身当成一个迫使非零三次字符消失的类群恒等式。

真正新增的是 (Q2) 把两个不同层的 Frobenius 与同一条椭圆曲线的整数迹相连。当前用于排除的仍是有限的 Hasse 窗口，以及由它产生的真实 Mordell–Weil 评价核。还没有得到控制变化 $Z$ 的高度、全部分母支撑或该核维数的统一结论。后续应寻找这一缺口的全局输入，不能把 (Q7) 的一次降维或互素次数的独立性扩大为 Serre 一致性证明。
