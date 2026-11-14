# 非实 CM 加法差分：代数障碍、整分量与实际深度界

日期：2026-11-12。**状态：以下命题均已证明；最后的全体素数求和与共同逆像仍未解决。**

本篇把固定整数伸缩的乘法差分改为非实 CM 伸缩的**加法**差分。
这样可以在惰性处使用整个 $\mu_{p^2-1}$ 的整幂等元，并在普通处直接调整一个整常数。
它没有证明无穷多个素数上的初级有限性。

## 1. 固定方程与奇偶性

仍取
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
\mathfrak f=(34(1+i)).
$$
R19 的固定函数满足
$$
\Phi(O)=1,\qquad \Phi(-P)=\Phi(P)^{-1},\qquad
\ell:=\delta\log\Phi=2S\in K(E),\qquad \ell(O)=0.
\tag{1.1}
$$
$\ell$ 非零，其极点恰在 $\Phi$ 的固定零极点集合 $S_0$ 中；
这些点都是 $\mathfrak f$-division 点。这里 $S$ 是 R19 的有理函数，
$S_0$ 是点集，两者不混用。由奇偶性，$\ell(-P)=\ell(P)$，
所以在 $z=\log_E(t)$ 坐标中
$$
h(z):=\ell(\operatorname{Exp}_E z)
=\sum_{\substack{k\ge2\\k\text{ 偶}}}h_kz^k.
\tag{1.2}
$$

为避免与 R17 的 $\alpha=v/u$ 混淆，将本篇的固定 CM 伸缩记作
$$
b=35+34i=1+34(1+i),\qquad A=N_{K/\mathbb Q}(b)=2381.
\tag{1.3}
$$
于是 $[b]$ 固定 $S_0$ 中的每一点，$\deg[b]=A>1$，两个复嵌入下都有
$|b|=\sqrt A>1$。记 $\sigma_b f=f\circ[b]$。

对固定整数 $m\ge1$，存在唯一常数项为零的形式解
$$
(\sigma_b-1)^m f_m=\ell,
\qquad
f_m(\operatorname{Exp}_E z)
=\sum_{\substack{k\ge2\\k\text{ 偶}}}
\frac{h_k}{(b^k-1)^m}z^k.
\tag{1.4}
$$
这是因为 $b^k\ne1$ 对所有 $k\ge1$ 成立。其他正则形式解正好是
$f_m+c$，其中 $c$ 为常数。特别地，所有这些解在 $O$ 的一阶导数为零。

对于原先的整数乘法差分
$\mathcal D_a F=(F\circ[a])/F^a$，链式法则给出准确关系
$$
\delta\log(\mathcal D_a^mF)
=a^m(\sigma_a-1)^m\delta\log F.
\tag{1.5}
$$
本篇直接使用加法方程 (1.4)，没有对全局函数取一个非整数的 $b$ 次幂。

## 2. 加法的有限极点引理

**引理 2.1。** 设 $C$ 是代数闭特征零域上的光滑射影曲线，
$u:C\to C$ 为度数 $d>1$ 的有限 étale 态射。
若有限集合 $S\subset C$ 被 $u$ 双射地置换，而
$$
u^*g-cg
$$
的全部极点都在 $S$，其中 $g\in k(C)$、$c\in k^\times$，
则 $g$ 是常数。特别地，当 $c=1$ 时该差为零。

**证明。** 令 $Z$ 为 $g$ 在 $S$ 外的极点集。
若 $Q\in Z$、$P\in u^{-1}(Q)$，则 $P\notin S$。
$u^*g$ 在 $P$ 有极点；由于给定差在 $P$ 正则，$g$ 本身也必须在 $P$ 有极点。
于是 $u^{-1}(Z)\subset Z$，而 étale 性给
$d\#Z\le\#Z$，所以 $Z=\varnothing$。

若 $g$ 还有极点 $Q\in S$，则 $u^{-1}(Q)$ 中恰有一个点在 $S$，
故另有 $P\notin S$。在 $P$ 处，$g$ 正则而 $u^*g$ 有极点，
与差的极点限制矛盾。故 $g$ 无极点，从而为常数。证毕。

这一步使用的是**极点是否存在**，不把函数的差当成除子的差。

## 3. 代数形式解也不存在

**命题 3.1。** 方程 (1.4) 的任何形式解都不代数于 $\overline K(E)$。

**证明。** 令 $k=\overline K$。反设某个形式解 $f\in k[[t]]$ 代数。
在 $k((t))$ 中令
$$
L=k(E)(f,\sigma_bf,\ldots,\sigma_b^{m-1}f).
$$
这是 $k(E)$ 的有限扩张。方程最高一项的系数为一，所以
$\sigma_b^m f$ 属于 $L$，进而 $\sigma_bL\subset L$。
设 $d_0=[L:k(E)]$。由于 $\sigma_b$ 是注入，
$$
[\sigma_bL:\sigma_bk(E)]=d_0,
\qquad
[L:\sigma_bk(E)]=d_0A,
$$
故
$$
[L:\sigma_bL]=A.
\tag{3.1}
$$

令 $C$ 为函数域 $L$ 的光滑射影曲线。
两个域嵌入给出有限态射
$$
\pi:C\to E,\qquad u:C\to C,
\qquad \pi u=[b]\pi,\qquad \deg u=A.
\tag{3.2}
$$
$L\subset k((t))$ 的形式支点给出 $Q\in C$，位于 $O$ 上方。
因为 $t\in k(E)$ 在该赋值下的阶为一，这个支点的分歧指数为一。
替换 $t\mapsto[b](t)=bt+O(t^2)$ 保持每个非零 Laurent 级数的阶，
所以 $u(Q)=Q$。

Riemann–Hurwitz 对 $\pi$ 给 $g(C)\ge1$；对度数 $A>1$ 的自映射 $u$
给 $g(C)\le1$。故 $g(C)=1$，并且 $\pi,u$ 都 étale。
以 $Q$ 为原点，$C$ 是椭圆曲线，$\pi,u$ 是保持原点的同源。
不必预先假定 $C$ 带整个 $\mathbb Z[i]$ 的作用。

令 $B=\ker\pi$。它是有限群，且被 $u$ 稳定。
取足够大的 $N$，使 $u^N B=u^{2N}B$、$\ker(u^N|_B)=\ker(u^{2N}|_B)$，
并置
$$
B_0=\ker(u^N|_B).
$$
则 $u^NB_0=0$，且 $u$ 在 $B/B_0$ 上是双射。
这是有限群上一个自同态的稳定核、稳定像分解。

把 $k(C)$ 看成 $k$-向量空间，令 $V_0=k(C)^{B_0}$ 为平移 $B_0$ 不变的子空间。
$u^*$ 保持 $V_0$，而 $(u^*)^N$ 的像包含在 $V_0$ 中：
对 $P\in C,Q_0\in B_0$，有 $u^N(P+Q_0)=u^NP$。
所以 $u^*$ 在商空间 $k(C)/V_0$ 上幂零，$u^*-1$ 在该商上可逆，
其逆为有限几何级数。由于 $\pi^*\ell\in V_0$，方程
$$
(u^*-1)^m f=\pi^*\ell
$$
迫使 $f\in V_0$。

因此这次是**函数本身**下降到 $C_1=C/B_0$。
令其像为 $f_1$，诱导同源为 $u_1:C_1\to C_1$、$\pi_1:C_1\to E$。
$u_1$ 在 $\ker\pi_1$ 上双射，故它在
$$
S_1=\pi_1^{-1}(S_0)
$$
上也是双射：每个纤维中的一个原像可通过 $\ker\pi_1$ 中唯一的修正得到。
仍有 $\deg u_1=A>1$，并且
$$
(u_1^*-1)^m f_1=\pi_1^*\ell\ne0.
$$
对 $g=(u_1^*-1)^{m-1}f_1$ 使用引理 2.1。
右端的全部极点在 $S_1$，所以左端只能为零，矛盾。证毕。

## 4. 复解析输入：整个平面上的亚纯和

在任一复嵌入下，有准确的亚纯表达式
$$
\boxed{
\widetilde f_m(z)=
\sum_{n\ge0}\binom{m+n-1}{n}
h\!\left(\frac{z}{b^{m+n}}\right).}
\tag{4.1}
$$

**证明。** $h$ 在原点正则且为 $O(z^2)$。
对任意紧圆盘 $|z|\le R$，充分大的 $n$ 对应项全都正则，且其绝对值至多
$$
C_R\binom{m+n-1}{n}|b|^{-2(m+n)}.
$$
这个级数收敛；前面只有有限个亚纯项。
因此 (4.1) 在整个 $\mathbb C$ 上定义亚纯函数。
在原点展开并用
$$
\sum_{n\ge0}\binom{m+n-1}{n}b^{-(m+n)k}
=\frac1{(b^k-1)^m}
$$
便得到 (1.4)。证毕。

### 4.1 利用留数的另一完整非代数性证明

式 (4.1) 还给命题 3.1 一个不经过稳定覆盖的证明。
选 $s\in S_0$，令 $z_s\ne0$ 为 $s$ 的绝对值最小的复对数。
这个最小值存在，因为 $s$ 的复对数是一个格的陪集，且 $s\ne O$。
$\ell(z)\,dz=d\log\Phi(z)$ 在 $s$ 有非零留数 $r_s=\operatorname{ord}_s\Phi$。
令 $z_n=b^{m+n}z_s$，则 $\operatorname{Exp}_Ez_n=s$。

在 (4.1) 的第 $j\le n$ 项，内点为 $b^{n-j}z_s$，仍是 $s$ 的复对数，
故该项在 $z_n$ 的留数为
$\binom{m+j-1}{j}b^{m+j}r_s$。
若某个 $j>n$ 的项也有极点，设其内点对应 $u\in S_0$，则
$[b]^{j-n}u=s$。由于 $[b]$ 固定整个 $S_0$，只能有 $u=s$。
但 $z_s/b^{j-n}$ 是 $s$ 的一个绝对值更小的复对数，矛盾。
所以后面的项都正则，并且
$$
\operatorname{Res}_{z=z_n}\widetilde f_m(z)\,dz
=r_s b^m\sum_{j=0}^n\binom{m+j-1}{j}b^j.
\tag{4.2}
$$
把和除以 $\binom{m+n-1}{n}b^n$，令 $j=n-r$，由支配收敛得到极限
$\sum_{r\ge0}b^{-r}=b/(b-1)\ne0$。
因此这些留数的绝对值趋向无穷。

若原形式函数代数于 $\mathbb C(E)$，其某个非零多项式关系由解析恒等式
延拓到整个 (4.1)。在每个 $z_n$ 使用同一局部变量 $w=z-z_n$，
有 $\operatorname{Exp}_E(z_n+w)=s+\operatorname{Exp}_Ew$，
所以所有 Laurent 级数 $\widetilde f_m(z_n+w)$ 满足同一个
$\mathbb C((w))[Y]$ 中的非零多项式。
它只有有限多个根，因而这些 Laurent 级数的留数只能取有限多个值，
与 (4.2) 矛盾。加常数也不改变留数。证毕。

由此得到全平面上的解析映射
$z\mapsto(\operatorname{Exp}_Ez,\widetilde f_m(z))\in E\times\mathbb P^1$。
Bost–Chambert-Loir Proposition 5.15 对任意半径圆盘给典范切线半范数上界
$1/R$，令 $R\to\infty$，无穷处半范数为零。
若未来能证明整个固定图像 A-analytic，Theorem 6.1 会使其代数，
与命题 3.1 矛盾。这里缺的是全体有限处大小的求和，复解析输入已经满足。

## 5. 完整 tame 群上的非共振整性

令 $\mathcal O$ 为好素数处的局部整数环：普通处分量为 $\mathbb Z_p$，
惰性处为无分歧二次扩张的整数环。分别写 $q=p$ 或 $p^2$。
CM 形式群带 $\mathcal O$-作用。排除一个固定有限素数集，使
$b\in\mathcal O^\times$、$\ell(t)\in t^2\mathcal O[[t]]$。

在加法模 $V=t\mathcal O[[t]]$ 上，令 $I=(p,t)$。
若 $c\in1+p\mathcal O$，则 $[c](t)-t\in It$，逐项代入给
$$
(\sigma_c-1)(V\cap I^N)\subset V\cap I^{N+1}.
\tag{5.1}
$$
所以该算子对 $I$-进拓扑幂零。现在整个 $\Delta=\mu_{q-1}$ 都能使用：
$$
e_j=\frac1{q-1}\sum_{\zeta\in\Delta}\zeta^{-j}\sigma_\zeta
\quad(j\bmod q-1)
\tag{5.2}
$$
是加法 $\mathcal O$-模的整幂等元。
这与乘法单位的情形不同：此处没有取非 $\mathbb Z_p$ 标量的幂。

写 $b=\omega(b)\langle b\rangle$，令
$d_p=\operatorname{ord}_{\mathbb F_q^\times}(b)$。
在第 $j$ 块上，
$$
\sigma_b-1=(\omega(b)^j-1)+\omega(b)^j(\sigma_{\langle b\rangle}-1).
$$
当 $d_p\nmid j$ 时，常数项是单位，由 (5.1) 的几何级数得到整的双侧逆。
于是对固定解 (1.4)，
$$
\boxed{e_jf_m\in t\mathcal O[[t]]\quad(d_p\nmid j).}
\tag{5.3}
$$
比较时在 $z$ 坐标中逐系数使用唯一性；非共振块没有常数项。
由 (1.2)，所有奇数 $j$ 块本来就是零。因此剩下的共振权准确为
$$
k\equiv0\pmod{D_p},\qquad D_p=\operatorname{lcm}(d_p,2).
\tag{5.4}
$$

## 6. 普通目标块的常数规范不再造成障碍

这一节是条件命题，其条件正是原先中心阶数反设所能给出的局部输入。
取一个普通目标素数，采用 R20/R24 的单位塔、$\chi$ 块与
$T=\gamma-1$，其中 $\rho_E(\gamma)=1+p$。
假设原 $\Phi$ 的 $\chi$-Coleman 元素被 $(T-p)^m$ 整除。
再假设在所选嵌入 $K\hookrightarrow\mathbb Q_p$ 下
$$
c_p(b):=v_p(b^{d_p}-1)=1.
\tag{6.1}
$$
那么 $\sigma_b-b$ 与 $T-p$ 相差一个 Iwasawa 单位。
具体地，若 $r=\log\langle b\rangle/\log(1+p)$，则 $r\in\mathbb Z_p^\times$，
且该块上的算子为
$$
\omega(b)\bigl((1+T)^r-(1+p)^r\bigr).
$$
其除以 $T-p$ 的商在 $(p,T)$ 处为单位。

因此存在一个整 Coleman 单位 $u$，使局部的乘法模等式
$(\sigma_b-b)^m u=e_\chi\Phi$ 成立。
在此处 $b\in\mathbb Z_p$，这些 $p$-进幂有明确的局部意义。
链式法则和 tame 权重下降一给
$$
(\sigma_b-1)^m\bigl(b^m\delta\log u\bigr)=e_0\ell.
\tag{6.2}
$$
$b^m\delta\log u\in\mathbb Z_p[[t]]$。
它与 $e_0f_m$ 只差一个常数；这个常数是其在 $O$ 的整值。
直接减去该常数仍是整级数，所以
$$
\boxed{e_0f_m\in\mathbb Z_p[[t]]
\quad\text{在上述中心整除和 }c_p(b)=1\text{ 条件下}.}
\tag{6.3}
$$
不必再留一个中心因子来保证一次对数矩为零。
但 (6.3) 没有处理 $c_p(b)>1$ 时的额外圆分因子，
也没有处理 $d_p\mid j$、$j\ne0\pmod{p-1}$ 的其他共振块。

## 7. 惰性处真正的图像大小下界

以下赋值统一归一化为 $v_p(p)=1$。
设 $p$ 惰性、好约化，并排除上面的固定有限例外。
置
$$
q=p^2,\qquad d_p=\operatorname{ord}_{\mathbb F_{p^2}^\times}(b),\quad
D_p=\operatorname{lcm}(d_p,2),\quad c_p=v_p(b^{d_p}-1).
\tag{7.1}
$$
有 $c_p\ge1$，且 $p\nmid D_p$。提升指数公式给全部非零分母的准确赋值：
$$
v_p(b^k-1)=
\begin{cases}
0,&d_p\nmid k,\\
c_p+v_p(k/d_p),&d_p\mid k.
\end{cases}
\tag{7.2}
$$

### 7.1 高度二的系数估计

使用 CLS 的严格 Lubin–Tate 坐标，形式群与
$[\varpi](X)=\varpi X+X^q$ 对应的群整严格同构，其中 $v_p(\varpi)=1$。
若其对数为 $L(X)=\sum l_nX^n$，则
$$
v_p(l_n)\ge-\frac{n-1}{q-1}.
\tag{7.3}
$$
为完整证明这一界，将
$L(\varpi X+X^q)=\varpi L(X)$ 比较 $X^n$ 系数。
$n\ge2$ 时左边的 $l_n$ 项除数为 $\varpi^n-\varpi$，赋值一。
其他项来自 $j<n$、$r\ge1$、$n=j+(q-1)r$，其除后赋值至少
$$
-\frac{j-1}{q-1}+j-r-1
\ge-\frac{n-1}{q-1}.
$$
从 $l_1=1$ 归纳即得 (7.3)。
将变量缩放为 $v_p(\rho)=1/(q-1)$ 后，$\rho^{-1}L(\rho X)$ 是线性项为一的整级数，
故其复合逆也整。严格整坐标变换保持这个界，因此
$$
v_p([z^n]\operatorname{Exp}_Ez),\quad
v_p([t^n]\log_Et)\ge-\frac{n-1}{q-1}.
\tag{7.4}
$$
由于 $\ell(t)\in t^2\mathcal O[[t]]$，(1.2) 的系数满足
$$
v_p(h_k)\ge-\frac{k-2}{q-1}.
\tag{7.5}
$$

### 7.2 从系数到图像大小

定义
$$
s_p=\frac1{p^2-1}+\frac{m c_p}{D_p-1}.
\tag{7.6}
$$
则 $f_m(t)=\sum a_kt^k$ 的全部系数满足
$$
\boxed{v_p(a_k)\ge-s_p(k-1)\quad(k\ge1).}
\tag{7.7}
$$

**证明。** 先在 $z$ 坐标证明。
非共振偶权只用 (7.5)。共振权为 $k=D_pn$，而
$$
c_p+v_p(n)\le c_pn
\le\frac{c_p(k-1)}{D_p-1}.
$$
结合 (7.2)、(7.5) 就得到所需界。
取 $v_p(\rho)=s_p$，则 $f_m(\operatorname{Exp}_E(\rho z))/\rho$ 整。
又因 $s_p\ge1/(q-1)$，$\log_E(\rho t)/\rho$ 为整级数，
复合后得到 $f_m(\rho t)/\rho$ 整，即 (7.7)。证毕。

故在半径 $p^{-s_p}$ 的二维圆盘上，
$$
(t,y)\longmapsto(t,y-f_m(t))
$$
是保持该圆盘的解析坐标变换，其逆也保持圆盘，且在原点的微分为恒等。
它把图像直化。按 Bost–Chambert-Loir 的大小定义，得到真正的图像大小下界
$$
\boxed{S_p(\widehat{\operatorname{graph}}f_m)\ge
p^{-\frac1{p^2-1}-\frac{m c_p}{D_p-1}}.}
\tag{7.8}
$$
这里使用 $|p|_p=p^{-1}$；若采用 $K$ 的乘积公式归一化，惰性处的对数损失乘以二。
式 (7.8) 不只是收敛半径的估计。

## 8. Stewart 的统一界确实控制这里的深度

**命题 8.1。** 对所有充分大的惰性 $p$，有
$$
\boxed{c_p\le v_p(A^{p-1}-1)
<p\exp\!\left(-\frac{\log p}{52\log\log p}\right)\log A.}
\tag{8.1}
$$

**证明。** 因为 $d_p\mid p^2-1$ 且 $p\nmid(p^2-1)/d_p$，
式 (7.2) 给
$v_p(b^{p^2-1}-1)=c_p$。
惰性处只有一个 $K$ 的素位，复共轭保持其赋值，所以
$v_p(\bar b^{p^2-1}-1)=c_p$。
相乘得 $v_p(A^{p^2-1}-1)\ge c_p$。
再对整数 $A$ 使用提升指数公式，因 $p+1$ 为单位，得到
$$
v_p(A^{p^2-1}-1)=v_p(A^{p-1}-1).
$$

Stewart 的出版原文 Theorem 1.2，p.295，式 (1.9) 证明：
固定整数 $a>b_0>0$，若 $p\nmid ab_0$ 大于一个仅依赖
$\omega(ab_0)$ 的可有效计算阈值，则对 $n>2$，
$$
v_p(a^n-b_0^n)
<p\exp\!\left(-\frac{\log p}{52\log\log p}\right)\log a+v_p(n).
$$
取 $a=A,b_0=1,n=p-1$ 即得 (8.1)。证毕。

这是固定次数、固定底数的已出版估计，没有让常数依赖变化的除法域。
它与此前字符投影的 Gaudron 界是不同对象；不能直接把 (8.1) 套到
$G_p(0)$、$G_p'(0)$ 或 R31 的高阶 jet 上。

**推论 8.2。** 固定 $0\le\theta<1$、$c>0$。在满足
$$
D_p\ge c p^2
\exp\!\left(-\frac{\theta\log p}{52\log\log p}\right)
\tag{8.2}
$$
的任意惰性素数集合上，式 (7.8) 给出的全部对数损失之和收敛。

**证明。** 高度二项 $\sum_p\log p/(p^2-1)$ 收敛。
另一项由 (8.1)–(8.2) 至多为固定常数倍的
$$
\sum_p\frac{\log p}{p}
\exp\!\left(-\frac{(1-\theta)\log p}{52\log\log p}\right).
$$
指数因子最终小于 $(\log p)^{-3}$，故可用
$\sum_{n\ge3}1/(n(\log n)^2)<\infty$ 比较。
有限个小素数的损失有限。证毕。

特别地，$D_p\ge c p^2$ 的任意子集已经无条件可控，不需要先假设
这些素数为非 Wieferich。

## 9. 目前还没有控制的量词

未证明满足 (8.2) 的惰性素数之外，其额外损失可求和。
真正剩余的对象可以准确写为
$$
\sum_{\substack{p\ \mathrm{inert}\\p\ \mathrm{outside\ a\ fixed\ finite\ set}}}
\frac{c_p\log p}{D_p-1}.
\tag{9.1}
$$
本篇给的是足以控制图像的上界；没有断言 (9.1) 发散就必使图像不 A-analytic，
因为原分子 $h_k$ 仍可能消去分母。

已经逐项核对的阶数文献给下列边界：

- Gras，*On the order modulo $p$ of an algebraic number*，JTNB **30** (2018)，
  Theorem 2.1 排除某些多项式因子，Theorem 4.1 给对数级的确定性下界。
  其 §5.1 明确先固定 $p$ 并让代数数模 $p$ 变化；Theorem 6.1 的概率模型
  和 Conjecture 8.1 不能当成固定 $b$ 的素数计数定理。
- Cohen，*Primitive Roots in Quadratic Fields II*，原文 Theorem 1.1 的结论是
  满足三项乘法独立性/非平方条件的 $85$ 个候选中，至少一项对无穷多个惰性 $p$
  有阶数至少 $(p^2-1)/24$。即使使用该结论并结合推论 8.2，它也只处理一个
  无穷子集，不处理所有剩余惰性位。本文不依赖该稿证明任何主结论。
- Fellini–Murty 的出版论文最终稿 Theorem 1.3/7.1 假设固定底数的
  super-Wieferich 素理想（深度至少三）只有有限多个，才推出无穷多个深度一的素理想；
  Theorem 1.2 则使用数域 $abc$。这不是可直接引用的无条件深度门槛。

此外，普通处尚有两类没有消去的块：其他 tame 共振块，以及
$c_p(b)>1$ 时的额外圆分因子。不能由 (6.3) 推出整张图像在普通处整。

选择几个不同的 $b$ 并分别构造 $f_{m,b}$，也不能直接相加局部好集合：
这些通常是不同的固定形式函数。后续若走多差分路线，须先对**同一个**形式函数
建立相容的多个方程，再证明其局部大小受共同共振控制。

## 来源与本篇依赖

- R19、R22、R28：固定 $\Phi$ 的零极点、对数导数、原乘法差分及其稳定覆盖方法。
- J. Coates、Z. Liang、R. Sujatha，*The Tate-Shafarevich group
  for elliptic curves with complex multiplication II*（2010），§2，式 (29)–(30)：
  惰性处严格 Lubin–Tate 坐标；[原文](https://arxiv.org/abs/1005.4206)。
  本篇所需的系数界另在 §7.1 完整证明。
- J.-B. Bost、A. Chambert-Loir，*Analytic curves in algebraic varieties over number fields*，
  §3 的大小、Definition 3.7、Proposition 5.15、Theorem 6.1；
  [原文](https://arxiv.org/abs/math/0702593)。
- C. L. Stewart，*On divisors of Lucas and Lehmer numbers*，Acta Math. **211**
  (2013)，291–314，Theorem 1.2，p.295，式 (1.9)；
  [作者保存的出版原文](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s11511-013-0105-y.pdf)，
  [DOI](https://doi.org/10.1007/s11511-013-0105-y)。已独立读取准确条件和结论。
- G. Gras，*On the order modulo $p$ of an algebraic number*，JTNB **30** (2018)，307–329；
  [出版原文](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1027.pdf)。
- J. Cohen，*Primitive Roots in Quadratic Fields II*，Theorem 1.1；
  [所核原文](https://arxiv.org/abs/math/0501120)。仅作范围核查，不作为本篇证明输入。
- N. Fellini、M. R. Murty，*Wieferich primes in number fields and the conjectures of
  Ankeny–Artin–Chowla and Mordell*，JNT **285** (2026)，209–229；
  [最终稿](https://arxiv.org/abs/2508.08472v2)，
  [出版 DOI](https://doi.org/10.1016/j.jnt.2026.01.002)。

未下载保存或上传 PDF，未渲染页面；本篇只含可复核的文本证明和来源链接。
