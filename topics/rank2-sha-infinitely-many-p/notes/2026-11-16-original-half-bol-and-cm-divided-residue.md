# 原半长算子的对称幂、两符号分解与 CM 点除 p 留数

日期：2026-11-16。**本注证明同一原半长算子的完整模 p 正规式、实际两符号核，以及保留 Hasse 缺陷的特征零除 p 留数公式。四个指定留数与修正项不同时相消仍未证明。**

只用已付的[原 GM 矩阵](2026-11-16-original-gauss-manin-half-density-p-curvature-and-hurwitz-interface.md)、[R856 的整 Hasse 缺陷](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)及[四个同纤维水平函数](2026-11-16-algebraic-horizontal-theta-frame-and-original-divided-rows.md)。本注的局部化及随 p 的 Hasse 坐标不替换原四函数、物理 jets 或任何中央输入。

## 1. 原正规和所读的同一半长行

保持原 $p=6s-1>211$，固定非零判别式参数曲线、其导子和微分
$$
D=L_2,\qquad a=g_2/12,\qquad
\omega(D)=1,\qquad
n=(p-1)/2,\quad N=n+1=(p+1)/2.
\tag{1}
$$
这里 $\omega$ 是参数曲线的微分，不是另添物理 $z$ 来源。
令 $H=H_p$ 是 R856 的指定特征零 Hasse 多项式，$C=DH$，并取其实际整缺陷
$$
R=(D^2H+aH)/p.
\tag{2}
$$
以下所有除 $p$ 都使用这些固定提升。

原标量算子仍为
$$
T_0=1,\quad T_1=D,\qquad
T_{r+1}=DT_r-\frac{r(2r-1)}2aT_{r-1}.
\tag{3}
$$
在同一个先于 $p$ 固定的代数覆盖上，四个函数 $f_\nu=f_\nu^{\rm flat}$
满足
$$
f_\nu(P)=Df_\nu(P)=D^2f_\nu(P)=0,\qquad
D^3f_\nu(P)=90/m_\nu^3,
$$
$$
m_\nu=34,72,136,66,\qquad P=(0,-4b),
\tag{4}
$$
并保留原纤维的所有物理 jets。所求首行准确为
$$
\mathfrak B_{\nu,p}
=(2m_\nu)^N\,\frac{(T_Nf_\nu)(P)}p\bmod p.
\tag{5}
$$
原 $f_\nu$ 不因本注的 $n,N,H$ 而改变。

## 2. 半长 T_N 是同一 GM 方程的对称幂算子

对任意非负整数 $n$，定义
$$
U^{(n)}_0=1,\quad U^{(n)}_1=D,\qquad
U^{(n)}_{r+1}
=DU^{(n)}_r+r(n-r+1)aU^{(n)}_{r-1}.
\tag{6}
$$
若 $D^2\ell+a\ell=0$，则对
$y_r=(n)_r\ell^{n-r}(D\ell)^r$ 有
$$
Dy_r=y_{r+1}-r(n-r+1)a\,y_{r-1}.
$$
所以 $y_r=U^{(n)}_r(\ell^n)$，且
$U^{(n)}_{n+1}(\ell^n)=0$。对两个独立周期解作
$(\ell_0+t\ell_1)^n$，比较 $t$ 系数，得到同一算子恰杀掉
全部 $\operatorname{Sym}^n$ 解，而非只一条周期线。

当 $n=(p-1)/2$ 时
$$
r(n-r+1)\equiv-r(2r-1)/2\pmod p.
$$
因此在整个参数函数域上，作为微分算子有
$$
\boxed{T_N=U^{(n)}_N\pmod p.}
\tag{7}
$$
该等式保完整低阶系数，不只保首项 $D^N$。

若 $h\ne0$ 且 $D^2h+ah=0$，置 $\delta_h=h^2D$。
取形式变量 $t$ 满足 $Dt=h^{-2}$，则
$h^n, h^nt,\ldots,h^nt^n$ 是(6)的完整解基。单首算子比较给
$$
\boxed{
U^{(n)}_{n+1}
=h^{-n-2}(h^2D)^{n+1}h^{-n}.
}
\tag{8}
$$
右边最高阶系数为1，且杀掉上述 $n+1$ 个解。
Wronskian 中只用 $0!,\ldots,n!$，故 $n<p$ 时同样成立。
也可由(6)逐次消元直接核定(8)，不需作任何未经说明的周期代数化。

模 $p$ 取 $h=H$，由(2)得到
$$
\boxed{
T_N=H^{-n-2}\delta^N H^{-n},\qquad \delta=H^2D
}
\tag{9}
$$
于 $H\ne0$ 的函数域。左边本来正规；在 $H=0$ 处必须把右边完整合并，不能逐因子取值。

## 3. 原绝对 GM 常数给准确的半长谱

令 $F$ 是原参数覆盖的一个约化函数域，常数域取完美域。
已付的同一原规范给 $D^p=0$，以及周期方程的
$$
P_p=\begin{pmatrix}HC&-H^2\\C^2&-HC\end{pmatrix}.
\tag{10}
$$
由此可自含读出
$$
\boxed{D^{p-1}(H^{-2})=-1.}
\tag{11}
$$
证明：在微分扩张 $F[t]$ 上规定 $Dt=H^{-2}$。
向量 $(Ht,Ct+H^{-1})$ 是同一周期系统的解。
(10)作用于其第一行恰得 $-H$。
另一方面 $D^p$ 是导子且在 $F$ 上为零，所以
$D^p(Ht)=H D^pt$。于是 $D^pt=-1$，正是(11)。

对任意非零一元导子 $D$，若 $D^p=0$，则标准一元 restricted 恒等式为
$$
(fD)^p=-f^pD^{p-1}(f^{-1})(fD).
\tag{12}
$$
这里给出所需规范的核准。可取 $u\in F$ 使 $Du=1$：
$F/F^p$ 的次数为 $p$，$\ker D=F^p$，故 $D$ 是一个长度 $p$ 的幂零块。
对 $\alpha=du/f$，Cartier 的系数定义给
$\mathcal C\alpha=(-D^{p-1}f^{-1})^{1/p}du$。
若 $\partial^p=A\partial$ 且 $\beta(\partial)=1$，则
$\mathcal C\beta=A^{1/p}\beta$：
$A=0$ 时取 $\partial$ 的加性坐标；$A\ne0$ 时扩常数取
$\lambda^{p-1}=A$，由一个非零特征函数 $z$ 写
$\beta=dz/(\lambda z)$。这个计算给(12)的准确负号。
它也可由 Bell 恒等式逐系数得出。

令 $f=H^2$，结合(11)–(12)，得到
$$
\boxed{\delta^p=H^{2p}\delta.}
\tag{13}
$$
这里 $H^p$ 是 $\delta$ 的常数。于是
$$
S=H^{-p}\delta^n,\qquad
S^3=S,
\tag{14}
$$
并有完整投影
$$
\boxed{
\Pi_0=1-S^2,\qquad
\Pi_+=(S^2+S)/2,\qquad
\Pi_-=(S^2-S)/2.
}
\tag{15}
$$
它们是 $F^p$-线性、两两正交、和为1；
$\operatorname{im}\Pi_0=F^p$，另外两个像各维 $n$。
维数证明不假设根已经在常数域：先作有限可分常数扩张，使
$\lambda^n=H^p$。此时 $\delta$ 的可能特征值为
$i\lambda$，$i\in\mathbf F_p$，且其可对角化。$\delta\ne0$，
故存在属于非零特征值的特征函数；它的
$0,\ldots,p-1$ 次幂给全部 $p$ 条不同特征线，故每个特征值各一次。
$S$ 在它们上分别读 $0$、二次剩余的 $+1$、非剩余的 $-1$；
投影及维数下降回原域。

设 $B=HD+C/2$、$\epsilon=\pm1$。在模 $p$ 下
$$
B(H^ng)=H^{n-1}\delta g
$$
因为 $n+1/2=0$。由(9)遂有
$$
\boxed{
(T_N-\epsilon B)f
=H^{-n-2}\delta(\delta^n-\epsilon H^p)(H^{-n}f).
}
\tag{16}
$$
因此
$$
\boxed{
\ker(T_N-\epsilon B)
=H^n\big(F^p\oplus\operatorname{im}\Pi_\epsilon\big),\qquad
\ker(T_N-B)\cap\ker(T_N+B)=H^nF^p.
}
\tag{17}
$$
两个核各维 $N$，其和为整个 $F$。

原水平 theta 的 R856 身份准确给
$$
(T_N-\epsilon_\nu B)f_\nu=0\pmod p,\qquad
(\epsilon_S,\epsilon_T,\epsilon_U,\epsilon_V)
=(\chi_{17},1,\chi_{17},\chi_{33}).
\tag{18}
$$
所以原四函数进入(17)各自的真实符号部分。
它们都不是公共的 $H^nF^p$ 线：在原 $P$ 上
$\operatorname{ord}(H^{-n}f_\nu)=3-n$，介于 $-p$ 与0且不为0，
不可能是 $p$ 次幂的阶。故每一 $\Pi_{\epsilon_\nu}$ 份额确非零。
这是同一已知模 $p$ 核的精确分解，**不**把该非零份额当成(5)的除 $p$ 非零。

## 4. 特征零提升：保留实际 Hasse 缺陷

不能把(9)、(13)直接除 $p$。在特征零的 $H\ne0$ 环中置
$$
a_H=-D^2H/H=a-pR/H.
\tag{19}
$$
把(6)里的 $a$ 换成 $a_H$，所得算子记为 $G_r$：
$$
G_0=1,\quad G_1=D,\qquad
G_{r+1}=DG_r+r(n-r+1)a_HG_{r-1}.
\tag{20}
$$
现在 $H$ 是这个实际变形方程的精确解，所以
$$
\boxed{G_N=H^{-n-2}(H^2D)^NH^{-n}}
\tag{21}
$$
是特征零恒等式。

定义 $V_r=(G_r-T_r)/p$，并置
$$
A_r=-r(2r-1)a/2,\qquad
b_r=r a/2-r(n-r+1)R/H.
$$
直接由(3)、(19)–(20)得到完整整递推
$$
\boxed{
V_0=V_1=0,\qquad
V_{r+1}=DV_r+A_rV_{r-1}+b_rG_{r-1}.
}
\tag{22}
$$
右边都在局部化整环中，故 $V_r$ 确实整。
约化后可将最后的 $G_{r-1}$ 换成 $T_{r-1}$，但须保留
$$
b_r\bmod p
=\frac r2a+\frac{r(2r-1)}2\,R/H.
\tag{23}
$$
这不是只对整数 $n$ 微分的形式修正；原 $R/H$ 是(2)指定的 Hasse 缺陷，不能删。

特征零的 $B$ 还多一个准确项：
$$
B(H^ng)=H^{n-1}\delta g+\frac p2 C H^ng.
$$
因此同一个原
$\mathcal Q_{p,\epsilon}=(T_N-\epsilon B)/p$ 满足
$$
\boxed{
\mathcal Q_{p,\epsilon}
=H^{-n-2}\frac{\delta^N-\epsilon H^p\delta}{p}H^{-n}
 -V_N-\frac{\epsilon C}{2}.
}
\tag{24}
$$
(24)只在对应的原输入上具有所需整性，不声称中间的除法算子在所有函数上整。
所有 $H^{-1}$ 项都必须先合并；原 $\mathcal Q$ 没有因此变成一个可在
$P$ 自由逐项取值的谱投影。

## 5. 原 CM 点的准确留数公式

原 $P$ 上，R856 给
$$
H(P)=0,\quad c:=C(P)\in\mathcal O_{(p)}^\times,\quad
R\in(g_2^2),\quad H/g_2\in\mathcal O_{P,(p)}^\times.
\tag{25}
$$
于是 $R/H$ 在 $P$ 附近整且为零，$a_H$ 同样正规。
这里 $H(P)=D^2H(P)=0$ 都是指定提升的**特征零准确等式**，不是仅模 $p$ 为零。所以全部 $G_r,V_r$ 在该点都为整微分算子。
这些断言在同一个固定 étale 覆盖点上仍成立。

**留数引理。** 若 $H$ 在 $P$ 简单为零、$DH(P)=c\ne0$、
$D^2H(P)=0$，且 $f$ 在 $P$ 正规，则对 $N=n+1$ 有
$$
\boxed{
(G_Nf)(P)
=N!\,c^{N+1}
 \operatorname{Res}_{P}\frac{f\,\omega}{H^{N+1}}.
}
\tag{26}
$$
证明在特征零作有限局部展开即可。取 $Du=1,u(P)=0$，
则 $H=cu+O(u^3)$，且没有 $u^{-1}$ 项阻止
$$
t=\int\omega/H^2=-1/(c^2u)+O(1),\qquad \delta t=1.
$$
$f/H^n$ 在 $t=\infty$ 的多项式部分次数至多 $n$，被 $N$ 次
$t$ 导数全部杀掉。写其 $t^{-1}$ 系数为 $\beta$；
其它负次项在(21)后于 $P$ 为零。
由 $H^{-n-2}\sim(-ct)^{n+2}$，所得值为
$-N!c^{n+2}\beta$。
另一方面 $t$ 在 $P$ 为单极，所以
$\operatorname{Res}_{P}(fH^{-n}dt)=-\beta$，正得(26)。
此处的符号和 $c^{N+1}$ 都由原微分 $\omega(D)=1$ 决定。

整性无需给完整形式积分指定 $p$-整原函数。
$H$ 自身是(25)下的整局部参数，$\omega=dH/C$，故
$$
\boxed{
\operatorname{Res}_{P}\frac{f\,\omega}{H^{N+1}}
=[H^N](f/C)\in\mathcal O_{(p)}.
}
\tag{27}
$$
所需有限阶只有 $N<p$，且 $N!$ 为单位。

把 $G_N=T_N+pV_N$ 代入(26)。由原来源的(18)及
$H(P)=f_\nu(P)=0$，$T_Nf_\nu(P)$ 整除 $p$；这一步不来自一般函数的三阶零。
$V_Nf_\nu(P)$ 已整，故(27)的原四留数也整除 $p$。
最终得到同一原首行的全式
$$
\boxed{
\mathfrak B_{\nu,p}
=2m_\nu\epsilon_\nu
\left[
N!c^{N+1}\,
\frac{\operatorname{Res}_{P}
 (f_\nu\omega/H^{N+1})}{p}
-(V_Nf_\nu)(P)
\right]\pmod p.
}
\tag{28}
$$
先确认方括号整，再把 $(2m_\nu)^N$ 约成 $2m_\nu\epsilon_\nu$。
没有删除高幂的 Fermat 商；它乘在已经整的原商上。

## 6. 可接续的实际问题及范围

(28)把原四条半长除 $p$ 行放在同一固定参数覆盖及同一指定
Hasse 坐标中。$f_\nu$ 固定先于 $p$，$H,N,V_N$ 是原素数给定的对象。
留数来自原函数，不是另择一个有相同三阶零的测试函数。

R856 已付的 $D^2R(P)=110bc_p$ 在(22)–(23)中仍完整出现。
但(28)须比较这个完整 $V_Nf_\nu$ 与同一函数的实际留数除 $p$；
不能只保该单位、公共核的非零符号份额，或总留数定理的一条总和，
就宣布四个原值不同时为零。
本注没有宣称随 $p$ 的 $H^{N+1}$ 高极点是固定低度 Cartier 来源，
也没有把 $\Pi_\pm$ 的模 $p$ 投影当作其无误差的模 $p^2$ 提升。

后继直接处理(28)的四个实际配对及共同 $A_{24}$ 的全相对乘法约束。
原全部物理 $P_{2,M}$、CM13 frame、Artin 来源、carry 和通常全 Selmer 条件不变。
本注无数学程序运行、数值扫描或新增算术非零假设。
