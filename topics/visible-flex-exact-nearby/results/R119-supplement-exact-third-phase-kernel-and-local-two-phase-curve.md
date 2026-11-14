# R119 续篇：第三相位核的准确正性与无 B 损失的局部两相位控制曲线

2026-11-14，visible-exact / tail_connector。

**状态：已证明的解析构造。** 在原实际 quartic 未使用支集内，
本文构造一条完整有限参数曲线，精确保持原 principal 与第一
相位，且第三个标量相位系数沿整条曲线严格增加。构造保留
$e=1/B>0$、全部 $\Delta\ge80$，不使用 $B=\infty$ 极限。

它解决的是原有限盒中径向两 bump 补偿造成的半径损失：
本曲线的两条局部补偿也在同一个未使用区间内，故原两个
$\Gamma$ 坐标在径向对象上**准确不动**。新实际半径只有
固定常数与 $J$ 的幂，没有 $B$ 或 $\delta$ 的逆幂。

第三相位系数的正性不等于有限 $\kappa$ 的完整散射 generator
正定。把它用于真实有限频率、整个混频簇及全源逆仍须支付
相应余项；本篇不省略这些量词。

## 1. 同一实际 profile 与准确两条 phase

取第67束同一个未使用区间 $I$，中心 $c$、长度 $\ell$，
$$
 I\subset[7/16,15/32],\qquad
 \ell>2^{-31}J^{-2},\quad J=j+5,\quad j\ge8193 .
 \tag{T.1}
$$
原两个 bump、其它已用控制与 $I$ 的一个邻域不交。
原实际量是
$$
 Q=7+Bf,\quad f=30x^2(1-x)^2,\quad
 dt=(\Delta/B)\,dx,\quad
 e=B^{-1}<2^{-190},\quad \tau=\Delta^{-1}<1/80 .
 \tag{T.2}
$$
记 $F=f+7e$、$H=F+e$、$\kappa=M^2/B$。
控制 $\Xi$ 作用后准确变为
$$
 F_\Xi=F-\tau\Xi',\qquad Q_\Xi=B F_\Xi .
 \tag{T.3}
$$
所有 $x$ 导数均取同一个固定材料坐标。

使用
[R119 全部实际五函数](R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md)
的两个归一多项式
$$
\begin{split}
 p&=F^3F',\\
 q&=(12F^4-8eF^3+12e^2F^2)F'
       +\tau^2(40FF'F''-35F'^3-8F^2F''').
\end{split}
 \tag{T.4}
$$
这里 $q$ 是该篇的第二列除以 $\Delta^2$。
置
$$
 W=pq'-p'q,\qquad
 {\cal A}=\partial_x^2-\frac{W'}W\partial_x+
                         \frac{p'q''-p''q'}W .
 \tag{T.5}
$$
已有实际证明给
$$
 W>1,\quad 1<F<2,\quad 3/4<F'<2,\quad p<16,\qquad
 \max_{0\le l\le5}(|b_0^{(l)}|+|b_1^{(l)}|)<2^{520}.
 \tag{T.6}
$$
原两个归一 phase 的准确形状改变量是第54束
$\mathsf C=(\mathsf C_1,\mathsf C_2)$。
对 $\|\Xi\|_{C^4}<2^{-20}$，
$$
 \|D\mathsf C\|<1/16,\qquad
 \|D^2\mathsf C\|<2^{-10};
$$
在 $\Xi=0$，对任意 compact $\psi$，准确有
$$
 D\mathsf C_1[\psi]
   =\frac12\int F^{-9/2}p\psi\,dx,\qquad
 D\mathsf C_2[\psi]
   =\frac1{256}\int F^{-9/2}q\psi\,dx.
 \tag{T.7}
$$
第二个 $1/256$ 是原 $n=m/4$ 相位单位；不能把它错当成
物理 $M=|m|$ 展开中的第一系数。物理 $M$ 展开对应
$4\mathsf C_2/M$。

## 2. 第三标量系数的完整局部泛函

对 $F_\Xi>0$ 定义
$$
 V_\Xi=-\frac{(F_\Xi+e)^2}{4F_\Xi}
       +\frac{\tau F_\Xi'}{2F_\Xi}
       -\frac{\tau^2F_\Xi''}{4F_\Xi^2}
       +\frac{5\tau^2(F_\Xi')^2}{16F_\Xi^3},
 \tag{T.8}
$$
$$
 {\cal C}_3(\Xi)
   =\frac{\Delta}{4}\int_I
       \{V_\Xi^2\sqrt{F_\Xi}-V_0^2\sqrt F\}\,dx .
 \tag{T.9}
$$
只取在正实值相接的平方根分支。这是一个实际 $C^4$ 形状的
全纯泛函；不需要对未知解作复径向延拓。

准确 Liouville 变换
$$
 s=\Delta\int^x\sqrt F\,dx,\qquad v=F^{1/4}u
$$
把
$$
 u_{xx}+\Delta^2\{\kappa F-H^2/4+\tau F'/2\}u=0
$$
变为 $v_{ss}+(\kappa+V_0)v=0$。
因此紧支变化的物理往返相位形式展开为
$$
 -2\Delta\sqrt\kappa\int\sqrt F\,dx
 -\Delta\kappa^{-1/2}\int V_0\sqrt F\,dx
 +\frac{\Delta}{4}\kappa^{-3/2}
                         \int V_0^2\sqrt F\,dx+\cdots .
 \tag{T.10}
$$
第三项的变化准确为 $\kappa^{-3/2}{\cal C}_3(\Xi)$。
局部 total derivative 的端值在同一支集外相消，根 germ 和
其它固定端点项并未被任意设零。

(T.10) 目前只用于识别一个准确的系数泛函；它不声称有限
$\kappa$ 的余项已小于第三项。下面的正性由有限恒等式证明，
不依赖形式级数的收敛。

## 3. 正性来自原 residual Wronskian，而非高频猜号

令 $\mathscr D_\kappa=\mathscr D_0+\kappa\mathscr D_1$ 为
第64/67束中作用于 $g=F^{9/2}{\cal K}$ 的准确三阶算子。
其最高项系数 $A_3=F'F^3=p$，而 $\kappa$ 部分准确为
$$
 \mathscr D_1=L\left(\partial_x-\frac{p'}p\right),
                 \qquad L=4\Delta^2F^4F'.
 \tag{T.11}
$$
设 $r_1=\mathscr D_0p,\ r_2=\mathscr D_0q$。旧完整恒等式成为
$$
 \mathscr D_1p=0,\qquad
 \mathscr D_1q=-32r_1,\qquad
 {\cal W}=r_1r_2'-r_2r_1'>0 .
 \tag{T.12}
$$
旧第二列与 $q$ 相差 $\Delta^2$，故其两个 Wronskian
同时除以 $\Delta^2$。旧已付的准确三态行列式恰给
$$
 \frac{{\cal W}}{p^2W}>2^{-80}\Delta^4 .
 \tag{T.13}
$$

以下把第三泛函的梯度接到这条恒等式。设
$$
 q_0=-H^2/4+\tau F'/2,\qquad
 T_\kappa=\Delta^2(\kappa F+q_0).
$$
取唯一的形式对角振幅
$$
 R=\Delta^{-1}\kappa^{-1/2}
           (a_0+\kappa^{-1}a_1+\kappa^{-2}a_2+\cdots)
$$
满足
$$
 2RR''-(R')^2+4T_\kappa R^2=4.
 \tag{T.14}
$$
每阶系数由 $a_0=F^{-1/2}>0$ 作代数递推，故不需收敛性。
前三项准确为
$$
 a_0=F^{-1/2},\quad
 a_1=-\frac{V_0}{2\sqrt F},\quad
 a_2=\frac{3V_0^2+(V_0)_{ss}}{8\sqrt F},
 \qquad \partial_s=\tau F^{-1/2}\partial_x .
 \tag{T.15}
$$
直接微分 (T.14) 也给
$R'''+4T_\kappa R'+2T_\kappa'R=0$。

一个完整的变分恒等式说明为何这确为相位梯度：
$$
 \delta T_\kappa\,R
 =\frac12\left[-\delta R'+\frac{R'}R\delta R\right]'
                         -2\frac{\delta R}{R^2}.
 \tag{T.16}
$$
因此对 compact 变化，
$-\int\delta T_\kappa R\,dx
 =\delta(-2\int R^{-1}\,dx)$，逐形式系数准确成立。
把 (T.15) 代入右侧，$(V_0)_{ss}$ 的积分是一个端项，便得
(T.9)--(T.10)。

对 $\delta F=-\tau\psi'$，左侧两次分部积分给梯度
$$
 {\cal K}_{\rm ph}
 =\Delta\left[-(\kappa-H/2)R'
                       +F'R/2+\tau R''/2\right].
 \tag{T.17}
$$
这个量是完整三态核的 $\Delta^2$ 倍，故
$F^{9/2}{\cal K}_{\rm ph}$ 满足同一 $\mathscr D_\kappa$
方程。写
$$
 {\cal K}_{\rm ph}
  =\tfrac12\sqrt\kappa\,F^{-9/2}
                (g_0+\kappa^{-1}g_1+\kappa^{-2}g_2+\cdots).
$$
由 (T.15)、(T.17) 直接有
$$
 g_0=p,\qquad g_1=q/32,\qquad
                 \mathscr D_1g_2=-r_2/32,
 \tag{T.18}
$$
以及准确的泛函恒等式
$$
                 D{\cal C}_3(0)[\psi]
          =\frac12\int_I F^{-9/2}g_2\psi\,dx .
 \tag{T.19}
$$
例如 $a_1$ 中的奇 $\tau$ 项
$-\tau F'/(4F^{3/2})=\tau a_0'/2$ 在 $g_1$ 中准确抵消；
剩下的全部 $e,\tau^2$ 项正好是 (T.4)，没有删掉密度项。

对任何 $g$，二阶 annihilator 的准确分解是
$$
 {\cal A}g=\frac Wp
     \left[\frac{(g/p)'}{(q/p)'}\right]'.
 \tag{T.20}
$$
(T.11)--(T.12) 给 $r_1=-LW/(32p)$，因此 $r_1\ne0$。
将 (T.18) 代入 (T.20)，全部常数保留后得到
$$
\boxed{\quad
 {\cal A}g_2
   =\frac{p\,{\cal W}}{L^2W}
   =\frac{p}{16\Delta^4F^2}\,
                              \frac{{\cal W}}{p^2W}
   >2^{-85}.
 \quad}
 \tag{T.21}
$$
最后一步使用 $p/F^2=FF'>3/4$。
这一完整实际下界没有 $B$、$\kappa$ 或根条件数。
它来自原已付的 finite-$e$ residual Wronskian。

## 4. 原 C4 单位中的明确 compact 正方向

取
$$
 \rho=2^{-40}J^{-2}<\ell/512,\qquad
 f_\rho=\rho^6(1-((x-c)/\rho)^2)_+^{14},
$$
$$
            \psi=2^{-700}F^{9/2}{\cal A}^*f_\rho .
 \tag{T.22}
$$
第67束同一个真实 jet 证明（其中取 $r=0$）给
$$
 \|\psi^{(l)}\|_\infty\le\rho^{4-l},\qquad
 \|\psi^{(l)}\|_{L^1}\le2\rho^{5-l},\quad 0\le l\le4,
 \qquad \|\psi\|_{C^4}\le1 .
 \tag{T.23}
$$
该方向至少 $C^9_c$，支集在 $[c-\rho,c+\rho]$。
准确分部积分给 $D\mathsf C(0)[\psi]=0$，而 (T.19)--(T.21)
给
$$
 D{\cal C}_3(0)[\psi]
  =2^{-701}\int f_\rho{\cal A}g_2\,dx
  >d:=2^{-789}\rho^7 .
 \tag{T.24}
$$
这里使用 $\int_{-1}^1(1-y^2)^{14}dy>1/8$。
所有导数都是原 $C_x^4$ 单位，未将一个缩放范数冒作原范数。

## 5. 两条同支集内的补偿列与真逆下界

在 $c-4\rho,c+4\rho$ 取
$$
 \eta_\pm(x)=2^{-80}\rho^4
        (1-((x-c\mp4\rho)/\rho)^2)_+^{14}.
 \tag{T.25}
$$
三个支集互不相交，全部在 $I$ 内。
原同一多项式的八阶 jet 界小于 $2^{64}$，故
$$
 \|\eta_\pm\|_{C^4}<2^{-12},\qquad
 \|\eta_+z_++\eta_-z_-\|_{C^4}
                              <2^{-10}|z|_\infty .
 \tag{T.26}
$$
记 $M=D_z\mathsf C(\eta_-z_-+\eta_+z_+)|_{z=0}$。
两个 phase 密度为
$$
 \ell_1=p/(2F^{9/2}),\qquad
 \ell_2=q/(256F^{9/2}).
$$
在 $I$ 上 $\ell_1>1/8$、$|\ell_1|,|\ell_2|<2$，且
$$
 \left(\frac{\ell_2}{\ell_1}\right)'
               =\frac W{128p^2}>2^{-15}.
 \tag{T.27}
$$
从左支集 $x$ 到右支集 $y$，$y-x\ge6\rho$。
故保持列顺序 $(\eta_-,\eta_+)$ 时，
$$
\begin{split}
 \det M
 &=\iint\eta_-(x)\eta_+(y)\ell_1(x)\ell_1(y)
       \left\{\frac{\ell_2(y)}{\ell_1(y)}
                    -\frac{\ell_2(x)}{\ell_1(x)}\right\}dxdy\\
 &>2^{-185}\rho^{11}.
\end{split}
 \tag{T.28}
$$
每个矩阵元的模小于 $2^{-78}\rho^5$，因为每个 bump
的积分至多 $2^{-79}\rho^5$。
完整两行逆因而满足
$$
                     \|M^{-1}\|_{\infty\to\infty}
                   <H_0:=2^{128}\rho^{-6}.
 \tag{T.29}
$$
这里已付两个补偿列的真实小支集；没有直接沿用原远端两 bump
的逆常数。

## 6. 有限非线性曲线：原两 Gamma 坐标径向不动

置
$$
                    r_0=2^{-1000}\rho^{13},
 \qquad |t|\le r_0 .
 \tag{T.30}
$$
用同一原 phase 泛函解
$$
 \Xi_t=t\psi+z_-(t)\eta_-+z_+(t)\eta_+,\qquad
                         \mathsf C(\Xi_t)=0.
 \tag{T.31}
$$
其完整构造是
$$
 z=-M^{-1}\{\mathsf C(t\psi+z_-\eta_-+z_+\eta_+)-Mz\}.
$$
在 $|z|_\infty\le H_0r_0^2$ 上，(T.7)、(T.26) 给
$\|\Xi_t\|_{C^4}\le2r_0$，右侧的模小于
$2^{-9}H_0r_0^2$，对 $z$ 的 Lipschitz 常数小于
$2^{-19}H_0r_0<1/2$。这给唯一的全纯曲线，且
$$
 |z(t)|_\infty\le H_0t^2,\qquad
 |z'(t)|_\infty\le H_0|t|,\qquad
 \|\Xi_t'-\psi\|_{C^4}\le2^{-10}H_0|t|.
 \tag{T.32}
$$
第二式由完整 $D_z\mathsf C$ 逆小于 $2H_0$，以及
$D\mathsf C(0)\psi=0$ 直接得到。对每个实际 $t$，
$$
                  D\mathsf C(\Xi_t)[\Xi_t']=0
 \tag{T.33}
$$
是准确等式，而非 $t=0$ 的一阶近似。

原第54束的支集分离恒等式为
$\mathsf F(\Gamma)+\mathsf C(\Xi)+\mathsf C_{\rm other}$。
由于 (T.31)，本曲线中原两个径向 $\Gamma$ 参数保持其
原值就精确保住两 phase；原局部逆的唯一性说明这也正是原
补偿图的值。因此
$$
                      D_t\bar\Gamma=0
                       \quad (|t|\le r_0)
 \tag{T.34}
$$
准确成立。本篇没有把真实非径向
$D_t\Gamma^*(a,\Omega)$ 设零；它仍是完整联立参数方程的响应。

## 7. 第三系数在整个真实盒中保持严格增加

(T.8)--(T.9) 给一个便于独立核验的统一界：
$$
 \|D{\cal C}_3\|+\|D^2{\cal C}_3\|<2^{40}
                 \quad(\|\Xi\|_{C^4}<2^{-20}).
 \tag{T.35}
$$
固定材料区间内原 quartic 直接给 $7/4<F<31/16$（使用 $e<2^{-190}$），所以整个所声明复 $C^4$ 球在扰动 $F_\Xi=F-\tau\Xi'$ 后仍有明确的上下模余量。
例如使用
$
 |F_\Xi|>1,\quad |F_\Xi|<2,\quad
 |F_\Xi'|<3,\quad |F_\Xi''|<31,\quad |F_\Xi+e|<3,
$$
逐项微分可取
$$
 |V_\Xi|<16,\quad
 |DV_\Xi[\psi]|<2^{10}\tau\|\psi\|_{C^4},\quad
 |D^2V_\Xi[\psi,\chi]|
          <2^{14}\tau^2\|\psi\|_{C^4}\|\chi\|_{C^4}.
$$
平方根的前两变分同样只带 $\tau,\tau^2$。
(T.9) 的 $\Delta$ 因子与第一次变分中的 $\tau$ 抵消；
二次变分另留有利的 $\tau$。乘 $|I|\le1/32$ 后远小于
(T.35)，故此界不含隐藏的 $B$ 或 $\Delta$ 增长。

由 (T.24)、(T.32)、(T.35)，
$$
 \left|\frac d{dt}{\cal C}_3(\Xi_t)
                       -D{\cal C}_3(0)[\psi]\right|
 <2^{42}H_0r_0
 =2^{-830}\rho^7<d/2 .
$$
所以整条实参数曲线满足
$$
\boxed{\qquad
 \frac d{dt}{\cal C}_3(\Xi_t)>d/2 .
 \qquad}
 \tag{T.36}
$$
用原有限坐标 $\theta=t/r_0\in[-1,1]$ 时，
$$
\boxed{\qquad
 \frac d{d\theta}{\cal C}_3(\Xi_{r_0\theta})
   >2^{-1790}\rho^{20}
   =2^{-2590}J^{-40}.
 \qquad}
 \tag{T.37}
$$
这已经包括真实有限半径，未把单位形状方向的导数当作
$\theta$ 的导数。

## 8. 原允许族、全部响应和后续消费边界

整曲线的 $C^4$ 大小小于 $2r_0<2^{-64}$，支集及全部端点
jets 仍在原未用 $I$ 内。因此它确实在第53--55束已给的
原允许 profile 全纯域中，不更改原 $h_j,\zeta_j,b_m$、
fixed-stop、根 germ 或最终物理端点。

这里要明确重付第55束的族入口，而不把“原 C4 域足够”当成
全部理由。第53束 (C.4) 覆盖的是完整 $C^4_0(J_x)$ 球，
并明确不要求两 phase 已满足；(C.6)--(C.28) 只消费形状的
四阶范数、端值、单峰性与支集。上述 $2r_0$ 比该实球
$2^{-21}$ 和复球 $2^{-20}$ 都小。第54束 (H.7)--(H.9)
也是整个 $C^4$ 球的 phase map；其中“线性 annihilator
上补偿从二阶起”的结论在这里无需借用，因为 (T.31) 已给
整个曲线的精确 $\mathsf C=0$。

第55束原先以线性 annihilator 子族陈述，但其
(N.2)--(N.4) 的完整状态与四阶 profile 输入由第53束原样满足；
(N.5)--(N.6) 的 radial 基点在这里更是准确不变。
因此 (N.7) 的全 KAM 平均行仍小于 $2^{-261844}$，
(N.10)--(N.12) 的非径向密度差使用同一固定参数盒和实际
$N_j^c\mathcal X$，而 (N.14) 的第二无限行收缩仍小于
$2^{-102043}$。形状没有产生新的 $Q_{ttt}$ 接缝原子，
根与正片的原对象也不变。这逐项重新授予其联合
$\Gamma^*(a,\Omega)$ 及两相位等式；没有把当前
$\Xi_t$ 错称为 $D\mathsf C(0)$ 的线性核中元素。
真实所有层和两个规范接缝继续使用原完整求和。

若同时安装多条曲线，
必须以原总 $C^4$ 和预算分配实际参数；(T.37) 只给本条
曲线的真实坐标，未把无限个单位盒直接同时打开。

同一当前点的总方向是
$\Psi=\Xi_t'$，其支集是三个真实 compact 支集的并，
且 (T.33) 消去当前的两个径向 phase 导数。
非径向 joint 参数列必须继续由准确方程
$$
 A\,D_t\Gamma^*=-f_{\rm joint}
$$
求出。这里径向参考列 $v^0=0$ 是由 (T.31)--(T.34)
得到的精确结论，非径向响应与两个 $D\Gamma^*$ 列没有消失。
(T.23)、(T.25)、(T.32) 还保留总方向的全部
$L^1$ 支集及四阶 jet 费用；不能把三支集当成一个零长度点。

普通和 weak 源、独立高度/flux mean、两个 principal 端图、
外端口及原 source-to-label 识别仍按原完整合同传播。
本篇改的是一个具体合法的辅助控制曲线，未自行换掉这些对象。

(T.37) 为高 $\kappa$ 正向控制提供一个已证明、无 $B$
半径损失的第三相位系数。下一步仍须把有限 $\kappa$ 的
两态振荡余项、整个非径向有序网络和同权源费用真实接上；
在这些门完成前，不能把 (T.37) 称为整个 near-kernel
cluster 的 PSD 或全网络逆。
