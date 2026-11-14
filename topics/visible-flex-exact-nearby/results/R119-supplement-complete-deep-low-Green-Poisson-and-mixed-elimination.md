# R119 续篇：真实深低外侧的完整 Green、双向 Poisson 与 mixed 消元

2026-11-14，visible-exact / tail_connector。

**状态：解析证明；完整根架、真实边界与原源单位已独立核对。** 本篇使用当前实际
$\Gamma^*(\mathbf a,\Omega)$，消去全部深层、非零频率的真正 low
外侧。没有假定整个近核事先落在一个局部 incoming 包，也没有
把无限多个低胞元当作有限个谱窗口。

本篇的未知空间仍是完整 root-Airy incoming；高外先按
[已修正外口范围的高外定理](R119-supplement-unitary-high-exterior-Poisson-and-buffered-angular-projections.md)
消去。未覆盖外口保持输入/输出，不给它添加反射。
所有 canonical 零模、有限浅前缀以及实际中频继续保留。
物理 mean 的恢复仍是原完整乘子公式，不能把它认成 canonical
的纯零模。

置
$$
 A_j=2^{-40}\delta_j^{-1/8},\qquad
 \delta_j=(2/25)2^{-j},\qquad J=j+5,\qquad
 F_j=2^{4096}J^4\delta_j^{-5}.                            \tag{L.1}
$$
$P_D$ 是所有 $j\ge8193$、$0<|m|\le A_j$ 的完整负窗 incoming
投影，两个端口同时保留；$m\in4\mathbb Z$。一个窗的根可以位于
相邻胞元，以下所有胞元账保留这一个邻层缓冲。

设高外后的内部算子为 $S_H$，则
$D_a=P_DS_{H,a}P_D$ 的真实 inverse 满足
$$
 \|wF^{-1}(I-D_a)^{-1}F^{-1}w^{-1}\|<2^{66}.             \tag{L.2}
$$
这里是明定的加权源到状态空间：源要提供 $\|wFg_D\|$，
状态在 $\|wF^{-1}x_D\|$ 中读取；不是宣称裸 $L^2$ 全源 inverse
有统一常数。对 $w=v$、$v^{-1}$ 均成立，其中
$$
 v_j=2^{-432000}J^{-4165}\delta_j^{1073/32}
$$
是已经选择的谱权下包络，没有重新挑选一个有利层权。

相应两个真实 Poisson，以仍保留的**内部**未知为输入、输出，
满足
$$
 \|wF^{-1}E_{D,a}w^{-1}\|,
 \quad \|wF_{D,a}F^{-1}w^{-1}\|<2^{130}.                 \tag{L.3}
$$
外端口和所有 affine 源按第8节的完整公式保留。
最终 low/high 消元后的内部 actual-minus-radial 差满足
$$
 \boxed{\quad
 \|v^{-1}(S_{\rm rem,a}-S_{\rm rem,0})v^{-1}\|
                                      <2^{-6000000}.
 \quad}                                                  \tag{L.4}
$$
本式尚不反演 remaining：有限浅前缀及真实物理 mean/原源权仍需
联立处理，见第9节。

## 1. 真 p*=1 接缝：没有逐层的虚假 delta 条件数

采用
[当前全标签与 raw 入口](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
(C.8)--(C.12),(C.34),(C.40)--(C.48)。
本节固定非零 $m$，$M=|m|\ge4$，并先取径向参考。
写
$$
 k=\sqrt{7M^2-16},\quad
 \nu=M^2(M^2-1)/12,\quad k_m=(M^2-4)/\sqrt{12}.
$$
在每胞 $p_*=1$ 的真正接缝，canonical 两态为
$$
 W=\left(\nu H/r^4,\,
       (H_t-M^2H)/(\sqrt{12}r^4)\right)^T,
 \qquad h=\rho H,\qquad \mu_0=\mu_j/(\rho r^8).
$$
设 $u=\sqrt{\mu_0}h$、$Y=(\sqrt k\,u,u_t/\sqrt k)$。
直接代入，而非使用粗 Cauchy 条件数，得到
$$
 Y=\sqrt{\rho\mu_j}\,C_mW,\qquad
 C_m=
 \begin{pmatrix}
 \sqrt k/\nu&0\\
 (M^2-4)/(\nu\sqrt k)&\sqrt{12}/\sqrt k
 \end{pmatrix},
 \qquad \det C_m=\sqrt{12}/\nu .                          \tag{L.5}
$$
特别 $C_m$ 不依赖 $j,\delta_j,r$。
原 $c_j\mu_j=\mu_{j-1}$ 与末行除以 $c_j$ 给真正物理单元传递
$$
                  Y_{j-1}=\sqrt{c_j}\,C_mB_jC_m^{-1}Y_j,
 \qquad \det(\sqrt{c_j}\,C_mB_jC_m^{-1})=1.              \tag{L.6}
$$
因此不能在每个胞元之间再乘一个粗 $\delta_j^{-16}$ 端口费。

深层 $c_j=C=16\sqrt2$、$\mathsf K=2^{128}$。
用原精确实特征基 $E_m$，其两列属于 $-B^\infty$ 的大、小根，
$\|E_m^{\pm1}\|_\infty<2$、$\det E_m>0$。令
$$
 z_j=(-1)^j\sqrt{\rho\mu_j\sqrt{12}\det E_m/\nu}\ E_m^{-1}W_j.
 \tag{L.7}
$$
它与 $Y$ 有相同实 Green pairing。齐次递推准确为
$$
 z_{j-1}=\mathcal B_jz_j,\qquad
 \mathcal B_j=-\sqrt C\,E_m^{-1}B_jE_m,\qquad
                         \det\mathcal B_j=1 .           \tag{L.8}
$$
这里的负号只是整胞交替标记，对 norm 和 pairing 无影响。

## 2. 真锥给两侧指数核，不只给一个理想大根

令
$$
 n(M)=\min\{j\ge8193:M\le A_j\}.
$$
它是有限整数；整个 $j\ge n(M)$ 都处于真实低窗。
原 (C.34) 给
$$
 \|\mathcal B_j-\operatorname{diag}(a,a^{-1})\|/a
     <2^{-11},\qquad
 a=\sqrt C\,\Lambda_m>2^{126}M^4 .                       \tag{L.9}
$$
原真行列式始终为1，不能将第二行的误差另当作一个自由大块。

以下是所用锥证明的完整机制。外向 $\mathcal B_j$ 保持
$|z_2|\le|z_1|/8$，在该锥的第一坐标至少放大 $a/2$。
其 projective derivative 是
$\det\mathcal B_j/(\mathcal B_{11}+\mathcal B_{12}s)^2$，
故绝对值小于 $4/a^2$。从任意真正深端允许线逐次向外取极限，
得到同一个已构造的真实无限尾线 $u_j$，且 $u_{j,1}=1$、
$|u_{j,2}|<1/8$。这与 (C.34)--(C.35) 的强尾允许线一致，
不是一个新指定的理想末端条件。

反向 $\mathcal B_j^{-1}$ 保持 $|z_1|\le|z_2|/8$。
从第一切口的 $(0,1)$ 向内传播，给互补线 $v_j$。
两条线的基及逆 norm 小于4；每次沿其衰减方向的因子小于
$8/a$。这是同时使用准确 determinant 和两个真锥的指数二分。
下文可统一放宽为
$$
                    q_M=2^{-100}M^{-4}<2^{-108}.         \tag{L.10}
$$
对有源递推，先沿 $v$ 行从未来求和，再沿 $u$ 行从第一切口求和。
其每个 scalar Green 核至多 $2^8q_M^{|j-k|}$。
第一基点取第 $n(M)-1$ 个真 $p_*=1$ 接缝。
左边界若为 $c_u u_{n-1}+c_v v_{n-1}=b$，还准确产生
$(c_v/c_u)q_M^{j+k-2(n-1)}$ 的 rank-one 核，以及
$(b/c_u)q_M^{j-(n-1)}$ 的齐次项。
下一节将真实边界的这两个量付清；写回窗编号的固定偏移在第4节保留。

这些式子可先在任意有限终点 $N$ 上，用同一真实允许线截断；
所有常数与 $N$ 无关，极限给真正无限尾。
源通过同一个收敛核进入，没有令 $j>N$ 的真实源等于零。

## 3. 每个实际根的完整两行恢复和边界下界

原四个根全在未修改的上升 quintic germ 中。
完整参考 canonical 光学变量满足
$$
 \alpha_e=b_e\mu_0(t_e),\quad
 |\ell_{\xi,e}|<8,\quad
 \delta_j^{-9/4}<b_e<2^{16}\sqrt J\,\delta_j^{-9/4}.
$$
真实两迹是
$$
 u_e=\sqrt{\rho\mu_jb_ep_e}\,W_{1,e}/\nu,\qquad
 (u_\xi)_e=\tfrac12\ell_{\xi,e}u_e+
 \varsigma_e\sqrt{\rho\mu_j}
 \left(\frac{\sqrt{12}}{\sqrt{b_ep_e}}W_{2,e}
        +\frac{M^2\sqrt{p_e}}{\sqrt{b_e}\nu}W_{1,e}\right).
                                                               \tag{L.11}
$$
右根 $\varsigma_e=-1$ 保留。对 total flux，另加入原真实端点
weak charge；不通过对 $F^t$ 求导制造额外源。

用完整自由 Airy $F_m(0)$ 的两列和导数，而非 height 单行，
$$
 |F_m(0)^{-1}(u,u_\xi)|
       \le2^{16}\{\kappa^{1/3}|u|+\kappa^{-1/3}|u_\xi|\},
 \qquad \kappa=M/b_e .
$$
原 (C.12) 对任意内部子段的正逆 canonical 流小于
$2^{141}M^4$，且 $\delta/2\le p\le2^{128}/\delta$。
将 (L.7),(L.11) 代入后，四个可能的最大幂依次为
$$
 \delta^{-7/6},\quad \delta^{-31/12},
       \quad\delta^{-5/6},\quad\delta^{-7/12}.
$$
例如最强的一项是 $M^{5/3}b^{5/6}\sqrt p$，
在 $M\le A_j$ 上正好至多常数乘 $J^{5/12}\delta^{-31/12}$。
所有上述显示常数、两行和固定 Green 归一化合计少于 $2^{300}$。
因此任一接缝到胞内根的完整正逆 frame 都满足
$$
                 \|\mathcal L_{j,e}^{\pm1}\|
                <G_j:=2^{2048}J^2\delta_j^{-11/4}.      \tag{L.12}
$$
逆界不是重新乘两个条件数：两个实两态具有同一个 Green pairing，
自由波列的固定行列式为 $-2ic^2/\pi$，付该固定常数后正逆
$2\times2$ 矩阵 norm 相等。这没有使用旧的错误 $b^{1/2}$ 低频架。

还须给真正允许线的边界下界。先明确这里的坐标换算。
(L.9) 的锥首先属于 $z$，不能只用 $\|E_m^{\pm1}\|<2$
就把它称为原 $W$ 锥。写 $\epsilon=2^{-11}$，一次真实向外映射给
$$
 \left|\frac{(\mathcal Bz)_2}{(\mathcal Bz)_1}\right|
 \le\frac{\epsilon+(a^{-2}+\epsilon)/8}
           {1-\epsilon-\epsilon/8}<2^{-10}
 \qquad (|z_2/z_1|\le1/8).
 \tag{L.12a}
$$
因此无限尾允许线在每个所用接缝都满足这个更窄的锥。
原精确特征基（强全标签篇 U.7--U.8）为
$$
 E_m=\begin{pmatrix}1&t_m\\s_m&1\end{pmatrix},
 \qquad -1/16<s_m<0,\qquad 0<t_m<1/(\mathsf K-1)<1/63.
$$
以 (L.7) 中同一个非零标量恢复 $W$，得到
$$
 \left|\frac{W_2}{W_1}\right|
 \le\frac{1/16+2^{-10}}{1-2^{-10}/63}<1/8,
 \qquad
 |W_1|>(1-2^{-15})\,|\text{该标量}\ z_1|.
 \tag{L.12b}
$$
所以下面 $(u,su)$、$|s|<1/8$ **确实指原 canonical 两态
$W$**，其中 $u=W_1$；不把 $u$ 与前面的密度高度同名变量混用。
此处至多付固定因子2，已包含在 (L.13) 的301 bits内。
这个压窄只用于真正允许的 $u$ 线；反向互补 $v$ 线、边界的
$c_v$ 项及其完整 affine 源仍全部保留，并由 (L.12) 收费。
准确平台的 sin/cos 式与短段的有序积分给：

* 第一上升段两个根，$|W_1|\ge|u|/2$、$p\ge1/2$；
* 第二上升段两个根，$|W_1|\ge\mathsf K\alpha\nu|u|/4$、
  $p\ge\delta/2$。

为明确这不是对完整大乘积用绝对误差猜测：第一峰前短段用
$(W_1,W_2)$；第一峰后到谷底用 $(W_1,W_2/\mathsf K)$；
谷底平台后用 $(W_1/(\mathsf K\alpha\nu),W_2/\mathsf K)$。
在相应三种尺度中，所有插入短段及平台 sin/cos 修正之和小于
$2^{12}\mathsf K M^4\sqrt\delta\le2^{-20}$。
第一高平台给 $W_2=-\mathsf K u$ 加该相对误差；
谷底平台给 $W_1=-\mathsf K\alpha\nu u$ 加该相对误差。
因而上述两个严格高度下界都保留，未把中间的小反剪切删掉。
这同样覆盖第一切口的一个邻胞：其频率超出 $A_{j-1}$
最多 $2^{1/8}$，上述误差仍小于 $2^{-19}$。
当邻胞为8192时使用其真实 $K=64$、同一 $c=C$，
直接把 (L.12b) 的原 $W$ 锥作为该胞输入。若改回旧
$E_{64,C}$ 坐标，仍完整乘原准确接缝 $Q_2$；本证明不需把它
设为恒等，也不从两个粗基范数推导一个更窄的锥。
此时第一峰后准确保留 $W_2=(s-K)u$ 的原 $s$ 项，
谷底后的主项准确为 $(1-K\alpha\nu)u+\alpha\nu su$。
不能遗漏其中的 $+u$，也不把 $s/K$ 错算成 $2^{-19}$：
$1/(K\alpha\nu)<1/1280$ 与 $|s|/K<1/512$ 的和，
连同已付短段误差，足以保留上述 $1/4$ 高度下界，
最多再固定放宽2。

对于实两态，两个自由波幅互为共轭，所以每一个 incoming 的
模长是完整波对 norm 的 $1/\sqrt2$。
仅从 height 一行
$|u_e|\le2^3\kappa^{-1/3}|a_e|$，上述两个根类分别给
常数乘 $\delta^{-1/6}$ 与 $\delta^{1/8}$ 的下界。
以第 $n-1$ 个接缝 (L.7) 为基，实际外端 incoming
在真正允许线上的系数满足
$$
 |c_u|\ge2^{-301}\delta_n^{1/8},\qquad
 |c_v|\le2G_n,\qquad
 |c_v/c_u|<2^{2350}J_n^2\delta_n^{-23/8}.                \tag{L.13}
$$
这是固定真实 root 端口的边界条件；没有把传入线除以 height，
也没有改变外部 Robin。径向共同酉 $H_0$ 逐频、逐根仅乘相位，
故该下界在当前 root 表示仍成立。

## 4. 全部 root 源、真正 Green 核和 radial Poisson

对一个 root incoming 残差 $g$，先用负窗的真实 incoming 构造
负段解，再用其 outgoing 作为正段 incoming 构造正段解。
两片在每根仅有一条 wave 坐标差，正是 $g$。
所以完整 $(I-U_0)x=g$ 等价于真实分段 ODE 加这些原位两态跳；
无需倒除 positive tiny transmission。
每个跳按 (L.12) 变为接缝两态源，再用 (L.10) 传播。

一个负窗的两根最多跨两个相邻胞元，因此将 cell 核写回原窗口
编号时，至多先出现 $q_M^{(|j-k|-2)_+}$。
这项也必须付费：$q_M^{-2}=2^{200}M^8$，
且 $M^8\le\delta_{\min(j,k)}^{-1}$。
边界 rank-one 项再乘 (L.13)；从 $G_jG_k$ 升为 $F_jF_k$
时的额外比是
$$
 {F_jF_k\over G_jG_k}
       =2^{4096}J_j^2J_k^2\delta_j^{-9/4}\delta_k^{-9/4}.
$$
它覆盖全部上述常数及幂：
$23/8+1=31/8<9/2$，显示的常数最多
$2350+200+128<4096$。因此真正 radial inverse 的全部根块有
$$
                  |(R_{D,0})_{jk}(m)|
                     \le F_jF_k q_M^{|j-k|}.            \tag{L.14}
$$
每层两个窗、每窗两个 incoming 的固定计数包含在这128 bits中。
本式也控制源所在同一胞元的完整 particular 项。

在深层允许任一正层权 $w$ 满足相邻比在 $[2^{-48},2^{48}]$。
(L.14) 的行列几何和给
$$
                    \|wF^{-1}R_{D,0}F^{-1}w^{-1}\|
                                                   <2^{64}. \tag{L.15}
$$
$v$、$v^{-1}$ 及下一节与 $F$ 的乘积均满足这个实际范围；
例如 $j\ge8192$ 时 $v_j/v_{j+1}<2^{35}$，
$F_{j+1}/F_j<2^6$。

同样由 (L.13)，齐次输入的真实根输出不超过
$2^{301}G_j\delta_n^{-1/8}q_M^{(j-n-2)_+}$。
$F_j/G_j=2^{2048}J_j^2\delta_j^{-9/4}$
已覆盖 $q_M^{-2}$、$\delta_n^{-1/8}$ 及所有固定邻层比，
因为 $1+1/8<9/4$。所以径向右 Poisson 满足
$$
            \|wF^{-1}E_{D,0}w^{-1}\|<2^{128}.           \tag{L.16}
$$
其输入为所有仍保留的内部未知；对固定 $m$，仅真正相邻的第一
外端口参加该式。其余输入列准确零，不是凭局部化假设删去。

左 Poisson 同样成立。一个直接验证是使用真实 reciprocity：
径向 $S_-$ 与 $R_+$ 的散射矩阵均对称，故
$U_0^*=\overline S_-\,\overline U_0\,\overline S_-^*$。
$P_D$ 包含整个负窗的两条 incoming，因而与径向 $\overline S_-$
交换；层权和 $F$ 在同一窗也为标量。
这把 adjoint 的 Poisson 准确化成 (L.16) 的共轭加两个 unitary。
若相邻根采用邻胞权，固定比仍落在已经付过的128 bits中。
于是
$$
                  \|wF_{D,0}F^{-1}w^{-1}\|<2^{128}.     \tag{L.17}
$$
这不是把逐模正型当成 mixed 块；径向这里只用于构造参考 inverse，
下一节才消费真实非径向全差。

## 5. 已消 high 与 deep-low 之间的准确分离

原径向网络只连接真实相邻窗口，并逐 Fourier 对角。
对于 $M\le A_j$ 及 $|k-j|\le2$，严格有 $M<T_k$；
例如 $T_k/A_j>2^{65000}$。
所以 high 直接交叉块的相应列和行准确为0。由真实 high inverse，
$$
                   E_{H,0}P_D=0,\qquad P_DF_{H,0}=0.    \tag{L.18}
$$
这不是对实际 mixed 网络作逐模化；actual 的这些块一般非零。

令 $\Delta U=\widehat U_a-\widehat U_0$。
[完整 root-wave 差](R119-supplement-complete-root-wave-network-and-high-Schur-difference.md)
(V.1) 给 forward 及 adjoint 一阶门
$$
 \epsilon_j=2^{35000}J^{40}\delta_j^{-47}\mathcal N_j\mathcal X,
 \qquad \mathcal X\le2^{-8388608}.                       \tag{L.19}
$$
值 $\Gamma^*-\bar\Gamma$、完整图及 shear 已在该门中；
其参数导数作为源列，未被设为零。

准确 high Schur 恒等式有两个有序版本。
用 (L.18)，对于 deep-low 输入或输出分别得到
$$
 \Delta S_H P_D=[I,F_{H,a}]\Delta U P_D,\qquad
 P_D\Delta S_H=P_D\Delta U[I;E_{H,a}].                    \tag{L.20}
$$
第二式的 norm 用 (L.19) 的 adjoint 门。
因此只要一个端口属于 $P_D$，相应一次角导可付
$\langle M\rangle<2A_j$；无需再收 $T_j$。
这同时处理从整个 retained 内部空间进入 low 的 mixed 列，
没有假设其输入频率先小于 $A_j$。

## 6. 当前 actual 的 low inverse 与双 Poisson

高外修订篇已经明确：这里的 strong 窗仅用于已覆盖内部未知，
外输入继续作为真实 affine 源。记
$\Delta D=P_D\Delta S_HP_D$。
为使用已经消去的 high，先在**全部已覆盖内部层**定义
同一 $F_j=2^{4096}J^4\delta_j^{-5}$，不在 $P_D$ 边界把它
突然改为1。高外篇 (H.12)--(H.19) 适用于任何真实相邻块比
不超过 $2^{256}$ 的层权。对 $w=1,v,v^{-1}$，以及
$wF^{\pm1},wF^{\pm2}$，单层比小于 $2^{92}$，实际距离至多2
的块比小于 $2^{184}$。因而同一个 $2^{-9000}$ Poisson 门在
这些权下都成立；它控制完整高 resolvent 的全部长程传播。

例如第一个 (L.20) 在 $wF$ 下先因式分解为
$(wF)[I,F_{H,a}](wF)^{-1}$ 与剩下的 $\Delta U$ 项。
前一个因素的 norm 小于2；后一个才使用 (L.19) 的有限邻接
行列和及 low 端的一次角导。另一个有序式及 adjoint 完全同样。
这里**不声称** $\Delta S_H$ 在高消元以后仍只有有限邻接。
由此得到
$$
 \|wF\Delta D Fw^{-1}\|
 \le\sum_{j\ge8192}
  2^{50000}J^{64}\delta_j^{-58}\mathcal N_j\mathcal X
 <2^{-7000000}.                                         \tag{L.21}
$$
这里 $47+1/8+10<58$；两份 $F$ 的8192 bits、相邻权和四种
端口均落在50000。深端先保留
$\mathcal N_j<2^{-20010}2^{-(31867/256)(j-8193)}$，
其与 $\delta^{-58}$ 的余幂大于66；8192的实际旧规范由原 (W.8)
支付，不借用未到该层的深指数。
第一深层二进制上界小于
$50000+64\cdot14+58\cdot8197-20010-8388608<-7800000$，
后续几何和及相邻项仍远小于所写门。

将 (L.15) 与 (L.21) 合成，真正 Neumann inverse 给 (L.2)。
先对有限层、有限 Fourier 源证明，再在
$\|wFg_D\|$ 与 $\|wF^{-1}x_D\|$ 两个明确空间中取极限。
另取 $w=1$ 时，齐次裸 $L^2$ 解包含在后一空间，
故没有另漏一个裸 $L^2$ 未知核；不声称任意裸 $L^2$ 向量
都自动具有 $v^{-1}F^{-1}$ 权。

对于交叉列，用
$$
 E_{D,a}=E_{D,0}
       +R_{D,a}(\Delta C+\Delta D\,E_{D,0}).              \tag{L.22}
$$
(L.20) 的输出低门给 $wF\Delta Cw^{-1}$ 同样的小界；
对第二项用 (L.21) 和 (L.16)。因此 (L.3) 的输入 Poisson 门成立。
对 adjoint 重复这个确切源空间论证，给其左式。
actual 的 $P_D$ 不与角乘子交换；所有这些 mixed 项都经
$\Delta C,\Delta D$ 保留在同一个 Neumann 系统中。

## 7. 两外消去后的完整差及真正层权

只在两端均为已覆盖内部 retained 未知的压缩中写
$$
 \Delta S_{\rm rem}
       =[I,F_{D,a}]\,\Delta S_H\,[I;E_{D,0}].            \tag{L.23}
$$
未覆盖外列另见第8节。将右边展开成四项：

* 没有 $E_D,F_D$ 的项，用 (V.2) 已付 $2^{-6000000}$ 的内部差；
* 只有一侧 low Poisson 的项，使用 (L.20)，一次角导是 $A_j$，
  再收一份 $F_j$；
* 两侧都有的项，收两份 $F_j$，一次角导仍是 $A_j$。

原谱权准确为
$v_j^{-2}=2^{864000}J^{8330}\delta_j^{-1073/16}$。
因此后三项的最大实际幂为
$$
                47+\frac18+10+\frac{1073}{16}
                     =\frac{1987}{16}=124+\frac3{16}.   \tag{L.24}
$$
两个 (L.3) 的260 bits、两份 $F$ 的8192 bits、(L.19) 的35000
以及谱权的864000和所有 fixed-degree 行列因素，均小于1200000；
$40+8+8330<8400$。所以每层可统一收
$$
       2^{1200000}J^{8400}\delta_j^{-1987/16}
                                  \mathcal N_j\mathcal X. \tag{L.25}
$$
深端的真实剩余幂是
$$
          \frac{31867}{256}-\frac{1987}{16}
                         =\frac{75}{256}>0 .             \tag{L.26}
$$
它很小，不能在第8193层直接假定多项式比已被吸收。
在 $8193\le j\le65536$ 用 $J<2^{17}$，保留
$\delta^{-1987/16}\mathcal N$ 的真实下降，首端指数严格小于
$$
 1200000+8400\cdot17+\frac{1987\cdot8197}{16}
                  -20010-8388608<-6047000 .              \tag{L.27}
$$
在 $j\ge65536$，由 $\log2>2/3$ 得
$(1+1/J)^{8400}<2^{1/4}$，于是净比至多 $2^{-11/256}$。
完整有限和、深尾几何和、相邻缓冲和四项计数仍给小于
$2^{-6000100}$。未到8193的至多两个邻胞，直接用原 (W.8)
第二段规范；同一个二进制预算还有超过四万 bits 的余量。

最后，没有 Poisson 的直接项不能仅把先前已粗化的
$2^{-6000000}$ 与正数相加后仍写同一严格界：
回用 (V.21)--(V.22) 的未粗化指数，它们各小于
$-6273000$；其真实有限和仍小于 $2^{-6200000}$。
将其与上述三项相加，准确得到 (L.4)。

这一步处理的是整个 mixed 低外及全部原高外响应，未把一个
局部 PSD 方向替代完整网络，也没有删除一个中间频带。

## 8. 完整 ordinary、weak、Gamma 与外端口

把原源按真实 root/strict/graph/positive 接线写成 $\widehat g$。
高外先保留
$g_L^H=\widehat g_L+F_H\widehat g_H$ 和
$x_H=E_Hx_L+R_H\widehat g_H$，其高源仍须满足原一阶门。

再分 $g_L^H=(g_{\rm rem},g_D)$，设外输入给 low 行的真实列为
$C_Xx_X$，则
$$
 \begin{split}
 (I-S_{\rm rem})x_{\rm rem}
       &=g_{\rm rem}+F_Dg_D+
                     (A_{{\rm rem},X}+F_DC_X)x_X,\\
 x_D&=E_Dx_{\rm rem}+R_D(g_D+C_Xx_X),\\
 y_X&=A_{X,{\rm rem}}x_{\rm rem}+A_{XX}x_X+B_Xx_D .
 \end{split}                                           \tag{L.28}
$$
$R_D$ 要消费 $\|wF(g_D+C_Xx_X)\|$。没有把任意 $L^2$ 外输入
授予这个新源 norm，也没有将真实外输出关成固定反射。

ordinary 原两态仍是 (C.42)--(C.43)，保留 $\mu p_*^2$；
weak 原两态保留 $F^t,F^\theta$ 和 total flux。
若消费者要求 bare Airy 两迹，真实 $F^t$ 端点 charge 必须另付。
每个实际径向或材料 jump 都作为上述原位两态源进入同一个核。

canonical $m=0$ 不在 $P_D$。物理 mean 高度、mean 通量和它们
被非径向 $\alpha_e$ 混合出的非零分量，仍由原 (J.39)--(J.40)
及本篇 $E_D,R_D$ 准确恢复；没有以纯零模替代物理 mean。
两列 $D\Gamma^*$、current-parameter/source 变化以及端角微分
均在 $\widehat g$ 中分别保留；微分共同 $H^*$ 时仍加
$\dot H^*g$ 与相应状态坐标项。本篇没有令这些列为0。

## 9. 精确已闭范围与下一阻塞

这里已给同一实际背景上的真正无限 deep-low 两向 inverse、
两个实际 mixed Poisson 和完整 affine 消元。
证明使用真实锥、完整两行根架、实际 high 两窗和全差，
未以逐频采样替代无限量词，不需要新的数值门。

remaining 仍包含129--8192的浅前缀和真正 mean 子系统。
五盒径向谱选择先前已经精确消去了这些真实外侧；
它给的是该有效矩阵的谱门，不是本篇裸 remaining 的 inverse。
要把两者联立，仍须对真实浅外响应和 mean/joint 源作同一单位、
同一参数的完整消费。尤其不能因 $M\ge M_*$ 就把整个浅前缀
冒称满足 $M\ge T_j$。

原普通/weak 源到 (L.2) 的 $F$ 权、完整标签权及两列
$D\Gamma^*$ 的最终联立范数也未被仅列出公式自动付清。
本篇不宣布 $\mathcal F=0$ 或本课题完成；下一项继续这些真实门。
