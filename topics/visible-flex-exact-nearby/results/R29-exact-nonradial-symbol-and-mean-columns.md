# R29：真实非径向主符号、曲线流、均值列与特征返回映射

2026-11-12，constructive-route。

**状态：已证明的中间结论。** 本文给出完整几何方程的精确改写及其
线性化接口，不假定 Fourier 截断。它说明哪些主项可以通过真实坐标变化
消去、自由径向均值实际提供哪些角向列，并给有理返回映射的准确共轭公式。
没有证明当前有限幅候选满足所列的闭轨条件，也没有给出它的全频右逆。

曲线流一节只需涉及的映射为 $C^2$。Gauss–Codazzi、主符号及返回映射
微分公式取足够光滑的核心（例如 $F\in C^4$），避免把曲率的经典导数
直接施加于任意 $C^2$ 面。最终闭面仍须另行支付固定帽及 $C^2$ 极限。

## 1. 常速材料圆的精确曲线流

设 $a(s)>0$。对每个 $s$，$\theta\mapsto F(s,\theta)$ 是正则闭曲线，
记其速度为 $\ell=|F_\theta|$、单位切向为 $T$、曲率为 $\kappa>0$，
主法向与双法向分别为 $N_c,B_c$。这里下标 $c$ 用于区别曲线法向和
下文的第二基本形式系数。

若
$$F^*e=ds^2+a(s)^2d\theta^2,$$
则
$$
\boxed{F_s=-\frac{a'}{a\kappa}N_c+
\epsilon\sqrt{1-\frac{a'^2}{a^2\kappa^2}}\,B_c,\qquad
\epsilon\in\{+1,-1\}.}                                      \tag{1.1}
$$
平方根严格正的每个连通区上符号固定；在其零集上两支重合，不能事先
禁止一个真实光滑解经过该退化集。

**证明。** $F_s\perp T$ 且 $|F_s|=1$。由 $|F_\theta|=a$，
$$
a'=\langle T,F_{s\theta}\rangle
=-\langle T_\theta,F_s\rangle
=-a\kappa\langle N_c,F_s\rangle.
$$
这决定 $F_s$ 的 $N_c$ 分量，单位长度条件决定剩下的 $B_c$ 分量。

反过来，若一个真实 $C^2$ 流满足 (1.1)，其中 $\kappa,N_c,B_c$ 都从
它自己的曲线读取，且在一条初始圆上 $\ell=a$，则它精确实现上述度量。
事实上，(1.1) 直接给 $F_s\perp F_\theta$ 和 $|F_s|=1$，并给
$$
\ell_s=-\ell\kappa\langle N_c,F_s\rangle=(a'/a)\ell.
$$
所以 $\partial_s(\ell/a)=0$，初始条件推出 $\ell=a$。证毕。

在旋转背景 $F=a e_r+z e_z$ 上，$N_c=-e_r$、$B_c=e_z$、
$\kappa=1/a$，式 (1.1) 正是 $F_s=a'e_r+z'e_z$、
$z'^2=1-a'^2$。因此腰部 $a'=0$ 在这个表示中没有高度投影奇点；
正半径平帽的 $|a'|=1$ 则是实际退化。式 (1.1) 是等价方程，
不是无需估计的存在定理；尤其不能只因右端含解析表达式，便把含
$\theta$ 二阶导数的演化称为一个普通 ODE。

## 2. 完整 Gauss–Codazzi 的一阶守恒形式

在精确度量 $g=ds^2+a(s)^2d\theta^2$ 下，取相容单位面法向 $n$，写
$$
\mathrm{II}=L\,ds^2+2M\,ds\,d\theta+N\,d\theta^2,
\qquad \mu=a'/a,\quad K=-a''/a.
$$
完整的 Gauss–Codazzi 方程为
$$
LN-M^2=Ka^2,
\qquad M_s=L_\theta-\mu M,
\qquad N_s=M_\theta+\mu N+aa'L.                       \tag{2.1}
$$
这些式子可由 $\Gamma^\theta_{s\theta}=\mu$、
$\Gamma^s_{\theta\theta}=-aa'$ 逐项代入协变 Codazzi 恒等式核对。
特别，第一条 Codazzi 给真正的守恒式
$$\partial_s(aM)=\partial_\theta(aL).                 \tag{2.2}$$

在 $N\ne0$ 的区间，可以准确消去 $L$，得到
$$
\begin{aligned}
M_s&=\partial_\theta\!\left(\frac{M^2+Ka^2}{N}\right)-\mu M,\\
N_s&=M_\theta+\mu N+aa'\frac{M^2+Ka^2}{N}.
\end{aligned}                                                    \tag{2.3}
$$
它仍是完整非线性方程。其关于 $(M,N)$ 的主矩阵为
$$
\begin{pmatrix}
2M/N&-(M^2+Ka^2)/N^2\\1&0
\end{pmatrix},                                                    \tag{2.4}
$$
特征根为 $(M\pm a\sqrt{-K})/N$。负曲率核心的两个真实特征速度是
$$c_\pm=\frac{-M\pm a\sqrt{-K}}{N}.                  \tag{2.5}$$
这里速度指向量场 $\partial_s+c_\pm\partial_\theta$ 的角速度；
矩阵特征根与该约定相差一个负号。

更明确地，在 $K<0$ 时令 $q=a\sqrt{-K}$、
$u=(M+q)/N$、$v=(M-q)/N$，直接代入 (2.3) 得
$$
\begin{aligned}
u_s-vu_\theta
 &=\frac{q'}{2q}(u-v)-\mu\left(\frac{3u+v}{2}+a^2u^2v\right),\\
v_s-uv_\theta
 &=-\frac{q'}{2q}(u-v)-\mu\left(\frac{u+3v}{2}+a^2uv^2\right).
\end{aligned}                                                    \tag{2.6}
$$
因此双曲区的最高导数有线性退化的交叉输运结构。$q'/q$ 在简单
转折点可能发散；(2.6) 不能越过该点当作有界系数系统使用，(2.3)
才是在 $N\ne0$ 时不包含这个人为除法的原始系统。

## 3. 法向主符号和交叉项的真实消元

对任意光滑浸入（本段先不要求诱导度量径向），法向变分的应变兼容
方程，其二阶法向主部在坐标 $(s,\theta)$ 中、除去非零密度因子后为
$$
\boxed{\mathcal D_2=N\partial_s^2-2M\partial_s\partial_\theta
                         +L\partial_\theta^2.}                  \tag{3.1}
$$
可在一个点取正常坐标独立核对：写变分
$V=v^iF_i+w n$，一阶应变为
$\nabla_i v_j+\nabla_jv_i-2wh_{ij}$。
作用 Saint-Venant 组合 $\partial_{22}E_{11}+\partial_{11}E_{22}
-2\partial_{12}E_{12}$，切向场的三阶导数相消，法向场的二阶部分
恰为 $-2(h_{22}w_{11}-2h_{12}w_{12}+h_{11}w_{22})$。
协变写法和密度变换给 (3.1)。这只是主符号结论：全部低阶项、
切向未知量、自由度量列及实际端口不能因此删掉。

设 $N$ 在一个有限圆柱上不为零，令 $A=M/N$，解圆周输运方程
$$
\phi_s=A\phi_\theta,\qquad \phi(s_0,\theta)=\theta,\qquad
\phi(s,\theta+2\pi)=\phi(s,\theta)+2\pi.               \tag{3.2}
$$
光滑周期速度 $-A$ 的流为圆微分同胚，故 (3.2) 的真实解存在且
$\phi_\theta>0$。令 $\eta=\phi(s,\theta)$。向量场
$X=\partial_s-A\partial_\theta$ 在新坐标下恰为 $\partial_s$，而
$\partial_\theta=\phi_\theta\partial_\eta$。由
$$
\frac{\mathcal D_2}{N}
=X^2+\left(\frac LN-A^2\right)\partial_\theta^2
\quad\text{模一阶算子}
$$
得到准确的变换后主部
$$
\boxed{\frac{\mathcal D_2}{N}
=\partial_s^2+
\frac{LN-M^2}{N^2}\phi_\theta^2\partial_\eta^2
\quad\text{模一阶算子}.}                              \tag{3.3}
$$
对于精确的径向诱导度量，可以用 Gauss 恒等式把系数写成
$$K(s)\,b(s,\eta),\qquad b=\frac{a^2\phi_\theta^2}{N^2}>0.        \tag{3.4}$$
所以这一坐标变化精确消去了交叉二阶项，而且保持径向的曲率转折位置。
若 $K(s_*)=0$、$K'(s_*)\ne0$ 且 $N\ne0$，(3.3) 的角向系数
在 $s_*$ 简单变号；没有用 $K^{-1}$ 或 $\sqrt{|K|}^{-1}$ 来伪装
转折处的正则性。

剩下的 $b$ 一般仍随角变化。事实上由 (2.1)、(3.2) 可进一步准确算得
$$
X\log\left|\frac{N}{a\phi_\theta}\right|=\mu a^2\frac LN,\qquad
X\log b=-2\mu a^2\frac LN.                            \tag{3.5}
$$
证明只需用 $X\log\phi_\theta=A_\theta$，以及
$X\log|N|=A_\theta+\mu+\mu a^2L/N$。式 (3.5) 没有推出 $b$ 为径向。

**近似图的必要区别。** 若当前候选仅有小的非均值度量残差，
它的实际诱导度量还不是 $ds^2+a^2d\theta^2$。此时仍可使用
(3.1)–(3.3)，但 $LN-M^2$ 必须从该候选自己的实际第二基本形式读取；
不能将它替换成角平均度量的 $K(s)a(s)^2$。
此外，(3.2) 是分析算子的坐标变换：原来的非零模投影、自由均值列
及两个外端边界图也必须随之变换，不能保留旧 RHS 和 Robin 线不动。

## 4. 实际非径向图上的自由均值列

本节不假定候选已精确等距，且 $r$ 可以是任何实际径向坐标。
在圆柱标架中写
$$
F_*=a_0e_r+z_0e_z+
\sum_{j\ge1}\left[
U_j\cos(n_j\theta)e_r+T_j\sin(n_j\theta)e_\theta
                   +W_j\cos(n_j\theta)e_z\right],
\quad n_j=4j.                                            \tag{4.1}
$$
有限和无需额外条件；无限和假设可按所用阶数逐项微分。
对保反射的均值变分 $V_0=A(r)e_r+C(r)e_z$，令
$\mathcal F(F)=P_{\ne0}(dF\cdot dF)$。则第 $n_j$ 模的准确导数列是
$$
\boxed{\begin{aligned}
(D\mathcal F_{F_*}V_0)_{\theta\theta}^{\cos n_j\theta}
 &=2A(U_j+n_jT_j),\\
(D\mathcal F_{F_*}V_0)_{r\theta}^{\sin n_j\theta}
 &=AT_j'-A'(n_jU_j+T_j)-n_jC'W_j,\\
(D\mathcal F_{F_*}V_0)_{rr}^{\cos n_j\theta}
 &=2(A'U_j'+C'W_j').
\end{aligned}}                                                   \tag{4.2}
$$
**证明。** 使用 $\partial_\theta e_r=e_\theta$、
$\partial_\theta e_\theta=-e_r$，有
$$
(F_*)_{\theta,j}=-(n_jU_j+T_j)\sin(n_j\theta)e_r
 +(U_j+n_jT_j)\cos(n_j\theta)e_\theta
 -n_jW_j\sin(n_j\theta)e_z.
$$
将它和 $(F_*)_{r,j}$ 分别与
$(V_0)_\theta=Ae_\theta$、$(V_0)_r=A'e_r+C'e_z$ 点乘即可。
径向背景 $a_0e_r+z_0e_z$ 的交叉应变完全为零模，已被投影删去。

因此均值列在真正非径向图上会产生非零角模，并非只能改变一个平均值。
但是对每个固定 $r$，所有模的三个张量分量都由同三个数
$A(r),A'(r),C'(r)$ 驱动，且 $A'$ 真是同一个 $A$ 的导数。
不能把它们当作每个角模各自独立的三个控制。
在径向背景上这些列全部为零；在只有第四模的一阶种子上，它们在
一阶只产生第四模。对于更高模，控制系数必须从同一实际候选的
$U_j,T_j,W_j$ 读取。

若另允许均值 $B(r)e_\theta$，新增的反射相反列为
$$
\begin{aligned}
\theta\theta\text{ 的正弦列}&=2B(n_jU_j+T_j),\\
r\theta\text{ 的余弦列}&=-BU_j'+B'(U_j+n_jT_j),\\
rr\text{ 的正弦列}&=2B'T_j'.
\end{aligned}                                                    \tag{4.3}
$$
这说明放开该均值也只有两个共同控制 $B,B'$，而非任意角向函数。

## 5. 双曲核心的返回映射及其真实微分

在两个固定切口 $s_-<s_+$ 之间，设实际特征速度 $c_\pm(s,\theta)$
对 $\theta$ 为 $C^1$、周期，对 $s$ 连续。简单转折附近的
$\sqrt{-K(s)}$ 亦满足此要求。令 $P_\pm$ 是两族特征从左到右的
圆流映射，则一次沿 $+$ 向右、沿 $-$ 向左的返回映射为
$$\mathcal R=P_-^{-1}\circ P_+.                           \tag{5.1}$$
它是一个真实圆微分同胚。径向情形 $c_\pm=\pm\omega(s)$ 才直接给
$$\mathcal R(\theta)=\theta+2I,\qquad I=\int_{s_-}^{s_+}\omega(s)\,ds.
                                                               \tag{5.2}$$

对任一速度 $c$，写流为 $\Theta(s;\theta)$，
$J=\partial_\theta\Theta>0$。固定端点下，其速度扰动 $\dot c$ 的准确
一阶变化为
$$
\boxed{\dot P(\theta)=J(s_+;\theta)
\int_{s_-}^{s_+}
\frac{\dot c(s,\Theta(s;\theta))}{J(s;\theta)}\,ds.}       \tag{5.3}
$$
这是将 $\dot\Theta_s=c_\theta\dot\Theta+\dot c$ 除以
$J_s=c_\theta J$ 后积分所得。对 (5.1) 作链式微分得到
$$
\boxed{\dot{\mathcal R}(\theta)=
\frac{\dot P_+(\theta)-\dot P_-(\mathcal R(\theta))}
     {P_-'(\mathcal R(\theta))}.}                         \tag{5.4}
$$
若扰动涉及移动转折点，应把端点项也计入；(5.3)–(5.4) 不省略这些
费用来处理移动端点。它们可直接用于支撑远离转折的均值控制，或已经
固定实际切口的计算。

在径向背景上，记 $I_s=\int_{s_-}^s\omega$，则特别有
$$
\dot{\mathcal R}(\theta)=
\int\dot c_+(s,\theta+I_s)\,ds-
\int\dot c_-(s,\theta+2I-I_s)\,ds.                    \tag{5.5}
$$
这给检验实际均值列能否控制返回映射所需的明确线性算子。
它一般有非恒定角模，不能只用一个径向作用量导数代替。

## 6. 有理返回角的无角宽损失部分

R25 的 $\mu=484/89$、$\sqrt A=495/89$ 给
$I=11\pi/89$。在四重材料角 $\chi=4\theta$ 中，径向返回角为
$$\alpha=\frac{88\pi}{89}=2\pi\frac{44}{89}.           \tag{6.1}$$
因此其阶数正好为 $q=89$。下面两条代数结论给实际非径向归一化的
正向接口；它们不声称当前返回映射已经满足所需输入。

令 $T f(\chi)=f(\chi+\alpha)$，
$\Pi_q f=q^{-1}\sum_{j=0}^{q-1}T^jf$。若 $\Pi_qf=0$，则
$$
u=\frac1q\sum_{j=0}^{q-1}jT^jf,\qquad (T-I)u=f,\qquad \Pi_qu=0.
                                                               \tag{6.2}
$$
在任何使实角平移为等距的范数（例如同一解析带上的上确界或 Fourier
指数加权 $\ell^1$ 范数）中，
$$\|u\|\le\frac{q-1}{2}\|f\|=44\|f\|.               \tag{6.3}$$
证明将 (6.2) 的和错位相减，直接得到
$(T-I)u=f-\Pi_qf$；范数界由系数绝对值之和给出。
所以非 $89\mathbb Z$ 的全部角模可同宽处理。
$\Pi_q$ 保留的非零 $89\mathbb Z$ 模是真正的共轭共振部分，
不能由一个只调常数返回角的参数自动删除。
这是返回映射坐标共轭的共振，不是宣称 R25 的 PDE 在物理第 $356$
模有核；R25 的谱核仍只有第四模，转折相位不能在这两个问题间省掉。

更强地，若某个实际、保向的圆微分同胚 $R$ 有升举满足
$$R^{\circ q}(\chi)=\chi+2\pi p,\qquad (p,q)=1,$$
则它具有一个完全显式的真实共轭：
$$
h(\chi)=\frac1q\sum_{j=0}^{q-1}
\left(R^{\circ j}(\chi)-j\frac{2\pi p}{q}\right),\qquad
h\circ R=h+\frac{2\pi p}{q}.                           \tag{6.4}
$$
因为 $h'=q^{-1}\sum_j(R^{\circ j})'>0$ 且
$h(\chi+2\pi)=h(\chi)+2\pi$，它是同正则性的圆微分同胚。
共轭等式由望远镜求和给出。这里真正需要的是完整有限阶闭轨恒等式，
只知道一个旋转数或径向作用量等于 $p/q$ 并不足以代替该输入。

## 7. 与有理强谱背景的组合范围

R28 的径向作用量保持和 Liouville 变化可以先处理真实径向部分；
本文件给出余下工作的明确对象：从同一实际图读取 $(L,M,N)$，
使用 (3.2)–(3.3) 处理交叉主项，并用 (4.2)、(5.3)–(5.4) 计算
自由均值对完整返回映射的作用。若确能支付 (6.4) 的输入，返回映射
本身的共轭完全不需要小除数定理；若只能支付小误差，必须继续处理
真实的共振部分、边界条件和转折连接，不能将小误差宣称为闭轨。

以上步骤仍未把整个混合型 PDE 变成一个已可逆的径向算子。
完整一阶余项、转折附近变换、受迫边界源、核规范和最终非线性收敛
都必须在同一实际对象上计入。本文据此提供可直接使用的公式，
不改变课题主目标尚未完成的状态。
