# R171：主化轨道的自局部公式与一个完整 Tate 斜率证书

本文接续 [R168](R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md)。
它把 R168 中尚未求值的、在 $q$ 处分歧的 $S$-单位行真正算出：
在 $p=43$ 的一个明确素数 $q$ 上，唯一全局单位行的局部值为零，
而规范化的自局部斜率为

$$
\lambda_q=16\in\mathbf F_{43}.
\tag{171.1}
$$

这里有一个需先保留的范围边界：此 $q$ 的 Gaussian $5$ 行非零，
已经违反 R157 的实际小素数迹条件。
所以本文给出真实 $q$-单位、精确根标签和自局部求值的首个完整证书，
不把这个 $q$ 宣称为实际椭圆曲线的存活支撑，更不宣称得到了统一排除。

三个文件组成完整记录：

- 本文；
- [标准库核验器](../notes/verify_r171_principal_norm_selflocal.py)；
- [整数、CM 模型、素性链及有限域证书](../notes/r171_principal_norm_selflocal_certificate.json)。

核验器复用 R161 的标准库有限域和椭圆曲线算术。
没有类群、基本单位、Mordell–Weil 群或高精度局部主化的计算假设。

## 1. 所计算的对象

沿用 R161、R163、R168 的记号：

$$
A:y^2=x^3-x,\qquad K=\mathbf Q(i),\qquad p=43,
$$

$$
T=K(A[p]),\qquad
\mathscr F=T^{\mathbf F_p^\times},\qquad
C=\operatorname{Gal}(\mathscr F/K)\simeq C_{44}.
\tag{171.2}
$$

取复共轭 $\tau$，以及 $0\ne P\in A[p]^{\tau=1}$。
在基 $(P,iP)$ 中，令

$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
F=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
K_0=JF=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{171.3}
$$

为避免把数域 $K$ 与矩阵混淆，本文把 R168 的矩阵 $K_q$ 写作 $K_0$。
对 $z=a+bi\in\mathbf F_{p^2}$，

$$
D_z:v\longmapsto z\bar v=aF+bK_0
\tag{171.4}
$$

给出二维分量 $W$。Cartan 元 $a$ 在 $W$ 上作用为
$z\mapsto a^{1-p}z$。

R163 已证明真正的全局单位线就是

$$
\mathcal D_p\simeq
(\mathcal O_{\mathscr F}^\times/\mathcal O_{\mathscr F}^{\times p}
\otimes W)^{\operatorname{Gal}(\mathscr F/\mathbf Q)},
\qquad \dim\mathcal D_p=1,
\tag{171.5}
$$

并且原始 Robert $11$-单位给出其生成元。
本文的素数 $q\equiv-1\pmod{4p}$ 满足

$$
\operatorname{loc}_q\mathcal D_p=0.
\tag{171.6}
$$

因此，在允许 $q$ 处分歧的对偶空间中，取奇异坐标为 $F$ 的
$q$-单位类 $d_q$。其有限坐标

$$
\operatorname{loc}^{\mathrm{fin}}_q(d_q)=\lambda_qK_0
\tag{171.7}
$$

不依赖 $d_q$ 加上全局单位线的选择。这正是 R168 §7 的斜率，
不是一个任意主化元依赖的剩余符号。

局部规范固定为

$$
\zeta_q=e_A(P,iP),\qquad
e_{\mathrm{Tate}}(\zeta,t^{1/p})=\zeta,
\tag{171.8}
$$

并使用 arithmetic Frobenius。改变 $P$ 为 $cP$ 会把
$\lambda_q$ 乘上 $c^{-2}$；本文的数值由证书中的确定点 $P$ 固定，
而零性和平方类不依赖这一缩放。

## 2. 主化元给出的轨道和：为什么不除以 $44$

下列构造不局限于本次的具体大素数。
设 $H=\mathscr F^{\langle\tau\rangle}$，$q\equiv-1\pmod{4p}$，
并选定 $\mathscr F$ 在 $q$ 上、分解群为 $\langle\tau\rangle$ 的素点。
其在 $H$ 中的下方素理想记为 $\mathfrak q$。
于是

$$
H_{\mathfrak q}=\mathbf Q_q,\qquad
\mathscr F_\lambda=\mathbf Q_{q^2},
\tag{171.9}
$$

而 $q$ 在 $K$ 上的素理想完全分裂于 $\mathscr F/K$。

假设有 $p\nmid h$ 以及 $\alpha\in\mathcal O_H$，使

$$
(\alpha)=\mathfrak q^h.
\tag{171.10}
$$

取 $\sigma\in C$，在 $W$ 上对应乘以 $\omega$；$\omega$ 的阶为
$p+1$。则

$$
d_q=\frac1h\sum_{j=0}^{p}
 [\sigma^j\alpha]\otimes D_{\omega^j}
\tag{171.11}
$$

是一个真正的全局 $q$-单位 Kummer 类。

证明有三个独立步骤。

首先，$\sigma$ 同时把两个因子的下标增加一，所以和式对 $C$ 不变。
又因为 $\alpha\in H$、$\tau\sigma\tau=\sigma^{-1}$，
$\tau$ 同时把 $\sigma^j\alpha$ 和 $\omega^j$ 变成下标 $-j$ 的项。
因此 (171.11) 也对 $\tau$ 不变，下降到 $\mathbf Q$。
这里 Kummer 类的自然作用是 $[u]\mapsto[\tau u]$；
系数中的 cyclotomic twist 已经包含在 Kummer 的 $\mu_p$ 中，
不能再人为添加一个复共轭负号。

其次，$C$ 在 $q$ 上的 $p+1$ 个素点上正则作用。
在基点 $\lambda$ 处，(171.11) 只有 $j=0$ 项有非零赋值，且等于 $h$。
因此它的奇异坐标恰为 $D_1=F$。
这说明公式中需要 $h^{-1}$，**不需要再乘 $(p+1)^{-1}$**。
若把轨道和误当成未归一化的全群平均，就会改变所求斜率。

最后，所有共轭只在 $q$ 上有赋值；其余 $2,p$ 外局部 Kummer 类均不分歧。
$p$ 处本来没有对偶局部限制，$2$ 处由 R161 的 $H^1(W(1))=0$ 处理。
所以 (171.11) 确实落在 R168 的同一个 $\mathcal D_{p,\{q\}}$ 中。

## 3. 自局部值只需 $21$ 个单位符号

写

$$
\alpha_j=\sigma^j\alpha\pmod\lambda,\qquad
\ell(u)=\log_{\zeta_q}\!\left(u^{(q^2-1)/p}\right)
\quad(u\in\mathbf F_{q^2}^\times).
\tag{171.12}
$$

除 $j=0$ 外，全部 $\alpha_j$ 都是单位。
在未分歧二次域 $\mathbf Q_{q^2}$ 上，对偶类的有限值为

$$
\frac1h\sum_j\ell(\alpha_j)D_{\omega^j}.
\tag{171.13}
$$

从 $\mathbf Q_q$ 限制到未分歧二次扩张时，
有限类的 Frobenius 值乘以 $1+\operatorname{Frob}_q$。
在 $W(1)$ 的正特征线 $\mathbf F_p K_0$ 上，这个因子是 $2$。
故 R168 的 $\mathbf Q_q$ 斜率为

$$
\boxed{
\lambda_q=\frac1{2h}\sum_{j=1}^{p}
\operatorname{Im}(\omega^j)\ell(\alpha_j).
}
\tag{171.14}
$$

这一步的 $1/2$ 来自限制映射，不来自群平均。

坏项 $j=0$ 不造成高精度局部计算：$D_1=F$ 没有 $K_0$ 分量。
更具体地，$\alpha/q^h\in H_{\mathfrak q}^\times=\mathbf Q_q^\times$，
其剩余类属于 $\mathbf F_q^\times$，而 $p\nmid q-1$，
所以它的 $p$ 次剩余符号已经为 $1$。
中央项 $j=(p+1)/2$ 同样由复共轭固定，且 $\omega^j=-1$，
也不贡献 $K_0$ 分量。

对其余各项，

$$
\alpha_{-j}=\alpha_j^q,\qquad
\ell(\alpha_{-j})=-\ell(\alpha_j),\qquad
\operatorname{Im}(\omega^{-j})=-\operatorname{Im}(\omega^j).
\tag{171.15}
$$

因此，取 $p=43$、$h=1$ 后，(171.14) 化成

$$
\boxed{
\lambda_q=\sum_{j=1}^{21}
\operatorname{Im}(\omega^j)\ell(\alpha_j).
}
\tag{171.16}
$$

以上推导同样适用于一般 $p\equiv3\pmod4$ 的主化见证 (171.10)。
它没有把“$S$-单位存在”替换成一个未经主化的形式符号。

## 4. $44$ 次域及其正确的二同源标记

### 4.1 环类域与原始实 $p$ 点

R163 给出 $\mathscr F$ 的导子为 $(1+i)^2p$。
把射线群进一步除以有理剩余单位，得到 $K=\mathbf Q(i)$ 中
导子 $2p=86$ 的环类域。其类数为

$$
h(-16p^2)=\frac{2p}{2}\left(1+\frac1p\right)=p+1=44.
\tag{171.17}
$$

所以 $\mathscr F/K$ 正是这个环类域。
$H=\mathscr F^{\langle\tau\rangle}$ 是 $44$ 次固定子域；
它并非全实域，本文不使用全实域的单位或范数下界。

对 $A$ 的有理二挠点 $(1,0)$ 作二同源，得到

$$
B:y^2=x^3-11x-14,
\qquad
\phi_2(x,y)=
\left(x+\frac2{x-1},\ y\left(1-\frac2{(x-1)^2}\right)\right).
\tag{171.18}
$$

对偶二同源的核点为 $(-2,0)$。因此本文始终保留
“$B$ 加上这个指定二挠点”的标记。

若 $A(\mathbf C)$ 的格为 $\Omega(\mathbf Z+i\mathbf Z)$，
则 $B$ 的格为 $\frac\Omega2(\mathbf Z+2i\mathbf Z)$。
原始实 $p$ 点产生的商 $B/\langle\phi_2(P)\rangle$
对应格参数 $2pi=86i$，所以是导子 $86$ 的主 CM 类。
这把复共轭固定的 $H$、原始实点和环类群的基点接在一起。

### 4.2 Hauptmodul 与较小的整模型

把指定二挠点平移到原点，写成

$$
y^2=x^3+a_2x^2+a_4x.
$$

采用

$$
\delta=\frac{16(a_2^2-4a_4)}{a_4},\qquad
j=\frac{(\delta+16)^3}{\delta}.
\tag{171.19}
$$

源曲线 $B$ 给 $a_2=-6,a_4=1$，故 $\delta=512$，
$j=287496$，与所选二同源标记一致。

令 $G$ 为判别式 $-29584$ 的 $\gamma_2=j^{1/3}$ 类多项式，
即 PARI/GP 2.19.0 的 `polclass(-29584,5)`。
取

$$
t^3=\delta,\qquad \gamma_2=t^2+16/t.
\tag{171.20}
$$

多项式 $t^{44}G(t^2+16/t)$ 的两个不可约因子次数分别为 $44$ 和 $88$。
次数 $44$ 的因子 $W(t)$ 对应唯一上行二同源标记：
目标从导子 $86$ 上行到导子 $43$。
其余两个二同源标记下行到导子 $172$，给次数 $88$ 的部分。
这个区分保留了源曲线的二同源标记，不能任意拿一个 $j$ 共轭代替。

证书保存一个更小的整生成元 $y$ 及其首一多项式 $P$，
还有完整的有理多项式 $t=t(y)$。核验器逐整数检查

$$
P(y)=0,\qquad W(t(y))=0,\qquad
W(t)\mid t^{44}G(t^2+16/t).
\tag{171.21}
$$

它还用模 $5$ 的 Rabin 判据证明 $P$、$W$ 都不可约，
从而上述有理多项式确给出相同的 $44$ 次域，
不是数值识别出的一个近似同构。

构造这个模型时可以调用 `polredbest`，但最终证书不依赖其选择过程。
也不需要声称 $\mathbf Z[y]$ 已经是最大整环：
$y$ 的整性和一个素数范数已经足够完成下一节的主化证明。

这里还须固定这个多项式生成元的全局嵌入。
先把 $H_0=\mathbf Q[Y]/(P)$ 看成抽象域，记其元素为 $y$。
在复数端取先前的实点 $P\in A[p]^{\tau=1}$，令 $\delta_\infty$
为带标记商 $B/\langle\phi_2(P)\rangle$ 的真实 Hauptmodul 值，
$t_\infty$ 为它的实立方根。
CM 的上行二同源标记使 $W(t_\infty)=0$。
因为 $t(y)$ 给出 $H_0\simeq\mathbf Q[t]/(W)$，要求

$$
\iota_\infty(t(y))=t_\infty
\tag{171.21a}
$$

唯一确定一个复嵌入 $\iota_\infty$。
反向的域同构也是有理多项式，所以 $\iota_\infty(y)$ 为实数。
这个嵌入把 $H_0$ 识别为已经固定的 $\mathscr F^{\langle\tau\rangle}$，
且其模含义是主 CM 类；不是先在有限域任意挑一个根再称它为实生成元。

### 4.3 Artin 方向与全部根标签

取 Gaussian primary 素元

$$
\beta=-1+2i,\qquad N\beta=5.
$$

它在 $A[p]$ 上的 arithmetic Frobenius 作用就是乘 $\beta$。
在 $W$ 上，

$$
\omega=\beta^{1-p}=8+25i\pmod{43},\qquad
\operatorname{ord}(\omega)=44.
\tag{171.22}
$$

因此 $\sigma=\operatorname{Frob}_{(\beta)}$ 生成 $C$，且
$\sigma^j$ 对应 $p$-子群 $\langle\beta^jP\rangle$。
这里使用与 R70、R161 相同的正向 primary 值，
没有只在标签一侧取 Artin 的逆。

在选定的有限素点上，核验器用精确 Vélu 公式计算全部

$$
B/\langle\phi_2(\beta^jP)\rangle\quad(0\le j<44),
\tag{171.23}
$$

并把指定二挠点 $(-2,0)$ 的像一并计算。
所得 $44$ 个 $\delta_j$ 与 $P$ 的 $44$ 个有限域根通过
$t(y)^3=\delta_j$ 一一匹配。
程序逐项检查方程、判别式非零、$j$ 恒等式、全部根互异以及

$$
y_{-j}=y_j^q,\qquad t_{-j}=t_j^q,\qquad y_{j+22}=-y_j.
\tag{171.24}
$$

这给出了整个轨道的确定标签，排除了事后任意排列共轭根的问题。

由于 $q\equiv-1\pmod{4p}$，$A[p]$ 在 $\mathbf F_{q^2}$ 上全有理，
$P$ 在 Frobenius 正特征线上。任意非零这样的有限域 $P$
都可由一个全局实 $p$ 点在适当素点处约化得到：
先把分解群共轭为 $\langle\tau\rangle$，再用与 $\tau$ 交换的
Cartan 标量调整正特征线上的点。
所以本次有限域标签确实来自同一个全局 $(P,iP)$，
而不是仅有形式相似的两套局部基。

更明确地，在上述全局嵌入 (171.21a) 固定后，
取使 $P$ 约化为证书中确定点的 $q$ 进嵌入 $\iota_q$。
模函数的代数相容性给

$$
\iota_q(t(y))^3
=\delta\bigl(B/\langle\phi_2(\bar P)\rangle,
             \overline{(-2,0)}\bigr).
\tag{171.24a}
$$

核验器证明右侧在 $P$ 的全部 $44$ 个根中有且只有一个匹配根，
故所得到的 $y_0$ 必定就是 $\iota_q(y)$。
$by_0=-1$ 是对这个已经固定的全局 $y$ 的计算结论。
之后取 $\alpha=by+1$，同时满足 $\alpha\in\mathscr F^{\langle\tau\rangle}$、
主 CM 类标记和所选 Frobenius 正特征线的约化要求。
其中用来调整 $\bar P$ 的 Cartan 标量作用在 $\mathscr F$ 上平凡，
因此不会再改变这个 $H$ 的嵌入。

## 5. 直接素数范数：不计算类群

证书的首一偶多项式为

$$
\begin{aligned}
P(Y)={}&Y^{44}-516Y^{40}-1290Y^{38}+59598Y^{36}+181116Y^{34}\\
&+2577721Y^{32}+46646916Y^{30}-976456083Y^{28}
-20137370592Y^{26}\\
&+14674269870Y^{24}+1927690658502Y^{22}
+8363579844980Y^{20}\\
&-77712625260012Y^{18}-678942658978083Y^{16}
-587754638748720Y^{14}\\
&+9635082255131184Y^{12}+911498768381760Y^{10}
-169912046493421984Y^8\\
&-535805618873718528Y^6-409760104149073152Y^4
+73719539004745728Y^2\\
&-3026144574634752.
\end{aligned}
\tag{171.25}
$$

取

$$
b=89460,\qquad q=-b^{44}P(1/b).
\tag{171.26}
$$

$q$ 是证书中逐位给出的 $776$-bit 正整数，满足

$$
q\equiv-1\pmod{172},\qquad
v_{43}(q+1)=1,\qquad
\frac{q+1}{43}\equiv11\pmod{43}.
\tag{171.27}
$$

所选有限域 CM 基点满足 $by_0=-1$，所以取

$$
\alpha=by+1.
\tag{171.28}
$$

由于 $P$ 为偶多项式且次数为偶数，

$$
N_{H/\mathbf Q}(by+1)=b^{44}P(-1/b)=b^{44}P(1/b)=-q.
\tag{171.29}
$$

这是一个精确整数等式。$\alpha$ 为整元，而 $q$ 为素数，
故其主理想的绝对范数为 $q$，于是

$$
(\alpha)=\mathfrak q
\tag{171.30}
$$

是 $H$ 中的一个一次素理想，指数恰为 $1$。
基点的 $by_0+1=0$ 确定了它就是 (171.9) 中的那个素理想。
在 $\mathscr F/H$ 中，该素理想未分歧且惰性，
所以延拓后仍只有一个素点、赋值仍为 $1$。
这完成 (171.10) 所需的 $h=1$ 主化见证。

### 素性证书的独立验证

数据包含 $33$ 步 ECPP 链，最后的素数为
$7059443040415189$。这个最后素数另附完整 Pratt 递归证书，
递归叶子都小于 $1000$，直接试除即可证明素性。

每一步 ECPP 数据为 $[N,t,s,a,(x,y)]$。
核验器令 $m=N+1-t$、$r=m/s$，并逐项检查

$$
r\text{ 已被递归证明为素数},\qquad
r>(\lfloor N^{1/4}\rfloor+2)^2,
$$

$$
\gcd(4a^3+27c^2,N)=1,\qquad
[m](x,y)=O,\qquad[s](x,y)\ne O,
\quad c=y^2-x^3-ax\pmod N.
\tag{171.31}
$$

全部点加法的除数都必须是模 $N$ 的单位。
因此最后的非零仿射点在每个素因子处都保持非零，
Hasse 界给出的 ECPP 论证适用。
这里采用的整数四次根界略强于通常的
$r>(N^{1/4}+1)^2$，不使用浮点比较。
标准库验证并不把 PARI 的 `ispseudoprime`、`isprime`
或 `primecertisvalid` 返回值当作素性证明的终点。

## 6. Robert 零值与配对方向

用与 R161 相同的

$$
P_2=(i,1-i),\qquad
v_{11}=64^{10}/\psi_{11}(P_2+P)
\tag{171.32}
$$

作为原始 Robert 单位。字符权仍为 $a^{1-p}$，不是 $a^{-p}$。
核验器逐一计算全部 $p^2-1=1848$ 个点

$$
P_2+[a]P,\qquad a\in\mathbf F_{p^2}^\times,
$$

以除法多项式递推求 $\psi_{11}$，再取 $p$ 次剩余符号和离散对数。
三个指定点另以实际 $[11]$ 倍点的 $x$ 坐标检查除法多项式公式。
结果为

$$
\sum_{a\ne0} a^{1-p}
\log_{\zeta_q}\!\left(
\psi_{11}(P_2+[a]P)^{(q^2-1)/p}
\right)=0\in\mathbf F_{p^2}.
\tag{171.33}
$$

程序还用另一种有限域幂法重新形成所有字符权，
并逐项核对 $a\mapsto-i\bar a$ 的共轭关系。
字符非平凡杀掉常数 $64^{10}$，Robert 的倒数只改变整体符号；
两者都不影响本式的零性。
由 R163 的全局生成性，(171.33) 正好证明 (171.6)。

配对使用标准 Miller 比值

$$
\zeta_q=(-1)^p\frac{f_{p,P}(iP)}{f_{p,iP}(P)},
\tag{171.34}
$$

并非一个未指定的 $p$ 次单位根。
这与 R168 的 Tate 规范 (171.8) 相容。
例如在 Tate 参数中令 $P=\zeta$、$Q=t=q^{1/p}$，取
$\theta(qu)=-u^{-1}\theta(u)$、
$\theta(u^{-1})=-u^{-1}\theta(u)$。
由

$$
f_P(u)=\left(\frac{\theta(u/\zeta)}{\theta(u)}\right)^p,
\qquad
f_Q(u)=u^{-1}\left(\frac{\theta(u/t)}{\theta(u)}\right)^p
$$

在原点的首项归一化后，所得 Miller 比值为
$(-1)^p\zeta$，再乘 (171.34) 中的 $(-1)^p$ 即为 $\zeta$。
因此本次数字的正负号没有留给一个未说明的配对对偶约定。

## 7. 自局部求和与 R168 的实际整数接口

程序对 $43$ 个非坏共轭计算 $\ell(\alpha_j)$，得到

$$
\sum_{j=1}^{43}\ell(\alpha_j)D_{\omega^j}=32K_0.
\tag{171.35}
$$

其中前半部分的 $21$ 个对数依次为

```text
37, 15, 6, 41, 27, 24, 1, 38, 34, 33, 5,
39, 28, 19, 10, 42, 14, 4, 8, 27, 38
```

中央项为 $0$，后半部分由 (171.15) 确定。
实部的加权和为 $0$，虚部的加权和为 $32$。
所以限制映射的因子 $2$ 给出 $\lambda_q=16$。

现在只为说明这个数值如何进入已经证明的实际必要条件，
假设 R19 的实际非 CM 曲线具有单个最小 Tate 支撑 $R=q$。
R168 给

$$
x_q\lambda_q=\frac{q+1}{2p^n}.
\tag{171.36}
$$

由 (171.27)、$n\ge1$ 以及 $p^n\mid q+1$，只能有 $n=1$。
于是

$$
z=11/2=27,\qquad
x_q=27/16=42=-1\pmod{43}.
\tag{171.37}
$$

若进一步 $Z=\pm q^e$，则 $n=1$ 迫 $43\nmid e$，
R168 的真实 Tate 系数为 $\mu_q=e\pmod{43}$。
其 Weil 乘数 $m$ 必须满足

$$
\left(\frac{-2mx_q/\mu_q}{43}\right)=1.
\tag{171.38}
$$

因此

| 单素数分母指数 | 必要的 Weil 乘数平方类 |
|---|---|
| $e=1$ | $(m/43)=-1$ |
| $e=3$ | $(m/43)=+1$ |

这是 (171.1) 与实际整数 $q+1$ 的直接联立，
不把 $\lambda_q$ 当成可以自由选择的局部参数。

不过，这个具体 $q$ 已经满足

$$
(-1+2i)^{(q^2-1)/43}\ne1\quad\text{于 }\mathbf F_{q^2}^\times.
\tag{171.39}
$$

R157 在 $5<43^2/16$ 处要求真实的首差反循环角色杀掉这个 primary 元。
所以 (171.39) 已排除此 $q$ 作为实际单素数支撑。
上表展示自局部值如何给出新的必要方程；
它不是在本例上另行宣称一个此前存活的实际曲线分支被排除。

## 8. 可复验内容与尚缺的全局步骤

在 `topics/serre-uniformity/notes` 中运行

```bash
python verify_r171_principal_norm_selflocal.py --check
```

一次核验完整覆盖：

1. $P$、$W$ 的模 $5$ 不可约性，精确域变换及 $\gamma_2$ 多项式关系；
2. $q$ 的 ECPP / Pratt 素性证明和 $N(\alpha)=-q$；
3. $P$ 在 $\mathbf F_{q^2}$ 中的全部 $44$ 个根；
4. 全部带二挠点标记的 $43$ 次 Vélu 商、Artin 标签及复共轭关系；
5. 同一 $P$ 的 Miller 配对、全部 $1848$ 个原始 Robert 符号；
6. 真 $q$-单位轨道的 $43$ 个单位符号、$1/2$ 限制因子、
   $\lambda_q=16$、$x_q=-1$ 与两条 Weil 平方类；
7. 本例的 Gaussian $5$ 阻碍。

唯一需与外部 CM 构造算法接合的输入是 $G$ 的类多项式身份。
它可以用下列独立 PARI/GP 命令重新产生，
再与 JSON 的 `gamma2_polynomial` 系数逐项比较：

```gp
G = polclass(-16*43^2, 5);
Vec(G)
```

这是已发表 CRT 类多项式算法的输入输出接口。
之后全部多项式关系、素性、范数及有限域计算都由标准库证书重新验证。
不需要类群预处理，也不使用 GRH 条件下的类群认证。

本文已经给出一个可直接代入 R168 的、真正求值的自局部行。
仍未证明变化最小 Tate 支撑上的相应行与 R164 的齐次矩阵总不相容，
也没有证明所有满足第一层方程的类都不能积成更高阶表示。
对同一个固定 $q$，后续层还必须保留整数 $q+1$ 的有限 $p$ 赋值、
完整 Tate 结构和 R19 的原始三族整数方程。
本次算法实例不替代这些全局条件。

## 9. 原始来源与规范定位

- R70、R78、R161、R163：CM primary 方向、原始 Robert 单位、
  全局单位线及同一个 Weil 配对的有限域实现。
- R168 §§2–7：arithmetic Frobenius、有限／奇异坐标、杯积规范、
  $\lambda_q$ 的选择独立性及实际 $q+1$ 方程。
- A. Enge、A. V. Sutherland，*Class invariants by the CRT method*，
  ANTS IX，LNCS **6197** (2010), 142–156，
  [作者稿](https://arxiv.org/abs/1001.3394)。
  PARI `polclass` 的相关实现由作者软件改编，见
  [作者项目说明](https://math.mit.edu/~drew/classpoly.html)。
- A. V. Sutherland，*Computing Hilbert class polynomials with the Chinese
  Remainder Theorem*，Math. Comp. **80** (2011), 501–538，
  [作者稿](https://arxiv.org/abs/0903.2785)。
- PARI/GP 官方说明：
  [`polclass` 的 $\gamma_2$ 条件与根分支提醒](https://pari.math.u-bordeaux.fr/dochtml/html/Polynomials_and_power_series.html)，
  [`primecert` 的证书格式及 ECPP 判据](https://pari.math.u-bordeaux.fr/dochtml/ref/Arithmetic_functions.html#primecert)。
  本文保留二同源标记并逐项验证标签，不从任意一个多项式根猜测 CM 共轭方向。
- J. Nekovář、A. Plater，*On the parity of ranks of Selmer groups*，
  Asian J. Math. **4** (2000), 437–498，§1.2.7，
  [作者全文](https://webusers.imj-prg.fr/~jan.nekovar/pu/parity.pdf)：
  $e_{\mathrm{Tate}}(\zeta,t^{1/p})=\zeta$ 的明确规范。

