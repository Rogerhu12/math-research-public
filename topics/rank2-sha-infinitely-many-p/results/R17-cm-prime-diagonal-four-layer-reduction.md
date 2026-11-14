# R17. CM 素数对角 trace 的四层固定级数归约

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

本结果把 R6 的 $a_{(p-3)/2}\bmod\mathfrak p^4$ 写为四个固定特征 $0$ 级数的对角系数。最低层为代数级数；其余三个含对数的层不是 D-finite。没有由此证明所需的无穷非消失性。

## 1. 固定对象和主公式

沿用 [R6](R6-cm-trace-recurrence.md) 及 [R13](R13-cm-trace-nonholonomicity.md) 的
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
F=K(u),\quad v^2=u^3-17u,
$$
其中 $(u,v)=P_f$ 为所用的 $f=34(1+i)$-division 点，$u,v$ 是代数整数。外部算术输入仍只是 CLS（2009）§3 的这一固定 torsion 点构造；其出处和相关导数递推见 R6。本结果不额外使用新的 Sha 定理。

定义固定有理函数
$$
S(X)=\operatorname{Tr}_{F/K}\!\left(\frac{v}{X-u}\right)\in K(X).
\tag{1}
$$
在无穷远点取参数 $t=-x/y$，并置
$$
s(t)=\sqrt{1+68t^4},\qquad
x(t)=\frac{1+s(t)}{2t^2},\qquad y(t)=-\frac{x(t)}t.
\tag{2}
$$
平方根取常数项为 $1$ 的支。再定义
$$
A(t)=\frac{\log_E(t)}t
=\sum_{k\ge0}\frac{(-1)^k\binom{2k}{k}17^k}{4k+1}t^{4k},
\qquad L(t)=\log A(t),
\tag{3}
$$
以及
$$
R(t)=\frac{S(x(t))}{s(t)},\qquad
U_j(t)=R(t)L(t)^j\quad(j=0,1,2,3).
\tag{4}
$$
这些对象均独立于 $p$。$R$ 是代数度至多 $2$ 的非零代数级数，属于 $\mathbb Z[i][[t]]$，且 $\operatorname{ord}_tR\ge2$；$L\in t^4\mathbb Q[[t]]$。

对素数 $p\ge5$，令
$$
b_j(p)=[t^{p-1}]U_j(t),\qquad u_p=\frac{(p-1)!}{2}.
$$
则 $b_j(p)$ 均为 $p$-integral，且有精确的特征 $0$ 系数公式
$$
\boxed{\quad
a_{(p-3)/2}=u_p[t^{p-1}]R(t)A(t)^{-p}.
\quad}
\tag{5}
$$
其模 $p^4$ 归约为
$$
\boxed{\quad
a_{(p-3)/2}\equiv
u_p\left(b_0(p)-p b_1(p)+\frac{p^2}{2}b_2(p)
-\frac{p^3}{6}b_3(p)\right)\pmod{p^4}.
\quad}
\tag{6}
$$
这里可在 $K\otimes\mathbb Q_p$ 的整数环中解释同余，也可在任一指定的 $\mathfrak p\mid p$ 处解释。对本题使用的 $p\equiv1\pmod4$、$p\ne17$，两种表述都适用。

## 2. 加法公式把奇部变成一个有理函数的导数

令 $P=(x,y)$，$P_\sigma=(u^\sigma,v^\sigma)$。在加法公式分母不为零的开集上，
$$
x(P+P_\sigma)=
\left(\frac{y-v^\sigma}{x-u^\sigma}\right)^2-x-u^\sigma.
$$
因此
$$
\frac{x(P+P_\sigma)-x(-P+P_\sigma)}2
=-\frac{2yv^\sigma}{(x-u^\sigma)^2}.
$$
求和，并记 $\delta x=2y$，得到有理函数恒等式
$$
g_o(P)=-2y\operatorname{Tr}_{F/K}\frac{v}{(x-u)^2}
=\delta S(x).
\tag{7}
$$
由于两边都是有理函数，在稠密开集上的等式已给出全局等式。

R13 已证明
$$
g_o^{(2n+1)}(0)=2a_n
$$
（$z$ 是满足 $\omega=dz$ 的复均匀化参数）。由式 (7)，
$$
\frac{d^{2n+2}}{dz^{2n+2}}S(x(z))\bigg|_{z=0}=2a_n.
\tag{8}
$$
特别地，取 $2n+2=p-1$，
$$
a_{(p-3)/2}=\frac{(p-1)!}{2}[z^{p-1}]S(x(z)).
\tag{9}
$$
这确定了式 (5) 中的 $2$ 倍和阶乘，未使用渐近近似。

## 3. 参数微分与 Lagrange 换元

对式 (2) 直接微分，或者从 $t=-x/y$ 和曲线方程计算，得到
$$
\omega=\frac{dx}{2y}=\frac{dt}{\sqrt{1+68t^4}}
=\frac{dt}{s(t)}.
\tag{10}
$$
逐项积分即给出式 (3)，且
$$
z=\log_E(t)=tA(t),\qquad dz=\frac{dt}{s(t)}.
\tag{11}
$$
形式留数的换元法则给出，对任意 $m\ge0$，
$$
\begin{aligned}
[z^m]S(x(z))
&=\operatorname{Res}_{z=0}\frac{S(x(z))\,dz}{z^{m+1}}\\
&=\operatorname{Res}_{t=0}
\frac{S(x(t))\,dt}{s(t)\,t^{m+1}A(t)^{m+1}}\\
&=[t^m]R(t)A(t)^{-m-1}.
\end{aligned}
\tag{12}
$$
该换元合法，因为 $z=t+O(t^5)$，是形式幂级数的可逆换元。取 $m=p-1$ 并代入式 (9)，得到式 (5)。

## 4. 整性与模 $p^4$ 截断

先证明 $R$ 的全局整性。令 $w(t)=1/x(t)$，则曲线方程给出
$$
w=t^2-17t^2w^2.
$$
由系数递推，存在唯一 $w\in t^2\mathbb Z[[t]]$ 满足此式，其首项为 $t^2$。另一方面，
$$
\frac1{s(t)}=
\sum_{k\ge0}(-1)^k\binom{2k}{k}17^kt^{4k}\in\mathbb Z[[t]].
$$
因为 $u,v$ 是代数整数，
$$
S(x(t))
=\sum_{m\ge0}\operatorname{Tr}_{F/K}(vu^m)w(t)^{m+1}
\in t^2\mathbb Z[i][[t]].
$$
故 $R\in t^2\mathbb Z[i][[t]]$。$S$ 不为零：它的各部分分式的极点 $u^\sigma$ 互异，且对应留数 $v^\sigma\ne0$。因此 $R$ 也不为零。

在式 (5) 所需的 $t^{p-1}$ 系数中，因 $R$ 的阶至少为 $2$，只需使用 $A^{-p}$ 到 $t^{p-3}$ 为止。此范围内，式 (3) 的任何分母 $4k+1$ 都满足
$$
1\le4k+1\le p-2;
$$
所以 $A$ 在该截断范围内 $p$-integral。对 $p\equiv1\pmod4$，$A$ 首个可能带有分母 $p$ 的项次数是 $p-1$，恰好位于本计算范围之外。

又因 $A-1$ 起于 $t^4$，在 $\log A$ 的该截断中，只会出现
$$
\frac{(-1)^{h-1}(A-1)^h}{h},
\qquad h\le\lfloor(p-3)/4\rfloor<p.
$$
故 $L$ 的所需系数也 $p$-integral。这同时证明每个 $b_j(p)$ 的 $p$ 整性。

最后，在同一截断范围内，
$$
A^{-p}=\exp(-pL)
=\sum_{j\ge0}\frac{(-p)^j}{j!}L^j.
$$
所有能够贡献的 $j$ 都小于 $p$，故 $j!$ 是 $p$-adic 单位。每个 $j\ge4$ 的贡献均落在 $p^4$ 中。因此
$$
A^{-p}\equiv1-pL+\frac{p^2}{2}L^2-\frac{p^3}{6}L^3
\pmod{p^4,t^{p-2}},
$$
乘 $R$ 并取 $t^{p-1}$ 系数就得到式 (6)。$u_p$ 是 $p$-adic 单位，不改变赋值门槛。

## 5. 最低层的固定线性微分空间，以及原始等价形式

由式 (2)，$R\in K(t,s)$，而 $s^2=1+68t^4$。这个二次函数域作为 $K(t)$-向量空间由 $1,s$ 生成，且在 $d/dt$ 下稳定。因此 $R,R',R''$ 在此二维空间中线性相关；清分母后，$R$ 满足一个阶至多 $2$ 的多项式系数线性微分方程。亦即 $U_0=R$ 为 D-finite。

也可以直接对 $g_o$ 应用 Lagrange 反演。若
$$
G(t)=g_o(P(t)),\qquad H(t)=G'(t)A(t)^2,
$$
则式 (8) 等价于
$$
a_{(p-3)/2}
=\frac{(p-3)!}{2}[t^{p-3}]H(t)A(t)^{-p}.
\tag{13}
$$
此形式亦可按同样方法截断成 $H,HL,HL^2,HL^3$ 四层。式 (5) 的优势是最低层 $R$ 本身已代数化。

为核对原式的阶界，式 (10)–(11) 给出
$$
t(1+68t^4)A''+(2+272t^4)A'+136t^3A=0.
\tag{14}
$$
所以 $A^2,AA',(A')^2$ 张成一个在微分下稳定的至多三维 $K(t)$-空间。$G'$ 属于 $K(t,s)$，再张量此二维代数函数空间，得到含 $H$ 且在微分下稳定的至多六维空间。因此 $H$ 为 D-finite，阶至多 $6$。这里的维数界是充分上界，不声称相应最小阶必取等号。

## 6. 其余对数层并非 D-finite

**引理。** 对每个整数 $j\ge1$，$R(t)L(t)^j$ 不是 D-finite。原式中的 $H(t)L(t)^j$ 也不是 D-finite。

**证明。** 在复均匀化 $E(\mathbb C)=\mathbb C/\Lambda$ 上，$t(z)$、$s(z)$ 及从 $K(E)$ 拉回的函数均为亚纯椭圆函数，且原点附近
$$
A(t(z))=\frac{z}{t(z)}.
\tag{15}
$$
假设所论函数满足某个非零线性微分方程。其最高阶系数的零点、各系数极点、$t$ 映射的分歧值及本计算中的其他例外点只构成 $t$ 球面上的有限集。取原点附近一个非例外基点，并在 $E$ 上选一条避开这些点的闭路，其不变微分积分为非零周期 $\omega$。可以如此选取，因为删掉有限个点不会杀掉 $E$ 的全部非零一维同调类。

沿此闭路反复延拓，在基点邻域内 $z$ 变成 $z+n\omega$，而所有代数椭圆函数回到原分支。因此 $RL^j$ 的延拓分支具有形式
$$
R(z)\left(\log\frac{z+n\omega}{t(z)}+c_n\right)^j,
\qquad n\in\mathbb Z_{\ge0},
\tag{16}
$$
其中 $c_n$ 只是可能的 $2\pi i$ 整数倍，不影响下述奇性计算。

这些分支在复数上任意有限组都线性无关。否则，除以公共的非零亚纯函数 $R(z)$，得到有限关系
$$
\sum_{n\in I}d_n\left(\log\frac{z+n\omega}{t(z)}+c_n\right)^j=0.
\tag{17}
$$
固定 $n\in I$，考察 $z=-n\omega$。$t(z)$ 在此有简单零点；恰好第 $n$ 项的分子也为零，因此该项的对数在此正则。其余每项的对数都具有形式 $-\log(z+n\omega)$ 加全纯函数。比较最高 $\log^j$ 项，得到
$$
\sum_{m\in I\setminus\{n\}}d_m=0.
$$
这对每个 $n\in I$ 成立；当 $|I|\ge2$ 时立即强制所有 $d_n=0$。单项关系也不可能。比较最高对数项可严格理解为绕该点的局部单值化差分作用 $j$ 次；全纯系数不变，最高项给出 $j!(2\pi i)^j$ 倍的对应系数。

但一个固定阶线性微分方程在普通基点处的解空间有限维，其所有解析延拓分支都位于该有限维空间中。这与式 (16) 的无限线性独立性矛盾。

对 $HL^j$，注意其通用覆盖上的形式为
$$
H(t(z))=B(z)z^2,
\qquad B(z)=\frac{G'(t(z))}{t(z)^2},
$$
其中 $B$ 是固定非零椭圆函数。因此分支变为
$$
B(z)(z+n\omega)^2
\left(\log\frac{z+n\omega}{t(z)}+c_n\right)^j.
$$
若有有限线性关系，除以 $B$ 后，在 $z=-n\omega$ 比较最高对数项，得到多项式恒等式
$$
\sum_{m\ne n}d_m(z+m\omega)^2=0.
$$
令 $P(z)=\sum_m d_m(z+m\omega)^2$，则对每个 $n$ 有 $P(z)=d_n(z+n\omega)^2$。两个不同的 $n$ 给出不同的二重根，所以只能 $P=0$、全部 $d_n=0$。同样得到无限维分支空间的矛盾。引理得证。

因此四个固定级数不能被整体宣称为 D-finite：最低层是，其他三层不是。这个性质并不否定它们模 $p$ 或模 $p^k$ 时可能出现的额外 Cartier 简化。

## 7. 秩 $2$ 的已知整除性在系数层的准确表现

对 good split $p$，R6 使用的 CLS 输入和已证秩 $2$ 给出
$$
a_{(p-3)/2}\in\mathfrak p^2.
$$
因为式 (6) 的 $u_p$ 为单位，故必有
$$
b_0(p)-p b_1(p)\in\mathfrak p^2.
\tag{18}
$$
这包含 $b_0(p)\in\mathfrak p$，但没有分别断言 $b_0(p)\in\mathfrak p^2$ 或 $b_1(p)\in\mathfrak p$。

若定义
$$
q_p=\frac{b_0(p)-p b_1(p)}{p^2}
+\frac{b_2(p)}2-\frac{p b_3(p)}6,
\tag{19}
$$
则 $q_p$ 在指定的 $\mathfrak p$ 处 integral，并且
$$
\frac{a_{(p-3)/2}}{u_pp^2}\equiv q_p\pmod{\mathfrak p^2}.
\tag{20}
$$
所以 R6 的充分条件等价于本式的 $q_p\not\equiv0\pmod{\mathfrak p^2}$。式 (18) 是每个素数处的对角系数同余，不是把 $R(t)$ 与 $L(t)$ 作全级数相等的恒等式。证明无穷多个 $p$ 满足式 (20) 的非零条件仍是新的算术任务。

这与 R13 无冲突：R13 排除特征 $0$ 的整条 $a_n$ 序列满足固定阶线性递推；式 (6) 只描述素数对角的有限 $p$-adic 精度，且显式保留三个非 D-finite 的对数层。不得由“四个固定级数”直接推断存在一个固定有限扩域，其 Frobenius 分类已控制该条件。
