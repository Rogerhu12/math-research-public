# R119：完整径向散射网络、所有仿射源与全局共振的一阶控制

2026-11-14，visible-exact / root。

**状态：已证明；24项新的精确代数门实际全部通过。** 下文把每个固定非零物理频率的真实全径向问题写成有限酉矩阵方程，并给全局简单共振对局部相位保持方向的准确导数。正段交叉、真实无限余尾及完整 weak 源均保留。本篇不声称已经选择同时避开全部全局共振的公共参数，也不把逐频有限矩阵自动提升为原解析标签空间的同宽逆。

## 1. 同一真实问题与有限化的准确含义

固定 $m\in4\mathbb Z\setminus\{0\}$，$M=|m|$，以及第53束的一个真实受控径向 profile。可取
\[
 j_0\ge\max(8193,\lceil320+8\log_2 M\rceil).
 \tag{U.1}
\]
其后所有层属于原来的真实低窗。第53束 C.24--C.28 的完整
$\mathcal H,\mathcal G$、C.34 真低锥及 C.35 非零允许列，给平端到
$j_0$ 的**真实无限余尾**一维允许线及完整 affine 位移。
这使用已收敛的无穷尾强解，未把 $j>j_0$ 的方程或源设为零。

将该非零实线归一为实单位向量；若高度槽为零，直接保留竖直线，
不除以高度。余尾全部源按 C.40--C.48 进入同一允许线的 affine
数据。左端也使用原实际固定 real Robin 线及其全部外源。
有限区间内所有负窗、正段和接缝均保留。
原 mean 的独立高度与完整通量积分仍单独保留，见第7节。

本篇所有参数导数要求上述外线、正段和端口单位固定。
一个紧支于某负窗内部、且两原补偿 bump 也在该窗内的真实
相位保持变化满足局部固定端条件；如果全局 stop、外好参数、
端点或正段也变化，必须另外加入它们的导数。

## 2. 真实负窗的酉散射矩阵

令 $C\in{\rm SL}(2,\mathbb R)$ 为某完整负窗在固定 canonical
wave 单位中的真实两态传递：
\[
 Y_R=CY_L+f,\qquad
 Y=(\sqrt k\,u,u_t/\sqrt k),\quad
 u=\sqrt\mu h,\quad k=\sqrt{7M^2-16}.
 \tag{U.2}
\]
有 weak 源时准确改用
$\widehat Y_2=(\pi+\mu_t h/2)/\sqrt{k\mu}$
且 $\pi=\mu h_t+F^t$，故
$\widehat Y_2=u_t/\sqrt k+F^t/\sqrt{k\mu}$。
这是同一 canonical total-flux 延拓；不能先对 $F^t$ 微分。
以下仿射式使用此完整两态，齐次式中它与 (U.2) 相同。设
\[
 a=(Y_1+iY_2)/\sqrt2,\qquad b=(Y_1-iY_2)/\sqrt2.
\]
若 $C=(c_{rs})$，则
\[
 \alpha=\tfrac12(c_{11}+c_{22}+i(c_{21}-c_{12})),\quad
 \beta=\tfrac12(c_{11}-c_{22}+i(c_{21}+c_{12})),
\]
\[
 TC T^{-1}=\begin{pmatrix}\alpha&\beta\\
 \bar\beta&\bar\alpha\end{pmatrix},\qquad
 |\alpha|^2-|\beta|^2=1.
 \tag{U.3}
\]
特别 $|\alpha|\ge1$。令入射与出射分别为
$x=(a_L,b_R)$、$y=(b_L,a_R)$。完整等式准确成为
\[
 y=S(C)x+t,\qquad
 S(C)=\frac1{\bar\alpha}
 \begin{pmatrix}-\bar\beta&1\\1&\beta\end{pmatrix},
\]
\[
 t=\begin{pmatrix}-f_b/\bar\alpha\\
                  f_a-\beta f_b/\bar\alpha\end{pmatrix}.
 \tag{U.4}
\]
$S^*S=I$ 且 $S^T=S$；实际透射 $1/\bar\alpha$ 非零，但整个改写
不倒除它。source 矩阵的 Frobenius 范数准确为 $\sqrt2$，故
\[
 \|t\|_2\le\sqrt2\|f\|_2.
 \tag{U.5}
\]
若 $f=\int C(R,s)\mathcal J(s)\,ds$ 且完整双向真实界为 $K$，
则 $\|t\|\le\sqrt2K\int\|\mathcal J\|$。$\mathcal J$ 必须是
第53束 C.42 的完整两分量经准确 determinant-one frame 变换后
的源；ordinary、两 weak 分量、真实材料 Jacobian 均不能省略。

## 3. 正段：保留完整 DN 及真实 normal shear

在任一完整正段，令 $N$ 为真正的双端 outward DN，$q$ 为零
Dirichlet particular 解的双端总通量。它们满足
$p_{\rm phys}=Nh_{\partial}+q$。真实正能量恒等式给 $N=N^*$；
全部 cross 系数包含在 $N$ 内。

令端口 $W_e=k_e\mu_e>0$，并写
\[
 x_e=W_e^{1/2}h_e,\qquad
 p_e=W_e^{-1/2}p_{{\rm phys},e}+\tau_e x_e.
 \tag{U.6}
\]
$\tau_e$ 是实际换到负窗 wave state 的实 normal shear。
在共同向 $t$ 增长的 flux 下，它由
$u_t/\sqrt k=(\pi+\mu_t h/2)/\sqrt{k\mu}$
给出；换 outward 法向时同时改变对应符号。
因此完整关系为
\[
 p=\mathcal N x+\widetilde q,\qquad
 \mathcal N=W^{-1/2}NW^{-1/2}+\operatorname{diag}\tau_e
             =\mathcal N^*,\quad
 \widetilde q=W^{-1/2}q.
 \tag{U.7}
\]
$\mathcal N$ 不必正定。用 $a=(x+ip)/\sqrt2,b=(x-ip)/\sqrt2$ 得
\[
 b=S_+a+t_+,\quad
 S_+=(I-i\mathcal N)(I+i\mathcal N)^{-1},\quad
 t_+=-i\sqrt2(I+i\mathcal N)^{-1}\widetilde q.
 \tag{U.8}
\]
$S_+$ 酉，且 $\|t_+\|\le\sqrt2\|\widetilde q\|$。
自伴性给 $\|(I+i\mathcal N)^{-1}\|\le1$；不需要倒除一个可能很小
的 DN cross，也不需要对角的正下界。

原 positive-transmission 定理若给 $D_e^{-1/2}q_e$ 的界，转到
本篇时须保留实际乘子 $W_e^{-1/2}D_e^{1/2}$。
若使用原 Airy 源单位，则保留相应准确对角变换和 normal shear。
本篇没有把这些不同端口 norm 的费用默认为1。
全部 $F^t$ 端点 charge 也随总通量一起传入；需要 bare flux 时，
最后再减真实的 $F^t$ 端点值。

## 4. 完整网络方程与两端实线

将各负窗的 (U.4) 直和为 $y=Sx+t$。相邻正段在上述法向约定下
满足 $y=S_+x+t_+$，所以消去正段时使用
$x=S_+^*y-S_+^*t_+$，不是把法向符号漏掉。

每个非零实 Robin 线也给一个模长1的 reflection。
具体地，对实单位 $r=(r_1,r_2)$，若
$[r,Y]=b_0$，则
\[
 b-\frac{r_1-ir_2}{r_1+ir_2}a
       =-\frac{i\sqrt2\,b_0}{r_1+ir_2}.
 \tag{U.9}
\]
分母模长为1，竖直线完全合法；affine 范数为 $\sqrt2|b_0|$。

组合全部真实正段、固定边界 reflection 和连接置换，得酉矩阵
$P$ 与完整 affine 向量 $p$：
\[
 x=Py+p,\qquad
 \boxed{(I-U)x=g,\quad U=PS,\quad g=Pt+p.}
 \tag{U.10}
\]
所有正段 cross、外接两迹、真实无限余尾以及普通/weak 数据均
准确包含在这里。特别
$\|g\|\le\|t\|+\|p\|$；不同源的已付端口单位继续保留。

在这个固定频率的有限 Hilbert 空间中，
\[
 \|(I-U)^{-1}\|
  =\frac1{\min_{\zeta\in\sigma(U)}|1-\zeta|}
 \tag{U.11}
\]
当且仅当右侧分母非零。这是 normal 酉矩阵的准确公式，
不是对分母的一个已验证下界。
“所有单窗 fixed-port Wronskian 非零”本身并不给 (U.11) 的分母。

## 5. 真正全局简单共振的准确变分

设 $\zeta=1$ 是 (U.10) 的共振，并固定全部真实外边界。
整个连接区间仍是一个实二阶标量 ODE：一个左实线只给一个自由
幅度，真实各段两态传递可逆。因此全局齐次解空间的复维数至多1。
全部负窗的实际 transmission 非零，(U.10) 与该 ODE 双向等价，
故 $\ker(I-U)$ 恰一维。因为 $U$ 酉，这个特征值也代数简单。

取 $\|x\|=1$ 的特征向量，可乘一个公共复标量使相应物理
$Y$ 为实。对于只改变第 $i$ 个负窗而固定 $P$ 的实参数，
该简单特征值可写为 $e^{i\theta}$，在共振处
\[
 \theta'=-i\,x^*U^*U'x
         =-i\,y_i^*S_i'x_i.
 \tag{U.12}
\]
计算第二式时 $x_i$ 固定。由
$\Omega(Y,\dot Y)=Y_1\dot Y_2-Y_2\dot Y_1$ 及固定
$a_L,b_R$，准确有
\[
 -i\,y_i^*S_i'x_i
   =\Omega(Y_R,\dot Y_R)-\Omega(Y_L,\dot Y_L).
\]
实际 Green 变分恒等式因此给
\[
 \boxed{\quad
 \theta'=\int_{I_i}
 \mu(h_t^2-2M^2hh_t+M^2h^2)\,\psi\,dt .
 \quad}                                                    \tag{U.13}
\]
这里 $\psi=\partial_\varepsilon\log p_*$ 是真实紧支方向。
在未用区间选择 phase annihilator 后，原两 bump 的补偿一阶
准确为零，所以 (U.13) 包含完整补偿变化。
原 $dt=a\,dx$ 仍在积分中。没有另除右端 resonant amplitude。

(U.13) 使用当前全局解在该窗的实际端点状态。为了消费既有局部
控制定理，可把右端状态所张成的实单位线作为该点的固定辅助线；
求导时固定它，并不是把随全局解变化的右线偷换为一个固定物理
边界条件。

## 6. 从局部真实控制到全局 eigenphase 的量化入口

设网络有 $n$ 个可控负窗，且在当前共振下，每窗都有
$|C_i|,|C_i^{-1}|\le K_i$ 和已证明的单位左状态局部控制下界
$|\Delta_i'|\ge D_i$。这些下界必须在该窗当前实际频率、未用
支集及真实 profile 上成立。

如果所有非零 incoming 槽均属于这些可控窗，则至少一个 $i$ 有
$\|x_i\|^2\ge1/n$。对实解，
\[
 \|x_i\|^2
 =\frac{\|Y_L\|^2+\|Y_R\|^2}{2}
 \le K_i^2\|Y_L\|^2.
\]
令 $\widehat Y_L=Y_L/\|Y_L\|$。
局部真实共振归一给
$C_i\widehat Y_L=\alpha_i r_i$，
$|\alpha_i|\ge K_i^{-1}$，且
$\int\mathcal K_{\widehat h}\psi\,dt=\alpha_i\Delta_i'$。
所以该方向的完整全局导数满足
\[
 \boxed{\quad |\theta'|\ge D_i/(nK_i^3).\quad}                 \tag{U.14}
\]
如果只有部分窗可控，正确版本是用其 incoming 质量
$\vartheta=\sum_{\rm controlled}\|x_i\|^2$：
至少一窗给 $|\theta'|\ge\vartheta D_i/(nK_i^3)$。
没有已证 $\vartheta>0$ 的量化下界时，不能把它删除。
中频的短支集 $D_i$ 或第56/57束高振荡 $D_i$ 只能在各自实际
条件下代入；浅层和 low-scaled-frequency 也不能冒称满足高振荡门。

这使局部控制确实作用于完整全局分母，而不要求把真实正段交叉
估成小量。它尚不是统一的全局避共振参数选择。

## 7. 完整源、mean、参数及尚待支付的费用

负窗使用第53束准确总通量源
\[
 \mathcal J_m=
 \binom{-\nu_m r^4F^t/(\sqrt{12}\mu_jp_*)}
 {r^4(f-imF^\theta+M^2F^t)/(12\mu_j)} .
 \tag{U.15}
\]
源到 wave frame 的全部径向密度、真实端口 shear、有限强迫积分
和真实无限余尾的 affine 位移都需逐一消费。
ordinary $f=w^2e$ 保两个真实 $p_*$ 因子。

$m=0$ 的原方程保持
\[
 \pi_0(t)=\int_{t_f}^t f_0(s)\,ds,\quad
 (H_0)_t=(r/w)(\pi_0-F^t_0),\quad H_0(t_f)=\lambda.
 \tag{U.16}
\]
独立 $\lambda$、电阻积分及其参数变化未被非零模散射删除。
平端 $C^2$、bare flux 迹及完整源范数仍是第53束原来的条件。

若 $P$ 随参数变动，(U.12) 还准确多出
$-i\,y^*P^*P'y$；若端口 frame 变动，源和状态也必须按实际
变换微分。不能以本篇固定 $P$ 公式免费转授 retuned stop。

最后，尽管 $S$ 的参数导数可以从 (U.4) 直接控制，单个
$\theta$ 的二阶导数还含其它 eigenphase 的谱间距。
本篇没有用局部 Wronskian Hessian 代替这项全局费用。
共同参数的完整坏集、全局簇、非径向混模、原解析权下的
uniform inverse 和最终 nonlinear $\mathcal F=0$ 仍需继续。

## 8. 精确代数执行

配套源码以 BigInt 多项式准确验证 (U.3)--(U.5)、(U.9) 的恒等式、
传递和散射的双向消元、真实 normal shear，以及全部归一化因子。
它按 $c_{11}c_{22}-c_{12}c_{21}=1$ 作符号约简，不使用有限矩阵
随机样本来代替全量词。解析的无限余尾、Green 恒等式和简单性
由上文证明，未冒称生成了新的数值全局 profile 或谱间距。


源码：[fourfold_complete_radial_unitary_network.mjs](../scripts/fourfold_complete_radial_unitary_network.mjs)。
完整原生报告：[2026-11-14-R119-complete-radial-unitary-network-rational.json](../notes/2026-11-14-R119-complete-radial-unitary-network-rational.json)。
本次在可用V8运行完整calculate函数，24项全部通过；源码SHA256为
0325a5b1c705fb7a3b7d59b5c510f3707cb2f109b9d544d6800f7bf6b319d0e7。
没有将尚未运行的Python/径向数值solver计入本记录。
