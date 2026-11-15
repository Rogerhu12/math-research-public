# R305：原 literal Gram 根迭代的共享方向算子与名义分解缺陷

作者：GPT-6 Astra Pro（exact_refinement）  
日期：2026-11-15  
类型：已证明（固定成功分支的准确实表达；不包含有限字运算误差界）

## 305.1 结论与对象

对 R283 的有限 root 程序，固定实际选出的成功迭代次数和每次接受的回溯指数。其真实矩阵 $C$ 来自独立的 literal `gram` 表；不需要、也不假设 $C=F_e$。在每个准确实 Cholesky 分解存在的迭代点，原 Cholesky 与两次三角回代的完整微分，等价于

$$
ds=C^{-1}(dF-(dC)s),\qquad s=C^{-1}F.
$$

而 $(dC)s$ 可直接由全部 $2M+1$ 个 Gram 矩导数收缩得到，不必为每列形成完整 $dC$ 或微分整个 Cholesky 因子。角点的有限标量表达可先计算共享局部偏导，再作用于所有方向。全部 literal cosine、sine、Gram 表及其有限求和仍保留。

**以上等价属于准确实算术。** 已舍入的名义 $C,L,t,s$ 一般不满足分解和两次回代的准确等式，不能把其缺陷或缺陷的导数默认为零。新 binary128 算子是同一准确实对象的另一数值实现；本证明不支付它与 R283 原逐 $dL$ 运算图的逐字相等、方向误差界或原 native 验收。

本文使用 R283 的 literal 表与完整 root/RK 定义，R302 的原成功 root 记录及全列责任。不引入新 root 阈值、截秩、normal matrix、不同物理场或参数接受门。

## 305.2 有限角点表达，保留独立常数

设 $M\ge1$、$J=M+1$，有限角点数为 $N$。记原包中的常数为 $c_{nj}$、$s_{nj}$、$\gamma_{nk}$、$m_j$、$\sigma_2$、$\sigma_{12}$。其中 $c,s,\gamma$ 分别来自原 cosine、sine、Gram 表；$\sigma_2,\sigma_{12}$ 是包中保存的平方根字值。证明把它们作为各自固定实常数，不用三角恒等式或精确根号关系替换它们。

一个 field 的几何字为 $(r,r',w,w_2,E)$，cell 参数为 $\mu$，状态包含 $M$ 个 $Q_j$、$M$ 个 $\Pi_j$ 和两个均值坐标。$w_2,E$ 是各自独立的输入坐标；若调用者知道它们来自某个几何函数，其方向必须通过那个函数的实际链式法则另行给出。

沿用原程序的有限代数：

$$
p_j=-\frac{m_jr^3Q_j}{\sigma_2w},\qquad
t_0=0,\qquad
t_j=\frac{o\sigma_{12}\mu}{\sigma_2r^4w_2}\Pi_j\quad(1\le j\le M),
\qquad L=t+e.
$$

这里 $o\in\{-1,1\}$，幂的实际数值实现仍由源程序规定；准确实证明不依赖这些等价乘法次序。角点量为

$$
P_n=\sum_{j=1}^M p_js_{nj},\quad
P_{t,n}=\sum_{j=1}^Mm_jp_jc_{nj},\quad
\ell_n=L_0+\sum_{j=1}^ML_jc_{nj},
$$

$$
U_n=\sum_{j=1}^M\bigl[-m_jL_j+(m_j^2-1)p_j\bigr]s_{nj},
\qquad K_n=\ell_n-P_{t,n}.
$$

为简化一角点公式，暂去下标 $n$。定义

$$
T=2K+K^2+EP^2,\quad u=w_2T,\quad
D=1-u,\quad S=1-w_2P^2,\quad A=1+\ell+w_2P_t,\quad d=\sqrt D,
$$

$$
f_c=\frac{u(2+d)}{2d(1+d)^2},\qquad
g_c=\frac{w_2\,[P^2+ST/(1+d)]}{Sd},
$$

$$
q=\frac{K^2+EP^2}{2}+KP_t+Tf_c+(1+K)P_tg_c,
$$

$$
a=\ell+w_2P_t,\qquad
d_m=\frac{u\,[d+1/(1+d)]}{Dd},\qquad
\rho=a+(1+a)d_m,
$$

$$
\varphi=U\,\frac{K+u/(1+d)+w_2P^2d}{Sd}.
$$

三式分别是原 $F$ 的角点非线性项、原 $C$ 的 Gram 角点项、原 RHS 的 flux 角点项。它们不是互相替换的定义。

在原合法分支上，各除数非零且 $D>0$。因此 $q,\rho,\varphi$ 对

$$
z=(P,P_t,\ell,U,w_2,E)
$$

具有通常实微分。$q,\rho$ 对 $U$ 的偏导为零，但不因此删去 $\varphi$ 的 $U$ 项。

**共享局部偏导引理。** 对任意有限组方向 $dz^{(a)}$，先计算六个坐标方向的偏导，再作

$$
dq^{(a)}=\sum_{k=1}^6q_{z_k}\,dz_k^{(a)},\quad
d\rho^{(a)}=\sum_{k=1}^6\rho_{z_k}\,dz_k^{(a)},\quad
d\varphi^{(a)}=\sum_{k=1}^6\varphi_{z_k}\,dz_k^{(a)},
$$

与逐方向完整链式微分一致。

证明：上述函数是有限次加减乘除及正平方根的复合；这些基本函数在所述域可微。逐层应用链式法则，所得微分是关于 $dz$ 的线性映射。线性映射由六个坐标基的像唯一确定。此论证没有近似、没有丢掉某个参数方向。它也不说明有限字重新组合这些偏导会与原双数运算逐字相同。证毕。

## 305.3 $F$ 与 $C$ 的两套完整投影

原 residual 定义为

$$
F_i=e_i+\frac1N\sum_{n=0}^{N-1}q_nc_{ni},\qquad 0\le i\le M.
$$

其完整微分是

$$
dF_i=de_i+\frac1N\sum_n dq_n c_{ni}.
$$

另一套独立 Gram 矩为

$$
\beta_k=\frac1N\sum_n\rho_n\gamma_{nk},\qquad 0\le k\le2M.
$$

源码 `root_matrix` 的准确矩阵条目为

$$
C_{00}=1+\beta_0,\qquad
C_{i0}=C_{0i}=\sigma_2\beta_i\quad(1\le i\le M),
$$

$$
C_{ij}=\delta_{ij}+\beta_{|i-j|}+\beta_{i+j}
\qquad(1\le i,j\le M).
$$

所以

$$
d\beta_k=\frac1N\sum_n d\rho_n\gamma_{nk}.
$$

无论 $c$ 与 $\gamma$ 的实际字值之间是否具有某个近似三角关系，这些式子都成立。证明和新实现均不以 cosine 外积重建 $C$，也不由 $F$ 的偏导定义 $C$。

## 305.4 完整 Gram 收缩恒等式

固定任意向量 $s\in\mathbb R^{M+1}$。定义线性映射 $\mathcal T_s:\mathbb R^{2M+1}\to\mathbb R^{M+1}$：

$$
(\mathcal T_s b)_0=b_0s_0+\sum_{j=1}^M\sigma_2b_js_j,
$$

$$
(\mathcal T_s b)_i=\sigma_2b_is_0+
\sum_{j=1}^M(b_{|i-j|}+b_{i+j})s_j,
\qquad1\le i\le M.
$$

则有准确恒等式

$$
(dC)s=\mathcal T_s(d\beta).
$$

证明：把 305.3 的全部矩阵条目逐项微分，再按定义乘以 $s$。第零行使用 $dC_{00}=d\beta_0$ 和 $dC_{0j}=\sigma_2d\beta_j$；其余行使用首列及所有 $j\ge1$ 条目，恰得到两式。对角 $i=j$ 的 $d\beta_0+d\beta_{2i}$、首行与首列的 $\sigma_2$ 都保留。没有将大下标项截去；最大 $i+j$ 正好为 $2M$。证毕。

这允许程序为每个方向只形成 $2M+1$ 个 $d\beta$ 和 $M+1$ 个 action 分量。它不是降低矩阵维数或删掉高模。

## 305.5 成功 Newton 更新的准确实导数

在一次实际选中的 root 更新上，假设准确实矩阵 $C$ 正定。令 $L_c$ 为原顺序 Cholesky 程序在准确实算术中的输出，令两次回代为

$$
L_cv_c=F,\qquad L_c^Ts=v_c.
$$

正定性给出 $C=L_cL_c^T$ 及非零正对角，故所有这些有限表达在该点可微，且 $Cs=F$。

对任意状态和几何方向微分：

$$
(dC)s+C\,ds=dF.
$$

$C$ 可逆，唯一得到

$$
\boxed{\quad ds=C^{-1}\bigl[dF-\mathcal T_s(d\beta)\bigr].\quad}
$$

另一方面，逐个微分原 Cholesky 标量循环和两次三角回代，得到的 $dL_c,dv_c,ds$ 也必须满足上式，因为这是它们准确等式的乘积法则；右端方程的唯一性说明两种微分相同。

反向也可以逐式验证：$dC=dL_cL_c^T+L_cdL_c^T$，
$dF=dL_c\,v_c+L_c\,dv_c$，$dv_c=dL_c^Ts+L_c^Tds$。代入并消去 $dv_c,v_c$ 即得上述方程。这里使用的是 $C$ 的真实微分，不是 $F_e$。

若该次接受指数为 $k$，$\alpha=2^{-k}$ 固定，则

$$
e^+=e-\alpha s,\qquad de^+=de-\alpha ds.
$$

这里 $v_c$ 专指三角回代中间向量，与305.2的物理基底向量 $t$ 区分。初始 $e=0,de=0$。按真实接受更新的有限次序归纳，即得完整成功 root 分支的返回方向 $dL=dt+de$。没有更新的正常返回或原 fallback 直接使用当前 $dt+de$；全拒而未返回的 root 不能伪造方向。

若当点具有保证整个程序分支在邻域不变的严格不等式，此方向也是该局部分支程序的通常导数。没有这种分支稳定性证明时，结论只针对明确固定的成功分支实表达；不自动变成带动态停止条件的程序的导数。

## 305.6 已舍入名义字：不得遗忘缺陷导数

本节不对 IEEE roundmap 求导。只考察任意光滑矩阵、向量表达 $C,L_c,v_c,s,F$，它们在某点可取保存的名义字值。定义三个可能非零的缺陷

$$
R=L_cL_c^T-C,\qquad a=L_cv_c-F,\qquad b=L_c^Ts-v_c.
$$

直接相乘得

$$
C s-F=a+L_cb-Rs.
$$

其完整微分是

$$
C\,ds=dF-(dC)s+da+(dL_c)b+L_c\,db-(dR)s-R\,ds.
$$

等价地，

$$
(C+R)ds=dF-(dC)s+da+(dL_c)b+L_cdb-(dR)s.
$$

证明只用乘积法则，因此没有可删的隐含项。准确实 Cholesky 和回代在邻域恒满足 $R=a=b=0$ 时，它们的导数亦为零，才退化为 305.5。

**一个点的缺陷小，甚至该点恰为零，都不蕴含其导数小或为零。** 例如标量函数 $R(x)=\varepsilon\sin(x/\varepsilon^2)$ 在 $x=0$ 的值为零，而导数为 $1/\varepsilon$。因此原保存值的 $\|R\|,\|a\|,\|b\|$ 不能单独替代方向误差证明。

新实现用记录的名义 $L_c$ 对 $dF-\mathcal T_s(d\beta)$ 作两次数值回代，是准确实公式的数值评价。它没有逐步评价旧运算图的 $dL_c$，故不得把上述 $dR,da,db$ 的影响称为已经控制。记录

$$
L_cL_c^T-C,\quad L_cv_c-F,\quad L_c^Ts-v_c,\quad Cs-F,
\quad C\,ds_{\rm new}-[dF-\mathcal T_s(d\beta)]
$$

有助于判读，但这些有限数值残差也不是方向误差的区间上界。

可在明确指定的列上另外执行 R283 原逐 $dL$ 链，与新方向在同一实际 tape、同一输入方向下比较；该比较应保原差异，不作为原 native 的新门。局部同 field 比较不等于独立传播两个完整 stage 后的比较。

## 305.7 全部几何方向、完整 226 态及端口

输入方向必须包含所选任务实际变化的 $Q,\Pi,r,r',w,w_2,E,\mu$。例如

$$
dp_j=d\!\left(-\frac{m_jr^3Q_j}{\sigma_2w}\right),\qquad
dt_j=d\!\left(\frac{o\sigma_{12}\mu\Pi_j}{\sigma_2r^4w_2}\right)
$$

按其原式求导；之后 $dP,dP_t,d\ell,dU$ 使用 305.2 的全部有限表。声明几何字方向为零只适用于固定几何的状态列，不能据此声称完成几何参数响应。

完整 RHS 为

$$
Q'_j=\frac{r'}r\left[(m_j^2-4)Q_j+\frac{\sigma_2wL_j}{r^3}\right],
$$

$$
\Pi'_j=4\frac{r'}r\Pi_j+
\frac{o\sigma_2r^3r'w_2}{\sigma_{12}\mu}m_j
\left[-m_jL_j+(m_j^2-1)p_j+
\frac1N\sum_n\varphi_ns_{nj}\right],
$$

$$
\overline z'=r'wL_0,\qquad \overline a'=r'w.
$$

将共享偏导给出的 $d\varphi$ 与 $dL$ 代入，并对全部外部系数使用乘积/商法则，即是完整 226 态的 RHS 方向。两个均值方向保留，但原 RHS 中它们不反馈到 shape/root；不是以删去均值来缩小状态。

固定原 atomic RK 分段拓扑后，四个实际 primal field 仍按原括号依次形成。四级方向按同一 RK 表达链式传播；若步长 $h$ 变化，每一级的 $dh$ 项也必须包括。原 stage 从 node $n+1$ 入、向 node $n$ 出，不能反向标记。

端口映射为 $Q\mapsto Q$、$\Pi\mapsto\Pi/\zeta$，其一般方向为

$$
d(\Pi/\zeta)=d\Pi/\zeta-\Pi\,d\zeta/\zeta^2.
$$

固定端口列可取 $d\zeta=0$。几何变化导致分段拓扑或采样点变更时，本文固定分支的声明本身不支付拓扑切换处的可微性。

## 305.8 完整原方程和本实现边界

576 段、577 节点的状态列完成后，原 cut/stage/far 线性行仍是

$$
dQ_0-dt_{\rm cut},\qquad
T_n\,dx_{n+1}-dx_n,\qquad
d\Pi_{576}-G\,dQ_{576}-(dG)Q_{576}.
$$

全部 224 列、两个均值行和端口必须齐全，才可称完整 stage-map；部分范围的未访问列不能当零列。原 $\sigma$、原 129248 行和原非线性接受阈值不因本代数恒等式改变。

配套独立源草稿是 `geometry_20261115_native_operator_trace128.hpp` 与 `_stage128.cpp`；其正式源码接口及实际运行另行登记，不作为本证明的前置条件。它保持原 `capture_root`/primal/RK/table 来源，用新的局部偏导与 Gram 收缩数值路径；保存每个完成 stage 的完整 primal、226×columns、post-port 224×columns、两个 mean 行和原 residual。其 stage CLI 只执行固定几何状态列；一般几何/RK-step/port 方向另由显式接口接入，不冒作已执行结果。

这两源不修改 request137 或已发表七组件，也不产生 native/fullDN 接受。完整 112 边界响应、338 endpoint 读出、物理审计、同场后继协议仍必须由实际来源正确的消费者支付；不能把新 schema 偷换成旧组件的已通过标签。

## 305.9 资源与可信度

原实现对每个方向重复角点 value shadow 和逐 Cholesky 微分。新实现按每个实际 root 迭代共享局部偏导，并将每列的 Cholesky 微分改成一个结构化 action 和两回代。这是操作结构的减少，不是实测加速证明。完整有限角点投影仍含所有 $N,M$ 与方向列；高精度软算术、完整名义因子缺陷读回、可选参考列和 root/primal 本身都仍消耗时间。

actual122 两 policy 都仅得到墙钟部分范围，不能用其 counts 猜未保存的 stage 索引；也不能从共享 primal 推出 576×224 在一个 Actions job 内必能完成。所有后续实际运行必须保全局截止、完整已完成范围、未访问后缀和原短读回。

本文没有任何新数值运行、方向误差界、连续 ODE 导数证明、同一精确场证书或原 native 最终接受结论。已证明的是有限实表达的完整等价以及名义分解缺陷不能被忽略的准确恒等式。

## 来源

- [R283：原 literal 表与成功有限 root 轨迹的逐步微分](R283-finite-root-trace-differentiation-with-literal-tables.md)。
- [R302：共享成功 root 记录及完整边界响应](R302-shared-finite-root-traces-and-complete-boundary-response.md)。
- [R303：actual122 的部分有限 root 方向与受控停止](R303-actual122-partial-finite-root-directions-and-controlled-stop.md)。
- 原 primal：`geometry_20261115_native_primal128.cpp`，SHA-256 `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d`。
- 原共享记录：`geometry_20261115_native_shared_trace128.hpp`，SHA-256 `bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b`。
