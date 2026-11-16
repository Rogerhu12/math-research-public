# R528：正交副本库在无极点常态区间上的严格二次障碍

日期：2026-11-16。**原式纸证；没有执行 profile 求积、符号程序、数值试验、秩计算或开发检查。**

本文固定 [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md) 的同一个有限正副本库。它给出一个具体实现限制：在下述无极点常态上，完整第四 ruling 的时间二次系数是严格负的 $\sin^2\theta$ 倍数。因此这份库不能在该状态运行任何正长度的常 scalar 区间；改变固定第二、第三规范或改变真正入历史均不能消去该系数。

无极点条件是证明的一部分。特别，结论覆盖所有合法的 $k=0$ 常态；本文不将它扩成全部合法 $k>0$ 状态，也不排除非恒偶端 germs 或原完整反馈的有限幅值返回轨道。

## 1. 固定库、真实常段和坐标范围

沿用 R521 的 profiles、完整基本块、右锚和共同区间 $I$。它们由十六元群
$$
\mathcal G=\{R_{j\pi/4},R_{j\pi/4}S:0\le j\le7\},
\qquad S=\operatorname{diag}(1,-1),
\tag{1}
$$
以及十一组共同正平移矩构成。实际块的位置全部不同；虚拟参考节点只用于 R521(14)(17) 的准确多项式读出。

在一个真实开时间区间令
$$
S_c=(h,k,\omega),\qquad h>0
\tag{2}
$$
为常数，所有 profile 坐标仍为原 $x$，并记
$$
z=x+\omega,\qquad e=hz-k.
$$
除了原物理窗口的 $z>0$，本稿明确要求
$$
\boxed{1-ke(x)\ne0\quad\text{在整个共同区间 }I\text{ 上}.}
\tag{3}
$$
这里的 $I$ 同时包含所有实际块、虚拟参考块及其所用 collars；不是只在若干 packet 中心检查(3)。紧性使该分母在 $I$ 上一致远离零。

若 $k=0$，(3)恒成立；在 R521 的 $e>0$ 域中，$k<0$ 时它也自动成立。对 $k>0$ 则须保留这条额外条件。若其零点落入原包络，R54 的紧 profile 迁移及其边界积分不能照搬；本文不通过极限或删去该点来扩大范围。

令时间坐标 $\sigma=s-s_0$。入值可以是同一真实全词给出的任意 $A_*,T_*$，固定规范可以是任意已合法的 $w_\theta,\chi_\theta$。整个区间不能随 $\sigma$ 重新选它们。

## 2. 完整原式的二次系数不读入历史或固定规范

记
$$
A_c=\Phi_{M_{\rm raw}(S_c,0,0)}.
$$
由 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(12)(16)(17)，
$$
A(\sigma)=A_*+\sigma A_c.
\tag{4}
$$
在常态，原局部 second 场的分子只有 $N$ 分量；$Y$ 的分子在 $T,B$ 平面，$\nabla_sY$ 在 $N$ 方向，而局部 second 场的协变导数在 $T,B$ 平面。因此其原点积 $T_\xi,T_s,\mathcal J$ 均按所需 mixed 配对为零。同时 R73(15) 的变化-profile 配对 $\Psi_s$ 在零速度时为零。原局部第三密度由此准确给 $\mathcal C_s=0$，而非仅取模某个第三空间。

于是完整有序第三累计为
$$
T(\sigma)=T_*-\sigma A_c\circ A_*-\frac{\sigma^2}{2}A_c\circ A_c.
\tag{5}
$$
复合保持原次序
$(B\circ C)(a;b,c)=B\{a,C(b,c)\}$。

使用 [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) **未消第三历史**的(23)(24)，
$$
q=A D_\theta+w_\theta,\qquad
b=-2T(\phi_\theta;D_\theta)
+2A(\phi_\theta,w_\theta)-\chi_\theta,
$$
$$
\mathscr K=\mathcal R+\mathcal L(q)-\mathcal E_c(q,q)
+2\mathcal E_c(\phi_\theta,b).
\tag{6}
$$
在常态 $\mathcal R$ 固定，速度线性项 $\mathcal L$ 为零。由(4)(5)，整个式子是 $\sigma$ 的至多二次多项式，其二次系数准确为
$$
\boxed{
\mathcal Q_c(\theta)
=-\mathcal E_c(A_cD_\theta,A_cD_\theta)
+2\mathcal E_c\{\phi_\theta,A_c(\phi_\theta,A_cD_\theta)\}.
}
\tag{7}
$$
它不含 $A_*,T_*,w_\theta,\chi_\theta$。这一推导不需要 R480 的第三 outer 矩，也没有删除 R521 中仍存在的 $YC$ 或第三累计。

因此若某个正长度常态区间的完整 $\mathscr K(s,\theta)$ 恒为零，必有 $\mathcal Q_c(\theta)\equiv0$。本稿下面直接证明当前库不满足这项必要条件。

## 3. 同一真实 profile 的标准螺旋面迁移

为避免和原 $x$ 混淆，用 $\xi$ 表示标准螺旋面的 profile 坐标。按 [R54](R54-constant-state-helicoid-transfer-and-first-ruling-gauge.md)(1)–(3)，置
$$
a=\sqrt{1+k^2},\qquad H=h^2/a^2,
$$
$$
\xi=\frac{e+k}{1-ke},\qquad
x=\frac{a^2\xi}{h(1+k\xi)}-\omega.
\tag{8}
$$
一个原实微包 $u_i$ 迁移为
$$
\psi_i(\xi)=\frac{(1+k\xi)^2}{a}
u_i\!\left(\frac{a^2\xi}{h(1+k\xi)}-\omega\right).
\tag{9}
$$
由(3)，这一变换在整个原包络上为光滑单射；原紧微包变成真实紧微包，非零性和彼此支撑分离均保留。

变换对 profile 实线性，所以原微包上的系数向量 $(a_i,b_i)$ 及其正交旋转没有被重新选择。记 $\rho_i^2=a_i^2+b_i^2>0$。

每个 R521 完整基本块本来已有三矩圆。R54 §3 因而保证迁移后的复 profile $q=F+iG$ 满足标准的完整复能量尾零，足够使用其 §4 的真实局部化。这里不声称迁移后的另外两个标准矩也各自为零；也不把个体实微包的左原函数尾改成零。

原时间为 $\sigma$，标准时间为 $a\sigma$，物理缩放为 $H$。R54 §3 的准确尺度给
$$
\mathcal Q_c^{\rm orig}=h^2\mathcal Q^{\rm standard}.
\tag{10}
$$
该因子严格正。

## 4. 每个实微包的两个严格正数

对标准实紧 profile $\psi$，令
$$
Q_0=1+\xi^2,\qquad p=\psi',\qquad r=\psi'',
$$
$$
L_\psi=\xi Q_0r^2-2Q_0pr,\qquad
R_\psi''=\frac14(\xi r-p)(\xi r-p+Q_0\psi''').
$$
采用 R54(5) 的原定义
$$
e_\psi=\frac14\int Q_0(R_\psi'')^2+
\frac1{128}\int\{L_\psi^2+2Q_0^2p^2r^2+4Q_0p^4\},
$$
$$
s_\psi=e_\psi+2t_\psi.
\tag{11}
$$
$t_\psi$ 是原完整 third/self 配对；不在此赋予符号。

第一式给 $e_\psi>0$：非零紧 $\psi$ 不可能有 $p\equiv0$，而最后一项为严格正的积分。另一方面，[R50](R50-disjoint-profile-circle-fourth-order-positive-obstruction.md) 的完整平方身份给
$$
s_\psi=\frac1{128}\int \mathcal Q(\xi,\psi,p,r)>0,
\tag{12}
$$
其中
$$
\begin{aligned}
\mathcal Q={}&
2Q_0r^2\left[
\left(\psi-\xi p+\frac{\xi^2-1}{6}r\right)^2+
\left(p-\frac{\xi r}{3}\right)^2\right]\\
&+\frac{Q_0^3r^4}{36}
+4p^2\left(\psi-\frac{\xi p}{3}\right)^2
+\frac{2(\xi^2+3)}9p^4 .
\end{aligned}
\tag{13}
$$
全部平方均为实平方。对非零紧 $\psi$，例如末项已经使(12)严格。

R54 §4 的推导完整保留真复尾，先利用整个块的复能量尾零作 IBP，再得到以下逐微包式。本文不对一个未经配平的实微包单独宣称其原 second 场左紧。

## 5. 有限正交平均的二次系数严格为负

对标准块写
$$
q=\sum_i\alpha_i\psi_i,\qquad
|\alpha_i|=\rho_i,\qquad
z_i=\alpha_i^2/|\alpha_i|^2.
$$
R54(6)(7)及 [R53](R53-overlapping-profile-fourth-leading-gate-existence.md)(2)(3)给
$$
\mathcal F(q)=\sum_i\rho_i^4z_i^2s_i,
$$
$$
4K_2(q)=\sum_i\rho_i^4
\{(z_i^2+1)s_i-(z_i+1)^2t_i\},
\qquad K_4=-\mathcal F/8,
\tag{14}
$$
$$
\mathcal Q^{\rm standard}(\theta)
=-\operatorname{Re}(K_2+K_4)
+\operatorname{Re}(e^{-2i\theta}K_2+e^{-4i\theta}K_4).
\tag{15}
$$
这里 $s_i=s_{\psi_i}$、$e_i=e_{\psi_i}$，$t_i=(s_i-e_i)/2$。

对(1)的有限群取平均。每个微包的真实系数向量随同一个正交矩阵旋转或反射，$\rho_i$ 保持；八个旋转已经准确给
$$
\operatorname{Av}_{\mathcal G}z_i=0,\qquad
\operatorname{Av}_{\mathcal G}z_i^2=0.
$$
故
$$
\operatorname{Av}_{\mathcal G}K_4=0,\qquad
\operatorname{Av}_{\mathcal G}K_2
=\frac14\sum_i\rho_i^4(s_i-t_i)
=\frac18\sum_i\rho_i^4(e_i+s_i)>0.
\tag{16}
$$
将(16)代入(15)，得到完整式
$$
\boxed{
\operatorname{Av}_{\mathcal G}
\mathcal Q^{\rm standard}(\theta)
=-\frac14\sum_i\rho_i^4(e_i+s_i)\sin^2\theta.
}
\tag{17}
$$

最后还须回到真实不同位置。R521(12)–(17)已付整个 fourth ruling 的共同位置次数至多十，且正权节点的0…10矩完全相同。因此可先对每一个固定群元素和每一个真实 $\sigma,\theta$ 使用该原多项式身份，再提取 $\sigma^2$ 系数。这个次序只消费已经证明的恒等式，不对迁移后的 $e_i,s_i$ 另猜位置次数。

设 $c_j,w_j>0$ 是 R521 的十一参考节点和正权，$\psi_{i,j}$ 是该参考位置的真实微包经(9)迁移后的 profile。由(10)(17)，最终实际库的二次系数为
$$
\boxed{
\mathcal Q_c(\theta)=-\Lambda_c\sin^2\theta,\qquad
\Lambda_c=
\frac{|\mathcal G|h^2}{4}
\sum_{j=0}^{10}w_j\sum_i\rho_i^4
(e_{\psi_{i,j}}+s_{\psi_{i,j}})>0.
}
\tag{18}
$$
若第一圆在 R521 最后整体作过一次正幅归一，(18)同时乘该正幅的四次幂，严格号不变。

所有权重和 profile 均来自同一实际库。正参考和不交实际副本之间的替换仅由原有限矩恒等式负责，没有使用带符号路径、无限平均或虚构的重叠字段。

## 6. 结论及对真实返回构造的准确影响

**定理。** 固定 R521 的实际正交副本库。在满足(3)的合法常态上，无论真实第二、第三入值和已合法固定 $w,\chi$ 为何，都不存在正长度的常 scalar 区间使完整第四 ruling 对所有 $s,\theta$ 恒为零。

证明：完整 ruling 对真实时间是二次多项式。若它在一个开区间恒为零，则二次系数必须为零；但(18)在任意非 seed 相位严格为负。证毕。

在一个预先固定的紧常态集合上，若 $h,z,|1-ke|$ 都有共同正下界且同一库/窗口保持，则(18)连续且严格为正，因而 $\inf\Lambda_c>0$。这只是同一合法坐标域中的紧性结论，不是计算所得数值界。

对 [R526](R526-real-incoming-history-reversal-and-one-gauge-endpoint-completion.md) 的用途应分清：

- 开常态 germ 只是反射拼接的一个形式上充分条件；本定理证明它在当前库的上述状态域中不能由 $K=0$ 实际段实现。
- 非恒偶 germs 不含正长度常态区间，不受本定理排除。仅端点速度为零，也不触发本定理。
- 本稿没有得到实际矩阵零块，也没有排除所有非恒 $M=0$ 块。原八矩、全第三历史、frame/位置和完整第四 period 仍须同一词内处理。
- R70 的常态矩阵控制段不能仅凭其末矩阵可控性移入当前受约束库。相反，R520 采用另一份从起点改造的母库，它的常态结果不与本定理冲突。
- 若(3)失败，不能把标准紧 profile 的平方积分强行用于 Möbius 无穷远；该情形不在本文结论内。

下一实际构造因此须从真正非恒的、反射匹配的端 germs 出发，并继续解同一个完整反馈系统的矩阵返回。本文没有以这一局部实现限制代替全局返回问题。
