# R624 — 原两 forcing 行列式的整双输入观察与四位除法返回

日期：2026-11-15。**状态：已证明的同源不变量接口；指定非零性未解决。**

本篇对原两个 forcing 的第一、第二块行列式给出三个完全相同的实际表示：原双输入变换的一条有限系数行、保留全部 Gaussian 中间项的固定 addition 分子、以及原 $\psi_p$ 最高 $2s$ 个系数的四位精度返回。第一表示的选择系数是准确的 $1/8$；第二表示有三项而非单一 theta 配对；第三表示在原坏项已出现的第二块仍只需 $\psi_p\bmod p^4$，但必须先支付除法的整性。

它与 R595/R606 的原两中央条件相接，仍保完整低余项与实际一次除 $p$ 商。没有把共同剪切的不变量另赋为零，也没有把 ordinary 的 $C_{12}=-A_{12}$ 搬到惰性素数。

## 1. 同一原两块与合法有限窗口

固定
$$
p=6s-1>71,\qquad d=p+1,\qquad w=z^6,\qquad
L=(p^2-1)/6,
$$
并在本题同一个 $p$ 整、$b$ 为单位的 $y^2=x^3+b$ frame 中使用
$$
D_zx=2y,\quad D_zy=3x^2,\quad
\sigma(z)=z+O(z^7),\quad D_z^2\log\sigma=-x.
\tag{1}
$$
取原 R606/R614 允许的 $c'-c\in\mathcal O$，置
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,\qquad
F_\ell=e^{-6c'z^d}f_\ell .
\tag{2}
$$
这里 $f_4$、$f_1$ 的原阶分别为四和一。定义原实际系数
$$
c_\ell=[w^{s-1}](z^{-\ell}F_\ell),\qquad
d_{\ell,2}=[w^{2s-1}](z^{-\ell}F_\ell),
\qquad \ell=4,1,
$$
$$
\boxed{\mathfrak D_p=c_4d_{1,2}-c_1d_{4,2}\pmod p.}
\tag{3}
$$
R614 的原加法整性给 $z^{-\ell}F_\ell$ 在 $w^{<L}$ 全整。
本篇双输入选择仅用至 $w^{3s-2}$，且
$$
3s-2<p<L.
\tag{4}
$$
故全部约化是在原实际整系数上进行，未先约化一个有 $p$ 极点的 raw sigma。

改变 $c'$ 为 $c'+\eta$ 时，
$$
(c_4,c_1)\longmapsto(c_4,c_1),\qquad
(d_{4,2},d_{1,2})\longmapsto
(d_{4,2},d_{1,2})-6\eta(c_4,c_1).
\tag{5}
$$
所以 (3) 是原两个块的真实不变量。下文直接读取这个不变量，而不删除任何第二块。

## 2. 一条 Hadamard 行准确读取整个行列式

因为 $F_4$ 在原点至少四阶零，下面两个函数均整：
$$
A(z)=F_4(z)/z^3,\qquad B(z)=F_1(z).
$$
两者都只含 $1\bmod6$ 次幂。定义实际整双输入核
$$
\mathcal K_{c'}(z,t)
=A(z+t)B(z-t)-B(z+t)A(z-t).
\tag{6}
$$
变换 $(z,t)\mapsto(z+t,z-t)$ 的行列式为 $-2$，在当前全部素数处是单位。除 $z^3$ 只在显示的原四阶零来源上使用；这不是在任意来源或任意普通测度上自由除 logarithm。

**定理 1。**
$$
\boxed{
\mathfrak D_p
=8[z^{\,2p-5}t^{\,p-2}]\mathcal K_{c'}(z,t)\pmod p.
}
\tag{7}
$$

**证明。** 写
$$
A(z)=\sum_{i\ge0}a_i z^{1+6i},\qquad
B(z)=\sum_{i\ge0}b_i z^{1+6i}.
$$
于是
$$
(a_{s-1},b_{s-1})=(c_4,c_1),\qquad
(a_{2s-1},b_{2s-1})=(d_{4,2},d_{1,2}).
$$
目标总次数为 $3p-7=18s-10$，故原两个指标满足
$i+j=3s-2$，均在 (4) 的实际整窗口。

令 $u=1+6i,v=1+6j$，则 $u+v=3p-7$。所读变换系数是
$$
K_{p-2}(u,v)=[T^{p-2}](1+T)^u(1-T)^v.
$$
因 $p-2<p$，Lucas/Frobenius 只留下 $u,v$ 的最低 $p$ 进位数
$u_0,v_0$。其和只能是 $p-7$ 或 $2p-7$：
第一种的次数不足 $p-2$，整项为零；第二种迫
$$
p-6\le u_0,v_0\le p-1.
$$
再用 $u,v\equiv1\pmod6$、$u,v\ge1$，只有
$$
(u,v)=(p-4,2p-3),\qquad(2p-3,p-4)
\tag{8}
$$
两个实际单项式。候选 $3p-2$ 已超过总次数，故不另有最高进位项。

对第一项，
$$
K_{p-2}(p-4,2p-3)
=[T^{p-2}]\frac1{(1+T)^4(1-T)^3}
=[T^{p-2}]\frac{1-T}{(1-T^2)^4}.
$$
写 $p-2=2m+1$，$m=(p-3)/2$，其值为
$$
-\binom{m+3}{3}\equiv\frac1{16}\pmod p.
$$
交换 $u,v$ 因 $p-2$ 为奇数而变号。式 (6) 在两项的原系数分别为
$\mathfrak D_p$、$-\mathfrak D_p$，故总值为
$2\mathfrak D_p/16=\mathfrak D_p/8$。这证明 (7)，并支付了其它所有原系数确实被该行杀掉。$\square$

这是一条完整有限双输入观察，不是将两个不同来源的边际系数拼合。

## 3. 固定 addition 分子、准确符号与全部除子

本节用
$$
x=x(z),\ y=y(z),\qquad v=x(t),\ Y=y(t),
$$
并置
$$
\Delta=v-x,\quad
N=x^2v^2-4b(x+v),
$$
$$
P_z=x^3+3x^2v+4b,\qquad
P_t=v^3+3xv^2+4b.
\tag{9}
$$
令 $s_+=z+t,s_-=z-t$，并把 $x(s_\pm),y(s_\pm)$ 写成 $x_\pm,y_\pm$。
原群加法直接给
$$
x_+x_-=\frac{N}{\Delta^2},\qquad
y_++y_-=\frac{2yP_t}{\Delta^3},\qquad
y_+-y_-=-\frac{2YP_z}{\Delta^3}.
\tag{10}
$$
例如
$$
x_\pm=
\frac{xv(x+v)+2b\mp2yY}{(v-x)^2},
$$
代 $y^2=x^3+b,Y^2=v^3+b$ 即得第一式；斜率公式给其余两式。
原 sigma addition 的首项固定为
$$
\sigma(z+t)\sigma(z-t)
=(v-x)\sigma(z)^2\sigma(t)^2.
\tag{11}
$$

因此原两个混合核为
$$
\begin{aligned}
M_+(z,t)
&:=f_4(s_+)f_1(s_-)+f_1(s_+)f_4(s_-)\\
&=-2y\,\Delta N P_t\,\sigma(z)^{12}\sigma(t)^{12},\\
M_-(z,t)
&:=f_4(s_+)f_1(s_-)-f_1(s_+)f_4(s_-)\\
&=-2Y\,\Delta N P_z\,\sigma(z)^{12}\sigma(t)^{12}.
\end{aligned}
\tag{12}
$$
所有正负号来自 (1)、$f_1=-xy\sigma^6$ 与 (11)，没有另选半特征。

未去 Gaussian 的 (6) 因而等于以下**固定完整函数**：
$$
\boxed{
\mathcal H(z,t)=
\frac{2\Delta N\,\sigma(z)^{12}\sigma(t)^{12}}
     {(z^2-t^2)^3}
\left\{
t(3z^2+t^2)yP_t-z(z^2+3t^2)YP_z
\right\}.
}
\tag{13}
$$
为核分母，直接从原来源写
$$
\mathcal H=
\frac{s_-^3 f_4(s_+)f_1(s_-)
      -s_+^3f_1(s_+)f_4(s_-)}
{s_+^3s_-^3}.
\tag{14}
$$
分子在每条 $s_\pm=0$ 上至少四阶零，因此 (14) 在两条相交直线上的除法都合法，商仍整，且分别至少一阶零。这也支付交点；没有只凭一般点的可除性删除交点条件。

式 (12) 的两份 theta 核各属于 $S_{12}\otimes S_{12}$；在 (13) 中，显式 $z,t$ 乘子及 $(z^2-t^2)^{-3}$ 仍是原观察的一部分。**整个商不被冒认为另一个 $S_{12}\otimes S_{12}$ theta 截面或其 CM 投影。**

原低阶系数给
$$
f_4/z^3=z\{1-4bz^6/35+\cdots\},\qquad
f_1=z\{1+6bz^6/35+\cdots\},
$$
故
$$
\mathcal H(z,t)
=-\frac{8b}{7}zt(z^2-t^2)
 (3z^4+10z^2t^2+3t^4)+O((z,t)^{14}).
\tag{15}
$$
特别整个固定核非零，最低总阶为八。
这不使 (7) 的随 $p$ 指定高阶行自动非零。

## 4. Gaussian 中间项：准确保留三份贡献

令
$$
g(z)=6c'z^d,\qquad
\mathcal B(z,t)=
g(z+t)+g(z-t)-2g(z)-2g(t),
$$
$$
\mathcal H_{c'}(z,t)
=e^{-12c'z^d-12c't^d}\mathcal H(z,t).
\tag{16}
$$
由定义得到特征零的整条恒等式
$$
\boxed{\mathcal K_{c'}=e^{-\mathcal B}\mathcal H_{c'}.}
\tag{17}
$$
中间偶二项式的每个系数都含一个 $p$，而 $v_p(c')=-1$，
所以 $\mathcal B$ 的全部系数整。置 $a=\overline{6pc'}=\overline{6pc}$，
则
$$
\boxed{
\overline{\mathcal B}(z,t)
=2a\!\!\sum_{\substack{2\le k\le p-1\\k\ {\rm even}}}
\frac{z^{p+1-k}t^k}{k(k-1)}.
}
\tag{18}
$$
这里使用
$\binom{p+1}{k}/p\equiv1/(k(k-1))$（$k$ 为所列偶数）。
所以该中间项一般非零；不能因未除的二项式含 $p$ 就将它删掉。

(4) 支付 $\mathcal K_{c'}$ 所需的全部系数整。
反用 $\mathcal H_{c'}=e^{\mathcal B}\mathcal K_{c'}$，
在目标总次数 $3p-7$ 内只用有限阶数和 $p$ 单位阶乘，
故 $\mathcal H_{c'}$ 的同一有限窗口也整。
这不是分别约化 (13) 的有极椭圆函数因子。

由 (15)，$\mathcal H_{c'}$ 的最低总阶仍为八。
$\mathcal B$ 的总阶为 $p+1$，因此目标行只能有 $r=0,1,2$ 三项：
$$
\boxed{
\mathfrak D_p
=8[z^{2p-5}t^{p-2}]
\left(1-\overline{\mathcal B}
      +\frac{\overline{\mathcal B}^{\,2}}2\right)
\overline{\mathcal H}_{c'}\pmod p.
}
\tag{19}
$$
这是本篇固定 addition 返回的完整式。
从 $S_{12}$ 的某个非退化有限矩阵直接猜该行非零，会遗漏 (19) 的第二、第三项以及 (13) 的原坐标除子。

改变 $c'$ 后，(18) 不变，而 $\mathcal H_{c'}$ 还须乘
$e^{-12\eta(z^d+t^d)}$。式 (5)、(7) 证明 (19) 的**全部和**
不变；不要求其中三项各自不变。

## 5. 同一原除法多项式的四位精度返回

本节把 (3) 的两个真实块直接接到原 $\psi_p$，不是引入另一 sigma。
为避免与双输入 $t$ 混淆，本节仍把原参数记为 $\tau=bu^6$：
$$
u=x^{-1/2},\quad z=uH(\tau),\quad
C(\tau)=(1+\tau)^{-1/2},\quad
K(\tau)=(\sigma(z(u))/u)^6,\quad L_K=\log K.
$$
所有运算限定在
$$
\mathcal R=\mathcal O[\tau]/\tau^{2s}.
\tag{20}
$$
此处 $2s-1<p<L$，$H,C$ 全整；$L_K$ 的各系数赋值至少 $-1$。
后者也由 R591 的
$Q_n=-(6n-4)Q_{n-1}/(6n-1)$ 直接得到：
此窗口唯一的坏分母类是 $n=s$，其后至 $2s-1$ 没有第二次坏分母。

保奇数标准除法多项式 $\psi_p(x)$ 的首项
$p x^{(p^2-1)/2}$，定义其真实反转系数
$$
Q_p(\tau)
=u^{p^2-1}\psi_p(u^{-2}),
\qquad u^6=\tau/b.
\tag{21}
$$
因此 $Q_p$ 是原最高系数加上显示的 $b^{-j}$ 单位尺度，
而非新构造的多项式。原同一 sigma 乘法式为
$$
Q_p=\frac{\sigma(pz(u))}{u}\exp(-p^2L_K/6).
\tag{22}
$$

在 (20) 中准确有
$$
\frac{\sigma(pz(u))}{u}=pH(\tau)+p^7\tau E(\tau),
\qquad E\in\mathcal R.
\tag{23}
$$
证明：需要的 $z$ 次数至多 $12s-5=2p-3$。
原 $\sigma/z$ 在相应 $w^{<2s}$ 的系数赋值至少 $-1$，
只有 $w^{\ge s}$ 才可能坏；这是 R614 的
$\sigma/z=e^{cw^s}U$、$U$ 整和此窗口最多一个 Gaussian 因子的直接结果。
对 $1\le n<s$，$\sigma$ 的 $z^{6n+1}$ 系数整，
代入 $pz(u)$ 后至少有 $p^7$；
对 $s\le n<2s$，即使损失一个 $p$，仍至少有
$p^{6s}=p^{p+1}$。原 $H$ 在 (20) 整，故代换不再损失精度。
这完整证明 (23)，而非把原 $\sigma$ 在第二块当成全整。

由 (22)、$v_p(L_K)\ge-1$，得到
$$
Q_p\in p\mathcal R,\qquad
T_p:=Q_p/(pH)\in1+p\tau\mathcal R,
$$
$$
\boxed{
\log T_p=-p^2L_K/6+p^6 E_1,\qquad E_1\in\mathcal R.
}
\tag{24}
$$
有限 log 只涉及小于 $p$ 的指数，全部除数合法。

现在取 R606 的原规范
$$
c_b^\dagger=-\frac{b^s C_s}{p(p+1)},\qquad
\Lambda^\dagger
=K\exp\{-6c_b^\dagger b^{-s}\tau^sH^d\}.
$$
定义
$$
\boxed{
\mathscr L_p^\dagger
=-\frac6{p^2}
 \left\{\log T_p+
 p^2c_b^\dagger b^{-s}\tau^sH^d\right\}.
}
\tag{25}
$$
式 (24) 准确给
$$
\mathscr L_p^\dagger
=\log\Lambda^\dagger+p^4E_2.
\tag{26}
$$
R606/R614 已付 $\Lambda^\dagger$ 在 (20) 整，且常数一；
因 $2s-1<p$，其有限 log 也整。
所以 (25) 花括号**整体**属于 $p^2\mathcal R$。
没有把其两个分别可能只有一次 $p$ 的项先除 $p^2$ 后擅自约化。

令
$$
\mathcal T_p=\exp(\overline{\mathscr L_p^\dagger})
=\overline{\Lambda^\dagger}
\quad\text{于 }k[\tau]/\tau^{2s}.
$$
完整原留数换元并保 $H^{-hp}$，再在本窗口使用 $\bar H^p=1$，
给同一 (3) 的明确式
$$
\boxed{
\mathfrak D_p
=b^{3s-2}
\det
\begin{pmatrix}
[\tau^{s-1}]\mathcal T_p C&
[\tau^{2s-1}]\mathcal T_p C/H\\
[\tau^{s-1}]\mathcal T_p H^3&
[\tau^{2s-1}]\mathcal T_p H^2
\end{pmatrix}.
}
\tag{27}
$$
准确输入精度是原 $Q_p\bmod p^4$、$H\bmod p^3$，
以及已定的 $pc_b^\dagger\bmod p^2$。先除原 $Q_p$ 的一个 $p$，
再按 (25) 对已经整体整除的量除 $p^2$；
故四位精度足够恢复 (27)，包括第二块。

这将 serre-uniformity 的 R760 第一临界窗口延长到了本题真实第二块，
没有重新计算其除法多项式。
R757 的 $Q_p\bmod p^2$ 单位只读原 $H$；
在 (24) 中，决定 (27) 的正常 log 修正仍位于更深的 $p^3$ 系数。
因此浅精度的 Frobenius 常数单位不使 (27) 自动非零。

## 6. 原两中央同时失败时的实际必要式

保已经发表的全块矩阵 note：
$$
\mathbf g_h=\mathsf M\mathbf d_h+\mathbf R_h,\qquad
\mathsf M=
\begin{pmatrix}
17\cdot503/45&-17\cdot488/45\\
12\cdot1472/5&-12\cdot1467/5
\end{pmatrix},
\quad \det\mathsf M=-266084/15.
\tag{28}
$$
每个 $\mathbf R_h$ 都是原 $\Lambda$ 的显示低截断卷积。
在本节用同一个 canonical $c_b^\dagger$。
若原完整 $j_{34}=j_{72}=0$，令
$$
\mathbf q=\overline{(g_{34,1},g_{72,1})^t/p},\quad
C_*=\overline{b^sC_s},\quad
\mathsf D=\operatorname{diag}(34,72).
$$
这里 $\mathbf q$ 是原实际商，包含 R606 的整个 $H^{-p}$ log 修正。
R595/R606 准确给
$$
\mathbf c=-\mathsf M^{-1}\mathbf R_1,\qquad
\mathbf d_2=-\mathsf M^{-1}
(\mathbf R_2+C_*\mathsf D\mathbf q).
$$
因而现在有完整同源必要式
$$
\boxed{
8[z^{2p-5}t^{p-2}]
\left(1-\overline{\mathcal B}
+\frac{\overline{\mathcal B}^{\,2}}2\right)
\overline{\mathcal H}_{c_b^\dagger}
=
(\det\mathsf M)^{-1}
\det(\mathbf R_1,\mathbf R_2+C_*\mathsf D\mathbf q).
}
\tag{29}
$$
左端也准确等于 (27) 的原四位 division 表示。
这给原不变量一个固定双输入观察和一个全局 division 数据入口，
不是新增的中央零。

尚未证明 (7)、(19) 或 (27) 非零；
也未证明 (29) 与原递推不相容。
不能删掉 (19) 的 Gaussian 补项、(29) 的 $\mathbf R_1,\mathbf R_2,\mathbf q$，
不能将原两中央零传给任意双变量 coefficient，
也不能把固定核 (15) 非零改称其指定随 $p$ 的行非零。
本篇不改变主目标的完成状态。

## 依赖与复用范围

- [R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)：同一个原 $f_4,f_1$ 和 sigma/微分规范。本篇 §3 自含所用 addition 推导。
- [R591](R591-original-inert-forcing-in-one-parameter-and-exact-resonance.md)、[R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)：原 $K,C,H$ 和完整留数。
- [R606](R606-original-gaussian-unit-gauge-and-canonical-second-central-row.md)：canonical Gaussian、真实一次商及两 $\Xi$。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：全部实际 $n<L$ 整窗口。
- [全块矩阵 note](../notes/2026-11-15-canonical-all-block-matrix-and-wilson-boundary.md)：(28) 的全部 $h$ 精确式和完整残差。
- [Serre R757](../../serre-uniformity/results/R757-full-original-division-polynomial-mod-p2-and-Frobenius-constant-units.md)、[Serre R760](../../serre-uniformity/results/R760-original-critical-sigma-jets-from-four-digit-division-data.md)：同一原奇 division identity、浅精度及第一临界四位接口。本篇 §5 自含第二块的分母和端点证明。

以上是一般恒等式、有限整除和 Lucas 选择证明；没有以新增素数扫描作为论证输入。
