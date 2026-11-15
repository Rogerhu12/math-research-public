# R634 — 原 T 伴随的完整单层返回与同单位反射比较

日期：2026-11-15。**状态：已证明。**

本篇把 R628 的原 $W$ 四层返回加强为完整单层两态。关键是对
$C$ 作真实六次平均以后，**整个第一 $W$ 因子仍属于原
$\mathcal S_{72}$**；R601 的两条分离张量各自需要的
$\mathcal S_{288}$ 上界，不是它们准确相减后的最小共同格。
第二态恰为 R465 的原 $\rho_1$ 再作同一 $C$ 平均，故其完整
$W$ 边际仍是原 $6\delta T$，并且第三条真实算术线的五伴随分解
也原样保留。

由此原 $T$ 中央行进入 $E_W$ 的每一层深域。另一方面，在原
$E_Y$ 深管内，两个实际反射观察确有同一个单位域，其中央差的
完整奇次级数首矩准确回到 R621 的原简单极点行，另保三个真补偿。
反射输出尚无原算术身份；本篇不把该差或其中一个补偿置零。

## 1. 同一六变量来源和原规范

沿用 R594、R601、R626、R628 的全部普通射线、固定坏集和规范：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1 .
\tag{1}
$$
$p\ge71$、$p\equiv7\pmod{64}$。R626 的实际符号
$\epsilon_p^2=1$ 保持未知，不另猜一个绝对号。

暂回到六个原独立 sigma 坐标
$(\xi_1,\xi_2,\xi_3,x,c,d)$，写
$$
\rho_0=-\frac1{84}\nu_\sigma^{\otimes6},\quad
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x,\quad
\gamma=3+\omega ,
$$
$$
Y=A+c+2d,\qquad W=A+3\delta c+4d,\qquad
C=(\xi_1-\xi_3+x)/\delta .
\tag{2}
$$
这与 R465 的前四输入先作 CM 缩放的写法完全相同。
在原标准 Hermitian 度量中，$N(C)=1$，且
$C\perp Y,W$。本篇整个来源仍是
$$
\boxed{\mu_0=\mathcal P_{6,C}\rho_0
=\nu_{B_C}(C)\otimes\nu^\flat(Z,Q,r,c,d).}
\tag{3}
$$
其中 $\mathcal P_{6,C}$ 是只旋转实际 $C$ 轴的六次平均，
$Z=\xi_1-\xi_3-2x,Q=\xi_1+\xi_3,r=\xi_2$，而
$$
\nu^\flat=\frac1{42}
(\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
\otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d)
$$
正是 R601 的完整五变量来源。全部隐藏坐标保留。

还记 R626–R628 的正交平面
$$
R=(1+3\omega)c+d,\quad K_0=c+(2+3\omega)d,\qquad
Y=V+aR,\quad W=V+a_WR,
$$
$$
a=-3\omega/8,\quad a_W=a+2,\quad
V=a_ZZ+a_QQ+2\delta r+b_KK_0,
$$
$$
a_Z=(-2+\omega)/2,\quad a_Q=(4+3\omega)/2,\quad
b_K=-(1+6\omega)/8 .
\tag{4}
$$
$\operatorname{Gram}(R,V)=\operatorname{diag}(8,263/8)$。

## 2. 真实 C 平均没有把第一 W 格放大

令 $\mathbf c$ 为 (2) 的 $C$ 行。实际旋转矩阵为
$$
R_{\zeta,C}=I+(\zeta-1)\bar{\mathbf c}^{\,t}\mathbf c,
\qquad\zeta\in\mu_6 .
\tag{5}
$$
逐项有 $WR_{\zeta,C}=W$，而非只在 $C=0$ 后成立。
所以对每个完整旋转支，第一 $W$ 生成变量的六个 sigma 系数都仍为
$$
(\delta,\,2\delta,\,\gamma,\,\bar\gamma,\,3\delta,\,4).
\tag{6}
$$
它们的范数和是 $72$，模二恰四个非零；非零模二 CM 单位置换
原 odd sigma 半特征，因此总半特征平凡。
所有与 $W$ 正交的完整伴随同 (6) 的 Gaussian 交叉均为零。
旋转可以改变伴随格，却不改变 (6)、其半特征或第一轴的平坦相位。

故在保全部伴随的 theta 格中，
$$
\boxed{\text{$\mu_0$ 的整个第一 $W$ 因子属于标准偶 }
       \mathcal S_{72}.}
\tag{7}
$$
这是六个原全函数的有限平均证明，不是从单个 $W$ 边际推测
其余伴随，也没有把 R601 的单独两张量格免费缩小。

R465(14) 已支付原绝对核心
$$
K_{72}=\frac14\sum_{t\in E[4]}\mathsf T_t^{(72)}
       -\frac12\sum_{t\in E[2]}\mathsf T_t^{(72)} .
\tag{8}
$$
为明确全部中心，当前
$g_\pi\equiv91+72\omega\pmod{144}$，
$g_\pi^2\equiv73\pmod{144}$。在标准 Schrödinger 基中，
$$
\mathsf T_{(s+r\omega)/4}^{(72)}e_j
=i^{s(j+9r)}e_{j+18r},\qquad
K_{72}e_j=-(-1)^je_{19j+36}\quad(j\bmod72).
\tag{9}
$$
因 $(19j+36)$ 与 $j$ 同奇偶，整个 $K_{72}^2=I$。
原 $\Theta(6z)$ 拉回锚的核心为 $-1$，与 (8) 的绝对号一致；
这里直接使用 R465 的原绝对规范。脚本检查全部 $72$ 列。

令 $\rho_1=K_W\rho_0$ 为 R465 的真实第二态，并定义
$$
\boxed{\mu_W=K_W\mu_0=\mathcal P_{6,C}\rho_1 .}
\tag{10}
$$
等号成立是因为 $C\perp W$，原整 trace、全部平移中心和
$C$ 旋转在完整张量格中分别作用于正交因子。于是
$$
\boxed{
\mu_0|_{W\in p}=\lambda(P_{W,\kappa})_*\mu_W,\qquad
\mu_W|_{W\in p}=\lambda(P_{W,\kappa})_*\mu_0 .
}
\tag{11}
$$
两态的完整 $W$ 边际准确相同：
$$
\boxed{W_*\mu_0=W_*\mu_W=6\delta\nu_T.}
\tag{12}
$$
这是 R465(13) 加上 $C$ 平均保持 $W$，不是新赋予的算术身份。

## 3. E_W 单层两态及完整矩形

沿用 R628
$$
E_W=R-c_WW,\qquad c_W=(19+3\omega)/72,\qquad
N(E_W)=263/72,\quad E_W\perp W.
\tag{13}
$$
$(W,E_W)$ 相对 $(R,V)$ 的行列式为 $-1$，故共同深域完全相同。
$72E_W$ 的原整数行是
$$
(-13-35\omega,\,-26-70\omega,\,-54-25\omega,\,
 -41+10\omega,\,33+111\omega,\,-4-12\omega),
\tag{14}
$$
范数 $18936=72\cdot263$，模二也是四个非零系数。
它同 $C$ 旋转逐项交换，因为 $E_W$ 位于 $Y/W$ 平面。

这里可以具体保一个完整整框架。记
$$
H=\delta(C-r),\quad K_b=\delta(C+r),\quad X=H+48V/263,
$$
$$
L_1=Z-\bar a_ZK_b,\quad
L_2=Q-\bar a_QK_b/3,\quad
L_3=K_0-4\bar b_KK_b/3 .
$$
则
$$
\mathfrak F=(W,72E_W,263X,2L_1,6L_2,6L_3)
\tag{15}
$$
全为原 CM 整数行；前两行与余四行全部正交。
其完整行列式为
$$
\det\mathfrak F=-586258560\delta
=-2^7\,3^4\,5\,43\,263\,\delta .
\tag{16}
$$
当前所有因子均为单位。后三个 $L_i$ 的非零交叉保在证书，
没有把它们冒充独立正交 tensor。特别 (15) 容许在同一完整来源上
交换第一 $W$ 与 $E_W$ 的限制及归一。

R626 的同一原平面共同深身份为
$$
\mu_0|_{W,E_W\in p}
=\epsilon_p\lambda^2(P_{\mathrm{pl},\kappa})_*\mu_0 .
\tag{17}
$$
将归一单轴核心记为 $K_W,K_E$。正交轴的限制与反缩放逐项交换，
故它们作为完整有界测度算子交换；(17) 说
$K_WK_E\mu_0=\epsilon_p\mu_0$。
结合 $K_W^2\mu_0=\mu_0$，得到
$$
\boxed{
K_E\mu_0=\epsilon_p\mu_W,\qquad
K_E\mu_W=\epsilon_p\mu_0 .}
\tag{18}
$$
例如第一式可严格写为
$K_E\mu_0=K_EK_W^2\mu_0
 =K_W(K_WK_E\mu_0)$，没有假定 $K_E$ 在整个
$\mathcal S_{18936}$ 为 scalar。

在两个真实来源 $\boldsymbol\mu=(\mu_0,\mu_W)^t$ 上，
$$
K_W=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
K_E=\epsilon_p\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{19}
$$
对全部 $r,s\ge0$，全部原伙伴和任意完整测试都有
$$
\boxed{
\mu_i|_{\{W\in p^r,E_W\in p^s\}}
=\lambda^{r+s}\epsilon_p^s
(P_{W,\kappa^r}P_{E_W,\kappa^s})_*
\mu_{\,i+r+s\bmod2}.}
\tag{20}
$$
指标 $0,1$ 在本节分别指 $\mu_0,\mu_W$，不与 R626 的
$\mu_1=K_R\mu_0$ 混同。

## 4. 同一原 q 的 T 中央现在对每层返回

固定 R594 的同一 $q=q_{+,N_0}$，$N_0\ge1$。
其 $C,F,G,D/\kappa^{N_0}$ 及全部 $\lambda,\kappa$ 系数不变。
$C,F,G$ 都与整个 $Y/W$ 平面正交，所以
$q\circ P_W=q\circ P_{E_W}=q$。

原完整 $\pi_4$ 中性身份也传给新第二态：
$$
\boxed{(\pi_4)_*(q\mu_W)=\beta^{N_0}(\pi_4)_*\mu_W.}
\tag{21}
$$
证明是把 $\mu_0$ 的原 $\pi_4$ 身份两边限制 $W\in p$，
应用 (11)，再取消 $\lambda$ 和在其整像上单射的
$P_{W,\kappa}$ 推前。$W$ 是 $\pi_4$ 的一条坐标，
该物理缩放在 $\pi_4$ 上闭合；因此没有交换一个非 $\pi_4$ cut。
这与 R628(32) 对 $R$ 第二态的证明相同，但使用本篇的实际
$\mu_W$。

由 (12)、(20)、(21)，整个 Mellin 参数上严格有
$$
\boxed{
\int_{\{E_W\in p^n,\ W\ {\rm unit}\}}
q\,\langle W\rangle^{d_pu}\,d\mu_0
=6\delta(\epsilon_p\lambda)^n\beta^{N_0}J_T(u),
\qquad n\ge0 .}
\tag{22}
$$
相邻深度相减给每一个完整环带的系数
$(\epsilon_p\lambda)^n(1-\epsilon_p\lambda)$。
R410 已给 $1\pm\lambda$ 为单位。
若再取 $W\in\kappa^r\mathbf Z_p^\times$ 并用实际
$W/\kappa^r$ 测试，(20) 给同一个完整矩形，外部系数为
$6\delta\lambda^{r+s}\epsilon_p^s\beta^{N_0}$。
这里归一的质量项属于同一 Mellin 身份，未将
$W/p^r$ 与 $W/\kappa^r$ 混用。

所以 R628 的比值中心 $f=8(19+3\omega)/263$ 所对应的原
$T$ 中央条件现在对**每个**半径 $p^n$ 成立，
不再限于 $4\mid n$。原 $y,w$ 两个失败球仍存在。

## 5. 旧第三算术线仍保完整五伴随

因为 $C\perp Y$，(10) 的完整 $Y$ 边际就是 R465 的
$\Xi$，不是 R542 的另一个 $\eta$：
$$
Y_*\mu_W=\nu_\Xi .
\tag{23}
$$
在 R465 的原固定覆盖
$$
L=(2Y,\,2Q_s,\,2U_s,\,R_1,R_2,R_3)
$$
中，只把第一坐标记为 $\mathcal Y=2Y$。
原完整第一轴算术投影 $\mathcal P_{\rm new}$ 满足
$$
\mathcal P_{\rm new}L_*\rho_1
=\nu_{S_{\rm new}}\otimes\nu_{\Lambda_{\rm old}},
\qquad \Lambda_{\rm old}(1)=52/3,\qquad
\mathcal P_{\rm new}L_*\rho_0=0 .
$$
实际 $C$ 旋转在此框架是第一轴恒等与五伴随的整线性变换，
所以和每一条真实第一轴 CM 纤维、中心 lift 及 $\mu_6$ 投影
逐项交换。准确得到
$$
\boxed{
\mathcal P_{\rm new}L_*\mu_W
 =\nu_{S_{\rm new}}\otimes\nu_{\Lambda_B},\quad
\Lambda_B=\mathcal P_{6,C}^{\rm comp}\Lambda_{\rm old},\quad
\Lambda_B(1)=52/3,\quad
\mathcal P_{\rm new}L_*\mu_0=0 .}
\tag{24}
$$
$\Lambda_B$ 是完整五变量整有界测度，质量为单位，故其整
Amice 级数仍为单位。本篇没有沿第一轴反卷积。

因此原第三中央零给 (24) 中任意完整纯伴随测试的条件中央零。
不过
$$
E_W=-\frac{263}{1224}Y+\frac{17-3\omega}{36}E_Y .
\tag{25}
$$
它的 $Y$ 系数不为零；$E_W$ cut 不是这种纯伴随测试。
若在 (24) 后附加它，必须像 R465(42)–(44) 那样，把第一 CM
纤维中的 $Y$ 尺度和旋转代入 (25)，同时保外部单位尺度及 log 质量。
(24) 没有给整个 $\Xi$、其参考谱或外谱的中央赋零。

## 6. 同一单位域上的两个真实 W 观察

R628 给
$$
E_Y=R-c_YY,\quad c_Y=(3+3\omega)/34,\qquad
\mu_0|_{E_Y\in p^n}
=(\epsilon_p\lambda)^n(P_{E_Y,\kappa^n}R_Y^n)_*\mu_0 .
\tag{26}
$$
置
$$
b_Y=1+2c_Y=(20+3\omega)/17,\qquad
W^+=b_YY+2E_Y=W,\qquad W^-=W\circ R_Y=-b_YY+2E_Y .
\tag{27}
$$
$N(b_Y)=349/289$；$349\equiv29\pmod{64}$，当前 $p$ 不等于
$349$，所以 $b_Y$ 为单位。对 $n\ge1$，在同一个实际管
$E_Y\in p^n$ 内，准确有
$$
W^+\ {\rm unit}\ \Longleftrightarrow\
W^-\ {\rm unit}\ \Longleftrightarrow\ Y\ {\rm unit}.
\tag{28}
$$

为明确另一个观察的来源，直接保原六 sigma 得
$$
W^-=\frac{-23-6\omega}{17}A
 +\frac{11+96\omega}{17}c
 -\frac{12+12\omega}{17}d .
\tag{29}
$$
因 $C$ 平均保持 $W^-$，其完整边际生成函数是
$$
-\frac1{84}\mathcal C_{29}\left(\frac{-23-6\omega}{17}z\right)
 \sigma\left(\frac{11+96\omega}{17}z\right)
 \sigma\left(-\frac{12+12\omega}{17}z\right).
\tag{30}
$$
物理范数虽然仍为 $72$，固定 $[17]$ 覆盖的标准偶 degree
却是 $20808=72\cdot17^2$。三个显示系数的分子范数分别为
$427,8281,144$，满足 $29\cdot427+8281+144=20808$；
总半特征仍有四个非零模二 CM 系数。
本篇未识别 (30) 为原 $T$ 或别的合格算术来源，也未给它的
中央导数赋值。若使用 $[17]$，实际 Mellin 尺度和质量导数须同时运输。

定义完整 native 差
$$
D_{n,N_0}=
d_p\int_{E_Y\in p^n}q
 \left(\mathbf1_{W^+\ {\rm unit}}\log\langle W^+\rangle
       -\mathbf1_{W^-\ {\rm unit}}\log\langle W^-\rangle\right)
\,d\mu_0 .
\tag{31}
$$
由 (26)–(28)，变换后两个常数 log 逐点相消：
$\langle-Y\rangle=\langle Y\rangle$。又整个权只依赖原
$R/V$ 平面，R594 的真实 $\pi_4$ 中性可抽出 $\beta^{N_0}$。
于是有完整收敛级数
$$
\boxed{
D_{n,N_0}
=2d_p\beta^{N_0}(-\epsilon_p\lambda)^n
 \sum_{j\ge0}
 \frac{(2\kappa^n/b_Y)^{2j+1}}{2j+1}\,M_{2j+1},
\quad
M_k=\int_{Y\ {\rm unit}}\left(\frac{E_Y}{Y}\right)^k\,d\mu_0 .}
\tag{32}
$$
所有 $M_k$ 都是同一个整来源的真单位矩。由于 $n\ge1,p\ge71$，
级数一致收敛，且
$$
D_{n,N_0}
-\frac{4d_p\beta^{N_0}(-\epsilon_p\lambda)^n\kappa^n}{b_Y}M_1
\in p^{3n}\mathcal O .
\tag{33}
$$
这没有把反射差置零，也没有由外部系数为单位推出 $M_1\ne0$。

## 7. 首矩回到原负五行，三个完整补偿不消失

原 $J_S(0)=0$，所以
$$
M_1=\int_{Y\ {\rm unit}}\frac RY\,d\mu_0 .
$$
与 R617、R621 的同一个
$P_1=\int_{V\ {\rm unit}}R/V\,d\mu_0$ 比较，直接按两单位域
的交和差分割，精确得到
$$
\boxed{
\begin{aligned}
M_1-P_1={}&
-a\int_{\{Y,V\ {\rm unit}\}}\frac{R^2}{YV}\,d\mu_0\\
&+\int_{\{Y\ {\rm unit},\,V\in p\}}\frac RY\,d\mu_0
-\int_{\{V\ {\rm unit},\,Y\in p\}}\frac RV\,d\mu_0 .
\end{aligned}}
\tag{34}
$$
这三项全都保在同一 $R/V$ 平面；加回 $q$ 时整式乘
$\beta^{N_0}$。R621 的实际原负五身份因此原样接入：
$$
\boxed{P_1=(-36b_K)\Omega^5 I_{f_1,-5}+\mathcal B_1.}
\tag{35}
$$
$\mathcal B_1$ 是 R621/R626 已逐项运输的三个 $H/V$ 补偿，
不是可忽略的符号。

其中 (34) 的 $V$ 深失败支有真正更强的赋值界。为区别两态，
令 $\mu_R=K_R\mu_0$，这是 R626 的第二态，**不是**
$\mu_W$。原 $V$ 核给
$$
\begin{aligned}
\int_{\{Y\ {\rm unit},\,V\in p\}}\frac RY\,d\mu_0
&=\epsilon_p\lambda
 \int_{R\ {\rm unit}}\frac{R}{aR+\kappa V}\,d\mu_R\\
&=\frac{\epsilon_p\lambda}{a}
 \sum_{k\ge4}(-\kappa/a)^k
 \int_{R\ {\rm unit}}(V/R)^k\,d\mu_R
\ \in p^4\mathcal O .
\end{aligned}
\tag{36}
$$
第二步的 $k=0,1,2,3$ 真零来自 R628(15) 的完整四 sigma 因子
$\mathcal C_{29}(v)=O(v^4)$，对任意完整 $R$ 测试成立；
不是从总质量猜出的消失。

另一条 $Y$ 深失败支也有准确 native 返回。设 $E=E_Y$、
$\theta=1-ac_Y=263/272$。由 R601 的整联合
$Y$ 核 $\lambda P_{Y,-\kappa}$，
$$
\boxed{
\int_{\{V\ {\rm unit},\,Y\in p\}}\frac RV\,d\mu_0
=\lambda\int_{E\ {\rm unit}}
 \frac{E-\kappa c_YY}{-aE-\kappa\theta Y}\,d\mu_0 .}
\tag{37}
$$
归一后的 $V$ 单位恰为 $E$ 单位，不能改成原 $R$ 或原 $V$ 单位。
$\mu_0(E\ {\rm unit})=0$ 是 (26) 和原质量零的直接结果，
因此 (37) 的常数 $-1/a$ 项消去；其余非恒定有理权完整保留。
(34) 的共同单位有理项也仍存在。

本篇已将实际反射条带的首行接回旧 $P_1$、同一个原负五矩和
全部明确补偿。原 $S/T/S_{\rm new}$ 三中央条件只在
(22)、(24)、R628 的已付完整域上使用。
它们尚未把 (34) 的共同单位项、(37) 或
$\mathcal B_1$ 合法消去，亦未赋反射观察 (30) 的中央为零。
故主目标仍需真正的全域算术关系。

## 精确文件和依赖

- [精确脚本](../scripts/check-r634-original-t-companion-and-reflected-unit-comparison.js)
- [精确证书](../scripts/check-r634-original-t-companion-and-reflected-unit-comparison.json)
- [R465：原完整 W 两态和第三算术线五伴随分解](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)
- [R488：原完整三态、半特征和算术张量表](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)
- [R601：原完整 Q 两张量及 Y/W 核](R601-original-q-tensors-complete-y-w-cores-and-fifteen-source-spectrum.md)
- [R626：原完整 R/V 两态与全部 H/V 边界](R626-original-v-core-and-finite-native-boundary.md)
- [R628：真伴随域相消和完整单位算子](R628-native-arithmetic-companions-and-complete-unit-operator.md)
- [R621：同一原负五矩的有限极点补偿](R621-original-six-degree-finite-pole-compensation.md)

证书用 BigInt 的 $\mathbb Q(\omega)$ 算术检查全部 $72$ 个
Heisenberg 列、所有中心符号、六个真实 $C$ 旋转、
完整整数框架及其逆、两个反射观察和全部显示系数。
测度限制相消、同一 $q$ 返回及级数的完整域由正文证明；
没有将数值采样用作全来源恒等式。
