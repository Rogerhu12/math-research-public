# R718　正定线性流支撑给出的整像距离下界与握持见证

2026-11-27，geometry，AI 辅助。**状态：新的条件性几何推论，已作完整纸面推导和实际源公式核对；没有新增科学运行，没有尚未返回的场、支撑、直径或握持比例结论。**

本文消费 [R650](R650-positive-definite-flow-support-reach.md) 已证明的完整闭球面单层正定流图，不重证它的 reach 定理。新增的是：从同一完整正支撑构造一个全空间 Lipschitz 屏障，直接给见证点到**整个闭面像**的距离下界。它可以与 [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 的完整目标盒距离下界取最大值。固定帽、上下片和标记始终属于目标整像。

已定向核读 R650 全文及其三个附录、R248 §6、R629、R645、R652、R717；这些条目分别给 reach、全相位像公式、帽替换、旧具体场的盒距离、旧开放前缀支撑、Fejér 图与完整直径接口，没有给出本文的指数流距离屏障。这里不迁用它们的旧场数值。

## 1. 完整几何对象与结论

设 \(F:\mathbb S^2\to\mathbb R^3\) 为 \(C^2\) 浸入，\(n\) 为连续全局单位法向。固定同一个中心 \(c\in\mathbb R^3\) 和实对称正定矩阵 \(A\)，记
\[
m=\lambda_{\min}(A)>0,\qquad L=\lambda_{\max}(A).
\]
假设**完整参数球面**满足
\[
\bigl(A(F-c)\bigr)\cdot n\ge \sigma>0. \tag{1}
\]
帽、标记、接缝和全部活动片都在这个量词之内。未闭合的带边像或 core-only 支撑不能代替 (1)。

R650 §2–3 在零偏移处已经证明：\(F\) 是嵌入，而且每条非零完整流轨道
\[
\Phi_t(x)=c+e^{tA}(x-c)
\]
与 \(S=F(\mathbb S^2)\) 恰交一次。对这一结论不需要另一个数值曲率上界；R650 的 reach 结论另用曲率，本文没有省略它。

每个 \(x\ne c\) 因此唯一写成
\[
x=\Phi_{T(x)}(y),\qquad y\in S. \tag{2}
\]
第 2 节证明 \(T=0\) 恰在 \(S\) 上，\(T>0\) 为整个外域，\(T<0\) 加上 \(c\) 为含中心的有界内域。

**定理。** 定义
\[
W(x)=
\begin{cases}
\bigl(e^{mT(x)}-1\bigr)/m,&T(x)>0,\\
0,&T(x)\le0,
\end{cases}
\qquad W(c)=0. \tag{3}
\]
则 \(W\) 在整个欧氏空间上为 \(1/\sigma\)-Lipschitz 函数，且对每个 \(x\in\mathbb R^3\)
\[
\boxed{\quad \operatorname{dist}(x,S)\ge \sigma W(x).\quad} \tag{4}
\]
特别地，对任意真实边界点 \(p\in S\) 和任意 \(s\ge0\)，
\[
\boxed{\quad
\operatorname{dist}(\Phi_s(p),S)
\ge {\sigma\over m}\bigl(e^{ms}-1\bigr).
\quad} \tag{5}
\]
这给欧氏距离，不把流时间、椭球半径或法向距离互相等同。

## 2. 中心、内域与外向性

为明确 (2) 的全局意义，沿用 R650 的准确全局坐标
\[
\Psi(q,t)=c+e^{tA}q,\qquad
(q,t)\in\mathbb S^2\times\mathbb R.
\]
R650 已证这是到 \(\mathbb R^3\setminus\{c\}\) 的微分同胚，且 \(\pi_A\circ F\) 为单层覆盖。因此存在 \(C^2\) 函数 \(r:\mathbb S^2\to\mathbb R\)，使
\[
S=\{\Psi(q,r(q)):q\in\mathbb S^2\}.
\]
\(C^1\) 已足够完成下文。若 \(x=\Psi(q,t)\)，则
\[
T(x)=t-r(q). \tag{6}
\]

因球面紧致，\(r\) 有有限上下界 \(a\le r(q)\le b\)。集合
\[
\Omega=\{c\}\cup\{\Psi(q,t):t<r(q)\}
\]
在原点平移后的某个球邻域内包含全部点：例如 \(t<a-1\) 的整段流内域包含以 \(c\) 为中心的非退化椭球。它也有界，因为 \(t\le b\) 时
\[
|\Psi(q,t)-c|\le \max_{|q|=1}|e^{bA}q|.
\]
这里用了每条流上欧氏范数严格随 \(t\) 增大，而不是假设 \(\Omega\) 凸。

\(\Omega\setminus\{c\}\) 与集合 \(\{\Psi(q,t):t>r(q)\}\) 各自连通，后者无界；加回位于其内部的 \(c\) 不改变前者的连通性。两集合连同 \(S\) 穷尽全空间，且 \(\partial\Omega=S\)。所以 \(\Omega\) 正是有界内域，\(T>0\) 正是无界外域。这同时证明 \(c\) 在内域，不能只把它当作可任取的坐标原点。

在 \(y\in S\)，\(T\) 沿所有切方向的导数为零，且
\[
T(\Phi_s(y))=s,\qquad
\nabla T(y)\cdot A(y-c)=1.
\]
故
\[
\nabla T(y)={n(y)\over A(y-c)\cdot n(y)}. \tag{7}
\]
分母正，\(\nabla T\) 指向 \(T>0\) 的一侧。因此 (1) 中的连续法向恰是有界内域的外法向；这里没有先假定错误的取向，再从它推出中心在内。

## 3. 梯度恒等式与全空间 Lipschitz 性

流时间满足
\[
T(\Phi_s(x))=T(x)+s.
\]
对 \(x\) 微分，并用 \(A=A^T\)，得到
\[
\nabla T(\Phi_s(y))
=e^{-sA}\nabla T(y)
={e^{-sA}n(y)\over A(y-c)\cdot n(y)}. \tag{8}
\]
当 \(s\ge0\) 时
\[
\|e^{-sA}\|_{\rm op}=e^{-ms},
\]
故外域上
\[
|\nabla T(x)|\le {e^{-mT(x)}\over\sigma},\qquad
|\nabla W(x)|=e^{mT(x)}|\nabla T(x)|\le {1\over\sigma}. \tag{9}
\]

内域的 \(W\) 恒为零；在边界两侧它连续，并且是局部 \(C^1\) 函数的非负部分的光滑函数组合，因此局部 Lipschitz。\(c\) 有整个内域邻域，故在 \(c\) 附近也恒为零。于是 \(W\) 在全空间处处局部 Lipschitz。

对任意两点之间的闭线段，紧性使其限制绝对连续。在位于外域的开子区间上，(9) 给沿线段的导数绝对值不超过线段速度除以 \(\sigma\)；在内域上导数为零。在其余边界参数集合上，限制函数等于零且非负，凡导数存在处导数也为零。故沿该线段几乎处处有同一导数界，积分得
\[
|W(x)-W(z)|\le {|x-z|\over\sigma}. \tag{10}
\]
这个拼接论证不要求外域、内域或线段在其中的交集为凸集，也不要求线段只穿越边界有限次。

对任意 \(z\in S\)，\(W(z)=0\)，(10) 给
\[
|x-z|\ge \sigma W(x).
\]
对整个 \(S\) 取下确界即得 (4)，再把 \(x=\Phi_s(p)\) 代入得 (5)。定理证毕。

作为常数的一致性检查，若 \(A=aI\)、\(S\) 为中心 \(c\)、半径 \(R\) 的球面，可取 \(\sigma=aR\)、\(m=a\)。式 (5) 恰为真实外侧径向距离 \(R(e^{as}-1)\)。这是准确符号恒等式，没有运行球面算例。

## 4. 任意见证的流匹配误差与非零高度

不要求见证 \(q\) 本身恰落在一个已知点的流线上。距离到任意非空闭集是 1-Lipschitz 函数，因此对任意 \(p\in S\)、\(q\in\mathbb R^3\)、\(s\ge0\)，
\[
\boxed{\quad
\operatorname{dist}(q,S)
\ge
\left[
{\sigma\over m}(e^{ms}-1)
-\bigl|q-c-e^{sA}(p-c)\bigr|
\right]_+ .
\quad} \tag{11}
\]
这里 \([v]_+=\max(v,0)\)。任何有证明的上界 \(E_+\) 可代替最后的范数；没有把误差项省去，也不要求 \(q\) 先被证明处在外域。

特别地，取共同原点 \(c=0\)、
\[
A_\beta=\operatorname{diag}(1,1,\beta),\qquad
m=\min(1,\beta),\quad \beta>0.
\]
若真实点
\[
p=(0,Y,z_0)\in S,\qquad q=(0,X,z_0),\qquad X\ge Y>0,
\]
记 \(r=X/Y\)，取 \(s=\log r\)，则
\[
e^{sA_\beta}p=(0,X,z_0r^\beta).
\]
所以
\[
\boxed{\quad
\operatorname{dist}(q,S)\ge
\left[
{\sigma\over m}(r^m-1)-|z_0|(r^\beta-1)
\right]_+ .
\quad} \tag{12}
\]
当 \(z_0\ne0\) 时，原点中心下的两个等高点通常不在同一条 \(A_\beta\) 流线上。式 (12) 显式支付这一差额。

另一种有条件的选择是把共同中心改为 \(c'=(0,0,z_0)\)。同一完整面的原支撑给
\[
A_\beta(x-c')\cdot n
=A_\beta x\cdot n-\beta z_0 n_z
\ge \sigma-\beta|z_0|. \tag{13}
\]
只有右侧严格为正时，才可用这个**新中心及其完整支撑下界**重新应用定理，得到无高度匹配损失的同流式。当前实际核心的准确高度为零，下一节不需要 (12) 的扣除，也不修改原共同中心。

## 5. 当前完整 SO3 场的核心见证确实位于 \(z=0\)

这一节只核实际函数身份和准确数学端口，不宣布任何尚未返回的 field 已通过完整费用。

当前完整 normal 的 \(\Gamma\) 由全部当前核心系数定义。设有限当前模式数为 \(M\)，写
\[
p_c(\theta)=1+\sum_{j=1}^{M}c_j\cos(2j\theta),\qquad
\rho_c=p_c+p_c''.
\]
准确核心曲线为
\[
\Gamma_c(\theta)=p_c(\theta)e_r(\theta)+p_c'(\theta)e_t(\theta), \tag{14}
\]
两个基向量的第三分量均为零。源码的 \(\Gamma\) 没有加入高度变量 \(H\)；\(H\) 只进入帽端点 \(P=R e_r(\Theta_0)+H e_z\)。

完整 R715 物理表示为
\[
U(s,\phi)=(1-h(s))P(\phi)+h(s)\Gamma(\phi)
+\int_0^sT(v,\phi)\,dv
-(1-h(s))\int_0^S T(v,\phi)\,dv,
\]
其中
\[
h(s)=1-10(s/S)^3+15(s/S)^4-6(s/S)^5.
\]
因此 \(h(0)=1\) 和零端点积分给
\[
U(0,\phi)=\Gamma(\phi)\in\{z=0\}. \tag{15}
\]
这不要求把 working raw closure defect 强置为零；完整 lift 本身保留了该准确端口。归零角、原积分、全部 normal stages 和所有自由变量均没有在本论证中删掉。

本次直接核读的实际源为：

- [完整 Fejér 基底](../scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py)，SHA256
  `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3`，
  `_core_and_cap` 用第三坐标为零的 \(e_r,e_t\) 构造 \(\Gamma\)；
- [完整 stage-point normal](../scripts/resume_20261126/fixed_fejer_stage_point_normal_lift.py)，SHA256
  `42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10`，
  `_core_and_cap` 与 `fields_torch` 分别给 (14) 和完整物理 lift；
- [完整闭面装配接口](../scripts/resume_20261126/fixed_fejer_complete_closed_phase_grip_evidence.py)，SHA256
  `d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9`，
  `current_core` 读完整实际自由点，`exact_ports` 明确记录 \(\Gamma\in\{z=0\}\) 及完整相位公式。

最后一个既刊消费者有自己的严格 source/model 绑定。引用其端口公式不使它自动接受不同的 stage-point、N4096 或 M320 来源；对应的完整来源适配仍须显式保留。本文也没有把有限 working sin/cos 在特殊角处的计算字当作准确三角恒等式。

在准确全角正 \(\rho_c\) 与固定正 \(\rho_0\) 条件下，当前和固定核心角变换都是圆周微分同胚。它们在 \(0,\pi/2,\pi,3\pi/2\) 处的正弦项准确为零，所以准确材料反变换保持这些轴角。定义
\[
X=1+\sum_{j=1}^{M}c_j,\qquad
Y=1+\sum_{j=1}^{M}(-1)^j c_j. \tag{16}
\]
则真实核心含
\[
(\pm X,0,0),\qquad (0,\pm Y,0). \tag{17}
\]
必须使用同一个实际完整点的**全部当前** \(M\) 个系数：M320 场不能只读参考 M160，也不能以初始七项 Fejér 系数替代其余自由系数。

原完整 phase 定义是
\[
F_t(s,\phi)=R_\alpha U\bigl(s,\zeta_\alpha(\phi)\bigr),\qquad
\zeta_\alpha=\Theta_0^{-1}(\Theta_0(\phi)-\alpha),\qquad
\alpha=\pi t/2,
\]
并对下片取已付准确镜像，帽和标记保持固定。于是 \(S_1\) 含有四分之一转后的 (17)。这使用 R248 的准确像关系，不假设整张带非轴标记的闭面随相位整体刚体旋转，也不需要 normal 根分支的半转协变。

## 6. 整像握持下界与全部混合目标责任

假设同一实际完整闭面 \(S_0\) 对原点和 \(A_\beta\) 已付 (1)，且上节准确核心和 phase 关系已付。设 \(X,Y>0\)，记
\[
r=\max\{X/Y,Y/X\}\ge1,\qquad m=\min(1,\beta). \tag{18}
\]

若 \(X\ge Y\)，取目标点 \(p=(0,Y,0)\in S_0\) 和 phase-one 点 \(q=(0,X,0)\in S_1\)。它们满足
\[
q=\Phi_{\log(X/Y)}(p).
\]
若 \(Y>X\)，取 \(p=(-X,0,0)\in S_0\) 和 \(q=(-Y,0,0)\in S_1\)，得到同样的比例 \(r\)。故由 (5) 和 Hausdorff 距离的完整目标定义，
\[
\boxed{\quad
\delta_{\rm hold}
\ge d_H(S_1,S_0)
\ge {\sigma\over m}(r^m-1).
\quad} \tag{19}
\]
核心单位外法向在四轴处是相应水平轴向；完整 (1) 本身给 \(X\ge\sigma\)、\(Y\ge\sigma\)。实际消费也应逐字检查正分母，不能对一个未绑定的核心数组自行假定它们为正。

式 (19) 的距离目标是 \(S_0\) 的全部点。某个帽、标记、上片或下片点若可能靠近 \(q\)，仍必须服从整个 \(S_0\) 的同一 Lipschitz 屏障。**这不是**把 \(|X-Y|\)、core-to-core 距离或同材料位移直接冒成整像距离。若仅活动带有正支撑而帽未付，(19) 不可使用。

当 \(\beta\ge1\) 时，\(m=1\)，右侧为准确有理组合
\[
\sigma(r-1). \tag{20}
\]
当 \(0<\beta<1\) 时，必须保留 \(r^\beta\)。整体缩放 \(A\mapsto aA\) 时，应同时变更 \(m\mapsto am\)、\(\sigma\mapsto a\sigma\)、流时间 \(s\mapsto s/a\)；(5) 不变。更一般地，若两个点在特征值 \(\lambda\) 的同一正向特征射线上，半径比为 \(r\)，指数是 \(m/\lambda\)，不能在未正规化的矩阵下仍写 \(r^m\)。

若只想使用独立未标记闭面 \(S^0\) 的完整支撑 \(\sigma_0\)，可以先对完整未标记 phase 族得到
\[
B_0={\sigma_0\over m}(r^m-1).
\]
再按 R248 (248.19) 使用固定帽集合的已付 Hausdorff 改变量 \(h_{\rm mark}\)，得到带标记族
\[
\delta_{\rm hold}^{\rm marked}\ge [B_0-h_{\rm mark}]_+. \tag{21}
\]
所选见证 \(q\) 位于没有改变的核心上，因此仍属于带标记的 \(S_1\)。对这个同一见证直接用
\[
\operatorname{dist}(q,S_0^{\rm marked})
\ge \operatorname{dist}(q,S_0^{\rm unmarked})-h_{\rm mark},
\]
所以此处只对完整目标集合支付一次帽替换误差。

未标记闭面条件必须独立成立，不能从带标记 reach 倒推；也没有假设完整活动像被夹在两个帽支撑平面之间。若直接用带标记的共同 \(\sigma\)，则使用 (19)，无需 (21) 的损失。

## 7. 与完整直径、reach 及准确有理判据的连接

令 \(D_+\) 为同一完整候选的已证上界
\[
D=\operatorname{diam}S_0\le D_+.
\]
它可以来自 R717 的完整逐叶三维范数与全部固定帽/标记预算，不能只用核心直径、水平投影或漏掉 \(H\)。由 (19)，
\[
{\delta_{\rm hold}\over D}
\ge {\sigma\over mD_+}(r^m-1). \tag{22}
\]
因此课题所需 \(\delta_{\rm hold}\ge D/5\) 的一个充分条件是
\[
{\sigma\over m}(r^m-1)\ge D_+/5. \tag{23}
\]
它不自动由 reach≥\(3D/100\) 推出。原握持区的非空内点、点点固定和直径≥\(D/5\) 仍是另一个已经明确的输入责任；本文没有把 \(\delta_{\rm hold}\) 定义改为对固定区稳定子的商距离。

当实际 \(\beta\)、\(\sigma\)、\(D_+\)、\(r\) 都以准确有理数给出，写
\[
m=a/b,\qquad a,b\in\mathbb N,\quad \gcd(a,b)=1.
\]
全部底数严格为正，故 (23) 等价于
\[
\boxed{\quad
r^a\ge
\left(1+{mD_+\over5\sigma}\right)^b.
\quad} \tag{24}
\]
这一判据只涉及准确有理数的整数次幂。无需对非有理 \(r^{a/b}\) 作浮点近似，更无需另算任何 \(F,J\)、normal root 或六 jet。若 \(r\) 仅有已证下界 \(r_-\ge1\)，将左边换为 \(r_-^a\) 仍是充分条件。若要求某个有理下界 \(\ell\ge0\)，相同推导给
\[
{\sigma\over m}(r^m-1)\ge\ell
\iff
r^a\ge(1+m\ell/\sigma)^b. \tag{25}
\]
对 (21) 只须把要求的 \(\ell\) 换成 \(\ell+h_{\rm mark}\)。

也可直接保存一个准确有理幂见证 \(\Lambda\ge1\)，而不保存非有理根：
\[
\Lambda^b\le r_-^a
\quad\Longrightarrow\quad
B_{\rm flow}:={\sigma\over m}(\Lambda-1)
\le {\sigma\over m}(r^m-1)
\le \operatorname{dist}(q,S_0). \tag{26}
\]
这里 \(r_-\ge1\) 必须是**实际所选方向**的已证半轴比下界。若取 \(X\ge Y>0\) 这支且仅有区间数据，可以用 \(r_-=X_{\rm lower}/Y_{\rm upper}\)，前提该比值已证至少为 1、分母严格正；相反方向交换 \(X,Y\)。只有两区间相交而无法确定哪支较长时，\(r_-=1,\Lambda=1\) 仍给诚实的零下界，不能把一个未证排序的正比值冒作见证。

完整的纯有理证据可记录 \(\beta,m,a,b,\sigma,r_-,\Lambda,B_{\rm flow},D_+\)，连同来源/点/核心区间身份；逐项核 \(m=\min(1,\beta)=a/b>0\)、\(\sigma>0\)、\(\Lambda\ge1\)、\(\Lambda^b\le r_-^a\)，再比较 \(B_{\rm flow}\ge D_+/5\)。等号允许使用非严格目标结论；\(\Lambda=1\) 不被误报成原几何命题失败。这只是已付完整几何上的算术证据接口，不是新的求解前置步骤。

指数很大时准确整数计算可能昂贵；这里没有声称其实际运行费用，也没有执行任何算例。

同一场若另有完整实际主曲率上界 \(K\)，共同 \(A_\beta\) 和同一 \(\sigma\) 已由 R650 给
\[
\operatorname{reach}(S_t)\ge
\min\{\sigma/\max(1,\beta),K^{-1}\}
\]
的全相位条件界。本文不改变这个 reach 界、不省略 mixed activity/cap/mark 的共同支撑，也不把新的距离结论当成曲率已付。

## 8. 实际消费者应记录的范围

这条推论可作为既有完整闭面消费完成后的额外纯数学下界，和完整目标盒得到的 \(B_{\rm box}\) 取
\[
B_{\rm final}=\max\{B_{\rm box},B_{\rm flow}\}.
\]
它不能让缺域、未闭合或未重验的流报告变成 complete。

需要的全部身份与数学输入是：

1. 同一最终完整主报告、完整 source/model/target/point/snapshot 和所有输入/输出字节重验；中途副件或可变进度点不充当证书。
2. 整个闭参数球面的准确 \(C^2\) 浸入和端口、全径向/全角覆盖、完整 32-stage 所选根分支及 periodic glue；现有纯公式接口不自行支付这些数据条件。
3. 同一中心 \(0\)、同一 \(A_\beta\)、同一完整闭面共同 \(\sigma>0\)，含活动上下片、两帽和所有固定标记。若选择未标记版本，另记录其独立 \(\sigma_0\) 与帽替换界。
4. 该完整点的全部当前核心系数、准确 \(X,Y\) 与 quarter-phase 成员关系。当前与参考 M、不同 N 观察网和任何 source 变体不可互换。
5. 同场完整 \(D_+\)，以及 (24) 或向外有理包围给出的实际下界；未通过充分不等式只表示该下界不够，不表示真实幅度失败。

本稿不产生某个新场的上述记录。新的 source-bound 消费者若实施本式，仍须按其真实完整来源派生，不得放宽已有族守卫。原已排求解、预算、域、变量、32 个阶段和费用源均不因本文改变。

## 9. 已闭合与尚未闭合的边界

本文闭合的是正定流支撑到全空间 Lipschitz 屏障、从屏障到完整像距离、准确 core-zero-height quarter witness、非零高度损失和有理阈值判据。它直接利用已经登记的 R650 单层流图与 R248 相位像关系，没有重复登记旧 reach 或旧实际距离数值。

尚未给出任何实际候选的 \(\sigma,D_+,X,Y,K\) 完整返回，也没有宣布 \(\delta_{\rm hold}/D\)、reach/D、完整相对度量误差或握持区比例过关。包含反射的 \(\delta_E>0\) 仍按 R716 的同场矩或其他完整准则独立支付；正的未对齐 Hausdorff 幅度不推出刚体商非全等。实际同 \(g\) 的完整 M/mesh/time 精化也没有由本条替代。

全部内容是源码阅读和准确符号证明；未作本地科学、数值 fixture、额外参数扫描或新的求解准入门。
