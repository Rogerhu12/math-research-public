# R1016：原小 index theta 下降、两个处处单位卷积与下一层精确零集

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：原 $\sigma$ 与 $\sigma^2$ 的指定临界卷积在全部范数 −1 方向处处非零；原 $U=x^2\sigma^6$ 的下一层完整卷积也有准确零集。** 这里使用 index one/two 的实际线丛及其小维角色空间，不是将 R1013 的三十六维比较未经证明地限制到一个子空间。原 bare 高系数仍须保 R1015 的全部余项，原 $F,G$ 的 primitive/Legendre 同标签任务也没有被替换。

## 1. 同一原源与结论

保持
$$
p=6N+5\ge41,\quad k=\mathbf F_{p^2},\quad
E_0:y^2=x^3-1,\quad dz=\frac{dx}{2y},
$$
以及原 $\sigma(z)=z+O(z^7)$ 的规范和 CM 嵌入。
定义原有理系数
$$
\sigma=z\sum_{i\ge0}b_i z^{6i},\qquad
V=\sigma^2=z^2\sum_{i\ge0}a_i z^{6i},\qquad
U=x^2\sigma^6=z^2\sum_{i\ge0}u_i z^{6i}.
\tag{1016.1}
$$
三行的首系数皆为一。本文出现的有限系数全部为 $p$-整；约化后属
$\mathbf F_p$。以下用相同字母表示约化。

令
$$
T^-=\{\eta\in k^\times:\eta^{p+1}=-1\},
$$
$$
\mathcal S_N(\eta)=\sum_{i+j=N}b_i b_j\eta^{6i},\qquad
\mathcal C_d(\eta)=\sum_{i+j=d}a_i a_j\eta^{6i},\qquad
\mathcal U_d(\eta)=\sum_{i+j=d}u_i u_j\eta^{6i}.
\tag{1016.2}
$$

**定理 1016.1。** 对全部所述 $p$ 和全部 $\eta\in T^-$，
$$
\boxed{\quad
\mathcal S_N(\eta)\ne0,\qquad
\mathcal C_N(\eta)\ne0,\qquad
\mathcal U_N(\eta)\ne0.
\quad}
\tag{1016.3}
$$
此外，
$$
\boxed{\quad
\{\eta\in T^-:\mathcal C_{N-1}(\eta)=0\}
=\{\eta\in T^-:\mathcal U_{N-1}(\eta)=0\}
=
\begin{cases}
\varnothing,&p\equiv11\pmod{12},\\
\{\eta\in T^-:\eta^6=-1\},&p\equiv5\pmod{12}.
\end{cases}
\quad}
\tag{1016.4}
$$
第二行的零集恰有六个元素。所有“单位”均指这些原有限整系数和在所指定 $p$ 上素点的约化非零；没有替换原微分或 sigma 规范。

## 2. 每个方向的实际同源与 index-one 线丛

消费 R1012 的逐方向定理。对任一
$$
v=(\alpha,\beta)\in\mathcal O^2,\quad
\mathcal O=\mathbf Z[\zeta],\quad N\alpha+N\beta=p,
$$
有实际矩阵
$$
A_v=\begin{pmatrix}\alpha&-\overline\beta\\
                    \beta&\overline\alpha\end{pmatrix},
\qquad A_v^\dagger A_v=pI.
\tag{1016.5}
$$
每个微分像方向 $\kappa=\alpha/\beta\bmod p\in T^-$ 恰有十二个向量；
每个核方向
$$
\gamma=-\overline\alpha/\beta\bmod p,\qquad
K_\gamma=\{(\gamma P,P):P\in E_0[p]\}
\tag{1016.6}
$$
也恰有十二个。以下 $\eta=\gamma^{-1}$，不能与 $\kappa$ 混同。

令 $L_m=O(mO)$。R1013 已用取偶次幂消去 $\operatorname{Pic}^0[2]$ 歧义，故 $m=2$ 时有实际、原点 rigidified 的
$$
I_{A,m}:A^*(L_m\boxtimes L_m)
 \xrightarrow{\sim}L_{mp}\boxtimes L_{mp}.
\tag{1016.7}
$$
这里 $m=1$ 也成立，但须补证明。

先在特征零考虑任一非零 $\nu\in\mathcal O$。$[\nu]^*L_1$ 的 divisor 是
$\ker[\nu]$ 的各点之和。二在 $\mathcal O$ 中惰性，因此该核的二-primary 部分要么平凡，要么为完整的 $E_0[2^a]$。它绝不会只有一个非零二挠点；有限群中各元素之和因而为零。由椭圆曲线的 divisor 类判据，
$$
[\nu]^*L_1\simeq L_1^{N\nu}.
\tag{1016.8}
$$
应用于 $\alpha,\beta$ 及其共轭；它们的 norm 均小于 $p$，所以此处核在所用 $p$ 处亦为 étale。

由 (1016.5)，
$$
\mathcal N=A^*(L_1\boxtimes L_1)
 \otimes(L_p\boxtimes L_p)^{-1}
$$
属于 $\operatorname{Pic}^0(E_0^2)$。式 (1016.8) 说明它在两个坐标轴上的限制都平凡。而
$\operatorname{Pic}^0(E_0^2)=\operatorname{Pic}^0(E_0)\times\operatorname{Pic}^0(E_0)$，两轴限制即这两个坐标，故 $\mathcal N$ 平凡。
按原点纤维取一，可在原良好整模型上得到 (1016.7)。这一步没有假定所有奇 index 都自动没有二挠歧义。

## 3. 同一个实际 theta 分布在 $m=1,2$ 的版本

令
$$
\mathcal H_m=H^0(E_0,L_{mp}),\quad
\mathcal H_{m,0}=\ker D
 =\{f^p s_{mp}:fs_m\in H^0(E_0,L_m)\}.
$$
$D=d/\omega$，$B\in\mathbf F_p^\times$、$q$ 和参数 $Y$ 全用 R889 的原规范。特别
$$
Dq=1,\quad q=-B^{-1}Y^{-p}+Y+O(Y^p),\quad D^p=0.
$$

原 theta section 的第 $p$ 个系数和相应算子为
$$
\Theta_{p,m}=d_p-mBq,\qquad
Q_m=q-\frac{d_p}{mB}.
\tag{1016.9}
$$
这是 R889 实际 multiplier 计算的 index-$m$ 版本：Cartier divisor 中的 $6p$ 换成 $mp$，其 $Y^p$ 极部变为 $mY^{-p}$，分布交换子给导数 $-mB$，奇性固定常数为零。因此 multiplier 正是 $-mBq$。
$d_p$ 仍是实际平移分布，不是 $D^p/p!$。

相同的实际 theta 关系给
$$
[D,Q_m]=1,\quad D^p=Q_m^p=0,\qquad
\mathcal H_m=\bigoplus_{r=0}^{p-1}Q_m^r\mathcal H_{m,0},
\quad\dim\mathcal H_{m,0}=m.
\tag{1016.10}
$$
可核准 $Q_m^p=0$ 而不作形式截断假设：实际 norm-one theta action 按 Frobenius vacuum 归一后，$Q_m$ 的权为 $-1$；
$Q_m^p$ 与 $D$ 交换，故将 vacuum 送回 vacuum，但其权为 $1\bmod p+1$，而 vacuum 只有零权，故为零。再与 $Q_m$ 交换即杀掉整个 (1016.10)。后者的直接和也由
$D^rQ_m^r|_{\mathcal H_{m,0}}=r!$ 和维数 $mp$ 得到。

在原整 local frame
$$
\epsilon_{mp}=s_{mp}/Y^{mp}
$$
中，对 $0\le r<p$ 有完整首-$p$ jet 公式
$$
\boxed{\quad
Y^{mp}Q_m^r(f^p)
\equiv\sum_{k=0}^r
 \frac{r!}{k!}(-mB)^{k-r}
 c_{r-k}(f\sigma^m)^pY^k
 \pmod{Y^p}.
\quad}
\tag{1016.11}
$$
其中 $c_j$ 是原普通 Taylor 系数。证明复用 R889 的实际 Bell 比较：
$\nabla_m=D-x\partial_\eta+m\eta$，
$\Phi(f\eta^j)=f^p(-Bq)^j$，则
$Q_m^r(f^p)=(-1/(mB))^r\Phi(\nabla_m^rf)$。
将同一个截断 zeta primitive 代入，误差仍为 $-BY\bmod Y^p$，展开便给 (1016.11)。所有阶乘小于 $p$。
原 $\sigma/z$ 的所需首-$p$ 单位截断为整：低阶 zeta 积分及有限指数中的全部分母小于 $p$；也可用 R702 的原首极块和取 $p$-单位次方根验证。没有约化整个无限 sigma 级数。

R1013 的完整有限平坦核证明只使用 (1016.9)–(1016.10) 和 $p\nmid m$，故同样给
$$
\Omega_{\gamma,m}(w)=\sum_{r=0}^{p-1}
 \gamma^{-r}Q_{m,1}^rQ_{m,2}^{p-1-r}w
\tag{1016.12}
$$
及实际同构
$$
I_{A,m}A^*=\Omega_{\gamma,m}T_{A,m},
\quad
T_{A,m}:H^0(E_0^2,L_m\boxtimes L_m)
 \xrightarrow{\sim}\mathcal H_{m,0}^{\otimes2}.
\tag{1016.13}
$$
其中完整不变条件仍为
$\gamma D_1+D_2=0,\ \gamma^pQ_{m,1}+Q_{m,2}=0$。
原 $\delta_1,\delta_p$ 生成全部有限分布及 splitting 唯一性已由 R1013 核准，不改成 étale 核求和。

## 4. Rigidified CM 角色与两个一维下降源

对 $L_m$ 的全局 CM 作用必须按原点纤维 rigidify。
即将 canonical pullback $[\epsilon]^*$ 乘 $\epsilon^m$；
这使 local frame $s_m/Y^m$ 在原点的纤维作用为一。
因此 analytic 表示 $f\sigma^m$ 的角色就是其 Taylor 次数模六。
在 $L_{mp}$ 上相应乘 $\epsilon^{mp}$。这个标量修改不改变算子共轭，所以 $Q_m$ 的全局 CM 权仍为一。

实际 $I_{A,m}$ 与这个对角 CM 作用交换：$A$ 的各条目在原 CM 环中，且两侧 rigidification 相同，其交换子是原点纤维为一的全局标量。

### Index two

$H^0(L_2)$ 的基是
$$
V=\sigma^2,\qquad \mathsf X=x\sigma^2,
$$
角色分别为二、零。令
$$
w_{0,2}=s_{2p}\boxtimes s_{2p},\qquad
s_{A,2}=T_{A,2}^{-1}w_{0,2}.
$$
$w_{0,2}$ 的角色为 $4p$，而 (1016.12) 总 $Q$ 次数为 $p-1$，故其下降源角色为
$$
4p+(p-1)=5p-1\equiv0\pmod6.
$$
在 $H^0(L_2)^{\otimes2}$ 中，零角色空间恰为
$k(\mathsf X\boxtimes\mathsf X)$；其它三个基向量角色为二、二、四。
所以
$$
\boxed{\quad
s_{A,2}=c_A\,\mathsf X\boxtimes\mathsf X,\qquad c_A\in k^\times.
\quad}
\tag{1016.14}
$$
$\mathsf X$ 在原 local frame 的常数为一，故
$$
J_{0,0}(\Omega_{\gamma,2}w_{0,2})=c_A.
\tag{1016.15}
$$

从 (1016.11) 直接计算这个 jet：只有
$r=6i+2,\ p-1-r=6j+2,\ i+j=N$ 贡献。
二者为偶数，Wilson 公式给 $r!(p-1-r)!=-1$，且
$(-2B)^{p-1}=1$。因此
$$
\boxed{\quad
J_{0,0}(\Omega_{\gamma,2}w_{0,2})
=-\gamma^{-2}\mathcal C_N(\gamma^{-1})=c_A\ne0.
\quad}
\tag{1016.16}
$$
这证明 $\mathcal C_N$ 在全部 $T^-$ 上非零，没有“充分大 $p$”的附加门槛。

### Index one

$H^0(L_1)^{\otimes2}$ 本来就是一维
$k(\sigma\boxtimes\sigma)$。使用 (1016.7) 的实际 index-one 同构，可写
$$
T_{A,1}^{-1}(s_p\boxtimes s_p)
=d_A\,\sigma\boxtimes\sigma,\qquad d_A\in k^\times.
\tag{1016.17}
$$
其角色 $2p+(p-1)\equiv2$ 也与右侧一致。右侧首项为 $d_A UV$，其拉回的 $YT$ 系数为
$$
d_A(\alpha\overline\alpha-\beta\overline\beta)
=2d_A N\alpha\ne0\pmod p.
\tag{1016.18}
$$
只用首二阶 jet，整 line-frame 的非常数项不影响此式。

另一方面，(1016.11) 取 $k=1$ 的两轴读数，仍只留下
$r=6i+2,\ p-1-r=6j+2,\ i+j=N$。这次常数为
$$
\boxed{\quad
J_{1,1}(\Omega_{\gamma,1}(s_p\boxtimes s_p))
=-B^2\gamma^{-2}\mathcal S_N(\gamma^{-1}).
\quad}
\tag{1016.19}
$$
它等于 (1016.18)，故 $\mathcal S_N$ 在全部 $T^-$ 上非零。

## 5. 原 norm-three 恒等式准确返回 $U$

令 $s=\sqrt{-3}$ 为原 CM 嵌入。原 sigma 的 multiplication identity 给
$$
\sigma(sz)=s\,x(z)\sigma(z)^3.
\tag{1016.20}
$$
可以在同一源内核准：两边有相同 sigma multiplier；商为椭圆函数。
非零 $\ker[s]$ 的两个点正是 $x=0$，其 divisor 和 $x$ 的二阶原点极给相同 divisor；原点首项均为 $sz$，遂固定常数为一。这里未添加 Gaussian。

平方得
$$
\sigma(sz)^2=-3x^2\sigma^6=-3U(z).
$$
因 $s^6=-27$，比较 (1016.1) 的系数即
$$
u_i=(-27)^i a_i,\qquad
\boxed{\ \mathcal U_d=(-27)^d\mathcal C_d.\ }
\tag{1016.21}
$$
这证明 (1016.3) 的第三个断言，也将以下下一层结论运输到 R1015 的同一个 $U$。

## 6. 实际 index-two 的下一层 $J_{3,3}$

本节取高于源首项的 jet，故必须先核 line-frame，不能仅沿用“首项乘一个单位”论证。

### 6.1 原 analytic 比较与整 frame 在首-$p$ 矩形相同

原 $j=0$ lattice 的 quasiperiod 满足 $\eta_\lambda=C\overline\lambda$，见 R697。由于 $A^\dagger A=pI$，且 index two 消掉全部 sigma semicharacter，原函数
$$
\mathsf X(\alpha z-\overline\beta t)
 \mathsf X(\beta z+\overline\alpha t)
\tag{1016.22}
$$
的 period multiplier 恰为 $L_{2p}\boxtimes L_{2p}$ 的 multiplier。
没有残余 quadratic Gaussian。它给出的线丛比较在原点纤维为一，故正是 (1016.7) 的 rigidified $I_{A,2}$。

转到实际整 local frame 时，每轴只多
$(Y/\sigma)^{2p}$。在各轴次数严格小于 $p$ 的有限范围，
$\sigma^2/Y^2$ 的所需系数为整，且
$$
(\sigma^2/Y^2)^p\equiv1\pmod{p,Y^p}.
\tag{1016.23}
$$
这里取的是合法有限截断的 $p$ 次幂；原非整高项不能降到此范围。
又 $Y=z+O(z^{p^2})$，故 (1016.22) 的首-$p$ 矩形系数与实际 frame 系数相同。特别可以读取 $J_{3,3}$，并没有声称整个 sigma trivialization 为整。

### 6.2 两侧的完整六阶系数

原固定低项为
$$
\mathsf X=x\sigma^2=1+\frac2{15}z^6+O(z^{12}).
\tag{1016.24}
$$
模 $p$ 的微分像为 $u=\kappa w$，
$w=\beta Y+\overline\alpha T$，其中 $\kappa=\alpha/\beta$。
由 (1016.14)、(1016.22)–(1016.24)，
$$
J_{3,3}(I_{A,2}A^*s_{A,2})
=c_A\frac83(\kappa^6+1)(\beta\overline\alpha)^3.
\tag{1016.25}
$$
因 $p\ge41$，式中的固定分母均为单位。

另一方面，(1016.11) 取两轴 $k=3$。只有
$$
r=6i+5,\qquad p-1-r=6j+5,\qquad i+j=N-1
$$
贡献；两指数为奇数，故 Wilson 公式给
$r!(p-1-r)!=1$。于是
$$
\boxed{\quad
J_{3,3}(\Omega_{\gamma,2}w_{0,2})
=\frac{(2B)^6}{36}\gamma^{-5}
 \mathcal C_{N-1}(\gamma^{-1}).
\quad}
\tag{1016.26}
$$
(1016.25) 和 (1016.26) 是同一实际 section 的同一整 jet。所有其它显示因子非零，故
$$
\boxed{\quad
\mathcal C_{N-1}(\gamma^{-1})=0
\iff\kappa^6=-1.
\quad}
\tag{1016.27}
$$

也可保留准确单位比值，而非只取零条件：
$$
\boxed{\quad
\frac{\mathcal C_{N-1}(\eta)}{\mathcal C_N(\eta)}
 =\frac3{2B^6}\eta^{-6}(\alpha^6+\beta^6),\qquad
\frac{\mathcal U_{N-1}(\eta)}{\mathcal U_N(\eta)}
 =-\frac{\eta^{-6}(\alpha^6+\beta^6)}{18B^6},
\quad \eta=\gamma^{-1}.
\quad}
\tag{1016.28}
$$
这是两个完整卷积的比值；它没有将 $\alpha,\beta$ 或某个单独的端系数从源中删除。

## 7. 准确零集的计数与定位

若 $p\equiv11\pmod{12}$，则 $N$ 奇数。假如
$\kappa^6=-1$，则
$$
\kappa^{p+1}=(\kappa^6)^{N+1}=1,
$$
与 $\kappa\in T^-$ 矛盾。因此 (1016.27) 在此行从不为零。

若 $p\equiv5\pmod{12}$，则 $N$ 偶数。
$\kappa^6=-1$ 在 $k$ 中有六个互异解，且
$(\kappa^6)^{N+1}=-1$，所以六个解都属于 $T^-$。
每个 image 方向恰有十二个 norm-$p$ 向量，故 (1016.27) 的 bad 向量恰有七十二个。每个 $\eta=\gamma^{-1}$ 也恰有十二个向量；由同一等价式，它们同时 bad 或同时不 bad。因此 $\mathcal C_{N-1}$ 在 $T^-$ 上恰有六个零点。

还可定位这六点，而不混同核方向与像方向。多项式
$$
C_{N-1}(X)=\sum_{i+j=N-1}a_i a_jX^i
$$
满足准确回文式
$$
C_{N-1}(X)=X^{N-1}C_{N-1}(X^{-1}),
$$
即使某些端系数为零也成立。因为 $N-1$ 奇数且 $p\ne2$，
$C_{N-1}(-1)=0$。
全部六个满足 $\eta^6=-1$ 的 $\eta\in T^-$ 因而都是零点，已经耗尽上面的六点。这证明 (1016.4)。
通过 (1016.21)，$U$ 行有完全相同的零集。

### 7.1 原 $r=8$ 首极块的正确层 $N-2$

这里进一步固定 $p\equiv5\pmod{12}$。取整数
$a,b\ne0$ 满足 $p=a^2+b^2$，并在同一原 CM 环中使用
$$
A=\begin{pmatrix}a&-b\\ b&a\end{pmatrix}.
$$
这是 (1016.5) 的实际特例；$a,b$ 均为 $p$-单位。
其像方向 $\kappa=a/b=\pm i$，$i^2=-1$，核方向
$\gamma=-a/b=-\kappa$，所以在这个特例
$\eta=\gamma^{-1}=\kappa$。这一步明确计算了两种方向，
没有把一般的 $\gamma^{-1}$ 与 $\kappa$ 识别。

原低阶系数由同一 $\wp$ 方程及 $\zeta'=-\wp$ 得
$$
\mathsf X(z)=1+\frac2{15}z^6+\frac4{17325}z^{12}+O(z^{18}).
$$
于是
$$
[z^{12}]\mathsf X(iz)\mathsf X(z)
=\frac8{17325}-\frac4{225}=-\frac4{231}.
$$
两轴次数六均小于 $p$，总次数十二也小于 $p$，故 §6.1
的原整 frame 比较适用。由于
$\binom{12}{6}(-4/231)=-16$，实际拉回给
$$
J_{6,6}(I_{A,2}A^*s_{A,2})=-16c_A(ab)^6.
\tag{1016.A1}
$$
这在每个所述 $p$ 上都是单位。

在另一侧，(1016.11) 的两轴 $k=6$ 只留
$r=6i+8,\ p-1-r=6j+8,\ i+j=N-2$。
两指数均偶，Wilson 符号为负，因而
$$
J_{6,6}(\Omega_{\gamma,2}w_{0,2})
=-\frac{(2B)^{12}}{(6!)^2}\gamma^{-8}
  \mathcal C_{N-2}(\gamma^{-1}).
\tag{1016.A2}
$$
由 (1016.16)、(1016.A1)–(1016.A2)，得到原规范下的准确比值
$$
\boxed{\quad
\frac{\mathcal C_{N-2}(\eta)}{\mathcal C_N(\eta)}
=-\frac{2025a^{12}}{B^{12}},\qquad
\frac{\mathcal U_{N-2}(\eta)}{\mathcal U_N(\eta)}
=-\frac{25a^{12}}{9B^{12}},
\quad\eta=\pm i.
\quad}
\tag{1016.A3}
$$
第二式还用了 $(-27)^{-2}=1/729$。
所有显示的固定分母、$a,b,B,c_A$ 都为单位。
因此 $\mathcal C_{N-2}$ 和 $\mathcal U_{N-2}$
在 $\eta=\pm i$ 非零；因它们只依赖 $\eta^6$，同样在全部
$\eta^6=-1$ 的六点非零。

层数不可移一格：原 bare $n=p-r=6\ell+3$ 的 sigma 总下标
为 $2\ell+1$，减去第一个极块的下标 $N+1$，余下
$2\ell-N$。$r=2$ 时为 $N$，而 $r=8$ 时为
$N-2$，不是 $N-1$。本附记给的是这个正确层的完整卷积单位，
仍须实际识别 bare 的全部 regular 部分和 shifted-factorial
三重卷积，才可推原 $c_{p-8}^-$ 非零。

root 与 o2_high_coefficient 已独立纸面核准两个 Wilson 符号、
常数 $2025,25/9$、核像方向及首-$p$ frame 边界；无数值执行。

### 7.2 Gaussian 方向上的原 scalar 完全值

仍设 $p\equiv5\pmod{12}$，令 $\iota^2=-1$ 于
$\mathbf F_p$。本节不仅给非零，而且固定原共同 scalar：
$$
\boxed{\quad
\mathcal C_N(\iota)
=-\frac12(-432)^{(p-1)/4},\qquad
\mathcal C_N(\iota)^2=-\frac14.
\quad}
\tag{1016.G1}
$$
它也给全部 $\eta^6=-1$ 的相同值。
在 §7.1 的真实 Gaussian norm-$p$ 矩阵中，
$c_A=\mathcal C_N(\iota)$；没有将 $c_A$ 归一成任意单位。

先沿用 [R812 的原 q 模型](R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)
§§3、5、6.1，取
$$
d_0^{12}=-432,\quad
\lambda=d_0\eta_D^{-2},\quad t=\lambda z,
$$
其中 $\eta_D$ 是 Dedekind eta，区别于本篇的方向变量。
定义实际 index-two theta 基
$$
\Theta_r(t,q)=\sum_{a\equiv r\ (2)}q^{a^2/4}e^{at},
\qquad
\Psi_r(z)=\eta_D^{-1}e^{-E_2t^2/12}\Theta_r(t,q),
\quad r=0,1,
$$
以及同一个原代数变换矩阵
$$
\Phi_2=\binom{V}{\mathsf X}
 =U_2\binom{\Psi_0}{\Psi_1}.
\tag{1016.G2}
$$
该 q 规范由原 $\sigma'(0)=1$、没有额外 Gaussian 的 sigma
确定，不能删除 $U_2$ 的共同尺度。

**行列式的准确规范。** Jacobi 恒等式给
$$
\Theta_0(0)\Theta_1''(0)-\Theta_1(0)\Theta_0''(0)
 =2\eta_D^6.
$$
可直接核常数：将
[Jacobi 平方恒等式](https://dlmf.nist.gov/20.7.E4)
在零点二次微分，再用
[导数乘积式](https://dlmf.nist.gov/20.4.E6)，得到
$\theta_3''/\theta_3-\theta_2''/\theta_2=\theta_4^4$。
本节 $\Theta_0(t)=\theta_3(-it,q)$、
$\Theta_1(t)=\theta_2(-it,q)$，故其 Wronskian 为
$\theta_2\theta_3\theta_4^4=2\eta_D^6$，最后等式直接由三个
Jacobi 乘积相乘得到。
原 $\Phi_2$ 的零、二阶导数矩阵行列式为 $-2$，而
$\Psi$ 的相同行列式为 $2\lambda^2\eta_D^4=2d_0^2$。
所以
$$
\boxed{\quad\det U_2=-d_0^{-2}.\quad}
\tag{1016.G3}
$$

**保完整 first-$p$ 频率和。** 取
$$
\mathscr B_2=[z^{p-1}]\Phi_2(z)\Phi_2(\iota z)^{\mathsf T}.
$$
两个 index-two Gaussian 精确抵消。
这里没有 R812 使用 $L^2,L^3$ 时的五个缺端项，
因为当前只是读取未微分乘积的完整 $p-1$ 系数。
Wilson 给每对整数频率的系数
$$
-\eta_D^{-2}\lambda^{p-1}(a+\iota b)^{p-1}.
$$
把该幂写成 $1-1_{\{a+\iota b=0\bmod p\}}$。
非格点一项在原基中为
$-\lambda^{p-1}\Phi_2(0)\Phi_2(0)^{\mathsf T}$，其
$VV$ 条目恒为零，因为 $V(0)=0$。

另一项用真正 Gaussian 理想重新索引。
选择 $p=m_0^2+n_0^2$、$m_0+\iota n_0=0\bmod p$，
写 $a=m_0c-n_0d,\ b=n_0c+m_0d$。
二次频率变为 $p(c^2+d^2)$。
模二的矩阵只有恒等或两轴交换；作用于同一个 theta-value
外积时两者相同。因此零指标格给的正是该外积的 Frobenius，
没有额外排列、Gauss scalar 或丢失的半周期。

令
$$
M_2=U_2(U_2^{(p)})^{-1},\qquad v_0=\Phi_2(0)=\binom01.
$$
所有 eta/lambda 幂的比准确为
$\lambda^{p-1}\eta_D^{2p-2}=d_0^{p-1}$，所以在原
$VV$ 条目有
$$
-\mathcal C_N(\iota)
 =d_0^{p-1}(M_2)_{V,\mathsf X}^{\,2}.
\tag{1016.G4}
$$
左侧的负号也可直接从
$V(\iota z)=-z^2\sum a_j(-1)^jz^{6j}$ 核准；
$N$ 为偶数，所以读数恰是 $-\mathcal C_N(\iota)$。

**CM 处真实 Frobenius 矩阵。** 取 $r=\sqrt3$、$e^3=1$。
原半周期作用在 $\Phi_2$ 列基上的 row 矩阵为
$$
H_e=\frac1r
 \begin{pmatrix}-1&e^{-1}\\2e&1\end{pmatrix}.
\tag{1016.G5}
$$
它由实际 multiplier
$(x-e)/(er)$ 和 R1017 (1017.8) 的加法式得到。
标准 level-two theta 矩阵的条目在 $\mu_4$ 中；
因 $p\equiv1\pmod4$，其 Frobenius 不变。
由 $H_eU_2=U_2D_e$ 及其 Frobenius 式，得到
$$
M_2H_e^{(p)}=H_eM_2.
$$
而 $\sum_eH_e=\operatorname{diag}(-r,r)$，在当前同余类
$r^p=-r$。因此 $M_2$ 反对角。
再用 $e=1$ 的完整矩阵，得
$$
M_2=\begin{pmatrix}0&\mu\\-2\mu&0\end{pmatrix}.
$$
由 (1016.G3)，
$$
2\mu^2=\det M_2=d_0^{2(p-1)}.
$$
代入 (1016.G4)，得到
$\mathcal C_N(\iota)=-d_0^{3(p-1)}/2$，即 (1016.G1) 的第一式。
再用
$(-432/p)=(-3/p)=-1$，得到其平方为 $-1/4$。

**实际 CM 评价的整性。** 此处未把 $\lambda$、q 参数或完整
非整 sigma 当作 supersingular 单位。
如 R812 §6.1，先把 (1016.G2) 代数化为 level-two theta
变换和行列式规范，再评价。这个小 index 情形可直接排除所有
$p>3$ 的坏分母：在 (1016.G5) 中，固定 $i=(\zeta-\zeta^2)/r$，可取
$$
w_+=(1,1+r)^{\mathsf T},\qquad
w_-=H_\zeta w_+
=-\frac{(1+r)(1+i)}2(1,1-r)^{\mathsf T}.
$$
该基行列式为 $r(1+r)(1+i)$，仅在二、三处可能不是单位。
在与原实半周期及 $\zeta$ 半周期一致的标记下，标准 theta 基
相对于上述 Heisenberg 基只带固定 $\mu_4$ 单位相位及一个共同尺度；
该共同尺度的平方再由 (1016.G3) 固定为单位。
因此 $U_2,U_2^{-1},M_2$ 在全部所述素数均可合法约化。
整个 apolar 输入只用各轴次数 $<p$ 的已证整截断。

o1_theta、o2_high_coefficient 与 root 分别核准了本节全部尺度、
原 theta Wronskian、完整格指标、Wilson 符号、row-action、
实际 CM 整性和共同 scalar；无数值执行。
本节仅断言这六个 Gaussian 方向的完全值；
后继 [R1022](R1022-original-theta-all-direction-constant-square.md) 已独立证明
全方向常平方，并用本节值确定整个 5mod12 行的常数为一。
这些结论仍未推出原 bare $A_r+BT_r$ 非零或 primitive/Legendre 同标签单位。

## 8. 对原问题的准确适用范围

本篇确实给出了同一个原 sigma 源的、对全部 $p\ge41$ 的非零结论，
并精确定位了一条相邻完整卷积的零点。它们比单纯的非零 section 或维数计数更强，因为被读取的就是 (1016.2) 指定的实际有限系数和。

然而 $\mathcal U_N$ 或 $\mathcal U_{N-1}$ 的非零，并不逐个决定
$u_N,u_{N-1}$。R1015 的原 bare 系数仍是
$$
c_{p-2}^-=\frac{49}{6}(u_N^2-R_{p-2}/C_{22}),\qquad
c_{p-8}^-=\frac{7^8}{342}(u_{N-1}^2-R_{p-8}/C_{22}),
$$
其中全部 $R_n$ 必须保留。任何从本篇卷积到这个差的进一步比较，须给实际 jet、除 $p$ 层和余项的完整恒等式。

同样，本篇的 $a_i,b_i,u_i$ 不可冒认成原 $f_i,g_j$ 的某个保留标签；
O1 要求的原 primitive/Legendre 因子仍在。R1013 的 $H_p$、实际全局高度、R1014 的非 CM 首提升与全部 O0 分支继续处理；Serre 主目标仍 OPEN。

## 9. 依赖与全文核准

- [R1012](R1012-original-p-similitude-divided-high-coordinates-and-critical-bridge.md)：每个核/像方向的十二表示与原实际 $A_v$。
- [R1013](R1013-original-theta-descent-and-uniform-critical-zero-bound.md)：实际有限平坦 splitting、完整分布不变条件和 $\Omega_\gamma$；本篇另证 $m=1,2$ 的实际线丛和小角色源。
- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md)：原分布、Bell 比较与 local-frame 规范；(1016.9)–(1016.11) 明确核准其 index-$m$ 版本。
- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md)、[R702](R702-first-pole-block-and-uniform-shifted-units.md)：原 sigma multipliers、CM quasiperiod 与有限整性；本篇未重做既有数值窗口。
- [R1015](R1015-original-class-two-Poincare-projection-and-balanced-triangular-bridge.md)：相同 $U$ 与必须保留的 bare 高系数完整余项。
- 有限平坦下降及 theta 表示唯一性的原始定理使用 R1013 已实读的 Moonen, Theorem 8.10、Proposition 8.15，以及 Shin, Propositions 2.12–2.13；本篇不使用 étale $p$-核算法。

o1_theta 与 root 独立核准 index-one 的二-primary kernel 点和、两轴 Picard 判据、rigidified CM 权、两个 Wilson 符号、首-$p$ frame 比较、下一层准确比值和双十二计数。无数学程序执行，没有重新计算旧矩阵、常数窗口或素数扫描。


## 后继：全部行的绝对常平方现为一

[R1027](R1027-original-level-p-squared-theta-distribution-and-constant-one.md)
用实际 $L_{p^2}$ 的 genuine 第 $p$ 个 theta distribution、
$A^\dagger A=[p]$ 的刚化复合及 R1025 的实际 dagger 符号，
证明全部 $p\ge41,\ p\equiv5\bmod6$ 都有 $D_p=1$。
共同 $\delta'_p$ 仍保其 $\pm1$ 符号；原 primitive/Legendre
同标签和 bare 完整余项不因此自动关闭。
