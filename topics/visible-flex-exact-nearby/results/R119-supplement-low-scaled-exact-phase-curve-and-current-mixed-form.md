# R119 续篇：低缩放精确相位曲线、两个真零因子与当前全混频型

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇将原共同低锥方向放入一条同支集精确
两相位曲线，在整个有限参数盒内保住全部
$16e\le\kappa\le1/4$ 的两个状态和 flux mean。
实际盒半径不再含旧远端补偿的 $\delta^{96}$ 损失。
随后逐项消费原 whole-profile-ball 响应与完整 joint 方程，
得到当前实际非径向全低锥的混频正型，而非只给径向单模结论。

全网近核是否落在这个低锥，或如何由紧/高缩放方向支付其
其它分量，仍须继续处理；本篇也保留任意带外输入的完整负项。

## 1. 原同一个有限 e 方向及同支集曲线

使用
[共同低缩放与混频型](R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md)
的真实 $C_e$、有限 $e$ 多项式及原方向。记
$$
 e=B^{-1}<2^{-190},\quad \tau=\Delta^{-1}<1/80,\quad
 F=f+7e,\quad f=30x^2(1-x)^2,\quad H=F+e,
$$
$$
 J=j+5,\quad j\ge8193,\quad80<\Delta<3J,\quad
 a=\Delta/B=\delta_j^{3/2}/(8\sqrt6),\quad
 \rho=2^{-1024}J^{-8}.
 \tag{L.1}
$$
在原未使用区间 $I$ 中，取中心 $c_\ell=c-\ell/4$，
使本篇支集与高缩放曲线及紧缩放三维图均不交。
所有系数仍在原 $[7/16,15/32]$ 范围。

用同一有限 $e$ 两 phase 算子 $\mathcal A_\phi$，令
$$
 f_\rho=\rho^7(1-((x-c_\ell)/\rho)^2)_+^{14},\qquad
 \psi=2^{-720}F^{9/2}\mathcal A_\phi^*
                              [-f_\rho'/\Delta-f_\rho].
 \tag{L.2}
$$
其四阶 sup、$L^1$ jets 和原 phase 核满足
$$
 \|\psi^{(l)}\|_\infty\le\rho^{4-l},\quad
 \|\psi^{(l)}\|_{L^1}\le2\rho^{5-l},\quad0\le l\le4,
 \quad \|\psi\|_{C^4}\le1,\quad D\mathsf C(0)\psi=0 .
 \tag{L.3}
$$
方向不依赖角频率。两条新补偿为
$$
 \eta_\pm=2^{-80}\rho^4
               (1-((x-c_\ell\mp4\rho)/\rho)^2)_+^{14}.
$$
三个支集互不相交。第三相位曲线的同一 determinant 计算给
其 phase Jacobian 逆
$$
 \|M^{-1}\|_{\infty\to\infty}<H_\ell:=2^{128}\rho^{-6}.
 \tag{L.4}
$$
这一步实际支付新补偿的支集长度，不借用远端原两 bump。

置
$$
 r_\ell=2^{-1000}\Delta^2\rho^9,\qquad
 \Xi_\alpha=\alpha\psi+z_-(\alpha)\eta_-+z_+(\alpha)\eta_+,
 \quad |\alpha|\le r_\ell,\quad \mathsf C(\Xi_\alpha)=0 .
 \tag{L.5}
$$
原 $\|D^2\mathsf C\|<2^{-10}$ 与 (L.4) 的 contraction
给唯一全纯曲线；它也定义于 $|\alpha|<2r_\ell$。
真实范围内
$$
 |z|_\infty\le H_\ell\alpha^2,\quad
 |z'|_\infty\le H_\ell|\alpha|,\quad
 \|\Xi_\alpha\|_{C^4}\le2r_\ell,\quad
 H_\ell r_\ell<2^{-3900}.
 \tag{L.6}
$$
最后一式由 $\Delta<3J$ 和 (L.1) 直接得到。
令当前完整紧支方向
$$
 \Psi_\alpha=\dot\Xi_\alpha=\psi+z_-'\eta_-+z_+'\eta_+ .
$$
它的 jets 满足
$$
 \|\Psi_\alpha^{(l)}\|_\infty\le2\rho^{4-l},\qquad
 \|\Psi_\alpha^{(l)}\|_{L^1}\le4\rho^{5-l},
                              \quad 0\le l\le4 .
 \tag{L.7}
$$
在整条曲线上，原两个径向 $\bar\Gamma$ 坐标准确固定；
真实非径向 $\Gamma^*$ 两列尚未被删去。

## 2. 原点 integrated 两态型的 determinant 下界

自然状态及完整径向 kernel 为
$$
 Y=(u,u_{t_{\rm ph}}/B),\quad u=\sqrt{\mu_0}\,h,\qquad
 Y_x=\Delta\begin{pmatrix}0&1\\
 H^2/4-\kappa F-\tau F'/2&0\end{pmatrix}Y,
 \tag{L.8}
$$
$$
 \mathcal K_{\rm rad}=B^2Y^T K_\kappa Y,\qquad
 K_\kappa=\begin{pmatrix}
 H^2/4-\kappa F&(H-2\kappa)/2\\
 (H-2\kappa)/2&1
 \end{pmatrix}.
$$
令 $U_\kappa(c_\ell,c_\ell)=I$。记无量纲 integrated 矩阵
$$
 L_{\kappa,0}=\int\psi\,U_\kappa^T K_\kappa U_\kappa\,dx .
$$
原 (M.7)、(M.18) 的准确伴随恒等式给
$$
 L_{\kappa,0}=2^{-720}\Delta^2
       \int f_\rho F^{9/2}U_\kappa^T C_eU_\kappa\,dx .
 \tag{L.9}
$$
原 (M.14)--(M.16) 已完整证明
$$
 (C_e)_{22}>2^{-7},\quad
 \det C_e>2^{-10}\kappa(\kappa-e),\quad
 \|C_e\|<2^{30},
 \qquad16e\le\kappa\le1/4 .
 \tag{L.10}
$$
前一个 22 界也适用于 $\kappa=0$；
$C_e$ 的复 $\kappa$ 范数界在 $|\kappa|\le1$ 成立。
这些是已付的有限 $e$ 结论，并不只给 $e=0$ 主项。

$\det U_\kappa=1$。对正定 $2\times2$ 矩阵，
$$
 \sqrt{\det(A+B)}\ge\sqrt{\det A}+\sqrt{\det B}.
$$
证明是
$\operatorname{tr}(\operatorname{adj}A\,B)
 \ge2\sqrt{\det A\,\det B}$；
有限和后由连续性即可用于 (L.9) 的正权积分。
由 $\int f_\rho>\rho^8/8$、$F^{9/2}>1$，
$$
 \det L_{\kappa,0}>
       2^{-1456}\Delta^4\rho^{16}\kappa(\kappa-e).
 \tag{L.11}
$$
这里直接控制整个 integrated 矩阵，不把某一列当成全部态。

设
$$
                           b_\ell=2^{-720}\Delta^2\rho^8 .
 \tag{L.12}
$$
短片内 $\|U_\kappa-I\|<2^6\Delta\rho$，
故由 (L.10)
$(U_\kappa^T C_eU_\kappa)_{22}>2^{-8}$。
对 $\kappa=0$ 同样成立。于是
$$
 (L_{\kappa,0}/b_\ell)_{22}>2^{-11},\qquad
 \frac{\det(L_{\kappa,0}/b_\ell)}{\kappa(\kappa-e)}>2^{-16}.
 \tag{L.13}
$$
第一式用于 $0\le\kappa\le1/4$ 的已付 22 范围；
第二式只需真实 $16e\le\kappa\le1/4$。

复圆盘 $|\kappa|\le1/2$ 上，短片 full flow 及逆 norm 都小于2。
同一个 (L.9) 与 $\|C_e\|<2^{30}$ 给
$$
                  \|L_{\kappa,0}/b_\ell\|_F<2^{40}.
 \tag{L.14}
$$
这是全复矩阵界，不将实正性冒作复模分母。

## 3. 当前曲线的两个真零因子与商估计

令 $F_\alpha=F-\tau\Xi_\alpha'$，
$U_{\kappa,\alpha}$ 是当前自然系统从 $c_\ell$ 出发的基本阵，
并定义
$$
 L_{\kappa,\alpha}
 =\int\Psi_\alpha\,
       U_{\kappa,\alpha}^T K_\kappa(F_\alpha)
                               U_{\kappa,\alpha}\,dx .
 \tag{L.15}
$$
复 $\kappa$ 中使用转置，不使用共轭，因此
$L_{\kappa,\alpha}$ 的各矩阵元是全纯函数。
实 $\alpha,\kappa$ 时仍是实际实对称 crossing 矩阵。

对任意当前 profile 和任意 compact 方向，物理 kernel
在 $M^2=0$ 时为 $\mu_0h_t\widetilde h_t$，
$h=1$ 是准确 null 解；在 $M^2=1$ 时为
$\mu_0(h_t-h)(\widetilde h_t-\widetilde h)$，
$h=e^{t_{\rm ph}}$ 是准确 null 解。
这是与任意第二状态的双线性 null，不只是二次型在某向量为零。
故当前完整 integrated 矩阵准确满足
$$
 \det L_{0,\alpha}=\det L_{e,\alpha}=0 .
 \tag{L.16}
$$
这里 $e>0$，两个零相异。于是
$$
 Q_\alpha(\kappa)=
   \frac{\det(L_{\kappa,\alpha}/b_\ell)}
                        {\kappa(\kappa-e)}
 \tag{L.17}
$$
在整个 $|\kappa|<1/2$ 全纯，可去点已由 (L.16) 支付。
不通过除以 $e$ 的差商估计其大小。

先在整个复圆盘上支付实际矩阵差。
由 (L.6)--(L.7)，
$|\Xi_\alpha^{(l)}|\le2r_\ell\rho^{4-l}$。
与紧缩放图相同的短片 Duhamel 逐项给
$$
 \|\Delta(A_{\kappa,\alpha}-A_{\kappa,0})\|
                              <16r_\ell\rho^2,\quad
 \|U_{\kappa,\alpha}-U_{\kappa,0}\|
                              <2^{10}r_\ell\rho^3 .
$$
两个 flow 均小于2，$K_\kappa$ 有界，中央原方向的积分误差
小于 $2^{20}r_\ell\rho^8$。
两条当前补偿的 $L^1$ 和至多
$2^{-78}H_\ell r_\ell\rho^5$，
其矩阵积分小于 $2^{57}r_\ell\rho^{-1}$。
两项合并安全地
$$
 \|L_{\kappa,\alpha}-L_{\kappa,0}\|_F
                                      <2^{64}r_\ell\rho^{-1}.
$$
所以由 (L.5)、(L.12)，
$$
 \|L_{\kappa,\alpha}/b_\ell-L_{\kappa,0}/b_\ell\|_F
                        <2^{784}r_\ell\Delta^{-2}\rho^{-9}
                         =2^{-216}.
 \tag{L.18}
$$
这个实际半径与 $B$、$\kappa$ 无关。

$2\times2$ determinant 的双线性公式和 (L.14) 给
$\left|\det(L_{\kappa,\alpha}/b_\ell)
            -\det(L_{\kappa,0}/b_\ell)\right|<2^{-174}$。
在 $|\kappa|=1/2$ 上，
$|\kappa(\kappa-e)|>1/8$；
最大值原理作用于已去奇点的差 (L.17)，得到
$$
              |Q_\alpha(\kappa)-Q_0(\kappa)|<2^{-171}
                               \quad(|\kappa|\le1/2).
 \tag{L.19}
$$
这正是避免绝对误差除 $\kappa^2$ 的步骤。

对真实 $16e\le\kappa\le1/4$，
$$
 (L_{\kappa,\alpha}/b_\ell)_{22}>2^{-12},\quad
 Q_\alpha>2^{-17},\quad
 \|L_{\kappa,\alpha}/b_\ell\|_F<2^{41}.
$$
因 $\kappa-e\ge15\kappa/16$，由 determinant/最大本征值可得
$$
 \boxed{\quad
 L_{\kappa,\alpha}>2^{-60}b_\ell\kappa^2I_2
       =2^{-780}\Delta^2\rho^8\kappa^2I_2 .
 \quad}
 \tag{L.20}
$$
在 $\kappa=0$，当前常高度仍是准确 null，
而 22 槽仍大于 $2^{-12}b_\ell$。
这证明了全部实际低缩放及 mean 的当前有限盒正性。

## 4. 原 physical 单位和整个中心低锥

物理 crossing 比 (L.15) 多准确因子
$B^2dt_{\rm ph}=B\Delta\,dx$。
对 $4\le M\le\sqrt B/2$，
原 wave 状态 $Z=(\sqrt{k_M}u,u_t/\sqrt{k_M})$、
$k_M=\sqrt{7M^2-16}$ 满足
$$
 |Y|^2=|Z_1|^2/k_M+(k_M/B^2)|Z_2|^2
                                            \ge (M/B^2)|Z|^2 .
$$
因此 (L.20) 在整个当前曲线上给
$$
 \mathfrak L_{\alpha,M}^0
   >2^{-780}\rho^8\Delta^3 M^5B^{-3}|Z_M|^2 .
 \tag{L.21}
$$
mean 用 $h_0(c_\ell)=0$ 代表元，
$v_0=\pi_0/\sqrt{\mu_0(c_\ell)}$，即 $Y=(0,v_0/B)$。
其完整径向项为
$$
 \mathfrak L_{\alpha,0}^0
                      >2^{-732}\rho^8\Delta^3B^{-1}|v_0|^2 .
 \tag{L.22}
$$
原物理常高度及其与所有场的交叉项准确为零。

保持原 complete-low-cone 的 $\mathscr H^s$ 定义：
包括全非零四重 Fourier 模的两个 wave 分量和 flux mean。
令 $\Pi_j$ 保留 $v_0$ 和 $4\le|m|\le\sqrt B/2$，
$Z_<=\Pi_j Z$。设
$$
                        d_\ell=2^{-800}\rho^8\Delta^3B^{-3}.
 \tag{L.23}
$$
径向 Parseval 给当前整盒
$$
                \mathfrak L_\alpha^0(Z_<)>d_\ell\|Z_<\|^2 .
 \tag{L.24}
$$
在使用这一径向结论后，下一节另付真实所有非径向交叉项，
不将 Parseval 原样用于实际背景。

对实际非径向中心输入，$Z$ 按同一个原物理角定义
$$
 Z_m=\left(\sqrt{k_m}\,u_m,\
       \frac{v_m-(1+Q(c_\ell))u_m/2}{\sqrt{k_m}}\right),
 \quad u=\sqrt{\mu_0}h,\quad v=\pi/\sqrt{\mu_0}.
 \tag{L.25}
$$
这里第二槽不是实际非径向 $u_t/\sqrt{k_m}$，
而是原相同 total-conormal 两迹。该区别不能省略。

## 5. 全部当前非径向响应与两个 joint 参数列

本节继续使用真实可达球 $\mathcal X\le2^{-1048576}$、
原两个接缝及完整邻胞和 $\mathcal N_{i|j}$。
先说明哪些已证范围真正适用。

第72束 (F.18) 明确在整个当前 $C^4$ 允许球中给
gauged 场的 $\rho^5$ 估计；其 (F.19) 的实际射线差在使用
annihilator 之前成立。第74束 (E.9)--(E.10) 的全低锥能量
只需 $M\ge4$、$M^2\le B$、同一四阶 profile 球和实际两个根，
不需当前 profile 在控制支集仍是 quartic。
本篇 $\|\Xi_\alpha\|_{C^4}\le2r_\ell<2^{-79}$，
根 germ、原外端和两个原补偿支集不变，故这些具体假设满足。

对完整方向 (L.7)，这些线性形状响应的 sup、$L^1$ 输入
至多旧方向的2倍。三个支集用其真实积分之和计费；它们全在
$[c_\ell-5\rho,c_\ell+5\rho]$，局部实两行比较的路程至多变为
旧短片的5倍，而 $5\rho\Delta(1+\sqrt\kappa)\ll2^{-12}$
仍由 (L.1) 严格满足。该路程只需另留3 bits，下面16 bits
一并覆盖；没有把每一列单独取零。相位的准确等式给
$$
 f^0=D\mathsf C(\Xi_\alpha)[\Psi_\alpha]=0,\qquad
                         v^0=D_\alpha\bar\Gamma=0 .
 \tag{L.26}
$$
在同一个当前 $\Gamma^*$ 处，原完整 joint 方程仍为
$$
 A e=-(f-f^0)-(A-A^0)v^0=-f .
 \tag{L.27}
$$
所以原72束 (F.20)--(F.23) 中来自非零径向补偿的 $r_a$ 列
确实为0；不是把它们估计成一个未支付的小数。
compact 的全部两列仍存在。置
$P_j=2^{-42}\delta^{-231/128}$、
$\mathcal W_i=J_i^4\delta_i^{-6}\mathcal N_i$。
用原同一个全无限行逆并为 (L.7) 放宽4 bits，可取
$$
 |e_{1,i}|+|e_{2,i}|
   <2^{1134}\mathcal W_i\mathcal XP_j\rho^5,\qquad
 \|e\|_\infty<2^{161154}\mathcal XP_j\rho^5 .
 \tag{L.28}
$$
这包括所有层的反馈，不是固定其它层参数的一行局部公式。

现在消费第74束 (E.9)--(E.13) 的实际 Fourier 能量及
$\ell^1*\ell^2\to\ell^2$ 乘子界。输出不截断，两个 mean、
相反锥、root 图、normal shear 及实际全空间 $\widehat z$
都在原序列中。
归一比仍准确为
$$
 \rho^5/d_\ell<2^{3887}J^{24}\delta^{-9/2}.
 \tag{L.29}
$$
(L.7)、(L.28) 只增加固定线性因子；用16 bits 同时覆盖所有
新增两列和有限和后，四种完整误差相对于
$d_\ell\|Z_<\|^2$ 的上界为
$$
 \begin{array}{ll}
 2^{4416}\mathcal N_{i|j}\mathcal XJ^{28}\delta^{-8},
 &2^{13016}\mathcal N_{i|j}\mathcal XJ^{40}\delta^{-39},\\
 2^{14016}\mathcal N_{i|j}\mathcal XJ^{48}\delta^{-47},
 &2^{174016}\mathcal N_{i|j}\mathcal X^2J^{40}\delta^{-39}.
 \end{array}
 \tag{L.30}
$$
它们依次是 local 全混频差、fixed-parameter 完整 hat 响应、
joint 两列的 metric 项、全部 joint 背景项。
原第74束已证四项首层分别小于
$2^{-990000},2^{-730000},2^{-660000},2^{-1590000}$，
且以后逐层衰减超过77 bits。
增加16 bits 后，每项仍小于 $2^{-600000}$。
原所有 $r_a$ 补偿项由 (L.26) 准确消失。

由 (L.24)、(L.30)，同一当前全盒、同一真实
$\Gamma^*(\mathbf a,\Omega)$ 的整负窗物理型满足
$$
 \boxed{\quad
 \mathfrak G_\alpha(Z_<)
 =\int_{I_i}
 [\Psi_{\rm tot}\mathcal K_{\rm act}
                    -\mathcal H_{\widehat z_{\rm tot}}]\,dt
                 >\frac{d_\ell}{2}\|Z_<\|_{\mathscr H^0}^2 .
 \quad}
 \tag{L.31}
$$
这是真实混频 Hermitian 型，包含所有低模之间、两锥之间及
它们与 flux mean 的交叉项。物理常高度仍是准确 null。
沿原实际新坐标 $\theta=\alpha/r_\ell$，完整式准确乘 $r_\ell$：
$$
 \boxed{\qquad
      \mathfrak G_\theta(Z_<)>
              \frac{r_\ell d_\ell}{2}\|Z_<\|_{\mathscr H^0}^2 .
 \qquad}
 \tag{L.32}
$$
没有旧 $r_a/N_a$ 或 $\delta^{96}$ 参数半径因子。

## 6. 带外状态、端图和完整源

(L.31) 不允许删除真正带外输入。
第74束 (E.15)--(E.21) 的全中心物理能量在同一 $C^4$ 球中适用。
原 (E.18)--(E.19) 中的远端径向补偿列现在准确为0；
(L.7)、(L.28) 支付其它全部列。
将旧常数 $2^{8600}$ 放宽至 $2^{8620}$，得到
$$
 |\mathfrak G_\alpha(Z,W)|
 \le C_\ell\|Z\|_{\mathscr H^4}\|W\|_{\mathscr H^4},
 \qquad C_\ell=2^{8620}\rho^5J^{16}\delta^{-30}.
 \tag{L.33}
$$
对准确分解 $Z=Z_<+Z_>$ 用一次 Young 不等式，
旧 (E.22)--(E.24) 的同一幂计算给安全的
$$
 \mathfrak G_\alpha(Z)\ge
     \frac{d_\ell}{8}\|Z_<\|^2
               -D_\ell\|Z_>\|_{\mathscr H^4}^2,\qquad
 D_\ell=2^{18260}\rho^2J^{36}\delta^{-71}.
 \tag{L.34}
$$
其中 $D_\ell$ 覆盖 $C_\ell+8C_\ell^2B^4/d_\ell$；
新增40 bits 的平方费用已经包含在60 bits 放宽中。

例如一个已明确的充分条件是
$$
 \|Z_>\|_{\mathscr H^4}
       \le2^{-12640}J^{-42}\delta^{38}\|Z_<\| .
 \tag{L.35}
$$
它使 (L.34) 的负项小于 $d_\ell\|Z_<\|^2/16$。
这是一个待由全网证明的定位门，不能因为本篇扩大了真实
参数半径，就自动断言所有 near-kernel 都满足它。

真实端点的 height/total-flux Green 恒等式不变；
compact 和本地补偿都离开根 germ，local endpoint shear 为0，
但实际背景和 principal 端角图仍随完整 joint 响应变化。
其参数列须在端口复合时保留。
本篇的 (L.31) 是物理整窗型，不把它未经转换称为
任意给定 KAM/Airy 坐标中的 generator。

普通/weak 源仍完整为
$$
 \mathbf s=(-a_{\rm Jac}F^t,\
         g-\partial_\theta(F^\theta+dF^t)),\qquad
 \widehat{\mathbf s}
      =D_{\alpha,\Gamma^*}\mathbf s
                             -\Psi_{\rm tot}\mathsf B\mathbf s .
 \tag{L.36}
$$
第61束完整有源 Green 恒等式中的
$\Omega(\mathbf s,\widehat{\dot Y})
 +\Omega(Y,\widehat{\mathbf s})$ 均保留。
无 $F^t_t$；bare flux 的实际 $F^t$ 端迹仍由原输入空间提供。
mean 继续满足
$\pi_{0,t}=g_0$、
$h_{0,t}=\langle d h_\theta+a_{\rm Jac}\pi-a_{\rm Jac}F^t\rangle$，
不从 source 空间删除任何独立 mean。

## 7. 允许族的重新消费和继续范围

本曲线和紧/高缩放两个子图可以在原 $I$ 的三个不交子区间
共存。每个子图各自 $\mathsf C=0$，故原 phase 加法式仍准确，
径向 $\bar\Gamma$ 固定。总 $C^4$ 范数仍小于 $2^{-79}$。
第53束完整 profile 球、54束 whole phase map 和55束两行
joint contraction 的具体输入与第三相位曲线的重新消费相同；
没有新接缝原子、根 germ 或 endpoint 输入。

本篇真正改变的是低锥有限盒半径，并以两条准确零因子保护
整个当前有限盒的退化小 $\kappa$ 正性。随后 (L.27)--(L.30)
独立保留非径向所有反馈，得到 (L.32)，没有从径向单模型
跳到混频 PSD。

紧/高缩放的当前实际非径向控制、整个 near-kernel 的定位、
三个区间外反馈、原层权和 source-to-label 全逆仍需继续。
本篇没有用新的低锥半径代替这些门。

所有新增估计为解析证明；只复用已经执行的有限 $e$ 多项式
和旧全盒能量预算，不声称运行了任何新数值实验。
