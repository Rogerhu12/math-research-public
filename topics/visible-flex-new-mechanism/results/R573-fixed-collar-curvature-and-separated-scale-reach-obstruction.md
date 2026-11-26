# R573：R570 分离尺度词的真实双 collar 曲率、直径与 reach 比例

日期：2026-11-26。原式几何证明。本文只判断已经登记的 R544–R570 依次固定母、$H,H_0,\Omega,R$ 后令 $\delta\to0$ 的分离尺度族；不排除任何未经本估计判断的有限参数，也不排除其他母、输入、紧凑返回或新的几何机制。

结论是：即使以后完整第四 period 和更高阶均支付，只要有限曲面仍保留该词的原双 collar，其闭面 reach 与实际直径之比在这个最后小 $\delta$ 极限中趋零。闭合净位移、整体缩放或在 collar 外增加有限校正，都不能修正这一具体比值。

## 1. 原基底与固定物理 collar

原 R37/R45 的几何为
$$
T_s=kN,\qquad N_s=-kT-B,\qquad B_s=N,
$$
$$
\alpha_s=h^2T,\qquad X(s,u)=\alpha(s)+uN(s).
\tag{1}
$$
R56 的实际活动坐标满足
$$
z=\xi+\omega(s)>0,\qquad u=\frac{h(s)}z.
\tag{2}
$$
$\xi$ 窗口及其两个开放 collar 是整词共同固定的。
R521/R526 的恢复要求各校正场在这些 collar 恒为零。
因而任何继续保留同一 collar 的有限曲面族，在相应开片上都准确等于
$X(s,h/(\xi+\omega))$，不是仅一阶或渐近相等。

下面设该有限曲面后来成为所需的闭 $C^2$ 嵌入面 $\Sigma$。
若它尚未嵌入，本课题的几何主门本来已经未满足；
本文的 reach 必要界只在这种假设下使用。

## 2. 原 ruled 片的完整形算子

先在 $(s,u)$ 坐标求导，避免把固定 $\xi$ 导数与固定 $u$ 导数混合。
置
$$
A=h^2-ku,\qquad a^2=A^2+u^2.
\tag{3}
$$
由于 $h>0$，$A,u$ 不会同时为零，故 $a>0$。
由(1)直接得到
$$
X_s=A T-uB,\qquad X_u=N,
$$
$$
E=a^2,\qquad F=0,\qquad G=1,\qquad
n=\frac{uT+A B}{a}.
\tag{4}
$$
其中 $n$ 是选定的单位法向。二阶导数为
$$
X_{ss}=(2hh_s-k_su)T+(Ak-u)N,
$$
$$
X_{su}=-kT-B,\qquad X_{uu}=0.
\tag{5}
$$
所以第二基本形式的真实坐标分量为
$$
b_{ss}=\frac{u(2hh_s-k_su)}a,\qquad
b_{su}=-\frac{h^2}a,\qquad b_{uu}=0.
\tag{6}
$$
在正交单位切基 $(X_s/a,N)$ 中，形算子准确写成
$$
\boxed{
S=
\begin{pmatrix}
\dfrac{u(2hh_s-k_su)}{a^3}&-\dfrac{h^2}{a^2}\\[2mm]
-\dfrac{h^2}{a^2}&0
\end{pmatrix}.}
\tag{7}
$$
(7)保留全部实际高度、曲率和速度；没有将基底换成中心线曲率模型。

由此
$$
\boxed{K_\Sigma=-\frac{h^4}{a^4},\qquad
\max(|\kappa_1|,|\kappa_2|)
 \ge\frac{h^2}{a^2}.}
\tag{8}
$$
第二式也可由 $|\kappa_1\kappa_2|=h^4/a^4$ 得到。
(2)只是同一表面的光滑坐标变化，不改变这些主曲率。

## 3. 原起点给一个独立于 δ 的 reach 上界

R544 原真实零 history 起点为
$$
h=H,\qquad k=0,\qquad \omega=\Omega,\qquad
h_s=k_s=0.
\tag{9}
$$
这里不假设 $k$ 在起点开放邻域恒定，也不需要 $k_{ss}=0$。
固定一个原开放 collar 内的 $\xi_c$，置
$$
z_c=\xi_c+\Omega>0,\qquad u_c=H/z_c.
$$
将(9)代入(7)，得到该真实 collar 点的两条主曲率
$$
\kappa_{1,2}
 =\pm\frac{H^2}{H^4+u_c^2}.
\tag{10}
$$
对闭 $C^2$ 嵌入面，reach 不大于任一主曲率绝对值的倒数。
这是 R4/R25 已用的局部必要界；它只给 reach 上界，不给全局下界。
因此任意保该 collar 的完成面均满足
$$
\boxed{
\operatorname{reach}(\Sigma)
 \le \rho_c:=H^2+\frac1{z_c^2}.}
\tag{11}
$$
$H,\Omega,\xi_c$ 在最后选择 $\delta$ 前已固定，所以 $\rho_c$ 与 $\delta$ 无关。
由于完成面在一个开片上准确等于原 $X$，它在(10)处的二 jet 也准确相同；
无需对有限校正使用任何“小 $\varepsilon$ 因而曲率近似”的论证。

## 4. 首高尾给实际表面直径下界

记 R570 §6 的首高尾起止参数为 $s_a,s_b$。
原位置 ODE 和已付慢图估计给
$$
\alpha(s_b)-\alpha(s_a)
 =-\Lambda_{R,\delta}n_a+E_{R,\delta},
\qquad |n_a|=1,
$$
$$
|E_{R,\delta}|\le C_R,\qquad
\Lambda_{R,\delta}
 \ge c_0\frac{\sqrt R\log R}{\delta}.
\tag{12}
$$
其中先固定一个足够大的有限 $R$，再取最后小 $\delta$；
$c_0>0$ 来自 R570 的共同原盒，$C_R$ 是这个固定 $R$ 的有限常数。
若只采用固定 $R$ 版本，也可把右侧常数写作
$A_R/\delta$，其中 $A_R>0$，不影响以下极限。

首高尾属于原公共前缀。其后为支付八矩及 pose 所作的重解，不删除这段；
R570 已在完整共同参数盒上保留(12)。
这里使用整个向量的长度，因此不需要另借某个最终空间轴的方向选择。

把同一个固定 collar 参数 $\xi_c$ 代入真实表面。
这两个完成面上的点为
$$
x_a=\alpha(s_a)+u_a N(s_a),\qquad
x_b=\alpha(s_b)+u_b N(s_b),\qquad
u_j=\frac{h(s_j)}{\xi_c+\omega(s_j)}.
\tag{13}
$$
固定 $R$ 后，原合法紧盒给 $h$ 有限上界、$z$ 严格正下界，
故 $|u_a|+|u_b|\le C_R$，其中的常数不随最后 $\delta$ 发散。
于是由反三角不等式，
$$
\begin{aligned}
D_\Sigma
&:=\operatorname{diam}(\Sigma)
 \ge|x_b-x_a|\\
&\ge|\alpha(s_b)-\alpha(s_a)|-|u_a|-|u_b|\\
&\ge c_0\frac{\sqrt R\log R}{\delta}-C_R'.
\end{aligned}
\tag{14}
$$
这是实际表面直径的下界，不把不一定属于物理片的中心线
$\alpha$ 直接当成曲面点。
也没有把原半词最终净位移、整个闭词净位移或一个直径上界
错用为 $D_\Sigma$ 的下界。

最终闭词的总位移虽然为零，(13)这两个已存在的 collar 点不会因此消失。
在 collar 外增加任何帽、连接或其它校正，也只能使整面包含更多点；
它不能降低(14)这条必要下界。

## 5. 准确的归一化比例与量词

联合(11)(14)，只要(14)的分母正，就有
$$
\boxed{
\frac{\operatorname{reach}(\Sigma)}{D_\Sigma}
\le
\frac{\rho_c}
 {c_0\sqrt R\log R/\delta-C_R'}.}
\tag{15}
$$
若再取
$$
0<\delta\le
\frac{c_0\sqrt R\log R}{2C_R'}
$$
（$C_R'=0$ 时略去此条件），则
$$
\boxed{
\frac{\operatorname{reach}(\Sigma)}{D_\Sigma}
\le
\frac{2\rho_c}{c_0}\,
\frac{\delta}{\sqrt R\log R}
\longrightarrow0
\quad(\delta\downarrow0).}
\tag{16}
$$
严格的量词是：先固定原母、$H,H_0,\Omega$、一个已选足够大的有限 $R$
及全部有限词，然后对该族令 $\delta\to0$。
未知的 $C_R'$ 不能藏进一个跨 $R$ 的统一低阶项；
这里只在固定 $R$ 后使用其有限性。

特别对每份这种固定资料，存在正阈值，使阈值以下所有保该 collar 的
完成面都违反 README 的 $\operatorname{reach}/D\ge0.03$。
例如由(15)得到的一个充分排除条件是
$$
\delta<
\frac{c_0\sqrt R\log R}{C_R'+\rho_c/0.03}.
\tag{17}
$$
本文没有算出一个实际已登记有限 $\delta$ 的全部常数，
所以不据(17)断言所有有限参数都被排除。

若将整个空间几何作相似缩放 $X\mapsto L X$，reach 与直径同乘 $L$，
故(15)(16)的比例不变。整体放大不能修复这一失配。

## 6. 对后继输入的具体要求

本稿的界只使用两个已经准确存在的对象：
原起点固定 collar 的局部二 jet，以及首高尾上两个固定 collar 点。
因此仅将 R570 最后的 pose 群代数闭合改得更精确、再添一段抵消净位移、
或先把第四有限矩全部消去，都不会改变(15)。

若继续这个 ruled 输入，新的紧凑构造必须实际改变至少一个来源：

- 在整个长段上控制位置的所有部分积分，避免 R570 的长近轴漂移；
- 让全路径（包括最早固定 collar）的物理曲率半径与直径同尺度，
  并同步支付高度比例、合法窗口、矩端点和完整 ruling；
- 或更换允许的局部几何输入／控制机制，再对同一个实际完成面核查 reach。

第一项要求的是整条路径的空间范围，不只是终点位置。
第二项也不能只把首段的 $H$ 单独改大而沿用旧以固定 $H$、
$R/H\to\infty$ 和最后小 $\delta$ 为前提的所有估计。
改变这些尺度时，原稳定支、真实 history、全部端图和副本窗口须在
新的一次初选中重新支付。

本文不证明这些新输入不可行，也不把尚未构造的紧凑控制称为已实现。
它明确给出当前已登记分离尺度返回族与主门之间一个不能由形式阶数
继续增加而消去的定量差距。

## 7. 直接来源

- [R37](../results/R37-closed-geometry-zero-period-operator.md)、[R45](../results/R45-reversal-four-block-third-period-cancellation.md)：原 frame、中心线与 ruled 基底。
- [R56](../results/R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)：物理 $u=h/(\xi+\omega)$ 与同一双 collar。
- [R544](../results/R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：原零 history 初态与参数次序。
- [R570](../results/R570-neutral-residence-pose-and-real-four-piece-return.md) §6：首高尾的完整慢图和原位置 ODE 位移尺度。
- [R4](../results/R4-reach-limited-port-length.md)、[R25](../results/R25-cosine-core-outward-port-budget.md)：reach 的局部法曲率必要界与实际直径下界的使用范围。
