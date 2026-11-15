# R379：完整 ZZ 第二角商、十七行根与唯一冻结的局部四次残量

日期：2026-11-15。**有限纸面恒等与建设；未执行求积、符号程序、参数扫描、人工测试或研究计算。**

本稿接 R376/R380 的同一全偶真实弱圆，计算最后 $ZZ_2$ 的完整角商。它不是一个能被原主锥免费支付的低阶余项：在全部18面积下，准确剩
$$
c_\Omega\,\operatorname{Re}\int(q'-xq'')^4,\qquad c_\Omega>0.
$$
本稿保原 primitive 完整求出这个系数，并把 $ZZ_2$ 的 $\pi/2$ 实际值与全部旧目标放入一个有限频率十七行根。

由此，全部对称 Gaussian 外矩只留下一个明确的 $C^2$ scalar 残量。还证明该 scalar 的全部单包平移系数已经由原 $\mathcal F_\star$ 决定，所以现有同纤维振荡、增加同类 $\chi$ 或增大有限 $N$ 都不能改变它。这是现控制器的准确范围，不是全 profile 类的不可解结论；真实弱基线仍须在更早的形状／模块层另行支付这个量。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R348](R348-true-translation-and-Green-self-terms-pay-the-first-positive-minus-one-Gaussian-moment.md)、
[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md)、
[R353](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R360](R360-complete-positive-negative-second-self-and-six-dimensional-middle-cone.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R372](R372-complete-ZZ-zero-angular-quotient-and-nine-target-finite-frequency-control.md)、
[R375](R375-exact-Y-second-cubic-and-thirteen-target-control-pay-ZY2-and-YY2.md)、
[R376](R376-cubic-cross-identities-and-fifteen-target-cone-pay-ZY0-and-WY1.md)、
[R377](R377-complete-YY-zero-angular-quotient-and-local-C2-quartic.md)、
[R380](R380-sixteen-real-targets-and-one-finite-root-pay-the-complete-Y-square.md)。

## 1. 当前条件与目标的规范

仍取
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU,
$$
其中固定 $0<\zeta=\kappa^2<1/100,\ \kappa>0$，并用原
$$
a=-\frac{51\zeta^2+2\zeta+8}{64h_e^2},\quad
b=-\frac{34\zeta^2+8\zeta}{64h_e^2},\quad
d=\frac{6\kappa\zeta}{h_e},\quad
e=-\frac{\kappa(15\zeta+1)}{4h_e}.
\tag{1}
$$
特别 $a,e,a-b,d+e,d-5e,d+6e$ 都非零。

$f,g$ 是当前同一个全偶实紧三矩圆，保原弱单 hook、真实 rank-two 核、
完整第三、全部18面积、R364 的 $\mathcal T$、$\Psi$ 和三条 directed 行。
令
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi,\qquad q=f+ig.
$$
$q$ 的三个双线性矩全部为零，不取复共轭。
因此 $X(q,q)$ 对全部 $X\in E_8$ 都真紧。

normalized 对称外矩仍为
$$
\mathcal Q_{XY,j}
=-I_j(XD,YD)
+I_j\{\phi,X(\phi,YD)+Y(\phi,XD)\}.
\tag{2}
$$
记
$$
S_{XY,j}(q)=2I_j\{q,[X,Y](q;q^2)\},
$$
$$
K_{ZZ,2}(q)=I_2(Zq^2,Zq^2)+2I_2\{q,Z(q,Zq^2)\}.
$$
合法紧方向 $Zq^2$ 的完整变分给
$$
\boxed{K_{ZZ,2}(q)=DF_{Z,2}(q)[Zq^2].}
\tag{3}
$$
这一步只在整个合法复输入上使用；没有将单个 nonlegal 实包的 $Z$ 输出当成紧。

## 2. 原 Z 输出与完整 cubic

写 $u=q,v=q',r=q'',t=q'''$，
$$
P_u=J(r^2),\quad B_u=J(xr^2),\quad
C_u=J(x^2r^2+2v^2).
$$
$J$ 为原共同右锚。为简写置
$$
A=2e-d,\qquad B=d/2-4e,\qquad C=d+4e.
$$
原 R259 八式给 $w=Z(q,q)$：
$$
w=duv+\frac A2xv^2-\frac d4x^2P_u
+exB_u+\frac{d+2e}{4}C_u,
$$
$$
w'=dur+Axvr-\frac{3e}{2}x^2r^2+eB_u-\frac d2xP_u,
$$
$$
w''=(du+Axv-3ex^2r)t+2evr-\frac C2xr^2-\frac d2P_u.
\tag{4}
$$
这些是真实原函数身份；尚未删任何 primitive。

R349 的原两个 cubic 给
$$
F_{Z,2}
=A\int xur^2+B\int x^2vr^2+e\int x^3r^3
-\frac C3\int v^3.
$$
于是(3)准确成为
$$
\boxed{
K_{ZZ,2}
=\int\left[
Axr^2w+(Bx^2r^2-Cv^2)w'
+(2Axur+2Bx^2vr+3ex^3r^2)w''
\right].
}
\tag{5}
$$
$I_2$ 的 $2u'w'$ 已在原 cubic 内共同计入，不能再省略或补一个猜测边项。

## 3. 完整 primitive、最高导数及八个系数

用 R376 的八个积分记号
$$
\begin{array}{llll}
E_1=\int u^2r^2,&E_2=\int xuvr^2,&
E_3=\int x^2v^2r^2,&E_4=\int x^2ur^3,\\
E_5=\int x^3vr^3,&E_6=\int x^4r^4,&
E_7=\int v^4,&E_8=\int xC_ur^2.
\end{array}
$$

先列全部含 $t$ 项，避免只取候选项：
$$
\begin{aligned}
&2Ad\int xu^2rt
+2(A^2+Bd)\int x^2uvrt
+3e(d-2A)\int x^3ur^2t\\
&\quad+2AB\int x^3v^2rt
+3e(A-2B)\int x^4vr^2t
-9e^2\int x^5r^3t.
\end{aligned}
\tag{6}
$$
所需完整 IBP 为
$$
\int xu^2rt=-E_1/2-E_2,\qquad
\int x^2uvrt=-E_2-E_3/2-E_4/2,
$$
$$
\int x^3ur^2t=-E_4-E_5/3,\quad
\int x^3v^2rt=-3E_3/2-E_5,
$$
$$
\int x^4vr^2t=-4E_5/3-E_6/3,\qquad
\int x^5r^3t=-5E_6/4.
\tag{7}
$$
边项均含真正紧 $u,v,r$。

全部 $\int x^3r^2P_u$ 的系数是
$$
-d\left(\frac A4+\frac B2+\frac{3e}{2}\right)=0.
$$
其余 $P_u$ 项为
$$
\frac{Cd}{2}\int xv^2P_u
-Ad\int xurP_u-Bd\int x^2vrP_u.
$$
保原 $P_u'=-r^2$ 后，
$$
\int xurP_u=-E_1/2-\int xv^2P_u+E_2,
$$
$$
\int x^2vrP_u=-\int xv^2P_u+E_3/2.
$$
又 $C/2+A+B=0$，因此这整组准确收为
$$
dA E_1/2-dA E_2-dB E_3/2.
\tag{8}
$$

全部 $B_u$ 项准确是
$$
-\frac{eC}{2}\int(x^2r^2+2v^2)B_u
=\frac{eC}{2}E_8-\frac{eC}{2}\mu_1\mu_2.
\tag{9}
$$
(9)保了 $B_u,C_u$ 的原左值；这里只因 whole legal $q$ 的三矩零，
最后一项才为零。它不对每个实微包分别删掉。

合并(4)—(9)及剩余 local 项，得到完整表
$$
\boxed{
\begin{aligned}
K_{ZZ,2}(q)={}&
\frac{d(d-2e)}2E_1+d(8e-d)E_2
+\left(\frac{d^2}{4}-\frac{7de}{2}+12e^2\right)E_3\\
&-3deE_4+2e(d-3e)E_5
+\frac{e(5e-d)}4E_6\\
&+\frac{(d+4e)(d+6e)}{12}E_7
+\frac{-d^2+2de+12e^2}{4}E_8.
\end{aligned}
}
\tag{10}
$$
这是真实全 self；不是模 $C^2$ 的主项。

## 4. 原面积消元后唯一的局部四次商

定义无除 $x$ 的完整局部泛函
$$
\mathcal O(u)=\int(u'-xu'')^4.
$$
紧总导数 $\int xv^3r=-E_7/4$ 给
$$
\mathcal O(u)=2E_7+6E_3-4E_5+E_6.
\tag{11}
$$

R270/R353 的完整 self 给
$$
S_{LY,0}=E_1-4E_2+3E_3+E_4-\frac43E_5+\frac5{24}E_6,
$$
$$
S_{UY,0}=-E_1+8E_2-9E_3-3E_4
+\frac{16}{3}E_5-\frac{25}{24}E_6-\frac23E_7,
$$
$$
S_{RY,1}=-E_1+4E_2-\frac72E_3-E_4
+\frac53E_5-\frac7{24}E_6-\frac16E_7,
$$
$$
S_{SY,1}=2E_2-E_3-E_4+E_5-\frac5{24}E_6+\frac12E_8
\tag{12}
$$
于 whole legal $q$；最后一式的 nonlegal $-\mu_1\mu_2/2$ 已按原范围保留至三矩施加以后。

逐系数代(10)—(12)，得到一个不需预设面积零的合法 self 身份
$$
\boxed{
K_{ZZ,2}
=c_\Omega\mathcal O
+r_\Omega S_{RY,1}
+s_\Omega S_{SY,1}
+z_\Omega S_{ZY,0},
}
\tag{13}
$$
其中
$$
c_\Omega=\frac{(d+e)(d^2+3de+6e^2)}{24e},
$$
$$
r_\Omega=\frac{(d-2e)(d^2+de-3e^2)}{2e},\qquad
s_\Omega=\frac{-d^2+2de+12e^2}{2},
$$
$$
z_\Omega=\frac{(d-2e)(d+3e)}{2e}.
\tag{14}
$$
例如先按 $S_{RY,1}$ 消 $E_1$，再按 $S_{SY,1}$ 消 $E_8$，
最后按 $S_{ZY,0}$ 消 $2E_2-E_4$；
余四系数准确为 $6c_\Omega,-4c_\Omega,c_\Omega,2c_\Omega$，
即(11)。这个消元保的是全部八系数。

现有18面积先给
$$
S_{PY,2}=S_{WY,1}=S_{ZY,0}=0.
$$
R360 的合法身份 $S_{PY,2}=-2(S_{RY,1}+S_{SY,1})$
及 $a-b\ne0$ 再给 $S_{RY,1}=S_{SY,1}=0$。
故
$$
\boxed{K_{ZZ,2}(q)=c_\Omega\mathcal O(q).}
\tag{15}
$$

原范围内 $e<0$、
$d+e=\kappa(9\zeta-1)/(4h_e)<0$，
而 $d^2+3de+6e^2>0$，所以
$$
\boxed{c_\Omega>0.}
\tag{16}
$$
合法复四次式不含共轭，(16)不授 $\operatorname{Re}\mathcal O(q)$ 的符号。

## 5. 完整 ZZ2 的准确两项，及所需新增义务

原 angular odd 已由十二完整副本清除。
R294 的完整四次角分解现在成为
$$
\boxed{
\mathcal Q_{ZZ,2}(\theta)
=\sin^2\theta\,\mathcal Q_{ZZ,2}(\pi/2)
+c_\Omega\sin^2\theta\cos^2\theta\,
\Omega_*,
}
\tag{17}
$$
$$
\Omega_*:=\operatorname{Re}\mathcal O(f+ig).
$$
两种角函数线性独立，且 $c_\Omega\ne0$。
所以完整 $ZZ_2=0$ 恰须
$$
\mathcal Q_{ZZ,2}(\pi/2)=0,\qquad \Omega_*=0.
\tag{18}
$$
前者是包含原 $C^3$ 主项和全部余项的实际 scalar；
后者是一个确切的局部 $C^2$ 四次量。
不能因为前者可用高频根支付，就把后者并入一个未识别的低阶误差。

为避免另造假欠账，本稿同时采用 R349 的原全式
$$
S_{UY,2}(u)=-5S_{LY,2}(u).
$$
R377 的 cubic 身份遂给
$$
K_{YY,0}(q)
=\frac{S_{UY,2}-S_{LY,2}}3
=-\frac{2}{d-5e}S_{ZY,2}(q)=0.
\tag{19}
$$
所以 $YY_0$ 只有一个 $\pi/2$ scalar；它没有第二个独立未付角商。
R380 已将该 scalar 与 R376 十五行联合支付。
以下只在同一点再添(18)的第一行。

## 6. 新主行真实独立，位置次数仍不超过10

原
$$
\alpha_Z=du+(2e-d)xv-3ex^2r,\qquad
\alpha_Y=x^2u-x^3v+x^4r/2,\quad
\alpha_W=2av-2(a+b)xr
$$
给
$$
\mathcal Q_{ZZ,2}(\pi/2)
\equiv_2\sum_i\lambda_i\int x^2\alpha_Z^2(u_i''')^2,
\qquad \lambda_i=-a_i^2(a_i^2-b_i^2).
\tag{20}
$$
完整连续 $C^2$ 余项仍留到实际求根。

沿用 R376 的赋权
$\deg(x,u,v,r)=(1,2,1,0)$。
原十五行的分组维数为 $1,4,5,3,1,1$。
R380 添加 $\alpha_Y^2$ 后，权8的两行
$\alpha_Y^2,x^2\alpha_Z\alpha_Y$ 独立：
约去非零多项式 $\alpha_Y$，
在 $(x^2u,x^4r)$ 上的 determinant 为 $-(d+6e)/2\ne0$。

现在新 $x^2\alpha_Z^2$ 位于权6。
原该组是
$$
x^2\alpha_P\alpha_Y,\qquad
\alpha_Z\alpha_Y,\qquad
x\alpha_W\alpha_Y,\qquad \alpha_P=-2r.
$$
从新行减去
$$
d\,\alpha_Z\alpha_Y+\frac{de}{a}\,x\alpha_W\alpha_Y.
$$
$x^2u^2$ 与 $x^3uv$ 准确消去，而余下 $x^4v^2$ 系数是
$$
\boxed{4e^2\ne0.}
\tag{21}
$$
原剩下的 $x^2\alpha_P\alpha_Y$ 没有 $v^2$ 项。
因此新的十七行完整主多项式独立；权分组现在是
$$
1+4+5+4+2+1=17.
\tag{22}
$$
新行的实际位置次数为6，最大次数仍由原 $YY_2$ 的10给出，
没有超过十二点正 kernel 的范围。

## 7. 同一有限观察、17个真实形状与204列正锥

这里使用 R376 的有限 jet 证明，不默认任意母都 regular。

先保全部真实 copy 偏移 $d_\nu$ 和正权 $\omega_\nu$。
对全偶主多项式使用
$$
\mathscr A p(y,u,v,r)
=\frac12\sum_\nu\omega_\nu
\{p(y+d_\nu,u,v,r)+p(y-d_\nu,u,v,r)\}.
$$
它在 $x$ 次数至多10上是对角元
$\sum_\nu\omega_\nu>0$ 的可逆三角算子。
所以(22)的十七行在真实 copy 平均后仍独立。

在 $0<y<1/2,U>0,R>0,V\in\mathbb R$ 的开放集上，选十七个
两两不同 $y$ 的实际二阶 jet 点值，使评价矩阵非零。
以 $\psi=\exp[-1/(1-y^2)]$ 的偶 Hermite prefactor 实现这些点值，
再作一次有限偶多项式逼近，得到正见证 $\psi P^\dagger$。

沿它与原
$$
\mathcal F_{\rm new}
=(\mathcal F_\star,\ 
\mathfrak j,\mathfrak k\text{ 的全部真实平移系数})
\tag{23}
$$
最大秩母的有限多项式直线，避开固定最大 minor 的有限零点。
因此同一个 $u_0=\psi P_0$ 同时有真最大 minor、全区正 prefactor 和十七点评价见证。
选十七个足够窄但有限的偶 cutoff，再以 $\psi$ 偶多项式逼近，保全部积分列的非零 determinant。

每个形状用原一个互异层的十二个交替索引
$$
0,1,33,34,49,50,65,66,81,82,97,98.
$$
十七层在原2048层中实际存在。
对每组递增真实位置 $X_i$，
$$
\beta_i=\prod_{k\ne i}(X_i-X_k)^{-1},\qquad
\beta_i/\lambda_i>0.
$$
每个主行的位置多项式次数不超过10，故每组准确有严格正 kernel。
若行 covector 消灭全部204列，它在每组的十二个真点消失，故对应十次多项式恒零；
再在其形式 $X=0$ 用十七点积分 minor，便迫 covector 为零。
于是
$$
\boxed{
\operatorname{rank}=17,\quad
\ker\cap\mathbb R_{>0}^{204}\ne\varnothing,\quad
\operatorname{cone}_+=\mathbb R^{17}.
}
\tag{24}
$$
每列的原副本权、镜像因子、静态四次幅度与频率平方平均 $1/2$ 都保留。
此处没有科学枚举，也没有将带符号 span 冒成正幅几何。

## 8. 一个有限 N 支付全部十七个实际 scalar

从 R376/R380 最后控制器以前的同一实际入口开始。
原弱核心、补矩、宽 cutoff、全部旧宏块和负 $\Psi$ 储备先固定；
按前节选择全部末控制器参数，再以静态正幅支付 $\Psi$。
不在一个已经冻结的十六行根上任意另改 profile。

对选中实际微包使用
$$
u_{N,z}
=u_0+N^{-3}z\chi_\alpha\cos Ny+\sum_\ell a_\ell(N,z)e_\ell,
\qquad
\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0).
\tag{25}
$$
最大 minor、局部常秩以及原 $O(N^{-1})$ 的 $C^2$ 与参数一导控制不变。
全部真尾和连续 $C^2$ 项留在完整目标里。

十七个实际目标为
$$
\begin{aligned}
\mathbf G_N=(&
\mathcal Q_{PP,0},F_0,F_1,F_2,
\mathcal Q_{PZ,2},\mathcal Q_{PY,0},\mathcal Q_{PY,2},
\mathcal Q_{ZW,1},\mathcal Q_{ZZ,0},\\
&\mathcal Q_{WW,0},\mathcal Q_{WW,2},
\mathcal Q_{ZY,2},\mathcal Q_{YY,2},
\mathcal Q_{ZY,0},\mathcal Q_{WY,1},
\mathcal Q_{YY,0},\mathcal Q_{ZZ,2})(\pi/2).
\end{aligned}
\tag{26}
$$
同 R285/R376 的完整分裂给
$$
\mathbf G_N(\mathbf z)
=\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1)
\tag{27}
$$
于一个先固定的有限正幅盒上一致。
$\mathbf G_{\rm base}$ 包含真实弱 rank-two 部分、其 cross 项、全部原尾、
copy 偏移、Green、原补偿和最后物理位置，不由单微包公式替代。

(24)给全分量严格正的极限平方幅解。
固定17个独立列以外的幅度，Jacobian $2z_iv_i$ 可逆。
所以非退化零的 $C^1$ 稳定性给某个实际有限整数 $N$ 及精确正幅根
$$
\boxed{\mathbf G_N=0.}
\tag{28}
$$
没有把离散 $1/N$ 冒作光滑参数。

式(25)保原面积、$\mathcal T$ 与有限 $C^2$ 观察；$\Psi$、三条 directed 行及原有 $C^3$ 目标由(28)的同一个真实根共同恢复，不能说它们在纤维扰动的每一点已自动不变。所有既付完整对称乘积同点保持。
$YY_0$ 由(19)是真正完整零。
$ZZ_2$ 的整个剩余函数则准确是
$$
\boxed{
\mathcal Q_{ZZ,2}(\theta)
=c_\Omega\Omega_*\sin^2\theta\cos^2\theta.
}
\tag{29}
$$
这里不把(28)称为完整 $ZZ_2$ 已付。

## 9. 原观察纤维已经固定此残量：一个准确有限身份

本节对任意实紧 $u$ 证明，不要求单包三矩为零。
令
$$
\mathscr D_2(u)
=\left.\frac{d^2}{ds^2}S_{ZY,2}(T_su)\right|_{s=0}.
$$
R349 的完整 nonlegal 身份及 R348 的真实中心导数是
$$
S_{UY,2}=-5S_{LY,2},\qquad
\partial_sS_{LY,2}(T_su)
=\frac{S_{UY,1}(T_su)-S_{LY,1}(T_su)}2,
$$
$$
\partial_sS_{LY,1}(T_su)=2S_{LY,0}(T_su),\qquad
\partial_sS_{UY,1}(T_su)=2S_{UY,0}(T_su).
$$
所以
$$
\boxed{
\mathscr D_2=(d-5e)(S_{UY,0}-S_{LY,0}).
}
\tag{30}
$$
这来自完整 self 的实际平移，不能替换成一般 mixed 圆只移动外矩权。

联立 $S_{ZY,0}=dS_{LY,0}+eS_{UY,0}$，得到
$$
S_{LY,0}
=\frac{S_{ZY,0}-e\mathscr D_2/(d-5e)}{d+e}.
\tag{31}
$$
另一方面，R360 的真 nonlegal 式是
$$
S_{PY,2}=-2S_{RY,1}-2S_{SY,1}-\mu_1\mu_2.
$$
故
$$
S_{RY,1}
=\frac{S_{WY,1}+\frac b2(S_{PY,2}+\mu_1\mu_2)}{a-b}.
\tag{32}
$$
R353 的完整 self 还给
$$
S_{RY,1}=-S_{LY,0}-\frac1{12}\mathcal O(u).
$$
因此
$$
\boxed{
\mathcal O(u)=-12\left[
\frac{S_{WY,1}+\frac b2(S_{PY,2}+\mu_1\mu_2)}{a-b}
+\frac{S_{ZY,0}-e\mathscr D_2/(d-5e)}{d+e}
\right].
}
\tag{33}
$$
所有分母在(1)的范围非零。

式(33)含真实 $\mu_1\mu_2$ 与全部 self；它不是只对 legal 复 q 的关系。
再把 $u$ 换成 $T_tu$，其两边都是固定有限度的真实平移多项式。
原 $\mathcal F_\star$ 已包含这些 Gaussian self 的全部平移系数及三个母矩，
所以它准确决定 $\mathcal O(T_tu)$ 的全部系数。
无需新增一个未支付的纤维假设。

## 10. 为何当前末控制器不能消掉真实弱基线

在不交微包上，局部四次式准确相加：
$$
\operatorname{Re}\mathcal O\!\left(\sum_i(a_i+ib_i)u_i\right)
=\sum_i\operatorname{Re}(a_i+ib_i)^4\,\mathcal O(u_i).
\tag{34}
$$
原末 equal-background 编码满足
$$
\operatorname{Re}(a_i+ib_i)^4
=R_i^2-4T_i^2=\frac{7B}{2}R_i,\qquad
\sum_iR_i t_i^k=0\quad(0\le k\le10).
$$
而 $\mathcal O(T_tu_0)$ 的 $t$ 次数至多4。
所以一个共同母的每个完整末模板的(34)本来准确为零；
全部真实平移、正四次幅及空间镜像继续保零。

之后即使不同微包使用不同有限振荡幅度，它们仍由(25)保持同一
$\mathcal F_{\rm new}$ 数据。式(33)逐包保持全部实际
$\mathcal O(T_tu_i)$，故这个末模板的总(34)仍准确为零。
更换共同最大秩母、增加同类 $\chi$、位置或有限频率，也不改变这一事实。

因此(29)中的 $\Omega_*$ 恰是此前固定弱核与旧宏模块的完整真实值。
本稿既没有证明它非零，也没有证明它已为零；
但准确证明了**当前末端同纤维机制对它没有响应**。
若该值未零，必须在更早的真实 profile／布局层改变这一基线并重新保旧面积，
不能只把 $\mathcal O$ 添入观察映射，或继续增加高频主列来宣称支付。

## 11. 新结论与后续范围

所有有限位置、复制权和末母从起点选择，根后不再整体平移。
$h_e$ 的非零共同行因子可先归一；在所有正负支撑包络确定后，
再按 R354 选择新的合法物理区间、足够大的 $\omega$ 下界和初始小 $h_e$，
安装真实闭 hook 与共振保护芽。
不继承另一条几何的 wholeE、Morse 或全 period。

本稿新增的完整结果是：

1. $ZZ_2$ 的 whole legal self 精确为(13)，在原18面积下只剩(15)这个明确局部四次商。
2. 原同一点有限控制器可扩为17个实际目标、204个正幅列，在一个有限 $N$ 上支付全部 $\pi/2$ scalar，并保持所有既付完整角函数。
3. 全部对称 Gaussian 外矩此后只剩(29)；完整二层支付在这些既有条件下，准确归结为 $\Omega_*=0$。
4. 原单包观察纤维已经固定 $\mathcal O$，现末模板对弱基线的该残量严格无响应，见(33)—(34)。

最后一条只限定当前控制器，绝不是所有弱圆或所有真实几何的刚性定理。
真实 $\Omega_*$ 的低层支付仍须新构造；原零／一 history、
canonical 第四 period、平台／退化通量／端芽、整条路径 ruling
和同一 gauge 的 joint 条件也仍未由本稿支付。
