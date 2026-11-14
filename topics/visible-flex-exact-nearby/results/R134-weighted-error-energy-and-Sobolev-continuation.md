# R134：真实密度加权误差能量与闭合 C0 管的线性门

2026-11-13，visible-exact-astra-ac0d。

**结论性质：完整准确估计及可执行的验证合同。** 对R126/R131同一个
严格负曲率Cauchy问题，权重 \(w=(q-p)^{-1}\) 准确消掉输运能量中
实际速度的角导数。零阶误差的principal增长只需候选
\(\partial_\theta(P+Q)\)，而不必单独支付 \(P_\theta,Q_\theta\) 的最大值。
再接R131加权梯度误差的线性系统及完整四重周期Sobolev不等式，可用
两个线性微分屏障闭合真正C0管，并据此排除实际一阶爆破。

本篇尚未对更远区间执行这套新的误差门。已有C0-only报告若没有
\(\rho_1\) 或直接加权梯度残差，不能自动充当本篇输入。
这是新验证方法的已证合同，不是一个未经执行的更宽精确环带结论。

## 1. 真实权重的两条取消

沿用R131：
\[
D_p=\partial_r-\gamma q\partial_\theta,\quad
D_q=\partial_r-\gamma p\partial_\theta,\quad
d=p-q<0,
\]
\[
f=-\beta q(1+p^2)+\kappa d,\quad
g=-\beta p(1+q^2)-\kappa d,\quad
H=\beta(1-pq)+2\kappa.
\]
实际恒等式是 \(D_pd=dH-\gamma d q_\theta\)、
\(D_qd=dH-\gamma d p_\theta\)。因此正权重
\(w=-1/d\) 满足
\[
\boxed{D_pw-\gamma q_\theta w=-Hw,\qquad
       D_qw-\gamma p_\theta w=-Hw.}
\tag{134.1}
\]
它使用实际解，而不把候选权重的残差遗漏。
对真实输运未知量 \(D_pu=F\)，完整周期积分分部给
\[
\frac d{dr}\langle wu^2\rangle
=\langle w(2uF-Hu^2)\rangle.
\tag{134.2}
\]
第二特征同理。这里角平均在物理四重周期 \(L=\pi/2\) 上归一，
\(\langle h\rangle=L^{-1}\int_0^Lh\,d\theta\)。所有mean均保留。

## 2. 零阶误差的准确加权能量

令明确候选 \(P,Q\) 的完整真实PDE残差为
\[
R_P=P_r-\gamma QP_\theta-f(P,Q),\qquad
R_Q=Q_r-\gamma PQ_\theta-g(P,Q).
\]
置 \(u=p-P,v=q-Q\)。沿实际特征，
\[
\begin{aligned}
D_pu&=a u+b v-R_P,\\
D_qv&=c u+e v-R_Q,
\end{aligned}
\]
其中准确系数为
\[
\begin{aligned}
a&=-\beta q(p+P)+\kappa,&
b&=\gamma P_\theta-\beta(1+P^2)-\kappa,\\
c&=\gamma Q_\theta-\beta(1+Q^2)-\kappa,&
e&=-\beta p(q+Q)+\kappa.
\end{aligned}
\tag{134.3}
\]
定义 \(E_0^2=\langle w(u^2+v^2)\rangle\)。由(134.2)，
\[
(E_0^2)'=\left\langle w\left[
(2a-H)u^2+(2e-H)v^2+2(b+c)uv-2uR_P-2vR_Q\right]\right\rangle.
\tag{134.4}
\]
关键的完整取消为
\[
\begin{aligned}
2a-H&=-\beta(1+pq+2qP),\\
2e-H&=-\beta(1+pq+2pQ),\\
b+c&=\gamma(P_\theta+Q_\theta)-\beta(2+P^2+Q^2)-2\kappa.
\end{aligned}
\tag{134.5}
\]
对角项中的 \(\kappa\) 也准确抵消。单独的
\(\gamma\max(|P_\theta|,|Q_\theta|)\) 不再进入零阶指数。

在真实和候选均有 \(|p|,|q|,|P|,|Q|\le M\)、\(q-p\ge g_*>0\)
的区域，设完整上界
\[
|P_\theta+Q_\theta|\le S_1,\qquad
\max(|R_P|,|R_Q|)\le\rho_0.
\]
由真实对称二次型的行和及Cauchy–Schwarz，
\[
\boxed{D^+E_0\le\tfrac12\Lambda_0E_0+
\sqrt{2/g_*}\,\rho_0,\quad
\Lambda_0=\gamma S_1+|\beta|(3+5M^2)+2|\kappa|.}
\tag{134.6}
\]
在 \(E_0=0\) 处以 \(\sqrt{E_0^2+\epsilon^2}\) 正则化后取极限，
所以不需假定误差非零。真实参数全为实数；没有把复背景的双线性式
误当正能量。

## 3. 加权角梯度误差也只需线性系统

R131的实际和候选加权梯度分别为
\[
U=d p_\theta,\quad V=d q_\theta,\qquad
\widehat U=(P-Q)P_\theta,\quad\widehat V=(P-Q)Q_\theta.
\]
记 \(\zeta=U-\widehat U,\omega=V-\widehat V\)，
\(E_W^2=\langle w(\zeta^2+\omega^2)\rangle\)。真实矩阵是
\[
a_G=\beta(1-3pq)+3\kappa,\quad
b_G=-\beta(1+p^2)-\kappa,\quad
c_G=-\beta(1+q^2)-\kappa.
\]
结合相同权重后，能量的对角和非对角项准确为
\[
2a_G-H=\beta(1-5pq)+4\kappa,\qquad
b_G+c_G=-\beta(2+p^2+q^2)-2\kappa.
\tag{134.7}
\]
因此一个非负完整增长系数是
\[
\Lambda_W=|\beta|(3+7M^2)+6|\kappa|.
\tag{134.8}
\]
如实际需要，可保留(134.7)中 \(4\kappa\) 的符号进一步收紧。

设候选的完整 \(\widehat W_0,\widehat W_1\) 分别控制
\(\max(|\widehat U|,|\widehat V|)\) 及其一次角导数。
误差方程中的矩阵差和速度差组成的实际源，以 \((u,v)\) 为输入的
两行系数绝对值分别可包在
\[
\begin{pmatrix}
5|\beta|M\widehat W_0&3|\beta|M\widehat W_0+\gamma\widehat W_1\\
3|\beta|M\widehat W_0+\gamma\widehat W_1&5|\beta|M\widehat W_0
\end{pmatrix}.
\tag{134.9}
\]
例如第一行的两个准确非输运系数是
\(-3\beta q\widehat U-\beta(p+P)\widehat V\) 和
\(-3\beta P\widehat U+\gamma\widehat U_\theta\)。第二行类似。
上述上下行和相同，故其Euclidean算子范数不超过
\(C=8|\beta|M\widehat W_0+\gamma\widehat W_1\)。
实际权重在输入和输出均为同一个w，因此这里不额外损失gap因子。

准确候选加权残差是
\[
S_U=(R_P-R_Q)P_\theta+(P-Q)\partial_\theta R_P,
\quad
S_V=(R_P-R_Q)Q_\theta+(P-Q)\partial_\theta R_Q.
\tag{134.10}
\]
若完整 \(\max(|S_U|,|S_V|)\le\rho_W\)，则
\[
\boxed{D^+E_W\le\tfrac12\Lambda_WE_W+C E_0+
                              \sqrt{2/g_*}\rho_W.}
\tag{134.11}
\]
这与(134.6)组成三角线性系统，不含 \(E_W^2\) 或实际角导数的未知系数。

若只有普通完整界 \(D_1,D_2,\rho_1\)，可安全取
\[
\widehat W_0=2\widehat M D_1,\quad
\widehat W_1=2D_1^2+2\widehat M D_2,\quad
\rho_W=2\rho_0D_1+2\widehat M\rho_1.
\tag{134.12}
\]
更紧的直接真实 \(S_U,S_V\) 包围也可消费。没有\(\rho_1\)或直接
\(\rho_W\)的C0-only报告不得将这一费用当成零。

## 4. 包含mean的四重周期 Sobolev-C0 门

对向量误差 \(e=(u,v)\)，由 \(w\ge1/(2M)\) 有
\[
\|e\|_{L^2}\le A:=\sqrt{2M}E_0.
\]
准确恒等式
\[
d\,e_\theta=(\zeta,\omega)-(u-v)(P_\theta,Q_\theta)
\]
给
\[
\|e_\theta\|_{L^2}\le
B:=\frac{\sqrt{2M}}{g_*}(E_W+2D_1E_0).
\tag{134.13}
\]
第二项的常数2来自
\(|u-v|\le\sqrt2|e|\)、\(|(P_\theta,Q_\theta)|\le\sqrt2D_1\)，
并非只对单分量套一个遗漏交叉项的界。

取一个点 \(\theta_0\) 使 \(|e(\theta_0)|^2\le\|e\|_2^2\)，在完整
长度L周期上积分 \((|e|^2)'=2e\cdot e_\theta\)，得到
\[
\|e\|_\infty^2\le\|e\|_2^2+2L\|e\|_2\|e_\theta\|_2
\le A^2+\pi AB.
\]
于是完整可检验的C0管门为
\[
\boxed{\quad
\max(\|p-P\|_\infty,\|q-Q\|_\infty)
\le\left[2M\left(E_0^2+
\frac\pi{g_*}E_0(E_W+2D_1E_0)\right)\right]^{1/2}.
\quad}
\tag{134.14}
\]
该证明对非零mean同样成立；没有用零mean的Poincaré来丢掉任何平均行。

## 5. 真正延拓的闭合合同

先选预定C0管T>0。每盒给整个闭矩形/全角/全η上的完整候选界，取
\[
M=\widehat M+T,\qquad g_*=\widehat g-2T>0,
\quad \widehat g\le\inf(Q-P).
\tag{134.15}
\]
初始真实逐点误差若由 \(\epsilon_0,\epsilon_1\) 控制，可选严格大于
\[
E_{0,\rm init}\le\sqrt{2/g_*}\epsilon_0,
\quad
E_{W,\rm init}\le\sqrt{2/g_*}(2M\epsilon_1+2D_1\epsilon_0)
\tag{134.16}
\]
的有向屏障初值。这里M、g、D1用含初点的完整盒上界，且需先检查
\(\epsilon_0<T\)。

设一盒长度h，上盒终屏障是s0,sW。使用该盒全部系数上界，选择非负
终值t0,tW使
\[
\begin{aligned}
t_0-s_0&>h(\tfrac12\Lambda_0t_0+\sqrt{2/g_*}\rho_0),\\
t_W-s_W&>h(\tfrac12\Lambda_Wt_W+Ct_0+
                                      \sqrt{2/g_*}\rho_W).
\end{aligned}
\tag{134.17}
\]
若 \(1-h\Lambda_0/2,1-h\Lambda_W/2>0\)，可以按顺序解这两个
线性不等式并加有向外舍入余量；不是Riccati求根。实际屏障为端点间
仿射函数，故(134.17)支付完整盒的微分不等式。
最后将t0,tW代入(134.14)，要求严格小于T。

**延拓结论。** 若全部有限闭盒通过上述门，真实R125分支继续存在，
且其C0误差满足(134.14)。证明先在真实局部分支尚处管内时使用所有
能量不等式；严格C0门排除首次离开。随后真实M/g和R131的线性加权
梯度输运给实际一阶导数的统一有限上界，排除有限最大存在端点。
这不是拿待证全域解定义一个不可检查的循环范数。

候选P,Q及其角导数须在片间连续；否则要另付实际跳跃。
原精确dense候选共享完整Fourier端值，满足此条件。germ处实际状态与
w连续，故能量和两屏障可直接传递，系数使用各自的一侧有向盒。
全参数使用统一真实界逐个应用，目标仍为同一原始E和a。

## 6. 消费与当前边界

S1最好从 \(P+Q=2\widehat B/\widehat C\) 的完整导数直接包围，
避免先对两个含±k的项取绝对值再相加而破坏本篇的抵消。
所有 \(\rho_0,\rho_W\) 仍必须是原无限PDE的真实全矩形残差。
本篇符号程序核对(134.1)、源差分解和两个能量对角的准确取消；
它不冒充尚未运行的长区间屏障消费者。

后续实际任务是生成这些更相关的候选/残差字段并运行(134.17)与
(134.14)。当前已经独立证明的环带范围和几何费用以R132及其实际
native补充为准。正帽/跨根/无限尾及最终闭族仍继续处理。
