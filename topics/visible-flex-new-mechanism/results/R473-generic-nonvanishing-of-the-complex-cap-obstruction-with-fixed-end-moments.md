# R473 — 固定末端三矩下复 cap 余量的真实开稠密非零

本稿是新的纸面结论，未执行程序、符号观察、人工数值或旧检查。它消费 [R471](R471-five-real-cap-conditions-and-the-complete-complex-second-moment-interface.md) 已付的完整复余量，不重新消元其余 self 系数。

**主结论。** 固定一个真实左 cap 的末端三矩、两端 germ 和一个严格内部窗口。在保持这些数据、$q>0$ 以及内部 $A_f>0$ 的 $C^\infty$ cap 类中，R471 的两个共轭复根上的余量同时非零是开稠密条件。更具体地，从任意 admissible cap 出发，可以选定一个实际紧支扰动方向，使余量成为一个最高系数非零的五次实参数多项式；因此只有至多五个实参数能使它消失。

这**不是**“每一个正 cap 都非零”的定理，也不识别当前冻结 cap 的值。它不把新的 cap 扰动自动装入 [R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) 的同 $q_0,\ldots,q_3$、共同 $D,E$、$F^\star$、二十目标库。末端三矩与那些全母观察是不同的约束。

## 1. 原左 cap 与固定复根

在固定有限区间 $[\ell,T]$ 上，设

$$
u'=p,\qquad p'=r,\qquad r'=q,
\qquad
u(\ell)=p(\ell)=r(\ell)=0.
\tag{1}
$$

所有函数光滑；原左平端 germ 保持不变。在 $(\ell,T)$ 上假设

$$
q>0,\qquad
A_f=6pq-2r^2>0.
\tag{2}
$$

于是 $r,p,u>0$。若 $T$ 是原唯一或指定的简单 $A_f$ 零点，本稿还保持其整个邻域，不仅保持一个端点数值。

定义三矩

$$
M_j=\int_\ell^T t^j q(t)\,dt,\qquad j=0,1,2.
$$

其中 $M_0>0$，且严格正测度具有正方差：

$$
m=\frac{M_1}{M_0},\qquad
v=\frac{M_2}{M_0}-m^2>0.
$$

取

$$
z_\pm=-m\pm i\sqrt v.
\tag{3}
$$

对任意复 $z$，保留原右端以前的真实累计：

$$
\begin{aligned}
w_z(t)&=-\int_\ell^t(s+z)q(s)\,ds
       =p(t)-(t+z)r(t),\\
a_z(t)&=\frac12\int_\ell^t(s+z)^2q(s)\,ds\\
      &=u(t)-(t+z)p(t)+\frac{(t+z)^2}{2}r(t).
\end{aligned}
\tag{4}
$$

则 $a_{z_\pm}(T)=0$。三矩与末端 jets 的对应完全明确：

$$
r(T)=M_0,\quad
p(T)=TM_0-M_1,\quad
u(T)=\frac{T^2M_0-2TM_1+M_2}{2}.
\tag{5}
$$

因此固定三矩等价于固定末端 $u,p,r$；它不固定 $q$ 的全部内部形状。

R471 已由完整原 primitive 与端项抵消给出

$$
\mathcal E_z(q)
 =\frac32\int_\ell^T
      (t+z)^2w_z(t)^2a_z(t)^2q(t)\,dt.
\tag{6}
$$

在 $a_z(T)=0$ 时，$a_z(\ell)=w_z(\ell)=0$，故原两次积分分部为

$$
\mathcal E_z(q)
 =3\int_\ell^T w_z^2a_z^2\,da_z
 =-2\int_\ell^T w_za_z^3\,dw_z.
\tag{7}
$$

这里没有把复被积函数称为正。实 $q$ 给
$\mathcal E_{z_-}(q)=\overline{\mathcal E_{z_+}(q)}$。

## 2. 一个实际紧支方向同时固定三矩和端 germ

任取非空开窗 $J$，使 $\overline J\subset(\ell,T)$。令
$f\in C^\infty_c(J;\mathbb R)$，并设

$$
u_\lambda=u+\lambda f,\quad
p_\lambda=p+\lambda f',\quad
r_\lambda=r+\lambda f'',\quad
q_\lambda=q+\lambda f'''.
\tag{8}
$$

这仍是从同一左零初值恢复出的完整链，不是仅修改一个 forcing 后任意补常数。对 $j=0,1,2$，三次真实分部给

$$
\int_\ell^T t^j f'''(t)\,dt=0.
\tag{9}
$$

因此三矩及 $z_\pm$ **精确不变**；$(u,p,r,q)$ 在 $J$ 外全不变，左右 germ 和末端简单 $A_f$ 零点的全部 jets 均不动。

对任何已经选定的有限 $f$，在其紧支包络上 $q$ 和 $A_f$ 有严格正下界。故存在 $\lambda_0>0$，使 $|\lambda|<\lambda_0$ 时仍有

$$
q_\lambda>0,\qquad A_{f,\lambda}>0
\quad\hbox{于 }J.
\tag{10}
$$

在窗口外这些不等式来自原 cap；末端原零点邻域原样保留。$q_\lambda>0$ 与同一左锚同时保证 $u_\lambda,p_\lambda,r_\lambda>0$。这不要求原平端附近有一个全局正下界，因为那里根本没有扰动。

固定三矩后，(4) 的 $w_z,a_z$ 都随 $\lambda$ 线性变化。所以对每一个固定的 $z=z_\pm$，

$$
\lambda\longmapsto \mathcal E_z(q_\lambda)
$$

是次数至多五的复系数多项式，其 $\lambda^5$ 系数准确为

$$
\mathcal E_z(f''')
=\frac32\int_J(t+z)^2
 \bigl(f'-(t+z)f''\bigr)^2
 \left(f-(t+z)f'+\frac{(t+z)^2f''}{2}\right)^2 f'''(t)\,dt.
\tag{11}
$$

这里对 signed $f'''$ 使用的是同一多项式表达，不赋予它正测度解释。

## 3. 真正满足 $\int(\phi'')^5\ne0$ 的紧支函数

需要一个实际函数，不能仅把第五矩当自由 jet。

先取偶的分段常数

$$
r_0(y)=
\begin{cases}
-1,& |y|<1,\\
2,&1<|y|<3/2,\\
0,&|y|>3/2.
\end{cases}
$$

它满足

$$
\int r_0=0,\qquad \int yr_0=0,\qquad
\int r_0^5=-2+32=30>0.
\tag{12}
$$

用偶、非负、单位质量的紧支光滑 mollifier 卷积，得
$r_\delta\in C^\infty_c(\mathbb R)$。偶性和总积分零精确保留；
$r_\delta\to r_0$ 于 $L^5$，故某个**固定有限**的充分小
$\delta>0$ 满足 $\int r_\delta^5>0$。

令

$$
\phi(y)=\int_{-\infty}^y(y-s)r_\delta(s)\,ds.
\tag{13}
$$

则 $\phi''=r_\delta$。在支撑左边 $\phi=0$；在支撑右边，

$$
\phi(y)=y\int r_\delta-\int s r_\delta=0.
$$

因此 $\phi\in C^\infty_c(\mathbb R;\mathbb R)$，两端所有 jets 都是零，并且

$$
\mathcal M_5(\phi):=\int(\phi'')^5>0.
\tag{14}
$$

一次正伸缩可把支撑放进 $(-1,1)$，不改变非零性。这里只需一个这样的函数；没有运行任何 profile 构造或数值积分。

## 4. 第五系数的原式渐近与非零

固定 $c\in J$，取上一节的 $\phi$，并令

$$
f_\varepsilon(t)=\phi\!\left(\frac{t-c}{\varepsilon}\right),
\qquad
\zeta=c+z.
\tag{15}
$$

先取 $\varepsilon>0$ 小到其支撑严格位于 $J$。因为
$\operatorname{Im}z\ne0$，所以 $\zeta\ne0$。

写 $y=(t-c)/\varepsilon$，并在本节简记

$$
p_0=\phi',\quad r_0=\phi'',\quad t_0=\phi''',
\quad x=\zeta+\varepsilon y.
$$

式(11)的两个真实累计恰是

$$
\begin{aligned}
w_{f_\varepsilon,z}
 &=\varepsilon^{-2}(\varepsilon p_0-xr_0),\\
a_{f_\varepsilon,z}
 &=\varepsilon^{-2}
   \left(\varepsilon^2\phi-\varepsilon xp_0+\frac{x^2r_0}{2}\right).
\end{aligned}
\tag{16}
$$

把它们代回原积分，而不是只引用最高形式 jet，得到

$$
\begin{aligned}
\mathcal E_z(f_\varepsilon''')
={}&\frac38\varepsilon^{-10}
       \int x^8r_0^4t_0\,dy\\
 &-\frac94\varepsilon^{-9}
       \int x^7p_0r_0^3t_0\,dy
   +O(\varepsilon^{-8}).
\end{aligned}
\tag{17}
$$

所有积分都在固定紧支撑上；余项来自有限多项式展开，故该
$O(\varepsilon^{-8})$ 是对已经固定的 $(\phi,c,z)$ 的实际有界余项。

三条原分部恒等为

$$
\int r_0^4t_0=0,\qquad
\int y r_0^4t_0=-\frac15\mathcal M_5(\phi),\qquad
\int p_0r_0^3t_0=-\frac14\mathcal M_5(\phi).
\tag{18}
$$

第一行(17)的首个非零项为
$-\frac35\zeta^7\varepsilon^{-9}\mathcal M_5$；
第二行为
$+\frac9{16}\zeta^7\varepsilon^{-9}\mathcal M_5$。
因此完整合式是

$$
\boxed{\;
\mathcal E_z(f_\varepsilon''')
=-\frac3{80}\zeta^7\varepsilon^{-9}\mathcal M_5(\phi)
 +O(\varepsilon^{-8}).
\;}
\tag{19}
$$

$-3/5+9/16=-3/80$。由于 $\zeta\ne0$ 且
$\mathcal M_5(\phi)\ne0$，某个**固定有限**的充分小
$\varepsilon$ 使(19)非零。共轭根的对应值同时非零。

这里的选参次序不可交换：

1. 固定原 cap、窗口 $J$、$c$ 和实际紧支 $\phi$；
2. 选定一个有限 $\varepsilon$，使支撑合法且(19)非零；
3. 此后只缩小 $\lambda$，用(10)保真实 cap 符号与所有原端 germ。

不要求 $\varepsilon\to0$ 的整个族都以同一个 $\lambda$ 保持
$q_\lambda>0$。高阶导数虽可大，在第二步之后已是有限常数，
第三步足以给严格合法扰动。

## 5. 固定端三矩类中的开稠密定理

**定理。** 在§1–2的固定区间、固定端 germ、固定末端三矩类内，
设原 admissible cap 非空。任取非空严格内部窗口 $J$。则

$$
\mathcal E_{z_+}(q)\ne0
\quad\Longleftrightarrow\quad
\mathcal E_{z_-}(q)\ne0
\tag{20}
$$

是相对开稠密条件；稠密性甚至只需 $J$ 内的实际紧支扰动。

**证明。** 式(6)是 $q$ 及其有限累计的连续多项式泛函。在固定有限区间上，它对 $q$ 的一致范数连续，也对原 $u$ 的 $C^3$ 范数连续，所以非零集相对开。

对任意基线，§3–4给出一个固定有限 $f_\varepsilon$，使
$\lambda\mapsto\mathcal E_{z_+}(q+\lambda f_\varepsilon''')$
的五次最高系数非零。故它至多有五个实零点，按重数亦不超过五。
在任意小的合法 $\lambda$ 区间内都可避开这些点，并保(9)–(10)。
由共轭性，另一根同时非零。

若基线恰好为零，$0$ 是这个非零多项式的某个有限重数根；
于是存在更小的 $\lambda_1>0$，使全部
$0<|\lambda|<\lambda_1$ 都非零。若基线已经非零，则直接用连续性。
最后，$\varepsilon$ 已固定，$\lambda f_\varepsilon$ 可在任意指定的
有限 $C^k$ 范数下任意小；同样进入任意给定的 $C^\infty$ Fréchet
邻域。证毕。

因此例外零集在这个准确的 cap 类内是闭且无内部的集合。本文没有证明它为空，没有将“至多五个沿线例外”误写成整个无限维类只有有限个例外。

## 6. 对 R471 实 self 门的含义

R471 的完整身份说明：在 $a_z(T)=0$ 的两个复根上，所列完整响应 self 与 $XY$ self 都零；$XH$ 留下的准确值是(6)。因此，若**所选真实 cap 本身**满足(20)，它就不能被那些 self 值的实线性组合消掉。

这一步的复数只用于一个实平移多项式的恒等检验。没有安装复几何、复 profile、复控制路径或复支撑位置；实多项式若相等，当然也必须在其两个共轭复测试点相等。

本稿把这个检验提升为真实 fixed-end-cap 类中的开稠密非零条件，但保留三个边界：

- 它不评价任何已经冻结母库的 $\mathcal E_{z_\pm}$。当前具体 cap 是否位于例外集，仍须其原完整身份或新的已授权观察。
- 它不单独判定原完整 $h/y$ 共同商。引用 R471 的不可消结论时，必须保其同一母、同一 self 规范、原 complete correction 与实际评价范围。
- 它不把一个新的 cap 方向当成负路径、实际成本或现成 actual 截面；本稿没有改变任何实际成本预算或已发表成员结论。

## 7. 不能免费保持的原库约束

扰动(8)精确保的是：

$$
\int t^j\delta q=0\ (j=0,1,2),\qquad
\delta u=\delta p=\delta r=\delta q=0\text{ 于 }J\text{ 外}.
\tag{21}
$$

它一般会改变
$\int r^5$、截断 $n_2$、全母 $q_0,\ldots,q_3$、共同 $D,E$、
原 $F^\star$ 及二十个真实目标。它也不能在多个已经不同的
mother 上逐个独立选择后冒称得到同一个公共 cap。

若要用于 R455/R464 的从起点构造，必须另外证明：在同一次初选中，
这些全母约束可用其它真实方向回补，且回补不撤销(20)、共同 cap、
根数、固定窗口与二十目标。本文不授予该附加兼容性。

还有一个函数类边界：非零 $C^\infty$ 紧支扰动通常不在整个连通内部解析。
若坚持“两函数在内部全解析且在一个开 cap 相同”，解析唯一性会迫它们全同。
本稿的 admissible 类明确是光滑类；它保留未扰动端 cap 的原解析 germ，
不宣称新函数在整个区间解析。

## 8. 当前结论与下一准确问题

已经闭合的是一个具体、有限、真实的扰动引理：固定三末端矩和全部端 germ，
选定一个有限紧支方向后，复余量是最高系数明确非零的五次多项式；
它的消失不能在这个正 cap 类内构成一个开条件。

仍未闭合的是“所有满足原正测度及 $A_f>0$ 的 cap 是否都非零”，以及
例外零集是否实际非空。证明这些更强结论必须继续处理完整复积分；
不能用被积正性、generic 性或本稿的有限参数选择代替。
