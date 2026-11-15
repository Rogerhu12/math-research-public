# R285：全部对称 Gaussian 乘积的三阶主项、真实二阶余项与位置空间上界

日期：2026-11-15。**原式纸面分解；没有执行符号程序、求积、profile 扫描、新人工检查或科学运行。**

[R282](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md)给十个对称 Gaussian history 系数的准确式；[R284](R284-six-alternating-packets-pay-the-square-history-and-even-energies.md)已联合支付整个 $E_{-3}^2$ 与六识别能量。本稿处理其余项之前，先给一份适用于全部十个乘积的准确导数阶数分解。

结论有两个不同层次：

1. 在真实不交微包上，每个对称乘积的三外矩，模去一个**保所有原尾的实际 $C^2$ 多项式泛函**后，恰为明确的 $u'''$ 平方积分。不能把这个余项直接称零或称已经由旧 $\mathcal F$ 保持。
2. 对一组固定母包、固定振荡因子和全部固定完整副本，三十个必要外矩加 $L_c,M_c$ 的高频主向量，是至多十次的位置多项式，故其位置张成空间维数至多十一。R284 的五维子系统给大正位置上的下界五；本稿不计算中间的实际秩，更不把十一当作三十二个完整方程的自由控制维数。

来源：[R259 的原二次输出、Euler 配对及真实跨包核](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R277 的保原尾 $C^2$ 降阶与完整观测纤维](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、[R279 的完整高频 $C^1$ 极限](R279-finite-frequency-fiber-control-pays-both-even-profile-energies.md)、R282、R284。

## 1. 本稿的“模 $C^2$”是明确的真实函数类别

固定有限物理区间 $I=[\ell,r_*]$，所有实际母包在其两端有共同零 collar。写

$$
v=u',\qquad \rho=u'',\qquad q=u''',
$$

$$
J_0(x)=\int_x^{r_*}\rho^2,\quad
J_1(x)=\int_x^{r_*}t\rho(t)^2\,dt,\quad
J_2(x)=\int_x^{r_*}\{t^2\rho(t)^2+2v(t)^2\}\,dt.
\tag{1}
$$

采用原正右积分，故 $J_0'=-\rho^2$、$J_1'=-x\rho^2$、
$J_2'=-(x^2\rho^2+2v^2)$。不将左端三个实际值置零。

称一个泛函为本稿的 $C^2$ 余项，是指它由固定有限区间上的下列运算有限组成：

- $x,u,v,\rho,J_0,J_1,J_2$ 的多项式、乘积和积分；
- 原真实三个矩及其多项式；
- 多个固定不交包时，相应各包的这些数据及真实排序所产生的尾系数。

这些都是共同支撑 $C^2$ Banach 域上的连续多项式，因此其 Fréchet 导数也连续。实际函数仍取 $C^\infty$；这里的导数阶数说明不是在给粗糙 profile 作三阶求导。

记 $A\equiv_2 B$，表示 $A-B$ 属于上述实际余项类。它是一个准确等式的简写，**不表示数值误差小、等式已零，或可任意选择余项**。

## 2. 只有一次 $u'''$ 的项可以准确降阶，全部尾保留

设 $H=H(x,u,v,\rho,J_0,J_1,J_2)$ 为有限多项式。定义关于 $\rho$ 的多项式原函数

$$
\mathcal A(x,u,v,\rho,J)
=\int_0^\rho H(x,u,v,z,J)\,dz,
$$

以及不作用于 $\rho$ 的显式导子

$$
D_0=\partial_x+v\partial_u+\rho\partial_v
-\rho^2\partial_{J_0}-x\rho^2\partial_{J_1}
-(x^2\rho^2+2v^2)\partial_{J_2}.
\tag{2}
$$

原链式法则给

$$
D_x\mathcal A=Hq+D_0\mathcal A.
$$

所以准确有

$$
\boxed{\int_I Hq
=[\mathcal A]_\ell^{r_*}-\int_I D_0\mathcal A
=-\int_I D_0\mathcal A.}
\tag{3}
$$

最后一个等号只用 $\rho=0$ 于两 collar。因为关于 $\rho$ 的原函数从0起算，所以即使 $J_0,J_1,J_2$ 的左尾不为零，$\mathcal A$ 的端值仍为零。

若人为把积分截在一个 $\rho\ne0$ 的活动点，必须保留端项；本稿从不这样删边界。(3)也允许 H 含多个其他包的真实尾多项式，只要这些系数按原数据保留。

## 3. 六个实际方向的完整最高导数系数

R259 的六个实际对角输出写为

$$
\begin{aligned}
P&=J_0,& R&=v^2+xJ_0,& S&=J_1,\\
L&=uv-\frac{xv^2}{2}-\frac{x^2J_0}{4}+\frac{J_2}{4},\\
U&=xv^2+xJ_1+\frac{J_2}{2},\\
V&=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2J_2}{4}.
\end{aligned}
\tag{4}
$$

这里只将对角函数简写为字母，其双线性极化仍是原 $\Phi_X$。直接作两次真实 x 导数，得到

$$
X''=\alpha_Xq+\beta_X.
\tag{5}
$$

完整表为：

| X | $\alpha_X$ | $\beta_X$ |
|---|---|---|
| P | $-2\rho$ | $0$ |
| R | $2v-2x\rho$ | $0$ |
| S | $-2x\rho$ | $-\rho^2$ |
| L | $u-xv$ | $-(J_0+x\rho^2)/2$ |
| U | $2xv-3x^2\rho$ | $2\rho(v-x\rho)$ |
| V | $x^2u-x^3v+x^4\rho/2$ | $-2uv+2x(u-xv)\rho-J_2/2+x^3\rho^2/2+xv^2$ |

例如 V 的 $J_2$ 原项在 $\beta_V$ 中仍然存在。表中不把任何原 primitive 替换成零，也没有只列主导 x 幂而删掉其他同阶 jet。

令

$$
A=-2\rho,\quad B=2v-2x\rho,\quad C=u-xv.
$$

则六个主系数可更紧地写成

$$
(\alpha_P,\alpha_R,\alpha_S,\alpha_L,\alpha_U,\alpha_V)
=(A,B,xA,C,xB+x^2A/2,x^2C-x^4A/4).
\tag{6}
$$

固定 x 时 $(u,v,\rho)\leftrightarrow(A,B,C)$ 可逆。这个三维局部 jet 表示只是在整理原式，不代表固定圆上的积分泛函只有三维。

四个真实 Gaussian 方向为

$$
B_1=\zeta\Phi_V,\quad
B_{-1}=d\Phi_L+e\Phi_U,\quad
B_{-2}=a\Phi_R+b\Phi_S,\quad
B_{-3}=c\Phi_P.
$$

因此

$$
\boxed{
\begin{aligned}
\alpha_1&=\zeta(x^2C-x^4A/4),\\
\alpha_{-1}&=dC+e(xB+x^2A/2),\\
\alpha_{-2}&=aB+bxA,\\
\alpha_{-3}&=cA.
\end{aligned}}
\tag{7}
$$

当 $(u,v,\rho)$ 视为固定母坐标 y 上的函数时，这四式关于物理 x 的次数分别不超过 $4,2,1,0$。

## 4. 三个原外矩的准确主项

原三外矩为

$$
I_0(X,Y)=\int X''Y'',\quad
I_1(X,Y)=\int xX''Y'',
$$

$$
I_2(X,Y)=\int\{x^2X''Y''+2X'Y'\}.
$$

由(5)，

$$
X''Y''=\alpha_X\alpha_Yq^2+
(\alpha_X\beta_Y+\beta_X\alpha_Y)q+\beta_X\beta_Y.
$$

中间项按(3)准确降为 $C^2$；最后一项原本就是 $C^2$。
$X',Y'$ 只含二阶及更低数据和原 primitive，所以 $I_2$ 中的 $2X'Y'$ 也属于真实余项，并不是被忽略。

因此对 $j=0,1,2$，

$$
\boxed{
I_j(X,Y)\equiv_2
\int x^j\alpha_X\alpha_Y(u''')^2.
}
\tag{8}
$$

一般不能进一步把右边降为 $C^2$。R282 的 P 平方正是一个已证明独立的新三阶条件。

## 5. 嵌套外槽的对称部分与同一个主平方配对

令

$$
F_{X,j}(u)=I_j\{u,\Phi_X(u,u)\}.
$$

R259 给其真实 local cubic 密度，R277 证明这是一份 $C^2$ 多项式。R259 的 Euler 配对是

$$
2I_j\{u,\Phi_X(u,w)\}
=\int Q_{X,j}(u)w,\qquad
Q_{X,j}=\operatorname{EL}(f_{X,j})-L_j\Phi_X(u,u),
\tag{9}
$$

其中 $L_0=D^4$、$L_1=xD^4+2D^3$、
$L_2=x^2D^4+4xD^3$。它对有真实左多项式尾的 w 也成立，因为 u 有两零 collar。

取 $w=\Phi_Y(u,u)$。此处先将 $w$ 乘一个在 $u$ 支撑邻域恒为一的紧 cutoff，再取原合法域内的变分 $DF_{X,j}(u)$；原 local 密度的一阶偏导在零 collar 为零，所得值与 cutoff 无关。这没有把带非零左尾的 $w$ 冒作原紧支撑 Banach 域中的方向。R259 的真实 Euler 配对仍保(9)及下述 Green 端项。这个变分的最高 $u'''$ 仅一次：$w,w'$ 无三阶导，$w''$ 由(5)至多线性含它。于是(3)证明这个变分是 $C^2$ 余项。

另一方面，

$$
\int wL_j\Phi_X(u,u)
=I_j\{\Phi_X(u,u),\Phi_Y(u,u)\}
+\text{真实端项}.
$$

二次输出的左尾是原三个矩确定的至多二次多项式，右尾为零；所以此处所有 Green 端项属于明确的 $C^2$ 类。它们没有被宣称为零。

因此得到

$$
\boxed{
2I_j\{u,\Phi_X(u,\Phi_Y(u,u))\}
\equiv_2-I_j\{\Phi_X(u,u),\Phi_Y(u,u)\}.
}
\tag{10}
$$

对 X、Y 交换后相加，

$$
I_j\{u,\Phi_X(u,\Phi_Y(u,u))
+\Phi_Y(u,\Phi_X(u,u))\}
\equiv_2-I_j\{\Phi_X(u,u),\Phi_Y(u,u)\}.
\tag{11}
$$

这一步使用的是对称部分，不能用 R277 的反对称 self 恒等代替。原 Green 数据虽在模号中归类，仍是最后准确方程的一部分。

## 6. 全部十个乘积在真实不交微包上的统一分解

设

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,
$$

包络两两不交。固定圆参数 $\theta$，记

$$
c_i(\theta)=a_i\cos\theta+b_i\sin\theta,\qquad
d_i(\theta)=a_i^2-c_i(\theta)^2.
$$

R282 的平方外矩记 $Q_{rr,j,\theta}$；交叉乘积外矩除以2，记
$\widetilde Q_{rs,j,\theta}=Q_{rs,j,\theta}/2$，平方则不除。
这样所有 $r,s\in\{1,-1,-2,-3\}$、$r\le s$ 统一为

$$
\begin{aligned}
\widetilde Q_{rs,j,\theta}={}&
-I_j(B_rD_\theta,B_sD_\theta)\\
&+I_j\{\phi_\theta,
 B_r(\phi_\theta,B_sD_\theta)
+B_s(\phi_\theta,B_rD_\theta)\}.
\end{aligned}
\tag{12}
$$

对于同一个包，(8)、(11)给高阶权重

$$
-d_i^2-c_i^2d_i=-a_i^2d_i.
$$

对于不同包，两个 $\alpha q$ 主项支撑不交，不能产生 $q_iq_k$。另一个包在当前支撑上留下的原二次输出只是至多二次多项式，系数为其真实三个矩；包含一次 $q_i$ 的项可按(3)降阶。对嵌套项也可使用(9)：外包的 local $Q_{X,j}$ 与别包的真实尾配对，经保边界的 IBP 降为同一 $C^2$ 类。

于是得到**完整准确分解**

$$
\boxed{
\widetilde Q_{rs,j,\theta}
=-\sum_i a_i^2d_i(\theta)
 \int x^j\alpha_r[u_i]\alpha_s[u_i](u_i''')^2
+\mathcal R_{rs,j,\theta}(\mathbf u).
}
\tag{13}
$$

$\mathcal R$ 是第1节指定的实际 $C^2$ 多项式泛函，含全部真实 self 低项、有序跨包尾和 Green 端项。这不是仅一个渐近首项公式。

对 $r=s=-3$，$\alpha_{-3}=-2c\rho$，故主项就是
$-c^2\sum_i a_i^2d_i\int x^j\{(\rho_i^2)'\}^2$。
R282 的完整计算还给出该项 j=2 的低阶余项，最终留下
$2\sum R_i^2\int\rho_i^4$；这实例说明 $\mathcal R$ 通常不能删掉。

在 R277/R280 的十二完整 odd 包装中，
$d_i=\sin^2\theta\,R_i-2\sin\theta\cos\theta\,T_i$。
主项的 x 次数不超过10，故原真实复制及十次平移消去其 odd 部分，留下 $\sin^2\theta$ 乘 $\lambda_i=-a_i^2R_i$ 的主向量。完整余项仍按原全角多项式保存。没有从“主项只有 $\sin^2\theta$”推断整个系数只含这个角函数。

## 7. 固定母包与固定振荡因子后的32个主观测

采用原同 $\mathcal F$ 有限 IFT 族

$$
u_N(z,y)=u_0(y)+zN^{-3}\chi(y)\cos Ny
+\sum_\ell a_{\ell,N}(z)e_\ell(y).
\tag{14}
$$

真实有限正幅盒先固定，随后

$$
u_N-u_0=O_{C^2}(N^{-1}),\quad
u_N'''=u_0'''+z\chi\sin Ny+O_{C^0}(N^{-1})
$$

及其参数一阶导数一致成立。$\mathcal R$ 为真正连续可微的 $C^2$ 多项式，所以其相对基点的值与参数导数均趋零；这只是极限事实，**不表示每个有限 N 上余项准确不变**。

固定一个完整 block 的全部真实偏移 $d_\nu$ 和正四次幅权
$\omega_\nu=\gamma_\nu^4$。对30个必要观测
$\widetilde Q_{rs,j,\pi/2}$ 定义主向量分量

$$
P_{rs,j}(X)=\frac12\sum_\nu\omega_\nu
\int (X+d_\nu+y)^j
 \alpha_r(X+d_\nu+y;u_0,v_0,\rho_0)
 \alpha_s(X+d_\nu+y;u_0,v_0,\rho_0)
 \chi(y)^2\,dy.
\tag{15}
$$

因子 $1/2$ 来自真实 $\sin^2 Ny$ 的平均。$u_0,v_0,\rho_0$ 均在母坐标 y 取值；没有随 X 任意换形状。

把 R279 的两个完整主系数 $\mathcal S(X),\mathcal T(X)$ 也加入，得到32维向量

$$
\mathbf P(X)=\bigl(P_{rs,j}(X),\mathcal S(X),\mathcal T(X)\bigr).
\tag{16}
$$

若六个或更多基本包取各自幅参数 $z_i$，各包仍复制到同一完整包装，则完整观测向量具有真实一致 $C^1$ 极限

$$
\boxed{
\mathbf V_N(\mathbf z)\longrightarrow
\mathbf V_0+\sum_i z_i^2\lambda_i\mathbf P(X+t_i).
}
\tag{17}
$$

$\mathbf V_0$ 是全部原主项和全部 $\mathcal R$ 的完整基线。
(17)既包含有限 N 的余项变化，也允许把已知余项完整放在基线中。若需要让某些余项在有限 N 上准确固定，必须另证它们已在原 $\mathcal F$ 中，或从一开始增添这些真实 $C^2$ 观测并重作最大秩选择；不能默认已有纤维固定一切二阶数据。

全角表达(13)的主变化都是同一个 $\sin^2\theta$ 倍。
因此其他角系数中仍可能有独立的 $C^2$ 条件；只解(16)也不能自动授予完整十个乘积的全角零。

## 8. 位置主空间至多十一维，而非三十二个独立控制

由(7)，每个(15)的 x 次数至多 $4+4+2=10$。
R279 的 $\mathcal S,\mathcal T$ 次数至多10、9。故有准确的固定向量

$$
\boxed{
\mathbf P(X)=\sum_{m=0}^{10}\mathbf c_m X^m,
\qquad \mathbf c_m\in\mathbb R^{32}.
}
\tag{18}
$$

所以

$$
\dim\operatorname{span}\{\mathbf P(X):X\in\mathbb R\}
=\dim\operatorname{span}\{\mathbf c_0,\ldots,\mathbf c_{10}\}
\le11.
\tag{19}
$$

等号左边的第一步只是多项式与任意11个不同实点的 Vandermonde 可逆性；这里不需要执行一个数值秩测试。

R284 从 P 平方的三个原外矩及 $L_c,M_c$ 提取出真正五维的主子系统，故在该大正位置构造中，(19)的实际维数至少5。本稿不证明它等于11，也没有列出未知余秩的严格核。

若某个 $\Lambda\in(\mathbb R^{32})^*$ 满足全部
$\Lambda\mathbf c_m=0$，则(17)的每个 principal 配平点都满足

$$
\Lambda\mathbf V_\infty=\Lambda\mathbf V_0.
\tag{20}
$$

因而要靠这一固定母包/固定 $\chi$ 的 principal 正平衡建立正则零点，必须先有
$\Lambda\mathbf V_0=0$。这个具体兼容条件不能仅靠再加同类位置消去。
若基线不满足它，(17)在任何已固定有限幅盒上收敛到一个与零分离的该投影，故该构造不能给大 N 根。

这不是对其他母包、多个不同 $\chi$、有限 N 非principal机制或更一般 profile 的不可解证明；也不能用这个上界否定已经明确支付的五维子系统。

## 9. 已付结论和下一步的准确边界

本稿已经完成六方向完整 $\alpha/\beta$ 表、保全部原尾的一次三阶项降阶、十个真实乘积的统一分解(13)，以及固定形状主控制空间的上界(19)。

接下来需要按原式确定具体 $\mathcal R$ 及其与旧 $\mathcal F$、已付三个 H 的关系，或提取(20)的真实兼容式。若更换或增加振荡形状，也必须保同一完整观测纤维和全部真实副本，再证明新的正锥和有限 N 正则根。

R284 已付的72面积、六能量和完整 P 平方保持为正面结果。本稿没有宣称其余九个乘积、零/一层 history、canonical period、同一 gauge 联立或主课题的闭嵌入/reach/固定 g 连续族已经完成。

