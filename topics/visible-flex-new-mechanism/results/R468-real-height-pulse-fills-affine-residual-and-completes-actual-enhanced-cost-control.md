# R468：真实高度脉冲补足仿射余商与完整增强成本的有限 C1 截面

日期：2026-11-16。**完整纸面证明。没有执行符号程序、原根恢复、profile 求积或新的数值、秩与几何计算。**

本文继续 [R465](R465-complete-zero-weight-affine-head-and-two-mirror-self-membership-gates.md) 与 [R466](R466-complete-mirror-anchor-identity-and-enhanced-minus6-minus4-cone-reduction.md) 的同一实际母库、同一完整增强映射 $J_{\rm aff}$。新增的是一条真实几何参数族：它先由原八矩桥精确保持整块 $M=0$，再与同一块的真倒行配对，使 $M=\mathbf T=0$。这条族能够补足原 $DQ+NQ$ 未覆盖的唯一余维。

本文不把“满闭锥”本身当作实际半群的结论。实际升级还使用下文明确构造的非零几何导数、严格正整数配平、原桥全基准、两次完整商校正及最后的有限响应收缩。

## 1. 结论：两个零成员条件可减为一个共同线性关系

使用原完整成本空间 $U$、响应空间 $\mathcal R$，以及 R463/R465 的有限真仿射稳定映射
$$
J=J_{\rm aff},\qquad
P=J(U),\quad L=J(\mathcal R),\quad Q=P/L.
\tag{1}
$$
$D$ 为真正伸缩的生成元，$N$ 为真平移生成元。令
$$
\mathcal A_Q=DQ+NQ,\qquad Z=Q/\mathcal A_Q.
\tag{2}
$$
R465 已给自然同构
$$
Z\simeq Q_0/NQ_1\simeq S(\mathcal W_0)/S(\mathcal K_0)
=\operatorname{span}\{\mathfrak h,\mathfrak y\}.
\tag{3}
$$
右边的 $\mathfrak h,\mathfrak y$ 是**同一个完整 self 商中的两个向量类**，不是两个数，也不是在不同母、宽度或补偿响应下各自取得的值。

R466 的满闭锥判据是
$$
\boxed{
\overline{\operatorname{cone}(J\mathcal S)}=P
\iff
\mathfrak h\in\operatorname{span}\{\mathfrak y\},
}
\tag{4}
$$
其中 $\mathcal S$ 是同一 scalar 常值 germ、frame $I\to I$、$M=\mathbf T=0$ 的有限真实成本集合。

**本文主定理。** 在原 R463/R428 的共同合法窗口实施前提下，(4)也足以给 $J$ 的实际有限 $C^1$ 截面：对任意紧相容目标集 $\mathcal K\subset P$，存在其有界开邻域 $\mathcal O$ 和一个固定有限真实词族 $\mathscr B(z)$，使
$$
M_{\mathscr B(z)}=\mathbf T_{\mathscr B(z)}=0,\qquad
F_{\mathscr B(z)}:I\to I,\qquad
J(V_{\mathscr B(z)})=z\quad(z\in\mathcal O).
\tag{5}
$$
所有辅助整数、构件类型及词顺序固定，只有有限真实参数按 $z$ 作 $C^1$ 变化。

共同窗口前提要求：同一母库、右锚、下文选出的有限路径、补偿桥、原型和它们的小紧参数族，从起点纳入一个合法物理窗口。没有声称任意旧冻结窄窗口能容纳这些新几何；目标邻域内也不再改变母或右锚。

三种情况应分开：

| 同一商中的实际关系 | 仿射余商 $Z$ | 本文使用的实际接口 |
|---|---:|---|
| $\mathfrak h=\mathfrak y=0$ | $0$ | R463 已有双参数截面 |
| $\mathfrak y\ne0,\ \mathfrak h=c\mathfrak y$ | $1$ 维 | 原仿射参数加本稿一个真实高度脉冲参数 |
| $\mathfrak h\notin\operatorname{span}\{\mathfrak y\}$ | 至少保留正字符障碍 | R466 的 $\lambda_+$ 经 $J$ 下降，满闭锥及任意目标控制均不成立 |

因此，在同一实施前提下，
$$
\boxed{
\mathfrak h\in\operatorname{span}\{\mathfrak y\}
\iff
\text{$J$ 有(5)的实际有限 $C^1$ 截面}.
}
\tag{6}
$$
这里没有预判正在消费的四个完整 self 原式给出哪种关系。特别，两个目标分别非零或分别不是响应成员，均不足以否定第一列共同关系。

## 2. 唯一余字符必有非零加速度系数

$D$ 在非零权上可逆，故(2)只保留 $Q_0/NQ_1$。R465 的同构还说明：$Z^*$ 拉回 $U^*$ 后，恰由杀 $\mathcal R$、$D$ 和 $N$ 的相应真实权零仿射字符组成。

R196 的全部此类头字符是 $\lambda_{x,y}$。对 R465 已作 whole-$E$ 与完整 current 校正的两代表 $V_H,V_Y$，
$$
\lambda_+(V_H)=1,\quad\lambda_+(V_Y)=0,\qquad
\lambda_{0,1}(V_H)=0,\quad\lambda_{0,1}(V_Y)=1,
\quad\lambda_+=\lambda_{-1,0}.
\tag{7}
$$
这些等式来自原 $C_2,C_4,C_6$ 头及真实响应校正，不从 self 最高项猜测。

现设 $\mathfrak y\ne0$、$\mathfrak h=c\mathfrak y$。取 $Z$ 的一个非零对偶 $\theta$，记
$$
\beta=\theta(\mathfrak y)\ne0.
$$
它拉回完整 $U$ 的值由(7)唯一确定：
$$
\boxed{
\theta\circ\bar q\circ q\circ J
=c\beta\lambda_++\beta\lambda_{0,1}
=\lambda_{-c\beta,\beta},
}
\tag{8}
$$
$q:P\to Q$、$\bar q:Q\to Z$ 为两个商映射。

所以这一真正剩余的头必满足 $y=\beta\ne0$。它不能是唯一非负射线 $\lambda_+$。这就是下文真实脉冲可用的具体原因；并非对任意余商都无条件假定有几何横截。

## 3. 保持原 frame、omega 与全部 germs 的高度脉冲

先固定任意原 scalar 常值 germ
$$
g=(h_0,k_0,\omega_0),\qquad h_0>0.
$$
由 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) §1，选择一条有限真实同 germ、frame $I\to I$、$M=0$ 路径 $B$。其某个开常值 collar 有正长度。在该 collar 的内部固定 $s_0$，取
$$
0\ne\chi\in C_c^\infty((-1,1)),\qquad a\in[1/2,3/2].
$$
$\chi$ 在实轴外延为零。对充分小的有限 $\varepsilon>0$，仅在
$s_0+\varepsilon(-1,1)$ 内改变
$$
\log h_{\varepsilon,a}(s)
=\log h_0+\varepsilon a\,
\chi\!\left(\frac{s-s_0}{\varepsilon}\right),
\qquad
k_{\varepsilon,a}=k_0,\qquad
\omega_{\varepsilon,a}=\omega_0.
\tag{9}
$$
其余路径与 $B$ 完全相同，记为 $B_{\varepsilon,a}$。

(9)保留的都是原物理等式：

- $h_{\varepsilon,a}>0$，且 $h_{\varepsilon,a}-h_0=O_{C^1(a)}(\varepsilon)$；
- 脉冲内 $k_s=0$，故原水平关系 $\omega_s=k_s/(2h)$ 准确成立；
- $k$ 在整条 $B$ 上完全未变，故原 frame 方程 $F_s=F\Omega(k)$ 的解及首末 frame 完全未变；
- 使用同一个真实时间区间，没有压缩整条路径或重置其起点；
- 脉冲支撑严格位于 collar 内部，全部原端 germs、连接处 jets、同一 $\xi$ 与同一右锚均保留。

这一步只保持 frame 和端口，**尚未保持 $M=0$**。下一节支付这个缺口。也没有把(9)当作对旧固定目标度量的微小误差修补：它是构造新实际几何的一条有限参数族。

## 4. 八矩缺陷只有 $O_{C^1(a)}(\varepsilon)$，并由独立前缀准确补偿

R130(1)中的完成分部积分后的原八矩密度是
$$
m=m_0(S)+m_2(S;h_s,k_s),\qquad S=(h,k,\omega),
\tag{10}
$$
其中 $m_2$ 对一阶速度齐次二次。此处没有遗漏一个仍未消掉的 $h_{ss}$ 项；原平端分部积分端项分别为零。

在(9)的固定 $a$ 盒上，
$$
h_s=h_{\varepsilon,a}\,a\chi',\qquad k_s=0.
$$
$h_s$ 及其 $a$ 导数统一有界，$S-S_0$ 及其 $a$ 导数均为 $O(\varepsilon)$。因此：

- 静态密度的变化及其 $a$ 导数为 $O(\varepsilon)$，再乘支撑长度给 $O(\varepsilon^2)$；
- 速度二次密度及其 $a$ 导数有统一有限界，乘支撑长度给 $O(\varepsilon)$。

所有其它路径部分未变，故
$$
\Delta M_{\varepsilon,a}
:=M(B_{\varepsilon,a})-M(B)
\quad\text{满足}\quad
\boxed{\|\Delta M_{\varepsilon,\cdot}\|_{C^1(a)}
\le C_M\varepsilon.}
\tag{11}
$$
这里 $C_M$ 与小 $\varepsilon$ 无关。没有要求(9)在 $C^2(s)$ 或更高范数中趋近原路径；事实上 $h_{ss}$ 可以按 $\varepsilon^{-1}$ 增大。

独立使用 R70 的局部矩阵目标截面：存在一个固定有限真实前缀族 $A(Z)$，对 $Z$ 在八维无迹矩阵空间的零邻域，
$$
M(A(Z))=Z,\qquad
F_{A(Z)}:I\to I,\qquad
A(Z):g\to g.
\tag{12}
$$
辅助圈数在该邻域固定，全部原状态、长度、所需有限 jets 对 $Z$ 光滑依赖；不是在每个 $\varepsilon$ 上重新放大辅助圈数。

取
$$
W_{\varepsilon,a}
=A(-\Delta M_{\varepsilon,a})\,B_{\varepsilon,a}.
\tag{13}
$$
因为 $M(B)=0$，原矩阵拼接给
$$
\boxed{M(W_{\varepsilon,a})=0}
\tag{14}
$$
并保同 germ 及 frame $I\to I$。

重要的加法边界是：一般
$M(A(-\Delta M_{\varepsilon,a}))\ne0$ 且
$M(B_{\varepsilon,a})\ne0$。本文**不**写
$V_W=V_A+V_B$。两部分真实二、三阶累计历史及所有第四交叉都留在完整 $V_W$ 内。下面仅对已经证明可用的局部标量 action 分段积分。

## 5. 同一个完整 action 给真正非零的横向导数

令 $\lambda=\lambda_{x,y}$，其中 $y\ne0$。沿路径记
$$
\rho=(\log h)_s.
$$
R196(12)取同一个乘子参数 $\alpha=0$ 后，完整局部 action 为
$$
\begin{aligned}
I_\lambda(B)=\int_B\bigg[
&y\rho_s^2+y\rho^4-\frac y3 k_s^2
-\frac{11y}{3}k\rho k_s\\
&+y\left(1-\frac43k^2\right)\rho^2
-(x+y)k^2+yk^4
\bigg]\,ds .
\end{aligned}
\tag{15}
$$
它包含原 $\Gamma$、同一个八矩乘子与完成分部积分后的全项。原高阶交叉 $2y\rho_s\rho^2$ 的积分为
$2y[\rho^3]/3=0$，因为每条路径有原常值 germs。

R109/R130/R196 给出的准确使用条件是
$$
\boxed{\lambda(V_W)=I_\lambda(W)\quad\text{当整条 }W\text{ 满足 }M_W=0.}
\tag{16}
$$
(16)不要求 $\mathbf T_W=0$。局部积分 $I_\lambda$ 可以按真实平端连接相加；一般非零矩阵的完整 $V$ 不在此相加。

设
$$
A_\chi=\int_{-1}^1(\chi'')^2>0,\quad
B_\chi=\int_{-1}^1(\chi')^4,\quad
C_\chi=\int_{-1}^1(\chi')^2.
$$
若 $A_\chi=0$，$\chi$ 为 affine 且实紧，迫 $\chi=0$，故第一项严格正。

在脉冲内，$\rho=a\chi'$、$\rho_s=a\chi''/\varepsilon$、$k_s=0$，其原静态 $k$ 项与同时间长度的常段完全相消。因此得到**准确差式**
$$
\boxed{
I_\lambda(B_{\varepsilon,a})-I_\lambda(B)
=
\frac{y a^2}{\varepsilon}A_\chi
+\varepsilon y a^4 B_\chi
+\varepsilon y\left(1-\frac43k_0^2\right)a^2 C_\chi .
}
\tag{17}
$$

前缀修正的 action 有独立的 $C^1$ 估计。令
$\mathcal I_A(Z)=I_\lambda(A(Z))$。R70 的固定有限光滑族及(15)使
$\mathcal I_A$ 在一个固定紧目标邻域上为 $C^1$，且导数有界。
由(11)与链式法则，
$$
\begin{aligned}
&|\mathcal I_A(-\Delta M_{\varepsilon,a})-\mathcal I_A(0)|
\le C_A|\Delta M_{\varepsilon,a}|,\\
&\left|\partial_a\mathcal I_A(-\Delta M_{\varepsilon,a})\right|
\le C_A|\partial_a\Delta M_{\varepsilon,a}|,
\end{aligned}
$$
从而
$$
\boxed{
\|\mathcal I_A(-\Delta M_{\varepsilon,\cdot})
-\mathcal I_A(0)\|_{C^1(a)}=O(\varepsilon).
}
\tag{18}
$$
这里所有前缀自身的四阶成本通过真实 action 保留；它们没有因“补偿 $M$”而被删除。
(18)使用的是有限参数目标的小变化，不调用一个不适用的 $C^r(s)$ 小扰动定理。

现在才使用真倒行：
$$
\mathscr D_{\varepsilon,a}
=W_{\varepsilon,a}W_{\varepsilon,a}^{R}.
\tag{19}
$$
两块都是整 $M=0$、frame $I\to I$。原 R83/R130 的真实传递准确给
$$
M_{\mathscr D_{\varepsilon,a}}=\mathbf T_{\mathscr D_{\varepsilon,a}}=0,
\qquad V_{\mathscr D_{\varepsilon,a}}=2V_{W_{\varepsilon,a}}.
\tag{20}
$$
第四倒行取同号，未制造负成本。

合并(16)—(20)，令
$C_0=2I_\lambda(A(0))+2I_\lambda(B)$，得到
$$
\lambda(V_{\mathscr D_{\varepsilon,a}})
=C_0+\frac{2y a^2}{\varepsilon}A_\chi
+O_{C^1(a)}(\varepsilon),
\tag{21}
$$
以及
$$
\boxed{
\partial_a\lambda(V_{\mathscr D_{\varepsilon,a}})
=\frac{4ya}{\varepsilon}A_\chi+O(\varepsilon)\ne0
}
\tag{22}
$$
在 $a=1$ 的一个固定小邻域内成立，只须先取一个充分小但**有限正**的 $\varepsilon$。

此后 $\varepsilon$ 完全冻结。(19)是一条真实有限 $C^1$ 族，不是极限路径；其高阶几何导数可以很大但有限。后文的所有整数、目标邻域和收缩都在这一固定族上选择。

## 6. 一个通用的实际参数增强引理

下面把新增几何参数与“满闭锥”之间真正需要的步骤单独证明。它也说明第5节为何不只是又给出一个 signed span 方向。

**参数增强引理。** 设 $J$ 为同一个有限真仿射稳定映射，定义(1)—(2)。假设：

1. $\overline{\operatorname{cone}(J\mathcal S)}=P$；
2. 有有限条原同端口、$M=\mathbf T=0$ 的真实 $C^1$ 族
   $\mathscr D_j(a_j)$，在固定内部参数 $a_j^0$ 处令
   $v_j=\partial_{a_j}qJ(V_{\mathscr D_j(a_j)})$；
3. 在这个完整商 $Q$ 中，
   $$
   \boxed{DQ+NQ+\operatorname{span}\{v_j\}=Q;}
   \tag{23}
   $$
4. 全部有限原型、真实桥、这些族及其紧参数盒服从同一共同窗口实施前提。

则任意紧商目标集有一个固定有限真实 $C^1$ 商截面；继而同一个 $J$ 有(5)的完整截面。

### 6.1 有限实际正配平必须包含新增族的完整基准

满闭锥连续投影给
$$
\overline{\operatorname{cone}(qJ\mathcal S)}=Q.
$$
按 R206 的有限选择，可以取有限个实际 $M=\mathbf T=0$ 块 $B_i$，使
$$
q_i=qJ(V_{B_i}),\qquad
\operatorname{cone}\{q_i\}=Q.
\tag{24}
$$
把每个 $\mathscr D_j(a_j^0)$ 作为另一个真实块加入这个有限集合。
加入向量不会破坏满正锥。

因(24)，$-\sum_iq_i$ 有一个非负表示
$\sum_i\beta_iq_i$。令
$$
\alpha_i=1+\beta_i>0,\qquad
\sum_i\alpha_iq_i=0.
\tag{25}
$$
(25)包含新增族的**完整基准成本**。没有只保其导数、却遗漏它可能很大的非零初始值。

$q_i$ 张满 $Q$，所以
$$
\operatorname{span}\{Dq_i,Nq_i\}_i=DQ+NQ.
$$
结合(23)，仿射导数与新增参数导数共同张满 $Q$。
乘上各个严格正 $\alpha_i$ 后仍然张满。因此可以从这些有限真实参数中选 $\dim Q$ 个导数列形成可逆 minor，其余参数固定在基点。这里是已知线性空间关系的直接推论，没有新的数值或函数秩计算。

### 6.2 真实仿射桥只贡献固定的全基准，不被省略

对普通 $B_i$ 使用原真实正伸缩和平移，成本主项为
$$
f_i(t_i,c_i)=T_{c_i}e^{t_iD}q_i,
\qquad f_i(0,0)=q_i.
\tag{26}
$$
其 scalar 端口一般改变。用 R70 的原 $M=0$、frame $I\to I$ 桥
$A_i(t_i,c_i)$ 接入，并用**同一桥的真倒行**返回。
原完整传递对任意正整数 $n_i$ 给
$$
V_{A_i(B_i^{t_i,c_i})^{n_i}A_i^R}
=2V_{A_i(t_i,c_i)}
+n_i\mathsf P_{t_i,c_i}V_{B_i}.
\tag{27}
$$
(27)中的两个桥成本取同号。它们的真实第三历史相消，第四全基准留下。

对新增固定端口族，直接取 $\mathscr D_j(a_j)^{n_j}$；其成本为
$n_jV_{\mathscr D_j(a_j)}$，不需要附加一个虚构的锚修正。
若还对这一块使用仿射参数，照(27)处理即可；证明只需选取足以满足(23)的有限参数。

将所有参数合记为 $z$，选出的可逆 minor 坐标以基点 $z=0$ 表示。拼接全部实际块后，
$$
\mathcal Q_N(z)
=\sum_i n_i(N)f_i(z_i)+E_Q(z),
\qquad
n_i(N)=\lfloor N\alpha_i\rfloor\ge1,
\tag{28}
$$
其中 $E_Q$ 是全部桥的完整商成本，固定、$C^1$ 且与 $N$ 无关。
每个 $f_i(0)=q_i$。所有路径块的 $M=\mathbf T=0$，所以此处第四成本相加合法。
此前(13)内部非零矩阵部分的交叉历史已经包含在新增块 $V_{\mathscr D_j}$ 中，不在(28)重新拆分。

### 6.3 固定有限整数上的统一商截面

在固定小参数盒上，
$$
G_N(z):=N^{-1}\mathcal Q_N(z)
\longrightarrow
G_\infty(z):=\sum_i\alpha_i f_i(z_i)
\quad\text{于 }C^1.
\tag{29}
$$
由(25)，$G_\infty(0)=0$；由(23)及所选 minor，
$$
J_*:=DG_\infty(0)
\quad\text{可逆}.
\tag{30}
$$
给定有界商目标集 $Y\subset Q$，先选固定小闭球使
$$
\sup_z\|I-J_*^{-1}DG_\infty(z)\|<1/4.
$$
再取一个有限整数 $N$，使对应 $G_N$ 的上界小于 $1/2$。
floor 误差与固定桥基准使 $G_N(0)=O(N^{-1})$，而
$\sup_{y\in Y}|y/N|=O(N^{-1})$。继续增大这个有限 $N$，可使
$$
z\longmapsto z-J_*^{-1}(G_N(z)-y/N)
\tag{31}
$$
对全部 $y\in Y$ 都是同一闭球上的自映射且严格收缩。

其唯一根满足 $\mathcal Q_N(z(y))=y$。$DG_N$ 可逆，有限维 IFT 给 $z(y)$ 在 $Y$ 的一个开邻域上为 $C^1$。
因此得到一个**固定有限词与固定整数**的真实商截面 $C(y)$。
整数倍、两座桥及其所有常数项均在(28)中；不存在实数次复制、负路径或取极限当解。

完整成本 $J(V_{C(y)})$ 也为 $C^1$。其响应分量并没有被商方程指定，后文必须保留。
正则性来自同一有限路径词的原 R56 全恢复、固定锚、真实积分与已冻结有限参数盒；不是把抽象有限维直接当作几何光滑性。

## 7. 第5节怎样准确满足这个增强引理

继续第2节的一维余商情形。取
$$
q_*(a)=qJ(V_{\mathscr D_{\varepsilon,a}}),\qquad
v_*=\partial_aq_*(1).
$$
由(8)和(22)，
$$
\theta(\bar q\,v_*)=
\partial_a\lambda_{-c\beta,\beta}
(V_{\mathscr D_{\varepsilon,a}})\big|_{a=1}\ne0.
\tag{32}
$$
$\theta$ 是一维 $Z$ 的非零对偶，所以 $\bar q\,v_*$ 张满 $Z$，即
$$
\boxed{DQ+NQ+\mathbb Rv_*=Q.}
\tag{33}
$$
这是真实几何参数导数进入**完整同一商**的结论。
它不是从自然函数投影中的一个 $x^6$ 前像推断 whole $J$，也没有把代数 $\delta$ 当成几何变化。

将新增块 $\mathscr D_{\varepsilon,1}$ 的完整成本加入(24)—(25)，然后第6节给实际商截面。其前缀、脉冲、真倒行的完整基准都乘实际整数参与配平。
$\varepsilon$ 在选择这些整数前已经固定；后面不再令它依目标或最后响应整数趋零。

若 $\mathfrak h=\mathfrak y=0$，$Z=0$，则(33)不需要 $v_*$，直接是 R463 的 $DQ+NQ=Q$ 情形。至此两种满闭锥分支均已支付同一个完整商截面。

## 8. 两次完整商校正，随后才清响应坐标

为使(5)的最后实际步骤可审，本节写出全部基准，不只引用一个抽象可达性结论。
令 $r=\dim L$。从真实响应生成器中选择
$$
K_j=\mathcal B_{E_j}\tau_j,\qquad
\kappa_j=J(K_j),\qquad 1\le j\le r,
$$
使 $\kappa_j$ 为 $L$ 的基。
若采用若干原生成器的组合，就按其有限真实表达绑定相应参数；不把一个未实现的形式方向直接当路径。

每个第三 prototype $\mathscr L_j$ 具有 $M=0$、$\mathbf T=\tau_j$，完整成本记为 $v_j$。
原真配对 $\mathscr L_j\mathscr L_j^R$ 有成本 $2v_j$、$M=\mathbf T=0$，
所以 $v_j\in U$；这只是线性空间归属，不执行半条路径。

### 8.1 第一次商校正：完整保留每个 prototype 的新基准

使用第6节已经证明的商截面，给有限目标 $-qJ(v_j)$ 选择实际 $M=\mathbf T=0$ 块 $C_j$，置
$$
\widehat{\mathscr L}_j=\mathscr L_jC_j,\qquad
\widehat v_j=v_j+V_{C_j}.
$$
每块矩阵为零，第三未变，故
$$
\mathbf T_{\widehat{\mathscr L}_j}=\tau_j,\qquad
qJ(\widehat v_j)=0.
\tag{34}
$$
校正块所有响应成本留在 $\widehat v_j$；不以它的商目标替代其完整成本。

原 R101/R212 的同原型、真倒行复制字随后给
$$
J(V_{\mathscr Z(t,n)})
=E_0(t)+n\left(2\sum_jJ(\widehat v_j)
+\sum_jt_j\kappa_j\right),
\quad M_{\mathscr Z}=\mathbf T_{\mathscr Z}=0.
\tag{35}
$$
$E_0(t)$ 是完整固定的 $C^1$ 偶基准。由(34)，商为 $qE_0(t)$，与最后的 $n$ 无关。

### 8.2 第二次商校正：补偿真实 $E_0(t)$，不删其响应代价

固定线性分解 $P=L\oplus J_Q$，令 $\ell$ 取 $\kappa_j$ 基下的响应坐标。
定义
$$
a_L=2\sum_j\ell J(\widehat v_j),\qquad t^0=-a_L.
$$
先按原小二阶族的有限重复，使(35)覆盖
$t^0+[-2,2]^r$，从而冻结该盒上的全部 $E_0$。

对指定紧目标集 $\mathcal K$，取一个有界开邻域 $\mathcal O$，并考虑紧集
$$
Y_Q=\{qz-qE_0(t):
z\in\overline{\mathcal O},\
t\in t^0+[-1,1]^r\}.
\tag{36}
$$
在确定这个集合后，才调用第6节，选其同一个实际 $C^1$ 商截面
$C(qz-qE_0(t))$，固定第二批全部整数。

把它接到(35)后，完整第四加法给
$$
qJ(V_{\widetilde{\mathscr Z}})=qz,\qquad
\ell J(V_{\widetilde{\mathscr Z}})
=n(a_L+t)+F(t,z),
\tag{37}
$$
其中
$$
F(t,z)=\ell E_0(t)+
\ell J(V_{C(qz-qE_0(t))}).
\tag{38}
$$
第二项是商校正的**完整实际响应成本**。
$F$ 与 $D_tF$ 在固定紧盒上有界，并且在此时尚未选择的最后 $n$ 之外完全固定。

### 8.3 最后有限响应整数与全目标 C1 性

取一个有限 $n$，使
$$
t\longmapsto -a_L+n^{-1}\{\ell z-F(t,z)\}
\tag{39}
$$
将盒映入内部且其 $t$ 导数范数小于 $1/2$。
唯一根 $t(z)$ 给(37)的响应坐标准确等于 $\ell z$；商已经等于 $qz$。
$nI+D_tF$ 可逆，故同一根在目标邻域上为 $C^1$，得到(5)。

若 $Q=0$ 或 $L=0$，省去相应步骤；若 $P=0$，取任一实际 $M=0$ 同端口块接真倒行即可。没有用空路径替代所需真实几何。

本节的两次商校正分别处理 prototype 基准与复制字偶基准。它们不能合并成一次只清自然坐标的操作，也不能先按一个未知最后整数改变商截面，再回头声称(38)与该整数无关。

## 9. 所有选择均有限，且共同窗口与原锚不循环

为避免把存在性证明写成无法实施的参数循环，选择顺序如下。

1. 固定同一母库、$J_{\rm aff}$ 的有限真仿射查询及其完整核；使用 R465/R466 的同一 $\mathfrak h,\mathfrak y$ 关系。
2. 若余商是一维，先选第3节的常值 collar、固定 $\chi$、独立 R70 矩阵前缀族；由(22)选一个有限 $\varepsilon>0$，再冻结脉冲参数的小盒。
3. 从满闭锥选有限实际正张成块，将上一步新增块的完整基准加入；选严格正配平。固定近恒等仿射族、全部真实桥、响应基、第三 prototypes、二阶小族及需要的背景子字。
4. 全部这些有限族的小紧参数包络须满足从起点采用的共同合法窗口前提。若使用 R414 的一次共同坐标识别，它须在母库的最终物理冻结之前一并确定，并输运同一个目标；不能在目标求解后补做。此后 profile、右锚与宽度不随目标移动。
5. 选择第一批有限商整数，支付所有 prototype 的完整商基准。
6. 根据这些实际基准确定 $t^0$，固定覆盖其盒的二阶小族重复数和 $E_0$。
7. 对(36)选第二批统一商整数，冻结完整 $F(t,z)$。
8. 最后选择响应整数 $n$，用(39)取同一个有限根。

真实正伸缩和平移只在已经冻结的近恒等小盒内使用。脉冲改变高度但不改变 $\omega$；其幅度是 $O(\varepsilon)$，固定前缀参数的变化也是 $O(\varepsilon)$。所有有限族的 $h$ 有统一正下界，$\omega$ 有有限包络。
后续整数复制只重复这些路径，不扩大 scalar 包络；真实长度与中心线位移则全部累加。

这个结论不承诺预给的长度、导数上界、reach、嵌入厚度或任意窄旧窗口。固定有限 $\varepsilon$ 不是取无限高频几何极限，也不用于修补此前数值 metric 误差。

所有路径从同一原 scalar/frame 端口出发，使用同一 $\xi$ 与同一右锚。R70 补偿接在脉冲之前，整个 $W$ 的历史按原顺序恢复；不在脉冲开始处重设二、三阶积分常数。
真倒行与后续拼接也沿原历史规则。因此本证明没有删去 $\Gamma M$、原型左尾、仿射锚常数或桥的第四成本。

## 10. 对现有增强门的准确影响

### 10.1 对 R465 四列观察的消费方式

R465 的四个新完整 self 目标，目的是确定同一个响应 self 商中的 $\mathfrak h,\mathfrak y$。本文改变的是这批结果的**后果**，没有重算它们。

- 若两者都为零，R463 原双参数证明已足，本文脉冲可省。
- 若 $\mathfrak y\ne0$ 且 $\mathfrak h=c\mathfrak y$，R466 给满闭锥；第2—8节补出原仿射导数缺少的一维，得到实际完整截面。
- 若不满足这一共同关系，R466 给 $\lambda_+$ 在 $J$ 上的非负下降。其对每条正时长实际 $M=0$ 成本满足
  $$
  \lambda_+(V_B)
  =\int_B k^2\,ds
  =L_B+\int_B((\log h)_s)^2\,ds>0.
  $$
  因而实际任意目标控制及非空零成本字均受阻。

这里的“关系”必须保全部非局部字、真实左常数、所选母的原精确恒等以及统一响应补偿。
两个分别 NONMEMBER 的结果既不自动否定关系，也不自动证明关系。
一个未经真实母条件归约的 formal 余字不能替代这个有限共同商。

### 10.2 对 R467 类型的额外 vertical 标量

若另一个真实有限读出 $G$ 已被证明满足
$$
G(\ker J)=G(\mathcal R\cap\ker J),
\tag{40}
$$
则现在可以把第8节的完整 $J$ 截面交给 R463 的 vertical 引理。原理仍是：先清各响应 prototype 的完整 $J$ 基准，再清复制字的 $J$ 偶基准，保它们全部 $G$ 代价，最后有限收缩。

因此，某个后续证明若此前为了获得实际 $J$ 截面而采用
$\mathfrak h=\mathfrak y=0$，可以在**同一库、同一锚及其它原前提完全不变**时，用本文已证明的较弱条件
$\mathfrak h\in\operatorname{span}\{\mathfrak y\}$ 替换这一特定接口。
其新增 vertical 覆盖、固定第三系数、实际 incoming 历史和最高项规范仍须由该证明自己支付。
本文不替那些读出证明(40)。

### 10.3 固定 hook 背景、保护 germ 与剩余几何门

若原闭 hook 背景、scalar/frame 桥和 Klein 字从起点纳入共同包络，原成本形式仍为
$$
V_{\rm base}+4V_{\mathscr B}.
$$
用(5)付目标 $-J(V_{\rm base})/4$，可消同一个 $J$ 的全部指定读出。$V_{\rm base}$ 保留，因子4来自原真实字，不从新增脉冲另造一个系数。

原保护 germ 可以作为固定子字保留，控制接在其外并按相同端口返回。
新路径的实际 incoming $m_*$、canonical 特解以及其它未纳入 $J$ 的 period 成本须重新按原式读取；不能拿旧几何的这些量作不变数据。

若还要求原无常段、Morse 或其它结构条件，不能仅凭(5)自动宣称保持。
本稿的 $W$ 具有一个独立正规矩阵前缀，所以它可作为 R302 那类“整块保持 $M=0$、共享同一真倒行”的原语：
在固定有限 $\varepsilon$ 后，允许的小自由扰动可由该前缀矩阵右逆补偿，整 $WW^R$ 继续保持 $M=\mathbf T=0$。
但全词的额外结构自由性、允许扰动的支撑及保护 germ 范围仍须按原 R302 条件核对。
一旦这些低阶条件有真实结构保证，(5)的满目标导数才可用于恢复全部 $J$，不是用高阶 IFT 代替低阶几何证明。

## 11. 本文究竟新增了什么

原 R463 已证明 $DQ+NQ=Q$ 时可以用真实仿射参数完成 actual 控制；
R465 找到了它可能遗漏的完整零权 self 余商；
R466 排除新增负权正字符，并把满闭锥缩成共同关系
$\mathfrak h\in\operatorname{span}\{\mathfrak y\}$。

本文新增的原式步骤是
$$
\begin{gathered}
\text{余商一维且其头系数 }y\ne0\\
\Longrightarrow
\text{真 collar 高度脉冲，}\ 
\Delta M=O_{C^1}(\varepsilon)\\
\Longrightarrow
\text{独立 R70 前缀精确补整 }M=0\\
\Longrightarrow
\partial_a\lambda(V_{WW^R})
=4yaA_\chi/\varepsilon+O(\varepsilon)\ne0\\
\Longrightarrow
DQ+NQ+\mathbb Rv_*=Q\\
\Longrightarrow
\text{包含全部真实基准的有限整数配平与两次商校正}\\
\Longrightarrow
\text{同一完整 }J_{\rm aff}\text{ 的实际有限 }C^1\text{ 截面}.
\end{gathered}
\tag{41}
$$
每一箭头都在同一成本空间、同一母库和同一原历史中完成。

这个结果没有宣称四列新观察已满足关系，也没有完成所有未加入 $J$ 的 full period、全曲面 ruling、高阶收敛、嵌入、reach 或主课题。
它使当前下一步变为一个明确问题：判定同一完整商中的一个共同线性关系，而不再额外要求两个目标分别为零，或因为 $DQ+NQ$ 留一维就停止 actual 构造。

## 12. 直接来源与本文未执行范围

主要原式来源：

- [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) §1：同端口/frame、任意小八矩目标的固定有限光滑桥截面；§2：共同物理窗口范围。
- [R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) (1)—(3)：$m=m_0+m_2$、真实局部积分和整 $M=0$ 后的完整成本身份；§3：真倒行配对。
- [R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) (7)—(16)：真实两参数头、同一个乘子与完整 action；(20)：正字符的严格实际长度式。
- [R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md) §3—7、[R212](R212-C1-sections-for-complete-real-pure-cost-control.md)：有限正配平、真实桥、floor 整数、两次商校正与有限响应根。
- [R428](R428-conditional-complete-joint-cost-cone-and-finite-actual-C1-sections.md) §4—5：共同完整映射、同一窗口和全目标 $C^1$ 截面的选择顺序。
- [R463](R463-real-partial-quotients-translation-defect-and-finite-affine-control-interface.md) §8、§11—12：有限真仿射闭包、$DQ+NQ$ 与 vertical 接口。
- [R465](R465-complete-zero-weight-affine-head-and-two-mirror-self-membership-gates.md)：$Z$ 的自然商同构及两头规范。
- [R466](R466-complete-mirror-anchor-identity-and-enhanced-minus6-minus4-cone-reduction.md)：同一增强映射的负权排除与准确满闭锥判据。
- [R302](R302-regular-chi-prototypes-shared-reversal-and-enhanced-Morse-control.md)：在另需结构保持时适用的共享真实原语边界。

全部新增结论为上述原式的纸面推论。
本文未执行 profile 数值、几何求值、符号器、原根恢复、旧秩复算或任何新研究入口。
