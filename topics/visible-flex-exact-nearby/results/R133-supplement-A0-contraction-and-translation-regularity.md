# R133 续篇：先在全频 A0 中收缩，再由角平移恢复二阶正则

2026-11-13，visible-exact-astra-ac0d / newton_source。

本篇沿用
[未加权驱动帽](R133-supplement-unweighted-driven-cap-and-small-nonlinear-branch.md)
的真正全频 Green 算子和四个独立端口，改变的是非线性小量所用的
范数。先在完整 $\mathcal X_0$ 球内证明存在和唯一性；再对给定
$A_2$ 边界的角平移曲线求导，得到同一个解的二阶角正则性。
这一做法不需要 $A_2$ 范数本身落在非线性小球内。

真实 nonlinear regular 外尾、与内侧 body 的两迹匹配，以及完整
frame/position 的周期 holonomy 仍是独立端口；本篇没有把它们
替换成某个浮点边界残差或删除。

## 1. 保持原算子、目标和所有模式

继续使用实际 $g_0=E(r)dr^2+a(r)^2d\theta^2$，完整
$|\eta|\le10^{-9}$，以及 $m\in4\mathbb Z$ 的所有复 Fourier 模。
在本篇的正帽区间上，紧支撑度量族 $E_\nu=E\exp(\nu h)$ 中的
$h$ 恒为零，因此每个该 $g_\nu$ 都准确等于同一个 $g_0$。
变化条带中的旧证书不因此转授。

令 $U=(B,c)$，其中 $C=C_0+c$，$C_0<0$ 是实际旋转参考。
定义实 Banach 空间
$$
\mathcal X_0=\left\{f:\sum_{m\in4\mathbb Z}
       \sup_{r\in I}|\widehat f_m(r)|<\infty\right\},
\qquad \|U\|=\|B\|_{\mathcal X_0}+\|c\|_{\mathcal X_0}.       \tag{V.1}
$$
系数取径向连续函数，保留实值共轭条件。乘法满足
$\|fg\|_{\mathcal X_0}\le\|f\|_{\mathcal X_0}\|g\|_{\mathcal X_0}$。
这是先取每模的径向 supremum 再求和的范数；不以某个采样网格的
最大值代替。

四个端口记为
$$
h=(c_{\ne0}(L),d_{\ne0}(R),B_0(R),c_0(R)),\qquad R=25/8,
\quad d_m=i\operatorname{sgn}(m)\widehat B_m+q_Mc_m .         \tag{V.2}
$$
$q_M$ 是原真正 R74 regular Jacobi 线，包括所有已付尾 fee。
本篇只将它用作准确三角坐标；任意 $d(R)$ 都是可给定的独立驱动，
不因此成为真正 nonlinear regular 条件。

前篇 (U.8)–(U.18) 对 $s=0$ 原样成立。把完整非线性固定点写成
$$
U=\mathcal Lh+\mathcal GQ(U),\qquad
Q(B,c)={B^2+\ell c^2\over C_0+c}.                            \tag{V.3}
$$
这里 $\mathcal L$ 保留四个端口，$\mathcal G$ 保留全部正负模与
两个 mean，且
$$
\|\mathcal Lh\|\le H_C\|c_L\|_{A_0}
       +H_D\|d_R\|_{A_0}+|B_0(R)|+|c_0(R)|=:H,
\qquad \|\mathcal G\|\le K .                                \tag{V.4}
$$
这些 $H_C,H_D,K$ 都由实际闭盒全频核计算，不由有限候选求解器
成功标记取得。

## 2. A0 收缩及完整二阶 Fréchet 导数

取 $C_*\le\inf_I|C_0|$、$\Lambda\ge\max(1,\sup_I\ell)$，
$0<\rho<C_*$，并记 $d_*=C_*-\rho$。前篇的完整代数估计给
$$
\|Q(U)\|\le {\Lambda\rho^2\over d_*},\qquad
\|DQ(U)\|\le\Lambda\left({2\rho\over d_*}
                      +{\rho^2\over d_*^2}\right).          \tag{V.5}
$$
假设严格门
$$
H+K{\Lambda\rho^2\over d_*}<\rho,\qquad
\lambda:=K\Lambda\left({2\rho\over d_*}
                         +{\rho^2\over d_*^2}\right)<1.     \tag{V.6}
$$
于是 (V.3) 在完整闭球 $\|U\|\le\rho$ 内有唯一解。
$C_0+c$ 的绝对值至少为 $d_*$。小球中出现的无限高 Fourier 模
没有被截掉。

为支付正则性，令 $N=B^2+\ell c^2$、$D=C_0+c$。对任意
$V=(V_B,V_c)$、$W=(W_B,W_c)$，完整二阶导数是
$$
\begin{split}
D^2Q(U)[V,W]
={}&{2V_BW_B+2\ell V_cW_c\over D}\\
&-{(2BV_B+2\ell cV_c)W_c+(2BW_B+2\ell cW_c)V_c\over D^2}
  +{2N V_cW_c\over D^3}.
\end{split}                                                   \tag{V.7}
$$
因此
$$
\|D^2Q(U)\|\le
J_2:=\Lambda\left({2\over d_*}+{4\rho\over d_*^2}
                         +{2\rho^2\over d_*^3}\right).      \tag{V.8}
$$
完整 $A_0$ Banach 代数中的 Neumann 级数还证明 $Q$ 在开集
$\|c\|<C_*$ 上解析；不需要预先知道未知解有角导数。

## 3. 自包含的角平移正则性论证

令 $T_\tau f(r,\theta)=f(r,\theta+\tau)$。在 (V.1) 中
$T_\tau$ 是等距且强连续的群：先截取有限 Fourier 和，再用
原绝对可和尾控制截取误差，即得强连续性。目标系数只依赖 $r$，
所有 $q_M$ 及 Green 核都是 Fourier 乘子，故
$$
T_\tau\mathcal Lh=\mathcal L(T_\tau h),\qquad
T_\tau\mathcal Gf=\mathcal G(T_\tau f),\qquad
Q(T_\tau U)=T_\tau Q(U).                                    \tag{V.9}
$$
两个 mean 端口在 $T_\tau h$ 中保持不变。

设两个非零模端口属于 $A_2$。于是 $\tau\mapsto T_\tau h$ 是
端口 $A_0$ 空间中的 $C^2$ 曲线，导数是实际角导，不是频率截止
后的导数。平移不改变 (V.6) 的球和收缩常数。设 $U_\tau$ 为
平移端口的唯一固定点；(V.9) 和唯一性给
$$U_\tau=T_\tau U_0.                                       \tag{V.10}$$

下面直接证明这个固定点曲线可以求导。对两个端口 $h,\widetilde h$，
收缩估计先给
$$
\|U(h)-U(\widetilde h)\|
\le {\|\mathcal L(h-\widetilde h)\|\over1-\lambda}.         \tag{V.11}
$$
在一个固定 $\tau$ 处，$I-\mathcal GDQ(U_\tau)$ 的 Neumann 级数
收敛，逆范数不超过 $(1-\lambda)^{-1}$。从两个固定点方程相减，
用 (V.8) 展开非线性项，Taylor 余项被
$KJ_2\|U_{\tau+t}-U_\tau\|^2/2$ 控制。(V.11) 将它变为 $O(t^2)$；
除以 $t$ 再取极限便得到第一导数。这个论证也表明导数连续。
再次对得到的线性方程作同样的差商，并使用 $DQ,D^2Q$ 的连续性，
得到第二导数。具体为
$$
\begin{split}
(I-\mathcal GDQ(U))U_\theta&=\mathcal Lh_\theta,\\
(I-\mathcal GDQ(U))U_{\theta\theta}
 &=\mathcal Lh_{\theta\theta}
       +\mathcal GD^2Q(U)[U_\theta,U_\theta].
\end{split}                                                   \tag{V.12}
$$
由 (V.10)，这里的导数确实是未知解的角导数。
若 $H_j\ge\|\mathcal Lh_{\theta^j}\|$，便有全模式估计
$$
\|U_\theta\|\le {H_1\over1-\lambda}=:M_1,\qquad
\|U_{\theta\theta}\|
\le {H_2+KJ_2M_1^2\over1-\lambda}=:M_2.                    \tag{V.13}
$$
它们可以很大，但只需要有限，完全不进入先前的存在小量门。
这正是与在 $A_2$ 小球中直接收缩的区别。

Fourier 坐标提取是 $\mathcal X_0$ 上的连续线性泛函。因此强导数的
每个坐标准确等于 $im\widehat U_m$、$-m^2\widehat U_m$，从而
$$
\|U\|_{\mathcal X_2\oplus\mathcal X_2}
\le\rho+2M_1+M_2.                                          \tag{V.14}
$$
这还明确给出全部频率的 $A_2$ 范数，不只是逐点形式导数。
所有 Fourier 级数及以上两条角导数在整个径向区间绝对一致收敛。
准确 Codazzi 方程再给 $U_r$ 及 $U_{r\theta}$ 的连续性；实际目标
系数在拼接处保持原已付正则性。相应 Gauss–Codazzi 数据因而支持
R126 的局部 $C^2$ immersion 重建。周期 frame/position 的全圆
holonomy 仍须独立支付，不能从局部重建推出。

## 4. 实际有向消费与输入身份

实际消费区间是
$$I=[21/20,25/8].$$
consumer 以320-bit Arb 重新核验原1334个闭盒的所有全频后缀
Riccati 严格边界，再消费其中875个相邻闭盒。首盒若横跨
$21/20$，只缩短被使用的区间，其原完整系数界仍保留。全部
primitive 尾、whole $\eta$、正型和真正 $q_M$ 的非第四模尾费均
与已冻结 native 相同。

下表将完整有向结果向外放松成便于阅读的小数；原生报告保存
实际 Arb 区间、每盒 margin 和全部输入 SHA256。

| 量 | 严格界 |
| --- | ---: |
| $q_+$ | $<1.190258951$ |
| $\sigma_D$ | $>3.611694363$ |
| $\sigma_C$ | $>1.391162506$ |
| $H_C$ | $<2.190258951$ |
| $H_D$ | $<7.047511509$ |
| 完整非线性核 $K$ | $<11.223128203$ |
| $\ell_-$ | $>0.910380913$ |
| $\Lambda$ | $<1.321225831$ |
| $C_*$ | $>0.170533801$ |

取准确半径及独立端口预算
$$
\rho={9\over2000},\qquad
\|c_L\|_{A_0}\le10^{-3},\qquad
\|d_R\|_{A_2}\le10^{-8},\qquad
|B_0(R)|,|c_0(R)|\le10^{-8}.                                \tag{V.15}
$$
此处三个外端口是独立的，尤其没有以 $d_R=0$ 来声称外尾匹配。
对于一般 $A_2$ 的 $c_L$，存在门只使用其 $A_0$ 上界；下面的
具体二阶数值则消费准确实际边界的导数大小。

原生计算严格给出
$$
H<0.002190349426,\qquad
H+K\Lambda\rho^2/(C_*-\rho)<0.003998853516<0.0045,
$$
$$
\lambda<0.814671981<1,\qquad
|C|>0.166033801.                                            \tag{V.16}
$$
因此 (V.15) 的完整四端口球上已有唯一全频非线性 Codazzi 驱动图。

具体内端函数来自已完整保存的 M64 三次径向候选
`2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz`，
SHA256
`4046eb7ac8da162ab9aad9fcb4991933200abdbc2c22ed6329d49bb13d72b856`。
consumer 把其中64个余弦系数的每个 float64 解释成准确 dyadic
有理数，在第787片的准确 $r=21/20$ 上用 Arb Horner 求值，并乘
准确振幅
$$\alpha=5854679515581645/9007199254740992.$$
得到的边界定义包含物理频率 $4,8,\ldots,256$，其余边界模式
准确为零；解的高模式则由 (V.3) 全部保留。原生界为
$$
\begin{split}
\|c_L\|_{A_0}&<0.000930623262,\\
\|\partial_\theta c_L\|_{A_0}&<0.003722847071,\\
\|\partial_\theta^2 c_L\|_{A_0}&<0.014894221684,\\
\|c_L\|_{A_2}&<0.023270539087.
\end{split}                                                   \tag{V.17}
$$
最后一项明显大于 $\rho$；它只是正则性输入，没有被错误用作
存在小量。对 $j=1,2$，$|m|^j\le(1+|m|)^2$，所以
$$H_j=H_C\|\partial_\theta^jc_L\|_{A_0}+H_D10^{-8}$$
同时覆盖 (V.15) 的所有外端 $d_R$，而两个 mean 的角导准确为零。
实际消费得到
$$
H_1<0.008154069592,\quad H_2<0.032622272821,\quad
J_2<16.789527069,
$$
$$
\|U_\theta\|<0.043998040,\qquad
\|U_{\theta\theta}\|<2.144264086.                            \tag{V.18}
$$
于是同一个实际解满足 (V.14) 的完整二阶 Fourier 范数界。

可复跑的命令为
```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_cap_A0_translation_budget.py \
  --left 21/20 --radius 9/2000 --inner-c-budget 1/1000 \
  --out notes/2026-11-13-R133-A0-driven-cap-r105-native.json.gz
```
producer 拒绝覆盖已有报告；独立重跑须使用新输出路径。
本次 source SHA256 是
`320d065038d6ca6478590b54163b1798fd05b431dbc902680c611e2480051783`，
成功报告 SHA256 是
`d81ebd097292b5ebbef8cd26e16b73b0ca6e975bf4fc38ec5496924e05f9c65c`。

另一次 $[1,25/8]$ 的实际粗球检查也完整保留：该次
$\rho=.006$、$\|c_L\|_{A_0}\le1/650$ 给出的球像上界
$0.007151534198$ 超过半径，收缩因子 $1.259779570>1$。
准确边界本身通过 $A_0$ 输入门，但上述两个存在门失败，所以报告
明确记为 false，未给该更大区间授证。其文件为
`2026-11-13-R133-A0-driven-cap-r1-native.json.gz`，SHA256
`e780eb3caee46dbd19139ef6b4a2056408bf1039d3eab248fe0bf57fc387c70b`。
这说明本次具体充分预算未通过，不说明该真实边值问题不存在解。

## 5. 严格范围

该结果消费的是一个准确有限边界函数，并解出完整无限 Fourier
非线性帽。它不使用该有限函数来源的浮点 BVP 是否收敛。
端口 $c_{\ne0}(L)$ 以外的候选内端 $B$、内端 mean 不是本证明
输入；它们由真实驱动解输出，必须与 body 另作两迹匹配。
右端的 $d_{\ne0},B_0,c_0$ 也保持独立，真正外尾 nonlinear regular
关系尚未代入。原参数区间、primitive 尾及全部均值均不缩减。
