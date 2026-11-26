# R986 — 原二次常数域的两平移绝对模型与完整商运输

日期：2026-11-26。会话：Astra-rank2-Sha-0b097461-20261127。
**状态：有限域构造及等价性已证明；独立 helper 仅作静态检查，尚未执行，未接入原 v8。**

本篇在 R974 已修正的实际原商 $k[t]/\pi$ 上给一个更具体的绝对有限域构造。
原常数域是 $k=\mathbf F_{r^2}$，有调用方指定的原 $\omega$。
两个元素 $t$ 与 $t+\omega$ 至少一个生成整个 $\mathbf F_{r^{2d}}/\mathbf F_r$。
由相应的 quadratic norm polynomial 可直接构造原生绝对域，
再显式恢复原 $\omega$ 和原 $t$。
此法不在大绝对域中对原 degree-$d$ 多项式列举全部根。

它只替换有限域的坐标模型，不替换任何原 thick quotient、
乘法矩阵、全长、相对 norm 或原常数目标。
当前公开运行 source `3b0fe32226b1f91ec37ef68a8d53ff865e9d9b26`
仍使用原 R974 构造；本文没有修改其生产源、增加作业或声称实际提速已测得。

## 1. 原商与全体真子域

令 $r\equiv2\pmod3$ 为素数，$r>3$，并保原常数域与元素
$$
k=\mathbf F_{r^2},\qquad
\omega\in k\setminus\mathbf F_r,\qquad
\omega^2+\omega+1=0.
\tag{1}
$$
生产原 $r$ 是29或41。
给定原 monic irreducible polynomial
$$
\pi(T)\in k[T],\qquad \deg\pi=d\ge1,
\qquad L=k[T]/(\pi),\qquad t=T\bmod\pi.
\tag{2}
$$
于是 $L$ 是 $r^{2d}$ 元域，$[L:k]=d$。

**引理1。** 对任意 $c\in\mathbf F_r$，令 $\theta_c=t+c\omega$。
若 $\mathbf F_r(\theta_c)\ne L$，则 $d$ 为奇数且
$$
\mathbf F_r(\theta_c)=\mathbf F_{r^d}\subset L.
\tag{3}
$$

**证明。** 设 $e=[\mathbf F_r(\theta_c):\mathbf F_r]$。
因 $t=\theta_c-c\omega$，有 $k(\theta_c)=k(t)=L$。
有限域中所有子域由其次数唯一决定，两个子域的合成次数为最小公倍数，故
$$
\operatorname{lcm}(2,e)=2d.
\tag{4}
$$
若 $e$ 偶，则左边为 $e$，故 $e=2d$，没有真子域。
若 $e$ 奇，则左边为 $2e$，故 $e=d$，且 $d$ 奇。
因此所有真子域的可能已经被(4)排尽，唯一剩余者正是(3)。证毕。

**引理2。** $\theta_0=t$ 与 $\theta_1=t+\omega$ 至少一个生成 $L/\mathbf F_r$。
若 $d$ 为偶数，则两者都生成。

**证明。** 偶数情形由引理1。
若两者都不生成，引理1迫使 $d$ 奇且两者都属于同一个
$\mathbf F_{r^d}$，故其差 $\omega$ 也属于该域。
但
$$
\mathbf F_{r^2}\cap\mathbf F_{r^d}
 =\mathbf F_{r^{\gcd(2,d)}}=\mathbf F_r,
\tag{5}
$$
与(1)矛盾。证毕。

这里不是只检查一个预选的真子域：引理1先由(4)证明不存在其它真子域可能。

## 2. 无需求根或扫描的确定平移

更具体地，
$$
\boxed{
c=\begin{cases}
0,&\pi\notin\mathbf F_r[T],\\
1,&\pi\in\mathbf F_r[T]
\end{cases}
\quad\Longrightarrow\quad
\mathbf F_r(t+c\omega)=L.
}
\tag{6}
$$

若 $t$ 不生成，由引理1它在 $\mathbf F_{r^d}$ 中，且其
$\mathbf F_r$-minimal polynomial 有次数 $d$。
该多项式在 $k[T]$ 中被 $\pi$ 整除，两者同为 monic degree $d$，故相等。
所以 $t$ 不生成必有 $\pi\in\mathbf F_r[T]$。
反之若 $\pi\in\mathbf F_r[T]$，它在 $k[T]$ 不可约，
在 $\mathbf F_r[T]$ 也不可约，故 $[\mathbf F_r(t):\mathbf F_r]=d$。
引理1还说明此时 $d$ 必为奇数；由引理2，$t+\omega$ 生成。
这证明(6)。

对原线性情形 $d=1$，R974 已直接返回同一个原 $k$ 对象；
helper 保留这条原路径，不为线性商新造绝对模型。

## 3. Norm polynomial 及原 $\omega$ 的准确恢复

取(6)的 $c$，唯一地写
$$
\pi(X-c\omega)=A_c(X)+B_c(X)\omega,
\qquad A_c,B_c\in\mathbf F_r[X].
\tag{7}
$$
$\pi$ monic 给
$$
\deg A_c=d,\quad A_c\text{ monic},\qquad \deg B_c<d.
\tag{8}
$$
由于 $\omega^r=\omega^2=-1-\omega$，系数 norm 是
$$
N_c(X)
 =\operatorname{Norm}_{k/\mathbf F_r}(\pi(X-c\omega))
 =A_c(X)^2-A_c(X)B_c(X)+B_c(X)^2.
\tag{9}
$$
它是 monic degree $2d$ 多项式。
$\theta_c=t+c\omega$ 使(7)为零，故 $N_c(\theta_c)=0$。
由(6)，$\theta_c$ 的 minimal polynomial 恰有 degree $2d$，
因此
$$
\boxed{N_c\text{ 在 }\mathbf F_r[X]\text{ 不可约。}}
\tag{10}
$$

置原生绝对域
$$
L^{\rm abs}=\mathbf F_r[X]/(N_c),\qquad a=X\bmod N_c.
\tag{11}
$$
首先 $B_c\ne0$：否则(9)为 $A_c^2$，与(10)矛盾。
又 $\deg B_c<d<2d=\deg N_c$，故 $B_c(a)\ne0$。
因此下面公式合法：
$$
\boxed{
w=-\frac{A_c(a)}{B_c(a)},\qquad t^{\rm abs}=a-cw.
}
\tag{12}
$$
把(9)在 $a$ 处的等式除以 $B_c(a)^2$，得到
$$
w^2+w+1=0.
\tag{13}
$$
由于 $r\equiv2\pmod3$，这个二次多项式在 $\mathbf F_r$ 上不可约，
故 $w\notin\mathbf F_r$。
原 $\omega\mapsto w$ 定义原域 $k$ 到 $L^{\rm abs}$ 的嵌入
$\iota_k$，而(7)、(12)给
$$
\iota_k(\pi)(t^{\rm abs})=0.
\tag{14}
$$
遂有 $k$-代数同构
$$
\boxed{
\Phi:L\longrightarrow L^{\rm abs},\qquad
\omega\longmapsto w,\quad t\longmapsto a-cw.
}
\tag{15}
$$
这里 $L^{\rm abs}$ 的 $k$-结构就是 $\iota_k$。
该同态非零且两域同为 $r^{2d}$ 元，所以为同构。

还有完全显式的反向描述：送 $a\mapsto t+c\omega$ 即给
$\Psi:L^{\rm abs}\to L$，由(7)和 $B_c(\theta_c)\ne0$ 得
$$
\Psi(w)=-A_c(\theta_c)/B_c(\theta_c)=\omega,
\qquad \Psi(t^{\rm abs})=t.
\tag{16}
$$
所以(15)–(16)在原 $\omega,t$ 上逐项往返，不是只说两个域有相同基数。

## 4. 对实际商接口、全坐标空间与 norm 的等价性

独立 helper 是
`scripts/original_quadratic_norm_field.py`。
其 `OriginalQuadraticNormFiniteFieldQuotient` 接受
**原 polynomial 对象、原 $\omega$ 对象和 tag**；
原 $k[T]/\pi$、原 polynomial ring 与原 base field 对象全部保留。
系数 $b_0+b_1\omega$ 依(15)送到 $b_0+b_1w$。

实现随后沿用 R974 的完整 $k$-basis
$$
1,t^{\rm abs},\ldots,(t^{\rm abs})^{d-1},
\tag{17}
$$
建立 `forward/backward`，并保原全部往返：

- 原商的全部 $d$ 个 power-basis 元素；
- 原生绝对域的全部 $2d$ 个 $\mathbf F_r$-basis 元素；
- 原 base 的完整二元 basis 和调用方指定的原 $\omega$；
- `lift(root)=T mod pi`、`reduce(lift(value))=value` 的原接口。

`make_original_quadratic_selector` 只返回一个显式 constructor，
不会自行安装 class bindings。
仅当调用 polynomial 的 base **就是调用方的原 $k$ 对象** 时才用新分支；
其它已生成 residue fields 上的更高 tower 仍退回原 R974 constructor。
因此不把本二次常数域证明误用到一般高次 base field。

设 $M$ 为原 $L$ 上任意完整有限维乘法矩阵。
逐项经(15)运输，由 determinant 的多项式定义有
$$
\det(\Phi(M))=\Phi(\det M).
\tag{18}
$$
相对 field norm 同样满足
$$
\operatorname{Norm}_{L^{\rm abs}/\iota_k(k)}(\Phi(x))
 =\iota_k\bigl(\operatorname{Norm}_{L/k}(x)\bigr),
\tag{19}
$$
因为它就是相应 $k$-linear multiplication determinant。
或者由有限域显式式子
$\operatorname{Norm}_{L/k}(x)=x^{(r^{2d}-1)/(r^2-1)}$ 直接核对。
最后通过 `lift` 返回的是原 $k$ 元素，未取到 $\mathbf F_r$ 的额外 norm。

若这个 residue factor 在原 nonreduced Artin algebra 中有厚度 $m$，
其对完整 norm 的贡献是(19)的 $m$ 次幂。
模型同构不改变 $m$、residue degree $d$、原全 $k$-length，
也不删除 nilpotents 的 contribution。
故 R931/R974 的全部厚 norm 与全 trace 可原样使用此坐标模型。

## 5. 实现状态及后继接入边界

R974 当前使用“先造绝对域，再把原 $\pi$ 运入其中并列举全部根”的构造。
本篇给(9)的已知 irreducible 绝对 modulus 以及(12)的指定根；
其替换工作是两次原系数多项式运算、一个 norm polynomial、一次有限域除法，
并保 R974 原有的完整 coordinate transport。
这从算法上删除了“大绝对域内 degree-$d$ 全根列举”这个步骤。
本篇没有声称它一定支配当前全作业时间，或给出未经实际运行的加速倍数。

helper 不被当前任何 producer/workflow import，也未运行数学实例。
当前 v8 仍唯一运行，source/run/job 为
$$
\begin{gathered}
\texttt{3b0fe32226b1f91ec37ef68a8d53ff865e9d9b26},\\
\texttt{45882239615}/\texttt{140124138541}.
\end{gathered}
$$
后续只有实际阶段需要此替换时，才在新的 source 中显式接入并记录真实结果。
本篇不把 helper 的静态 AST 检查写成 Sage PASS，
不将其写成原两图、七映射、四全厚交或原 shadow 的完成回执。

## 6. 引用范围

1. [R974](R974-original-residue-native-model-and-complete-norm-return.md)：
   原 Sage 非素 base 的 relative/native 失配、完整原商运输和相对 norm 目标。
2. SageMath 的有限域 constructor 官方文档：
   [Finite fields](https://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_constructor.html)，
   指定 prime-field modulus 生成 native absolute field。
   本课题实际执行版本仍为 pinned Sage 10.6；本文未声称新 helper 已在那里运行。
3. 有限域子域唯一性、合成域次数公式，以及(7)–(19)的全部新增代数推导已在正文给出。

本文无新数学运行、无新 job、无原生产源修改、无可重算数据输出。

独占 helper 的 SHA-256 为 `36cab0960c86ad7203db43f7ab52c5a2832e818c29a276b15f775adee1a2d0f6`；本次仅解析 AST，未执行 Sage 或实例。
