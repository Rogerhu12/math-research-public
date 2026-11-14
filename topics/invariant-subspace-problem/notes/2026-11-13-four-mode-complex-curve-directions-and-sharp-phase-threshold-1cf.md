# 工作接口：四模式复曲线方向的选择与严格相位阈值

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：方向选择与方法边界完整证明；正文数学已获根代理及 boundary_resume_1cf 全文独审。循环性范围经再次去重归入已有定理合成，不登记为新的循环范围。普通复 Hilbert 不变子空间问题仍未完成。

**范围订正。** 本文的四等差模式全部复二次、全部外层复合结论，已经可由已发表的多尺度全柱稿 §§1–4、合并矩最高曲线定理及实二次/最大纯矩逆接口合成，而且该合成不要求 $s_0<3d$。因此下文保留的独立内容是 §3 的复方向选择引理、§4 的实际相位缺陷入口及 §7 对整个射影曲线方向族的明确障碍。$s_0<3d$ 是本空谱方向构造的充分阈值，不是目标循环性的阈值。

准确旧来源：[真实多尺度全柱](../results/R150-appendix-multiscale-column-budgets-bell-covariance-and-full-plane-joint-polynomials.md)（回读 blob `77032e2d67349dd08e442638d357e88fd92cb373`）与[合并矩](../results/R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)。在 §2 的表示中，若 $\gamma\ne0$，最高中心为 $(be-c^2)$ 的非零系数 $d^2/(\rho_2\rho_4\rho_3^2)$；若 $\gamma=0,\beta\ne0$，最高中心为 $(ae-bc)$ 的非零系数 $2d^2/(\rho_1\rho_4\rho_2\rho_3)$。这两阶均高于全部仿射项，且真实 log 行满足规范尾 $O(1/(\sqrt n\log n))$，故旧多尺度柱适用整个 $Q(F)$。剩余 $\beta=\gamma=0$ 是复标量乘实二次加任意复仿射，已有实二次全复合定理覆盖。

本稿首先使用 [R138 完整第一阶谱分类](../results/R138-first-chaos-complete-spectrum-classification.md) §1 的空谱分支及 §3 的实际预解证明：
非可和第一阶行只要有一个可和相位缺陷方向，其真实闭 first 就为空谱。
随后使用[全域偏导逆稿](../results/R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md) §§2–4 的真实有界逆和完整单 first Bell 逆，
以及[曲线方向稿](../results/R150-appendix-physical-logarithmic-curve-directions-and-smooth-leading-symbols.md) §§2–4 的合法合并方向和原核块提升。
新的内容是任意复二次系数下的方向存在证明；该方向的一条虚部行可以不可和，不能以有界 $\ell^1$ 扰动替代 R138 的相位缺陷判据。

## 1. 原模式和主结论

固定
$$
s_0>0,\qquad d>0,\qquad \boxed{s_0<3d},
$$
并取四个正实指数
$$
\rho_j=s_0+(j-1)d,\qquad 1\le j\le4.
$$
原模式及归一化为
$$
u_{\rho_j}=-\kappa_{\rho_j}
+\sum_{p\ge0}\frac{\rho_j(\log(p+2))^{\rho_j-1}}{p+2}\chi_p,
\qquad
U_j=u_{\rho_j}/\rho_j.
\tag{1.1}
$$
这里只作固定非零标量缩放，原 $\kappa_{\rho_j}$ 同步保留。
令 $w=w_*+\sum_pw_p\chi_p$，$(w_p)\in\ell^2(\mathbb C)$。

**定理。** 对任意非恒定复系数多项式
$F\in\mathbb C[x_1,x_2,x_3,x_4]$、$\deg F\le2$，
以及任意非零一变量多项式 $Q$，
$$
\boxed{
Q(F(U_1,U_2,U_3,U_4))e^w
\text{ 非零且对原 }A\text{ 循环}.
}
\tag{1.2}
$$
特别包括全部 $\lambda\in\mathbb C$、$r\ge1$ 的
$$
[F(U)-\lambda]^r e^w.
$$
系数不要求是同一复标量乘实系数。
四个原模式 $(u_1,u_2,u_3,u_4)$ 是 $s_0=d=1$ 的特例，故也全部包含。

本稿最后给出一个准确边界：若 $s_0\ge3d$，存在复二次共振，使本稿全部非零曲线方向产生的 first 均为全平面连续谱。
这只限定当前方向逆方法，不否定这些目标的循环性。

## 2. 零最高曲线的全部二次形式

在显示变量 $(a,b,c,e)$ 中记
$$
v(z)=(1,z,z^2,z^3).
$$
这里用 $e$ 表示第四个显示变量，以免与指数间距 $d$ 混淆。

若 $F$ 为仿射非恒定，或其二次部分 $F_2$ 满足
$$
F_2(v(z))\not\equiv0,
$$
则[合并矩定理](../results/R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)
的最高普通曲线非零条件直接给 (1.2)。
归一化后的实际曲线是一个非零共同因子乘
$(1,t^d,t^{2d},t^{3d})$，所以这两个“恒零”条件准确等价。

以下只处理
$$
F_2(v(z))\equiv0,\qquad F_2\ne0.
$$
按 $z^0,\ldots,z^6$ 比较全部十个二次单项式的系数，准确得到
$$
\boxed{
F_2=\alpha(ac-b^2)+\beta(ae-bc)+\gamma(be-c^2),
}
\tag{2.1}
$$
其中 $\alpha,\beta,\gamma\in\mathbb C$ 不全为零。
加上任意复仿射项，写 $F=F_2+\ell$。

定义
$$
D_z=(v(z)\cdot\nabla)F.
$$
因为 $F_2(v(z))=0$，有限标量展开准确为
$$
\boxed{F(y+t v(z))=F(y)+tD_z(y).}
\tag{2.2}
$$
$D_z$ 的常数项是 $\ell_{\mathrm{lin}}(v(z))$，线性系数为
$$
\begin{aligned}
p_1(z)&=\alpha z^2+\beta z^3,\\
p_2(z)&=-2\alpha z-\beta z^2+\gamma z^3,\\
p_3(z)&=\alpha-\beta z-2\gamma z^2,\\
p_4(z)&=\beta+\gamma z.
\end{aligned}
\tag{2.3}
$$
直接恒等式
$$
p_2=-2zp_3-3z^2p_4,\qquad
p_1=z^2p_3+2z^3p_4
\tag{2.4}
$$
将用于方向选择。它保留全部四个真实模式。

## 3. 任意复系数下存在一个可用方向

**代数引理。** 对每个非零三元组 $(\alpha,\beta,\gamma)$，存在有限 $z\in\mathbb C$，
使 (2.3) 非零，并满足下列之一：

1. $p_4\ne0$，且 $p_3/p_4,p_2/p_4$ 都为实数；
2. 全部非零 $p_j$ 有一个共同复因子，其余系数为实数。

第一种情况允许 $p_1/p_4$ 为非实数。

### 3.1 $\gamma=0$

若 $\beta=0$，则 $\alpha\ne0$；取 $z=0$，只留下
$p_3=\alpha$，属于第二种情况。

若 $\beta\ne0$，记
$$
\alpha/\beta=A+iB,\qquad A,B\in\mathbb R,
$$
并取
$$
z=-A/2+iB=x+iy.
$$
此时 $p_4=\beta\ne0$，且
$$
p_3/p_4=A+iB-z=3A/2=-3x.
$$
由 (2.4)，
$$
p_2/p_4=3(x^2+y^2)\in\mathbb R.
$$
因此第一种情况成立，包括 $B=0$。

### 3.2 $\gamma\ne0$ 且 $\beta/\gamma$ 为实数

提出共同因子 $\gamma$，置
$$
a_0=\alpha/\gamma,\qquad b_0=\beta/\gamma\in\mathbb R.
$$
取 $z=-b_0$。
若 $a_0\ne b_0^2$，则
$$
(p_1,p_2,p_3,p_4)
=\gamma(a_0-b_0^2)(b_0^2,2b_0,1,0),
$$
非零且属于第二种情况。
若 $a_0=b_0^2$，原三个归一化系数都是实数；
取任意实 $z\ne-b_0$，则 $p_4\ne0$ 且全部系数相对实，仍成立。

### 3.3 $\gamma\ne0$ 且 $\operatorname{Im}(\beta/\gamma)\ne0$：实方向分支

仍提出 $\gamma$，记
$$
a_0=A+iB,\qquad b_0=u+iv,\qquad v\ne0.
$$
对于实 $z=x$，
$$
\operatorname{Im}\frac{p_3(x)}{p_4(x)}
=
\frac{v x^2+B x+B u-A v}{|b_0+x|^2}.
\tag{3.1}
$$
分母严格为正。
设判别式
$$
\Delta=B^2-4v(Bu-Av)
=(B-2uv)^2+4v^2(A-u^2).
\tag{3.2}
$$
若 $\Delta\ge0$，实二次式有实根 $x$。
此时 $p_3/p_4$ 为实数，(2.4) 也使 $p_2/p_4,p_1/p_4$ 为实数。
所以第一种情况成立，且实际还得到第二种。

### 3.4 判别式为负时的椭圆分支

以下设 $\Delta<0$。
令
$$
D=u^2-A>0.
$$
(3.2) 给
$$
|B-2uv|<2|v|\sqrt D.
\tag{3.3}
$$
考虑平面中的椭圆和实函数
$$
\mathcal E:\quad
(x+u)^2+2(y+v/4)^2=D+v^2/8,
$$
$$
f(x,y)=B+2vx-uy-xy.
\tag{3.4}
$$
它与 $y=0$ 相交于两点
$$
x_\pm=-u\pm\sqrt D.
$$
在这两点，
$$
f(x_\pm,0)=B-2uv\pm2v\sqrt D
$$
由 (3.3) 严格异号。

取连接这两点且满足 $yv>0$ 的椭圆开弧。
两个交点将椭圆分为上下两条弧，所以这条弧存在。
连续性给其内部一点 $(x,y)$ 满足 $f(x,y)=0$。
特别 $y\ne0$、$yv>0$。
令 $z=x+iy$，则
$$
\operatorname{Im}(b_0+z)=v+y\ne0,
$$
所以 $p_4=\gamma(b_0+z)\ne0$。

椭圆方程与 $f=0$ 两式合在一起准确为
$$
a_0+b_0(2x-iy)+x^2+2y^2-ixy=0.
$$
而
$$
p_3+3x p_4
=\gamma\bigl[a_0+b_0(3x-z)+3xz-2z^2\bigr].
$$
右端恰为上述表达式，因此
$$
\boxed{
p_3/p_4=-3x,\qquad
p_2/p_4=3|z|^2.
}
\tag{3.5}
$$
后式来自 (2.4)。
这证明第一种情况。
另有准确的最低系数
$$
\boxed{
p_1/p_4=-x^3-3xy^2-2iy^3.
}
\tag{3.6}
$$
它通常不是实数，因此本分支确实不能只引用实 first 加有界常数的旧证明。
全部参数分支至此完结。

## 4. 真正的空谱来源：最低虚部的相位缺陷可和

对代数引理的第二种情况，取出共同相位。
剩余是有限个不同正实对数幂的非零实线性组合，
最大指数项最终定号、绝对值不可和。
有限头不影响相位缺陷的可和性，所以 R138 给其原 first 空谱。

对第一种情况，除以固定非零 $p_4$，写
$$
p_3/p_4=r_3\in\mathbb R,\quad
p_2/p_4=r_2\in\mathbb R,\quad
p_1/p_4=r_1+i t,\qquad r_1,t\in\mathbb R.
$$
令 $L=\log(p+2)$。
原 $D_z(U)$ 的归一物理行准确为
$$
c_p=
\frac{L^{s_0-1}}{p+2}
\left[r_1+it+r_2 L^d+r_3 L^{2d}+L^{3d}\right].
\tag{4.1}
$$
被提出的 $p_4$ 只决定一个固定相位和非零模长。
设
$$
R(L)=L^{s_0+3d-1}+r_3L^{s_0+2d-1}
+r_2L^{s_0+d-1}+r_1L^{s_0-1},\qquad
I(L)=tL^{s_0-1}.
$$
充分大的 $L$ 有 $R(L)\ge\tfrac12L^{s_0+3d-1}$。
因此逐项
$$
\begin{aligned}
|c_p|-\operatorname{Re}c_p
&=\frac1{p+2}\frac{I(L)^2}{\sqrt{R(L)^2+I(L)^2}+R(L)}\\
&\le \frac{C}{p+2}L^{s_0-3d-1}.
\end{aligned}
\tag{4.2}
$$
由于 $s_0<3d$，右侧可和。
另一方面 $|c_p|\asymp L^{s_0+3d-1}/(p+2)$，
所以行不属于 $\ell^1$，而且属于 $\ell^2$。

现在直接适用 R138 §1 的 (1.3) 及 §3 的真实域预解证明：
$$
\boxed{\sigma(X_{D_z(U)})=\varnothing.}
\tag{4.3}
$$
$D_z$ 的仿射常数与原各 $\kappa_{\rho_j}$ 已含在这个 first 中，不需要改中心。
(4.2) 不声称虚部行是 $\ell^1$：
事实上当 $t\ne0$ 时它是一个不可和的最低对数行。
其贡献是二次相位缺陷，准确预算是
$L^{s_0-3d-1}/(p+2)$。

对任意原复权 $w$，实际倾斜的一阶
$$
T=X_{D_z(U)}+H_w,\qquad H_w\in\{A\}'\cap B(H)
$$
在同一完整 first 域上成立。
此处额外倾斜才由原 $\ell^2$ 行与 $w$ 的乘积范数绝对收敛付清。
令 $L_0=X_{D_z(U)}^{-1}$；它是 $\{A\}'$ 中拟幂零有界元。
所以
$$
T^{-1}=L_0(I+H_wL_0)^{-1}\in\{A\}'
\tag{4.4}
$$
是真实两侧逆。
任意复位移同理，因此 $T$ 仍为空谱，其逆 $L=T^{-1}$ 拟幂零。

## 5. 完整普通幂的逆及原自然域

对每个固定 $h\ge1$，原点态
$D_z(U)^h e^w$ 的完整普通 Bell 实现为
$$
\mathsf B_{h,w}
=T^h+\sum_{j<h}C_jT^j,\qquad
C_j\in\{A\}'\cap B(H).
$$
自然幂的完整域是
$$
\operatorname{Dom}T^h=\operatorname{Ran}L^h,\qquad T^h=(L^h)^{-1}.
$$
在该域上，
$$
\mathsf B_{h,w}
=\left(I+\sum_{j<h}C_jL^{h-j}\right)T^h.
$$
括号内除单位外是有限个交换拟幂零项之和，故括号是有界单位。
因此
$$
\boxed{
\mathsf B_{h,w}^{-1}
=L^h\left(I+\sum_{j<h}C_jL^{h-j}\right)^{-1}
\in\{A\}'.
}
\tag{5.1}
$$

这里不能以 $T^h$ 代替完整 Bell。
其图识别使用 R186 的同一共同正则器：
对固定 $N\ge h$ 和自然域中 $x$，
$R(\varepsilon)^Nx\to x$，
$T^hR(\varepsilon)^Nx=R(\varepsilon)^NT^hx\to T^hx$。
所以共同有限词域是 $T^h$ 的图核心；有界单位使它也为
$\mathsf B_{h,w}$ 的图核心。
原规范 Bell 的闭包与这个实现相同。

按四原模式构造 $D_z(U)^h$，或按其单个实际 first 构造普通幂，
两者在 $\mathbb C[A]e^w$ 上动作相同，该轨道又分别为两者的图核心；
因而它们的闭图完整相等。
这正是下一节所用的全域偏导逆，而非形式上的单变量逆。

## 6. 复方向确实属于原合并矩表

固定外层 $Q$ 的次数 $h\ge1$，最高系数 $q_h\ne0$。
对整个 $G=Q\circ F$ 重建全部至 $\deg G$ 的原矩表。
归一模式的物理乘积按
$$
k=|\omega|,\qquad
s_{\rm key}=k(s_0-1)+d\,m,\qquad
m=\sum_{j=1}^4(j-1)\omega_j\in\{0,\ldots,3k\}
\tag{6.1}
$$
准确合并。
没有分开相同键的行。

在总矩阶 $h$ 上定义一个合法有限方向
$$
\boxed{
\eta_{(h,h(s_0-1)+dm)}=z^m,\qquad 0\le m\le3h,
}
\tag{6.2}
$$
其他总阶的方向分量为零。
这里 $z$ 为 §3 的一个固定复数。
指数 $m$ 都是非负整数，所以 (6.2) 没有多值幂；
$z=0$ 时按 $z^0=1$、其余为零定义。

若两个原多重指标具有同一键，则其 $m$ 相同，
同时满足
$$
v(z)^\omega=z^{\sum(j-1)\omega_j}=z^m.
$$
因此曲线方向稿的有限生成式计算逐项成立，给
$$
\partial_\eta Q_G
=\frac{(-2)^{h-1}}{h!}Q_{(v(z)\cdot\nabla)^hG}.
\tag{6.3}
$$
这只是一个合并矩方向的一次偏导，不是把任意高阶显示偏导免费当作原 $P^r$ 的顶部。

由 (2.2)，
$$
(v(z)\cdot\nabla)^hQ(F)=h!q_hD_z^h.
$$
原实际 Bell 修正与显示偏导交换，所以真实闭偏导准确为
$$
\boxed{
\mathsf D=(-2)^{h-1}q_h\,\mathsf B_{h,w},
\qquad
\mathsf D^{-1}\in\{A\}'\cap B(H).
}
\tag{6.4}
$$
(5.1) 已付这个逆的整个自然域和规范图。

对完整物理池矩阵 $\Xi_B$，取
$\beta_B=\tfrac14\Xi_B^{-1}\eta$，
并把块输入右乘固定 $\mathsf D^{-1}$。
在原规范核中已付的深域上，一次顶部准确以
$\mathsf D\mathsf D^{-1}=I$ 消去。
$r$ 块的新费用只有固定
$(\|\eta\|\,\|\mathsf D^{-1}\|)^r$；
跨池矩逆仍有 $e^{O(\log N)}$ 的费用。

同一正分量
$\mathcal R_r=R(r^{-2})^{c_G r}$ 保持原核并强趋 $I$，
支付全部 $O(r\deg G)$ 原自然词。
所有逆位于反射右侧的输入中，保持原核与这些词域；
不把逆穿过物理反射，不让逆的伴随保持未知核。
原多池平均、两侧 $A$ 四次局部界及全空间 $C$ 配对因而完整适用，
迫 $\ker\mathsf P_{G,w}=0$。
R186 图循环判据给 (1.2)。
$h=0$ 是非零常数倍 $e^w$，单独成立。
每个外层 $Q$ 都重做了完整构造，没有从一次循环性继承点态幂。

## 7. 当前曲线方向机制在 $s_0=3d$ 的准确障碍

本节不是不循环反例，只说明 §3–§6 的统一空谱方向结论确实使用
$s_0<3d$。

令 $s_0\ge3d$，并取同一四个等差模式上的非零复二次式
$$
F_* =-(ac-b^2)+i(ae-bc)+(be-c^2).
\tag{7.1}
$$
没有仿射项。
其最高物理曲线恒零。
对每个有限 $z$，(2.3) 给
$$
p_4=i+z,\qquad p_3=-1-iz-2z^2,
$$
而 $p_1,p_2$ 仍满足 (2.4)。
$z=-i$ 时四个 $p_j$ 全为零；
任何其他有限 $z$ 都有 $p_4\ne0$。

若此时相应 first 有可和相位缺陷，
唯一可能的方向是最高系数 $p_4$ 的相位。
而所有四个指数均满足
$$
2\rho_j\ge2s_0\ge s_0+3d=\rho_4.
$$
若某个较低比值 $p_j/p_4$ 有非零虚部，取其中最大的指数。
逐项缺陷的主项就是一个正数乘
$$
\frac{(\log(p+2))^{\,2\rho_j-\rho_4-1}}{p+2},
$$
其总和发散，包括等号时的 $1/[p\log p]$ 情形。
所以有限相位缺陷必迫三个比值
$p_1/p_4,p_2/p_4,p_3/p_4$ 全为实数。

写 $z=x+iy$、$p_3/p_4=r\in\mathbb R$。
由 (2.4)，若 $y\ne0$，$p_2/p_4$ 为实迫 $r=-3x$，
继而
$$
\operatorname{Im}(p_1/p_4)=-2y^3\ne0,
$$
矛盾。
若 $y=0$，对 (7.1) 直接相除得
$$
p_3/p_4=-2x+i,
$$
也不是实数。
故每个非零有限曲线方向的 first 都无可和相位方向。

射影端点 $z=\infty$ 对应纯第四坐标方向，
得到 $iU_1+U_2$。
其相位缺陷以
$(\log(p+2))^{s_0-d-1}/(p+2)$ 为主项，
因 $s_0\ge3d>d$ 同样发散。

所有这些非零行都非可和且平方可和。
R138 §1 的 (1.4) 因而给它们的原 first
$$
\boxed{\sigma=\sigma_{\mathrm{ap}}=\mathbb C,}
$$
并且全部为连续谱。
零方向 $z=-i$ 不提供可逆的一阶系数。
因此不能把本稿选取的曲线方向 first 全部免费换成有界逆。
这不排除其他矩目标、其他实际证书或这些 $F_*$ 的循环性；
它只给当前曲线方向方法的一条精确边界。

## 8. 去重和范围

已有实二次定理允许任意有限个正实对数指数；多尺度列还覆盖 §2 中最高加权组中心非零的复系数分支。两者合成已经覆盖本文全部循环结论，且不需要指数间距限制。本文不把这种既有交集重新计为新增循环范围。

原曲线方向稿主要使用 $\tau>0$ 的实方向。
本稿的复方向通过整数键 (6.1)–(6.2) 直接构造，
不需要解释非整数指数的复杂分支，也不改变原物理坐标。

空谱的关键来自 R138 的实际可和相位缺陷定理；
最低虚部行本身不可和没有被忽略。
[五模式的穷尽合成](../results/R150-appendix-all-complex-quadratics-in-five-real-logarithmic-modes.md) 现已给任意至多五个不同正实指数、任意复二次的全部外层多项式循环性，无指数间距条件。因此 §7 的 $F_*$ 本身也已全部闭合；那里全平面谱的是候选曲线方向 first，不是对原目标循环性的否定。本工作记录保留可用于其他问题的方向构造与其方法边界，一般更高模式或更高次数仍须另证。
