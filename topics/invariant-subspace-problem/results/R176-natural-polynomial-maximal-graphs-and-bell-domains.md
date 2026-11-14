# R176：一阶自然多项式的最大闭图、C 自伴与 Bell 乘子的准确域

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R176。

状态：完整证明。本稿处理真实闭算子的自然多项式及其实际 Bell 修正。一般点态多项式的核，特别慢平方共振，仍未排除。

## 1. 设置与使用的准确输入

令

$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad 0\ne a\in\ell^2,
$$

并令 $X=X_u$ 为 R125 的实际闭一阶乘子。记

$$
\mathfrak C=\{A\}',\qquad
(Cf)(y)=\overline{f(-1-y)},\qquad
B(f,g)=\langle f,Cg\rangle.
$$

使用以下已经证明的事实：

- R88：$\mathfrak C$ 是交换代数，每个成员均为 $C$ 对称，并且是 $\mathbb C[A]$ 的强算子闭包。因此每个闭 $A$ 不变子空间被全部 $\mathfrak C$ 保持。
- R125/R128：$X^*=CXC$，有限柱空间 $\mathcal D_c$ 是 $X$ 与 $X^*$ 的图核心；每个 $D\in\mathfrak C$ 保持 $\operatorname{Dom}X$ 且与 $X$ 域交换。
- R161/R172：每个自然幂 $X^p$ 闭、稠密定义；对 $0\le k<p$ 及任意 $\varepsilon>0$，

$$
\|X^kx\|\le\varepsilon\|X^px\|+C_{\varepsilon,p,k}\|x\|,
\qquad x\in\operatorname{Dom}X^p.
\tag{1.1}
$$

- R128/R140/R172 的共同正则器 $R(t)\in\mathfrak C$ 单射稠密、收缩，$R(t)\to I$ 强；$S(t)=XR(t)\in\mathfrak C$ 有界，而且

$$
R(t)^pH\subseteq\operatorname{Dom}X^p,\qquad
X^kR(t)^p=S(t)^kR(t)^{p-k}.
\tag{1.2}
$$

每个固定 $R(t)^pM$ 是 $X_M^p$ 的图核心，其中 $M$ 是任意闭 $A$ 不变空间，$X_M=X|_{\operatorname{Dom}X\cap M}$。

R145 的常向量幂域或 R171 的次数加权估计还给 $1\in\operatorname{Dom}X^p$ 对全部 $p$ 成立。本稿不从稠密性本身推断任何高次图核心。

## 2. 有界交换系数多项式的自然闭域

取 $p\ge1$ 以及

$$
E_0,\ldots,E_p\in\mathfrak C,\qquad
E_p\text{ 在 }B(H)\text{ 中可逆}.
$$

其逆仍属于 $\mathfrak C$。定义自然算子

$$
P(X)x=\sum_{k=0}^pE_kX^kx,\qquad
\operatorname{Dom}P(X)=\operatorname{Dom}X^p.
\tag{2.1}
$$

每个 $E_k$ 保持全部自然幂域：从第一阶域交换逐次归纳即可。它们与这些幂域交换。

先左乘 $E_p^{-1}$，把最高系数化为 $I$。由 (1.1)，低阶项相对 $X^p$ 的界可以任意小。因此存在 $c_1,c_2>0$，使

$$
c_1(\|x\|+\|X^px\|)
\le \|x\|+\|P(X)x\|
\le c_2(\|x\|+\|X^px\|).
\tag{2.2}
$$

所以 $P(X)$ 在准确域 $\operatorname{Dom}X^p$ 上闭、稠密定义。这里没有取一个未经识别的更大形式域。

全部 $D\in\mathfrak C$ 保持该域并满足

$$
P(X)Dx=DP(X)x.
\tag{2.3}
$$

同样，对每个闭 $A$ 不变 $M$，各项把 $\operatorname{Dom}X^p\cap M$ 送入 $M$，自然限制 $P(X)_M$ 闭、稠密定义，且 (2.2) 在 $M$ 上仍成立。每个固定 $R(t)^pM$ 也是 $P(X)_M$ 的图核心。

## 3. 原参数图与最大分式图确实相等

固定 $t>0$，简记

$$
Z=R(t)^p,\qquad
Q=P(X)Z
=\sum_{k=0}^pE_kS(t)^kR(t)^{p-k}\in\mathfrak C.
\tag{3.1}
$$

在 $\operatorname{Dom}X^p$ 上还有 $ZP(X)=Q$。对任意闭 $A$ 不变 $M$，定义最大闭分式关系

$$
\mathcal T_M=\{(x,y)\in M\oplus M:Qx=Zy\}.
\tag{3.2}
$$

因 $Z$ 单射，这是一张单值闭图。

**命题3.1。**

$$
\boxed{
\mathcal T_M=\operatorname{Graph}(P(X)_M).
}
\tag{3.3}
$$

证明：自然图包含于 (3.2) 已由域交换得到。反向，设 $Qx=Zy$，$x,y\in M$。令

$$
x_s=R(s)^px\in\operatorname{Dom}X^p\cap M.
$$

利用全部有界因子的交换性及真正域等式，

$$
ZP(X)x_s
=Q R(s)^px
=R(s)^pQx
=Z R(s)^py.
$$

单射性允许消去有界因子 $Z$，得到

$$
P(X)x_s=R(s)^py.
$$

当 $s\downarrow0$，两端图向量趋于 $(x,y)$。$P(X)_M$ 闭，故 $(x,y)$ 属于自然图。证毕。

同时由固定图核心，

$$
\boxed{
\operatorname{Graph}(P(X)_M)
=
\overline{\{(Zh,Qh):h\in M\}}.
}
\tag{3.4}
$$

(3.3) 是最大分式，(3.4) 是原分母参数图；本稿证明了它们相等，未把一个默认成另一个。

这里的全部 $M$ 结论没有使用商空间或限制上的共轭。下一节的 $C$ 自伴只在原 $H$ 上陈述。

## 4. 完整 C 自伴及最大伴随域

对 $x,y\in\operatorname{Dom}X^p$，逐次使用 $X$ 的 $B$ 对称及系数的域交换，得

$$
B(P(X)x,y)=B(x,P(X)y).
\tag{4.1}
$$

记 $T=P(X)$，$T^\#=CT^*C$。于是 $T\subseteq T^\#$。

为证明反向包含，取 $x\in\operatorname{Dom}T^\#$、$y=T^\#x$。对任意 $s>0$，置

$$
Z_s=R(s)^p,\qquad Q_s=T Z_s\in\mathfrak C.
$$

$Z_s,Q_s$ 都是有界 $C$ 对称算子。对任意 $h\in H$，

$$
B(Q_sh,x)=B(TZ_sh,x)=B(Z_sh,y).
$$

有界 $B$ 对称及非退化性给

$$
Q_sx=Z_sy.
$$

而 $Z_sx$ 确实属于 $\operatorname{Dom}T$，所以

$$
TZ_sx=Z_sy.
$$

令 $s\downarrow0$，$Z_sx\to x$、$Z_sy\to y$。$T$ 闭，故 $x\in\operatorname{Dom}T$ 且 $Tx=y$。

因此

$$
\boxed{P(X)^*=CP(X)C.}
\tag{4.2}
$$

这一步证明了整个伴随域，超出了共同稠密核心上的对称恒等式。

特别，

$$
\boxed{(X^p)^*=(X^*)^p}
\tag{4.3}
$$

右侧是自然幂，准确域为 $C\operatorname{Dom}X^p$。标量多项式满足

$$
q(X)^*=\overline q(X^*)
$$

在对应自然域上成立。本稿不由此声称 $\operatorname{Dom}X^p=\operatorname{Dom}(X^*)^p$；第一阶通常伴随同域不能未经证明升到全部高次。

## 5. 任意循环域向量都是多项式图核心的生成元

下述机制对 $T=P(X)$ 及任意 $\xi\in\operatorname{Dom}T$ 适用，只要 $\xi$ 对 $A$ 循环。

记 $\mathcal L_\xi=\operatorname{span}\{A^n\xi:n\ge0\}$。由 (2.3)，其全部向量在 $\operatorname{Dom}T$ 中。

对任意 $D\in\mathfrak C$，R88 给一个多项式网 $p_\alpha(A)$ 强趋于 $D$。于是

$$
p_\alpha(A)\xi\to D\xi,\qquad
T p_\alpha(A)\xi=p_\alpha(A)T\xi\to DT\xi=T D\xi.
$$

所以 $D\xi$ 属于 $\mathcal L_\xi$ 的图闭包。

固定 $Z=R(t)^p$。将上句用于 $D=Zp(A)$，图闭包包含 $Z\mathcal L_\xi$。$\xi$ 循环，且从 $H$ 到 $T$ 图范数空间的映射

$$
h\longmapsto Zh
$$

有界，因为 $TZ=Q$ 有界。因此 $Z\mathcal L_\xi$ 在 $ZH$ 中图稠密。后者是固定图核心，故

$$
\boxed{
\mathcal L_\xi\text{ 是 }T\text{ 的图核心}.
}
\tag{5.1}
$$

进而

$$
\boxed{
[\;T\xi\;]_A=\overline{\operatorname{Ran}T}.
}
\tag{5.2}
$$

反向包含由图核心得到，正向包含由 $TA^n\xi=A^nT\xi$ 得到。结合 (4.2)，

$$
\boxed{
T\xi\text{ 循环}\ \Longleftrightarrow\ \ker T=0.
}
\tag{5.3}
$$

没有要求 $\xi$ 是有限柱，也没有把 $\xi$ 在 $H$ 中的循环性直接误当成图循环；固定有界正则器是从一种拓扑转到另一种的依据。

### 5.1 一个已完成的自然多项式推论

取 $\xi=1$、$T=q(X)$。R172 已独立证明每个非零标量多项式 $q(X)$ 的像稠密。因此

$$
\boxed{q(X)1\text{ 循环}\qquad(q\in\mathbb C[z]\setminus\{0\}).}
\tag{5.4}
$$

这是自然算子多项式作用于 $1$ 的向量。它一般不是点态 $q(u)$。

## 6. 有限柱本身也是全部自然多项式的图核心

为了精确识别点态乘子的最小闭包，本节给真实的范数逼近，不调用一个未经证明的高次有限柱核心断言。

记

$$
W_n=\|A^n\|=\prod_{\ell=1}^n\alpha_{v_2(\ell)},\qquad
d_j=W_{2^j},\qquad N_j=A^{2^j}/d_j.
$$

$W_n$ 递减、$W_0=1$，且二进制无进位计数给

$$
W_n=\prod_{j:\,n_j=1}d_j.
\tag{6.1}
$$

令

$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
Z_m=\prod_{j<m}(I+N_j)
=\sum_{n<2^m}\frac{A^n}{W_n}.
\tag{6.2}
$$

这里 (6.1) 可由
$\lfloor n/2^k\rfloor=\sum_{j\ge k}n_j2^{j-k}$
代入权积计数直接验证。真实逆界 $\|(I+N_j)^{-1}\|<3$ 给

$$
\|Z_m^{-1}\|\le3^m.
\tag{6.3}
$$

不同位乘积满足 $V_J1=\chi_J$。乘以共同分母 $Z_m$ 后，$\{V_J:J\subseteq[0,m)\}$ 的分子是

$$
\prod_{j\in J}(I-N_j)\prod_{j\notin J}(I+N_j).
$$

Walsh–Hadamard 变换说明其线性张成恰为全部不同位单项式 $\prod_{j\in F}N_j$ 的张成。故有限头柱乘子的空间准确是

$$
\boxed{
\operatorname{span}\{X_f:f\text{ 只依赖前 }m\text{ 位}\}
=
\{p(A)Z_m^{-1}:\deg p<2^m\}.
}
\tag{6.4}
$$

其中 $X_f1=f$，每个 $X_f$ 是真正的有界有理解析乘子。

固定整数 $r\ge1$，取 $2^m>r$，令 $p_m$ 是标量多项式 $z^rZ_m(z)$ 的低于 $2^m$ 次截断。则高次部分只有 $r$ 项。对其指标 $2^m-r\le n<2^m$，

$$
\frac{\|A^{n+r}\|}{W_n}
\le\frac{d_m}{W_{2^m-1}}
=\alpha_m.
$$

于是

$$
\boxed{
\|A^r-p_m(A)Z_m^{-1}\|
\le r\,3^m\alpha_m\longrightarrow0.
}
\tag{6.5}
$$

$r=0$ 的恒等算子已经是柱乘子。对有限多项式取有限线性组合，再用 $\mathcal A=\overline{\mathbb C[A]}^{\|\cdot\|}$，得到

$$
\boxed{
\overline{\operatorname{span}\{X_f:f\in\mathcal D_c\}}^{\|\cdot\|}
=\mathcal A.
}
\tag{6.6}
$$

现在 $1\in\operatorname{Dom}T$，由 §5，$\mathbb C[A]1$ 是 $T$ 的图核心。用 (6.6) 按范数逼近任意固定 $p(A)$：若 $X_{f_n}\to p(A)$，则

$$
f_n=X_{f_n}1\to p(A)1,\qquad
Tf_n=X_{f_n}T1\to p(A)T1=Tp(A)1.
$$

每个 $f_n$ 都是有限柱。因此

$$
\boxed{\mathcal D_c\text{ 是 }P(X)\text{ 的图核心}.}
\tag{6.7}
$$

这只是原 $H$ 上的结论。对未知真不变空间 $M$，不声称 $\mathcal D_c\cap M$ 稠密或非零。

## 7. 自然实现就是对应向量的最小闭乘子

对任意 $h\in H$，有限柱上的规范初始乘子定义为

$$
\mathcal X_{h,0}f=X_fh,\qquad f\in\mathcal D_c.
\tag{7.1}
$$

取 $h=T1=P(X)1$。由域交换，

$$
Tf=T X_f1=X_fT1=X_fh.
$$

所以 (6.7) 立即给

$$
\boxed{\overline{\mathcal X_{h,0}}=P(X).}
\tag{7.2}
$$

它的准确域为 $\operatorname{Dom}X^p$，是 $C$ 自伴算子，并具有 §§3、5 的最大图、原参数图和图循环核心。

### 7.1 点态多项式的 Bell 修正

为避免将 (5.4) 与点态符号混淆，记

$$
L_n(v)=
\left.\frac{d^n}{dt^n}\log(\cosh t+v\sinh t)\right|_{t=0}.
$$

每个 $L_n$ 是有限标量多项式，$L_1(v)=v$，而 $L_n(1)=0$ 对 $n\ge2$ 成立。

对 $n\ge2$，

$$
K_n=\sum_ja_j^nL_n(V_j)\in\mathcal A
\tag{7.3}
$$

按算子范数绝对收敛：$\sup_j\|V_j\|<\infty$ 且 $a\in\ell^2$ 给 $\sum_j|a_j|^n<\infty$。并有 $\chi(K_n)=0$。

等价地，规范乘积

$$
\mathcal B(t)
=\prod_j e^{-ta_jV_j}
\bigl(\cosh(ta_j)I+V_j\sinh(ta_j)\bigr)
\tag{7.4}
$$

是 $\mathcal A$ 值整单位函数，各因子与 $I$ 的差在紧 $t$ 集合上为 $O(|a_j|^2)$，逆乘积同样收敛。R134/R145 的真实真空恒等式给

$$
u^n=\sum_{k=0}^n\binom nk\mathcal B^{(n-k)}(0)X^k1.
\tag{7.5}
$$

§10 还将用伴随图核心重新证明包括指数权的这一机制。

因此对次数 $p$、最高系数 $q_p\ne0$ 的标量多项式 $q$，存在实际有界 $\mathcal A$ 系数多项式

$$
P_q(z)=q_pz^p+\sum_{k<p}E_kz^k,\qquad
P_q(X)1=q(u).
\tag{7.6}
$$

其全部系数的字符满足

$$
\chi(P_q)(z):=\sum_k\chi(E_k)z^k=q(z),
\tag{7.7}
$$

因为 $\chi(\mathcal B(t))=1$。

由 (7.2)，

$$
\boxed{
\overline{\mathcal X_{q(u),0}}=P_q(X),\qquad
\operatorname{Dom}\overline{\mathcal X_{q(u),0}}
=\operatorname{Dom}X^p.
}
\tag{7.8}
$$

所以任意单模式点态多项式的规范最小闭乘子都已获得准确自然域和 $C$ 自伴性。但其核仍需另外判定。

例如

$$
P_{z^2}(X)=X^2+B_2,\qquad
B_2=\sum_ja_j^2(I-V_j^2).
$$

本稿保留 $B_2$，没有把慢共振 $X^2+B_2-a_{j_0}^2I$ 换成 $X^2-a_{j_0}^2I$。

## 8. 任意多项式核上，一阶乘子自动成为有界限制

令 $T=P(X)$，固定 $Z=R(t)^p$、$Q=TZ$。由最大图 (3.3)，

$$
\boxed{\ker Q=\ker T.}
\tag{8.1}
$$

确实，$Qx=0=Z0$ 自动把 $x$ 放入自然域并给 $Tx=0$；反向由 $Qx=ZTx$。

记 $M=\ker T=\ker Q$。它是闭 $A$ 不变空间，并且

$$
M\subseteq\operatorname{Dom}X^p.
$$

由于 $Q\in\mathfrak C$ 与 $X$ 域交换，对 $x\in M$，

$$
QXx=XQx=0.
$$

所以 $Xx\in M$。于是 $X|_M$ 是从整个 $M$ 到 $M$ 的闭算子，闭图定理给

$$
\boxed{
Y:=X|_M\in B(M),\qquad
M\subseteq\bigcap_{n\ge1}\operatorname{Dom}X^n.
}
\tag{8.2}
$$

这把任意此类多项式核化为一阶算子的有界限制，而不只处理二次平方。

### 8.1 Acal 系数的有限谱约束

进一步假设全部 $E_k\in\mathcal A$，并置

$$
q_0(z)=\sum_{k=0}^p\chi(E_k)z^k.
$$

最高系数在 $\mathcal A$ 中可逆，所以 $\chi(E_p)\ne0$，$q_0$ 非零。若 $M\ne0$，则

$$
q_0(Y)
=-\sum_{k=0}^p(E_k|_M-\chi(E_k)I_M)Y^k.
\tag{8.3}
$$

每个 $E_k-\chi(E_k)I$ 在全 $H$ 拟幂零，限制后仍拟幂零。它与有界 $Y$ 交换，故对应乘积仍拟幂零。有限个交换拟幂零算子的和仍拟幂零，可由二项式和各幂的任意小指数界直接验证。因此 $q_0(Y)$ 拟幂零。

普通有界多项式谱映射遂给

$$
\boxed{\sigma(Y)\subseteq q_0^{-1}(\{0\}).}
\tag{8.4}
$$

它可按这些有限谱点作 Riesz 分解；每个谱子空间仍闭且 $A$ 不变，并在其上使 $X-\mu I$ 成为有界拟幂零限制。这里没有把全空间 $\sigma(X)$ 传给限制。

对点态 Bell 多项式 (7.6)，$q_0=q$。所以任何非零点态 $q(u)$ 的未知核上，$X$ 的谱只能落在 $q$ 的有限零集。单个根分支仍可能是未解决的无限维拟幂零限制；本稿不把这个必要条件写成排核。

## 9. dyadic gauge 确实保持全部自然幂域

R125/R128 给

$$
U_\zeta XU_\zeta^*=X+D_\zeta,\qquad D_\zeta\in\mathcal A,
$$

以及第一阶域相等。

若 $H\in\mathfrak C$ 有界，则它与 $X$ 域交换，归纳得到

$$
\boxed{
\operatorname{Dom}(X+H)^p=\operatorname{Dom}X^p,
\qquad
(X+H)^p=\sum_{k=0}^p\binom pkH^{p-k}X^k.
}
\tag{9.1}
$$

反向域归纳值得明确：若 $x\in\operatorname{Dom}(X+H)^{p+1}$，已知 $x\in\operatorname{Dom}X^p$，而 $(X+H)^px\in\operatorname{Dom}X$。二项式中所有低于 $p$ 的项已经在 $\operatorname{Dom}X$ 内；相减得 $X^px\in\operatorname{Dom}X$，故 $x\in\operatorname{Dom}X^{p+1}$。

将 (9.1) 用于 $D_\zeta$，

$$
\boxed{U_\zeta\operatorname{Dom}X^p=\operatorname{Dom}X^p.}
\tag{9.2}
$$

并有真实闭算子等式

$$
U_\zeta P(X)U_\zeta^*
=\sum_{k=0}^p(\gamma_\zeta E_k)(X+D_\zeta)^k
$$

于同一个自然域。即使最高系数为固定标量，共轭差也通常只是低一阶的无界多项式，不能自动视为有界扰动。

## 10. 任意复 ℓ² 指数权的倾斜自然实现

取

$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,\qquad \xi_w=e^w.
$$

该向量属于 $H$ 且对 $A$ 循环。以下给出准确的域构造，未将倾斜后的形式乘子直接套进一个未证明的伴随域结论。

### 10.1 倾斜第一阶是实际有界交换扰动

定义

$$
R_j(b)
=
(V_j\cosh b_j+I\sinh b_j)
(I\cosh b_j+V_j\sinh b_j)^{-1}.
\tag{10.1}
$$

分母属于 $\mathcal A$，字符为 $e^{b_j}\ne0$，因此实际可逆。等价地，

$$
R_j(b)=(I-e^{-2b_j}N_j)(I+e^{-2b_j}N_j)^{-1}.
$$

由于 $b_j\to0$，高位分母在 $I$ 的固定邻域内；有限个低位单独取界，得到

$$
\sup_j\|R_j(b)\|<\infty,\qquad
R_j(b)-V_j=b_jK_j,\qquad
\sup_j\|K_j\|<\infty.
\tag{10.2}
$$

后一式在 $b_j=0$ 时由解析差商连续延拓；它来自准确恒等式

$$
R_j(b)-V_j
=(I-V_j^2)\sinh b_j
(I\cosh b_j+V_j\sinh b_j)^{-1}.
$$

于是

$$
H_{a,b}=\sum_ja_j(R_j(b)-V_j)\in\mathcal A
\tag{10.3}
$$

按算子范数绝对收敛，因为 $\sum_j|a_jb_j|<\infty$。每项字符为0，故 $\chi(H_{a,b})=0$。

令

$$
X_b=X+H_{a,b},\qquad\operatorname{Dom}X_b=\operatorname{Dom}X.
\tag{10.4}
$$

它是实际闭的 $C$ 自伴有界扰动。由 (9.1)，

$$
\operatorname{Dom}X_b^p=\operatorname{Dom}X^p.
\tag{10.5}
$$

所有含 $X_b$ 的最高系数可逆的有界交换系数多项式，展开后都是 §2 的同类 $X$ 多项式。因此它们闭、$C$ 自伴，并有固定 $R(t)^p$ 图核心。这里不需要假定 $[X_b^*,X_b]$ 仍有界。

### 10.2 不同位倾斜恒等式

对有限不同位集合 $J$，

$$
\boxed{\left(\prod_{j\in J}R_j(b)\right)\xi_w=\chi_J\xi_w.}
\tag{10.6}
$$

证明：先截断 $w$ 到包含 $J$ 的有限位。乘以相应局部因子
$\cosh b_j+V_j\sinh b_j$ 后，(10.1) 把它准确变为
$V_j\cosh b_j+\sinh b_j$。所有位各出现一次，使用 $V_F1=\chi_F$，便得到有限位等式。再让截断趋无穷，两端在 $H$ 中收敛，左边只是固定的有界算子作用。

(10.6) 不表示 $R_j(b)^2=I$，也不表示该变换是点态乘法同态。

### 10.3 整规范乘积和真正的所有幂域

定义

$$
\mathcal B_b(t)
=\prod_j e^{-ta_jR_j(b)}
\bigl(\cosh(ta_j)I+R_j(b)\sinh(ta_j)\bigr).
\tag{10.7}
$$

在每个紧 $t$ 集合上，充分高位的因子与 $I$ 的差为 $O(|a_j|^2)$，常数由 (10.2) 统一控制；局部逆也有同阶估计。有限低位因子的字符均为1，故实际为解析单位。因此 (10.7) 与其逆都按范数局部一致收敛，给 $\mathcal A$ 值整单位函数，且

$$
\mathcal B_b(0)=I,\qquad \mathcal B_b'(0)=0,\qquad
\chi(\mathcal B_b(t))=1.
\tag{10.8}
$$

置

$$
u_N=a_*+\sum_{j<N}a_j\chi_j,\qquad
X_{b,N}=a_*I+\sum_{j<N}a_jR_j(b).
$$

由 (10.6)，有限位上准确有

$$
V_N(t):=\mathcal B_{b,N}(t)^{-1}e^{tu_N+w}
=e^{tX_{b,N}}\xi_w.
\tag{10.9}
$$

Rademacher 指数矩估计

$$
\mathbb E e^{s\operatorname{Re}\sum c_j\chi_j}
=\prod_j\cosh(s\operatorname{Re}c_j)
\le e^{s^2\|c\|_2^2/2}
$$

及尾部 $\ell^2$ 收敛，保证 $e^{tu_N+w}\to e^{tu+w}$ 在紧 $t$ 集合上以 $H$ 范数一致收敛，并且极限为 $H$ 值整函数。故

$$
V_N(t)\longrightarrow
V(t):=\mathcal B_b(t)^{-1}e^{tu+w}
$$

局部一致，全部有限阶导数也局部一致收敛。

现在核对域，而非只比较形式级数。R125 的有限一阶截断及其伴随在有限柱上强收敛；(10.3) 的部分和按范数收敛。因此

$$
X_{b,N}^*h\longrightarrow X_b^*h\qquad(h\in\mathcal D_c).
$$

$\mathcal D_c$ 仍是 $X_b^*$ 的图核心，因为这里只作有界扰动。对 $h\in\mathcal D_c$，(10.9) 给

$$
\langle V_N'(t),h\rangle
=\langle V_N(t),X_{b,N}^*h\rangle.
$$

取极限，并借助伴随图核心延拓测试向量，得到

$$
V(t)\in\operatorname{Dom}X_b,\qquad X_bV(t)=V'(t).
$$

在同一个弱等式中反复对 $t$ 求导，逐次得到

$$
\boxed{
V^{(k)}(t)\in\operatorname{Dom}X_b,\qquad
X_bV^{(k)}(t)=V^{(k+1)}(t).
}
\tag{10.10}
$$

特别

$$
\boxed{
\xi_w\in\bigcap_{p\ge1}\operatorname{Dom}X_b^p
=\bigcap_{p\ge1}\operatorname{Dom}X^p,\qquad
X_b^p\xi_w=V^{(p)}(0).
}
\tag{10.11}
$$

这是真正的自然幂域结论，使用了通常伴随核心和闭性。

### 10.4 加权 Bell 向量与闭算子范围的精确等式

由 $e^{tu+w}=\mathcal B_b(t)V(t)$ 求导，

$$
u^n e^w
=\sum_{k=0}^n\binom nk
\mathcal B_b^{(n-k)}(0)X_b^k\xi_w.
\tag{10.12}
$$

因此对次数 $p$ 的 $q$，存在最高系数 $q_pI$ 的实际 $\mathcal A$ 系数多项式 $P_{q,b}$，使

$$
\boxed{q(u)e^w=P_{q,b}(X_b)\xi_w.}
\tag{10.13}
$$

其字符多项式仍为 $q$。高次累积量为
$\sum_ja_j^nL_n(R_j(b))$，$n\ge2$，由同一 $\ell^2$ 估计按范数收敛；每项是实际 $\mathcal A$ 元素。

自然算子 $T_{q,b}=P_{q,b}(X_b)$ 在准确域 $\operatorname{Dom}X^p$ 上闭且 $C$ 自伴。$\xi_w$ 循环，并由 (10.11) 属于该域，所以 §5 适用：

$$
\boxed{
\operatorname{span}\{A^n\xi_w:n\ge0\}
\text{ 是 }T_{q,b}\text{ 的图核心},
}
\tag{10.14}
$$

以及

$$
\boxed{
[\;q(u)e^w\;]_A
=\overline{\operatorname{Ran}T_{q,b}},
\qquad
q(u)e^w\text{ 循环}\Longleftrightarrow\ker T_{q,b}=0.
}
\tag{10.15}
$$

这是闭实现的精确加权核接口。它没有声称规范初始乘子
$f\mapsto X_f(q(u)e^w)$ 本身的闭包域就是 $\operatorname{Dom}X^p$；
(10.13) 的基向量是 $\xi_w$，不是 $1$。

若 $M=\ker T_{q,b}\ne0$，§8 适用于 $X_b$，得到 $X_b|_M$ 有界、谱包含于 $q$ 的零集。又 $X|_M=X_b|_M-H_{a,b}|_M$，后者是与之交换的拟幂零扰动，因此两个有界限制的谱相同。故

$$
\boxed{\sigma(X|_M)\subseteq q^{-1}(\{0\}).}
\tag{10.16}
$$

这仍只是非零核的必要结构，不排除其中的单根拟幂零限制。

## 11. 完成的接口与仍然保留的缺口

本稿完成：

- 最高系数为有界交换单位的自然多项式：闭性、准确域、固定图核心和整个 $C$ 伴随域；
- 每个不变限制的最大分式图等于原参数图闭包；
- 每个循环域向量产生多项式图核心，并精确识别其像向量的循环空间；
- 有限柱乘子的范数稠密性以及全部自然多项式的有限柱图核心；
- 单模式点态多项式的规范最小闭乘子等于完整 Bell 自然实现；
- 任意复 $\ell^2$ 指数权下的真实有界倾斜扰动、全部幂域和加权范围／核判据；
- 任意此类多项式核上的一阶有界限制及 $\mathcal A$ 系数的有限谱约束。

没有由这些接口推出：

- 一般 Bell 多项式或慢平方共振已无核；
- $C$ 自动保持任意未知不变空间；
- 原空间 $C$ 自伴自动下降为限制 $C$ 自伴；
- 倾斜有界扰动自动继承 R161 的有界自交换子估计；
- 算子多项式 $q(X)$ 可以替代点态 $q(u)$；
- 指数加权向量的整个规范闭乘子域等于 $\operatorname{Dom}X^p$。

一般 Hilbert 不变子空间问题仍未解决。
