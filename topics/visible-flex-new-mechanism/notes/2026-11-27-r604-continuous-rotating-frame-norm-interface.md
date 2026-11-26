# R604：从同一有限场的连续径向盒到实际几何范数

2026-11-27。新纯区间接口，**尚未给任何97q连续范数或非圆reach证书**。
本地只纸面代数、源码与AST/hash，没有执行科学。
圆参考已由[R611](../results/R611-actual-circular-reference-complete-reach-certificate.md)付清。
现在要补的是[R604](../results/R604-normal-chord-stability-and-finite-parametric-norm-interface.md)
的实际非圆输入；[R504](../results/R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders.md)
与[R514](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)
已证的原函数和完整jets直接复用。

## 1. 同一完整场与不可省的输入

使用原连续定义

$$
X=a\Pi T+ze_3,\qquad
T=c(v)e_\theta(\theta+u)+v c(v)e_3,
\qquad c(v)=(1+v^2)^{-1/2}.
$$

必须由原角对称给 $\langle T\rangle=0$，及其两次径向导数的同一闭合。
不能把任意不闭合场放入零均值原函数后，仍声称 $X_\theta=aT$。
在每个真实径向闭区间上，输入须包住同一个全角连续场的
$u,u_s,u_{ss},u_\theta$、$v,v_s,v_{ss},v_\theta$，
以及当前 $a,z$ 与R611参考 $a_0,z_0$ 的完整两阶径向jets。

这些区间可以来自实际材料quintic的准确系数、原B样条与完整背景解析式，
但不能直接用径向网格样本的最大值。若要认证的是有限Hermite所定义的场，
应保持该同一C²场；若进一步声称无限flat kernel或数值seed的准确ODE性质，
相应ODE/插值/零suffix误差另付。浮点准备系数不能静默改变准确共享端jets。

## 2. 避免近圆相减的准确frame差

用正交基 $(e_\theta(\theta),e_r(\theta),e_3)$ 写

$$
\Delta T:=T-e_\theta=Ae_\theta+Be_r+Ce_3,
\quad A=c\cos u-1,\quad B=-c\sin u,\quad C=vc.
$$

实际区间实现改用完全相同的稳定恒等式

$$
A=-2c\sin^2(u/2)-\frac{v^2c^2}{1+c}.
$$

它利用 $c-1=-v^2c^2/(1+c)$，没有将原归一化或相位线性化。
源码的四分量Jet同时微分这个同一恒等式，得到值、$s,ss,\theta$导数。
于是

$$
\Delta T_s=A_se_\theta+B_se_r+C_se_3,
\quad \Delta T_{ss}=A_{ss}e_\theta+B_{ss}e_r+C_{ss}e_3,
$$
$$
\Delta T_\theta=(A_\theta+B)e_\theta+(B_\theta-A)e_r+C_\theta e_3.
$$

这些式子完整保留了随角变化的基，特别是 $+B,-A$ 两项。
各向量范数可直接由三个标量区间的平方和包住，不必把旋转基各坐标分别绝对值相加。
记前三种差的全角上界为 $M_0,M_1,M_2$。
由R504的连续原函数范数，令 $P_j=(11/7)M_j$，则
$\|\Pi\partial_s^j\Delta T\|\le P_j$；$11/7>\pi/2$仅是有理保守常数，
没有重证旧原函数界或把它混作FFT舍入界。

## 3. 当前半径、高度也改变时的完整差

记 $d_a=a-a_0$、$d_z=z-z_0$，其导数同理。
设 $e=X-X_0$，则

$$
e=d_ae_r+d_ze_3+a\Pi\Delta T,
\quad e_s=d_{a,s}e_r+d_{z,s}e_3+a_s\Pi\Delta T+a\Pi\Delta T_s,
$$
$$
e_\theta=(d_a+aA)e_\theta+aBe_r+aCe_3.
$$

因此完整连续 $C^0$ 和两列 $C^1$ 上界可直接组合；源码以归一列的Frobenius范数
包住R604要求的导数算子范数。这是充分上界，没有把各列的最大值当成它们同点可独立选择的新曲面。

为避免协变二阶项中先粗估再相减，设

$$
b_0^2=a_{0,s}^2+z_{0,s}^2,\quad
k_b=\frac{a_{0,s}a_{0,ss}+z_{0,s}z_{0,ss}}{b_0^2},
\quad k_a=\frac{a_{0,s}}{a_0},\quad k_t=\frac{a_0a_{0,s}}{b_0^2}.
$$

R604(24)的三个分子准确为

$$
\begin{aligned}
b_0^2 H_{11}={}&(d_{a,ss}-k_bd_{a,s})e_r
 +(d_{z,ss}-k_bd_{z,s})e_3\\
&+(a_{ss}-k_ba_s)\Pi\Delta T
 +(2a_s-k_ba)\Pi\Delta T_s+a\Pi\Delta T_{ss},
\end{aligned}
$$

$$
\begin{aligned}
a_0b_0H_{12}={}&[d_{a,s}-k_ad_a+(a_s-k_aa)A+aA_s]e_\theta\\
&+[(a_s-k_aa)B+aB_s]e_r+[(a_s-k_aa)C+aC_s]e_3,
\end{aligned}
$$

$$
\begin{aligned}
a_0^2H_{22}={}&a(A_\theta+B)e_\theta
 +[-d_a+a(B_\theta-A)+k_td_{a,s}]e_r\\
&+[aC_\theta+k_td_{z,s}]e_3
 +k_ta_s\Pi\Delta T+k_ta\Pi\Delta T_s.
\end{aligned}
$$

这是R514完整空间jets代入R604的代数整理，未删除任何实际高度或半径差。
有限项先按同一旋转正交基平方和；原函数项用 $P_j$。
最终
$\beta\le\sqrt{|H_{11}|^2+2|H_{12}|^2+|H_{22}|^2}$。
若全闭面的 $\alpha<1$、$\beta$ 均已包住，才使用R604的
$\lambda\le1+\alpha$、$\nu\le\alpha$、
$K\le(1/\rho+\beta)/(1-\alpha)^2$。

## 4. 实现与必须完成的真实覆盖

源为 [r604_rotating_frame_continuous_norms_20261127.py](../scripts/r604_rotating_frame_continuous_norms_20261127.py)。
它绑定R611修复后的准确区间算术，没有科学main、seed或旧检查。
所有区间输入都由调用方提供；原函数误差、材料语义和全域覆盖均不能由此接口自动取得。

后继须从真实97q/实际已生成材料端jets取得准确区间，处理每个不同的原结点和gate端点，
再覆盖中央柱及完整帽盘。圆柱纵向重参数化须按真实材料坐标计入，
不能只拿 $s=0$ 圈替代整个柱；帽轴用Cartesian图，不能除半径0。
这些完整条件具备后才能将全域范数送入R604的近远法弦预算。
当前实现没有替任何有限点观察授予连续资格，也未改变正在运行的97q源或接受门。

## 5. 同场差的准确消去接口

`radial_block_bounds(...,difference=...)` 可消费由同场代数直接形成的六个差jets，而非分别减两个宽区间。实际新mean接口先消共享无限H与固定μν，再形成控制差；当比较圆面与当前q共享全部mean及帽高时，高度差准确零，半径差只保核心归一周长的真实差。所有frame/connection/协变公式不变；difference仍须包住同一当前/参考的准确差，不能来自另一个场。省略参数仍是原保守相减行为。
