# R368：两个真实 cubic 恒等与七行有限频率根支付完整 P–Y 对称乘积

日期：2026-11-15。**完整有限纸面证明；未运行求积、符号程序、参数扫描、人工测试或研究计算。**

当前同一个全偶真实弱圆已沿 R360/R361/R364 保持全部18个反对称 Gaussian 外矩，并支付完整 $P^2,PW,PZ$ 对称乘积、$\Psi$ 和原三条 directed 行。本稿处理 $PY$。

这个 pair 的两个剩余外矩有比一般 corrected-self 更强的原式：$F_{P,0}\equiv0$ 与 $F_{Y,2}\equiv0$，结合已付面积，直接把整个对称外矩化为对真紧 $D$ 的线性读出。因此本稿不需要假设任何新 $C^2$ 角商已由旧纤维固定。两个实际 $\pi/2$ 值与既有五行组成真正七维主锥，同一个有限 $N$ 的精确根共同支付它们。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R291](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R360](R360-complete-positive-negative-second-self-and-six-dimensional-middle-cone.md)、
[R361](R361-even-weak-circles-and-three-oscillation-shapes-pay-the-negative-three-square.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)。

## 1. 同一个对象及原规范

继续采用
$$
P=\Phi_{r_0},\qquad
W=aR+bS,\qquad Z=dL+eU,\qquad Y=\Phi_{p_2},
$$
和原小共振范围 $0<\kappa^2<1/100$。$a,d,e$ 都非零；$W,Z$ 的共同 $h_e$ 因子仍按 R354 最后安装的规范处理。

令
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi.
$$
$f,g$ 为原全偶实紧 profiles。保真实三矩圆
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0,
\tag{1}
$$
弱单 hook、非零 derivative rank-two 开段及完整第二／第三 range。
$D$ 的三个原矩为零，原二次输出
$$
PD,\quad YD
\tag{2}
$$
因此在两侧 collar 真为零。没有把单包 $P(u,u)$ 或 $Y(u,u)$ 的尾设成零。

normalized 对称外矩与面积分别为
$$
\mathcal Q_{PY,j}
=-I_j(PD,YD)+I_j\{\phi,P(\phi,YD)+Y(\phi,PD)\},
$$
$$
\mathcal A_j=I_j\{\phi,[P,Y](\phi;D)\}.
\tag{3}
$$
当前三个 $\mathcal A_j$ 已对所有相位为零。
$I_2(u,v)=\int(x^2u''v''+2u'v')$，两个项始终保留。

原 R361/R364 的末端目标是
$$
(\mathcal Q_{PP,0},F_0,F_1,F_2,\mathcal Q_{PZ,2})(\pi/2),
\tag{4}
$$
而 $PZ$ 的额外角商
$$
\mathcal T=
\operatorname{Re}\{\mathfrak k(f+ig)-\rho_\kappa\mathfrak j(f+ig)\}=0
\tag{5}
$$
已先通过真实低层正锥支付，并由 R364 的显式新 $C^2$ 纤维保持。
本稿不会把(5)或任何其他新角商当作原先未经证明的自动条件。

## 2. 第一个原 cubic 恒等不要求单包合法

对任意紧 $u$，写 $v=u',r=u''$。
$P(u,u)=J(r^2)$ 给
$$
F_{P,0}(u)=I_0\{u,P(u,u)\}
=-2\int r^2r'=0.
\tag{6}
$$
这个恒等不要求 $I_0(u,u)=0$，也不要求 $P(u,u)$ 左尾为零。

对两个真正紧的输入 $u,w$，沿紧族 $u+tw$ 微分(6)，得到
$$
\boxed{
2I_0\{u,P(u,w)\}
=-I_0\{w,P(u,u)\}.
}
\tag{7}
$$
式(7)右侧仍保完整 $P(u,u)$。本稿只对(2)这样的真紧 $w$ 使用变分，不沿 nonlegal 带尾方向偷套公式。

## 3. 第二个原 cubic 恒等跨负轴仍准确

R291 已证明 $F_{Y,2}(u)=0$。为适用 R354 的正负支撑，这里直接给无 $u/x$ 除法的原式核对。

设
$$
J_2=J(x^2r^2+2v^2),
$$
$$
Y(u,u)
=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2J_2}{4}.
\tag{8}
$$
它的左尾一般为 $-x^2I_2(u,u)/4$，本节不删此尾。
完整一导为
$$
Y'=-u^2+x^2ur-x^3vr+\frac{x^4r^2}{4}-\frac{xJ_2}{2}.
\tag{9}
$$
二导的线性 $r'$ 部分为
$(x^2u-x^3v+x^4r/2)r'$，其余项是
$$
-2uv+2x(u-xv)r-\frac{J_2}{2}
+\frac{x^3r^2}{2}+xv^2.
$$

代 $I_2(u,Yu^2)$，三项含 $r'$ 的积分准确收为
$$
\int\left\{
-2x^3ur^2+2x^4vr^2-\frac{x^5r^3}{2}
\right\}.
$$
与完整低阶项合并后，余下
$$
\int\left\{
\frac{x^4vr^2}{2}-x^3v^2r-2u^2v
-\frac12(x^2v)'J_2
\right\}.
$$
最后的真实 primitive 经 $J_2'=-(x^2r^2+2v^2)$ 及紧 outer $v$ 的零端值，变成
$$
-\frac12\int x^4vr^2-\int x^2v^3.
$$
于是全部积分等于
$$
-\frac13\int(x^3v^3)'-\frac23\int(u^3)'=0.
$$
因此
$$
\boxed{F_{Y,2}(u):=I_2\{u,Y(u,u)\}=0}
\tag{10}
$$
对任意实坐标区间中的紧 $u$ 成立，不要求区间避开 $x=0$，也不需要单包的二次矩为零。

对真正紧的 $u,w$ 作同一合法变分，得到
$$
\boxed{
2I_2\{u,Y(u,w)\}
=-I_2\{w,Y(u,u)\}.
}
\tag{11}
$$
这就是 R291 的准确原关系，所有原尾仍在。

## 4. 两个整圆公式；无需新增未知 C² 角商

在(7)取 $u=\phi,w=YD$，在(11)取 $u=\phi,w=PD$。
两个 $w$ 的真正紧性均由(1)—(2)支付。

注意
$$
I_j\{\phi,P(\phi,YD)+Y(\phi,PD)\}
=2I_j\{\phi,P(\phi,YD)\}-\mathcal A_j,
$$
也等于
$2I_j\{\phi,Y(\phi,PD)\}+\mathcal A_j$。
代(3)，准确得到
$$
\boxed{
\mathcal Q_{PY,0}
=-I_0\{P(f,f),YD\}-\mathcal A_0,
}
\tag{12}
$$
$$
\boxed{
\mathcal Q_{PY,2}
=-I_2\{Y(f,f),PD\}+\mathcal A_2.
}
\tag{13}
$$
这是原 whole mixed 式，不是 diagonal 主项。
$P(f,f)$ 的真实常尾、$Y(f,f)$ 的真实二次尾都在右侧；紧的是 $PD,YD$，不能将两类场混同。

当前已付 $\mathcal A_0=\mathcal A_2=0$，故两外矩均**准确线性于 $D$**。
因为
$$
D=\sin^2\theta\,(f^2-g^2)
-2\sin\theta\cos\theta\,fg,
$$
(12)—(13)只含 $\sin^2\theta$ 与 $\sin\theta\cos\theta$ 两个相位系数。
原十二完整副本准确清掉后一项，所以
$$
\boxed{
\mathcal Q_{PY,j}(\theta)
=\sin^2\theta\,\mathcal Q_{PY,j}(\pi/2)
\quad(j=0,2).
}
\tag{14}
$$
原平移次数仍不超过 R285/R294 的十次界；完整副本和正四次权均保持。

等价地，若按 R294 额外角项记号，
对三复矩零的 $q=f+ig$ 有
$$
K_{PY,0}(q)=-\frac12S_{PY,0}(q),\qquad
K_{PY,2}(q)=+\frac12S_{PY,2}(q).
$$
面积零迫两者为零。这个结论来自(6)、(10)的完整原恒等，**不是**说原 $\mathcal F_{\rm new}$ 自然固定一切未知二阶余项。

$PY$ 第1矩由 R361 的真实反射律直接为零：
$\epsilon_P\epsilon_Y(-1)^1=-1$，而当前 $f,g$ 全偶。
因此只需联合支付(14)的两个实际 scalar，便支付整个 $PY$ 乘积。

## 5. 新两行的完整主项与真实余项

仍只在末端强控制器的真实 rank-one 微包内扰动，弱核和所有此前宏块固定。
写
$$
f_i=a_i u_i,\quad g_i=b_i u_i,\quad
\lambda_i=-a_i^2(a_i^2-b_i^2),\quad
v=u_i',\ r=u_i'',\ t=u_i'''.
$$
原二导主系数是
$$
\alpha_P=-2r,\qquad
\alpha_Y=x^2u-x^3v+\frac{x^4r}{2}.
$$
R285 的保真尾分裂因此给
$$
\mathcal Q_{PY,0}(\pi/2)
\equiv_2
\sum_i\lambda_i\int
\{-2x^2ur+2x^3vr-x^4r^2\}\,t^2,
\tag{15}
$$
$$
\mathcal Q_{PY,2}(\pi/2)
\equiv_2
\sum_i\lambda_i\int
\{-2x^4ur+2x^5vr-x^6r^2\}\,t^2.
\tag{16}
$$
$\equiv_2$ 表示相差一个实际连续 $C^2$ 多项式泛函，含全部 Green、原尾及低项；没有把它删掉。
特别(16)原 $I_2$ 的 $2X'Y'$ 确在该余项中。

旧 $PZ,2$ 行的 principal 是
$$
\sum_i\lambda_i\int
\{-2dx^2ur+2(d-2e)x^3vr+6ex^4r^2\}\,t^2.
$$
所以作一个固定可逆行变换
$$
\mathcal R_{\rm new}
=\mathcal Q_{PZ,2}+6e\,\mathcal Q_{PY,0},
$$
其完整 principal 准确为
$$
\sum_i\lambda_i\int
\{-2(d+6e)x^2ur+2(d+4e)x^3vr\}\,t^2.
\tag{17}
$$
(17)只用来证明主列秩；有限频率根仍评价全部七个完整原函数，包括该行变换下的全部实际低阶基线。

## 6. 同一母、同三个 χ 的七维实际主空间

采用 R361/R364 从起点选出的同一个最大秩正解析母 $u_0$。
三个真实偶形状 $\chi_\alpha$ 满足下列三列独立：
$$
R_\alpha=\int r_0^2\chi_\alpha^2>0,\qquad
V_\alpha=\int yv_0r_0\chi_\alpha^2,\qquad
U_\alpha=\int u_0r_0\chi_\alpha^2.
\tag{18}
$$
其存在已由明确 finite-jet 条件
$$
\Delta_{\rm jet}
=\frac{-r^2r_2+2ur_2^2-ur r_4}{24r^3}\ne0
$$
和正见证 $\psi e(1+3y^2/2+2y^4+47y^6/12)$ 的值 $-30$ 支付。
与任意有限初选 $C^2$ 映射的最大 minor 在同一母上相容，仍用原多项式直线与有限根论证；不假设任意母函数 regular。

为核七行秩，先用 R361 的非退化四行变换，将旧四目标写成
$$
(H_0,H_a,H_b,H_d)
=\left(\int r^2t^2,\int x^2r^2t^2,
\int xvr t^2,\int ur t^2\right).
$$
再用(17)，七个 principal 行可换为
$$
(H_0,H_a,H_b,H_d,\
\mathcal Q_{PY,0},\mathcal R_{\rm new},\mathcal Q_{PY,2}).
\tag{19}
$$

保全部实际 copy 权 $\omega_\nu>0$ 和偏移 $d_\nu$。
对固定 $\chi_\alpha$，把物理 $x$ 写成 $X+d_\nu+y$ 并积分。
各行是真正位置多项式：

- $\mathcal Q_{PY,2}$ 次数6，最高系数为 $-W_cR_\alpha\ne0$；
- $\mathcal Q_{PY,0}$ 次数4，最高系数亦为 $-W_cR_\alpha$；
- $\mathcal R_{\rm new}$ 因 $u_0r_0$ 偶、$v_0r_0$ 奇，次数至多2，二次系数为
$$
W_cT_\alpha,\qquad
T_\alpha=-2(d+6e)U_\alpha+6(d+4e)V_\alpha;
$$
- $H_a$ 次数2，二次系数为 $W_cR_\alpha$；
- $H_0,H_b,H_d$ 为常向量
$W_c(R_\alpha,V_\alpha,U_\alpha)$。

这里 $W_c=\sum_\nu\omega_\nu>0$。实际 copy 平移产生的所有低次项仍在，未将它们换成同心或均匀理想模型。

先取次数6系数，再取模掉它的次数4系数，获得两个独立方向。
模掉这两个高次方向以后，各 $\chi$ 的二次系数在
$(H_a,\mathcal R_{\rm new})$ 上是
$$
W_c(R_\alpha,T_\alpha).
$$
这些列至少有秩2。否则 $T_\alpha/R_\alpha$ 对三个 $\alpha$ 全同，
会给三个独立向量(18)一个共同线性关系
$$
-\tau R_\alpha+6(d+4e)V_\alpha-2(d+6e)U_\alpha=0.
$$
由(18)满秩，它迫
$\tau=0,d+4e=0,d+6e=0$，从而 $e=0$，与原参数矛盾。

最后模掉上述四个位置方向，常数列仍在
$(H_0,H_b,H_d)$ 上给(18)的秩3。故
$$
\boxed{\text{同一个真实母、三个实际偶 }\chi
\text{ 的联合七行主空间恰为 }\mathbb R^7.}
\tag{20}
$$
这是 $1+1+2+3=7$ 的实际系数证明，不是只看七个被列出的形式。

## 7. 三十六个真实列的严格正核

每个 $\chi_\alpha$ 使用原实际编码中一层的十二个交替位置，
索引仍为
$$
0,1,33,34,49,50,65,66,81,82,97,98.
$$
同名八／十二副本和空间镜像共享一个微包参数。
原实际幅、位置、复制正权一并包含于各列。

七行的位置次数均不超过6。令真实递增位置为 $X_i$，
$$
\beta_i=\frac1{\prod_{k\ne i}(X_i-X_k)}.
$$
原 high/low 交替保证 $\beta_i/\lambda_i>0$。
十二点准确消去次数至多十的多项式，所以每一形状组有严格正 kernel。
三组联合的 span 已由(20)证明为 $\mathbb R^7$。
每组正锥等于其 span，因而
$$
\boxed{
\operatorname{cone}_+(\text{36个真实七行列})=\mathbb R^7,
\qquad\text{并有全部分量严格正的 kernel}.
}
\tag{21}
$$
没有把 signed span 当作正幅可实现性，也没有添负 copies。

## 8. 同一个有限 N 保全部旧门并精确支付新两行

取 R364 在新低层角商已零、全部18面积为零而最后强控制器尚未安装的实际入口。
弱核、宽过渡、补矩、所有旧位置及全部已计入的 residual 都固定。
按 R364 从起点使用
$$
\mathcal F_{\rm new}
=(\mathcal F_\star,\ 
\text{全部 }\mathfrak j,\mathfrak k
\text{ 的真实平移系数}),
\tag{22}
$$
其局部 self 正是有限 $C^2$ 多项式。
该映射保持末强块的全部72面积、quartic $C$ 与新角商(5)的零。
本稿没有为 $PY$ 另加一个未证可保持的角条件：其完整身份已由§2—4支付。

先固定成对反射强控制宏块的实际位置与静态正幅，使 $\Psi$ 准确为零。
然后在每个选中微包作
$$
u_{N,z}
=u_0+N^{-3}z\chi_\alpha\cos Ny
+\sum_\ell a_\ell(N,z)e_\ell,
$$
解原有限维方程
$$
\mathcal F_{\rm new}(u_{N,z})
=\mathcal F_{\rm new}(u_0).
\tag{23}
$$
同一最大 minor 与局部常秩保整个有限映射；
纠正及参数一导在 $C^2$ 为 $O(N^{-1})$，
固定光滑方向的三导贡献也为 $O(N^{-1})$。
有限幅盒先固定，频率后选。

完整七量向量取
$$
\mathbf G_N=
(\mathcal Q_{PP,0},F_0,F_1,F_2,\mathcal Q_{PZ,2},
 \mathcal Q_{PY,0},\mathcal Q_{PY,2})(\pi/2).
$$
所有实际 strong／weak blocks 的真尾保留；R325/R361/R364 的完整跨包加法仍适用。
R285 的原 $C^2$ 余项及高频平均给
$$
\mathbf G_N(\mathbf z)
=\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1)
\tag{24}
$$
在这个有限正幅盒上一致成立。
$\mathbf G_{\rm base}$ 包括弱 rank-two 区、全部新增面积模块、
各完整 copy 的最终位置、原右历史及整个低阶值；
没有在弱核心上套 rank-one 公式。

由(21)，把 $-\mathbf G_{\rm base}$ 表为所有36列严格正的平方幅组合。
选七个独立列、固定其他正幅，极限 Jacobian 为 $2z_i v_i$，可逆。
非退化零在小 $C^1$ 扰动下稳定，故存在一个足够大但**实际有限**的整数 $N$ 及精确正幅根
$$
\boxed{\mathbf G_N=0.}
\tag{25}
$$
这不是 $N=\infty$ 的形式解，也没有把离散 $1/N$ 当作光滑参数。

完整面积及(5)由(23)保持，所以 R364 的 $PZ$ 全角结论保持；
原 $P^2,PW$ 由前五行、面积与反射保持。
本稿(12)—(14)把新两行的零准确提升到全部相位。
空间镜像共享参数，最终 $f,g$ 仍全偶，因此 $PY$ 第1矩为零。
最终同一真实圆满足
$$
\boxed{
\mathcal Q_{PP,j}=\mathcal Q_{PW,j}
=\mathcal Q_{PZ,j}=\mathcal Q_{PY,j}=0,
\qquad j=0,1,2,\quad\text{全部相位}.
}
\tag{26}
$$
原全部18面积、$\Psi$、三条 directed 行、指定一层及完整第三也同时保持。

同一证明还可将最后两行指定为任意固定有限实数 $(\tau_0,\tau_2)$，前五行为零。
(14)给新两函数分别为 $\tau_j\sin^2\theta$。
因此这不是由旧五行自动推出的新零，而是两个真实可联合调节的方向。
共同正归一化的四次因子由固定三矩确定；若指定归一后的值，预先使用这个固定因子即可。

## 9. 选择顺序和未付范围

本稿沿 R364 的实际有限选择，不改变已经计入的低层／中层／高层费用：

1. 固定小 $\kappa$，完成原弱核和所有有限面积、角商模块；保旧18面积与(5)，并留负 $\Psi$。
2. 从起点选(22)的同母最大 minor、正 finite-jet 见证附近的母、三个实际偶 $\chi$ 和有限纠正方向。
3. 固定成对强控制器全部真实 copy、最终位置和静态 $\Psi$ 幅；固定有限正幅盒后，才选同一个足够大有限 $N$ 并解七行。
4. 不在根后平移、重锚或更改共享 copy。全部 profiles 与正负支撑确定后，按 R354 选新共同物理区间、足够大的 $\omega$ 下界及初始小 $h_e$，真实安装闭 hook 与共振保护芽。

新增两行只涉及原 $P,Y$ 的固定非零 Gaussian 系数；
与原 $W,Z$ 的行缩放一起，最终 $h_e$ 的初选不改变零等式。
不将其当作一个任意冻结旧窄区间或旧几何上的免费变形。

当前剩余的反射允许对称位置为
$$
Z^2:0,2;\quad ZW:1;\quad ZY:0,2;\quad
W^2:0,2;\quad WY:1;\quad Y^2:0,2.
$$
共10个完整角函数位置，不是独立 rank，也不是已经可任意指定的十个 scalar。
尤其 $Z^2$ 等 pair 的额外 $C^2$ 角项不能仿照本稿无证删除；
本稿选择 $PY$ 正是因为(6)、(10)给两个原准确恒等。

其余零／一 Gaussian history 函数、整条闭路径、canonical 第四 period、
平台／退化通量／端芽与同一个 gauge 的 joint 条件仍未由(26)支付。
当前新几何也不继承另一几何的 wholeE、Morse 或全 period。
本稿完成的是整个 $PY$ 对称乘积与既有三乘积、原反对称面积和指定一层的真实同点联合支付。
