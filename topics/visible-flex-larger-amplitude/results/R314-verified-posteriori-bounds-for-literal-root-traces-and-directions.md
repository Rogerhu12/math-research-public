# R314：literal root 有限轨迹及完整方向的条件后验误差界

作者：GPT-6 Astra Pro（exact_refinement）  
日期：2026-11-15  
类型：已证明（有限 literal 模型的条件后验定理；尚无实际区间数值证书）

## 314.1 结论与严格对象

本文在 [R305](R305-literal-gram-root-contraction-and-nominal-factor-defects.md) 的准确恒等式上，给出三层可实施的充分条件：

1. 用原名义因子、两次回代及真实 literal 矩阵的严格缺陷，包围一次线性求解的误差。
2. 用完整方向方程的严格缺陷，包围新 Gram 收缩方向相对于准确实求解映射导数的误差。名义解代入 $(dC)\widehat s$ 的误差必须单独保留。
3. 把局部界传播到实际固定的有限 root 更新、完整 226 态 RK、端口、全部 cut/stage/far 行；另以实际 $F_e$ 的可验证条件证明一个真正的有限方程根及其隐式方向。

这三层不能相互冒名。一次线性求解的误差小不等于 root 已收敛；有限次迭代轨迹的导数不等于隐式根导数；准确实表达式的导数不等于 IEEE 舍入映射的导数。所有定理均保留原 $F$ 与原独立 Gram 矩阵 $C$，不假设 $C=F_e$。

本证明不改变实际求解的 root 停止阈值、原 native 的 $2\times10^{-9}$ 阈值、原严格范数下降条件或 final-J/audit 责任。未通过下述充分条件只说明该证书没有取得，不能自动改写成一次原 native 拒绝。本文没有执行新的科学计算，也没有把现有 binary128 残差最大值升格为严格误差上界。

## 314.2 完整维度、字值与合法闭包

固定本任务原维度

$$
M=112,\qquad J=M+1=113,\qquad N=2048,\qquad 2M+1=225.
$$

root 的未知量和线性系统有 113 维；全部 Gram 矩有 225 项；shape 输入有 224 个坐标；完整 primal 有 226 态，包含两个 mean。每个 stage 从 node $n+1$ 入、向 node $n$ 出。576 段、577 节点的完整 cut/stage/far 残差有 129248 行。下文不删高模、不丢两个 mean，也不把未访问的方向列记作零。

原 cosine、sine、Gram、frequency、orientation、平方根字值等各为独立固定常数。验证器必须从实际 IEEE 原字解码有限 dyadic；不能只把打印的十进制近似当原字。binary128 的有限字也同样准确解码，NaN 或无穷不能当有限有理数。不得以三角恒等式、重新生成的三角表或“更准确的根号”替代原常数。

几何输入 $w_2,E$ 仍是各自的坐标。只有当调用者提供真实几何来源及其导数时，才沿该来源作链式法则；不能从名字推定 $w_2=w^2$ 或额外的 $E$ 恒等式。

每个用到导数或区间界的闭盒都必须处在相关准确实有限表达的定义域内部：原 $D,S,A$ 严格合法；所有除数，包括实际出现的 $r,w,w_2,\mu$ 和端口比，均排除零；平方根参数严格为正。比较原准确实 Cholesky 图时，还须证明真实 $C$ 在相应闭盒上正定。本文后面的条件都以这些完整域条件为前提。

## 314.3 非负比较矩阵给出的逆界

以下引理适用于任意有限方阵，不限于对称矩阵。向量绝对值、矩阵绝对值及不等式均逐分量解释。

**引理 314.1。** 设 $A,Y$ 为同阶实方阵，存在非负矩阵 $N_A$、正向量 $w$ 及 $0\le q<1$，使

$$
|I-YA|\le N_A,\qquad N_Aw\le qw.
$$

则 $A,Y$ 都可逆，且对任意向量 $b$，

$$
|A^{-1}b|
\le (I-N_A)^{-1}|Yb|.
\tag{314.1}
$$

**证明。** 在加权最大范数 $\|v\|_w=\max_i|v_i|/w_i$ 中，$N_A$ 的诱导范数至多为 $q$，因而 $E=I-YA$ 的诱导范数也至多为 $q<1$。Neumann 级数给出 $(YA)^{-1}=(I-E)^{-1}$，所以两个同阶方阵 $A,Y$ 均可逆。再由 $|E^k|\le N_A^k$，

$$
|A^{-1}b|
=\left|\sum_{k\ge0}E^kYb\right|
\le \sum_{k\ge0}N_A^k|Yb|
=(I-N_A)^{-1}|Yb|.
$$

非负比较逆存在，且逐项非负。证毕。

实际消费者不必数值形成 $(I-N_A)^{-1}$。只要严格验证某个非负向量 $E_b$ 满足

$$
|Yb|+N_AE_b\le E_b,
$$

就有 $|A^{-1}b|\le E_b$。另一直接选择是：若 $|Yb|\le\eta w$，则取 $E_b=\eta w/(1-q)$。候选 $Y,w,E_b$ 可以由普通数值过程提出，但上面各个包含关系必须由准确有理或向外舍入计算独立成立；候选本身的来源不是证明。

这些证明用的权和比较范数不是原 native 的 $\sigma$，不能把它们替换进原接受条件。

## 314.4 名义因子与真实 literal 矩阵的区别

在同一名义输入 $\widehat z$ 上，记准确实 literal 函数为

$$
C_0=C(\widehat z),\qquad F_0=F(\widehat z).
$$

原数值程序实际保存的有限字分别记为

$$
\widehat C,\quad \widehat F,\quad
\widehat L_c,\quad \widehat v_c,\quad \widehat s.
$$

这些帽号对象在证明中均作为准确 dyadic 读取，而不是重新执行其来源运算。定义

$$
B=\widehat L_c\widehat L_c^T,\qquad
\Delta C=C_0-\widehat C,\qquad
\Delta F=F_0-\widehat F.
$$

即使 $\widehat C$ 与 $\widehat F$ 的普通计算来源正确，$\Delta C,\Delta F$ 也不能默置为零。它们涵盖 literal 有限求和、除法、平方根及中间形成的数值误差。

若 $\widehat L_c$ 的对角均非零，$B$ 正定。可以选择固定的 $Y=B^{-1}$，通过准确有理三角回代定义它；也可以选择另一个明确保存的候选 $Y$，再按引理 314.1 验证。后者不能只因来自 Cholesky 就跳过 $|I-YC_0|$ 的严格验证。

若要确认与原准确实 Cholesky 程序对应，而不只是线性系统可逆，还需正定性。一个可直接验证的充分条件是：对准确对称的 $C_0$，

$$
H=\widehat L_c^{-1}(C_0-B)\widehat L_c^{-T},
\qquad \|H\|_2<1.
\tag{314.2}
$$

因为 $C_0=\widehat L_c(I+H)\widehat L_c^T$，而 $I+H$ 的最小特征值正，所以 $C_0$ 正定。可用严格的 $\sqrt{\|H\|_1\|H\|_\infty}$ 上界，或对称情形的严格行和上界，支付该条件；普通浮点特征值读数本身不支付它。要在整个验证闭盒上使用 Cholesky 的导数，必须在整个闭盒上验证相应条件。

## 314.5 一次 primal 求解的后验界

按准确字值定义三个缺陷

$$
\widehat R=B-\widehat C,\qquad
\widehat a=\widehat L_c\widehat v_c-\widehat F,\qquad
\widehat b=\widehat L_c^T\widehat s-\widehat v_c.
$$

真实求解残差为 $u=C_0\widehat s-F_0$。直接相乘得到

$$
u=
\widehat a+\widehat L_c\widehat b-\widehat R\,\widehat s
+\Delta C\,\widehat s-\Delta F.
\tag{314.3}
$$

该式包括原因子、forward solve、backsolve 三项缺陷，也包括真实矩阵和右端的形成误差。任何一项都没有被声明为零。

设引理 314.1 对 $A=C_0$ 成立，且 $s_*=C_0^{-1}F_0$。则

$$
|\widehat s-s_*|
\le (I-N_C)^{-1}|Yu|.
\tag{314.4}
$$

**证明。** $C_0(\widehat s-s_*)=u$，直接使用引理。证毕。

消费者可用 (314.3) 的完整右端求严格包围，也可直接包围 $C_0\widehat s-F_0$，取其中已严格证明的较小界。现有日志中的 $\|\widehat R\|,\|\widehat a\|,\|\widehat b\|$ 只是普通数值读数，不能单凭它们等于零或很小，就删去 $\Delta C,\Delta F$，也不能自动得到 (314.4)。

## 314.6 完整方向方程的严格误差界

固定一个完整输入方向 $v$。它可含 $e$、shape 及实际需要的几何参数；不把未实现的几何方向冒成已经处理。记真实 literal 微分

$$
\dot F_0=DF(\widehat z)[v],\qquad
\dot C_0=DC(\widehat z)[v].
$$

准确实求解映射的方向 $\dot s_*$ 满足

$$
C_0\dot s_*=\dot F_0-\dot C_0s_*.
$$

设新收缩实现给出的名义方向字为 $\widehat{\dot s}$，定义

$$
\nu=C_0\widehat{\dot s}
-\bigl(\dot F_0-\dot C_0\widehat s\bigr).
\tag{314.5}
$$

**定理 314.2。** 若 $E_s\ge|\widehat s-s_*|$ 是已经严格成立的逐分量包围，则

$$
C_0(\widehat{\dot s}-\dot s_*)
=\nu-\dot C_0(\widehat s-s_*),
\tag{314.6}
$$

从而

$$
|\widehat{\dot s}-\dot s_*|
\le (I-N_C)^{-1}
\left(|Y\nu|+|Y\dot C_0|E_s\right).
\tag{314.7}
$$

**证明。** 将 (314.5) 与准确方向方程相减，得到 (314.6)；再应用引理 314.1 和逐分量三角不等式。证毕。

式中的 $|Y\nu|$ 与 $|Y\dot C_0|$ 都必须是相应准确量的外包。先把 $Y\dot C_0$ 作普通浮点乘法再取绝对值不构成证明。也不能删去第二项：名义右端实际用了 $\widehat s$，而准确方向方程用了 $s_*$。

为直接对接 R305 收缩程序，记它实际形成的右端字为 $\widehat h$，实际局部偏导与 Gram 矩方向字为 $\widehat{\dot F}$ 和全部 225 项 $\widehat{\dot\beta}$。令 $\mathcal G(\widehat{\dot\beta})$ 表示按原 literal 结构、在准确实算术中形成的矩阵方向，定义

$$
\tau_h=\widehat h-
\bigl[\widehat{\dot F}-\mathcal G(\widehat{\dot\beta})\widehat s\bigr],
\qquad
r_h=\widehat C\widehat{\dot s}-\widehat h.
$$

则准确恒有

$$
\begin{aligned}
\nu={}&r_h+\Delta C\,\widehat{\dot s}+\tau_h
-(\dot F_0-\widehat{\dot F})\\
&+\bigl[\dot C_0-\mathcal G(\widehat{\dot\beta})\bigr]\widehat s.
\end{aligned}
\tag{314.8}
$$

这逐项保留共享局部偏导、有限投影、Gram 收缩、右端相减和两次回代的误差。无需为了这个证明每列再次微分 Cholesky，但必须严格评价真正的 $\dot F_0,\dot C_0$。全部 224 列可共享同一个 $N_C$、固定预条件器和局部偏导外包；每列的 $\nu,E_s$ 修正、方向范围仍须完整存在，不能只读最坏一列就声称全列完成。

## 314.7 原名义逐因子方向的缺陷导数并未消失

R305 已指出，小的缺陷值不控制其导数。此处给出能够直接检查的准确比较式，说明新后验界没有偷用这种推论。

任选在名义点取值为 $\widehat C,\widehat F,\widehat L_c,\widehat v_c,\widehat s$ 的一阶 jet，记其方向为 $\dot C,\dot F,\dot L_c,\dot v_c,\dot s_{\rm old}$。这些可以是原逐因子计算保存的方向字，但本节把它们作为明确给定的代数数据，不称它们为 IEEE roundmap 的导数。定义

$$
\dot R=\dot L_c\widehat L_c^T+\widehat L_c\dot L_c^T-\dot C,
$$

$$
\dot a=\dot L_c\widehat v_c+\widehat L_c\dot v_c-\dot F,\qquad
\dot b=\dot L_c^T\widehat s+\widehat L_c^T\dot s_{\rm old}-\dot v_c.
$$

令

$$
h_0=\dot F-\dot C\widehat s,\qquad
\zeta=\dot a+\dot L_c\widehat b+\widehat L_c\dot b-\dot R\widehat s.
$$

由乘积法则或直接展开，

$$
B\dot s_{\rm old}=h_0+\zeta,\qquad
B(v-\dot s_{\rm old})=(Bv-h_0)-\zeta.
\tag{314.9}
$$

因此，若要比较新方向字与旧方向字，可以严格包围 (314.9) 的全部右端并使用 $B^{-1}$ 的比较界。但只有 $\widehat R,\widehat a,\widehat b$ 的数值不足以包围 $\zeta$；即使三者在一个点全为零，也不能推导其形式方向为零。

这里的字值比较仍不是准确实导数的误差证明。定理 314.2 直接以真正 $DF,DC$ 及真实方程残差建立该误差证明，因而没有把任何未知的 $\dot R,\dot a,\dot b$ 默置为零。两种可认证对象应保留不同标签。

## 314.8 固定有限 root 轨迹的 primal 与方向传播

固定实际选中的成功更新次数 $K$ 和每次接受的 $\alpha_k=2^{-j_k}$。准确实更新为

$$
T_k(e,x)=e-\alpha_k C(e,x)^{-1}F(e,x),\qquad e_0=0.
$$

$x$ 包括本次 field 的外部状态与几何输入。正常返回与 fallback 都使用其实际已经接受的有限前缀；没有接受更新的返回不补造一次 Newton 步。原 root 抛错或全拒而未返回时，不能将它记成成功可微轨迹。

把实际更新字的形成缺陷准确写为

$$
\tau_k=\widehat e_{k+1}-\widehat e_k+\alpha_k\widehat s_k.
$$

在名义当前点对准确 $T_k$ 的局部 primal 缺陷至多为

$$
\eta_k\le|\tau_k|+\alpha_kE_{s,k}.
\tag{314.10}
$$

同理，若方向更新字为 $\widehat d_k$，

$$
\tau'_k=\widehat d_{k+1}-\widehat d_k+\alpha_k\widehat{\dot s}_k,
$$

其相对于 $DT_k$ 作用在同一个名义输入方向的局部缺陷至多为
$|\tau'_k|+\alpha_kE_{\dot s,k}$。实际返回 $L=t+e$ 的值和方向还须计入对应加法形成缺陷及外部 $t$ 的已有误差界。

为了把各步连成严格结论，令 $z=(e,x)$，并把外部输入作为不变分量带入
$\Psi_k(z)=(T_k(e,x),x)$。设某凸闭盒 $X_k$ 同时包含名义状态 $\widehat z_k$ 与准确实固定轨迹状态 $z_k$，且

$$
|\widehat z_k-z_k|\le E_k,\qquad
|D\Psi_k(z)|\le A_k\quad(z\in X_k).
$$

若名义下一状态相对于 $\Psi_k(\widehat z_k)$ 的局部缺陷由 $\eta_k$ 包围，则

$$
E_{k+1}=\eta_k+A_kE_k
\tag{314.11}
$$

是有效包围。证明是局部缺陷与线段上的均值积分相加。

对任意列 $a$，令名义方向为 $\widehat D_{k,a}$，准确固定轨迹方向为 $D_{k,a}$，已有
$|\widehat D_{k,a}-D_{k,a}|\le Z_{k,a}$。若局部方向缺陷为 $\varepsilon_{k,a}$，并在 $X_k$ 上严格包围二阶偏导

$$
\left|\frac{\partial^2\Psi_{k,i}}{\partial z_j\partial z_\ell}\right|
\le H_{k,i j\ell},
$$

则逐分量可取

$$
Z_{k+1,a,i}
=\varepsilon_{k,a,i}+(A_kZ_{k,a})_i
+\sum_{j,\ell}H_{k,i j\ell}E_{k,j}|\widehat D_{k,a,\ell}|.
\tag{314.12}
$$

确实，把方向差拆为局部缺陷、
$D\Psi_k(z_k)(\widehat D_{k,a}-D_{k,a})$、
以及 $[D\Psi_k(\widehat z_k)-D\Psi_k(z_k)]\widehat D_{k,a}$，分别使用上述界即得。若直接用方向区间自动微分在完整闭盒上包围第三项，可避免存储巨大 Hessian 张量；但不能省略状态误差引起的导数变化。

这些结论针对**明确固定的准确实分支表达式**。若还要把它称为带动态停止条件的准确实程序在邻域内的通常导数，必须证明相关邻域上整个控制流不变：包括成功和被拒的候选、原域判断、停止条件、回溯选择、fallback 与必要的 pivot 判断。一个充分方式是在全部实际访问谓词上得到保留原真假值的严格区间裕量。边界相等、遗漏的拒绝候选或未包围的谓词不能由“primal shadow 同字”补证。

这里的“准确实程序”只指将有限表达的算术解释为实运算并保留原分支定义；无论有无分支裕量，本文都不把 IEEE 离散舍入程序当作该光滑映射。

## 314.9 真正有限方程根必须使用实际 $F_e$

原代码在角点形成

$$
\ell_n=L_0+\sum_{j=1}^{M}L_jc_{nj},
\qquad
F_i(e,x)=e_i+\frac1N\sum_{n=0}^{N-1}q_n\,c_{ni}.
$$

应严格区分输入系数与投影系数。定义

$$
v_{n0}=1,\qquad v_{nj}=c_{nj}\quad(1\le j\le M).
$$

那么 $\partial\ell_n/\partial e_j=v_{nj}$。在固定外部输入 $x$ 时，$P_n,P_{t,n}$ 不依赖 $e$；R305 的 $q$ 也不依赖 $U$。因此准确地

$$
(F_e)_{ij}
=\delta_{ij}+\frac1N\sum_n
q_{\ell,n}\,c_{ni}v_{nj}.
\tag{314.13}
$$

只有另行核实实际 $c_{n0}=1$，才可把最后的 $v_{n0}$ 改写成 $c_{n0}$。原 root 源码直接使用 $L_0$，不能凭 cosine 表的名称偷用这个恒等式。

式 (314.13) 来自真实有限 $F$ 的微分，不是原 Gram $C$ 的重新命名。可以借用 $C$ 构造候选预条件器，但仍须支付

$$
I-YF_e=(I-YC)-Y(F_e-C)
\tag{314.14}
$$

中的真实差异；$C$ 易逆本身不证明 $F_e$ 易逆。

**定理 314.3。** 固定真实外部输入 $x_0$，设
$X=\{e:|e-\bar e|\le r\}$，其中 $r$ 逐分量正，$F$ 在包含 $X$ 的开集上连续可微。若存在固定方阵 $Y$、非负矩阵 $N_F$、正向量 $w$ 及 $q<1$，严格满足

$$
|I-YF_e(e,x_0)|\le N_F\quad(e\in X),
$$

$$
|YF(\bar e,x_0)|+N_Fr\le r,\qquad N_Fw\le qw,
\tag{314.15}
$$

则 $F(e,x_0)=0$ 在 $X$ 中有唯一解 $e_*$，并且

$$
|e_*-\bar e|
\le (I-N_F)^{-1}|YF(\bar e,x_0)|
\le r.
\tag{314.16}
$$

**证明。** 令 $G(e)=e-YF(e,x_0)$。均值积分和 (314.15) 给出 $G(X)\subseteq X$；在 $\|\cdot\|_w$ 中，它以常数至多 $q<1$ 收缩。闭盒完备，Banach 定理给出唯一不动点。引理 314.1 在盒内任一点适用，故 $Y$ 可逆，不动点恰是 $F=0$。将不动点等式与中心相减，反复使用非负比较矩阵即得第一界；由自映射条件与比较逆的非负性得第二界。唯一性也同时适用于盒内其他零点。证毕。

该结论仅证明这个有限 literal 方程在明确盒中的局部根；不证明原连续 ODE、无限尾、物理场或 native 的全局存在性。原正常 root 停止或 fallback 也不能替代 (314.15)。

## 314.10 隐式根方向的后验界

在定理 314.3 的条件下，$F_e(e_*,x_0)$ 可逆。若 $F$ 在 $(e_*,x_0)$ 的开邻域连续可微，则隐函数定理给出局部根分支。对外部方向 $v$，真正的隐式根方向 $d_*$ 满足

$$
F_e(e_*,x_0)d_*+F_x(e_*,x_0)v=0.
$$

设候选方向为 $\widehat d$。若对整个根盒 $X$ 严格包围

$$
\left|Y\bigl[F_e(e,x_0)\widehat d+F_x(e,x_0)v\bigr]\right|
\le b_d\quad(e\in X),
$$

则

$$
|\widehat d-d_*|\le(I-N_F)^{-1}b_d.
\tag{314.17}
$$

证明是在 $e_*$ 处使用引理 314.1。若只在盒中心评价该残差，必须另加实际二阶偏导与 (314.16) 根误差产生的变化项，不能用中心读数代替整个根盒包围。返回 $L=t+e$ 时，再加真实 $dt$ 及其已有误差。

有限次 root 轨迹方向与这个隐式方向是不同对象。只有分别取得有效界或直接包围它们的差，才可以定量联系；原 root 停止阈值本身不支付两者的导数差。

## 314.11 完整 226 态、RK、均值和端口的传播

R305 的完整 field 包含 $Q_j,\Pi_j,\overline z,\overline a$。两个 mean 不反馈到 shape/root，并不允许删去它们的值或方向。原 $r,r',w,w_2,E,\mu$、物理基底 $t$ 及其所有实际方向，都按真实表达链式传播。一个固定几何的 224 状态列包不自动包含几何参数响应。

以一个固定步长 $h$ 的完整准确实 RK4 为例。令四个 field 值为 $a,b,c,d$，中间状态为
$y_b=y_0+ha/2$、$y_c=y_0+hb/2$、$y_d=y_0+hc$。保存的名义字定义准确形成缺陷

$$
\xi_b=\widehat y_b-(\widehat y_0+h\widehat a/2),\qquad
\xi_c=\widehat y_c-(\widehat y_0+h\widehat b/2),
$$

$$
\xi_d=\widehat y_d-(\widehat y_0+h\widehat c),\qquad
\xi_+=\widehat y_+-
\left[\widehat y_0+\frac h6
(\widehat a+2\widehat b+2\widehat c+\widehat d)\right].
$$

这些是实际名义字与准确目标表达的差，不要求程序真的采用上述括号执行；原实际括号产生的数值误差正包含在缺陷中。

设每个完整 field 在相应合法闭盒上都有局部评价缺陷 $\eta$ 及严格 Jacobian 绝对值上界 $A$。则递推

$$
E_a\le\eta_a+A_aE_0,\qquad
E_{y_b}\le|\xi_b|+E_0+\frac{|h|}{2}E_a,
$$

$$
E_b\le\eta_b+A_bE_{y_b},\qquad
E_{y_c}\le|\xi_c|+E_0+\frac{|h|}{2}E_b,
$$

$$
E_c\le\eta_c+A_cE_{y_c},\qquad
E_{y_d}\le|\xi_d|+E_0+|h|E_c,\qquad
E_d\le\eta_d+A_dE_{y_d},
$$

$$
E_+\le|\xi_+|+E_0+
\frac{|h|}{6}(E_a+2E_b+2E_c+E_d)
\tag{314.18}
$$

给出完整 226 态的后验包围。每条都是三角不等式与闭盒上的均值积分；所有 field 缺陷必须已包含其内部 root、有限投影和 RHS 形成误差。全部原 atomic 步按真实顺序串接即可。

方向使用 (314.12) 或等价的完整区间链式法则；还须加入每次方向乘加的准确形成缺陷。若 $h$、采样位置或几何参数变化，把它们带为扩展输入坐标，对原表达求导，不能删去 $dh$ 项。分段拓扑改变另需独立责任，固定拓扑公式不证明拓扑切换处可微。

端口原映射为 $Q\mapsto Q,\Pi\mapsto\Pi/\zeta$，一般方向为

$$
d(\Pi/\zeta)=d\Pi/\zeta-\Pi\,d\zeta/\zeta^2.
$$

只有固定端口任务才能取 $d\zeta=0$。值与方向都须保实际除法形成误差并在盒上排除 $\zeta=0$。

全部 224 请求列、完整 226 输出、post-port 的 224 输出及两个 mean 行齐全，才是本任务的完整 stage 责任。若输入只请求了 224 shape 列，不能据此声称另两个 mean 输入列或全部几何列也已经数值执行。

## 314.12 全部原行与原归一化范数

对原同一状态与参数，cut/stage/far 分别沿真实定义装配。stage $n$ 的残差为
$\Phi_n(y_{n+1})-y_n$，其误差由完整 stage 输出误差、node $n$ 误差及实际残差形成缺陷相加。cut 的目标与 far 的 $G$ 也必须沿真实来源；当它们变化时不能删去目标方向或 $(dG)Q$。固定输入任务可明确将相应源误差设为零，但不能换用旧场来源。

令完整 129248 行准确目标残差为 $r$，名义残差字为 $\widehat r$，已证逐分量误差 $|r-\widehat r|\le E_r$。原固定归一化尺度 $\sigma_i$ 是严格正的实际输入字。则

$$
\left|
\max_i\frac{|r_i|}{\sigma_i}
-\max_i\frac{|\widehat r_i|}{\sigma_i}
\right|
\le
\max_i\frac{E_{r,i}}{\sigma_i}.
\tag{314.19}
$$

**证明。** 每行由反三角不等式得到
$||r_i|-|\widehat r_i||/\sigma_i\le E_{r,i}/\sigma_i$；有限最大值函数在最大范数下为 1-Lipschitz，遂得。证毕。

右端必须严格向外形成。左边第二个最大值是名义字在准确实算术中的商与最大值，不能未经说明当作已经舍入的原 norm 标量；若要比较那个原标量，还须保留其实际除法/归约形成误差。此区别不改变原 norm 的实现或接受门。

同样的完整行包围可以作用于原线性 action；本定理不因此给出完整 shooting 系统的根、112 边界响应、338 endpoint 或原物理审计。那些任务的全部来源、行列和验收责任须由其各自实际消费者支付。

## 314.13 可执行验证的最小完整合同

数学结论可以由独立 Actions 消费者执行，但当前普通最大值日志不足以直接生成上述证书。最小接线应在原同 job 现场仍存在时读取，或从真实来源按声明顺序重做；不能把已经删除的 raw 的 SHA 当作数据恢复。

| 层 | 必须有的真实输入 | 可声明的结果 |
|---|---|---|
| 一次 solve | 完整 literal 包、当前输入、原 $C,F,L_c,v_c,s$ 字及合法域 | 真实准确实 $C^{-1}F$ 的后验值界 |
| 一列收缩方向 | 该列完整输入方向、实际方向字/RHS、全部 225 Gram 方向；真实 $DF,DC$ 外包 | (314.7) 的准确实 solve-map 方向界 |
| 固定 root trace | 所有实际接受更新与返回类型；每步完整状态/方向/域/误差包围 | 明确固定的准确实有限轨迹包围 |
| 动态准确实分支 | 另有全部访问谓词及严格稳定裕量 | 该邻域中的准确实程序分支导数 |
| 真正有限根 | 实际 $F,F_e$ 的完整根盒包围与 (314.15) | 该盒内唯一有限根及可选 (314.17) |
| 完整 stage | 全 atomic 步、226 态、224 请求列、两个 mean、端口 | 真实请求范围的 stage 值/方向外包 |
| 完整残差 | 原全部 cut/stage/far、原 target/G/正 $\sigma$ | 129248 行及 (314.19) 的范数误差界 |

执行要求如下：

1. 所有原件、输入状态和方向、literal 表、数值源及验证器均绑定完整 bytes/SHA 与实际请求范围。解码原字不依赖短十进制；不得把另一 policy、另一 state 或旧 $J$ 贴到当前记录。
2. 精确 dyadic 的有限乘加缺陷可用任意精度整数/有理数求值；真正平方根、商、偏导及区间传播必须采用有明确包含语义的向外算术。普通 binary128 重算缺陷仅是新读数，不自动成为外包。
3. 候选预条件器、缩放与误差向量可以普通数值提出；最终 $Nw\le qw$、自映射、域、SPD 和残差包含须严格成立。任何未决项保留未决，不能从 shadow mismatch 为零推导误差为零。
4. 保全部 113 root 行、225 Gram 项、224 请求列和 226 输出。允许流式累计、共享局部区间偏导、逐块列处理；未访问后缀、未证盒及失败原因必须明确，不能用部分最大值冒完整范围。
5. 增加验证精度、缩小验证盒或改善固定预条件器只改变证书资源。它们不修改原 $F/C$、root policy、原 nonlinear 回溯、native 阈值或原最终门。
6. 上述各层分别记录完成与证书成立状态。尤其“验证程序受控结束”“原 primal 重放完成”“方向证书成立”“有限根已证”“原 native 已接受”必须保持不同字段。
7. 原 raw 可在同 job 临时使用，按规则清理；公开保留源、参数、真实 run/source、必要输入和输出 SHA、明确范围及紧凑证明结果，不重复上传可重算数组。

这是一个可直接据公式落实的验证接口，不是给现有 140 追加前置验收门。没有真实外包数据时，本文只支付条件定理，不支付未来某次运行的数值结论。

## 314.14 结论与剩余责任

已证明：在明确可验证的域、逆界及外包条件下，名义 Gram/Cholesky/两次回代缺陷给出严格值界；完整方向残差连同名义 primal 解误差给出严格方向界；固定有限 root/RK/端口链可保全部 226 态与请求列；实际 $F_e$ 的独立收缩条件则给出真正有限根与隐式方向。原名义缺陷导数没有被假设为零。

这些充分条件可能因条件数、区间过宽、分支不稳定、根盒不自映射或资源不足而未取得。本文不据此断言原问题无根、原方向无用或普遍浮点误差底线，也不预测 140 的速度、数值证书或最终接受。原 140 源与运行身份保持独立。

## 来源与源码边界

- [R283：原 literal 表与成功有限 root 轨迹的逐步微分](R283-finite-root-trace-differentiation-with-literal-tables.md)。
- [R302：共享成功 root 记录及完整边界响应](R302-shared-finite-root-traces-and-complete-boundary-response.md)。
- [R305：准确实 Gram 收缩与名义分解缺陷](R305-literal-gram-root-contraction-and-nominal-factor-defects.md)，已发布证明 SHA-256：26ebd720353f32114ef3eee62e9c98a3bed615f00ef372a3227e3a132aa13d8c。
- 原 primal：geometry_20261115_native_primal128.cpp，23890 B，SHA-256：1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d。314.9 的零模输入/投影区分直接依该源的 root_evaluate。
- 已发表 R305 数值组件：geometry_20261115_native_operator_trace128.hpp（950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0）、geometry_20261115_native_operator_stage128.cpp（86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926）、geometry_20261115_native_operator_final128.py（a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef）。它们提供实际名义读数的来源，不因本证明而自动具有区间证书。
