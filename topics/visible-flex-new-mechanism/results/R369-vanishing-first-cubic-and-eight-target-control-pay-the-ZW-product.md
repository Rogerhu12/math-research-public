# R369：零 cubic 第1矩与八行有限频率根支付完整 Z–W 对称乘积

日期：2026-11-15。**完整有限纸面证明；未运行求积、符号程序、参数扫描、人工测试或研究计算。**

R368 在当前同一个全偶真实弱圆构造中，已联合支付完整 $P^2,PW,PZ,PY$ 对称乘积，全部18个反对称 Gaussian 外矩、$\Psi$ 和原三条 directed 行。本稿继续处理 $ZW$。

原算子给一个准确恒等：$F_{Z,1}(u)=I_1(u,Z(u,u))\equiv0$，对任意紧 $u$ 成立，不要求单包三矩为零。结合当前已付的 $ZW$ 面积，它把完整第1对称矩化为对真紧 $D$ 的线性读出。因此没有新的未知 $C^2$ 角商需要猜测。本稿把该唯一实际 scalar 与既有七行组成八维真实主锥，以四种偶振荡形状、48个实际正幅列和一个有限频率精确根共同支付。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R361](R361-even-weak-circles-and-three-oscillation-shapes-pay-the-negative-three-square.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R368](R368-two-exact-cubic-identities-and-seven-target-control-pay-the-PY-product.md)。

## 1. 同一个弱圆与原规范

固定原小共振范围
$$
0<\kappa^2<1/100,\qquad \kappa>0.
$$
仍用
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU.
$$
写 $\zeta=\kappa^2$，实际系数为
$$
a=-\frac{51\zeta^2+2\zeta+8}{64h_e^2},\qquad
b=-\frac{34\zeta^2+8\zeta}{64h_e^2},
$$
$$
d=\frac{6\kappa\zeta}{h_e},\qquad
e=-\frac{\kappa(15\zeta+1)}{4h_e}.
\tag{1}
$$
特别
$$
a\ne0,\quad d\ne0,\qquad
d+6e=-\frac{3\kappa(11\zeta+1)}{2h_e}\ne0,\qquad
2e-d=-\frac{\kappa(27\zeta+1)}{2h_e}\ne0.
\tag{2}
$$

令
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi.
$$
$f,g$ 是原全偶实紧 profiles，保真实三矩圆
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0,
\tag{3}
$$
弱单 hook、非零 derivative rank-two 核和完整第二／第三 range。
(3)保证 $PD,WD,ZD,YD$ 的三种真实左尾均为零；紧的是整个 $D$ 的输出，不能据此把单包输出的尾删掉。

normalized 对称外矩与相应面积为
$$
\mathcal Q_{ZW,j}
=-I_j(ZD,WD)
+I_j\{\phi,Z(\phi,WD)+W(\phi,ZD)\},
$$
$$
\mathcal A_{ZW,j}
=I_j\{\phi,[Z,W](\phi;D)\}.
\tag{4}
$$
全部 $\mathcal A_{ZW,j}$ 已对所有相位为零。
这里 $I_0(u,v)=\int u''v''$，
$I_1(u,v)=\int xu''v''$，
$I_2(u,v)=\int(x^2u''v''+2u'v')$；原 $I_2$ 的两项始终共同保留。

本稿从 R364/R368 最后控制器以前的实际入口选择末控制器，最后同时恢复全部八行。它不声称可以任意改变一份已经冻结的母函数而免费保持旧门。

## 2. 原 L 的 cubic 第1矩：真常尾准确抵消

对任意实紧 $u$，写
$$
v=u',\qquad r=u'',\qquad P_u=J(r^2),\qquad Jq(x)=\int_x^{r_I}q(t)\,dt.
$$
原二导为
$$
(Lu^2)''=(u-xv)r'-\frac{xr^2+P_u}{2}.
\tag{5}
$$
$P_u$ 在左侧一般有非零常尾，本节不删它。

第一项准确分部积分：
$$
\begin{aligned}
\int xr(u-xv)r'
&=-\frac12\int(u-xv-x^2r)r^2\\
&=-\frac12\int ur^2+\frac12\int xvr^2
+\frac12\int x^2r^3.
\end{aligned}
$$
故
$$
F_{L,1}(u):=I_1(u,Lu^2)
=-\frac12\int ur^2+\frac12\int xvr^2
-\frac12\int xrP_u.
\tag{6}
$$
真实 primitive 满足 $P_u'=-r^2$。只用紧 outer $u,v$ 的端值，得到
$$
\begin{aligned}
\int xrP_u
&=-\int vP_u+\int xvr^2\\
&=-\int ur^2+\int xvr^2.
\end{aligned}
\tag{7}
$$
第一步来自 $r=v'$，第二步来自 $v=u'$。
两次边项都是紧 outer 乘完整 $P_u$，所以准确为零；没有使用 $P_u$ 左常数为零。

代(6)便得
$$
\boxed{F_{L,1}(u)=0.}
\tag{8}
$$
这是对任意紧 $u$ 的原恒等，不是仅对满足三复矩的输入成立。

## 3. 原 U 的 cubic 第1矩及合法紧变分

原另一二导为
$$
(Uu^2)''
=(2xv-3x^2r)r'+2vr-2xr^2.
\tag{9}
$$
因此
$$
F_{U,1}(u)
=\int(2x^2vr-3x^3r^2)r'
+2\int xvr^2-2\int x^2r^3.
$$
两个含 $r'$ 项分别通过 $(r^2)'$、$(r^3)'$ 积分，合计准确为
$$
-2\int xvr^2+2\int x^2r^3.
$$
故
$$
\boxed{F_{U,1}(u)=0,\qquad F_{Z,1}(u)=dF_{L,1}+eF_{U,1}=0.}
\tag{10}
$$

对真正紧的两个输入 $u,w$，沿紧族 $u+tw$ 微分(10)，得到
$$
\boxed{
2I_1\{u,Z(u,w)\}=-I_1\{w,Z(u,u)\}.
}
\tag{11}
$$
(11)右侧保完整 $Z(u,u)$ 的左尾。
本稿只对真正紧的 $w$ 使用此式，不沿一个 nonlegal 带尾方向套用紧域变分。

所有式(5)—(11)均无 $1/x$，因此在 R354 的正负支撑物理区间上同样成立。

## 4. 完整 ZW 全角式；一个实际 scalar 足够

由(3)，$w=WD$ 真紧。取(11)中的 $u=\phi,w=WD$。
同时
$$
I_1\{\phi,Z(\phi,WD)+W(\phi,ZD)\}
=2I_1\{\phi,Z(\phi,WD)\}-\mathcal A_{ZW,1}.
$$
代(4)并合并 $ZD+Z(\phi,\phi)=Z(f,f)$，得到
$$
\boxed{
\mathcal Q_{ZW,1}
=-I_1\{Z(f,f),WD\}-\mathcal A_{ZW,1}.
}
\tag{12}
$$
式(12)是整个 mixed 原式。
$Z(f,f)$ 的二次／一次左尾仍在；只有 $WD$ 的紧性来自整个三矩零。

当前 $\mathcal A_{ZW,1}=0$，于是(12)准确线性于 $D$。
而
$$
D=\sin^2\theta\,(f^2-g^2)-2\sin\theta\cos\theta\,fg.
$$
原十二完整副本准确清除后一相位系数，其真实平移次数仍在原十次界内，全部复制正权与最终位置不变。因此
$$
\boxed{
\mathcal Q_{ZW,1}(\theta)
=\sin^2\theta\,\mathcal Q_{ZW,1}(\pi/2).
}
\tag{13}
$$
也可在 R294 的角商记号下，用合法复输入 $q=f+ig$ 写
$K_{ZW,1}(q)=-S_{ZW,1}(q)/2$。
已付面积使该角商为零；这个结论由(10)的完整原恒等给出，不能表述为旧纤维自然固定所有未知 $C^2$ 余项。

原真实反射律给 $\epsilon_Z=-1,\epsilon_W=1$。
因 $f,g$ 全偶，
$$
\mathcal Q_{ZW,0}=\mathcal Q_{ZW,2}=0.
\tag{14}
$$
这里使用 R361 的 whole 反射律及真紧 $D$，并非对单包带尾输出假设简单奇偶。
所以只要再支付(13)的一个实际值，整个 $ZW$ 乘积便完成。

## 5. 新行的完整主项与两个准确行变换

仍只在末端强控制器的实际 rank-one 微包内扰动。
弱 rank-two 核与此前宏块全部固定。写
$$
f_i=a_i u_i,\quad g_i=b_i u_i,\quad
\lambda_i=-a_i^2(a_i^2-b_i^2),
\quad v=u_i',\ r=u_i'',\ t=u_i'''.
$$
原二导主系数为
$$
\alpha_P=-2r,\qquad
\alpha_Z=du+(2e-d)xv-3ex^2r,\qquad
\alpha_W=2av-2(a+b)xr.
\tag{15}
$$
R285 保真实尾的分裂给
$$
\mathcal Q_{ZW,1}(\pi/2)
\equiv_2\sum_i\lambda_i\int x\alpha_Z\alpha_W\,t^2.
\tag{16}
$$
$\equiv_2$ 表示相差一个完整连续 $C^2$ 多项式泛函，含 Green、原右历史及所有低阶项；本稿不会把它删掉。

从 R368 保留
$$
\mathcal R_P=\mathcal Q_{PZ,2}+6e\,\mathcal Q_{PY,0},
$$
其 principal 为
$$
\sum_i\lambda_i\int
\{-2(d+6e)x^2ur+2(d+4e)x^3vr\}\,t^2.
\tag{17}
$$
新增另一个固定行变换
$$
\mathcal R_Z=\mathcal Q_{ZW,1}-(a+b)\mathcal Q_{PZ,2}.
$$
将(15)逐项相乘，$x^2ur$ 与 $x^4r^2$ 准确抵消，得到
$$
\boxed{
\mathcal R_Z\equiv_2
2a\sum_i\lambda_i\int
\{dxuv+(2e-d)x^2v^2-3ex^3vr\}\,t^2.
}
\tag{18}
$$
(17)—(18)只用于识别主列的秩。
最后有限频率根仍使用全部八个完整原函数，所有行变换带来的实际 $C^2$ 余项留在基线中。

R361 原四目标
$(\mathcal Q_{PP,0},F_0,F_1,F_2)$
的 principal 在
$$
(H_0,H_a,H_b,H_d)
=\left(\int r^2t^2,\int x^2r^2t^2,
\int xvr t^2,\int ur t^2\right)
$$
上的矩阵是
$$
\begin{pmatrix}
4&0&0&0\\
0&4&0&0\\
0&4(a+b)&-4a&0\\
0&6e&2d-4e&-2d
\end{pmatrix},
\qquad\det=128ad\ne0.
\tag{19}
$$
故八个主行可等价换成
$$
(H_0,H_a,H_b,H_d,\mathcal Q_{PY,0},
\mathcal R_P,\mathcal Q_{PY,2},\mathcal R_Z).
\tag{20}
$$

## 6. 四种 χ 的存在：明确 finite-jet 见证

本稿需要四种实际偶形状，而不是把四个积分当自由参数。
对同一个偶母 $u_0$，记
$$
R_\alpha=\int r_0^2\chi_\alpha^2,\quad
V_\alpha=\int yv_0r_0\chi_\alpha^2,\quad
U_\alpha=\int u_0r_0\chi_\alpha^2,\quad
V^{(2)}_\alpha=\int v_0^2\chi_\alpha^2.
\tag{21}
$$
要求四列 $(R_\alpha,V_\alpha,U_\alpha,V^{(2)}_\alpha)$ 满秩4。

先给一个正见证。设
$$
\psi(y)=\exp[-1/(1-y^2)]\quad(|y|<1),
$$
在外延拓为零，并取
$$
u^\dagger(y)=\psi(y)\exp(1)
\left(1+\frac32y^2+2y^4+\frac{47}{12}y^6\right).
\tag{22}
$$
括号在闭支撑上严格为正，且
$$
u^\dagger=1+\frac12y^2+y^6+O(y^8),\quad
v^\dagger=y+6y^5+O(y^7),\quad
r^\dagger=1+30y^4+O(y^6).
$$
在 $r\ne0$ 的小邻域置 $z=y^2$。四个比值函数满足
$$
\frac{yv}{r}=z-24z^3+O(z^4),\qquad
\left(\frac vr\right)^2=z-48z^3+O(z^4),
$$
$$
\frac ur=1+\frac z2-30z^2+b_3z^3+O(z^4).
$$
按列顺序 $(1,yv/r,u/r,(v/r)^2)$，
零至三阶 Taylor 系数矩阵为
$$
\begin{pmatrix}
1&0&1&0\\
0&1&1/2&1\\
0&0&-30&0\\
0&-24&b_3&-48
\end{pmatrix},
\qquad\det=720\ne0.
\tag{23}
$$
未知 $b_3$ 不影响这个子式。

因此可取四个足够小且不同的正 $|y|$，使四个实际点值列独立。
再取分别集中于相应 $\pm y$ 的偶 smooth cutoff；
对有限而足够窄的支撑，(21)仍满秩。
最后用 $\psi$ 乘偶多项式逼近这四个 cutoff，连续性保持严格 minor。
所得 $\chi_\alpha$ 都是固定、真实、光滑的偶函数；不取点质量极限作为最终输入。

## 7. 同一个最大纤维 minor；不假任意母 regular

继续从起点使用 R364 的有限观察映射
$$
\mathcal F_{\rm new}
=(\mathcal F_\star,\ 
\text{全部 }\mathfrak j,\mathfrak k
\text{ 的真实平移系数}).
\tag{24}
$$
它是共同固定支撑偶 $C^2$ 域上的有限多项式映射。
新增两类局部量正是 R364 的角商所需内容；本稿不删它们，也不将其改称旧 $\mathcal F_\star$ 已包含。

令该域上最大微分秩为 $r_*$. 原 $\psi$ 偶多项式类的 $C^2$ 稠密性与导数连续性，给一个此类最大秩母及固定 $\psi$ 偶多项式方向 $e_1,\ldots,e_{r_*}$，实现一个真非零 minor。
将该母与(22)用同类多项式直线连接。该固定 minor 沿直线是一个多项式，在最大秩端不为零，故在任意靠近(22)的区段中只有有限零点。

由此可在(22)附近选同一个实际母 $u_0$，同时满足：

- $\mathcal F_{\rm new}$ 的最大秩 minor 非零；
- 正 prefactor 在闭支撑上严格正；
- $r_0(0)\ne0$，且(23)的有限 jet minor 仍非零。

这是固定有限多项式直线上的选择，不是把 $C^2$ 接近错误地当作高阶 jet 接近。
如果 $r_*=0$，无需纠正方向，仍可直接选择正见证附近的母。

随后按§6在这个 $u_0$ 上选择四个 $\chi_\alpha$。
非零最大 minor 的小邻域中秩恒为 $r_*$；
解其 $r_*$ 个坐标方程便局部保持整个(24)，与 R277/R281/R293 的同母常秩论证相同。
因此 principal 的四列独立与完整纤维的实际纠正是在同一个母上实现。

## 8. 全部真 copy 加权后的八维秩

保全部实际复制正权 $\omega_\nu>0$ 和偏移 $d_\nu$。
在一个未反射分支写物理位置
$$
x=X+d_\nu+y,\qquad W_c=\sum_\nu\omega_\nu>0.
$$
空间镜像按本稿八行的准确 even 反射律贡献同号列，可并入正权；没有删真实负侧位置。

对固定 $\chi_\alpha$，(20)的主列是真正的 $X$ 多项式：

- $\mathcal Q_{PY,2}$ 次数6，最高系数 $-W_cR_\alpha$；
- $\mathcal Q_{PY,0}$ 次数4，最高系数 $-W_cR_\alpha$；
- $H_a$ 次数2，二次系数 $W_cR_\alpha$；
- $\mathcal R_P$ 次数至多2，二次系数为
$$
W_cT_\alpha,\qquad
T_\alpha=-2(d+6e)U_\alpha+6(d+4e)V_\alpha;
$$
- $\mathcal R_Z$ 次数至多2，二次系数为
$$
W_cS_\alpha,\qquad
S_\alpha=2a\{(2e-d)V^{(2)}_\alpha-9eV_\alpha\};
$$
- $H_0,H_b,H_d$ 为常向量
$W_c(R_\alpha,V_\alpha,U_\alpha)$。

$\mathcal R_Z$ 中 $xuv$ 的积分只给常项，因为 $uv$ 奇；
$x^3vr$ 的二次系数为 $3\int yvr\chi_\alpha^2$。
所有偏移造成的一次和常数项仍完整保留。

若一个行 covector 消灭这四组全部位置多项式，先看六次项，迫其 $\mathcal Q_{PY,2}$ 坐标为零；
再看四次项，迫其 $\mathcal Q_{PY,0}$ 坐标为零。
二次项给四个方程
$$
c_aR_\alpha+c_PT_\alpha+c_ZS_\alpha=0.
$$
(21)满秩4，而(2)使 $U_\alpha$、$V^{(2)}_\alpha$ 的系数分别迫
$c_P=c_Z=0$，随后 $c_a=0$。
最后常数项在 $(R_\alpha,V_\alpha,U_\alpha)$ 上满秩3，
迫剩余三个坐标为零。

因此
$$
\boxed{\text{同一母、四个实际偶 }\chi
\text{ 的联合八行主空间为 }\mathbb R^8.}
\tag{25}
$$
该证明明确保所有真实 copy 权和偏移，不用独立指定母积分，也不忽略原低次系数。

## 9. 四十八个实际列的严格正核

每种 $\chi_\alpha$ 使用原实际编码的一层，十二个交替索引为
$$
0,1,33,34,49,50,65,66,81,82,97,98.
$$
四种形状使用四个不同的实际层。
同名八／十二副本及空间镜像共享一个母参数；
实际幅、复制正权和最终位置全部属于相应列。

对每组真实递增位置 $X_i$，令
$$
\beta_i=\frac1{\prod_{k\ne i}(X_i-X_k)}.
$$
这些实际 high/low 索引使 $\beta_i/\lambda_i>0$。
十二点有限差分消去次数至多十的所有多项式，而本稿八行次数均不超过6。
所以每个形状组都有全部分量严格正的 kernel。

另一方面，十二个点上的零多项式因次数至多6必恒零。
由§8的 covector 证明，四组48列的联合 span 为 $\mathbb R^8$。
每组正核使其正锥等于其 span，合并后得到
$$
\boxed{
\operatorname{cone}_+(\text{48个真实八行列})=\mathbb R^8,
\quad\text{且有全部分量严格正的 kernel}.
}
\tag{26}
$$
这里没有负幅、负副本或从 signed span 跳到实际正锥的步骤。

## 10. 同一有限频率的完整八行精确根

采用 R364/R368 的实际入口：弱核和所有旧模块已固定，全部18面积及 R364 的新角商
$$
\mathcal T=\operatorname{Re}
\{\mathfrak k(f+ig)-\rho_\kappa\mathfrak j(f+ig)\}
$$
为零，并留负 $\Psi$ 供最后强控制器支付。
从起点选(24)及§7的同母最大 minor，不在根后更换母形。

先固定末端成对反射强宏块的全部位置和静态正幅，使 $\Psi$ 准确为零。
在各选定微包作
$$
u_{N,z}
=u_0+N^{-3}z\chi_\alpha\cos Ny
+\sum_{\ell=1}^{r_*}a_\ell(N,z)e_\ell,
$$
并解
$$
\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0).
\tag{27}
$$
同一个最大 minor 保整个有限映射。
纠正及参数一导在 $C^2$ 为 $O(N^{-1})$，
固定光滑纠正方向的三导贡献也为 $O(N^{-1})$。
先固定有限正幅盒，后选频率。

全部48列使用相同的实际有限整数 $N$。
完整目标为
$$
\mathbf G_N=
(\mathcal Q_{PP,0},F_0,F_1,F_2,\mathcal Q_{PZ,2},
\mathcal Q_{PY,0},\mathcal Q_{PY,2},\mathcal Q_{ZW,1})(\pi/2).
$$
弱核心上的原 whole mixed 表达式和全部原尾直接放入基线；
不在该 rank-two 区套单微包主式。
R325 的完整 block 加法、R285 的完整 $C^2$ 余项及同频平均给
$$
\mathbf G_N(\mathbf z)
=\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1)
\tag{28}
$$
在固定有限盒上一致成立。$\sin^2Ny$ 的平均 $1/2$ 已包含于实际列 $v_i$ 的共同正因子。

$\mathbf G_{\rm base}$ 保全部 weak／strong 宏块、宽 cutoff、补矩、真实 Green、右历史、copy 权和最终中心。
不同完整 block 的相应 $D$ 各有真三矩零，恢复场和 nested cross 按原完整支持论证相消；
单微包内部的尾则由 R285 原余项保留，未假设其分别紧。

由(26)，选择全部严格正的平方幅，使极限向量等于零。
保一个严格正 kernel 的余量后，选八个独立列并固定其余正幅，
极限 Jacobian 的列为 $2z_iv_i$，可逆。
非退化零在小 $C^1$ 扰动下稳定，故存在一个足够大但实际有限的整数 $N$，使
$$
\boxed{\mathbf G_N=0.}
\tag{29}
$$
不把离散 $1/N$ 当连续光滑参数，也不以无限频率极限替代真实解。

(27)保持末强块全部72面积、quartic $C$ 和 R364 的新局部角商。
因而原三条 directed 行、$\Psi$、完整 $P^2,PW,PZ$ 及 R368 的完整 $PY$ 都保持。
本稿(12)—(14)把第八行的零准确提升为完整 $ZW$ 的三外矩、所有相位为零：
$$
\boxed{
\mathcal Q_{PP,j}=\mathcal Q_{PW,j}
=\mathcal Q_{PZ,j}=\mathcal Q_{PY,j}
=\mathcal Q_{ZW,j}=0,\qquad j=0,1,2.
}
\tag{30}
$$

同一证明还能指定第八行为任意有限实数 $\tau$，前七行为零。
此时准确有 $\mathcal Q_{ZW,1}(\theta)=\tau\sin^2\theta$。
因此该新条件是一个可联合支付的真实方向，不是旧七行的自动推论。

## 11. 有限选择顺序与未付范围

本稿只重选原构造允许的末控制器，不丢已支付的母／copy 费用：

1. 固定小 $\kappa$，完成弱核、全部有限面积和局部角商模块，保18面积与 $\mathcal T=0$，留负 $\Psi$。
2. 从起点选(24)、同母最大 minor、§6的正 finite-jet 见证附近母、四个偶 $\chi$ 及固定纠正方向。
3. 固定成对反射强宏块全部真实位置、复制正权和静态 $\Psi$ 幅；随后固定有限正幅盒，选有限 $N$，解完整八行。
4. 根后不再平移、换锚、更换共享 copy。全部实际支撑确定后，按 R354 选择新共同物理区间、足够大的 $\omega$ 下界和初始小 $h_e$，安装真实闭 hook 与共振保护芽。

$W,Z$ 的共同非零 $h_e$ 行因子不改变零目标；§8的非退化性只要求(2)，所以最终初选 $h_e$ 与这个顺序相容。
这不授任意旧冻结窄区间上的扩域，也不继承另一几何的 wholeE 或 Morse。

当前反射允许但尚未支付的对称位置为
$$
Z^2:0,2;\qquad ZY:0,2;\qquad
W^2:0,2;\qquad WY:1;\qquad Y^2:0,2.
$$
共9个完整角函数位置，不是独立 rank。
特别它们的新 $C^2$ 角商不能由本稿 $F_{Z,1}=0$ 的身份类推删除。

原完整第四 period、平台／退化通量／端芽、其余零／一 Gaussian history、
整条闭路径上的 ruling 与同一个 gauge 的 joint 条件仍未由(30)支付。
本稿完成的是同一最终真实弱圆上，完整 $ZW$ 与既有四个对称乘积、全部18面积、
$\Psi$、三条 directed 行及指定一层／完整第三的联合有限构造。
