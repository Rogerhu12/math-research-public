# R133 续篇：完整实 δ 外图的固定角解析平移族

2026-11-15，visible-exact-astra-0df9。

**已证明的解析接口。** 对原实族 $|\delta|\le10^{-8}$，把真实 long 方程和曲率图一起拉回到固定基点的外端角，能够得到无权完整 Fourier Hilbert module 上有界、全纯的角平移族。下面给出宽 $1/512$ 上的粗界 $2^{64}$。这只补充解析平移族的存在和粗界；原实轴上的精细小常数仍分别使用已经证明的外图和 O.14。

这里不把纯角复合算子在复平移下视为无权 $L^2$ 有界。未知方向的 bounded extension 由拉回后的完整方程构造。完整 physical $C_R$ 反演、holonomy 小根、$B_0,C_0$ 和外高度列均保留。

## 1. 对象、两个角和真正的已付输入

背景仍是定义 SHA256 为
$440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$
的连续修补中心及原完整方向
$6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04$。
本征参数固定为 $\eta_0$；$\nu$ bump 在整个帽和 long 上为零。

以 $\theta_0$ 表示基点物理角，$\theta_\delta$ 表示 $Q_\delta$ 的自然物理角。在外端 $R=25/8$ 定义
$$
 \theta_\delta=\tau_\delta(\theta_0)
       :=\Theta_\delta(R,\Phi_0(R,\theta_0)),\qquad
 j_\delta=\partial_{\theta_0}\tau_\delta .
 \tag{T.1}
$$
把这一同一个圆周坐标变换沿整个 long 延伸为与 long 径向坐标 $t$ 无关的变换。它不改变任何物理端点或背景。$m_\delta<0$ 始终保留原符号。

[完整实族固定基点帽逆](R133-supplement-complete-real-delta-fixed-base-cap-linear-inverse.md)
及其实际两个 consumer 给
$$
 \|Z\circ\Phi_0\|_{\mathscr A_{1/128},{\rm pair}}<1,\qquad
 |m_0|,|m_\delta|>3 .
$$
本节所用 $\|C_0\|_{A_{1/64}}<1/3$ 只需在准确外端 $R$ 成立。
原 Hs 外图 S.20–S.21 的完整 endpoint 证书在此给 $|m_0|>5.8$、
$\|w_0\|_{A_{1/8}}<10^{-8}$，$w_0=(v_0-m_0)/m_0$。
原已证 $\Phi_0(R)-\mathrm{id}$ 的 $A_{1/64}$ 范数小于
$1.5\,10^{-11}$，所以固定已知复合仍严格落在原 $1/8$ strip。
Neumann 级数直接给
$$
 \|C_0(R)\|_{A_{1/64}}
 \le\frac{1}{5.8(1-10^{-8})}<1/3 .
$$
这没有将 V 中只显式用于 $\mathscr A_0$ 的门扩成未经支付的正宽门。
因此准确恒等式
$$
 j_\delta=
 \frac{1+\delta(Z_v/v_0)\circ\Phi_0}
      {1+\delta\langle Z_v\rangle/m_0}
 \tag{T.2}
$$
给
$$
 \|j_\delta-1\|_{A_{1/128}}<2^{-26},\quad
 \|j_\delta^{-1}\|_{A_{1/128}}<33/32,\quad
 \|(j_\delta)_{\theta_0}\|_{A_{1/256}}<2^{-18}.
 \tag{T.3}
$$
最后一项只用 $x e^{-x/256}\le256$。原角规范还给
$\tau_\delta-\mathrm{id}=(\psi_\delta-\psi_0)\circ\Phi_0$，
其中 $\psi_\delta=I_\varphi(v_\delta/m_\delta-1)$。
用 $I_\varphi$ 的 $1/4$ 因子和同一完整 $Z$ 界可取
$$
 \|\tau_\delta-\mathrm{id}\|_{A_{1/256}}<2^{-26}.
 \tag{T.4}
$$
这里只复合已知解析系数，不对未知方向使用复角复合。

真正 full-$\delta$ 外图的原公开 run 43615531666/1 已给同一物理角中的
$$
 \|C_\delta(R)-C_0(R)\|_{A_{1/64}}
 <3.951\,10^{-20}.
 \tag{T.5}
$$
准确字段为 additional_full_physical_C_change_Aone_sixtyfourth；
完整 native SHA256 是
$5ab1d1b85cb71556b051fd53f5579cb30260ebdda6a844df9a4b377508e057fc$。
它保完整193端值、mean 和复合产生的无限尾。

[原物理帽—尾接口](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md)
L.5–L.6 的实际背景平移界小于 $7.7\,10^{-13}$。
加原连续修补的 $4.970\,10^{-19}$ 及 (T.5)，在宽 $1/128$ 上仍小于
$10^{-12}$。整个实族遂位于同一个真正复背景球
$$
 \|\mathcal Z\|_{A^0}<\bar z=10^{-10},\qquad
 \|f_B\|_{\dot A^2}<\bar b=10^{-11},\qquad
 F=10(\bar z+\bar b)+\bar b=111/10^{11}.
 \tag{T.6}
$$
这里 $\mathcal Z=(C-C_{\rm ref})_{\perp}$，不把它与方向 $Z$ 混同。
若只从两端复平移界读取范数，则分别用 $z=\pm i/128$ 后相加，仍给完整 joint $A_{1/128}$ 输入小于 $2\cdot10^{-12}<\bar z$；不需要把单侧平移范数冒为 joint norm。原 full-fourfold long 定理因而在同宽给 $\|h_\delta\|_{\mathcal Y_{1/128}}<6F$，
这个 $6F$ 是把上述完整 joint 输入直接放进原同宽 weighted Wiener 固定点定理所得；不是先分别取两侧完成解的范数再相加。唯一性把该同宽解识别为原真实背景。其真正 $C_R$ inverse、holonomy 根和两个 mean 均在这个球上定义。

原 L.6 已直接授予自然物理角的平移族；它本身没有授予
$\mathcal C_{\tau_\delta}$ 在 complex $L^2$ 上的有界性。下文支付后一个坐标问题。

## 2. 加权 mean 与同一个完整 Hilbert module

以下写 $x=\theta_0$、$j=j_\delta$，定义
$$
 M_jf=\langle jf\rangle_x,\qquad
 J_jy=y-M_jy,\qquad D_j=j^{-1}\partial_x .
 \tag{T.7}
$$
$\langle j\rangle_x=1$ 是 degree-one 坐标变换的准确恒等式，在复平移后也保持。
若 $\langle y\rangle_x=0$，则 $M_jJ_jy=0$。物理 long 未知的拉回准确为
$h^\flat=J_jy$，而非直接 $h^\flat=y$。

对 ordinary-mean-zero 的 $y$，采用原完整强 Hilbert module
$$
 \|y\|_{\mathcal Y_2}^2=
 \sum_{n\in4\mathbb Z\setminus\{0\}}
 \left(n^2\|y_n\|_\infty+|n|\|(y_n)_t\|_\infty+
                      \|(y_n)_{tt}\|_\infty\right)^2 ,
$$
$$
 \|f\|_{\mathcal F_2}^2=
             \sum_{n\ne0}\|f_n\|_\infty^2 .
 \tag{T.8}
$$
背景对应逐 mode 径向 supremum 后 $\ell^1$ 的 $\mathcal Y_A$。
所有系数、mean 读取和乘法在原平方零代数
$\mathfrak A\oplus\epsilon\mathfrak M$ 中运算；背景与方向相乘有界，
不使用两个未知 Hilbert 方向之积。

准确拉回的 mean-zero primitive 是
$$
 I_j f=
 I_x\{j(f-M_jf)\}
       -M_j I_x\{j(f-M_jf)\}.
 \tag{T.9}
$$
它满足 $D_jI_jf=f-M_jf$ 及 $M_jI_jf=0$。
其模块范数小于2：分别使用 $\|j\|<33/32$、
$\|M_j\|\le33/32$ 和 $\|I_x\|=1/4$。
特别所有 mean 均为真实 $j$-weighted mean，没有按 ordinary Fourier mean 代换。

## 3. 拉回完整 long 主体及小根

[真正长径向 Dirichlet 定理](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
D.6–D.13 的准确式，在本坐标中写成
$$
 P=D_jh^\flat,\quad U=D_jP,\quad
 K_\perp=2h^\flat+h^\flat_t,\quad V=D_jK_\perp,\quad
 K=K_\perp+\kappa ,
$$
$$
 {\cal Q}_j(y)=P_{\perp,x}
 \frac{E(V-P)^2+K^2+2EKU+EU^2-qP^2}{1+K+EU},
 \qquad q=w^2,\quad E=1+q<2 .
 \tag{T.10}
$$
$\kappa$ 是同一 physical holonomy-one 小根，只是所有角平均写为 $M_j$。
原 mean 高度和一个整体高度 gauge 仍按原径向积分恢复。

对于 $R_y=\|y\|_{\mathcal Y_A}\le2^{-20}$，(T.3) 及 $|n|\ge4$ 给
$$
 \|P\|<R_y/3,\quad \|U\|<2R_y,\quad
 \|K_\perp\|<R_y/2,\quad \|V\|<2R_y .
 \tag{T.11}
$$
这里 $\|y\|\le R_y/16$、$\|y_t\|\le R_y/4$，
且 $\partial_x J_jy=\partial_xy$；$j$ 与 $t$ 无关。

为明确小根的统一性，可直接用原可去商
$$
 \Phi_q=
 M_j\left[
 \frac{(1-q\mathcal Z_q)^{-1/2}-1}{q}
 +\frac{(1+K)U}{(1-qP^2)\sqrt{1-q\mathcal Z_q}}\right],
 \quad
 \mathcal Z_q=2K+K^2+EP^2 .
 \tag{T.12}
$$
$q=0$ 时取原幂级数的可去值。
$M_jK_\perp=M_jU=0$，故其线性项仅为 $\kappa$。
在 (T.11) 的球上，完整 binomial 和 reciprocal 级数给
$$
 |\kappa|\le2^{12}R_y^2,\qquad
 \left|\partial_\kappa\Phi_q-1\right|<1/4 .
 \tag{T.13}
$$
一个直接核法是用
$D+q(1+K)^2=E(1-qP^2)$，得到
$\partial_\kappa\Phi_q=M_j[(1+K+EU)D^{-3/2}]$。
再将 (T.12) 的线性 $K_\perp+U$ 先消去，其余平方项总界小于
$2^{11}R_y^2$；半径 $2^{12}R_y^2$ 的固定点保留足够余量。
同一绝对级数证明在平方零 Hilbert module 中逐项成立。

令 $N=\|P\|+\|K\|+\|U\|+\|V\|$。
(T.11)–(T.13) 给 $N<8R_y$，分母大于 $1/2$；
(T.10) 分子的范数不超过 $10N^2$。因此
$$
 \|{\cal Q}_j(y)\|_{\mathcal F_A}<2^{11}R_y^2 .
 \tag{T.14}
$$
ordinary 非mean 投影在 $\ell^1$ 和 $\ell^2$ 中均收缩。原 physical
投影是 $I-M_j$；在对方程再施加 $P_{\perp,x}$ 后，二者的常数差准确消去，
不是删去一个 source mean。

未知强方程准确为
$$
 [(\partial_t+2)^2+\partial_x^2]y
       ={\cal Q}_j(y)-{\cal V}_jy ,
$$
$$
 {\cal V}_j=P_{\perp,x}
 \{(j^{-2}-1)\partial_x^2-j^{-3}j_x\partial_x\},\qquad
 \|{\cal V}_j:\mathcal Y_2\to\mathcal F_2\|<2^{-18}.
 \tag{T.15}
$$
这个源费使用
$\|j^{-2}-1\|<2^{-24}$、
$\|j^{-3}j_x\|<2^{-17}$ 和 $1/4$ 的一阶频率因子。
没有径向坐标导数或新的 $t$ 接缝项。

## 4. 已知背景与完整 Dirichlet 导数

这里允许复合的是已知解析背景 $h_\delta$。
(T.4)、原宽 $1/128$ 和完整链式公式给
$$
 \|P_{\perp,x}(h_\delta\circ\tau_\delta)\|_{\mathcal Y_{A,1/512}}
       <5\,\|h_\delta\|_{\mathcal Y_{A,1/128}}
       <30F<2^{-24}=:r .
 \tag{T.16}
$$
因子5逐项来自
$(h\circ\tau)_x=j(h_\theta\circ\tau)$、
$(h\circ\tau)_{xx}=j^2(h_{\theta\theta}\circ\tau)+j_x(h_\theta\circ\tau)$，
以及没有额外项的 $t,tt$ 导数。
$\|j\|<33/32$、$\|j_x\|<2^{-18}$ 已远小于该宽放；
三个强范数分量求和亦被5覆盖。整个复合域仍严格位于原 $1/128$ 条带。

把平方零方向的复幅度取为 $r$，(T.14) 在 $2r$ 球上的 Cauchy 界给
$$
 \|D{\cal Q}_j(y_{\rm bg}):\mathcal Y_2\to\mathcal F_2\|
       <2^{13}r=2^{-11}.
 \tag{T.17}
$$
原 D.17 的完整 Green 范数小于32，故
$$
 32(2^{-18}+2^{-11})<1/32 .
 \tag{T.18}
$$
这构造了真实 Dirichlet Jacobi inverse，粗 norm 小于64；
原两端 lift 的5和3分别变成小于8和4。
它们是全 signed Fourier 和完整 radial sup module 的结论，
不以任意角截断代替全解。
这里原 D.17–D.18 的各频标量 Green 使用绝对积分核 majorant；joint Wiener 乘法、加权 mean 和 t 无关 j 使用绝对 Fourier 矩阵。先逐频取径向 sup，再由该同一非负矩阵在 ℓ² 中求和，故 (T.18) 的 Neumann 估计确实作用于所定义的 ℓ²(C_t) 强模块。第6节 Hilbert 核界只用于单一 r=R 的端口 L²=ℓ²，不被转授为内部径向 sup 的算子界。

对于 zero-Dirichlet particular，原 D.27 的两端合计
$|n|\,|h_n'|$ 核小于16，故在每个端点
$$
 \|h_t\|_2\le4\|f\|_{\mathcal F_2}.
 \tag{T.19}
$$
它是原 constant-coefficient Green 的实际端导核。
以下将扰动解写回该同一个 Green 后使用 (T.19)，不把完整 $\mathcal Y_2$
的32当成更紧端点核。

## 5. 真正 $C_R$ 反演，保留有限长反射

令 $\chi_R=w_R/a_R<1/5$。
原准确端点公式是
$$
 B=\chi_R\,\frac{V-P}{\sqrt D},\qquad
 C=-\frac{\chi_R}{\sqrt E}\,
                  \frac{1+K+EU}{\sqrt D},\qquad
 D=1-q(2K+K^2+EP^2).
 \tag{T.20}
$$
其完整线性 $C$ 部分为
$-\chi_R\sqrt E(K_\perp+U)$；
不是把 $K$ 的系数误写成 $-\chi_R/\sqrt E$。

由 (T.11)–(T.13)，在 $R_y\le2^{-20}$ 的完整复球，
(T.20) 减去常数和上述线性项后的余项可取
$$
 \|{\cal R}_{C,j}(y)\|_{A^0}<2^{14}R_y^2,\qquad
 \|D{\cal R}_{C,j}(y_{\rm bg})\|_{\mathcal Y_2\to L^2}<2^{-8}.
 \tag{T.21}
$$
其中 $E\kappa$ 的费用不超过 $2^{13}R_y^2$；
其余项由同一 $D^{-1/2}$ 级数的二次尾及 $K U,P^2$ 给出，合计小于
剩余的 $2^{13}R_y^2$。完整 $C_0$ 也在这个余项中，未因输出非mean而先删除。

记 $\mathcal L_C$ 为原真实有限长、constant-angle 的线性曲率图。
原定理给
$\|\mathcal L_C^{-1}:L^2_\perp\to\dot H^2_\perp\|<9$，
包括所有频率、实际 $q_n$ 和严格正长段反射。

对单位右端 $\dot H^2$ 输入，新的 Dirichlet 导数有
$\|\dot y\|_{\mathcal Y_2}<4$。
它与原线性 lift 的差是 zero-Dirichlet particular，故 (T.17)、(T.15)、(T.19) 给
$$
 \|\dot y_t(R)-(\dot y_D)_t(R)\|_2
 \le16(2^{-11}+2^{-18})<2^{-6}.
 \tag{T.22}
$$
另外 $D_j^2-\partial_x^2$ 的端点费用小于 $2^{-18}$；
(T.21) 的非线性曲率导数费用小于 $4\,2^{-8}=2^{-6}$。
由于 $\chi_R\sqrt E<1$，完整 $C_R$ 导数与 $\mathcal L_C$ 的差小于
$2^{-5}+2^{-18}$。因此
$$
 9(2^{-5}+2^{-18})<1/2,\qquad
 \|(D C_R)^{-1}:L^2_\perp\to\dot H^2_\perp\|<18 .
 \tag{T.23}
$$
这是同一真实曲率图的导数反演，不是将旧 $\mathcal L_C$ 的9重新命名。
它保留原 $q_n$，不以 $q_* I$ 或无穷长近似替换参考。

新 graph 的 $\mathcal Z$ 列因而有 long 状态 norm 小于 $4\cdot18<2^7$。
对于左端 $\dot H^2$ 高度输入，先保留小于8的 lift，再用 (T.20)、
(T.23) 解掉它的真实右曲率荷，可统一取 long 状态 norm 小于 $2^{14}$。
这只是粗界，未消去 long 本身的 exponentially small 物理源因子。

完整 $(B,C)$ 端点微分与两种 weighted mean 的范数可各宽放到
$16\|\dot y\|_{\mathcal Y_2}$。因此自然 pulled 曲率 graph 和
$f_B|D_x|^{-2}$ 两列分别有安全界 $2^{11}$ 与 $2^{18}$。
这里 mean 高度的常数 gauge 仍独立；$B_0,C_0$ 是实际曲率输出。

## 6. 回到真实 moving graph 的有界代数，而非裸复合

在共同 $x=\theta_0$ 坐标中，原完整
[DΨ 及其 inverse](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md)
G.4–G.5 的每个角 primitive 都用 (T.9)，每个 physical mean 都用 $M_j$。
因此 natural physical curvature variation 与原 moving variation 的换算，
只由已知解析乘法、$I_x$ 和有限秩 mean 构成。
原 $D\Psi_0$ 的端点换算也同样固定，不含未知的角取值算子。

原实际全δ端点记录还给
$$
 5.8<|m_\delta|<8,\quad
 \|v_\delta-m_\delta\|_{A_{1/8}}<2^{-26},\quad
 \|u_\delta\|_{A_{1/8}}<2^{-28}.
 \tag{T.24}
$$
经同一个已知 $\Phi_0(R)$ 复合，在本宽内可宽放为
$\|\widehat v_\delta-m_\delta\|,\|\widehat u_\delta\|<2^{-25}$，
其一阶导数小于 $2^{-18}$。这些原 endpoint 数值来自 (T.5) 同一实际 summary 的 corrected_moving_U_Aone_eighth、corrected_moving_Vnonmean_Aone_eighth 与两 mean gap 字段；并非新计算。原宽 $1/8$ 支付这些导数，不把未知方向提高一阶。

曲率 nonmean chart 写为 $c^\flat=J_j z+c_0(z)$。
(T.21)、(T.23) 给
$|c_0(z)|< (33/32)\,2^{-8}\cdot72\,\|z\|<\|z\|/2$。
恢复 $h_2$ 后，ordinary 非mean chart 的 leading 部分为
$-m_\delta^2 z$。其余部分来自
$v_\delta^2-m_\delta^2$ 和
$v_\delta^3C_{\delta,\theta}p_c=-m_\delta(v_{\delta,\varphi})p_c$；
(T.9)、(T.24) 给 $\|c^\flat\|<2\|z\|$、$\|p_c\|<16\|z\|$，两项分别小于 $2^{-19}\|z\|$ 和 $2^{-11}\|z\|$；故该余项 norm 小于 $1/4$。
因此这个完整 even chart 的 inverse 可取 $1/16$。
若采用原 moving mean 而非 $x$ mean，只加准确的
$y\mapsto y-\langle\Phi_{0,x}y\rangle_x$；其范数小于2，
完整 inverse 仍可取 $1/8$。独立 moving mean 是
$-m_\delta^2 c_0$，仍为真实有限秩行。

原 $J_\varphi$ 在 $x$ 坐标中的换算也不拆成纯复合。
使用 [完整 Hilbert 共轭](R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md)
L.14–L.18 的准确核及其对角消去式。为给出独立的粗核界，
先令 $X=4x$，将圆周写成 $2\pi$ 周期，并把准确外端坐标写为
$F(X)=X+e(X)$。原 endpoint 条带预算在整个
$|\operatorname{Im}z|\le1/512$ 上远强于
$\|e'\|,\|e''\|<\epsilon:=1/16$；
此处的 $e''$ 已包含从 $x$ 到 $X$ 的 $1/4$ 因子。

对 $s=X-Y\in[-\pi,\pi]$，
$F(X)-F(Y)=s(1+\bar e')$，故其绝对值小于 $17\pi/16<3\pi/2$。
消去极点的
$$
 R(s)=\cot(s/2)-2/s
       =4s\sum_{k\ge1}(s^2-4\pi^2k^2)^{-1}
$$
在整个复圆盘 $|s|\le3\pi/2$ 有
$$
 |R(s)|\le\frac{3}{2\pi}
       \left(\frac{16}{7}+\frac{128}{165}\right)<2,\qquad
 |R'(s)|\le\frac1{\pi^2}
       \left(\frac{400}{49}+\frac{9344}{9075}\right)<2 .
$$
这些式子将 $k=1$ 分离，其余用
$\sum_{k\ge2}k^{-2}<2/3$；故为完整级数的复域上界。
真正差核的 pole 部分由原积分消去式小于
$2\epsilon/(1-\epsilon)$，regular 部分小于
$2\epsilon+2\pi\epsilon$。总和小于2。
归一圆周测度上这给差算子 $L^2$ norm 小于2，
加原 $J$ 的1后小于 $3<4<16$。
这个核在 lift 切换处仍准确周期；没有额外接缝源。
因此完整 Hilbert family 可安全取16，
不需要保留原 $7.190442\,10^{-9}$ 的精细数值。

由上述 chart、完整曲率 graph、真正 Hilbert 行和固定 gauge 换算，
原 O 篇中的 $\mathcal E_\delta$、真实 mean 行及其完整外高度列，
在固定角中的同一个准确表示均有粗界小于 $2^{32}$；
将全部未显示的输入/输出 chart 和独立 mean 一起计入 $2^{64}$。
该构造先给完整四重周期方向的 bounded extension，
再限制回原奇/偶反射类。$B_0$ 行始终保存，只有在原反射方向才准确为零。

## 7. 全纯平移族与 input 身份

现在仅平移共同 $x$ 坐标的所有已知系数：
$j(x)\mapsto j(x+z)$、背景 $y_{\rm bg}(t,x)\mapsto y_{\rm bg}(t,x+z)$，
并平移真正 mean functional 的系数。$\langle j_z\rangle=1$。
(T.3)–(T.24) 在 $|\operatorname{Im}z|\le1/512$ 上一致成立。
原 constant-coefficient Green 和 $\mathcal L_C^{-1}$ 与角平移对易；
两个 Neumann inverse 的余量一致。
因此所构造完整外图 $\mathcal T_{\delta,z}$ 是有界算子值全纯族，且
$$
 \sup_{\delta\in[-10^{-8},10^{-8}]}
 \sup_{|\operatorname{Im}z|\le1/512}
       \|\mathcal T_{\delta,z}\|<2^{64}.
 \tag{T.25}
$$
在有限 Fourier 输入上，真实拉回方程及其唯一性给
$\mathcal T_{\delta,z}=C_z\mathcal T_{\delta,0}C_{-z}$；
随后使用 (T.25) 完成无权 Hilbert module 延拓。
此恒等式没有单独延拓 $C_z$ 或任何 nonlinear angle composition。

外高度 input 的准确坐标是
$y_B=P_{\perp,x}(f_B\circ\tau_\delta)$，
归一化列为 $y_B=|D_x|^{-2}g_B$、$g_B\in L^2_\perp$。
这是同一个真实高度方向的 pulled chart。
若最终源仍用原 $\theta_\delta$ 角的 $H^{s+2}$ norm，
必须再支付真实实角 pullback 及其密度伴随的有限 Sobolev 费用；
本条不把该 conversion 宣称为 complex $M_0$ 中的裸有界复合。
整体常高度继续独立。

把本条 bounded row family 与已付固定基点源 lift 的 bounded analytic
family 复合，只需乘各自粗界。特别当该基点 ordinary/divergence lift
在所用更窄 strip 上的界小于 $2^{16}$、固定端口系数界小于 $2^{16}$ 时，
包含两份外图差及全部原 mean 的 outer-feedback analytic family
可以统一取 $2^{128}$。实轴 small norm 仍直接使用原 O.14；
这里不拿 $2^{128}$ 作 Neumann smallness。

## 8. 范围

本条补齐的是 whole-real-δ、同固定角、全频 true regular boundary
的 analytic-family 粗门；未复算任何旧 target、long 解、端点或 cap cell。
所有新不等式是原完整核和准确方程的符号推导。

它不授予任意附近非线性背景的同域解图，不改变原 affine 数据的单位，
也不把未知角方向限制为193态。高阶或负阶 Sobolev 门还须实际消费
对应的 signed-lag/shifted-weight lemma 并付实角 source conversion。
完整 inner-body/negative-high/ν Schur 和最终闭等距族仍须各自完成。
