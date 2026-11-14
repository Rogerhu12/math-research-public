# R100：二次支撑核的整图尺寸窗与深尾的完整线性 C² 接帽

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**可信度：本文命题及其注明假设下的推论均已证明。** 本文没有构造新的非线性等距闭族，
也没有改变当前 M15/W22 主计算的度量、频率或物理参数。
它回答两个具体问题：纯二次支撑核能否留下 `held/D ≥ .2` 与 `reach/D ≥ .03`
兼容的必要尺寸窗口；原深源中 `ideal(2)=0` 究竟是否允许完整 XYZ 二阶端迹消失。

结论是：轴点见证路线有非空的必要窗口，但要求整个闭图的直径不超过 $100/33$；
原深源确有非零、完整 C² 平接的二次模**无穷小等距变形**。
有限重排尾的实际外端直线、非线性尾图和整个短闭图均还须另外求得。

## 1. 二次核及正常曲率的明确假设

将核的周长归一为 $2\pi$。取

$$
h_q(\phi)=1+q\cos2\phi,\qquad
\rho_q=h_q+h_q''=1-3q\cos2\phi,
\qquad 0<q<1/3.
\tag{1}
$$

以 $e=(\cos\phi,\sin\phi)$、$e^\perp=(-\sin\phi,\cos\phi)$ 定义

$$
\gamma_q=h_qe+h_q'e^\perp,\qquad
u(\phi)=\phi-\frac{3q}{2}\sin2\phi.
\tag{2}
$$

因为 $u'=\rho_q>0$、$\gamma_q'=\rho_qe^\perp$，这是严格凸闭曲线的正向单位弧长参数。
假设它作为 $(\gamma_q,0)$ 位于初始闭曲面 $\Sigma_0$ 的中央圈；中央的另一切向为竖直方向。
后一条件正是 R13/R17 镜像接合中 $F_s^{xy}=0$ 且 $F_s\ne0$ 的情形，
而不是任意包含该空间曲线的曲面都自动具备的性质。

由直接计算，令 $c=\cos2\phi$，有

$$
|\gamma_q|^2=1+2qc+4q^2-3q^2c^2.
\tag{3}
$$

其对 $c\in[-1,1]$ 的导数 $2q-6q^2c$ 严格为正。
故 $\max|\gamma_q|=1+q$，并且中心对称性给

$$
\operatorname{diam}\gamma_q=2(1+q).
\tag{4}
$$

在 $\phi=0$，水平曲率法向也是闭曲面的一个单位法向，故该切向的正常曲率绝对值为
$1/(1-3q)$。形算子的算子范数至少是该值。因此，记 $D=\operatorname{diam}\Sigma_0$，
完整曲面的 reach 必须满足

$$
D\ge2(1+q),\qquad
\operatorname{reach}(\Sigma_0)\le1-3q.
\tag{5}
$$

这里用的是实际正常曲率，不是把某个曲率上界倒置。
所用一般事实 `reach ≤ 1/|κ|` 及切向二阶展开证明见
[R1 §2](R1-phase-quotient-and-narrow-cap-bound.md)；它适用于完整 C² 闭嵌入。

## 2. 轴点见证的必要尺寸窗口

取旋转相位 $\alpha=\pi/2$。核的长轴点 $(1+q,0,0)$ 变成

$$
p=(0,1+q,0)\in\Sigma_{\pi/2}.
$$

初始核含短轴点 $p_-=(0,1-q,0)$，所以无论如何延伸闭曲面，

$$
\operatorname{dist}(p,\Sigma_0)\le|p-p_-|=2q.
\tag{6}
$$

核本身的支持半平面是 $y\le1-q$，所以到核的距离恰为 $2q$。
但前缀、尾或帽可能更靠近 $p$；式 (6) 不等于它到完整曲面的下界。

**命题 1。** 若要求上述单个轴点作为 `held/D ≥ 1/5` 的见证，
同时要求完整曲面 `reach/D ≥ 3/100`，则必有

$$
\boxed{\quad
\frac14\le q\le\frac{47}{153},\qquad
2(1+q)\le D\le
\min\left\{10q,\frac{100}{3}(1-3q)\right\},\qquad
D\le\frac{100}{33}.
\quad}
\tag{7}
$$

**证明。** 见证要求 $D/5\le\operatorname{dist}(p,\Sigma_0)$，与 (6) 合并给 $D\le10q$。
reach 要求与 (5) 合并给 $D\le(100/3)(1-3q)$。
再分别同 $D\ge2(1+q)$ 比较，得 $q\ge1/4$ 和 $q\le47/153$。
函数 $10q$ 严格递增，$(100/3)(1-3q)$ 严格递减；其交点为 $q=10/33$，
共同值是 $100/33$，故它们的最小值不超过该数。证毕。

**范围不能扩大。** 命题 1 是这个纯二次核、这个中央切平面、这个轴点见证路线的必要条件。
它不是任意闭延伸的全局不等式 $\delta_{hold}\le2q$：其它部位可以产生更大的 Hausdorff 变化。
也没有把核直径当作整图直径。

[R21 §3](R21-m12-whole-map-and-actual-metric-decrease.md) 的实际两个固定帽轴心给
$D>3.542609695989968>100/33$。
所以保留该**实际空间摆放**不可能通过命题 1 的二成轴点路线。
未知的新二次模嵌入可有不同的平均高度；R21 §2 本来也允许固定帽整体竖直平移而保持帽度量。
不能用旧图的帽高度下界给一个尚未求出的新嵌入增设相同高度。

### 2.1 支撑修正的必要误差项

若实际核是 $h=1+q\cos2\phi+r(\phi)$，其中 $r$ 为偶的 $\pi$ 周期函数，
令 $\epsilon_0=\|r\|_\infty$、$\epsilon_2=\|r+r''\|_\infty$。
继续假定严格凸、中央竖直切向，并沿同样两个轴点取见证，则其最大可用距离为

$$
d_{axis}=\left|2q+r(0)-r(\pi/2)\right|\le2q+2\epsilon_0,
$$

而 $D\ge2(1+q-\epsilon_0)$、reach $\le\rho(0)\le1-3q+\epsilon_2$。
由 $D\le5d_{axis}$ 和 reach 门，消去 $q$ 得

$$
D\le\frac{100}{33}(1+3\epsilon_0+\epsilon_2).
\tag{8}
$$

这说明 (7) 不可无条件用于带有未知高支撑修正的数值解。
若 $r=\sum_{j\ge2}c_j\cos(2j\phi)$，轴差的修正恰为
$2\sum_{j\ge3,\,j\text{ odd}}c_j$；例如 $\cos4\phi$ 不改轴差，仍会以 $-15c_2$ 改轴点曲率半径。

### 2.2 竖直压缩不是保持共同度量的坐标变更

设活动带的准确相位族为 $F_\alpha=R_\alpha F_0\circ\tau_{-\alpha}$，
其中 $\tau$ 是材料角平移，且所有相位的诱导度量都是一个角不变的 $g$。
记 $h=F_0^z$。施加轴向线性变换
$B=\operatorname{diag}(\lambda,\lambda,\eta)$，其中 $\lambda,\eta>0$。
因为 $B$ 与 $R_\alpha$ 可交换，准确地有

$$
(BF_\alpha)^*e
=\lambda^2g+(\eta^2-\lambda^2)
\tau_{-\alpha}^*(dh\otimes dh).
\tag{8a}
$$

若 $\eta\ne\lambda$，变换后的全部相位具有同一个诱导度量，
当且仅当 $h$ 与材料角无关。

**证明。** 共同度量条件由 (8a) 等价于 $dh\otimes dh$ 角不变。
对每个固定经线参数 $s$，令 $v(\theta)=(h_s,h_\theta)$。
矩阵 $v(\theta)v(\theta)^T$ 不随 $\theta$ 变化。
若它为零，则 $v$ 全为零；若不为零，其平方根向量仅有正负两个选择，
连续性使 $v$ 在连通圆周上保持同一选择。
所以 $h_\theta$ 在该圈为常数，而周期性给
$2\pi h_\theta=\int_0^{2\pi}h_\theta\,d\theta=0$。
因此 $h_\theta=0$；反向代 (8a) 即明。证毕。

一致缩放 $\eta=\lambda$ 不改变任何归一比值。
若原族只是有限误差近似，设 $F_0^*e=g+E_0$，则 (8a) 的右边须再加
$\lambda^2\tau_{-\alpha}^*E_0$。
这仍是准确恒等式；不能将非径向高度产生的角变张量当作数值坐标误差抹去。
新的压缩有限图是否满足某个共同度量容差，要重新计算这个完整张量。
所以把 R21 的实际空间图简单压矮，不是通过同一共同度量构造绕过 (7) 的免费步骤。

## 3. 包含前缀、尾和帽的完整 Hausdorff 下界

下面的条件允许前缀在离开中央圈后逐渐向外展开，不要求整图都落在核的支持半平面内。

**命题 2。** 若完整初始曲面每个点 $X=(x,y,z)$ 在 $|z|\le2q$ 时满足

$$
y\le1-q+\beta z^2,
\qquad 0\le\beta\le\frac1{4q},
\tag{9}
$$

则 $\operatorname{dist}(p,\Sigma_0)=2q$，从而相位族有 $\delta_{hold}\ge2q$。

**证明。** 在 $|z|\ge2q$ 部分，仅竖直坐标已给 $|X-p|\ge2q$。
在其余部分，$2q-\beta z^2\ge q>0$，所以

$$
\begin{aligned}
|X-p|^2
&\ge(2q-\beta z^2)^2+z^2\\
&=4q^2+(1-4q\beta)z^2+\beta^2z^4\ge4q^2.
\end{aligned}
\tag{10}
$$

$p_-$ 达到等号。又 $p\in\Sigma_{\pi/2}$，单个有向 Hausdorff 距离已给所需下界。证毕。

### 3.1 一个非空的完整标量预算

取 $q=3/10$、$\beta=5/6$。若未来实际闭合的参数球面同时满足

$$
|F|\le\frac{29}{20},\qquad
F\cdot n\ge\frac1{10},\qquad
|\kappa_i|\le11,
\tag{11}
$$

并满足 (9)，且其相位构造有真实共同两 jet，则整个相位族有

$$
D\le\frac{29}{10},\qquad
\frac{\delta_{hold}}D\ge\frac6{29}>\frac15,
\qquad
\frac{\operatorname{reach}}D\ge\frac{10}{319}>\frac3{100}.
\tag{12}
$$

这里 reach 使用 [R10](R10-positive-support-offset-reach.md)：
$\min\{1/10,1/11\}=1/11$。活动部分的空间旋转保持同一球包络、支撑和曲率，
固定帽另满足同样界，因而这些是全时结论。

核的最大半径 $13/10<29/20$，其最大正常曲率是 10，均与 (11) 相容。
若固定帽含高度 $z=\pm5/4$ 的两个轴心，则 $\operatorname{diam}H\ge5/2>.2D$。
半径不超过 $3/20$、高度在 $\pm5/4$ 附近、凸起不超过 $1/2000$ 的两帽在球包络内也有余量，
因为 $(3/20)^2+(5/4+1/2000)^2<(29/20)^2$。
这些数字只表明**全图要求的标量预算不矛盾**；没有证明中间连接面满足 (9)、(11)，
更没有由相离片或柱核推断整个闭面的 reach。

## 4. 深源的准确二次模，而非只读 `ideal(2)=0`

以下只用 [R15 §§1–2](R15-weighted-inner-background-and-collar-bounds.md) 的同一未改深源。
记当前 cuff 半径为 $7/50<a_c<3/20$、cut 半径为 $3/5$，并取 $N=160$。
对 $n\ge N$，

$$
R=64,\quad a_{exp}=11/4,\quad
\delta_n=d_0 2^{-n},\quad c_n=c_0 2^{-n/2},\quad
\eta_n=\delta_nc_n,
\tag{13}
$$

其中 $d_0\in[1/200,1/160]$、$c_0\in[1/25,1/16]$。
每层选 R15 已证明存在的 exact 校准根 $\alpha_n\in[1/2,2]$，
使二次模的真实线性传递矩阵满足 $T_{21}=0$。
这里说的是原无限背景的 exact 根，不是把浮点 Newton 的有限残差写成零。

源定义见 `general_root_smooth_tail_cells.cjs::cellSegments` 及
`tailnext_balanced_tail.mjs::balancedCellTransfer`；它们位于
`repro/source-root/topics/large-amplitude-twist-flex/scripts/`。
一个 cell 依次有两端口、四个 log 过渡和三个平台。
三个平台的 $p$ 值为 $R,\delta^2/\alpha,1$，各自长度比为 1；
另六段长度比都是 $c$，端口值为 $\delta,\delta2^{11/4}$。
过渡以 $S(x)=x^3(10-15x+6x^2)$ 插值 $\log p$。

对二次模取状态 $(Q,\pi)$，其中高度系数 $f=r^4Q$，$\pi$ 是按本层正数 $\mu$ 归一的动量。
每段的准确方程为

$$
\frac d{dx}\binom Q\pi
=\ell_{ratio}
\begin{pmatrix}0&\delta^2/p(x)\\-p(x)&0\end{pmatrix}
\binom Q\pi.
\tag{14}
$$

方向取当前物理 `orientation=+1`，即每段 $x$ 增加是由内向外。
一般模的对角项含 $m^2-4$，在 $m=2$ 恰好为零；下三角的系数
$m^2(m^2-1)/12$ 恰好为 1。

### 4.1 全层准确增益至少 30

**引理 3。** 对所有 $n\ge160$，每层由内向外的准确矩阵有

$$
T_n\binom10=\binom{t_n}0,
\qquad t_n\le-30.
\tag{15}
$$

任意初始部分层的传递矩阵在 $\ell^\infty$ 算子范数下不超过 24960。

**证明。** 校准已给第一列下项为零。为控制上项，比较三平台和三个极限剪切矩阵。
对固定平台 $p$，准确矩阵为

$$
H(p)=
\begin{pmatrix}
\cos\delta&(\delta/p)\sin\delta\\
-(p/\delta)\sin\delta&\cos\delta
\end{pmatrix}.
\tag{16}
$$

对应 $p=R,\delta^2/\alpha,1$ 的矩阵范数分别不超过 $65,3,2$。
它们分别与

$$
U_R=\begin{pmatrix}1&0\\-R&1\end{pmatrix},\quad
V_\alpha=\begin{pmatrix}1&\alpha\\0&1\end{pmatrix},\quad
U_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix}
\tag{17}
$$

相差至多 $12\delta^2$。
这是 $|1-\cos\delta|\le\delta^2/2$、
$|1-\sin\delta/\delta|\le\delta^2/6$、$|\sin\delta|\le\delta$
在 $R=64,\alpha\in[1/2,2]$ 上的逐行估计。
同样范数界也覆盖任意部分平台。

全部过渡和端口有 $\delta^2/2\le p\le64$；故 (14) 的系数矩阵范数至多 $64c$。
当 $64c\le1/2$ 时，任一此类短段的矩阵 $J$ 满足

$$
\|J\|_\infty\le e^{64c}\le2,\qquad
\|J-I\|_\infty\le e^{64c}-1\le128c.
\tag{18}
$$

三个剪切的顺序乘积为

$$
S_\alpha=U_1V_\alpha U_R
=\begin{pmatrix}
1-\alpha R&\alpha\\
-(R+1)+\alpha R&1-\alpha
\end{pmatrix}.
\tag{19}
$$

九个因子在逐一替换前后的范数乘积均不超过
$65\cdot3\cdot2\cdot2^6=24960$。
望远镜展开给

$$
\|T-S_\alpha\|_\infty
\le24960(6\cdot128c+3\cdot12\delta^2)
<2\cdot10^7c+10^6\delta^2<1.
\tag{20}
$$

最后一步在 $n\ge160$ 用 $c\le2^{-84}$、$\delta\le2^{-160}/160$ 即得。
而 $(S_\alpha)_{11}=1-64\alpha\le-31$，故 $t_n\le-30$。
任意部分层同样由这些因子及任意部分的最后一段组成，给所述 24960 界。证毕。

### 4.2 非零解在全部层内的衰减

记 $r_n$ 为 cell $n$ 的外端，故 $r_n\downarrow a_c$。
任取 $Q_N\ne0$，在所有边界选 $\pi_n=0$，并递推

$$
Q_{n+1}=Q_n/t_n.
\tag{21}
$$

按 (14) 在每层由内端发展，由 (15) 恰好得到外端值，故各层组成同一个非零解。
相邻层的动量归一化相差正数 $2^{11/4}$，并不改变零动量；物理动量连续。
对 $C=25000$，(15) 及部分层界给

$$
|Q_n|\le |Q_N|30^{-(n-N)},\qquad
|Q(r)|,|\pi(r)|\le C|Q_n|\quad (r_{n+1}\le r\le r_n).
\tag{22}
$$

式 (22) 是准确 ODE 的估计，没有执行一个有限 RK 然后外推到无穷层。

## 5. 从高度二 jet 到完整 XYZ 二 jet

物理变量关系是

$$
f=r^4Q,\qquad
f_r=4r^3Q+\frac{\sqrt{12}\mu}{r^4w}\pi,
\qquad
\frac\mu w=\frac{r^7\delta}{p}.
\tag{23}
$$

消去 $Q,\pi$，或直接对 (23) 求导并代 (14)，得

$$
f_{rr}=-\frac{w_r}{w}\left(f_r-\frac{4f}{r}\right).
\tag{24}
$$

所有深层 $a_c<r<r_{160}<1$。由 $p\ge\delta^2/2$、$\sqrt{12}<4$，
结合 (22)，有

$$
|f|\le C|Q_n|,\qquad
|f_r|\le\frac{12C}{\delta_n}|Q_n|,
\qquad
\left|f_r-\frac{4f}{r}\right|\le\frac{8C}{\delta_n}|Q_n|.
\tag{25}
$$

R15 的 log 跳跃界为 $H_n=17+7n/5$，且 $\|S'\|_\infty=15/8$。
由于 $a_c>1/8$、$\eta_n<1$，源的明确径向公式给

$$
\left|\frac{w_r}{w}\right|
\le\frac7{a_c}+\frac{\sqrt{12}(15/8)H_n}{a_c\eta_n}
\le\frac{116H_n}{\eta_n}.
\tag{26}
$$

因此

$$
|f_{rr}|\le\frac{928C H_n}{\delta_n\eta_n}|Q_n|.
\tag{27}
$$

因为 $\delta_n\eta_n=d_0^2c_0\,2^{-5n/2}$，而 $30>2^{5/2}$，
(22)、(25)、(27) 证明 $f,f_r,f_{rr}\to0$，且是在每层所有内部点上一致趋零。
角导数只乘以固定频率 2，所以高度扰动 $f(r)\cos2\theta$ 的全部混合二 jet 都趋零。

### 5.1 完整空间变形

旋转背景为

$$
F_0(r,\theta)=(r e_r(\theta),h_0(r)),\qquad h_0'=w.
$$

定义

$$
U(r)=\frac{w(r)}3\bigl(rf_r(r)-4f(r)\bigr),\qquad V(r)=-\frac{U(r)}2,
$$

$$
\mathcal V(r,\theta)=
U(r)\cos2\theta\,e_r(\theta)
+V(r)\sin2\theta\,e_\theta(\theta)
+f(r)\cos2\theta\,e_z.
\tag{28}
$$

其中 $e_r,e_\theta$ 在此为三维水平单位向量。
准确地有

$$
U_r=-wf_r,\qquad U_{rr}=-\frac{4w_rf}{r}.
\tag{29}
$$

第一个恒等式由 (24) 代入 $U_r$ 后相消得到；再求一次导数并代 (24) 得第二个。
R15 已给 $w,w_r$ 有界且均趋零。由 (25)–(27)、(29)，
$U,U_r,U_{rr},V,V_r,V_{rr}$ 全趋零。
于是 **完整 Cartesian** $\mathcal V$ 的所有总阶数不超过二的导数都趋零。
在 $r\le a_c$ 定义 $\mathcal V=0$，得到真实 C² 延拓，不只是一条高度函数的接合。
各有限源接点处 $w,w_r$ 连续，(24) 与物理状态连续也给同一 C² 接合。

最后直接核线性等距方程。对任意频率 $m$，形如 (28) 的变形对应三个一次度量项为

$$
U_r+wf_r,\qquad U+mV,\qquad rV_r-mU-V-mwf.
\tag{30}
$$

取 $m=2$，(28)–(29) 使三者分别为零。
故 $\mathcal V$ 是同一旋转度量的非零 C² 无穷小等距变形，且在整个 cuff 内盘严格为零。

**这不是非线性族。** $F_0+t\mathcal V$ 的精确诱导度量还含
$t^2(d\mathcal V)^T d\mathcal V$。本文没有消去这个二次项，
没有证明它能积分成固定度量的非线性族，也没有用有限阶小量支付 G5。

## 6. 理想远端、真实有限尾和均值的不同含义

### 6.1 `ideal(2)=0` 的准确内容

令 $\varrho=2^{11/4}$。极限平台校准 $\alpha=1+1/R$ 后，
包含外端动量重归一化的理想传递为

$$
T_{ideal}=
\begin{pmatrix}-R&1+1/R\\0&-1/(R\varrho)\end{pmatrix}.
\tag{31}
$$

因此二次模的向内衰减直线是 $\pi/Q=0$，其向外特征值为 $-R$。
`scripts/950f-tail-subdivision.mjs::ideal` 与
`scripts/closing_recalibrated_tail.mjs::idealModeGraph` 的二次分支返回 0，
正对应这条直线。

但在一个有限端口 $\pi=0$ 时，由 (23) 得 $f_r=4f/r$，通常并不为零。
它也不是 $f=0$ 的 Dirichlet 条件。§§4–5 的无穷衰减才付出了真正的 C² 平接。

### 6.2 当前物理重排的有限部分不能省略

当前固定背景在 raw cells $0,\ldots,159$ 中经过真实径向重分配、斜率 cap 与控制修正。
原源的 exact 校准不能自动保证这些**新物理方程**的 $T_{21}$ 仍为零。
源码 `physicalModeColumn` 正是用实际 $r,r_x,w$ 重新计算物理线性流；
`solvePhysicalCell` 也把物理二次模校准单列为一个问题。

因此，以 $n=160$ 的已付深线 $\pi=0$ 为端口、通过实际全部有限物理 cells 向外传递，
才能得到这条 exact 线性深解在 cut 的真正直线。
该直线还可能在 $Q$ 图上竖直；本文没有假定实际 DN 斜率有限。
若取例如 $N_{far}=32<160$ 并直接施加 `ideal(2)=0`，
那只是选择了一个有限理想端条件，不能借 §§4–5 宣称它已经等于无限物理 DN。
同一提示也适用于把现有三次模的有限远端控制未经计算地移植给二次模。

### 6.3 二次模不会造成一个自动的均值或单圈闭合奇点

[R96 §§1–2](R96-quadratic-momentum-near-rotating-state.md) 给原角连接矩
$\mathfrak m=(\omega-1)/w^2=L+O((|L|+|P|+|P_\theta|)^2)$。
在旋转态，消去 $L$ 均值的方程 $\langle\mathfrak m\rangle=0$ 对该均值的导数为 1。
所以在每个固定正背景截面，频率间隔改为 2 不会破坏局部均值隐函数定理。
这不是跨无限层的统一非线性估计；小邻域及常数可以依赖截面。

若真实连续高度及其径向一 jet 是偶的 $\pi$ 周期函数，并满足原投影正条件及
$\langle\omega\rangle=1$，则 [R85 §3](R85-darboux-curl-and-tail-metric-frequency.md)
中的 $\rho,\omega,P\omega$ 均为 $\pi$ 周期。
发展角 $\psi=\theta+P\omega$ 满足 $\psi(\theta+\pi)=\psi(\theta)+\pi$；
水平角切向 $T=\rho e_\theta(\psi)$ 因而反周期，$\int_0^{2\pi}T\,d\theta=0$。
加上周期高度，这确实使每个固定径向截面的空间曲线闭合。
其径向发展仍须满足完整 Darboux/GC 相容；仅按截面闭合不能替代该二维方程。

非线性运算也不保留单个 $\cos2\theta$：R96 的二次项一般产生均值和 $\cos4\theta$，
随后会有其它偶模。不能把 `ideal(2)=0` 解释成非线性二次模子空间不变。

## 7. 现有三凸起可保严格非全等，但原三阶证明不能照搬

二重对称的未标记活动实体有纯水平三阶矩为零，故 R21 的活动 $A_3$ 与帽 $B_3$
直接干涉证明不能原封不动套用。下面给一个不要求增大现有凸起的替代条件。

**命题 4。** 设闭曲面的有界实体在相位 $\alpha$ 下为
$\Omega_\alpha=R_\alpha\Omega_A\cup\Omega_B$，内部不交。
$\Omega_A$ 绕 $z$ 轴二重对称，$\Omega_B$ 是固定的三重对称帽凸起实体。
假设活动实体的水平二阶矩有不同特征值；固定凸起的纯水平复三阶矩 $B_3$ 非零。
则某两个相位的边界不在含反射的 $E(3)$ 下全等，因而相位族有 $\delta_E>0$。

**证明。** 两个实体的水平质心均为零，总质心在 $z$ 轴且不随相位改变。
关于总质心，记完整二、三阶矩为 $S_{ij}$、$T_{ijk}$。
二重及三重对称给 $S_{xz}=S_{yz}=0$，且水平块为

$$
S_h(\alpha)=R_\alpha S_{A,h}(0)R_\alpha^T+bI.
\tag{32}
$$

其两个不同特征值记为 $a,b_1$，都不随相位变化。
三阶矩中含一个水平指标、两个 $z$ 指标的分量为零；
含两个水平指标、一个 $z$ 指标的矩阵随活动部分共轭旋转，加上帽的固定标量矩阵。
纯 $z$ 分量保持不变。纯水平三阶矩只来自帽，且为一个三次谐张量：
三重对称使它的水平迹向量为零。

考虑完整、含反射也不变的收缩

$$
I=T_{ijk}T_{lmn}S_{il}S_{jm}S_{kn}.
\tag{33}
$$

$S$ 的水平/竖直分块使不同竖直指标数的项互不混合。
含 $z$ 的部分因上述共同旋转而不随相位变化。
选择帽的水平坐标使 $B_3>0$ 为实数，令 $t=B_3/4$。
帽谐张量的非零基本分量为 $T_{xxx}=t$、$T_{xyy}=-t$ 及其排列。
在 $S_h$ 的特征坐标中，它旋转了某角 $\alpha-\alpha_0$。
直接收缩得纯水平部分

$$
I_h(\alpha)=\frac{B_3^2}{32}
\left[(a+b_1)^3+(a-b_1)^3\cos6(\alpha-\alpha_0)\right].
\tag{34}
$$

例如余弦平方项的权为 $a^3+3ab_1^2$，正弦平方项的权为 $3a^2b_1+b_1^3$，
相加减即为 (34)。其非恒定系数不为零，证明某两实体不全等。
边界若全等则其有界实体也全等，矛盾。
紧集的近似刚体对齐若距离趋零，平移部分有界而 $O(3)$ 紧，取子列便得到实际全等；
故非全等相位的对齐 Hausdorff 下确界严格大于零。证毕。

命题 4 还需要**整个活动实体**的水平二阶矩非各向同性，不能从中央圈直接推断。
纯二次凸截面的复二阶面积矩确为
$\int_{K_q}(x+iy)^2\,dx\,dy=\pi q(4-9q^2)/4>0$，
这可由 Green 公式 $\frac14\int_{\partial K_q}z^2(x\,dy-y\,dx)$ 与 (2) 展开验证；
但不同高度的完整前缀/尾仍可能改变总矩，须使用实际全体积或额外几何符号证明。

另一方面，[R24](R24-cap-marking-quotient-upper-bound.md) 对任何活动对称阶都给
$\delta_E\le1/2000$，只要仍是同一固定高度凸起。
所以命题 4 仅保严格 $\delta_E>0$，不支付加强的 $\delta_E/D\ge.05$。

## 8. 留给真正闭合的具体问题

本稿实际支付了全闭图轴点见证的必要窗和充分外包条件，及同一 exact 深背景二次模的
非零、完整 C²、固定开内盘的**线性**接合。下一步若采用这条新几何路线，仍需：

1. 用实际有限物理尾传递而非任意 `ideal(2)=0` 得到端口，
   并求非线性偶模/均值图及其无限端控制；
2. 将该真正端口与二次支撑核的二维前缀相配，保同一候选内部的共同度量和全部 Cartesian 两 jet；
3. 在自己的完整闭图上证明 (9) 及足够短的 $D$、全域支撑/曲率或其它 reach 证书；
4. 用实际整体矩或其它集合不变量付严格非全等，并按 README 完成同一度量的数值加密或精确存在证明。

当前固定 g 的主 M15/W22 计算不因本文而改变。
旧 R21 的完整几何仍是其自身的结论，不能移植给尚不存在的二次模闭图。
