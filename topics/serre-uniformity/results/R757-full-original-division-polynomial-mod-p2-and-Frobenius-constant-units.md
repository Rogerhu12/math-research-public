# R757：由原形式对数确定全部除法多项式模 $p^2$ 系数

日期：2026-11-14。状态：**已证明。** 本文给每个素数 $p\equiv5\pmod6$
的原 $E_0:y^2=x^3-1$ 标准除法多项式 $\psi_p\bmod p^2$ 的完整显式式，
包括常数端点。R753 的全部 Frobenius 常数方向由此被确定，
且其非恒定系数均为模 $p$ 单位。
证明只在显示的有限截断中运算；没有运行或引用新的有限素数实验。

这里确定的是原除法多项式的一个完整精度层。
它并不将原 $C_p$ 或 $A_p$ 识别为某个已证单位；
R697/R698 的临界 sigma 系数仍保持原定义与未解决状态。

## 1. 完整公式

固定
$$
p=6N+5,\qquad q=p^2,\qquad
M=\frac{p^2-1}{6}=Np+5N+4,
\tag{757.1}
$$
以及标准规范的 $\psi_p$：
$$
\psi_p(x)=p\,x^{3M}+\cdots,\qquad
x([p]P)=
\frac{x\psi_p^2-\psi_{p+1}\psi_{p-1}}{\psi_p^2}.
\tag{757.2}
$$
令
$$
c_j=\frac1{4^j}\binom{2j}{j},\qquad
Z_j=\frac{c_j}{6j+1}.
\tag{757.3}
$$

**定理 757.1。** 对每个 $p\ge5$、$p\equiv5\pmod6$，
$$
Z_j\in\mathbf Z_{(p)}\quad(0\le j<M),\qquad
v_p(Z_M)=-1.
\tag{757.4}
$$
因此下面右边的每个系数 $pZ_j$ 都是 $p$ 整的，并且
$$
\boxed{
\psi_p(x)\equiv
p\sum_{j=0}^{M}
\frac{\binom{2j}{j}}{4^j(6j+1)}
x^{3(M-j)}
\pmod{p^2}
}
\quad\text{于 }\mathbf Z_{(p)}[x].
\tag{757.5}
$$
这包括最高项和常数项，不是只在某个局部 $x$ 截断中的公式。
特别在 $j=M$，必须先使用
$$
6M+1=p^2,\qquad
pZ_M=\frac{c_M}{p}
=\frac{\binom{2M}{M}}{p\,4^M}\in\mathbf Z_{(p)}^\times,
\tag{757.6}
$$
再作约化；不能把 $Z_M$ 当成模 $p$ 的数。

对 R753 的
$$
H_p(x)=\frac{\psi_p(x)+1}{p}\in\mathbf Z[x],
$$
所有正次数的系数均满足
$$
\boxed{
[x^{3k}]\overline H_p=\overline Z_{M-k}
\quad(1\le k\le M).
}
\tag{757.7}
$$
故先前微分恒等式没有确定的 $N$ 个系数有
$$
\boxed{
[x^{3p\ell}]\overline H_p
=\overline Z_{M-p\ell}\in\mathbf F_p^\times
\quad(1\le\ell\le N).
}
\tag{757.8}
$$
当 $p=5$ 时该索引集为空，其他结论照样成立。

还有准确的中央二项式推论：
$$
\boxed{
\binom{(p^2-1)/3}{(p^2-1)/6}
\equiv
-p\,16^{(p^2-1)/6}\pmod{p^3}.
}
\tag{757.9}
$$

## 2. 同一原 sigma、同一微分与两个有限环

继续使用 R697/R698 的原规范
$$
x=\wp(z),\qquad y=\wp'(z)/2,\qquad
dz=\frac{dx}{2y},\qquad
\sigma(z)=z+O(z^7),\qquad
D_z^2\log\sigma=-x.
\tag{757.10}
$$
这固定 Gaussian 参数为零；不使用 ordinary sigma 的替代规范，
也不把 $\sigma$ 另乘一个未指定的 $\exp(cz^2)$。

令
$$
u=x^{-1/2}=z+O(z^7),\qquad w=u^6.
$$
其符号由 $y=-u^{-3}\sqrt{1-u^6}$ 固定。R698 的精确恒等式为
$$
z(u)=uZ(u^6),\qquad
Z(w)=\sum_{j\ge0}Z_jw^j,\qquad
\frac{dz}{du}=(1-u^6)^{-1/2},
\tag{757.11}
$$
$$
L(w)=\log T(w)=\sum_{j\ge1}\frac{h_j}{j}w^j,\qquad
h_0=1,\quad h_j=\prod_{a=1}^j\frac{6a-4}{6a-1},
\tag{757.12}
$$
$$
\boxed{
\sigma(z(u))=u\exp\bigl(L(u^6)/6\bigr).
}
\tag{757.13}
$$
式 (757.13) 是 R698 的六次幂恒等式按首项 $u$ 取唯一的形式六次根；
因为先在特征零中工作，且 $p\ne2,3$，这里没有选择一个新的根式相位。

以下全部 $w$ 运算在
$$
\mathcal R_{\mathbf Q}=\mathbf Q_p[w]/(w^{M+1}),
\qquad
\mathcal R=\mathbf Z_p[w]/(w^{M+1})
\tag{757.14}
$$
中进行。对于坐标反演及 $\sigma(pz(u))$，先在
$\mathbf Q_p[u]/(u^{q+1})$ 中保留至 $u^q$；
除以 $u$ 后保留至 $u^{q-1}=w^M$。
所以任何需要的最高指数和端点都是明确的。

下文只使用如下有限指数事实。若 $A\in p^a w\mathcal R$、$a\ge1$，
则有限幂零指数展开满足
$$
\exp(A)\in1+p^a w\mathcal R.
\tag{757.15}
$$
确实，第 $m$ 项的赋值至少
$am-v_p(m!)\ge am-(m-1)\ge a$；
$A$ 没有常数，所以在固定截断中只出现有限多个 $m$。
这既保留 $m!$，也避免了不合法的无限模 $p$ 指数。

## 3. 形式对数的整性与唯一最高极点

对 $0\le j\le M$，写 $j=ap+b$、$0\le b<p$。
由于 $2j\le2M=(p^2-1)/3<p^2$，阶乘赋值公式给
$$
v_p(c_j)
=\left\lfloor\frac{2j}{p}\right\rfloor
 -2\left\lfloor\frac jp\right\rfloor
=\left\lfloor\frac{2b}{p}\right\rfloor
\in\{0,1\}.
\tag{757.16}
$$
因此 $v_p(c_j)=1$ 当且仅当 $b\ge(p+1)/2$。

如果 $p\mid6j+1$，则唯一的剩余类是
$$
b=b_0:=\frac{5p-1}{6}=5N+4.
\tag{757.17}
$$
它严格大于 $(p-1)/2$，所以此时 $v_p(c_j)=1$。
对于 $j<M$，有 $6j+1<p^2$，
故分母若被 $p$ 整除，恰有一个 $p$，被 (757.16) 完整抵消。
其余 $j$ 的分母本来就是单位。这证明 $Z_j$ 在 $j<M$ 整。

在端点
$$
j=M=Np+b_0,\qquad 6M+1=p^2,
$$
(757.16) 仍给 $v_p(c_M)=1$，故恰有
$$
v_p(Z_M)=1-2=-1.
\tag{757.18}
$$
这是整个截断中唯一非整的 $Z$ 系数，且其位置恰为最高次数。
从而
$$
pZ(w)\in\mathcal R,\qquad
pZ(w)\equiv(pZ_M)w^M\pmod{p\mathcal R}.
\tag{757.19}
$$

这也说明为何不能简单在后文写“$Z$ 整”：
最高项确实有一个 $p$ 分母，必须单独保留。

## 4. $\log T$ 的每个分母都至多为一个 p

这里需要比 R698 的低阶合法范围更长的估计，但不约化无限 $T$。

对于 $1\le j\le M$，式 (757.12) 的各整数因子满足
$$
2\le6a-4\le p^2-5,\qquad
5\le6a-1\le p^2-2.
$$
所以任何一个被 $p$ 整除的因子恰有一个 $p$，没有 $p^2$ 因子。
在每个长度 $p$ 的指标块中：

- 分母 $6a-1$ 的唯一零剩余类为 $d=(p+1)/6=N+1$；
- 分子 $6a-4$ 的唯一零剩余类为 $e=2(p+1)/3=4N+4$。

注意 $1\le d<e<p$。写 $j=ap+b$ 后，完整计数给
$$
\boxed{
v_p(h_j)=
\mathbf1_{b\ge e}-\mathbf1_{b\ge d}
=
\begin{cases}
-1,&d\le b<e,\\
0,&\text{其余}.
\end{cases}
}
\tag{757.20}
$$
特别地，若 $p\mid j$，其末位 $b=0$，则 $h_j$ 本身是单位；
不能在这个指标同时再算一个来自 $h_j$ 的 $p$ 分母。

因为 $j\le M<p^2$，只有 $p\mid j$ 时 $j$ 有一个 $p$。
于是所有指标都满足
$$
\boxed{
v_p(h_j/j)\ge-1\qquad(1\le j\le M).
}
\tag{757.21}
$$
换言之，在本次完整截断中
$$
pL(w)\in w\mathcal R.
\tag{757.22}
$$
因此由 (757.15)，
$$
A(w):=\exp(-p^2L(w)/6)
\in1+p\,w\mathcal R.
\tag{757.23}
$$

本步并没有声称 $T$ 本身在这个较长截断中整：
$T=\exp L$ 的极点没有被抹掉。
可安全取指数的是显示的 $-p^2L/6$，其每项都在 $p\mathcal R$。

## 5. 原 $\sigma(pz)$ 的合法整数误差

令 $u(z)$ 是 (757.11) 的组合逆。由于 $z(u)$ 只有 $1\bmod6$ 次项，
逆函数也有
$$
u(z)=z+\sum_{j=1}^M a_jz^{6j+1}\pmod{z^{q+1}}.
\tag{757.24}
$$
由 §3，原 $z(u)$ 在次数 $q$ 以下的系数都整，
故其逆在次数 $q$ 以下也都整。
在最高次数 $q=6M+1$，组合反演的三角关系是
$$
a_M=-Z_M+\text{一个 }p\text{ 整数},
$$
因为该最高原系数和最高逆系数各只线性出现一次。
所以
$$
a_j\in\mathbf Z_p\quad(j<M),\qquad v_p(a_M)\ge-1.
\tag{757.25}
$$

定义实际形式乘法参数
$$
u_p(u)=u\bigl(pz(u)\bigr)\pmod{u^{q+1}}.
\tag{757.26}
$$
在 (757.24) 的任何非线性项
$a_j(pz(u))^{6j+1}$ 中，$j\ge1$。
若其幂乘积选中 $z(u)$ 的唯一非整最高项 $Z_Mu^q$，
其余至少六个因子各有正次数，总次数至少为 $q+6>q$，
已经超出截断。因此这些非线性项在所需范围只使用 $z(u)$ 的整系数。
再由 $v_p(a_j)\ge-1$，
$$
v_p\bigl(a_jp^{6j+1}\bigr)\ge6j\ge6.
$$
得到
$$
\boxed{
u_p(u)-pz(u)\in
p^6u^7\mathbf Z_p[u]/(u^{q+1}).
}
\tag{757.27}
$$
此外，$pz(u)$ 在整个截断中整，其次数小于 $q$ 的系数均在 $p\mathbf Z_p$。
所以
$$
u_p(u)\in\mathbf Z_p[u]/(u^{q+1}),\qquad
u_p(u)\in p\,u\mathbf Z_p[u]/(u^q).
\tag{757.28}
$$
其中 $u^q$ 系数可以是单位；第二式有意只写模 $u^q$。

在 $L(u_p^6)$ 中，每个幂 $u_p^{6j}$ 至少有六个正次数因子。
求次数至多 $q-1$ 的系数时，(757.28) 中可能非 $p$ 整除的 $u^q$ 项
完全不出现。由 (757.21)，
$$
L(u_p^6)\in
p^5u^6\mathbf Z_p[u]/(u^q),
\tag{757.29}
$$
因为各项赋值至少 $6j-1\ge5$。
由 (757.13)、(757.15)，
$$
\sigma(pz(u))
=u_p(u)\exp\bigl(L(u_p(u)^6)/6\bigr),
\qquad
\exp\bigl(L(u_p^6)/6\bigr)
\in1+p^5u^6\mathbf Z_p[u]/(u^q).
\tag{757.30}
$$
用 (757.27) 除以 $u$，并注意 $u_p/u$ 在全部保留次数都整，最终得到
$$
\boxed{
\frac{\sigma(pz(u))}{u}
=pZ(w)+p^5wB(w)
\quad\text{于 }\mathcal R_{\mathbf Q},
\qquad B(w)\in\mathcal R.
}
\tag{757.31}
$$
各式保持 $1\bmod6$ 或 $0\bmod6$ 的支撑，因此最后确实是 $w=u^6$ 的式子。

这里没有把 $z(u)$ 在最高次数的极点忽略：
它出现在 (757.18)、(757.19) 的 $pZ_Mw^M$ 中。
它只是在非线性乘积中因总次数过大而不出现。
这与把整个 $z(u)$ 无条件约化模 $p$ 是不同的步骤。

## 6. 原乘法恒等式与最高极点隔离

奇数 $p$ 的原 sigma 乘法恒等式是
$$
\boxed{
\psi_p(\wp(z))
=\frac{\sigma(pz)}{\sigma(z)^{p^2}}.
}
\tag{757.32}
$$
其常数和符号可直接固定：右边的格乘子相消，故为椭圆函数；
它在全部非零 $p$-挠点有单零点，在 $O$ 有阶 $p^2-1$ 的极点，
且首项是 $p z^{-(p^2-1)}$。
这与标准 $\psi_p$ 的除子和首项完全相同，商为一。
因为 $p$ 为奇数，sigma 的符号乘子也相消；这里没有偶数除法多项式的额外负号。

由 $x=u^{-2}$、$\sigma(z(u))=u\exp(L(w)/6)$，
式 (757.32) 给
$$
Q_p(w):=u^{p^2-1}\psi_p(u^{-2})
=\frac{\sigma(pz(u))}{u}\exp(-p^2L(w)/6).
\tag{757.33}
$$
标准原 $\psi_p$ 属于 $\mathbf Z[x^3]$（R753 的加权齐次性），
所以 $Q_p(w)$ 是次数 $M$ 的整多项式。
结合 (757.23)、(757.31)，存在 $A_1,B\in\mathcal R$ 使
$$
Q_p(w)=\bigl(pZ(w)+p^5wB(w)\bigr)\bigl(1+pwA_1(w)\bigr)
\quad\text{于 }\mathcal R_{\mathbf Q}.
\tag{757.34}
$$

将唯一的最高极点项分离：
$$
pZ(w)=pZ_{<M}(w)+(pZ_M)w^M,\qquad
Z_{<M}(w)\in\mathcal R.
$$
则
$$
\begin{aligned}
pZ(w)\,pwA_1(w)
&=p^2Z_{<M}(w)wA_1(w)
  +p(pZ_M)w^{M+1}A_1(w)\\
&\in p^2\mathcal R,
\end{aligned}
\tag{757.35}
$$
第二项在该截断中恰为零。
而 $p^5wB(1+pwA_1)$ 当然属于 $p^2\mathcal R$。
所以
$$
\boxed{
Q_p(w)\equiv pZ(w)\pmod{p^2\mathcal R}.
}
\tag{757.36}
$$
按 $w^j\leftrightarrow x^{3(M-j)}$ 反转系数，这就是定理 (757.5)。
因为已经覆盖 $j=0,\ldots,M$ 的每个系数，它是整条原多项式的结论。
式 (757.7) 对正指数直接除去原系数中的一个 $p$ 后随即成立。

## 7. 全部 Frobenius 常数系数及其单位性

对 $1\le\ell\le N$，置
$$
j=M-p\ell=(N-\ell)p+b_0,\qquad b_0=5N+4.
\tag{757.37}
$$
由 (757.16)，$v_p(c_j)=1$；另一方面
$$
6j+1=p^2-6p\ell=p(p-6\ell),
$$
其中 $1\le\ell\le N$ 使 $p-6\ell$ 是 $5,\ldots,p-6$ 之间的正整数，
不被 $p$ 整除。因此 $v_p(Z_j)=0$，证明 (757.8)。

若需完全不含先除 $p$ 的显式剩余式，令 $a=N-\ell$。
对 $n=dp+e<p^2$ 的阶乘，剥去恰 $d$ 个 $p$ 后，
$$
\frac{n!}{p^d}\equiv(-1)^d d!\,e!\pmod p.
$$
这里 $j=ap+b_0$、$2j=(2a+1)p+(4N+3)$，
于是
$$
\frac1p\binom{2j}{j}
\equiv
-\frac{(2a+1)!\,(4N+3)!}{(a!)^2((5N+4)!)^2}
\pmod p.
$$
再用 $4^j\equiv4^{a+b_0}$ 和 $p-6\ell\equiv-6\ell$，得到
$$
\boxed{
[x^{3p\ell}]\overline H_p
=
\frac{(2a+1)!\,(4N+3)!}
 {6\ell\,4^{a+5N+4}(a!)^2((5N+4)!)^2}
\in\mathbf F_p^\times,
\qquad a=N-\ell.
}
\tag{757.38}
$$
所有显示阶乘的指标严格小于 $p$；所有分母均为单位。
这不只是给出这些系数的一个求值算法，而是对每个允许 $p$、每个原方向
都证明其非消失。

R753 只用 $D x([p])=2p\,y([p])$ 的微分身份；
其中 $\mathbf F_p[x^{3p}]$ 是确切的微分核。
本篇增加的是原形式对数和原 sigma 乘法恒等式，
故可以确定该核中的实际系数。没有把“微分方程留下自由方向”
误解成实际除法多项式存在歧义。

## 8. 常数端点与模 $p^3$ 中央二项式恒等式

R753 已从原三挠点 $(0,\pm i)$ 的标准除法递推证明
$$
\psi_p(0)=-(-4)^M.
\tag{757.39}
$$
定理 (757.5) 的常数端点给
$$
-(-4)^M
\equiv pZ_M
=\frac{c_M}{p}
=\frac{\binom{2M}{M}}{p\,4^M}
\pmod{p^2}.
\tag{757.40}
$$
这里 $v_p(c_M)=1$ 已在 §3 证明，所以整个等式的两边均为 $p$ 整数。
乘以 $p4^M$，模数变为 $p^3$，得到
$$
\binom{2M}{M}\equiv-p(-16)^M\pmod{p^3}.
\tag{757.41}
$$
对奇素数 $p>3$，$p^2-1$ 被 $24$ 整除，
故 $M=(p^2-1)/6$ 是四的倍数，$(-16)^M=16^M$。
这便逐式推出 (757.9)，没有另作数值拟合或改变 sigma 的尺度。

## 9. 对原临界 sigma 单位问题的精确范围

本篇实际补全了原 $\psi_p\bmod p^2$ 的所有系数。
特别，原 Frobenius 常数方向不再是待求数据，且正次数方向全部为单位。
但在 (757.34)–(757.35) 中，$\exp(-p^2L/6)-1$ 的贡献恰被整体推入
$p^2\mathcal R$。这说明本精度的原除法多项式只留下原形式对数 $Z$；
它没有直接提取 R698 的
$$
[w^{(p-5)/6}]\,T(w)C(w),\qquad
[w^{(p-5)/6}]\,T(w)Z(w)^3.
\tag{757.42}
$$
二者仍是原 $A_p,A_{p-3}$ 的确切低阶指数表达式。

原高权中心值与截面系数的 R697 规范保持不变。
要把 (757.5) 或 (757.38) 的单位送到 (757.42)，
仍须证明一个保持原 CM 选择、六挠标记、普通导数和阶乘的额外恒等式。
本篇没有提供该恒等式，也不据此声称原 $C_p$ 全素数单位，
或同一真本原 $h$ 的三个原因子同时为单位。

更高精度的 $\psi_p$ 可以继续从 (757.33) 研究；
其 $L$ 项、较低阶乘和最高极点的乘积必须重新估计，
不能把本篇模 $p^2$ 的消项公式无条件搬到模 $p^3$ 或更高。
本文的实际完成点是全多项式精度层及其原系数单位结论。

## 依赖

- [R698](R698-two-actual-square-roots-at-one-low-degree.md)：原 $u,w,Z,H,T$、
  同一 sigma 与完整形式恒等式。本文独立扩展且证明全部所需有限分母范围。
- [R753](R753-original-division-polynomial-variation-and-three-torsion-unit.md)：
  标准原除法规范、原三挠点常数、$\psi_p\in\mathbf Z[x^3]$、
  微分核的准确范围。
- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md)：
  原临界 $A_k,C_k$ 的普通导数和六挠标记；只用于说明未改的问题。
- 标准 sigma 乘法恒等式的符号和常数已在 §6 由除子及首项核准；
  本文不依赖新的外部非消失定理或有限窗口。

