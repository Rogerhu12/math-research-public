# R654：释放停留段与接点 jets 的真实四端隐式图

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

**已证明的条件定理。** 设 [R651](R651-four-true-even-ends-affine-rest-time-chart.md) 的具体运动段给出严格为正的四个零目标时长、原长度盒和其余物理盒的严格裕量。则同一四端根附近存在一个真实形状图：旧停留内部和旧接点的一、二阶 jets 均可改变，四个真实偶端仍精确为零。分段物理坐标和整段固定归一坐标上的全部时间导数如下。图外输入须重新解四端；图内一般点的控制 Jacobian 必须由**当前**完整积分重新计算。该定理不假设 R651 的有限搜索已经得到正时长，也不假定全 ruling 有根。

## 1. 满秩物理输入可以先作保四端的三阶接边

把源曲线按物理时间分成有限段，第 $j$ 段以 $t\in[0,1]$ 表示，时长 $D_j>0$，基础场为 $B_j(t)=(h_j,k_j)$。其中四段时长是独立控制 $\tau_1,\ldots,\tau_4$。源在这些段 $B_j$ 为常数，接点的物理一、二导数由两侧共同给出。R651 的实际多项式移动段在静止端的一、二阶导数都为零，但各侧三阶导数未必相同。在固定材料 $t$ 上积分，没有跨移动接点微分的问题。若在固定归一 $x=s/L$ 上求加速度的参数导数，可以先把基础接边升至 $C^3$。

具体地，在每个静止移动端点附近的宽度 $\epsilon$ 内，以从端点起的局部距离 $r$ 计，将 $B-B_{\rm end}$ 乘
$$
\chi(r/\epsilon),\qquad
\chi(z)=35z^4-84z^5+70z^6-20z^7\quad(0\le z\le1),
$$
其余处 $\chi=1$。$\chi'(z)=140z^3(1-z)^3$，两端一至三阶导为零；端点值被保留，移动段在静止端的前三导均为零，分段 $C^3$。各修改邻域取不相交。因 $B-B_{\rm end}=O(r^3)$，其前两导分别为 $O(r^2),O(r)$，乘积规则给总 $C^2$ 改变量 $O(\epsilon)$。初始非零中心速度端不作修改。R651 的各移动段只动 h 或只动 k；升阶不会改变端点 $(h,k,\eta)$：固定 k 段 $\eta$ 恒定，固定 h 段有 $\Delta\eta=\Delta k/(2h)$。此结论也包括在一个静止点插入并回到原状态的轴向 k 往返。

因此四个静止列仍精确为同一可逆 $V$，移动段积分 $b_\epsilon\to b$。取 $\tau_\epsilon=-V^{-1}b_\epsilon$，新曲线四端仍精确为零且 $\tau_\epsilon\to\tau$。由全部严格裕量，充分小的 $\epsilon>0$ 保时长、长度和所有原场盒。这给出可选择任意小有理 $\epsilon$ 的 $C^3$ 基础；实际给定数值时，必须重付该基础的 $b_\epsilon$、时长和场界，不能转移原积分证书。以下在这种基础上工作。

## 2. 释放整条曲线，包括每个旧接点的速度、加速度

记 $S_j=\sum_{m<j}D_m$，$L=\sum_mD_m$。在每段同一物理点取
$$
s=S_j+D_jt,\qquad x_j(t)=\frac{S_j+D_jt}{L},\qquad
C_j(t)=B_j(t)+F_q(x_j(t)),\quad C=(h,k).
\tag{1}
$$
$F_q=(f_q,g_q)$ 是定义在整条 $[0,1]$ 上的有限维 $C^3$ 扰动，$F_0=0$。只施加原中心/末端的线性 germ，例如 $f'_q(0)=0$、$g_q(0)=g''_q(0)=0$、$f'_q(1)=g'_q(1)=0$。这里直接用物理 k，持续检查真实中心速度与 $B_2$。若另要求固定归一中心导数 $k_x(0)$，其方程必须包括改变的 L。在各旧内接点不对 $F_q$ 附加零条件。对任一有限组内接点，可在不交的小邻域用光滑 cutoff 乘二次多项式，分别给两分量任意值、一阶和二阶 jet；也可在每个旧停留内部取非零紧支方向。因此 (1) 的扰动空间可实际包含这些方向。四个时长的自动修正不会抵消其在源内接点的物理 jets：基础 $B'_j,B''_j,B'''_j$ 在那里均为零，且 $F_0=0$。

每段的真正物理导数是
$$
C_s=B'_j/D_j+F'_q/L,\qquad
C_{ss}=B''_j/D_j^2+F''_q/L^2 .
\tag{2}
$$
两侧扰动在同一个 $x$ 有相同值和物理一、二导。因此全部接边始终 $C^2$，邻近参数给 $C^2([0,1]_x)$ 连续族。源的旧常值段在 $q\ne0$ 时可以有非零速度、加速度；只调固定平段的长度则做不到。

在固定材料 $t$ 对 $(q,\tau)$ 的任意方向取点号，记 $\delta F_q$ 仅对系数求导。写 $D=D_j,x=x_j$，则
$$
\dot x=(\dot S_j+t\dot D-x\dot L)/L,\qquad \dot L=\sum_m\dot D_m,
$$
$$
\begin{aligned}
\dot C &=\delta F_q+F'_q\dot x,\\
\dot C_s &=-B'_j\dot D/D^2
 +(\delta F'_q+F''_q\dot x)/L-F'_q\dot L/L^2,\\
\dot C_{ss} &=-2B''_j\dot D/D^3
 +(\delta F''_q+F'''_q\dot x)/L^2-2F''_q\dot L/L^3 .
\end{aligned}\tag{3}
$$
基础 $B_j$ 在本图中固定。若工作读出固定原归一点 $x$ 而非材料点，则 $t=(Lx-S_j)/D$，$\dot t=(x\dot L-\dot S_j-t\dot D)/D$。应以 $\delta F_q$ 代替总的 $\dot F$，并给基础 $B_j,B'_j/D,B''_j/D^2$ 的导数分别增加 $B'_j\dot t,B''_j\dot t/D,B'''_j\dot t/D^2$。第 1 节的接边使这些导数在移动接点两侧一致。

## 3. 原非局部 $\eta$ 和四端的真正控制矩阵

写 $\nu=k_s$。每段都要在同一状态积分
$$
\eta_j(t)=\eta_j(0)+\int_0^t D_j\frac{\nu}{2h}\,du,
\quad
\dot\eta_j(t)=\dot\eta_j(0)+\int_0^t
\left[\dot D_j\frac{\nu}{2h}
+D_j\left(\frac{\dot\nu}{2h}-\frac{\nu\dot h}{2h^2}\right)\right]du .
\tag{4}
$$
第一段中心值与导数均为零，后段初值均继承上段完整末值。固定归一 $x$ 的部分段还须加当前上限项 $D_j\nu(t)\dot t/(2h(t))$。这保留旧停留变为运动后对以后所有 $\eta$ 的影响。

以 R651 (1) 的完整四密度为 $m(h,k,\eta,h_s,k_s)$，则
$$
E(q,\tau)=\sum_j\int_0^1 D_j m_j\,dt,\qquad
\dot E=\sum_j\int_0^1(\dot D_jm_j+D_jDm_j[\dot h,\dot k,\dot\eta,\dot h_s,\dot k_s])\,dt .
\tag{5}
$$
其中 $\dot d=\dot h\eta+h\dot\eta-\dot k$、$\dot v=\dot h_s\eta+h_s\dot\eta-\dot k_s/2$，$\dot u=\dot h_s/h-h_s\dot h/h^2$。由有限段、严格正 h 与时长和 (1)–(4)，$E$ 对参数 $C^1$。在 $q=0$ 各旧停留真正静止，$E(0,\tau)=b_\epsilon+V\tau$，故在上述保四端源 $E_\tau=V$ 可逆。隐函数定理给唯一局部 $C^1$ 时长图 $\tau(q)>0$，使 $E(q,\tau(q))=0$。总方向为
$$
\boxed{D_q\tau=-[E_\tau(q,\tau(q))]^{-1}E_q(q,\tau(q)).}
\tag{6}
$$
在每个当前非零 $q$，须从 (1)–(5) 的同一真形状、真 $\eta$ 重新积分自由列和四条时长列，再作当前四行解；一次线性预测 $-V^{-1}E$、冻结 $\eta$ 或删掉 $\dot D_jm_j$ 均不给 (6)。数值控制验收须检查实际正时长、原 L 和所有原场盒、当前控制矩阵、原十端；有限求积根仍需要同态 fine 和连续误差资格。

## 4. 真实全段物理盒的直接充分条件

设 $m_B=\min B_h$，$m=m_B-\|f_q\|_\infty>0$。同一基础运动和当前实际时长下，记 $\eta_B$ 为未加全局扰动时的真积分。把两条路径的 $d\eta=dk/(2h)$ 相减，得到
$$
\eta-\eta_B
=\int_0^x \frac{g'_q(y)}{2h(y)}dy
 -\sum_{\text{已走的段或部分段}}\int
  \frac{B'_{k,j}(t)f_q(x_j(t))}{2B_{h,j}(t)h(t)}dt .
$$
故
$$
\boxed{\|\eta-\eta_B\|_\infty\le
\frac{\|g'_q\|_\infty}{2m}
+\frac{\|f_q\|_\infty\mathrm{TV}(B_k)}{2m_Bm}.}
\tag{7}
$$
各轴向单调段的 $\eta_B$ 由原准确端值取得，$\mathrm{TV}(B_k)$ 为各段 k 改变量绝对值之和。上述 cutoff 保单调：从端点看，$\chi$ 与 $|B-B_{\rm end}|$ 均非降。对 h/k 用基础极值加扰动上界；对两速度用
$$
\|h_s\|_\infty\le\max_j\frac{\|B'_{h,j}\|_\infty}{D_j}
+\frac{\|f'_q\|_\infty}{L},\qquad
\|k_s\|_\infty\le\max_j\frac{\|B'_{k,j}\|_\infty}{D_j}
+\frac{\|g'_q\|_\infty}{L}.
$$
这些充分量能在整段上支付原 h/k/η/γ/υ 盒；界不够紧时不能据它判实际越界。在严格内点有足够小的扰动保持全部资格。一个具体 256 列选择为 $\cos(j\pi x),0\le j\le128$ 与 $\sin((j+1/2)\pi x),0\le j\le126$，可乘任意固定正列尺度。其函数与一阶导范数由全部系数绝对和及频率加权绝对和控制。第一组张成 $P(\cos\pi x)$；第二组张成 $\sin(\pi x/2)Q(\cos\pi x)$，因为半整数正弦除以 $\sin(\pi x/2)$ 等于 $1+2\sum_{m=1}^j\cos(m\pi x)$。内点的乘子和坐标导数均非零，多项式 Hermite 插值因此可给至多 42 个不同内接点独立指定两场 0–2 阶 jets。这里的形状列是新材料图上的全局基，不继承 R641 的数值资格。

## 5. 原全部历史、ruling 与同态读出

每个原 $A$ 密度 $M_\ell$ 的同态部分和是 $\sum\int D_jM_\ell$。对每分量用 (5) 的同型公式；对原奇槽按 [R609](R609-true-integral-histories-and-kinetic-input.md) 减完整末积分及其**全导数**以锚定末零，偶槽保中心零。两侧六个原 $\rho$ 以完整原系数、$A$、$C_s,C_{ss}$ 和符号反射重建；写其物理率为 $R$，每段微分 $\int(\dot D_jR+D_j\dot R)$，包括 $\dot A,\dot C_{ss}$。固定 $x$ 的部分段仍有 $D_jR(t)\dot t$ 上限项。源正势系数 1、中心势差、两条 ruling 和常 gauge 投影的原链保持。$\dot L=\sum\dot D_j$ 进入原归一时间与 ODE 读出，不能用固定总长的替代式。

同一粗/细物理曲线由相同 $B_j,F_q,D_j$、原八中心 A 和三个 gauge 确定。固定 fine 时这些量全部冻结，按同一 $x$ 重新积分；不得另解四时长、重锚、或省略移动时间后把另一条曲线称为同态。四端图只提供完整 ruling 求解的可变真实输入。原十八块、正势、原绝对门及后续 period/pose 和全时闭曲面几何仍需实际支付。
