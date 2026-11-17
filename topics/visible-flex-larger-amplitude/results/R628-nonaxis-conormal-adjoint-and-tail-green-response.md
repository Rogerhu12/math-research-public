# R628 — 非轴 Darboux 共法向、伴随与尾边界 Green 读出

作者：parallel-model / GPT-6 Astra Pro，AI-assisted。日期：2026-11-17。

**状态：下述连续恒等式和条件误差公式有完整证明；尚无新的闭面或新数值误差常数。** 本文支持新的完整零模低阶尾 BVP：把深端 Robin/稳定图误差转换成浅端 DN 误差时，使用真实边值 Jacobi/伴随场，避免以巨大的单向 Cauchy 增益代替边值响应。

[R29](../results/R29-real-head-columns-and-boundary-green-envelope.md)、R65、R84 等已处理轴对称线性背景的逐模 Wronskian；[R419](../results/R419-correlated-nominal-Robin-row-formation-with-complete-family-errors.md) 已处理齐次 Robin 行的方向与表示误差。本文新增的是**一般非轴高度中心的完整共法向、非精确中心的缺陷项与真实伴随边界，以及可以用当前有限 BVP 响应近似并检验的全频耦合公式**。R75 的均值输运是其中一个零模特例，不另行重报。

## 1. 同一个几何 Darboux 算子

取一个定向二维 Riemannian 环带 $(A,g)$，高度候选 $h$ 足够光滑，且

$$
\nu^2=1-|\nabla_g h|_g^2>0.
$$

记 $H=\nabla_g^2h$ 为 Hessian 的 $(1,1)$ 形式，$\kappa=K_g$，以及

$$
\mathscr D(h)=\det H-\kappa\nu^2=:\varepsilon.
\tag{1.1}
$$

这是 R44.28 的同一个内蕴缺陷，未乘另一个坐标行列式。Darboux 方程的标准形式及 cofactor 张量的曲率散度可参看 Khuri, *On the Local Solvability of Darboux's Equation*, DCDS Supplement 2009, 451–456，公式(1)、证明中的 $b^{ij}$：[作者公开原文](https://www.math.stonybrook.edu/~khuri/Khuri_AIMS_Darboux.pdf)。本文以下权重与误差公式全部在这里推导，不把它们作为该文的引用结论。

令对称反变张量

$$
C^{ij}=(\Delta_g h)g^{ij}-h^{;ij}.
\tag{1.2}
$$

它是二维 Hessian 的 cofactor；不要求 Hessian 可逆。固定 $g$ 的准确线性化为

$$
L_hv=C^{ij}v_{;ij}+2\kappa\langle\nabla h,\nabla v\rangle_g.
\tag{1.3}
$$

本节的经典推导可先取 $g,h,v$ 光滑。只要所列散度和边界迹有意义，就可按通常积分分部形式使用；下文不把一个仅有离散节点的场自动当作此类连续对象。

## 2. 一般候选的准确散度式

置 $\omega=\nu^{-3}$。则对任意 $v$，

$$
\boxed{
\operatorname{div}_g(\omega C\nabla v)
=\omega L_hv+3\varepsilon\nu^{-5}
                       \langle\nabla h,\nabla v\rangle_g.}
\tag{2.1}
$$

**证明。** Ricci 换序在二维给

$$
\nabla_iC^{ij}=-\kappa h^{;j}.
\tag{2.2}
$$

它也可从 $C=(\Delta h)g^{-1}-\operatorname{Hess}h$ 和
$\operatorname{div}\operatorname{Hess}h=\nabla\Delta h+\operatorname{Ric}(\nabla h)$ 直接得到；二维 $\operatorname{Ric}=\kappa g$。另一方面

$$
\nabla\log\omega=3\nu^{-2}H\nabla h,
\qquad CH=(\det H)I.
$$

因此

$$
\omega^{-1}\operatorname{div}(\omega C\nabla v)
=C^{ij}v_{;ij}
 +\left(-\kappa+3\frac{\det H}{\nu^2}\right)
            \langle\nabla h,\nabla v\rangle.
$$

用 $\det H=\kappa\nu^2+\varepsilon$，括号化为
$2\kappa+3\varepsilon/\nu^2$，即 (2.1)。证毕。

所以准确 Darboux 中心 $\varepsilon=0$ 的线性化对权体积 $\omega\,dV_g$ 形式自伴，曲率改变符号不影响该代数事实。**形式自伴不保证椭圆性、边值可解性或正能量。** 对非精确中心，(2.1) 的最后一项必须保留。

## 3. 原 $(P,K)$ 尾坐标中的共法向密度

现在取原背景

$$
g=E(r)dr^2+r^2d\theta^2,\qquad E=1+w^2,
$$

且 $h$ 是一个真实兼容高度。沿 R64/R75 的记号，

$$
P=\frac{h_\theta}{rw},\quad K=\frac{h_r}{w}-1,
\quad z=w^2,\quad T=P_\theta,\quad U=K_\theta-P,
$$
$$
L=1+K+ET,\quad D=E(1-zP^2)-z(1+K)^2,
\quad W=LD^{-3/2},\quad \alpha=EU/L.
\tag{3.1}
$$

于是 $\nu^2=D/E$。对高度变化 $v$ 定义向增加 $r$ 方向的共法向**角密度**

$$
\Pi_h[v]=\sqrt{\det g}\,\omega C^{rj}\partial_jv.
\tag{3.2}
$$

边界积分是 $\int\Pi_h[v]\,d\theta$，因此不再额外乘 $r$ 或 $\sqrt E$。准确有

$$
\boxed{
\Pi_h[v]=\frac w{D^{3/2}}
 \left(Lv_r-\frac{EU}{r}v_\theta\right).}
\tag{3.3}
$$

若变化也用原归一分量

$$
p_v=\frac{v_\theta}{rw},\qquad k_v=\frac{v_r}{w},
$$

则

$$
\boxed{\Pi_h[v]=zW(k_v-\alpha p_v).}
\tag{3.4}
$$

**证明。** 坐标 Hessian 的两项为
$h_{;\theta\theta}=rwL/E$、$h_{;r\theta}=wU$，而
$C^{rr}=h_{;\theta\theta}/(Er^2)$、
$C^{r\theta}=-h_{;r\theta}/(Er^2)$。
代入 $\sqrt{\det g}=r\sqrt E$ 和 $\omega=(E/D)^{3/2}$，即得 (3.3)。再代入 $v_r=wk_v,v_\theta=rwp_v$ 得 (3.4)。证毕。

取常数测试函数1时，(3.4) 的角平均是 R75 的 $zD_Y\mathcal M[v]$。这里保留整个 $\theta$ 函数及任意两个高度变化，所以能够处理非轴中心的频率耦合。

## 4. 两个任意变化的完整 Green 恒等式

为简化常数，下文所有角括号均取 $\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f\,d\theta$，体积分同除以 $2\pi$。定义

$$
\mathfrak W_r(u,v)=\langle u\Pi_h[v]-v\Pi_h[u]\rangle.
\tag{4.1}
$$

对 $a<b$，若 $L_hu=f_u,L_hv=f_v$，则

$$
\begin{split}
\mathfrak W_b(u,v)-\mathfrak W_a(u,v)
={}&\frac1{2\pi}\int_{[a,b]\times S^1}
 \omega(uf_v-vf_u)\,dV_g\\
&+\frac1{2\pi}\int_{[a,b]\times S^1}
 3\varepsilon\nu^{-5}
 \{u\langle\nabla h,\nabla v\rangle
   -v\langle\nabla h,\nabla u\rangle\}\,dV_g.
\end{split}
\tag{4.2}
$$

**证明。** 对向量场 $\omega C(u\nabla v-v\nabla u)$ 求散度。$C$ 对称，使两个一阶交叉项相消；对其余两项用 (2.1)，再对环带积分。两条径向边界的外法向符号相反，角方向周期边界相消，给出 (4.2)。证毕。

在准确中心及两个准确 Jacobi 场上，(4.1) 对 $r$ 恒定。对非精确中心，最后一项的绝对值可直接由

$$
\frac1{2\pi}\int
3|\varepsilon|\nu^{-5}|\nabla h|
 (|u|\,|\nabla v|+|v|\,|\nabla u|)\,dV_g
\tag{4.3}
$$

控制。它不能因某个有限求解器的离散残差通过而删除。

### 兼容尾源的单位核对

若背景固定，候选高度兼容，R44 给

$$
\varepsilon=\frac z{r r_xE^2}L f_K.
$$

对兼容高度变化作真实线性化，便有

$$
L_hv=\frac z{r r_xE^2}
\{L\,\delta f_K+(k_v+E\partial_\theta p_v)f_K\}.
\tag{4.4}
$$

这里 $\delta f_K$ 是候选真实残差的导数，不是仅把投影 RHS 的 Jacobian 当成完整 PDE。体积权准确满足

$$
\omega\,dV_g=\frac{rE^2}{D^{3/2}}\,dr\,d\theta,
$$

所以 (4.2) 第一项在 source 坐标中的相应因子恰为
$zD^{-3/2}\{L\delta f_K+(k_v+E\partial_\theta p_v)f_K\}\,dx$。
没有额外 $r_x$ 或隐含的 $w^{-1}$。若变化未由同一高度产生，必须先恢复兼容高度，或直接用 (1.3) 计算 $f_v$。

## 5. 非精确中心的真实伴随与端点修正

若希望把 (4.2) 中含未知误差场的漂移项吸收到伴随算子，定义

$$
\mathcal A=\omega C,\qquad
\mathcal b=3\varepsilon\nu^{-5}\nabla h,
$$

$$
\mathcal L v=\omega L_hv
=\operatorname{div}(\mathcal A\nabla v)-\mathcal b\cdot\nabla v,
\tag{5.1}
$$

以及相对于 $dV_g$ 的形式伴随

$$
\mathcal L^*u=\operatorname{div}(\mathcal A\nabla u+\mathcal b u).
\tag{5.2}
$$

定义伴随共法向角密度

$$
\Pi_h^*[u]=\Pi_h[u]+\gamma_hu,
\qquad \gamma_h=\sqrt{\det g}\,\mathcal b^r.
\tag{5.3}
$$

在 (3.1) 的坐标中，准确为

$$
\boxed{
\gamma_h=\frac{3rE^2\varepsilon w(1+K)}{D^{5/2}}.}
\tag{5.4}
$$

**证明。** $\mathcal b^r=3\varepsilon\nu^{-5}h_r/E$，乘 $r\sqrt E$，再用 $\nu^{-5}=(E/D)^{5/2}$、$h_r=w(1+K)$，即得 (5.4)。普通乘积展开给

$$
u\mathcal Lv-v\mathcal L^*u
=\operatorname{div}
 \{u\mathcal A\nabla v-v\mathcal A\nabla u-uv\mathcal b\},
$$

故

$$
\left[\langle u\Pi_h[v]-v\Pi_h^*[u]\rangle\right]_a^b
=\frac1{2\pi}\int(u\mathcal Lv-v\mathcal L^*u)\,dV_g.
\tag{5.5}
$$

这同时证明了伴随与其边界项。证毕。

非精确中心的伴随不等于原 Jacobi 方程，也不等于只转置一个未说明离散化的 Fourier 矩阵。有限 BVP 的矩阵转置可给该**有限模型**的离散伴随；把它用于连续 (5.5)，仍须记录实际 $\mathcal L^*u$ 及角/径向积分误差。

## 6. 深 Robin 误差如何传到浅 DN

本节先采用 $a<b$ 的径向顺序；若物理深端在较大 $r$，按有向边界交换两端，符号同样随 (5.5) 处理。

设误差高度 $e$ 满足

$$
L_he=f\quad\text{在环带上},\qquad e(b,\theta)=0,
$$
$$
\Pi_h[e](a)-T e(a)=g_a.
\tag{6.1}
$$

$T$ 是一个已明确的线性深端共法向关系，可耦合全部角频；$g_a$ 是其真实边界缺陷。设对给定浅端测试高度 $\varphi$，已构造一个实际伴随场 $u_\varphi$，满足

$$
\mathcal L^*u_\varphi=0,\quad
u_\varphi(b)=\varphi,\quad
\Pi_h^*[u_\varphi](a)=T^*u_\varphi(a),
\tag{6.2}
$$

其中 $T^*$ 关于同一角平均配对定义。则

$$
\boxed{
\langle\varphi,\Pi_h[e](b)\rangle
=\langle u_\varphi(a),g_a\rangle
 +\frac1{2\pi}\int u_\varphi\,\omega f\,dV_g.}
\tag{6.3}
$$

**证明。** 对 (5.5) 取 $u=u_\varphi,v=e$。浅端 $e=0$，故浅边界项是左侧；深端用 (6.1)–(6.2)，$T/T^*$ 项准确相消，留下 $\langle u_\varphi(a),g_a\rangle$。体积分只剩 $u_\varphi\omega f$。证毕。

因此例如归一角 $L^2$ 配对给

$$
|\langle\varphi,\Pi_h[e](b)\rangle|
\le\|u_\varphi(a)\|_2\|g_a\|_2
 +\frac1{2\pi}\int|u_\varphi|\omega|f|\,dV_g.
\tag{6.4}
$$

关键量是**单位浅端 Dirichlet 伴随解在深端的实际值**。它可能很小，而单向 Cauchy 流范数很大；(6.3) 没有把二者混同。小不小、是否可求解，都必须由当前同一个 BVP 的实际响应给出。

如果只采用普通 Jacobi 场而没有做非精确中心伴随，则回到 (4.2)，保留其实际 $f_u$ 与 (4.3)。若深边界用普通 $\Pi_h[u]=Tu$ 而 $T$ 不自伴，还须保留
$\langle u,(T-T^*)e\rangle$。不能仅凭“它叫 Robin”就删除这项。

### 在浅端恢复需要的径向斜率

由于 $e(b,\theta)=0$ 对整圈成立，有 $e_\theta(b)=0$。所以 (3.3) 给

$$
e_r(b,\theta)=\frac{D(b,\theta)^{3/2}}{w(b)L(b,\theta)}
                  \Pi_h[e](b,\theta).
\tag{6.5}
$$

若最终要的是某个 Fourier 斜率系数，(6.3) 的浅端测试函数应乘上这个**实际非轴权函数**，再按相同 Fourier 归一化积分。直接把一个 conormal 模误认为同一 $K$ 模会遗漏频率耦合。

## 7. 用于非线性接合时，二阶余项有明确形式

二维行列式的二次展开给准确恒等式

$$
\mathscr D(h+e)
=\varepsilon+L_he+
\det(\nabla_g^2e)+\kappa|\nabla_ge|^2.
\tag{7.1}
$$

如果 $h+e$ 是准确高度，则 (6.3) 中的体源可取

$$
f=-\varepsilon-\det(\nabla_g^2e)-\kappa|\nabla_ge|^2.
\tag{7.2}
$$

若同一误差管内有 $\|\nabla_g^2e\|_{op}\le E_2$、
$|\nabla_ge|\le E_1$，则

$$
|f|\le |\varepsilon|+E_2^2+|\kappa|E_1^2.
\tag{7.3}
$$

这只是两个实特征值乘积的界与 (7.1)。深端准确非线性稳定图与所用线性关系之间的余项，则必须作为 $g_a$ 的组成部分。R18 的特定有理深源已给这种余项，但只有在其真实参数球、端口、角宽与度量完全一致时才能代入；不能把它继承给尚未对齐的新插值 source。

(6.3)、(7.3) 提供一个实际边界响应预算，并未单独证明整个误差管存在或闭合。需要的逆/自映条件若尚未实际计算，仍保持未完成，而不是把二阶余项直接置零。

## 8. 新低阶动态尾可立即计算的量

建议保持同一固定背景与角规范，从当前已收敛有限尾中生成以下实际输出，而不是先重建旧巨大 provider 协议：

1. 兼容高度候选 $h$、真实 $\varepsilon$、连续或加密的 $D,L$ 余量。
2. 选定少量浅端物理高度方向的有限 BVP 响应，重建成真实高度变化 $u_j$；记录其真实 $L_hu_j$，以及深端高度值与共法向。
3. 用 (4.2) 对两个响应检查浅端 conormal 响应的反对称部分：准确中心和自伴准确尾关系时该部分为0；有限中心、投影、边界和积分差额分别放进右侧。这是物理线性化检查，不等于复步 Jacobian 对有限差分的一致性检查。
4. 深度增加时，先在同一背景上把较深解限制到较浅域，计算其在旧深端的实际 $g_a$，再以 (6.3) 的同一响应读出浅端影响。只有拿到有效边界/体源界后才给真尾误差帽；连续两次 depth 数值接近本身不是无限尾证明。

当同一准确中心的内端 trace 来自固定平 cuff 的准确尾，且其变分的高度/共法向在 cuff 消失时，(4.2) 给深 trace 是 Lagrangian 的边界子空间；相应可解 Dirichlet chart 的 conormal DN 导数自伴。该结论依赖所述真实 cuff 极限，未从有限 Robin 行免费推出。

本条尚未新算上述响应，也没有证明特定深图与大幅前缀匹配。它支付的是可直接计算、正确带权且保留非精确中心项的接合误差公式。
