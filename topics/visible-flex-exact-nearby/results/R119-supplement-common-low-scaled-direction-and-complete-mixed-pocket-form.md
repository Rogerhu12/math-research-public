# R119 续篇：一条共同低缩放方向及完整混频负窗型

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 在同一个原允许控制族内，可以为整个
$M\in[U/2,U]$、$U^2\le B/4$ 的频带使用同一条真实两相位
annihilator 方向。它在当前完整有限参数盒和当前
$\Gamma^*(\mathbf a,\Omega)$ 上，对中心频带全部两迹及 flux
mean 同时给正定 crossing form。各模式之间的实际交叉项
由一个完整能量估计支付，未以单模 PSD 推混模 PSD。
物理常高度是准确 null 槽，仍作为独立高度 mean 保留。

结论是实际整个负窗的型；输出仍有全部 Fourier 模和两个
mean。它不是已经定位好的 whole-network near-kernel：
带外中心输入、不同窗口的共同参数布局、physical principal
端口识别及 source-to-label 全网逆，仍须接入。完整外方程
$\mathcal F=0$ 未由本文自行得到。

## 1. 同一对象与共同方向的定义

沿用第67--72束的
$$
 j\ge8193,\quad J=j+5,\quad
 \delta=\delta_j,\quad
 a=\Delta/B,\quad80<\Delta<3J,\quad
 B>2^{190},\quad K=2^{6000}J^8\delta^{-16}.
$$
本篇不加强 $\Delta$ 的下界。控制起点在原未占用区间
$I\subset[7/16,15/32]$，其长度满足原
$\ell>2^{-31}J^{-2}$。在此处
$$
 Q=7+Bf(x),\quad f=30x^2(1-x)^2,\quad dt=a\,dx.
$$
暂将 $\tau=1/\Delta$、$e=1/B$、$\kappa=M^2/B$，以及
$$
 F=f+7e,\qquad
 p_1=F^3F',\qquad
 p_2=(12F^4-8eF^3+12e^2F^2)F'
       +\tau^2(40FF'F''-35F'^3-8F^2F''')
                                                               \tag{M.1}
$$
用于两个真实 phase 核。$p_2$ 只是第67束第二列除以
$\Delta^2$，不改变 annihilator。令
$$
 W_p=p_1p_2'-p_1'p_2,\quad
 b_1=-W_p'/W_p,\quad
 b_0=(p_1'p_2''-p_1''p_2')/W_p,\quad
 \mathcal A_\phi=\partial_x^2+b_1\partial_x+b_0 .
$$
这完整保留 $e>0$，且准确消去两列。

对实际频带取
$$
 2^{-40}\delta^{-1/8}\le U/2,\qquad U^2\le B/4,\qquad
 \mathcal X\le2^{-1048576}.                         \tag{M.2}
$$
令 $c$ 是原区间的中点，取共同尺度和同一方向
$$
 \rho=2^{-1024}J^{-8},\qquad
 f_\rho(x)=\rho^7(1-((x-c)/\rho)^2)_+^{14},
$$
$$
 \boxed{\quad
 \psi=2^{-720}F^{9/2}\mathcal A_\phi^*
                           [-f_\rho'/\Delta-f_\rho].
 \quad}                                                       \tag{M.3}
$$
$\psi$ 不依赖 $M$。它同时准确消去两个实际径向 phase。
第67束的完整系数 jets 和 bump jets，逐项保留 $\rho$ 幂，给
$$
 \|\partial_x^\ell\psi\|_\infty\le\rho^{4-\ell},\quad
 \|\partial_x^\ell\psi\|_{L^1(dx)}\le2\rho^{5-\ell},
 \qquad0\le\ell\le4 .                              \tag{M.4}
$$
两个加项、$1/\Delta$、Leibniz 系数均在 $2^{-720}$ 中。
原 $2^{520}$ phase 系数、$2^{64}$ bump 导数、$2^{42}$ 高度
权和最多 $2^{20}$ 的有限和，总 bits 小于720。
方向为真 $C^9$ 紧支函数，根和外接口的全部所需 jets 不变。

$\rho<\ell/8$ 且
$\rho(1+\Delta+\Delta\sqrt\kappa)<2^{-12}$，
故它完全落在原真实两行短片中。这里没有为了共同频带而扩大
原未使用区间。

## 2. 完整局部矩阵，先保留两个状态

置
$$
 u=\sqrt{\mu_0}h,\quad\mu_0=w/r,\qquad
 Y=(u,u_x/\Delta).
$$
真实径向方程准确写为
$$
 Y_x=\Delta A Y,\qquad
 A=\begin{pmatrix}0&1\\
 (F+e)^2/4-\kappa F-\tau F'/2&0\end{pmatrix}.
                                                               \tag{M.5}
$$
原 canonical profile kernel 是
$$
 \mathcal K_{\rm rad}=B^2Y^T K_0Y,\qquad
 K_0=\begin{pmatrix}
 (F+e)^2/4-\kappa F&(F+e-2\kappa)/2\\
 (F+e-2\kappa)/2&1
 \end{pmatrix}.                                                \tag{M.6}
$$
对矩阵定义
$\mathcal D C=\tau C_x+A^TC+CA$，并令
$r=(9/2)F'/F$、$D_s=\mathcal D^sK_0$。直接三次乘法微分给
$$
 \frac{(\tau\partial_x-1)\mathcal A_\phi
                  (F^{9/2}\mathcal K_{\rm rad})}
                        {F^{9/2}B^2\Delta^2}
                  =Y^T C_eY,                                  \tag{M.7}
$$
$$
 \begin{split}
 C_e={}&D_3+[\tau(3r+b_1)-1]D_2\\
 &+\{\tau^2[3(r'+r^2)+2b_1r+b_1'+b_0]
                          -\tau(2r+b_1)\}D_1\\
 &+\{\tau^3[r''+3rr'+r^3+b_1(r'+r^2)
                      +(b_1'+b_0)r+b_0']
                  -\tau^2(r'+r^2+b_1r+b_0)\}K_0 .
 \end{split}                                                  \tag{M.8}
$$
这保留完整 height、通量和交叉项；没有选某一条 WKB 分支。

当 $\tau=e=0$，(M.8) 特别给
$$
 (C_0)_{22}=F(F-4\kappa)(F-2\kappa-1),\qquad
 \det C_0=F^2\kappa^2(F-4\kappa)^2
                              (F^2-4F\kappa-1).                \tag{M.9}
$$
对 $F>7/4,\kappa\le1/4$，最后的括号大于 $5/16$。
但以下不是仅用这个主项：整个 $\tau\in[0,1/80]$ 已准确支付。

## 3. 全 $\tau$ 的有理多项式正性

本节仅令 $e=0$。用
$$
 z=x(1-x),\quad v=1-2x,\quad v^2=1-4z,\quad
 q=30z^2,\quad
 c_0=450z^6+\tau^2(5-8z)
$$
作准确代数约化。原区间给
$$
 63/256\le z\le255/1024,\qquad1/16\le v\le1/8.
$$
沿实际曲线 $\partial_x=v\partial_z-2\partial_v$。
此导数保持约束 $v^2=1-4z$，所以在每次乘法后约化不改变
任何实际导数。

真实 phase Wronskian 是
$4199040000000\,z^9v^3c_0$。
将 $\mathcal A_\phi$ 的高度权展开，准确得到
$$
 A_1=9v/z+6/v-v(c_0)_z/c_0,\quad
 A_0=12/z^2-30/z+12/(1-4z)
                   -2(c_0)_z(1/z-3)/c_0 .                     \tag{M.10}
$$
这里 $\mathcal A_\phi(F^{9/2}K)/F^{9/2}
=K''+A_1K'+A_0K$。
因此 (M.8) 只有一个共同正分母
$$
 D=z^3(1-4z)^2c_0^2 .
$$
令 $C^{\rm num}=DC_0$，约化后的
$P^{\rm num}=\det C^{\rm num}/\kappa^2$ 是多项式。
程序以准确有理运算重建 (M.10) 和完整两个状态的
$D_1,D_2,D_3$；没有从有限数值点插值。

在更大的矩形
$$
 [63/256,255/1024]\times[1/16,1/8]\times[0,1/80]
                                             \times[0,1/4]
                                                               \tag{M.11}
$$
上，完整 Bernstein 系数给
$$
 C^{\rm num}_{22}>2^{-30},\qquad
 P^{\rm num}>2^{-57}.                              \tag{M.12}
$$
第一项多重次数 $(23,1,7,2)$，1152个系数全部正；
第二项次数 $(46,1,14,3)$，5640个系数全部正。
实际最小值的有理数保存在原生记录中，约为
$1.5653\,10^{-9}$ 和 $1.1331\,10^{-17}$。
这不是采样正性；(M.11) 还允许 $z,v$ 独立，因而严格覆盖
实际曲线。

直接用 $z<1/4$、$1-4z\le1/64$，
$$
 0<D<
 \frac1{64^3}
       \left(\frac{450}{4096}+\frac5{6400}\right)^2<2^{-24}.
$$
于是完整 $e=0$ 结论为
$$
                (C_0)_{22}>2^{-6},\qquad
                    \det C_0/\kappa^2>2^{-9}.       \tag{M.13}
$$
包括 $\kappa=0$ 时多项式商的连续值。

## 4. 有限 $e>0$：先保留准确的两个零因子

这里绝不对裸行列式作一个与 $\kappa$ 无关的绝对扰动。
原物理方程是
$(\mu_0h_t)_t+M^2\mu_0Qh=0$，$\mu_{0,t}/\mu_0=-1-Q$。
当形式参数 $M^2=0$ 时，$h=1$ 是准确解，
$\mathcal K(h,\widetilde h)=\mu_0h_t\widetilde h_t=0$。
当 $M^2=1$ 时，$h=e^t$ 是准确解，
$\mathcal K(h,\widetilde h)=\mu_0(h_t-h)
(\widetilde h_t-\widetilde h)=0$。
因此 (M.7) 的整个双线性矩阵在 $\kappa=0,e$ 分别有一个
真 null 向量。不是仅二次型在某向量取零。

(M.8) 的矩阵元是次数至多3的 $\kappa$ 多项式，系数在下面
复 $e$ 域全纯。对 $e\ne0$ 两个准确零因子相异，故
$$
                \det C_e=\kappa(\kappa-e)P_e(\kappa)             \tag{M.14}
$$
是准确多项式除法；其商系数在 $e=0$ 也全纯。
例如从最高系数向下递推，仅出现有限次乘 $e$，没有除以 $e$。

以下给出可核验的复系数费用。在 $|e|\le1/128$，真实
$x$ 区间上有
$|F|<2$、$|F|>5/3$，且
$(|F'|,|F''|,|F'''|,|F^{(4)}|)\le(2,30,45,720)$。
正系数 Taylor 乘法给 $p_1,p_2$ 的0--3阶 jets 分别小于
$$
 (2^4,2^9,2^{12},2^{16}),\qquad
 (2^9,2^{13},2^{17},2^{22}).
$$
$|W_p|<2^{19}$ 在此复域成立。实际 $e=0$ 有
$W_p>12(7/4)^6(3/4)^3>2^7$。Banach Cauchy 公式于是给
在 $|e|\le2^{-24}$，
$|W_p-W_p|_{e=0}|<8$，特别 $|W_p|>64$。
没有把一个实正分母直接用于复参数。

由这些 jet 和商法则，
$$
 |b_1|<2^{16},\ |b_0|<2^{21},\
 |b_1'|<2^{33},\ |b_0'|<2^{38},\qquad
 |r|<6,\ |r'|<2^7,\ |r''|<2^9 .
$$
在 $|\kappa|\le1$，完整 $\mathcal D$ 的正系数递推给
$\|D_s\|<2^4,2^5,2^7,2^9$，$s=0,1,2,3$。
将 $\tau\le1/80$ 留在 (M.8)，三个附加标量系数分别小于
$2^{10},2^{21},2^{21}$，因此安全地
$$
                         \|C_e\|<2^{30}.            \tag{M.15}
$$
这里直接付两个状态的全矩阵 norm，未用只在实相位成立的酉性。

每个 $\kappa$ 系数小于 $2^{30}$；行列式系数小于 $2^{63}$。
对 (M.14) 作不除 $e$ 的有限递推，商系数小于 $2^{64}$。
故 $|\kappa|\le1/4$ 时 $|P_e|<2^{65}$。
复 $e$ 圆盘上的 Cauchy 比较给实际 $0<e<2^{-190}$
$$
 |P_e-P_0|<2^{90}e<2^{-100},\qquad
 |(C_e)_{22}-(C_0)_{22}|<2^{55}e<2^{-135}.          \tag{M.16}
$$
结合 (M.13)，$P_e>2^{-10}$、$(C_e)_{22}>2^{-7}$。
对真实非零四重模，$\kappa=M^2e\ge16e$。
由 (M.14)--(M.16) 和完整最大本征值界，得到
$$
 \boxed{\qquad C_e>2^{-48}\kappa^2I,\qquad
                  16e\le\kappa\le1/4 .\qquad}       \tag{M.17}
$$
同一结论对 $\kappa\downarrow0$ 的实际尺度统一，不存在隐藏的
$e/\kappa^2$ 费用。

## 5. 真实 $dt$、共同径向频带和 mean

在 (M.3) 上两次伴随积分给
$$
 \int\psi\mathcal K_{\rm rad}dt
 =a\,2^{-720}\int f_\rho
          [(\Delta^{-1}\partial_x-1)
                 \mathcal A_\phi(F^{9/2}\mathcal K_{\rm rad})]dx .
                                                               \tag{M.18}
$$
真实 $dt=a\,dx$ 和全部 density/height 因子都在此式中。
短片内 (M.5) 的双向 flow norm 小于2。对原中心 wave
$Z_M=(\sqrt k\,u,u_t/\sqrt k)$，
$k=\sqrt{7M^2-16}$，
$$
 |Y(c)|^2
   =|Z_1|^2/k+(k/B^2)|Z_2|^2
                      \ge(M/B^2)|Z_M|^2 .
$$
使用 $\int f_\rho dx>\rho^8/8$，(M.17)--(M.18) 给
$$
 \int\psi\mathcal K_{\rm rad}dt
       >d(M)\|Z_M\|^2,\qquad
 d(M)=2^{-800}\rho^8\Delta^3M^5B^{-3}.              \tag{M.19}
$$
未放宽的 bits 为773。

mean 不能通过令 $M=0$ 代入一个带 $k^{-1}$ 的 wave frame。
单独在 $(h,h_t/B)$ 中处理：$\kappa=0$ 的真 null 向量是
常高度，故 (M.7) 的均值矩阵准确为
$\operatorname{diag}(0,(C_e)_{22})$。
物理 flux mean $\pi_0$ 沿径向参考恒定；置
$v_0=\pi_0/\sqrt{\mu_0(c)}$。短片内 $\mu_0(c)/\mu_0(t)>1/2$。
由同一个正 bump 积分，
$$
                  L_{\psi,0}>d_0|v_0|^2,\qquad
             d_0=2^{-800}\rho^8\Delta^3/B.           \tag{M.20}
$$
物理常高度的全部交叉项准确为0，不把它当成正定槽。

令 $\mathcal V_U$ 为中心所有 $U/2\le|m|\le U$ 的两迹，加上
独立 height/flux mean。按当前实际中心物理变量取
$h_0(c)=0$ 的代表元，记
$$
 \mathcal E_c=\sum_{U/2\le|m|\le U}\|Z_m(c)\|^2+|v_0|^2,
$$
$$
 d_{\rm band}=2^{-805}\rho^8\Delta^3U^5B^{-3},\qquad
                  d_c=\min(d_{\rm band},d_0).
                                                               \tag{M.21}
$$
其它高度 mean 值由准确 null 槽加回。
径向参考按 Parseval 直接给 $L_\psi^0>d_c\mathcal E_c$。
不是先分别估计每一模，再把未知的交叉项扔掉。

## 6. 同一个原有限盒，不改变允许 profile

第68束本 band 的全部 $\psi_M$ 可以取为 (M.3) 的同一个
$\psi$，但每个 $\theta_M$ 仍保留原独立坐标：
$$
 \Xi^{(n)}=(r_U/N_{\rm band})\sum_M\theta_M\psi,\qquad
 r_U=d_U/[2^{36}K^6(U+B)^2].
$$
全 $C^4$ 半径、原 graph/source 合同、原 $\zeta,h,b_M$、
fixed-stop 和全部外几何规范不变。这里只选择原允许族中的
另一组明确合法方向。

由 $J<U^{1/64}$ 和 $U\le\sqrt B/2$，(M.19)--(M.21) 与原
第68束 $d_U$ 直接比较给
$$
                       d_c>2^{13000}d_U .           \tag{M.22}
$$
例如 band 比值至少
$2^{13098}J^{-64}B^{27/2}\Delta^{106}$，mean 比值至少
$2^{13108}J^{-64}B^{13}\Delta^{106}$；两者都大于显示的值。
因此原半径无需放大，且原 radial PSD 消费者的假设继续满足。
这并不宣称旧某个已选参数点不经选择自动有新的实际混频结论。

非零 band 部分在同一当前 $\Gamma$ 的辅助径向路径上，用
第72束中心矩阵 Hessian，变化小于 $2^{-14}d_U$。
mean 另用准确积分
$L_{\psi,0}=\int\psi\,\mu_0(c)/\mu_0(t)\,dt$。
本 compact 盒使该比值的相对变化小于 $4r_U$，故其直接项
相对 $d_0$ 小于
$$
 2^{803}r_U\rho^{-3}\Delta^{-2}
       <2^{-32161}J^{-24}\delta^{96}<2^{-32000}.
$$
两个真实径向补偿 bump 一般非零，$|v^0|_1\le2r_U$。
它们的 mean 项用下一节完整物理能量和第72束的
$r_U/d_U$ 预算支付，而不假定它们对 mean 也消去。
因此同点、全盒径向参考仍满足
$$
                         L_\psi^0>\frac{d_c}{2}\mathcal E_c .
                                                               \tag{M.23}
$$
辅助路径准确终止于当前 $\Gamma^*(\mathbf a,\Omega)$，
不改变实际两相位目标。

## 7. 真非径向全频带误差；不丢交叉项

第69--72束的物理能量均是 Fourier 二次能量和
Wiener 乘子估计，因而可在本完整频带上一次应用。
具体把局部能量频率尺度取为 $U$：对全部输入
$U/2\le|m|\le U$，$\sqrt{7m^2-16}$ 与 $U$ 的比在
$[1,3]$；最多四阶输入角导的比较只增加一个固定 $2^{16}$。
完整实际 Fourier 输出不作投影，乘子用
$\ell^1*\ell^2\to\ell^2$，不存在 $N_{\rm band}$ 的重复相加。

mean 代表元 $h_0(c)=0$、$v_0$ 在中心 density frame 中为
$w_d=0$、$\zeta_d=q^{-1/2}v_0$，其任何已用角 Sobolev norm
小于2倍 $|v_0|$。所以同一个 full-space 能量也接纳它。
原两个 root 的 balanced mean、normal shear 和变图基本定理
照原顺序保留。安全的完整物理界为
$$
 E_{\rm low}<2^{7840}J^{16}\delta^{-32}\mathcal E_c,\qquad
 E_{\rm strong}<2^{8440}J^{20}\delta^{-34}\mathcal E_c .
                                                               \tag{M.24}
$$
40个新增 bits 包括上述 dyadic 比较、mean 输入和所有有限和。
原 strict $7/2$、root $H^4$ 仍在已付闭窗内，不要求更高输出
角导。

当前实际参数差仍准确分为第72束的两列：
$$
 e_i=D_\psi\Gamma_i^*-v_i^0,\quad
 |e_i|_1<
 2^{1130}\mathcal W_i\mathcal XP_j\rho^5
                       +2^{280}\mathcal W_i\mathcal Xr_U ,
$$
$$
 \|e\|_\infty<
 2^{161150}\mathcal XP_j\rho^5+2^{160300}\mathcal Xr_U .
                                                               \tag{M.25}
$$
所有联立行、当前真实共轭平均和首密度相位仍在这里。

关键新归一是
$$
 \frac{\rho^5}{d_c}
 \le2^{4100}J^{24}\delta^{-31/8}.                  \tag{M.26}
$$
band 分支用
$\rho^{-3}=2^{3072}J^{24}$、
$a^{-3}<2^{15}\delta^{-9/2}$、
$U^{-5}\le2^{200}\delta^{5/8}$，未放宽的 bits 是4092；
mean 分支只需
$2^{3877}J^{24}\delta^{-3/2}$，更小。
这使用真正完整 $d_c$，没有用旧径向谱隙去除一个绝对误差。

第69束 local actual-minus-radial 估计的全频带版本，及整个
固定 $\Gamma$ hat 响应，除以 $d_c\mathcal E_c$ 后分别小于
$$
 2^{4400}\mathcal N_{i|j}\mathcal XJ^{28}\delta^{-7},\qquad
 2^{13000}\mathcal N_{i|j}\mathcal XJ^{40}\delta^{-38}.
                                                               \tag{M.27}
$$
第一项使用全部交叉模式的同一 Cauchy--Schwarz，不取输出频率
对角。第二项使用真实 $\widehat z$，不加回局部 $\rho^4$ 裸场。

(M.25) 的 $\rho^5$ 参数 metric 行和其全部背景响应分别小于
$$
 2^{14000}\mathcal N_{i|j}\mathcal XJ^{48}\delta^{-46},\qquad
 2^{174000}\mathcal N_{i|j}\mathcal X^2J^{40}\delta^{-38}.
                                                               \tag{M.28}
$$
完整 bits 未放宽前是13678、173146。
非零径向补偿与 (M.25) 的 $r_U$ 列仍用实际
$r_U/d_c\le r_U/d_U$，连同 (M.24) 逐项给
$$
 2^{-27000},\quad2^{-28000},\quad2^{-27000},\quad2^{-1900000}
                                                               \tag{M.29}
$$
四个相对上界；它们分别支付实际/径向补偿 metric 差、
$v^0$ 背景、$e$ 的 $r_U$ metric 列、全参数 $r_U$ 背景。
最后一项的固定正指数132202由真实
$\mathcal X^2\le2^{-2097152}$ 支付，未删全参数和。

原接缝的全局因子仍是
$\mathcal N_{i|j}<2^{-20010}2^{-(31867/256)(j-8193)}$。
(M.27)--(M.28) 四项首层对数分别小于
$-1000000,-740000,-670000,-1600000$，
并且所有层比的衰减指数大于78。
原真实 incoming 已进入这个共同小球。

于是，在当前整个实际盒和实际联合参数上，
$$
 \boxed{\quad
 \int_{I_i}[\Psi_{\rm tot}\mathcal K_{\rm act}
                 -\mathcal H_{\widehat z_{\rm tot}}]dt
              >\frac{d_c}{4}\mathcal E_c ,
       \qquad Y_c\in\mathcal V_U/\{\text{constant height}\}.
 \quad}                                                       \tag{M.30}
$$
这是一个完整混频压缩型，包括 band--band 和 band--flux-mean
交叉项。常高度与任意场的交叉型准确为0，因为第61束
$\mathcal K,\mathcal H$ 中只出现 $h_\theta,\pi$。
沿原独立 $\theta_M$，整式准确再乘 $r_U/N_{\rm band}$。

## 8. 端口、全部源及全网络的准确余项

同一个实际 Jacobi 高度和 total conormal 从中心传播到两个
原物理截面；两根附近控制及其 jets 为0，实际背景响应仍非零。
所有输出模式、相反锥、height/flux mean 都通过完整物理
能量与两个 root 图，而不是先截成某个径向低维子空间。

ordinary/weak 源及其完整参数列保持
$$
 s=(-a_{\rm Jac}F^t,\ g-\partial_\theta(F^\theta+dF^t)),\qquad
 \widehat s=D_{\psi,\Gamma^*}s-\Psi_{\rm tot}\mathsf Bs .
$$
它们在原有序 Duhamel、Piola、height 和 normal-shear 合同中
保留；没有 $F_t^t$。物理均值仍为
$\pi_{0,t}=g_0$、
$h_{0,t}=\langle dh_\theta+a_{\rm Jac}\pi-a_{\rm Jac}F^t\rangle$。
bare flux 两端仍另需真实 $F^t$ 迹。
任意粗 weak 源没有因为本文齐次变图估计而获得新的迹正则性。

本篇解决了此前“每个模式自己的方向为正，但混频簇未必有共同
正方向”的低缩放局部门。范围是当前中心 $\mathcal V_U$。
实际 whole-network near-kernel 若还带有该 band 外的中心分量，
必须支付这些分量及其交叉项；physical principal 角图随参数的
识别、不同窗口的参数支持和全源同权重建也仍保留。
本篇不从 (M.30) 直接推出完整随机谱选择或非线性
$\mathcal F$ 的逆。

完整准确矩阵、Bernstein 系数和新增有理预算：
[源码](../scripts/fourfold_common_low_scaled_mixed_pocket_20261114.py)、
[实际记录](../notes/2026-11-14-R119-common-low-scaled-mixed-pocket-budget.json)。
