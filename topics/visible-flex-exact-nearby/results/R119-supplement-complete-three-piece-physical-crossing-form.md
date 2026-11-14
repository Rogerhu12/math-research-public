# R119 续篇：负—正—负三段的真实共同方向与完整物理 crossing

2026-11-14，visible-exact / tail_connector（0df957a82d09）。

**状态：已证明。** 对第76束同一个完整正片和两侧负窗，本文把两个已付负窗型补成沿一个真实共同 profile 方向的三段 crossing：计入一个窗口控制在另一窗口的全部联合背景及两列 $D\Gamma^*$ 响应，计入正片内部的参数型，并支付两张 KAM 端角的参数导数。两个内根的物理边界 pairing 准确相消。对原零 mean 低频 incoming 包，这个三段型仍有严格正下界。

本篇固定原内部标签、材料坐标、fixed-stop 和实际腰尺度。它不微分外好参数的重新选择，也不把三段以外的网络响应填0。尚未证明任意 whole-network 近核的 incoming 满足本篇的低包条件。ordinary/weak 源的准确附加项在末节保留；齐次 crossing 下界不冒充全源逆。

## 1. 当前对象、统一符号与要证明的型

采用[第76束](R119-supplement-positive-Cayley-packets-to-complete-center-forms.md)的实际正片 $I$、左右负窗 $I_-,I_+$、物理根—中心 map 和完整两端 Cayley graph。记
$$
j\ge8193,\quad J=j+5,\quad\delta=\delta_j,\quad
\mathcal X\le2^{-1048576},\quad
\mathcal N=\mathcal N_j^{\rm pair}
 <2^{-19500}2^{-\alpha(j-8193)},\quad\alpha=31867/256.
\tag{T.1}
$$
正片的两个端点与相邻负窗仍使用各自真实 $b_e,\mu_{0,e},K_e$。原 $\zeta,h,b_m$、邻胞规范接缝和物理源单位均不改。

两窗分别用第73—74束的同一个全低锥方向 $\psi_e$。它们支集互不相交，且在各自 $C_x^4$ 范数中不超过1；每个方向已经对本窗两个实际 radial phase 做 annihilation。沿未缩放的共同方向
$$
\dot\Xi_- =\psi_-,\qquad \dot\Xi_+=\psi_+,
\qquad\dot\Xi_i=0\ (i\ne-,+)
\tag{T.2}
$$
取第55束准确的联合 $\Gamma^*(\mathbf a,\Omega)$ 及实际全频背景导数。不是把 $\Gamma$ 固定后再称为联合导数。

设正片 incoming 为 $a$，满足
$$
a_0=0,\qquad a_m=0\quad(|m|>L_0),\qquad
L_0=\tfrac14\min(\sqrt{B_-},\sqrt{B_+}).
\tag{T.3}
$$
这只限制 incoming；真实 outgoing、两条物理迹和两个 mean 输出不截断。在正片取真正齐次解，再按物理 height/total flux 向两侧负窗作齐次延拓。两中心的常物理高度商代表仍记为 $Z=\mathcal B a$。

第76束已经证明
$$
\|Z_<\|\ge(2K_j)^{-1}\|a\|_2,\qquad
\|Z_>\|_{\mathscr H^4\oplus\mathscr H^4}<\chi_j\|Z_<\|,
\tag{T.4}
$$
其中
$$
K_j=2^{8300}J^{15}\delta^{-26},\qquad
\chi_j=2^{-12800}J^{-42}\delta^{38}.
$$
这些是两个中心一起的界，不要求其中任何一个单独承载固定比例的质量。

本篇的三段型 $\mathfrak Q_{I_-\cup I\cup I_+}$ 是共同方向 (T.2) 对这三个实际 Jacobi 散度系数的积分变分，等价于第7节两个最外物理根的 crossing。结论是
$$
\boxed{\quad
\mathfrak Q_{I_-\cup I\cup I_+}(a)
>2^{-25800}J^{-94}\delta^{57}\|a\|_2^2 .\quad}
\tag{T.5}
$$

## 2. 联合参数的局部偏差，而非全局行和的粗替代

需要一个在任意深层都可消费的异窗参数界。对完整负分量 $i$，按[第69束](R119-supplement-actual-two-phase-compact-response-and-complete-pocket-form.md)记
$$
\mathcal W_i=J_i^4\delta_i^{-6}\mathcal N_i.
$$
令 $\bar\Gamma_i(\Omega)$ 为第54束真实 radial 两相位补偿，$\Gamma_i^*(\mathbf a,\Omega)$ 为第55束联合选择。其整个已给 profile 复球中都有
$$
\boxed{\quad
|\Gamma_i^*(\mathbf a,\Omega)-\bar\Gamma_i(\Omega)|_1
<2^{160}\mathcal W_i\mathcal X .\quad}
\tag{T.6}
$$

证明逐行使用原方程。第55束 (N.9) 给
$$
|\gamma_{1,i}^*-\chi_i(q_i,\Omega)|
<2^{39}J_i\sqrt{j_i}\,\delta_i^{-3/4}\mathcal N_i\mathcal X.
$$
第54束 (H.10)—(H.12) 在整个原复参数盒给
$\|D_\gamma(\beta_i(0,\Gamma,\Omega)/\sqrt{B_i})\|<4$；这也直接来自其显示的 $\|D\mathsf F\|<4$。第55束 (N.11) 的非径向首密度差除以 $\sqrt{B_i}>1$ 后不会增大。因此同篇准确第二行中的 $E_i$ 满足
$$
|E_i|<2^{145}J_i^3\delta_i^{-5}\mathcal N_i\mathcal X.
$$
原逆 $q_i=\varphi_i(-E_i)$ 有 $\varphi_i(0)=0$、$|\varphi_i'|<2^{10}$，所以 $|q_i|<2^{155}J_i^3\delta_i^{-5}\mathcal N_i\mathcal X$。再用 $|\partial_q\chi_i|<2$，两坐标差的和小于 $3|q_i|+|\gamma_{1,i}^*-\chi_i|$，严格小于 (T.6)。整个无限联立固定点已由原全局收缩构造；这里没有用一个局部形式方程另造解。

所有当前 compact 形状的 $\ell^\infty(C^4)$ 范数小于 $2^{-79}$。沿 (T.2) 或任一单独方向取复半径
$$
R=2^{-68};\qquad 2^{-79}+2R<2^{-64}.
\tag{T.7}
$$
它严格包含于第54—55束已经构造的真实联合域。对纯形状变化不移动径向接缝，固定材料截面的全频背景也是该域中的全纯 map。这里不声称外好参数的逐点选择全纯。

若只开启另一个窗口的 $\psi_{e'}$，$e'\ne e$，径向 phase 的严格支集分离给
$D_{\psi_{e'}}\bar\Gamma_e=0$ **准确成立**。Cauchy 作用于 (T.6) 的差，且相邻尺度给
$\mathcal W_e\le2^{10}J^4\delta^{-6}\mathcal N$，从而
$$
\boxed{\quad
|D_{\psi_{e'}}\Gamma_e^*|_1
<2^{240}J^4\delta^{-6}\mathcal N\mathcal X .\quad}
\tag{T.8}
$$
未放宽的常数是 $2^{160+10+68}=2^{238}$。这个界保留两列以及所有层进入联立选择的响应；没有把 $D\Gamma^*$ 当作对角矩阵。

## 3. 异窗完整物理核的参数费用

在窗口 $e$ 中，控制 $\psi_{e'}$ 没有直接 compact 项，其实际 log-profile 方向只是本窗两个原 bump 乘 (T.8) 的系数，记为 $\Psi_{e\leftarrow e'}$。每个原 bump 的幅度小于1，故
$$
\int_{I_e}|\Psi_{e\leftarrow e'}|dt
\le |D_{\psi_{e'}}\Gamma_e^*|_1.
$$
当前实际相对背景 $z/w=(p/w,k/w)$ 的完整角二阶范数在 (T.7) 的复盘中小于 $4\mathcal N\mathcal X$。Cauchy 给
$$
\|D_{\psi_{e'}}(z/w)\|_{\mathcal A_2^2}
<2^{70}\mathcal N\mathcal X.
$$
完整 gauged 响应仍是
$\widehat z=\dot z-\Psi_{e\leftarrow e'}F_1$。准确转换为
$$
\widehat z/w=D(z/w)
 +\Psi_{e\leftarrow e'}(z/w-F_1/w).
$$
第59/69束的完整有理式给括号范数小于 $2^8(4\mathcal N\mathcal X)$。结合 (T.8)，且 $\mathcal N\mathcal X<1$，可统一取
$$
\boxed{\quad
\int_{I_e}|\Psi_{e\leftarrow e'}|dt
 +\sup_{I_e}\widehat n_{e\leftarrow e'}
<2^{300}J^4\delta^{-6}\mathcal N\mathcal X .\quad}
\tag{T.9}
$$
它针对原物理梯度归一，不含一个隐藏的 $w_{\max}/w_{\min}$。这次使用完整 profile 复球，未把有支集长度收益的旧 $P_j\rho^5$ 界粗暴丢掉 $\rho^5$ 后推广到无限深层。

对 (T.4) 的真实数据，第74束 (E.10)、(E.17) 经相邻层比较分别给
$$
\sum_e\sup_{I_e}E_{{\rm strong},e}(Y_{e,<})
<2^{8540}J^{20}\delta^{-34}\|Z_<\|^2,
$$
$$
\sum_e\sup_{I_e}E_{{\rm strong},e}(Y_{e,>})
<2^{8600}J^{16}\delta^{-30}\|Z_>\|_{\mathscr H^4\oplus\mathscr H^4}^2.
$$
完整传播线性，$E(Y_<+Y_>)\le2E(Y_<)+2E(Y_>)$；用 (T.4) 后
$$
\sum_e\sup_{I_e}E_{{\rm strong},e}(Y_e)
<2^{8700}J^{20}\delta^{-34}\|Z_<\|^2.
\tag{T.10}
$$
这保留两锥、无限高输出及两个 flux mean，不用每个窗口各自的质量下界。

第74束已付的完整核界为
$|\mathcal K_{\rm act}|\le2^{40}E_{\rm strong}$、
$|\mathcal H_{\widehat z}|\le2^{24}\widehat nE_{
\rm strong}$，后者用含 $Q$ 的物理能量，并不在根处除 $Q$。因此两个异窗项一起满足
$$
\boxed{\quad
|\mathfrak Q_{-\leftarrow+}(Y_-)
 +\mathfrak Q_{+\leftarrow-}(Y_+)|
<2^{9200}J^{24}\delta^{-40}\mathcal N\mathcal X\|Z_<\|^2 .\quad}
\tag{T.11}
$$
在放宽前 $300+8700+40+2=9042$ bits 已覆盖两项和。原同窗型中的 radial 补偿与实际反馈没有再算作异窗小量，也未重复扣除。

## 4. 正片完整 Cayley 对共同方向的真导数

本节始终使用第76束的**参考归一**完整双端 Cayley $\mathcal C_a$，未加第48束的实际根 frame。固定材料坐标与腰尺度后，负窗 compact 及两个补偿 bump 均远离正片，所以正片径向参考 $A,\mu_0,b_e,\ell_{0,e},W_e$ 对 (T.2) 准确不变；其径向 $\mathcal C_0$ 也不变。实际背景与两端角依然变化。

第76束 (A.8)、(A.10) 的比较在复盘 (T.7) 中继续成立。理由是：真实 drift 和光学插值仍用相同的完整商式；正片篇 (C.7)—(C.12) 的复 form 差只用这些商式的绝对值界。把该差插入 (C.19) 的两个参考 resolvent，原 $4\epsilon_j<1/2$ 的 Neumann 门统一保留。因此取得的是全纯有界算子族，未把复参数的 Cayley 声称为 unitary。只有当前实参数使用真正的 unitarity。

对 $|s|\le4$，对这个实际族使用 Cauchy 便给
$$
\|\dot{\mathcal C}_a:H^s(I\text{ 两端})\to H^s(I\text{ 两端})\|
<2^{280}J^2\delta^{-2}\mathcal N\mathcal X,
\tag{T.12}
$$
$$
\|\dot K_e\|_{\mathcal A_{1/4}}
 +\|\dot K'_e\|_{\mathcal A_{1/4}}
<2^{180}J^2\delta^{-1}\mathcal N\mathcal X.
\tag{T.13}
$$
直接 Cauchy 常数分别是 $2^{200+68}$ 和 $2^{100+68}$；显示界保留额外余量。两端 off-diagonal transmission 块、mean 和所有 angular lag 全包含在 (T.12) 中。

## 5. 端角导数与真实正片边界 pairing

现仅在正片使用 outward 通量，故第76束 (A.11) 的两端符号都取 $+1$；负窗材料正向符号留到下一节再转换。写该完整真实变换为 $\mathcal T_K$。它在积分 pairing 下 symplectic：height 使用 $C_{K^{-1}}$，通量先乘 $1/K'$ 再复合，$d\theta=K'd\eta$ 准确消去密度因子；其参考 shear 是实自伴乘子。径向 $V,W,b,\mu_0$ 在本方向固定。

对固定光滑输入，真实逆图满足
$\dot K^{-1}=-(\dot K/K')\circ K^{-1}$。微分第76束 (A.11) 的三个非零块，使用其 (A.14) 同一个强复合公式及到六阶的已付链式费用，得到
$$
\|\dot{\mathcal T}_K:H^{s+1}\oplus H^{s+1}
                          \to H^s\oplus H^s\|
<2^{160}\sqrt{b_e}
(\|\dot K_e\|_{\mathcal A_{1/4}}+
  \|\dot K'_e\|_{\mathcal A_{1/4}}).
\tag{T.14}
$$
这个强导数损一阶角导；没有把 $C_K$ 写成同阶 norm 可微。第76束的 $\sqrt{b_e}<2^{12}J^{1/4}\delta^{-9/8}$、(T.13) 给
$$
\|\dot{\mathcal T}_K:H^1\to H^0\|
<2^{380}J^3\delta^{-3}\mathcal N\mathcal X,
$$
$$
\|\mathcal T_K^{-1}\dot{\mathcal T}_K:H^1\to H^0\|
<2^{500}J^4\delta^{-5}\mathcal N\mathcal X.
\tag{T.15}
$$
第二式使用同一当前 $\|\mathcal T_K^{-1}\|<2^{120}J\delta^{-2}$。这些 norm 是两个端点的直和，均包含 mean。

令 $b=\mathcal C_a a$、$Y_h=(a+b)/\sqrt2$、$Y_p=(b-a)/(i\sqrt2)$，微分时固定 incoming $a$。采用内积对第二个变量线性以及
$\Omega(Y,Z)=\langle Y,\mathsf JZ\rangle$。直接展开给准确恒等式
$$
\Omega(Y,\dot Y)=\langle a,-i\mathcal C_a^*\dot{\mathcal C}_a a\rangle.
\tag{T.16}
$$
在物理平衡状态 $x=\mathcal T_KY$ 中，symplectic 性给完整的
$$
\Omega(x,\dot x)=
\langle a,-i\mathcal C_a^*\dot{\mathcal C}_a a\rangle
 +\Omega(Y,\mathcal T_K^{-1}\dot{\mathcal T}_KY).
\tag{T.17}
$$
第二项是原 principal 端角的真实导数，不能删去。参考 normal shear 的导数在此固定 germ 上准确为0；实际密度/shear 已通过参考归一 DN 和完整物理通量保留，不再另添一张实际 root frame。

对 (T.3)，$\|Y\|_0=\sqrt2\|a\|_0$、$\|Y\|_{H^1}<4\|a\|_{H^1}$，而
$$
\|a\|_{H^1}\le\sqrt{B_{\max}}\|a\|_0
<2^{10}J\delta^{-1}\|a\|_0.
$$
故 (T.12)、(T.15)—(T.17) 给正片的**全部**物理参数型
$$
\boxed{\quad
|\mathfrak Q_I(a)|
<2^{520}J^5\delta^{-6}\mathcal N\mathcal X\|a\|_2^2 .\quad}
\tag{T.18}
$$
未放宽的 frame 项常数小于 $2^{513}$。由正片真实 Green identity，(T.17) 的两端和准确等于 $\int_I\nabla\overline h\cdot\dot G\nabla h$：微分齐次弱方程后，与原方程配对相减，所有 $\dot h$ 的内部项相消。该证明只用已经构造的完整正型 form，未在转向根处估计一个无界的 $\dot d/\sqrt A$。

## 6. 同一个尺度上的三项相加

第76束的两个**同窗**型之和满足
$$
\mathfrak P(Z)\ge
\left(\tfrac18-2^{-200}\right)d_*\|Z_<\|^2
>\frac{d_*}{16}\|Z_<\|^2,
\qquad d_*=2^{-9100}J^{-64}\delta^5.
\tag{T.19}
$$
由 (T.4)，正片项 (T.18) 的绝对值除以 $d_*\|Z_<\|^2$ 小于
$$
2^{26400}J^{99}\delta^{-63}\mathcal N\mathcal X<2^{-20}.
\tag{T.20}
$$
实际未放宽的指数为 $520+2+2\cdot8300+9100=26222$。异窗项 (T.11) 的同一比值小于
$$
2^{18300}J^{88}\delta^{-45}\mathcal N\mathcal X<2^{-20}.
\tag{T.21}
$$
这两条是全深尾界：在首层，使用 $J<2^{14}$、$\delta^{-1}<2^{8197}$，两比值的二进制上界分别为 $-523879,-679679$。随后
$((j+6)/(j+5))^{99}<65/64$、$(65/64)^{32}<2$；指数 $\alpha-63-1/32>61$，分别保证至少61及79 bits 的逐层衰减。这里没有以首层检查替代无限尾。

共同方向的三段型准确等于
$$
\mathfrak Q_{I_-\cup I\cup I_+}(a)
=\mathfrak P(Z)+\mathfrak Q_{-\leftarrow+}(Y_-)
 +\mathfrak Q_{+\leftarrow-}(Y_+)+\mathfrak Q_I(a).
\tag{T.22}
$$
用 (T.19)—(T.21) 得
$$
\mathfrak Q_{I_-\cup I\cup I_+}(a)
>\frac{d_*}{32}\|Z_<\|^2
\ge\frac{d_*}{128K_j^2}\|a\|_2^2.
$$
最后的未放宽常数是 $2^{-25707}J^{-94}\delta^{57}$，从而证明 (T.5)。这是真实多频包与两端任意比例的整体型，不是逐模正型的重新命名。

## 7. 两个内根的准确消项与原允许参数盒

对每个负窗，第61束完整 canonical 恒等式给
$$
[\Omega((h,\pi),(\dot h,\dot\pi))]_{\partial I_e}
=\int_{I_e}(\Psi_{\rm tot}\mathcal K_{
\rm act}-\mathcal H_{\widehat z_{\rm tot}})dt.
\tag{T.23}
$$
所有 compact 和补偿 bump 都在根 germ 外，故端点 local gauge 剪切为0。正片使用其 outward 总通量；负窗使用其材料正向总通量并按左负右正取边界差。在每个内根，$h,\pi$ 的实际连续关系及其参数导数都保留，正片 outward 通量恰是相邻负窗 outward 通量的负值。因此两个内根的完整 $h\dot\pi-\pi\dot h$ pairing 两两相消，留下三段最外两个物理根的 crossing。

这个消项是在原物理迹上完成的。若改用 KAM/Airy 端口，则必须同时带回 (T.17) 的角图项，才得到相同的物理表达式；单独把内部 Cayley 生成元相加会漏项。固定物理高度常数仍是准确 null 方向，但由正片产生的 flux mean 保持在全部式中。

未缩放方向 (T.2) 可以在第74束原有限参数盒内实际实现。选两窗各一个仍可用的 anchor 坐标，其真实幅度为
$u_e=r_{a,e}/N_{a,e}>0$；取 $u_* =\min(u_-,u_+)$。当所选两个坐标的当前绝对值不超过 $1/2$，沿
$$
\theta_e(s)=\theta_e(0)+\frac{u_*}{2u_e}s,
\qquad -1\le s\le1,
\tag{T.24}
$$
其它坐标固定，始终留在原 $|\theta_e|\le1$ 盒中，并有
$d\Xi/ds=(u_*/2)(\psi_-+\psi_+)$。所以该原坐标路径的实际 crossing 下界是 (T.5) 右边乘 $u_*/2$。并未放大 $r_a$、合并全部原独立参数或另给一个免费的共同坐标。

## 8. 全部源、尺度与剩余全网量词

本篇 (T.5) 是齐次三段定理。源不能通过“相同配对”而消失。对第61束完整物理总通量系统
$$
Y_t=\mathsf AY+s,\qquad
s=(-\mu^{-1}F^t,\ g-\partial_\theta(F^\theta+dF^t)),
$$
及 $\widehat{\dot Y}=\dot Y-\Psi\mathsf BY$，准确源恒等式为
$$
\partial_t\Omega(Y,\widehat{\dot Y})
=\Psi\mathcal K_{\rm act}-\mathcal H_{\widehat z}
 +\Omega(s,\widehat{\dot Y})+\Omega(Y,\widehat s_\Psi),
\qquad\widehat s_\Psi=\dot s-\Psi\mathsf Bs.
\tag{T.25}
$$
这里 $\widehat s_\Psi$ 必须按同篇 (J.26) 的完整两行读取，保留 ordinary 源导数、weak 源导数、$\dot dF^t$ 和 $-\Psi L_c(\mu^{-1}F^t)$。它不要求 $F_t^t$。源只在正片时，其原两端仿射 $g_{\mathcal F}$ 和到两中心的 (A.28)—(A.30) 费用仍有效；负窗也有源时，须加入其真实有序 Duhamel 列，不能把 (T.25) 的两个源 pairing 设0。裸通量另外为 $\pi-F^t$，两端的 $F_e^t,\dot F_e^t$ 仍需输入空间提供实际迹。

两个 mean 继续满足 $(\pi_0)_t=g_0$ 与
$(h_0)_t=\langle dh_\theta+\mu^{-1}\pi-\mu^{-1}F^t\rangle$，只有一个全局高度常数。本文没有从源空间删除任何 mean。

固定的物理腰尺度保证本篇的 log-profile 核与第69—74束同单位。若继续对外 connector 的停止尺度或移动物理 cut 求导，必须另加真实 $\delta\mu_0/\mu_0$、$\dot Q$、$A\,\delta\ell$ 和 $w_e\delta a_e$，并使用第53束 (C.50) 后的一般变分式。本文未对外好参数的选择授予可微性。

三段以外，(T.2) 仍通过联合背景及 $\Gamma^*$ 影响其余网络块；本篇没有给那些块加零。还必须证明真实网络近核的 incoming 频率定位、将余下外部响应与它们的状态质量一起支付，随后才可能消费一个全网 Schur 逆。原 source-to-label 空间和完整非线性 $\mathcal F=0$ 均仍是后续实质任务。

新增恒等式与预算见[源码](../scripts/fourfold_complete_three_piece_crossing_20261114.py)及[实际记录](../notes/2026-11-14-R119-complete-three-piece-crossing-budget.json)。其核验只检查本文显示的精确代数与有理费用；不会把这些检查称为一个已求得的全网解。
