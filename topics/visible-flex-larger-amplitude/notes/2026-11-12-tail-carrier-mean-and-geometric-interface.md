# Carrier 候选的完整 mean、两阶接缝及几何误差接口

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-12

**状态：以下条件引理已证明；尚无新的数值几何证书。** 本文补充
[carrier 构造](2026-11-12-tail-background-carrier-compatible-interpolation.md)
的验收接口，不改其候选、固定真实度量或四步实际执行。
它把已有的非均值两 jet 条件与完整 mean、真正的空间接缝和
握持量/reach 所需误差分别连接起来。所有不等式均要求连续径向、全角及所用
参数范围的一致界；保存样本或单个源 ODE jet 不支付这些量。

## 1. 共享端点所确定的量

固定 $g=E(r)\,dr^2+r^2d\theta^2$，$E=1+w^2$，其中 $w>0$、$w\in C^1$。
记候选非均值高度为 $\widehat H$，并设

$$
 P=\frac{\widehat H_\theta}{rw},\qquad
 \overline K=\frac{\widehat H_r}{w},\qquad
 T=P_\theta,\qquad K=c+\overline K.
 \tag{G.1}
$$

$c$ 是 R64 的完整角平均方程的唯一可容许根。它不是截断均值，也不由
任意平均斜率代替。假设相邻两段使用同一个真实端点对象
$(r,w,w_r,\widehat H,\widehat H_r,\widehat H_{rr})$，且各自支付同一根分支的
严格单调和实正门。

这些对象确定共同的 $P,\overline K,T$ 及它们的实际径向导数：

$$
 P_r=\frac{\overline K_\theta}{r}
       -\left(\frac1r+\frac{w_r}{w}\right)P,\qquad
 T_r=\partial_\theta P_r,\qquad
 \overline K_r=\frac{\widehat H_{rr}}w-\frac{w_r}{w}\overline K.
 \tag{G.2}
$$

完整 mean 方程及其隐函数导数在两侧因此完全相同。根唯一性和
$\mathcal M_c>0$ 给相同的 $c,c_r$。由一个统一常数定义

$$
 \widehat h_0(r)=C+\int_{r_*}^{r}w(t)(1+c(t))\,dt,\qquad
 \widehat h=\widehat h_0+\widehat H,
 \tag{G.3}
$$

于是 $\widehat h_r=w(1+c)+\widehat H_r$ 和
$\widehat h_{rr}=w_r(1+c)+wc_r+\widehat H_{rr}$ 在接缝连续。
其余角与混合两 jet 由共享 Fourier 场及 (G.2) 给出。因此这是同一个整体
$C^2$ 高度候选。有限段上参数的 $C^2$ 连续性还需要统一的根分母余量；
无限 cuff 的一致极限须另用真实深尾定理支付。

**两个必须保留的区别。**

1. 上述结论比较的是使用同一完整根的候选段。保存的 worker mean、前缀
   PPoly mean 或 ODE 二阶输出若只近似该根，仍须在真实接缝中核销差异。
   原文件中非均值两 jet 相同不能单独证明前缀已与精确内尾接合。
2. mean 的导数在两个外端相同，不强迫整个区间的 mean 高度差为零。
   不得在每个共享节点重新设置 $C$。

## 2. 只用已付五正矩的 mean 高度账本

对同一物理子段，R48 基函数恒等满足 $q_{00}+q_{01}=1$。因此每个真实源叶 $I$
上均有

$$
 \omega_I:=\int_I w\,dr=I_{00,I}+I_{01,I}>0.
 \tag{G.4}
$$

它是已经存在的两个正矩之和，**不需要新积分**。两种候选 $A,B$ 若在左端使用
同一个 mean 常数，则

$$
 \Delta h_0(r)=\int_{r_L}^{r}w(c_B-c_A)\,dr.
 \tag{G.5}
$$

若已付整叶 $|c_A|\le C_{A,I}$、$|c_B|\le C_{B,I}$，有

$$
 \sup_{r\in[r_L,r_R]}|\Delta h_0(r)|
 \le \sum_I \omega_I(C_{A,I}+C_{B,I}).
 \tag{G.6}
$$

对中间叶可保留前缀和及该叶整量；不把一个采样根代替整叶 supremum。
若另有同一整叶的联合根差界 $C_{\Delta,I}$，可用它替换
$C_{A,I}+C_{B,I}$，但现有两个独立根区间本身不给有符号相消。

现 PM primary 的 moments["00"]、moments["01"] 正好提供 (G.4)；
PA/CF primary 的 bounds_upper.complete_mean_abs 给 (G.6) 的上界。
字段 source_width 在这个重建 PM 中表示真实 $\Delta r=\int r_xdx$，并非
$x_R-x_L$；PA 已按这一物理量使用它。式 (G.4) 可进一步避免旧
$\Delta r\,\sup w$ 中的无关位置放大。这是合法收紧同一 mean 积分，不能与
两个不同高度候选的 Darboux 缺陷取最小混淆。

若将首子段替换进原八子段，只在左端锚定一次 mean 高度，此后未改子段的
mean 高度整体平移 (G.5) 在右端的值，mean 导数与非均值场不因此改变。
自由 cuff 的绝对高度可随之平移；若某个已经固定的外部空间拼接同时指定
另一端 mean 高度，则该有符号差必须作为边界条件支付，不能宣布被平移消除。
同一物理相位平移下完整平均根不变，因此这个平移量对相位相同。

### 2.1 从现 primary 得到两候选完整高度差

在同一个源叶，设 $\Delta H_m,\Delta K_m,\Delta K_{r,m}$ 是两个已保存
实 cosine 系数区间的相减，所有模式之和均包括实际全部非均值模式。
区间相减允许作为有效上界；它不声称获得了两个计算过程之间的更强关联。
记 $\|\cdot\|_0$ 为这些完整 Fourier 系数的绝对和，则

$$
\begin{aligned}
 |\Delta h|&\le |\Delta h_0|+\|\Delta H\|_0,\\
 |\Delta h_\theta|&\le\|\partial_\theta\Delta H\|_0,\qquad
 |\Delta h_{\theta\theta}|\le\|\partial_{\theta\theta}\Delta H\|_0,\\
 |\Delta h_r|&\le w\bigl(C_A+C_B+\|\Delta K\|_0\bigr),\\
 |\Delta h_{r\theta}|&\le w\|\partial_\theta\Delta K\|_0,\\
 |\Delta h_{rr}|&\le |w_r|\bigl(C_A+C_B+\|\Delta K\|_0\bigr)
       +w\bigl(C_{r,A}+C_{r,B}+\|\Delta K_r\|_0\bigr).
\end{aligned}
\tag{G.7}
$$

这里 PA/CF 的 complete_mean_source_derivative_abs 就是 $|c_r|$：
这两入口明确以物理 $r$ 为独立变量，radius_x=1。它不是原 source $x$ 导数。
(G.7) 仅比较两个候选；把其中一个换成精确解时，所有差界必须由实际
Green/Schur 验证另行给出，不能由小 $\mathcal J$ 裸值直接推导。

## 3. 从完整高度两 jet 到真正空间 $C^2$ 接缝

**条件接缝引理。** 两侧已有真正的 $C^2$ 等距浸入，使用同一 $C^1$ 度量 $g$、
同一物理坐标及正向水平 Jacobian，且 $n_z>0$。若共同边界的空间位置相同，
两侧完整高度两 jet 相同，则两侧完整空间两 jet 相同。

**证明。** 沿共同边界的位置一致给共同 $F_\theta$。
写 $X$ 为水平分量，$a=(r^2-h_\theta^2)^{1/2}$，令
$t=X_\theta/a$、$n=Jt$。同一正向分支下 R30 给

$$
 X_r=-\frac{h_rh_\theta}{a}\,t
 -\frac{\sqrt{E(r^2-h_\theta^2)-r^2h_r^2}}a\,n.
 \tag{G.8}
$$

右侧只含相同的一阶高度和度量数据，因此 $F_r$ 相同，单位法向也相同。
正竖直法向分量 $\nu=n_z$ 不为零，故

$$
 \mathrm{II}_{ij}=\frac{(\operatorname{Hess}_g h)_{ij}}{\nu}.
 \tag{G.9}
$$

共享完整两 jet 及 $g,\partial g$ 给同一第二基本形式。Gauss 分解

$$
 F_{ij}=\Gamma^k_{ij}F_k+\mathrm{II}_{ij}n
 \tag{G.10}
$$

于是给相同的全部二阶空间偏导。证毕。

引理要求的空间位置等式不能由两个 mean 导数等式取代；切口的转角及位置
周期按 R30/R32 处理。纯高度候选即使精确解了完整 mean 根，只要
$\mathcal J\ne0$，其 $g-d\widehat h^2$ 尚不能直接当平直度量展开为上述等距浸入。
因此 carrier 的候选 $C^2$ 与最终曲面 $C^2$ 是两个不同的已付/未付层次。

## 4. 可直接接 Green 误差的主曲率门

这一步只需要真实高度误差，不需要先对全域水平图 Hessian 设过强阈值。
对任何高度函数 $h$ 定义

$$
 v(h)=\left(\frac{h_r}{\sqrt E},\frac{h_\theta}r\right),\qquad
 \mathcal H(h)=
 \begin{pmatrix}
 (h_{rr}-E'h_r/(2E))/E&
 (h_{r\theta}-h_\theta/r)/(r\sqrt E)\\
 (h_{r\theta}-h_\theta/r)/(r\sqrt E)&
 h_{\theta\theta}/r^2+h_r/(Er)
 \end{pmatrix}.
 \tag{G.11}
$$

假设 $h$ 是待验证的真实等距高度，$\widehat h$ 是当前完整候选，且已获得同一
整叶上的

$$
 \|v(h)-v(\widehat h)\|_2\le e_1,\quad
 \|\mathcal H(h)-\mathcal H(\widehat h)\|_{\rm op}\le e_2,\quad
 \max(\|v(h)\|_2,\|v(\widehat h)\|_2)\le\rho_*<1.
 \tag{G.12}
$$

令 $\nu_*=\sqrt{1-\rho_*^2}$、$\widehat\nu=\sqrt{1-|v(\widehat h)|^2}$、
$\widehat K=\|\mathcal H(\widehat h)\|_{\rm op}/\widehat\nu$。
则真实主曲率满足

$$
 \boxed{\max_i|\kappa_i(h)|
 \le \widehat K+\frac{e_2}{\nu_*}
 +\frac{\rho_*\,\|\mathcal H(\widehat h)\|_{\rm op}}{\nu_*^3}e_1.}
 \tag{G.13}
$$

**证明。** $|\nu-\widehat\nu|\le\rho_*e_1/\nu_*$，从而
$|1/\nu-1/\widehat\nu|\le\rho_*e_1/\nu_*^3$。对
$\mathcal H(h)/\nu-\mathcal H(\widehat h)/\widehat\nu$ 使用三角不等式，
再用 R31 的真实形算子恒等式即得 (G.13)。这里 $\widehat K$ 只是已定义的
代数控制量；若候选尚无等距浸入，不称它为候选面的真实曲率。证毕。

若误差包给出实际六 jet 上界 $e_r,e_\theta,e_{rr},e_{r\theta},e_{\theta\theta}$，
则可取

$$
\begin{aligned}
e_1&=\sqrt{e_r^2/E+e_\theta^2/r^2},\\
A&=(e_{rr}+|E'|e_r/(2E))/E,\\
B&=(e_{r\theta}+e_\theta/r)/(r\sqrt E),\\
C&=e_{\theta\theta}/r^2+e_r/(Er),\qquad e_2=\max(A,C)+B .
\end{aligned}
\tag{G.14}
$$

区间中按分母正下端取界。mean 的 $e_r,e_{rr}$ 和无限高频导数不能省略。
没有 R58/R90 等内头真解与外头两点系统的一致接合和实际误差半径时，
(G.13) 仍是条件接口。

## 5. 握持量与全曲面直径的误差预算

设已有同一紧材料面上的连续族 $F_t,\widehat F_t$，并已证明全 $t$、全材料点
的真实空间误差 $\|F_t-\widehat F_t\|_\infty\le e_0$。这里必须是空间映射误差；
高度标量误差不单独控制水平展开或刚体规范。则

$$
 |D-\widehat D|\le2e_0,\qquad
 |\operatorname{diam}F_0(H)-\operatorname{diam}\widehat F_0(H)|\le2e_0,
 \tag{G.15}
$$

$$
 |\delta_{\rm hold}-\widehat\delta_{\rm hold}|\le2e_0,\qquad
 |\delta_{\rm E}-\widehat\delta_{\rm E}|\le2e_0.
 \tag{G.16}
$$

**证明。** 相应像集的 Hausdorff 距离至多 $e_0$。Hausdorff 距离的三角不等式
给每个 $t$ 的二个端集误差至多 $2e_0$；再取最大值即得握持量界。
对任意 $A\in\mathrm E(3)$，$A$ 保持同一 Hausdorff 误差，
先对 $A$ 取下确界再对 $t$ 取最大值得欧氏取商量界。直径界由每一对材料点的
距离误差至多 $2e_0$ 直接得到。证毕。

因此若已有真正的固定握持区 $F_t|_H=F_0|_H$，以下充分门符合本课题定义：

$$
\begin{aligned}
 \widehat{\operatorname{diam}H}_{\rm lower}-2e_0
    &\ge \tfrac15(\widehat D_{\rm upper}+2e_0),\\
 \widehat\delta_{{\rm hold},{\rm lower}}-2e_0
    &\ge \tfrac15(\widehat D_{\rm upper}+2e_0),\\
 \widehat\delta_{{\rm E},{\rm lower}}-2e_0&>0.
\end{aligned}
\tag{G.17}
$$

固定性本身不由小误差推出。R32 的物理相位作用在真实平 cuff 上逐材料点固定，
可支付这一条件；候选插值的相位协变只支付相应高度的结构，不自动支付整个
闭面、握持区直径或非全等量。

## 6. reach 的连续空间接口

主曲率界是必要的局部门，还需全局成对条件。选择
$\tau\ge0.03(\widehat D_{\rm upper}+2e_0)$。
对真正连续的参考空间块及定向法向，假设每个有序点对有

$$
 \ell\le|\widehat q-\widehat p|\le u,\quad
 |\widehat n_p\cdot(\widehat q-\widehat p)|\le b,\quad
 |p-\widehat p|\le e_p,\quad |q-\widehat q|\le e_q,\quad
 |n_p-\widehat n_p|\le e_n.
 \tag{G.18}
$$

置 $e=e_p+e_q$。若 $\ell>e$ 且

$$
 \boxed{(\ell-e)^2\ge2\tau(b+e_nu+e),}
 \tag{G.19}
$$

则该有序点对满足 $2\tau|n_p\cdot(q-p)|\le|q-p|^2$。
证明只是 $|q-p|\ge\ell-e$ 及
$|n_p\cdot(q-p)|\le b+e_nu+e$。对交换后的有序点对也须使用其法向界。
近对角处不应强行使用带固定 $e$ 的 (G.19)；可用 R16/R37 的真实曲率与
内蕴局部覆盖。尾图内部可在支付 R32、R31 和 R27 后使用 R25 整图延拓。
不同片及标记混合点对仍用 R11/R62 的全相位门，而非相位采样。

若实际映射导数误差也已付，设
$|F_r-\widehat F_r|\le d_r$、$|F_\theta-\widehat F_\theta|\le d_\theta$，
$|\widehat F_r\times\widehat F_\theta|\ge\zeta>0$。因为真实等距映入有
$|F_\theta|=r$、$|F_r|=\sqrt E$，可取

$$
 e_\times=r d_r+(\sqrt E+d_r)d_\theta,\qquad
 e_n\le\frac{2e_\times}{r\sqrt E+\zeta}.
 \tag{G.20}
$$

归一化向量不等式
$|a/|a|-b/|b||\le2|a-b|/(|a|+|b|)$ 及叉积差恒等式证明此式。
共同法向必须取对应的同一方向。源高度的两个导数误差不是 (G.20) 的映射
导数误差；水平标架和位置的真实积分仍要给出。

## 7. 四步完成后的最小实际执行计划

1. 先保持 PM、PA、CA、CF 和比较器的现数学源不变，等待每项真实退出及
   全覆盖/完整 mean/J/R77 门。首子段外另七段不自动启动。
2. 比较器读取两个正式 primary，分别报告两个不同候选的全段上界、完整谱
   和连续叶 Fourier 下界，不跨候选取逐点最小。
3. 独立 stdlib/Fraction consumer 按 (part,panel,x_left,x_right) 配对 PM、PA、CF。
   核完整 header/trailer、所有 SHA、真实同一分割和共享端点。读取 (G.4)
   五矩中的两项，实际付 (G.6) 及 (G.7) 的六 jet 差上界和每个前缀 mean 偏移。
   使用 directed dyadic 有理端点，不新建 Arb/ODE/Node。
4. 当且仅当采用新首子段时，保留新的 mean 常数传播记录，并把该函数明确
   替换进全段候选身份；完整外 Green/Schur 的源、边界及非线性误差均使用
   这个同一候选。原候选和已付真实残差下界单列保全。
5. 得到真外解后的完整误差半径，再消费 (G.13) 曲率和 (G.15)–(G.20) 的空间
   几何门。真实 Cartesian 切口迹与 R27 的高正则角导要求仍须逐项支付；
   source $r,\theta$ 不直接充当 Cartesian 极径/极角。
6. 当前未给出新的 $e_0,e_n,e_1,e_2$ 数值，也未宣称 reach、握持幅度或本题完成。
   本文只将剩余量精确列成可执行接口，避免以小候选缺陷代替它们。

引用的完整已证明工具：
[R30](../results/R30-source-cut-to-cartesian-boundary-traces.md)、
[R31](../results/R31-complete-height-curvature-transfer.md)、
[R32](../results/R32-height-development-and-global-tail-graph.md)、
[R25](../results/R25-entire-graph-curvature-and-reach.md)、
[R27](../results/R27-explicit-star-shaped-graph-extension.md)、
[R64](../results/R64-general-outer-mean-and-compatible-defect.md)、
[R75](../results/R75-complete-mean-transport-and-shear-constraint.md)、
[R77](../results/R77-complete-mean-defect-zero-mode.md)。
