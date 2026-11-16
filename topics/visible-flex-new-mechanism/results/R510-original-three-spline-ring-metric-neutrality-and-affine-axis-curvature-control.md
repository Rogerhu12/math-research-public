# R510：原三样条的同圈精确度量中性方向与轴主曲率仿射响应

2026-11-16。本文只消费已发表源码和接受57的人读收据，进行纸面推导；没有执行几何、Jacobian、求积、符号程序、秩计算、求解器或开发检查。既有数值任务及其费用不变。

主结论是：在原168坐标中，取原末端三个自由五次样条的一个明确组合，可以在选定整圈上准确保持位置、全部一阶位置jet及第一基本形式，同时准确改变径向第二基本形式。原反射轴上两主方向分离，因此其中一支主曲率对该有限参数准确仿射，另一支准确不变。此结论不是当前57已经存在合格降峰步；它不支付全body的门、有限盒可用幅度或实际耦合非零。

## 1. 当前事实与准确目标

[接受57的原实际笔记](../notes/true56-small168-seven-exchanges-original-two-grid-accepted57-20261116.md)明确记载：

- 细网最大绝对主曲率为57.99982125481755，位置是 $s=.78,\theta=\pi/2$；两主曲率为 $-57.99982125481755,-2.6244174617363965$。
- 两网metric辅助量的最大位置均为 $s=.4725,\theta=0$；细网值为0.2660070686486975。
- 两网14个原实际门通过，$.26$ 和主reach所需曲率上限 $1000/61$ 仍未达到。

这些是已付原实际收据，不是本文新求的值。特别不能继续把更早接受点的 $.09$ metric峰当57的峰。原笔记没有标明上述两主曲率中哪一个是本文的径向支，本文不作这个额外认定。

[R490](R490-fixed-metric-intrinsic-curvature-bound-and-a-nested-complete-body-extension.md)已纸证固定目标度量

$$
g=ds^2+a(s)^2d\theta^2,\qquad |K_g|<217<(1000/61)^2.
\tag{1}
$$

因此不能仅由固定 $g$ 的Gaussian乘积条件，将当前约58的外在峰判为不可降低。另一方面，(1)也不构造Gauss–Codazzi解，不控制当前非等距场的实际Gaussian曲率，更不认证全局reach。

本稿保持固定 $a,b_0$、永久参考、全部168场、原172物理坐标和全部端口。改变的是现有切向系数的一个真实子方向，不增加新参数，不改现已运行任务的目标或预算。

## 2. 完整场与原正交形算子

沿R490和[R504](R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders.md)，记

$$
\begin{aligned}
\psi&=\theta+u,\qquad
N=(\cos\psi,\sin\psi,0),\qquad
H=(-\sin\psi,\cos\psi,0),\\
c&=(1+v^2)^{-1/2},\qquad
T=cH+vc\,e_z,\qquad P=\Pi T,\\
X&=aP+z\,e_z,\qquad
U=X_s=a'P+aP_s+b\,e_z,\\
B&=X_{ss}=a''P+2a'P_s+aP_{ss}+b_s e_z.
\end{aligned}
\tag{2}
$$

$\Pi$ 是原完整角圈的零均值周期原函数。本文从不将它替换成某一点的局部角jet，也不删除固定参考高度或原角常数。原场满足完整角闭合，故

$$
X_\theta=aT,\quad X_{s\theta}=a'T+aT_s,\quad
X_{\theta\theta}=aT_\theta,\quad |T|=1.
\tag{3}
$$

令

$$
E=|U|^2,\qquad f=U\cdot T,\qquad
q=\sqrt{E-f^2}>0,\qquad
W=\frac{U-fT}{q},\qquad n=W\times T.
\tag{4}
$$

这是实际场的法向和实际第一基本形式，不用目标 $g$ 代替它们。取此有向法向时，在切平面正交基 $(W,T)$ 中，形算子为

$$
S=
\begin{pmatrix}
\dfrac{L-2fM+f^2N_c}{q^2}&\dfrac{M-fN_c}{q}\\[2mm]
\dfrac{M-fN_c}{q}&N_c
\end{pmatrix},
\quad
L=n\cdot B,\quad M=n\cdot T_s,\quad
N_c=\frac{n\cdot T_\theta}{a}.
\tag{5}
$$

证明是将归一坐标基 $(U,T)$ 的第一形式
$\begin{psmallmatrix}E&f\\f&1\end{psmallmatrix}$和第二形式
$\begin{psmallmatrix}L&M\\M&N_c\end{psmallmatrix}$
作同一个实际基变换；(3)中 $n\cdot T=0$ 消去 $a'T$。若原实现选择相反法向，两主曲率一并反号，绝对曲率、PSD两侧门和本文的响应非零性不变。

(5)把曲率下降需要改变的量明确分开：$B$ 控制径向第二形式，$T_s$ 控制混合项，$T_\theta$ 控制角向项；它们仍受同一完整 $T$ 和 $\Pi$ 约束，并非三组可任意独立指定的数据。

## 3. 反射轴上真实主方向分离

原字段及新增八个角字段均为 $\pi$ 周期、关于零点反射奇的 $u,v$。原椭圆相位模式、原单Q和已固定入口修正保留相同对称性；参见R490 §4及原 angular_basis、EllipticNormalizedQ。

对

$$
\theta_k=\frac{k\pi}{2},\qquad
N_k=(\cos\theta_k,\sin\theta_k,0),\quad
H_k=(-\sin\theta_k,\cos\theta_k,0),
\tag{6}
$$

准确数学场有

$$
u=v=u_s=v_s=u_{ss}=v_{ss}=0,\quad
T=H_k,\quad T_s=0,\quad
T_\theta=-(1+u_\theta)N_k+v_\theta e_z.
\tag{7}
$$

不能从 $T_s(\theta_k)=0$ 推出 $\Pi T_s(\theta_k)=0$。

完整 $\Pi$ 的反射性质给

$$
P(s,\theta_k),P_s(s,\theta_k),P_{ss}(s,\theta_k)
\in\operatorname{span}\{N_k,e_z\}.
\tag{8}
$$

例如相对轴角的水平 $H_k$ 分量为偶函数，其零均值原函数为奇函数，故在轴上为零；其余两分量为奇函数，原函数可在轴上非零。零均值规范唯一固定了积分常数，所以这里没有凭端点将 $\Pi$ 的常数删掉。

由(2)、(7)、(8)，$U,B$都在这个轴平面，故 $f=0,M=0$，(5)准确对角化：

$$
\boxed{\quad
\kappa_s=\frac{n\cdot B}{E},\qquad
\kappa_\theta=\frac{n\cdot T_\theta}{a}.
\quad}
\tag{9}
$$

等价地，写轴曲线
$X(s,\theta_k)=R_k(s)N_k+Z_k(s)e_z$，则

$$
\kappa_s=
\frac{R_k' Z_k''-Z_k'R_k''}
{((R_k')^2+(Z_k')^2)^{3/2}}.
\tag{10}
$$

$R_k=a\,N_k\cdot\Pi T$，不是固定的 $a$；因此固定 $g$ 不固定这条轴曲线的径向曲率。(7)–(10)是准确对称场恒等；binary64角值和FFT会留下原浮点误差，不能把它们当实际逐位零的验收门。

## 4. 原三个完整样条的明确延拓

原径向自由数为9，五次夹持结点的准确定义为

$$
\ell=\frac9{250},\qquad b=\frac{423}{500},\qquad
t_j=\ell+\frac{j}{10}(b-\ell)\quad(1\le j\le9).
\tag{11}
$$

两端各六重。完整15个五次B样条记为 $\mathcal B_0,\ldots,\mathcal B_{14}$。原 RadialBasis 只保第3至11列；末三列 $\mathcal B_{12},\mathcal B_{13},\mathcal B_{14}$ 固定为零，因此所有允许增量在右端消去0、1、2阶jet。

最后一个结点片为

$$
I_{\rm last}=(153/200,423/500)=(.765,.846).
\tag{12}
$$

该片上只有 $\mathcal B_9,\mathcal B_{10},\mathcal B_{11}$ 三个自由列非零。它们在右端的最低非零阶依次为5、4、3；故三列的限制准确张成

$$
\mathcal V_{\rm last}
=\operatorname{span}\{(b-s)^3,(b-s)^4,(b-s)^5\}.
\tag{13}
$$

这是原夹持样条的端阶与维数论证，不是新采样矩阵的数值rank。

固定任意 $\sigma\in I_{\rm last}$，令 $d=b-\sigma>0$。唯一满足

$$
R_\sigma(\sigma)=R_\sigma'(\sigma)=0,\qquad
R_\sigma''(\sigma)=1
\tag{14}
$$

的(13)中多项式是

$$
\boxed{\quad
R_\sigma(s)=
\frac{(s-\sigma)^2(b-s)^3}{2(b-\sigma)^3}
\quad(s\in I_{\rm last}).
\quad}
\tag{15}
$$

直接因式分解证明(14)。唯一性也可由
$(b-s)^3,(b-s)^4,(b-s)^5$的三jet行列式绝对值 $2(b-\sigma)^9>0$ 得到。

令 $(r_9,r_{10},r_{11})$ 是(15)在原三列限制中的唯一系数。**本稿的完整 $R_\sigma$ 定义为**

$$
\boxed{\quad
R_\sigma(s)=\sum_{i=9}^{11}r_i\mathcal B_i(s)
\quad\hbox{在整个原区间上。}
\quad}
\tag{16}
$$

不能将(15)在 $.765$ 左侧直接置零；那会造出不属于原家族的跳接。由真实样条支持，(16)在 $s\le9/25=.36$ 和 $s\ge b$ 为零，保原端口二jet；在 $(.36,.765)$ 内保其真实延拓。该范围也已超过入口权重的活动端，所以这些列上原 $W_2,W_5$ 权重均为1，不存在遗漏的乘积导数。

(11)、(15)在有理 $\sigma$ 下给准确有理系数定义；如未来针对实际缓存行，应取其原binary64径向值对应的准确有理数，而不是将打印小数重新解释成另一个点。本文没有求出或执行任何这些实际系数。

## 5. 同一整圈的有限参数恒等

取原 $u$ 角空间中的 $A(\theta)$、原 $v$ 角空间中的 $D(\theta)$，例如任意原共同 $\sin(2j\theta)$ 组合。沿真正原168参数方向定义

$$
u_\varepsilon=u+\varepsilon R_\sigma(s)A(\theta),\qquad
v_\varepsilon=v+\varepsilon R_\sigma(s)D(\theta),
\tag{17}
$$

全部高度坐标、原单Q及新增九个坐标的增量都可取零。基点自身的新九坐标仍为真实非零值，没有回到旧159场。导数 $T_u,T_v$ 始终在当前完整168场求值。

由(14)，在整个 $s=\sigma$ 圆上，对任意有限 $\varepsilon$，

$$
\begin{aligned}
(u_\varepsilon,v_\varepsilon)&=(u,v),&
(u_{\varepsilon,s},v_{\varepsilon,s})&=(u_s,v_s),\\
T_\varepsilon&=T,&T_{\varepsilon,s}&=T_s,\\
T_{\varepsilon,\theta}&=T_\theta,&
T_{\varepsilon,ss}&=T_{ss}
+\varepsilon(T_uA+T_vD).
\end{aligned}
\tag{18}
$$

最后一行来自完整链式法则：
$T_{ss}=T_iY_{i,ss}+T_{ij}Y_{i,s}Y_{j,s}$。
当前 $Y,Y_s$不变，只有 $Y_{ss}$准确线性变化，故没有被省略的 $\varepsilon^2$ 项。

将(18)沿完整角圈作原 $\Pi$，同圈得到

$$
\begin{aligned}
X_\varepsilon&=X,\quad
X_{\varepsilon,s}=U,\quad
X_{\varepsilon,\theta}=aT,\\
X_{\varepsilon,s\theta}&=X_{s\theta},\quad
X_{\varepsilon,\theta\theta}=X_{\theta\theta},\\
X_{\varepsilon,ss}
&=B+\varepsilon a\Pi(T_uA+T_vD).
\end{aligned}
\tag{19}
$$

因此在这整圈，第一基本形式、法向、metric的 $e=E-1,f$ 以及辅助量 $\eta(e,f)$ **对有限参数准确不变**。这是有限恒等，不只某个线性梯度为零。

在整圈任意正则点，(5)相应给出

$$
S_\varepsilon
=S+
\varepsilon\frac{a\,n\cdot\Pi(T_uA+T_vD)}{q^2}
\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\tag{20}
$$

非轴处两主曲率未必各自线性，因为原 $S$ 可能有混合项；不能把(20)的矩阵仿射冒成全圈每个特征值仿射。

在(6)的轴点，(9)准确给

$$
\boxed{
\begin{aligned}
\kappa_s(\varepsilon)
&=\kappa_s(0)+\varepsilon\,\mathcal L_k(A,D),\\
\mathcal L_k(A,D)
&=\frac{a(\sigma)}{E(\sigma,\theta_k)}
 n(\sigma,\theta_k)\cdot
 \Pi(T_uA+T_vD)(\sigma,\theta_k),\\
\kappa_\theta(\varepsilon)&=\kappa_\theta(0).
\end{aligned}}
\tag{21}
$$

这说明角模式在轴点自身为零，并不使它们对轴曲率无效。真正系数是完整角原函数，不是局部 $A(\theta_k),D(\theta_k)$。

## 6. 一个非退化校准及当前57的未付量

(21)并不自动断言当前57的所有可选系数中有非零值。为说明它不是形式上的恒零算子，可在角圆背景 $u=v=0$ 明算原表达，而不将该背景当57。

令 $n_0=2j\ge2$。原完整零均值原函数准确满足

$$
\Pi[-N\sin(n_0\theta)]
=
\frac{n_0\cos(n_0\theta)N-\sin(n_0\theta)H}{n_0^2-1},
\qquad
\Pi[e_z\sin(n_0\theta)]
=-\frac{\cos(n_0\theta)}{n_0}e_z.
\tag{22}
$$

在轴点写 $n=n_NN_k+n_ze_z$。对
$A=\lambda_u\sin(n_0\theta),D=\lambda_v\sin(n_0\theta)$，

$$
\mathcal L_k
=\frac{a\cos(n_0\theta_k)}E
\left(
\frac{n_0n_N}{n_0^2-1}\lambda_u
-\frac{n_z}{n_0}\lambda_v
\right).
\tag{23}
$$

$n_N^2+n_z^2=1$，$\cos(n_0\theta_k)=\pm1$，所以在这个校准场至少一个原 $u/v$ 方向非零。它也显示只试一族可能漏掉另一族的正常响应。

对57，必须保真实 $c(v),\psi$、当前法向和完整 $\Pi$，使用(21)；(23)不可替代它。当前尚未付的是：真实系数、活动曲率支的辨认、可用幅度、其余同圈及全网峰的同时变化。这些不是已有峰值元数据能够反推出的量。

文学代理仅独立核对了(18)–(21)的同圈链式、完整 $\Pi$ 和轴分离代数；没有执行新计算，也未将此窄核扩大成57的具体响应证据。

## 7. 原172盒、物理步长与有限幅度

将(17)写成原独立坐标方向 $v_*\in\mathbb R^{168}$。它只含原切向坐标，五null-height及全部新增九坐标增量可为零。因此真实172物理映射 $M$ 对此方向保原切向恒等块，但仍必须使用完整172比较。

未来若保持当前小域
$h=4\|M\delta\|_\infty\le1/128$，则沿此方向至少必须有

$$
|\varepsilon|\|Mv_*\|_\infty\le\frac1{512},
\qquad
\underline x_j\le x_j+\varepsilon(Mv_*)_j\le\overline x_j
\quad(1\le j\le172).
\tag{24}
$$

右端盒是原盒，不因(21)改动。若当前某一相关坐标已经在边界，可用参数可能只有一侧或仅零；不能因为线性函数 $\mathcal L_k\ne0$ 就授任意降曲率符号。

对一条已辨认的轴支，目标 $|\kappa_s|\le K_*$ 给出的参数条件是

$$
-K_*\le\kappa_s(0)+\varepsilon\mathcal L_k\le K_*.
\tag{25}
$$

(24)、(25)的交必须非空，且不变的另一支也必须满足 $|\kappa_\theta|\le K_*$。该条件只解决这个轴点；整圈其它点要用完整(20)，其它径向位置的场不再满足(18)，必须保持完整非线性预测和原实际门。

本文也未声称(16)系数幅度小。靠近右端时(15)含 $d^{-3}$，真实原系数盒可能使降峰量很小。不能把有理数学方向舍入成binary64后继续宣同圈逐位不变；实际候选应由R504已明确的实际坐标预测及原ordinary门读取。

## 8. 对下一完整方向的准确贡献

接受57的metric峰 $.4725$ 与曲率峰 $.78$ 不在同一圈。单独(17)保持的是后者的第一形式，不能据此授前者下降；(16)在 $.4725$ 一般非零，必须保真实影响。

原还有六个较前的自由径向列 $\mathcal B_3,\ldots,\mathcal B_8$。它们的支持右端至多为 $.765$，所以任何只用这些列的切向变化，在 $\sigma=.78$ 的一个邻域中准确为零。因而可以形成一个真实的有限参数分工：

1. 用(17)改变后段峰环的径向第二形式；
2. 同时允许前六径向列改变较前的metric峰；
3. 第二组对峰环全部位置二jet为零，不会把(21)的同圈响应改成另一未绑定场；
4. 在两组支持相交的中段，完整 $T$ 非线性必须保留，不能宣两组对所有门可独立相加。

这给下一整个方向一个具体的三角结构，而不是固定 $g$ 的不可能结论。是否能在 $.4725$ 获得所需metric下降、能否补偿后段方向的其它影响，仍是同一实际点、同一真实盒及全网约束的有限问题。本文没有重启任何已闭master、line或开发检查，也没有把不用后端的纸面插值称为已完成优化。

最后，环上的第一形式值保持，不等于其邻域所有导数保持，故(20)不与Gauss方程矛盾。整个body的正则性、球/条带/高度、非局部法弦、连续误差与reach仍属于原任务；本文不以一个轴点的降峰替代它们。

## 9. 准确源码与已读来源

- [R490](R490-fixed-metric-intrinsic-curvature-bound-and-a-nested-complete-body-extension.md)，特别§4–6的完整 $T,\Pi$、全位置二jet和末片结构；本次读取blob为23644c6c020e8e61205629f1c3003c9f95cc72de。
- [接受57原笔记](../notes/true56-small168-seven-exchanges-original-two-grid-accepted57-20261116.md)，本次读取blob为8f1a2d40a33277f615aa1283845f1a35ae83d9c1；这里只消费其峰位置和标量。
- [frame_collar_bvp.py](../scripts/frame_collar_bvp.py)：RadialBasis的五次夹持、原3:-3自由列、target_frame和完整periodic_operator；读取blob586074c9bfba5b64246c015ae9a8303f5076df54。
- [frame_collar_enriched.py](../scripts/frame_collar_enriched.py)：rational_knots、原角列和原列序；读取blobbaab26d567b284520611b459af393488682292a7。
- [frame_entry_paired_repair.py](../scripts/frame_entry_paired_repair.py)：weight_jets与真实入口修正，后段权重准确为1；读取blob13fb63ea486345efc43e4b9240f0c760247938a5。
- [frame_entry_single_q.py](../scripts/frame_entry_single_q.py)：保原Q、固定高度参考和完整六位置jet。
- [frame_complete_body_extension168.py](../scripts/frame_complete_body_extension168.py)及[完整当前168导数](../scripts/frame_complete_body_extension168_joint_selected.py)：基点的非零新九列原样保留，方向使用当前场，未沿用旧159数值J。

可发布的新结论是原完整三样条延拓(16)、同圈有限恒等(18)–(20)、轴主曲率仿射式(21)与明确幅度条件(24)–(25)。当前57的实际响应和全body可行下降仍未由本文宣告。
