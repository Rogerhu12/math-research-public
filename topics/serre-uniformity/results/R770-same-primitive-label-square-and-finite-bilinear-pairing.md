# R770：同一真本原标签的原平方公式与有限双线性配对

日期：2026-11-14。状态：**准确平方公式及有限配对已证明；配对的非零性仍开放。**

本篇把 R760 的两个原临界 sigma 系数、R727 的原有限范数及原 $M_{2,h}$ 合并成一个保留全部常数的平方等式。随后将同一标签的三因子写成一个有本原投影的有限双线性配对。所有系数都来自原 $c=0$ sigma；没有更换 Gaussian、环面、split vector 或正三次方向。

本篇不选择一个未经证明的平方根符号，也不把平方公式或形式卷积本身当成非零定理。R765 的非零截断残差与本篇临界配对之间还差两个总指标，不能直接相认。

## 1. 原函数、系数和标签

固定
$$
p=6N+5\ge41,\qquad E_0:y^2=x^3-1,\qquad dz=dx/(2y),
$$
$$
\sigma(z)=z+O(z^7),\qquad D_z^2\log\sigma=-x.
\tag{770.1}
$$
记
$$
F=x\sigma^6=z^4 f(z^6),\qquad
G=-xy\sigma^6=z g(z^6),
\tag{770.2}
$$
其中 $f(0)=g(0)=1$。R697 证明所需普通导数的整性；R760 也直接证明下述低阶 Taylor 系数在 $p$ 处整。本文令
$$
f(v)=\sum_{i=0}^{N-1}f_i v^i,\qquad
g(v)=\sum_{j=0}^{N-1}g_j v^j
\quad\text{于 }\mathbf F_p[v]/(v^N),
\tag{770.3}
$$
始终表示 (770.2) 原系数的有限约化。这里的 $v=z^6$ 与 R760 的 $w=u^6$ 是不同变量。

保留 R760 的
$$
u=x^{-1/2},\quad w=u^6,\quad z=uZ(w),\quad dz/du=C(w),
\quad \sigma^6=u^6T(w).
\tag{770.4}
$$
$C=(1-w)^{-1/2}$，$Z+6wZ'=C$，而原 $T$ 的系数仅在已证整范围内约化。取
$$
h=6a+1,\qquad 1\le a\le N,\qquad (h,p+1)=1.
\tag{770.5}
$$
这包含全部非端点正本原标签。端点 $h=1$ 保留 R760 §3 的独立公式；本文不引入 $C_{-1}$。

形式留数换参给
$$
\begin{aligned}
f_i&=[w^i]TCZ^{-(6i+5)},\\
g_j&=[w^j]TZ^{-(6j+2)}.
\end{aligned}
\tag{770.6}
$$
令 $i=a-1$、$j=N-a$，则 $i+j=N-1$，且
$$
\boxed{f_{a-1}=U_h,\qquad g_{N-a}=V_h.}
\tag{770.7}
$$
第一式是准确的原 Taylor 抽取。第二式使用
$$
6(N-a)+2=p-h-2,\qquad Z^p=1\pmod{(p,w^{N+1})},
$$
故 $Z^{-(p-h-2)}=Z^{h+2}$ 于所需截断内。这正是 R760 的
$$
U_h=[w^{a-1}]TCZ^{2-h},\qquad
V_h=[w^{N-a}]TZ^{h+2}.
$$
所需次数至多 $N-1$；没有越过 $T$ 的首个 $p$ 分母。

## 2. 两个原 Cartier 数的同标签平方常数

置
$$
m_1=h-3=6a-2,\qquad
m_2=p-h-3=6(N-a)+1,
$$
$$
Q_h=(h-2)(h-1)h(h+1)(h+2).
\tag{770.8}
$$
于是 $m_1+m_2=p-6$，$m_1$ 为偶数，且所有显示阶乘指标及 $Q_h$ 的五个因子均严格介于零和 $p$ 之间。

R697/R760 的普通导数和两个平方公式给
$$
\begin{aligned}
A_{h-2}&=2^{-m_1/2}m_1!U_h,&
C_{h-2}&=3\cdot2^{-m_1}m_1!U_h^2,\\
A_{p-h-2}&=2^{-(m_2-1)/2}m_2!V_h,&
C_{p-h-2}&=-2^{-m_2}m_2!V_h^2.
\end{aligned}
\tag{770.9}
$$
这里第二个 $C$ 的负号和因子二来自
$-2m_2!C_{p-h-2}=A_{p-h-2}^2$，并未把两个分支的常数混用。

Wilson 恒等式给
$$
m_2!=(p-1-(m_1+5))!
 \equiv\frac{(-1)^{m_1+6}}{(m_1+5)!}
 =\frac1{(m_1+5)!}\pmod p.
$$
所以
$$
m_1!m_2!\equiv Q_h^{-1}\pmod p.
\tag{770.10}
$$
此外 $2^{-(p-6)}=2^5$ 于 $\mathbf F_p^\times$。乘 (770.9) 得
$$
\boxed{
Q_h C_{h-2}C_{p-h-2}
 =-96(U_hV_h)^2\quad\text{于 }\mathbf F_p.
}
\tag{770.11}
$$
这是同一个 $h$ 的恒等式，所有因子由原规范固定。

## 3. 加入同一个原有限范数

取 $s^2=-3$，$\alpha^3=4$，并保留原 $\zeta$、原 Cartier 单位
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\ne0\pmod p.
\tag{770.12}
$$
$P_d$ 表示 $P_d(1)=1$ 的 Legendre 多项式。R727 给
$$
\overline N_h=-P_{h-1}(1/s)^2,
\tag{770.13}
$$
以及保持完整原 Fourier 尾的范数约化
$$
\frac{(p^2M_{2,h})^2}{\zeta^2}
 =\frac{864N_hB^5}{\alpha^2}\,Q_h\,
 \mathfrak r_{h-2}\mathfrak r_{p-h-2}\pmod p.
\tag{770.14}
$$
此式左侧整；所需所有高块的丢弃由 R727 §§6–7 逐块证明。本文没有再次截去未经控制的尾。

原 R683 比较为
$$
\mathfrak r_k=c(-3B)^{-(k-1)}C_k,\qquad
c=(3/p)\alpha^2/2.
\tag{770.15}
$$
两个指标都在该比较的范围内。它们的 $(k-1)$ 之和为 $p-6$，故
$$
\mathfrak r_{h-2}\mathfrak r_{p-h-2}
=-\frac{243\alpha^4B^5}{4}
 C_{h-2}C_{p-h-2}\pmod p.
\tag{770.16}
$$
这里 $c^2=\alpha^4/4$，而
$(-3B)^{-(p-6)}=(-3B)^5$；因此二次角色已经精确消去。

将 (770.11)、(770.13)、(770.16) 代入 (770.14)，得到
$$
\boxed{
\left(\frac{p^2M_{2,h}}{\zeta}\right)^2
 =
 \left(
 1296\,\alpha\,s\,B^5\,
 P_{6a}(1/s)\,U_hV_h
 \right)^2
 \pmod p.
}
\tag{770.17}
$$
为独立核常数，右侧的标量平方为
$$
1296^2s^2=-2^8\,3^9=-5038848,
$$
而 (770.14)–(770.16) 与 (770.11) 给
$864(-243)/4\cdot(-96)\cdot(-1)=-5038848$，完全一致。

(770.17) 是平方等式。它本身不确定不同 $h$ 的原解析平方根符号，也不允许在一个求和式中任意把左侧取成右侧的正号。R747/R748 所用的原实嵌入和严格 CM 球定号是另一项实际输入。

所有 $h-1$ 为偶数，故 $P_{h-1}(1/s)\in\mathbf F_p$；改换 $s$ 的平方根不改变它。由 R727 的完整尾，仍有精确等价
$$
\boxed{
P_{6a}(1/s)U_hV_h\ne0
\quad\Longleftrightarrow\quad
N_h,\ C_{h-2},\ C_{p-h-2}\text{ 同为单位}.
}
\tag{770.18}
$$
该条件蕴含原 $v_p(M_{2,h})=-2$ 和对应 scalar Abel primitive 在 $v_p(a-1)>3$ 只有中心零。它没有把真实正秩有理候选等同于该 scalar primitive 的零。

## 4. Legendre 权的有限几何平均

先证明一个不含 sigma 的多项式恒等式：
$$
\boxed{
P_d(1/s)=s^{-d}\operatorname{CT}_q(1+q+q^{-1})^d.
}
\tag{770.19}
$$
事实上对形式变量 $t$，
$$
\operatorname{CT}_q
 \frac1{1-t(1+q+q^{-1})/s}
 =
 \frac1{\sqrt{(1-t/s)^2-4t^2/s^2}}
 =
 (1-2t/s+t^2)^{-1/2},
$$
其中用了 $s^2=-3$。最后一式是 Legendre 的生成函数。对本文所有 $d<p$，二的幂和所需阶乘均可在 $p$ 处约化。

令 $\mu_{p+1}\subset\mathbf F_{p^2}^{\times}$，对 $q\in\mu_{p+1}$ 定义
$$
R_q=(1+q+q^{-1})/s,\qquad A_q=R_q^6.
\tag{770.20}
$$
因 $p\equiv5\pmod6$，有 $s^p=-s$、$q^p=q^{-1}$，所以
$$
R_q^p=-R_q,\qquad A_q\in\mathbf F_p.
\tag{770.21}
$$
当 $q$ 为原非平凡三次单位根时 $R_q=0$；下列求和中的正次幂使这些项自然为零，不作除法。

由于 $6i+6\le6N=p-5<p+1$，(770.19) 的 Laurent 次数严格小于 $p+1$。因此常数项可准确改成 $\mu_{p+1}$ 的有限平均：
$$
P_{6i+6}(1/s)
 =\frac1{p+1}\sum_{q\in\mu_{p+1}}A_q^{\,i+1},
\qquad 0\le i<N.
\tag{770.22}
$$
分母 $p+1$ 是 $\mathbf F_p$ 中的单位。它保留的是有限平均规范；约化后该分母的值为一。

定义作用于 (770.3) 的线性算子
$$
\boxed{
(\mathcal Lf)(v)
 =\frac1{p+1}\sum_{q\in\mu_{p+1}}A_q f(A_qv)
 =\sum_{i=0}^{N-1}P_{6i+6}(1/s)f_i v^i.
}
\tag{770.23}
$$
这不是形式新增的未知权：每个系数恰是原范数平方根的 Legendre 因子。

## 5. 真本原筛选的准确有限投影

写
$$
m=N+1=(p+1)/6,\qquad
r=\prod_{\substack{\ell\mid m\\\ell\ge5}}\ell,
\tag{770.24}
$$
乘积取不同素数，空积为一。因为 $6i+7\equiv1\pmod6$，
$$
(6i+7,p+1)=1
\quad\Longleftrightarrow\quad
(6i+7,r)=1.
\tag{770.25}
$$

对每个 $d\mid r$，选择
$$
6\rho_d\equiv7\pmod d
$$
并定义
$$
(\Pi_df)(v)=\frac1d\sum_{\xi\in\mu_d}\xi^{\rho_d}f(\xi v).
\tag{770.26}
$$
$d$ 与 $6p$ 互素，$\mu_d\subset\mathbf F_{p^2}$。对 $d=1$ 取恒等算子。有限根和给
$$
[v^i]\Pi_df=
\begin{cases}
f_i,&d\mid6i+7,\\
0,&d\nmid6i+7.
\end{cases}
\tag{770.27}
$$
所以
$$
\boxed{
\Pi_{\rm prim}=\sum_{d\mid r}\mu(d)\Pi_d
}
\tag{770.28}
$$
的 $v^i$ 系数乘上准确指示函数
$\mathbf1_{(6i+7,p+1)=1}$。虽然 (770.26) 在 $\mathbf F_{p^2}$ 中写出，其结果和 (770.28) 均在 $\mathbf F_p[v]/(v^N)$。这里是 Möbius 的 $\mu(d)$，不与根群记号混用。

该投影只在原正标签 $h=6i+7$ 上筛选本原性；没有把负三次方向或非本原角色拼进原目标。

## 6. 原三因子的有限双线性配对

由 (770.7)、(770.23)、(770.28)，定义
$$
\mathcal B_p(f,g)
 =[v^{N-1}](\Pi_{\rm prim}\mathcal Lf)(v)\,g(v).
\tag{770.29}
$$
则有完整有限恒等式
$$
\boxed{
\mathcal B_p(f,g)=
\sum_{\substack{1\le a\le N\\(6a+1,p+1)=1}}
 P_{6a}(1/s)\,U_{6a+1}V_{6a+1}.
}
\tag{770.30}
$$
也可完全展开成
$$
\boxed{
\mathcal B_p(f,g)=
\sum_{d\mid r}\frac{\mu(d)}{d(p+1)}
 \sum_{\xi\in\mu_d}\sum_{q\in\mu_{p+1}}
 \xi^{\rho_d}A_q
 [v^{N-1}]\, f(\xi A_qv)g(v).
}
\tag{770.31}
$$
全部系数只使用 (770.3) 的原低阶整截断，有限求和不引入任何高阶 $p$ 分母。

因此
$$
\boxed{
\mathcal B_p(f,g)\ne0
\ \Longrightarrow\
\text{存在同一个真本原 }h
\text{ 满足 (770.18)}.
}
\tag{770.32}
$$
反向不成立于一般有限和：不同实际标签的非零项可能相消。本文既没有证明 $\mathcal B_p$ 非零，也不因它可能为零就断言所有单项为零。

### 6.1 可将两个有限权同时移到另一因子

为给后续真正的配对证明一个可核验的对称接口，先注意
$$
P_{p-1-d}(X)\equiv P_d(X)\pmod p,\qquad 0\le d\le p-1.
\tag{770.33}
$$
证明可逐项用
$$
P_d(X)=\sum_{k=0}^d
 \binom dk\binom{d+k}{k}\left(\frac{X-1}{2}\right)^k.
$$
对 $d'=p-1-d$ 及 $k<p$，两二项式分别约化为
$(-1)^k\binom{d+k}{k}$ 与 $(-1)^k\binom dk$；
超出任一实际次数的系数也因此为零。故得到多项式恒等式，而不只是某点的巧合。

若 $i+j=N-1$，则
$$
(6i+6)+(6j+4)=p-1.
$$
从而
$$
P_{6i+6}(1/s)=P_{6j+4}(1/s).
\tag{770.34}
$$
定义
$$
(\widetilde{\mathcal L}g)(v)
 =\frac1{p+1}\sum_{q\in\mu_{p+1}}R_q^4 g(A_qv)
 =\sum_{j=0}^{N-1}P_{6j+4}(1/s)g_jv^j.
\tag{770.35}
$$
对原本原条件也有
$$
6i+7\equiv-(6j+5)\pmod{p+1}.
\tag{770.36}
$$
因此以 $6\widetilde\rho_d\equiv5\pmod d$ 构造的
$\widetilde\Pi_{\rm prim}$ 筛选 $(6j+5,p+1)=1$，且
$$
\boxed{
\mathcal B_p(f,g)
 =[v^{N-1}]f(v)
   (\widetilde\Pi_{\rm prim}\widetilde{\mathcal L}g)(v).
}
\tag{770.37}
$$
这仅是同一有限卷积的伴随表达；没有把实际 CM 角色由正方向改成负方向，也没有宣称可以把两个不相关标签的单位拼合。

## 7. R765 的非零残差为何尚不等于本配对

R765 在原 $w=u^6$ 中证明
$$
\mathscr Q(\mathcal T)=Bw^N+O(w^{N+1}),\qquad B\ne0,
\tag{770.38}
$$
其中 $\mathcal T=T\bmod(p,w^{N+1})$ 取次数至多 $N$ 的多项式代表，
$$
\mathscr Q(A)=6w(1-w)(AA''-A'^2)+(5-8w)AA'-2A^2.
\tag{770.39}
$$
它的已证卷积混合 $\tau_i\tau_j$ 的总指标 $N$ 与 $N+1$。

这个错位在原 $z,F,G$ 坐标中仍可准确看见。对任意常数项一的 $A(w)$ 置
$$
F_A=u^4A,\qquad G_A=uA/C,\qquad D_z=C^{-1}D_u.
$$
直接微分给不含未知常数的恒等式
$$
\boxed{
F_A''G_A-2F_A'G_A'+F_AG_A''
 -\left(4x+\frac8{x^2}\right)F_AG_A
 =\frac{12u^9}{C}\mathscr Q(A).
}
\tag{770.40}
$$
这里撇号在左侧指 $D_z$；(770.39) 中仍指 $D_w$。

一种核对方式是令 $a=D_z\log F_A$、$b=D_z\log G_A$。
则 $a-b=3C/u$，且左侧除以 $F_AG_A$ 后为
$$
(a-b)^2+D_z(a+b)-4u^{-2}-8u^4
 =
12u^4\left[
6w(1-w)(A'/A)'
 +(5-8w)A'/A-2
\right].
$$
再用 $F_AG_A=u^5A^2/C$ 即得 (770.40)。

对 $A=\mathcal T$，(770.38) 的右侧首项为
$$
12Bz^{6N+9}=12Bz^{p+4}.
\tag{770.41}
$$
所需 $z(u)$ 的系数至此仍整：对应 $Z$ 的分母至多 $6(N+1)+1=p+2$，其中不存在 $p$ 的倍数。故此显示阶的换参没有偷越一个积分极点。

若写 $F_A=z^4f_A(z^6)$、$G_A=zg_A(z^6)$，左侧微分乘积在
$z^{p+4}=z^{3+6(N+1)}$ 处使用的最高总指标为 $N+1$，再有由 $x$ 的低阶修正带来的更小总指标。反之本篇真正临界项满足
$$
m_1+m_2=p-6=5+6(N-1),
$$
恰是 $[v^{N-1}]f(v)g(v)$ 的总指标。
所以 (770.40) 的非零右侧不是 (770.29) 的直接来源；
还必须证明能够消去较高总指标并保留原 Legendre 与真本原投影。

本文未作这种消去。R765 的非零残差与 R702 的已知移位单位相容，
但不能因此把移位权冒认成原临界权，也不能把未经证明的带投影配对宣布为单位。

## 8. 后续必须解决的实际问题

原同标签单位问题现可在固定原函数中准确写成：

> 对充分大的允许 $p$，证明存在 $1\le a\le N$，
> $(6a+1,p+1)=1$，使
> $P_{6a}(1/s)f_{a-1}g_{N-a}\ne0$。

证明 (770.30) 的实际配对非零是一个充分条件；
证明原临界两序列与 Legendre 的公共零受限也是另一个可能入口。
这两个非零机制均不由本篇形式恒等式自动产生。
端点 $h=1$ 仍可作为原 R760 端点条件的补充，未被排除。

本篇新增的是：完整原常数的同标签平方 (770.17)，
Legendre 权的明确有限平均 (770.23)，
本原投影 (770.28)，以及保持指标的双线性表达 (770.30)–(770.37)。
没有新增数值窗口，没有重算已存值，也没有改变主课题的完成标准。

## 依赖

- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md)：原 $F,G$、普通导数及两个实际平方式。
- [R760](R760-original-critical-sigma-jets-from-four-digit-division-data.md)：合法低阶截断、原同标签 $U_h,V_h$ 及固定 Gaussian。
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md)：原范数、原比较标量、同标签全部 Fourier 尾。
- [R683](R683-even-weight-Cartier-channel-and-actual-r3.md)：实际 $\mathfrak r_k/C_k$ 比较。
- R765：原截断的首个非零 Cartier 残差及下一项的真实 $p$ 极点。
