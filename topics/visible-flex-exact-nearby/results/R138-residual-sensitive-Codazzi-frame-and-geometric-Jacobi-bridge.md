# R138：由 Codazzi 残差到几何 Jacobi 的非循环桥

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明：**同一物理 Codazzi 中心可先作准确径向正交重建；其不满足二维等距的缺陷由完整 Codazzi 残差作两次有向积分控制，不需先有全频逆或真实解。本文给出真实高度 Darboux 残差、完整方向微分、193 条低端行在高度图中的形式，以及无需全正高度法向的 R32 星形应变接口。

桥中保留实际 residual、初始 frame/位置缺陷、独立 mean、接口和完整边界行。它没有证明边界型正定、标量实现 onto、当前正区全逆或非线性存在性。WVC 的替换算子不完全等于修补中心的真实 Jacobi；第 7 节保留其额外主部差。本文没有执行数值计算。

## 1. 同一中心、物理残差与准确径向重建

取原 ac1 候选的连续修补 Qrepair，定义 SHA256 为
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47，
或同一已声明参数族中的一个固定成员。使用其真实各片上的相同 metric
$$
g=e(r)^2dr^2+a(r)^2d\theta^2,\qquad
b_0=a'/e,\quad\beta=a'/a,\quad\gamma=e/a.
\tag{J.1}
$$
完整 moving 场先用 [C.1、C.11](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md) 的真实角图转成物理 $B,C$。置
$$
A=(K+B^2)/C,\quad
R_B=B_r-\gamma A_\theta+2\beta B,\quad
R_C=C_r-\gamma B_\theta-\beta(A-C).
\tag{J.2}
$$
$C\ne0$ 是原图前提；两个 $R$ 是完整 residual，不是有限投影。

沿每条真实角射线解
$$
O_r=O\Omega_r,\qquad F_r=eX,\qquad
O=(X,Y,n),\quad n=Y\times X,
$$
$$
\Omega_r=
\begin{pmatrix}0&0&-eA\\0&0&-eB\\eA&eB&0\end{pmatrix},
\qquad
\Omega_\theta=
\begin{pmatrix}0&-b_0&-aB\\b_0&0&-aC\\aB&aC&0\end{pmatrix}.
\tag{J.3}
$$
初始 $O$ 取准确正交且定向正确的周期数据，$F$ 也取周期数据；不假定初始二维角向方程成立。反对称性与 ODE 唯一性给全程正交和周期。此时还不能把径向对象认作指定 metric 的浸入。

定义角向 frame 与位置缺陷
$$
Z=O_\theta-O\Omega_\theta,\qquad P=F_\theta-aY.
\tag{J.4}
$$
矩阵相乘及准确代数 Gauss 式给
$$
\mathfrak D:=\partial_\theta\Omega_r-\partial_r\Omega_\theta
+\Omega_\theta\Omega_r-\Omega_r\Omega_\theta
=a\begin{pmatrix}0&0&R_B\\0&0&R_C\\-R_B&-R_C&0\end{pmatrix}.
\tag{J.5}
$$
因此
$$
\boxed{Z_r=Z\Omega_r+O\mathfrak D,\qquad P_r=eZ_X.}
\tag{J.6}
$$
$Z_X$ 是第一列。这是 R126 平坦传播的非零 residual 版本。

写初始点为 $r_0$、$r\ge r_0$；反向使用相应区间的绝对积分。令
$$
\begin{split}
\zeta_0(r)&=\|Z(r_0)\|_\infty+
 \int_{r_0}^r a\|(R_B,R_C)\|_\infty\,dt,\\
\pi_0(r)&=\|P(r_0)\|_\infty+\int_{r_0}^r e\zeta_0\,dt .
\end{split}
\tag{J.7}
$$
范数覆盖完整角圆，二分量用 Euclidean norm，矩阵用 operator norm。因为 $\Omega_r$ 的传播正交，
$$
\|Z(r)\|_\infty\le\zeta_0(r),\qquad
\|P(r)\|_\infty\le\pi_0(r).
\tag{J.8}
$$
没有指数 Gronwall 费用。若 $\pi_0<a$，则
$|F_r\times F_\theta|\ge e(a-\pi_0)>0$，径向构造已经是实际浸入；其实际 metric 为
$$
\widetilde g_{rr}=e^2,\quad
\widetilde g_{r\theta}=eX\cdot P,\quad
\widetilde g_{\theta\theta}=a^2+2aY\cdot P+|P|^2.
\tag{J.9}
$$
它的 metric 误差由 residual 支付，不得直接写成 $g$。

## 2. 一次角导数的可用包络

记 $d_j=\|\partial_\theta^j\mathfrak D\|_\infty$，
$o_\theta=\|\Omega_\theta\|_\infty$，
$o_{r1}=\|\partial_\theta\Omega_r\|_\infty$。
由 $O_\theta=O\Omega_\theta+Z$，有 $\|O_\theta\|\le o_\theta+\zeta_0$。所以
$$
\begin{split}
\zeta_1(r)&=\|Z_\theta(r_0)\|_\infty+
 \int_{r_0}^r\{\zeta_0o_{r1}+(o_\theta+\zeta_0)d_0+d_1\}\,dt,\\
\pi_1(r)&=\|P_\theta(r_0)\|_\infty+\int_{r_0}^r e\zeta_1\,dt
\end{split}
\tag{J.10}
$$
控制 $\|Z_\theta\|_\infty,\|P_\theta\|_\infty$。证明只需对 (J.6) 一次求导后用同一正交传播。
$d_1=a\|(R_B,R_C)_\theta\|_\infty$，故只需要一次角 residual 导数；系数都是指定中心的已知函数，不含待求 inverse。

连续径向分片逐片使用这些式子。若所用对象有真实跳，须把 $Z,P$ 及相应角导数的真实跳加为原子；初始缺陷或接口费用不能设零。对 Qrepair 使用其已证连续状态，metric 的真一侧导数仍按原片处理。

## 3. 高度 Darboux residual 的准确表达

选固定环境单位向量 $k$，置
$$
z=F\cdot k,\quad w=n\cdot k,\quad y=Y\cdot k,\quad q=P\cdot k/a.
\tag{J.11}
$$
本节只在所选 patch 的 $w>0$ 且
$S=1-|\nabla_gz|^2>0$ 时作图。相对于 $g$ 的正交基，由 (J.3)--(J.4) 得
$$
\nabla_g^2z=
w\begin{pmatrix}A&B\\B&C\end{pmatrix}
+\begin{pmatrix}0&E_{12}\\E_{12}&E_{22}\end{pmatrix},
\tag{J.12}
$$
$$
E_{12}=\frac{(eZ_X-\beta P)\cdot k}{ea},\qquad
E_{22}=\frac{(aZ_Y+P_\theta)\cdot k}{a^2},\qquad
S=w^2-2yq-q^2.
\tag{J.13}
$$
例如 $z_{r\theta}=e(b_0Y+aBn+Z_X)\cdot k$；减去 $\beta z_\theta$ 后两个 $a'Y$ 项准确抵消。第二角项同样与 Hessian 的径向连接项抵消。

因此 $D_z=\det_g\nabla_g^2z-KS$ 准确为
$$
\boxed{D_z=w(AE_{22}-2BE_{12})-E_{12}^2+K(2yq+q^2).}
\tag{J.14}
$$
取
$$
\epsilon_{12}=\zeta_0/a+|\beta|\pi_0/(ea),\qquad
\epsilon_{22}=\zeta_0/a+\pi_1/a^2,
\tag{J.15}
$$
得到不依赖未知逆的逐点预算
$$
|D_z|\le |A|\epsilon_{22}+2|B|\epsilon_{12}
+\epsilon_{12}^2+|K|\{2\pi_0/a+(\pi_0/a)^2\}.
\tag{J.16}
$$
这把完整物理 residual 送入一个真实高度方程，而不预先假定二维重建成立。

## 4. 同一构造的完整 Jacobi 方向

固定 metric，令 $x=(b,c)=(\delta B,\delta C)$，并置
$$
\alpha=(2Bb-Ac)/C=\delta A,\qquad
f=(\delta R_B,\delta R_C).
\tag{J.17}
$$
对同一径向构造求方向导数，记
$V=\delta O,T=\delta Z,p=\delta P$，则
$$
\begin{split}
V_r&=V\Omega_r+O\delta\Omega_r,\\
T_r&=T\Omega_r+Z\delta\Omega_r+V\mathfrak D+O\delta\mathfrak D,\\
p_r&=eT_X .
\end{split}
\tag{J.18}
$$
$\delta\mathfrak D$ 是 (J.5) 把 $(R_B,R_C)$ 换成 $f$ 的矩阵。
初始 $V,T,p$ 由同一真实边界 frame/位置图给出；它们是数据，不能用“刚体规范”删除整组角函数。

例如
$$
\begin{split}
v_0(r)&=\|V(r_0)\|_\infty+
 \int_{r_0}^r\|\delta\Omega_r\|_\infty\,dt,\\
t_0(r)&=\|T(r_0)\|_\infty+
 \int_{r_0}^r\{\zeta_0\|\delta\Omega_r\|_\infty+v_0d_0
                                      +a\|f\|_\infty\}\,dt,\\
p_0(r)&=\|p(r_0)\|_\infty+\int_{r_0}^r et_0\,dt
\end{split}
\tag{J.19}
$$
控制 $V,T,p$，仍没有指数放大。base residual 及全部 base/方向角缺陷都为零时，齐次 Jacobi $f=0$ 给 $T=p=0$；这是推论，不是前提。

令 $h=\delta F\cdot k$，
$\dot w=\delta n\cdot k,\dot q=p\cdot k/a,\dot y=\delta Y\cdot k$，
而 $\dot E$ 由 (J.13) 将 $Z,P$ 换成 $T,p$。逐项微分 (J.14) 得完整线性化
$$
\begin{split}
L_zh:={}&\operatorname{cof}(\nabla_g^2z):\nabla_g^2h
                 +2K\langle\nabla_gz,\nabla_gh\rangle\\
={}&\dot w(AE_{22}-2BE_{12})
+w(\alpha E_{22}+A\dot E_{22}-2bE_{12}-2B\dot E_{12})\\
&-2E_{12}\dot E_{12}+2K\{\dot yq+(y+q)\dot q\}.
\end{split}
\tag{J.20}
$$
源 $f$ 引起的所有项通过 (J.18) 保留；不能只取“residual 乘方向”而删除 $\delta\mathfrak D$。

正交 frame 的微分还给
$$
w\dot w=-\langle\nabla_gz,\nabla_gh\rangle
                         +y\dot q+q h_\theta/a .
\tag{J.21}
$$
故完整曲率回读为
$$
\begin{split}
b&=\frac{(\nabla_g^2h)_{12}}w+
 \frac{B}{w^2}\langle\nabla_gz,\nabla_gh\rangle+r_B,\\
c&=\frac{(\nabla_g^2h)_{22}}w+
 \frac{C}{w^2}\langle\nabla_gz,\nabla_gh\rangle+r_C,
\end{split}
\tag{J.22}
$$
$$
r_B=-\frac B{w^2}(y\dot q+q h_\theta/a)-\dot E_{12}/w,\qquad
r_C=-\frac C{w^2}(y\dot q+q h_\theta/a)-\dot E_{22}/w .
\tag{J.23}
$$
这是完整 forward 与回读身份；$r_B,r_C$ 仍经 (J.18) 与方向、源和初始数据相连，单独写出 (J.22) 不证明标量 onto 实现。

## 5. 散度差只含实际高度 residual

令 $H=\nabla_g^2z,A_z=\operatorname{cof}_gH,\mu=S^{-3/2}$。
二维曲率交换与余子式代数给
$$
\operatorname{div}_gA_z=-K\nabla_gz,\qquad
A_z\nabla_gS=-2\det_gH\,\nabla_gz .
$$
因此在同一 patch 上
$$
\boxed{\mu^{-1}\operatorname{div}_g(\mu A_z\nabla_gh)
=L_zh+\frac{3D_z}{S}\langle\nabla_gz,\nabla_gh\rangle.}
\tag{J.24}
$$
这与 [R119 的 off-shell 差](R119-supplement-exact-off-shell-divergence-Jacobi-and-narrow-residual-defect.md) 属于同一 residual 原理；此处的高度、metric 和 $D_z$ 由 (J.3)--(J.16) 指定，未假定 curvature 中心是真高度解。

一个可直接消费的局部充分界是：选 $\varepsilon\in\{-1,1\}$ 使
$\varepsilon\mu A_z\succeq\lambda I$，设 patch 的 Dirichlet Poincaré 常数为 $C_P$。若
$$
3C_P\|\mu D_zS^{-1}\nabla_gz\|_\infty<\lambda,
\tag{J.25}
$$
则零 Dirichlet 完整 $L_z$ 的弱型强制常数至少为右侧减左侧。
证明将 (J.24) 的一阶差以
$\|h\|_2\le C_P\|\nabla h\|_2$ 支付；这个充分界不含待证 inverse。
它只适用于指定 Dirichlet patch；本题真实的 193 混合行不能直接消费该 Dirichlet 结论。

## 6. 193 条真实低端行没有变成 Dirichlet

记 $\mathfrak M_Q=(D\Psi(Q))^{-1}$ 为原 C.12--C.13 的完整逆微分，含 even mean 和回到 moving 角的拉回。在物理角中它为
$$
\mathfrak M_Q(b,c)=
\begin{pmatrix}v&-uv\\0&-v^2\end{pmatrix}
\left\{\binom bc-vW_\theta I_\theta(c-mC\langle c\rangle_\theta)\right\}.
\tag{J.26}
$$
记 (J.22) 的两个主项为 $\mathfrak K_zh$，则完整 moving 方向是
$$
h_{\rm mov}=\mathfrak M_Q\{\mathfrak K_zh+(r_B,r_C)\}.
\tag{J.27}
$$

保留 [W96.4--8](R133-supplement-genuine-low96-Poisson-columns-and-exact-positive-boundary-completion.md) 的真实外图。低 193 行由 root 的 96 个非mean even 值与外端的 97 个 regular/mean 行组成：
$$
\begin{split}
\mathcal B_Lh_{\rm mov}&=P_{1:96}^{\rm even}h_{{\rm mov},2}(r_*),\\
\mathcal B_Rh_{\rm mov}&=
\binom{P_{1:96}^{\rm even}
[-\mathscr J_\phi h_{{\rm mov},1}-p_Rh_{{\rm mov},2}
                         -\mathcal E_RPh_{{\rm mov},2}]}{
\Pi h_{{\rm mov},2}-\mu_RPh_{{\rm mov},2}}\bigg|_R .
\end{split}
\tag{J.28}
$$
外端第一行先由 Hilbert 算子把 odd 量送到 even，故输出投影为 even；等价的原实正弦行有相同 96 维数。高 stable root 输入、高 regular 外行及全部独立 affine/height/source 端口仍按原系统保留。这里只显示低 193 行，不投掉方向的高频输入。

真实标量边界因而是
$$
\mathcal B_{L,R}\mathfrak M_Q\mathfrak K_zh
=\text{原边界数据}-\mathcal B_{L,R}\mathfrak M_Q(r_B,r_C).
\tag{J.29}
$$
不可将 $\mathfrak M_Q$ 与 Fourier 投影交换，也不可删掉右侧中 $T,p$ 的 mean 或初始 frame 变化。原 root-complement odd96 加 mean1 的 97 个量是输出观察，不是又加的一组 Dirichlet 条件。

作为符号检查，径向真实背景在单个 $a_s\ne0$ patch 选 $w=|a_s|$ 的高度方向。对 $h_n(s)\cos n\theta$，$s$ 为子午弧长，
$$
c_n=-\frac{n^2h_n}{a^2w}+\frac{a_s}{aw^3}(h_n)_s .
\tag{J.30}
$$
所以 $c_n=0$ 等价
$$
(h_n)_s-\frac{n^2a_s}{a}h_n=0.
\tag{J.31}
$$
在左端 $a_s>0$ 时，按左外法向这是正 Robin，而非 height Dirichlet。实际非径向行还有 (J.26)、$\mathcal E_R,\mu_R$ 和 (J.23)，其正性需要完整真实二次型，不能由这个径向示例转授。

## 7. moving residual 与 WVC 主部差

令 $R_{\rm mov}=Q_r-F(Q)$。原准确协变式是
$$
R_{\rm phys}=D\Psi R_{\rm mov},\qquad
D\mathcal R_{\rm phys}[D\Psi h]
=D\Psi\,\mathcal D_{\rm mov}h+D^2\Psi[R_{\rm mov},h].
\tag{J.32}
$$
第二项的 common transport、mean 和一次角 residual 导数完整保留原 C.20--C.28。必须把 (J.32) 的全右侧作为 (J.17)--(J.18) 的 $f$。

另须区分 [WVC.2](R133-supplement-continuous-repaired-centre-trials-and-clipped-tracefree-reference.md) 的替换生成元。它的 lower-order 项使用 Qrepair，却保留选定完整成员的
$\eta_*=-\gamma\langle v_*\rangle$。令 $\eta_c=-\gamma\langle v_c\rangle$，则
$$
\mathscr A_c=DF(Q_c)+
(\eta_*-\eta_c)\begin{pmatrix}0&-K\\1&0\end{pmatrix}\partial_\phi.
\tag{J.33}
$$
故若 $(\partial_r-\mathscr A_c)h=f_c$，(J.32) 必须使用
$$
\mathcal D_{{\rm mov},c}h=
f_c+(\eta_*-\eta_c)\begin{pmatrix}0&-K\\1&0\end{pmatrix}h_\phi .
\tag{J.34}
$$
它是真实角导源，不是 scalar residual 乘法；$\eta_*=\eta_c$ 的特例才消失。本文不把这个替换生成元称作新物理背景，也不把强方向估计免费扩到旧 $H^{-1}$ 全输入窗。

## 8. 无需全正高度法向的 R32 接口

由 (J.9) 有一个实际浸入。若其真正法向支撑为正，且径向投影在所用片是一一图，按 R32 的固定球面坐标写 $F(u)=u/\rho(u)$。此时用的是实际诱导 metric $\widetilde g$。同一方向的真实应变在原材料坐标中为
$$
\begin{split}
f_{rr}&=0,\\
f_{r\theta}&=e(V_X\cdot P+X\cdot p),\\
f_{\theta\theta}&=2a(V_Y\cdot P+Y\cdot p)+2P\cdot p .
\end{split}
\tag{J.35}
$$
按固定基准径向图拉到球面，令 $\omega=\delta F\cdot u$。R32 的完整恒等式给
$$
\mathcal D_\rho\omega=-\tfrac12\mathcal C_\sigma(\rho^2f),
\qquad
\mathcal D_\rho=\operatorname{div}_\sigma(A\nabla_\sigma)
+\operatorname{tr}_\sigma B,
\quad B=\nabla_\sigma^2\rho+\rho\sigma,\quad A=\operatorname{cof}B.
\tag{J.36}
$$
这里不需要 $n\cdot k>0$。若区域紧含某开半球，可用 R32.7.2 的正一次球谐消去零阶，但保留完整 conormal shear 与 charge。

相对 $g$ 的正交张量范数，(J.35) 给
$$
|f|_g\le 4(v_0\pi_0+p_0)/a+2\pi_0p_0/a^2 .
\tag{J.37}
$$
在球面片上以
$\|\varphi\|_{H^2}^2=\|\varphi\|_2^2+\|\nabla\varphi\|_2^2+
\|\nabla^2\varphi\|_2^2$ 定义零边界测试范数，则
$$
\left\|\tfrac12\mathcal C_\sigma e\right\|_{(H^2_0)^*}
\le\frac{\sqrt3}{2}\|e\|_{L^2}.
\tag{J.38}
$$
证明用
$\mathcal C_\sigma^*\varphi=\nabla^2\varphi-(\Delta\varphi+\varphi)\sigma$：
二维 cofactor 保持 Hilbert--Schmidt 范数，故其 $L^2$ 范数至多
$\|\nabla^2\varphi\|_2+\sqrt2\|\varphi\|_2\le\sqrt3\|\varphi\|_{H^2}$。
这是 interior 弱源估计；坐标/密度转换、边界 charge 和 R32 全局重建域仍须保留。

所以指定中心的实际径向图、非零应变及标量源已有 (J.3)、(J.35)--(J.38) 的具体构造。要得到本题正区 inverse，还需同一参考实际形算子的正性、完整 mixed 边界型、输入输出范数和残差吸收。

## 9. 全域高度图的准确限制与本篇范围

若 $a'(r_c)=0$ 且 $K(r_c)>0$，材料圈 $r=r_c$ 是闭测地线。任一真实等距浸入和任一固定环境方向 $k$，$n\cdot k$ 都不能在该整圈严格同号：沿单位速该圈有
$z''=\mathrm{II}(T,T)(n\cdot k)$；正曲率使 $\mathrm{II}$ 在连通圈上定号，若 $n\cdot k$ 严格同号则 $\int z''\ne0$，与周期性矛盾。

这不妨碍 R32 的星形图：$n\cdot k$ 与位置的一次球谐
$k\cdot F/|F|$ 是不同量；后者可在上半面保持正值。本文不新增当前候选的 $a'$ 数值门，也不把该一般判据冒称已核同对象的全正区端点。

本篇完成 residual 到 frame、metric、height Jacobi 与 R32 应变的准确桥和非循环包络。193 行、初始/接口缺陷和 WVC 主部差可直接进入后续真实边界能量。正区全频逆、true phase Schur、同态 cut 入口及最终闭合仍未由本文证明。振幅保持现行 open 中的输出身份，不另加 fixed-alpha 行或旧 $S_{\rm amp}\ne0$ 门。

