# R327：真实周期齐次核的逐包分类与十三端口门的有限联合系统

日期：2026-11-15。**完整纸面原式证明；没有执行积分、符号程序、人工检查、数值秩或研究计算。**

[R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md) 已在 R324 的同一实际圆上支付指定有理端口的完整 ruling，同时保留所选二阶规范对整个第四周期的真实代价。其剩余未知 k 必须同时属于十三条显示线性门的核，并解原全函数周期方程；十三是行数，不是控制秩。

[R221 §§6—10](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md) 已给一般活动包的周期核分类、有限矩像与相位降秩接口。本稿不将这些一般结论当作首次证明，也不预授周期特解存在。这里新增的实际专门化是：**一旦原两个周期函数有真实同 collar 特解，全部保持周期不变的规范对这十三门的像，准确由每个最细实际包的两列给出。** 因而原无限维联合问题等价于一个带相位光滑、种子条件的有限矩阵问题。包间平台、原二次尾、解析临界点跨接和秩降点均保留。

来源：[R221 一般核与联合矩接口](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R181 原退化周期算子](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)、[R184 同一规范的 joint 条件](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R259 原 E8 算子与尾表](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R281 实际解析母包](R281-analytic-packet-fibers-and-finite-canonical-end-germ-conditions.md)、[R324](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md)与 R326。

## 1. 本稿使用的实际 profile 类

把 R324 最后有限频率圆的全部**最细**不交实紧包列为
$$
f=\sum_{i=1}^n a_i u_i,\qquad
g=\sum_{i=1}^n b_i u_i,\qquad a_i\ne0.
\tag{1}
$$
各支撑包络 $J_i=(\ell_i,r_i)$ 严格不交，并有正间隙。全部真实八副本、十二副本、最后五块及其幅度都已展开到这些实际 $a_i,b_i,J_i$ 中；不以一个新同母近似替代它们。

每个 $u_i$ 是 R281/R324 实际得到的有限频率函数。经其原固定仿射坐标，它具有
$$
u_i(y)=\psi(y)P_i(y),\qquad
\psi(y)=\exp\{-1/(1-y^2)\},\quad |y|<1,
\tag{2}
$$
外面为零；$P_i$ 在闭区间邻域实解析且严格正。有限频率 cos 和有限纠正都已包括在 $P_i$ 中，并非未取极限的形式级数。

原等背景编码的两种 $a_i^2$ 都严格正，后续副本幅度非零，故(1)的 $a_i\ne0$ 对当前实际圆成立。不同基本包可以有不同最终形状；本稿不要求它们相同。

以下分类也适用于更一般的有限真紧包：只需每包内 $f'$ 的零点有限阶，且
$A_f=6f'f'''-2(f'')^2$ 没有开零集。本文先证明(2)满足这些实际条件；不把结论扩到存在开幂曲段、$A_f\equiv0$ 的弱 hook 构造。

## 2. 原周期算子和真正的齐次核

本节按 R221 的原核分类证明核对当前实际包的假设，保留证明中用于后续两类列的端点信息；一般分类本身沿用该来源。

保同一右锚，
$$
L_f(k)=\mathfrak H(k;f,f),\quad
p=f',\quad q=f'',\quad A_f=6pq'-2q^2,\quad V_f=6(qq')'.
$$
R181 的原式为
$$
L_f(k)''=(A_fk'')'-V_fk',
$$
$$
\boxed{pL_f(k)''=\{A_f(pk''-qk')\}'.}
\tag{3}
$$
当 $L_f(k)=0$ 且 k 同 collar 真紧时，右 collar 的原通量为零，因此
$$
A_f(pk''-qk')=0
\quad\text{在整个共同物理区间}.
\tag{4}
$$
此处没有对原方程除以 $p$ 或 $A_f$，也没有重新设置每个包的积分常数。

### 2.1 实际解析包的退化点可严格跨接

在一个包内部，p 和 $A_f$ 实解析。它们不恒为零。对 p 这由非零真紧包直接得到；对 $A_f$ 还可在一个平端令 t 为到边界的正距离，写
$$
u_i=t^\mu a(t)e^{-c/t},\qquad c>0,\quad a(0)\ne0.
$$
本例 $\mu=0$，保一般有限幂也不影响首项。由原导数，
$$
p\sim a_i c\,u_i t^{-2},\quad
q\sim a_i c^2u_i t^{-4},\quad
q'\sim a_i c^3u_i t^{-6},
$$
$$
A_f\sim4a_i^2c^4u_i^2t^{-8}>0.
\tag{5}
$$
右端的奇阶导号共同翻转，$pq'$ 的首号仍正。(5)仅说明端点邻域无零；整个包内仍允许真实临界点。

所以 p、$A_f$ 在靠近两端的内部邻域不为零，在余下紧内部区间的零点有限，且都为有限阶。由(4)，先在 $A_f\ne0$ 的稠密开集得到
$pk''-qk'=0$，再由连续性扩到全部包内。

在 p 非零的每个连通区间，
$$
(k'/p)'=0,\qquad k'=c\,p.
$$
若 $x_0$ 是 p 的 m 阶零点，两侧常数暂记 $c_-,c_+$。k 光滑，比较 $k'$ 的第 m 阶导数：
$$
c_-p^{(m)}(x_0)=c_+p^{(m)}(x_0),\qquad
p^{(m)}(x_0)\ne0.
$$
所以 $c_-=c_+$。跨过所有实际临界点后，每包只有一个常数。因此
$$
\boxed{k|_{J_i}=\gamma_i u_i+\beta_i.}
\tag{6}
$$
不能在每个 $f'=0$ 的子区间边界独立选常数；也没有因 $u_i$ 平端而允许内部常数跳跃。

### 2.2 完整核分解，保留平台与间隙

一次固定 $\chi_i\in C_c^\infty(I)$，在 $\overline J_i$ 的邻域恒等于1，在其他全部包的邻域为0，其变化只发生在间隙。定义
$$
\mathscr G=\{\eta\in C_c^\infty(I):\eta|_{J_i}=0
\text{ 对全部 }i\}.
$$
则
$$
\boxed{
\ker L_f=
\operatorname{span}_{\mathbb R}\{u_i,\chi_i:1\le i\le n\}
\ \oplus\ \mathscr G.
}
\tag{7}
$$

必要性由(6)直接给出，减去显示的有限和后余函数属于 $\mathscr G$。系数唯一：一个非零、非恒定的 $u_i$ 与常数在 $J_i$ 线性无关。

充分性必须回到原 hook，不仅检查求两次导后的式(3)。对 $u_i$，所有不同包的导数乘积为零，唯一自项是
$\mathfrak H(u_i;u_i,u_i)=0$。对 $\chi_i$ 或 $\eta\in\mathscr G$，它们的正阶导数在 f 的所有正阶导数支撑处为零，原 R181 单层右积分及 local 项逐项零。因此整个同锚 $L_f$ 为零，包括左仿射尾，(7)确为完整周期核。

(7)中的平台常数 $\beta_i$可以不同。它们由真实光滑间隙连接，不要求在各个包端把 k 的值重新清零。

## 3. 间隙自由度对十三端口门完全不可见

沿 R326 记
$$
\mathcal A_\theta(k)=
\bigl(\mathbf I(\phi_\theta,k),\
(P_{\ell,\theta}(k))_{-4\le\ell\le2},\
(H_{B,j,\theta}(k))_{0\le j\le2}\bigr)\in\mathbb R^{13}.
\tag{8}
$$
这里使用 R326 的**完整**局部 pairing、原 E8 history 及同一右锚，不更换门。

若 $\eta\in\mathscr G$，则
$$
\boxed{\mathcal A_\theta(\eta)=0
\quad\text{对全部 }\theta.}
\tag{9}
$$

首先，$\eta$ 与 $\phi_\theta$ 的全部非零 jets 不交，所以三个直接矩为零，且 $X(\phi_\theta,\eta)=0$ 对每个 E8 方向成立。原 $\mathcal T^\#$ 中两个 inner 槽的所有密度也在原包内；outer $\eta$ 及其 jets 在那里为零，故两个 T 项准确为零。

剩下的是 $I_j(XD_\theta,\eta)$。在每个间隙，$XD_\theta$ 是原右积分产生的一个确定二次多项式 p；它通常不为零。$\eta$ 可按有限个间隙分开，因它在包内恒零而光滑，所以每个间隙分量在两端全平。R326 的原式
$$
I_j(\eta,p)=0,\quad j=0,1,2
$$
遂逐间隙适用。这里用的是二次尾与真紧 outer 的精确正交，不是删去 history。

因此(7)的全部端口作用准确由 $2n$ 个有限列决定。改变 $\chi_i$ 的具体间隙插值只增加 $\mathscr G$，所以这些列不依赖该辅助选择。

## 4. 第一类列：每包母函数倍数

写
$$
c_i(\theta)=a_i\cos\theta+b_i\sin\theta,\qquad
d_i(\theta)=a_i^2-c_i(\theta)^2,
$$
$$
\mu_i=\mathbf I(u_i,u_i),\qquad
M_{X,i,j}=I_j\{u_i,X(u_i,u_i)\}.
\tag{10}
$$
单包的 $X(u_i,u_i)$ 可以带真实二次左尾，$M_{X,i,j}$ 必须按原全式计算。

原有理端芽沿用
$$
h=H(1+\varepsilon\sigma^2),\quad K=1+\kappa^2,\qquad
\mathsf o=\sigma\sum_{p=-3}^{1}h^pA_p+EB,
$$
其中 $A_p,B$ 就是 R326(27)—(28)，全部实际几何参数已冻结。

定义仅依赖原实际包的七个数
$$
\begin{aligned}
J_{i,\ell}=[h^\ell]\bigg[
2H\varepsilon\,\mathcal T_h^\#(u_i;u_i,u_i)
-\sum_{p=-3}^{1}\big\{
&\tfrac K4h^{p-1}M_{A_p,i,0}\\
&-\tfrac\kappa2h^pM_{A_p,i,1}
+\tfrac14h^{p+1}M_{A_p,i,2}
\big\}\bigg].
\end{aligned}
\tag{11}
$$
$\mathcal T_h^\#$ 是 R326(30)的完整原式。

则母函数列准确为
$$
\boxed{
\begin{aligned}
\mathbf I(\phi_\theta,u_i)&=c_i\mu_i,\\
P_{\ell,\theta}(u_i)&=(a_i^2-3c_i^2)J_{i,\ell},\\
H_{B,j,\theta}(u_i)&=(3c_i^2-a_i^2)M_{B,i,j}.
\end{aligned}}
\tag{12}
$$

证明中 local T 的同点支撑直接给
$\mathcal T(u_i;D)-2\mathcal T(\phi;\phi,u_i)
=(d_i-2c_i^2)\mathcal T(u_i;u_i,u_i)$。
能量项的不同包交叉只留下二次尾，与紧 outer $u_i$ 的三个矩均为零；所以同样逐包分开，且 $d_i-2c_i^2=a_i^2-3c_i^2$。这不是把一般第四 history 局部化，只用于当前二阶规范的三次线性响应。

等价地，完整奇响应为
$$
\widehat{\mathcal B}_\theta(u_i)
=2(a_i^2-3c_i^2)
\bigl[\mathcal T_\sigma(u_i;u_i,u_i)
-\mathcal E_h\{u_i,\mathsf o(u_i,u_i)\}\bigr].
\tag{13}
$$

## 5. 第二类列：平台常数的真实尾贡献

这类列不能当作零。直接矩虽为零，但 $XD_\theta$ 在间隙有多项式尾。

设
$$
\operatorname{tail}_X(\mu_i)=A_Xx^2+B_Xx+C_X .
$$
用正确的三个 adjoint
$$
L_0=\partial_x^4,\quad
L_1=x\partial_x^4+2\partial_x^3,\quad
L_2=x^2\partial_x^4+4x\partial_x^3,
$$
在包 $J_i$ 上准确积分，得到
$$
\boxed{
\mathbf I(XD_\theta,\chi_i)
=d_i\,\ell_X(\mu_i),\qquad
\ell_X(\mu)=(0,-2A_X,2B_X).
}
\tag{14}
$$
例如
$\int L_1v=[xv'''+v'']$，
$\int L_2v=[x^2v'''+2xv''-2v']$；
左右二次尾之差就是该包自己的原 tail。其他右方包的同一尾在两端相消，不需要其为零。

另一方面，由原 E8 对多项式常数1的准确作用，
$$
q_X(\mu)=2\mathbf I\{u,X(u,1)\}
$$
只依赖 $\mu$，得到下表：

| 原方向 X | $\ell_X(\mu)$ | $q_X(\mu)$ |
|---|---|---|
| $P=r_0$ | $(0,0,0)$ | $(0,0,0)$ |
| $R=r_1$ | $(0,0,2\mu_0)$ | $(0,0,0)$ |
| $S=s_0$ | $(0,0,0)$ | $(0,0,0)$ |
| $L=p_0$ | $(0,\mu_0/2,0)$ | $(0,-\mu_0/2,-\mu_1)$ |
| $U=s_1$ | $(0,0,2\mu_1)$ | $(0,0,0)$ |
| $P_1=p_1$ | $(0,\mu_1/2,0)$ | $(\mu_0/2,0,-\mu_2/2)$ |
| $T=t_1$ | $(0,0,2\mu_2)$ | $(0,0,0)$ |
| $V=p_2$ | $(0,\mu_2/2,0)$ | $(\mu_1,\mu_2/2,0)$ |

例如 $L(u,1)=u'/2$，
$P_1(u,1)=(xu'-u)/2$，
$V(u,1)=(x^2u'-2xu)/2$。这些输出真紧；原 primitive 已按同一个右锚计算，没有把多项式输入随意截断后遗失常数。

因此令
$$
h_{X,i,\theta}=-d_i\ell_X(\mu_i)+c_i^2q_X(\mu_i),
\tag{15}
$$
便有
$H_{X,j,\theta}(\chi_i)=(h_{X,i,\theta})_j$。

原 T 项也可直接读出。$\chi_i$ 在包内为1，所有正阶导数为零，R326(30)的 $F_{\chi_i}=2h^2$，所以
$$
\mathcal T_h^\#(\chi_i;D_\theta)
=\frac{d_i}{16}\left(\frac{K\mu_{i,0}}{h^2}-\mu_{i,2}\right),
\qquad
\mathcal T_h^\#(\phi_\theta;\phi_\theta,\chi_i)=0.
\tag{16}
$$
原 $I_2$ 的 $2(u_i')^2$ 正好包括在 $\mu_{i,2}$，不能另删。

平台列遂准确为
$$
\boxed{
\begin{aligned}
\mathbf I(\phi_\theta,\chi_i)&=0,\\
H_{B,j,\theta}(\chi_i)&=(h_{B,i,\theta})_j,\\
P_{\ell,\theta}(\chi_i)&=[h^\ell]\left[
\frac{H\varepsilon d_i}{8}
\left(\frac{K\mu_{i,0}}{h^2}-\mu_{i,2}\right)
+\sum_{p=-3}^{1}\left\{
\frac K4h^{p-1}(h_{A_p,i,\theta})_0
-\frac\kappa2h^p(h_{A_p,i,\theta})_1
+\frac14h^{p+1}(h_{A_p,i,\theta})_2
\right\}\right].
\end{aligned}}
\tag{17}
$$

(14)—(17)保住了平台本身和两侧不同原尾。它们只用该实际包的三矩及冻结几何常数，不依赖选定 cutoff 的形状。

## 6. 必须先支付的两个真实周期特解

R326 中已经保留的周期是
$$
V_\theta^c=\sin^2\theta\,V_d^c+
2\sin\theta\cos\theta\,V_e^c,
$$
整个第三算子为 $\tau\mathfrak H$，$\tau\ne0$。定义两个固定目标函数
$$
G_d=-V_d^c/(2\tau),\qquad G_e=-V_e^c/(2\tau).
\tag{18}
$$
周期部分存在一个光滑周期的同 collar 家族解，当且仅当两个原全函数问题各自有同 collar 解
$$
\boxed{L_f(k_d)=G_d,\qquad L_f(k_e)=G_e.}
\tag{19}
$$
充分性取
$$
k_\theta^0=\sin^2\theta\,k_d+
2\sin\theta\cos\theta\,k_e .
\tag{20}
$$
反过来，从任何家族解取
$k_d=k_{\pi/2}$、
$k_e=k_{\pi/4}-k_{\pi/2}/2$ 即得(19)。这里没有预限最终联合解的相位谐波；(20)只是周期方程的一个方便特解。

(19)仍是原退化算子的实际像条件，不是本稿已证明的存在性。具体按 R181，若目标在右 collar 为零，令 $v=k'$，它等价于
$$
(A_fv')'-V_fv=G'',\qquad
v\text{ 在双 collar 为零},\qquad
\int_Iv=0,\qquad k(x)=\int_r^xv .
\tag{21}
$$
右锚补回求两次导丢失的两个常数，整个固定 G 同时约束左尾。内部 $A_f=0$ 的通量、光滑跨接与平端逆解仍必须真实成立。若目标的右 collar 不是零，便已不能落入这里的紧规范像；不能把目标尾截掉后再解。

本稿只在(19)已确有解时进入以下有限系统。

## 7. 完整联合问题的有限矩阵 iff

定义真实 $13\times2n$ 矩阵
$$
C_\theta=
\bigl(
\mathcal A_\theta(u_1),\ldots,\mathcal A_\theta(u_n),\
\mathcal A_\theta(\chi_1),\ldots,\mathcal A_\theta(\chi_n)
\bigr).
\tag{22}
$$
全部列已在(12)、(17)明确给出。

**定理。** 对当前实际圆，存在同一个光滑、$2\pi$ 周期、同 collar 且在 $0,\pi$ 为零的二阶补偿 k，使其同时支付 R326 的完整第四周期、第三合法性和指定端口商，当且仅当：

1. 两个真实周期特解(19)存在；
2. 存在光滑周期的实系数家族
   $\beta_\theta\in\mathbb R^{2n}$，在 $0,\pi$ 为零，满足
$$
\boxed{
C_\theta\beta_\theta
=-\mathcal A_\theta(k_\theta^0)
\quad\text{对全部 }\theta.
}
\tag{23}
$$

**必要性。** 减去(20)，真实差在 $\ker L_f$ 内。由(7)唯一写成有限列组合加间隙函数。其系数可由每包内一个固定 $u_i'\ne0$ 的点读取比例，再由固定点读取平台值，故随原家族光滑、周期，并在种子为零。(9)使全部间隙项消失，于是得到(23)。

**充分性。** 准确取
$$
k_\theta=k_\theta^0+
\sum_{i=1}^n\bigl((\beta_\theta)_i u_i+
(\beta_\theta)_{n+i}\chi_i\bigr).
\tag{24}
$$
它有正确周期与种子，(7)保留完整周期方程，(23)使全部十三门零。再按 R326 原全局第三 Gram 右逆支付新的 $\mathcal W_e$ 平方与交叉项，即可保持指定端口的完整 ruling 为零，而第四周期也已为零。没有对 period 与端口另选两个不同 k。$\square$

这个 iff 没有支付其他几何段的 ruling；要得到整个闭路径第四 range，仍须把那些原条件作用于(24)的同一个 k。

更换(19)的特解不改变可解性：两个特解的差属于(7)，其端口像恰是 $C_\theta$ 的列组合，因此(23)的右边只改变一个已允许的列向量。

## 8. 真正的有限障碍，不以十三代替秩

固定相位时，(23)可解的必要充分条件准确为
$$
\boxed{
z^T\mathcal A_\theta(k_\theta^0)=0
\quad\text{对每个 }z\in\ker(C_\theta^T).
}
\tag{25}
$$
这些是原周期特解类上的真实有限线性兼容条件；由上一段，它们与所选特解无关。

本稿没有证明 $C_\theta$ 满行秩。母函数列的真实三次 self、平台列的原矩和相位因子都可能产生关系；即使包数很大，也不能按未知量个数宣布(25)自动成立。反之，若某相位的原值违反(25)，便准确排除仅靠同一二阶规范同时支付该周期与端口。

同样，逐相位满足(25)尚不足以保证光滑周期的 $\beta_\theta$。下一节给出这个区别的明确有限接口。

## 9. 秩降点、光滑系数及两个准确种子

(12)、(17)表明 $C_\theta$ 的条目是 $\sin\theta,\cos\theta$ 的次数至多二的多项式；直接合法性三行只有一次。由(20)，右边
$$
b_\theta=-\mathcal A_\theta(k_\theta^0)
$$
同样是次数至多四的真实相位多项式。这里的系数是固定实际包的积分和两个原特解的固定配对；没有相位采样近似。

设全圆最大秩为 r。若 r=0，条件就是 $b_\theta\equiv0$，可取 $\beta=0$。若 r>0，选一个不恒零的 r 阶 minor。它是实解析三角多项式，圆上的零点有限。在其余开放区间可以用原非零 minor 求解，并保自由列。

在每个可能秩降相位 $\theta_*$，令 $t=\theta-\theta_*$。对一变量实解析矩阵作精确局部消元，存在可逆解析矩阵 U、V，使
$$
U(t)C(t)V(t)=
\begin{pmatrix}
t^{\nu_1}&&&0\\
&\ddots&&\vdots\\
&&t^{\nu_r}&0\\
0&\cdots&0&0
\end{pmatrix},
\qquad \nu_j\ge0.
\tag{26}
$$
这里无需数值秩：取非零条目最小消失阶、除去其解析非零因子，其他条目都可被该 $t^\nu$ 解析整除，再用可逆行列操作消去其行列并递归。全局最大秩 r 保证余下块最终恒零。

记 $\widetilde b=Ub$。在该邻域存在光滑解，当且仅当：

- 零行对应的 $\widetilde b$ 恒零；
- 对每个非零对角元，$\widetilde b_j$ 在0至少消失到 $\nu_j$ 阶。

后一条件就是相应有限个真实导数为零；Hadamard 引理保证除以 $t^{\nu_j}$ 后仍光滑。本文的 b 解析，所以得到局部解析特解。若该点是指定种子 $0$ 或 $\pi$，还要求 $\beta(\theta_*)=0$；由于 V 可逆，这等价于非零对角元对应的 $\widetilde b_j$ 至少消失到 $\nu_j+1$ 阶，并把自由坐标在该点取零。

在常秩区间和这些有限邻域各取上述局部解，再用相位圆上的光滑分割统一，线性方程使组合仍解(23)。种子附近的局部解全取零值，组合也保种子。因此(26)给出了从点态兼容到整个光滑周期家族的准确补充，不把有限行数当作一个处处正则的假设。

没有把最终 $\beta_\theta$ 限制为有限 Fourier 多项式。原 R184 允许的是全体光滑相位家族；上面的 gluing 正在这个原允许类内。

## 10. 本稿完成的归约与仍然未付的门

现在，R326 的指定端口加完整周期联合问题准确分成：

- 两个原退化周期算子的真实同 collar 像问题(19)，保右锚、全部通量和左尾；
- 一个由实际微包给出的有限系统(23)，并保(26)的光滑与种子兼容。

无限多间隙函数没有被误当成无代价控制方向：它们在这十三门下确实全部不可见。每包平台则不同，其原尾贡献已显示在(14)—(17)，不能与间隙项一同删去。

本稿没有计算任何新矩阵、没有宣称满秩、没有宣称实际周期目标属于 $L_f$ 的像，也没有支付其余几何段的 ruling 或整个第四校正。它给出了一个完全保留原未知规范的必要充分有限接口，下一步必须评价真实像或真实兼容，而不是继续凭维数增加任意二阶参数。
