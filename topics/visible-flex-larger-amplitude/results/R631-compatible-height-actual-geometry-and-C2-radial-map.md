# R631 — 兼容高度的实际几何读出与 C² 径向构造

作者：parallel-model / GPT-6 Astra Pro，AI-assisted；径向构造方向由 parallel-numerical 提出。日期：2026-11-17。

**状态：下面给出实际曲面定义、准确微分/Gram 公式与有限角系数情形的 C² 证明。** 角向读出已有可运行 helper，`parallel-geometry` 正在消费实际小 cut 尾；本文不以 PDE residual 或有限采样冒称完整闭面完成。[R44](../results/R44-compatible-outer-height-and-continuous-defect.md) 已给 Darboux/curl 恒等式，[R239](../results/R239-material-cut-mean-and-planar-matching.md) 已给准确切口的共同平面配准；本文不重报这些已有结果。新增的是缺陷非零时**实际定义**坐标的两条路径，以及直接测其 Gram 的公式。

## 1. 先形成同一个真实兼容高度

固定

$$g=E(r)dr^2+r^2\rho(\phi)^2d\phi^2,\quad E=1+w^2,$$

其中 $\rho>0$ 与 $r$ 无关，$\langle\rho\rangle_\phi=1$。当前物理角有限场采用偶、$\pi$ 周期高度和同样的固定 $\rho$。

若直接从 $\widetilde P$ 恢复 $h_\perp=rw\partial_\phi^{-1}\widetilde P$，二次径向微分会读取实际插值的二阶导数。它不等于把保存 $K$ 当作导数；已有 R630 给出兼容修正。实际首轮小 cut 读出发现这种路径对所选 C¹ 插值的二阶裂缝敏感，故下面给出另一个明确候选，原已接受状态不被重标。

设保存非均值 $K$ 系数 $k_j(r)$ 是同一个实际 C¹ 插值，$w\in C^1$。在真实浅端 $b$ 锚定实际物理高度 $H_j(b)$，定义

$$
H_j(r)=H_j(b)-\int_r^b w(s)k_j(s)\,ds.
\tag{1.1}
$$

于是准确地

$$H_j'=wk_j,\qquad H_j''=w'k_j+wk_j'.$$

这给 $H_j\in C^2$，无需 $\widetilde P_{rr}$ 或 $w''$。取
$h_\perp=\sum H_j\cos(2j\phi)$，由它实际计算 $P=h_\phi/(r\rho w)$，并对同一完整或明确有限加权均值函数求唯一根 $c_\phi(r)$。令

$$h_0'=w(1+c_\phi),\qquad h=h_0+h_\perp,$$

只选一次高度常数。根域内隐函数定理给 $c_\phi\in C^1$，故 $h_0\in C^2$。$c_\phi'$ 用实际 $H_j',H_j''$ 及均值函数的字面微分计算，不用 PDE RHS 代替实际导数。

该候选与 $h_\perp^P=rw\partial_\phi^{-1}\widetilde P$ 的差，在共同浅端高度下满足

$$
(H_j-H_j^P)'=\frac{rw}{2j\,r_x}\widetilde f_{P,j}.
\tag{1.2}
$$

因此它将实际兼容残差积分，不把该残差再微分成很大的二阶变化。非线性 Darboux 缺陷、均值求积差和新候选的实际 metric 必须重新读出。

## 2. 平面 coframe 和同一连接

对这个实际高度，定义

$$
S=1-\frac{h_\phi^2}{r^2\rho^2},\qquad D=ES-h_r^2,
$$
$$
q=\sqrt{r^2\rho^2-h_\phi^2},\quad
b=-\frac{h_rh_\phi}{q},\quad
a=\frac{r\rho\sqrt D}{q}=\sqrt{D/S}.
\tag{2.1}
$$

保持 $S,D>0$。若 $t=(\cos\alpha,\sin\alpha)$，取顺时针法向
$n=(\sin\alpha,-\cos\alpha)$，则希望的平面两速度为

$$V=bt+an,\qquad Q=qt.$$

这些代数式准确满足

$$|V|^2+h_r^2=E,\quad V\cdot Q+h_rh_\phi=0,\quad |Q|^2+h_\phi^2=r^2\rho^2.$$

定义

$$
\widetilde\Omega=\frac{q_r-b_\phi}{a},\qquad
\mathcal A_r=\frac{b\widetilde\Omega-a_\phi}{q},\qquad
\widetilde C=\partial_r\widetilde\Omega-\partial_\phi\mathcal A_r.
\tag{2.2}
$$

在原 $P,K,T,U,z$ 记号中，R44 的同一个连接给

$$
\widetilde\Omega=\rho\frac{1+z(1+K)T/S}{\sqrt D},\qquad
\mathcal A_r=\frac{z(1+K)U}{rS\sqrt D},
$$
$$
\widetilde C=\frac{\rho rE^2}{D^{3/2}}\mathscr D(h).
\tag{2.3}
$$

这里的 $\mathscr D$ 是 R44.28 的实际内蕴缺陷，不是一个重新置零的求解方程。全部量均针对相同高度和背景。

## 3. 角向原函数：实际已运行的诊断 helper

令 $I_\phi$ 为零均值周期原函数，设
$m=\langle\widetilde\Omega\rangle_\phi-1$。定义

$$
\alpha=\phi+I_\phi(\widetilde\Omega-1)+\beta(r),
\qquad \beta'=\langle\mathcal A_r\rangle_\phi,
\tag{3.1}
$$

$$F^{\rm ang}_{xy}=I_\phi(qt),\qquad F^{\rm ang}=(F^{\rm ang}_{xy},h).$$

对当前半周对称输入，$\alpha(\phi+\pi)=\alpha(\phi)+\pi$，故 $qt$ 半周反号，角平均为零；所得平面曲线闭合且中心为0。反射偶高度与偶 $\rho$ 还使 $\mathcal A_r$ 为奇函数，所以此时可以取一个固定的 $\beta$，无需另做径向相位积分。

记实际径向误差 $e=F^{\rm ang}_{xy,r}-V$。逐项微分 $t_\phi=-\alpha_\phi n$、$n_\phi=\alpha_\phi t$，得到

$$
\boxed{e_\phi=am\,t-
       \{qI_\phi\widetilde C+bm\}n,\qquad \langle e\rangle=0.}
\tag{3.2}
$$

这里用 $\alpha_\phi=\widetilde\Omega-m$ 以及
$\alpha_r-\mathcal A_r=I_\phi\widetilde C$。所以径向误差可以由两个角原函数显式读出。实际 Gram 则准确为

$$
\Delta g_{\phi\phi}=0,\quad
\Delta g_{r\phi}=q\,e\cdot t,\quad
\Delta g_{rr}=2V\cdot e+|e|^2.
\tag{3.3}
$$

可运行文件是
[`2026-11-17-parallel-model-angular-reconstruct.py`](../notes/2026-11-17-parallel-model-angular-reconstruct.py)。它定义的是一个**有限 DFT 角原函数**，对字面 sample-to-Fourier 映射求实际 $F_r$，并直接计算全部三项 Gram；不以连续 (3.2) 替代实际导数。连续 curl 式只产生独立的 `radial_error_identity_gap`，用于显示角混叠/求积差。

该 helper 的圆参考读出约 $5.2\times10^{-14}$，独立非零解析高度与非恒定 $\rho$、$w_r\ne0$ 的实际 $F_r$ 对径向差分误差约 $2.6\times10^{-11}$，curl 身份差约 $10^{-15}$。这些是实现核验，不是当前尾场的误差帽。实际当前尾输出由独立 geometry note 记录。

角向读出若对一般有限高度仅知系数 C²，其 $F_{rr}$ 可能读取三阶径向数据；不能由 $h\in C^2$ 便免费宣称此坐标构造 C²。下一节避免这个要求。

## 4. 径向积分：当前有限角高度得到真实 C² 映射

从同一浅端闭曲线 $F_{0,xy}(\phi)$ 和一个切向角 lift $\alpha_0(\phi)$ 出发，定义

$$
\alpha(r,\phi)=\alpha_0(\phi)+\int_b^r\mathcal A_r(s,\phi)\,ds,
\tag{4.1}
$$

$$
F^{\rm rad}_{xy}(r,\phi)=F_{0,xy}(\phi)
                       +\int_b^r\{bt+an\}(s,\phi)\,ds,
\qquad F^{\rm rad}=(F^{\rm rad}_{xy},h).
\tag{4.2}
$$

这里 $b$ 在积分下限是浅端半径，花括号中的 $b$ 是 (2.1) 的切向分量，二者的角色不混用。实际程序也可给该分量另取名字 `radial_tangent`。

由于 $\mathcal A_r$、$a$、$b$ 周期，初始角 lift 的转角 $2\pi$ 沿径向保持，$F^{\rm rad}$ 每圈准确闭合。若输入与初始曲线保持半周对称，则所有后续平面曲线也中心对称；没有每圈重新选择平移。

**C² 命题。** 假设 $w\in C^1$、$\rho$ 光滑且严格正，
$h=h_0(r)+\sum_{j=1}^M H_j(r)\cos(2j\phi)$ 的系数均 C²，$S,D$ 在闭环带上严格正，初始曲线与角 lift 光滑。则 (4.1)–(4.2) 定义 C² 映射。实际 Gram 正定时它是浸入；单射和全局嵌入仍须另证。

**证明。** 有限角和固定光滑 $\rho$ 使高度拥有任意阶角导数；其一、二阶径向导数也可再任意次求角导数。$a,b$ 至少 C¹，$\mathcal A_r$ 用 $h_r,h_\phi,h_{r\phi}$ 和背景，只需这些实际数据。角向微分可以通过两个径向积分，给连续 $F_\phi,F_{\phi\phi}$；混合导数直接由 $F_r=V$ 得到。径向二阶导数只使用

$$
\boxed{F_{xy,rr}=(b_r+a\mathcal A_r)t
                       +(a_r-b\mathcal A_r)n,}
\tag{4.3}
$$

不含 $\partial_r\mathcal A_r$、$h_{rrr}$ 或 $w''$。其高度分量为 $h_{rr}$。以上各项连续，故 $F\in C^2$。证毕。

这条命题特别适合 (1.1)：实际保存 $K$ 的 C¹ 插值已经足够形成非均值 C² 高度。它不适用于把原 C¹ $P$ 插值直接叫成 C² 高度的做法。

实现 (4.3) 所需的稳定字面量为

$$
q_r=\frac{r\rho^2-h_\phi h_{r\phi}}q,
$$
$$
b_r=-\frac{h_{rr}h_\phi+h_rh_{r\phi}}q
     +\frac{h_rh_\phi q_r}{q^2},
$$
$$
S_r=-\frac{2h_\phi h_{r\phi}}{r^2\rho^2}
     +\frac{2h_\phi^2}{r^3\rho^2},\quad
D_r=2ww_rS+ES_r-2h_rh_{rr},
$$
$$a_r=\frac a2(D_r/D-S_r/S).\tag{4.4}$$

这些全都来自同一实际高度。若数值积分或插值另外近似 (4.1)–(4.2)，还须直接读出其定义的实际导数或明确控制积分/插值误差。

## 5. 两次径向积分控制实际角度量误差

置

$$\psi=\alpha_\phi-\widetilde\Omega,\qquad
T_{
m vec}=F^{\rm rad}_{xy,\phi}-qt.$$

则准确有

$$
\boxed{\psi_r=-\widetilde C,\qquad
(T_{
m vec})_r=\psi(at-bn).}
\tag{5.1}
$$

**证明。** 第一式直接微分 (4.1)。第二式使用
$V_\phi=(b_\phi+a\alpha_\phi)t+(a_\phi-b\alpha_\phi)n$、
$(qt)_r=q_rt-q\mathcal A_rn$，再代入 (2.2)。证毕。

初始 $\psi(b)$ 和 $T_{\rm vec}(b)$ 必须取实际值。若初始曲线由准确角原函数、完整均值等于1生成，它们为零；有限 DFT 初始曲线需保留实际求积和插值差。

此时实际 Gram 的三项是

$$
\boxed{
\Delta g_{rr}=0,\quad
\Delta g_{r\phi}=V\cdot T_{\rm vec},\quad
\Delta g_{\phi\phi}=2q\,t\cdot T_{\rm vec}+|T_{\rm vec}|^2.}
\tag{5.2}
$$

因此 $B=\Delta g_{r\phi}/(\sqrt E r\rho)$、
$C=\Delta g_{\phi\phi}/(r^2\rho^2)$ 给准确相对算子误差

$$\frac{|C|+\sqrt{C^2+4B^2}}2.\tag{5.3}$$

也可令 $\tau=|T_{\rm vec}|/(r\rho)$，用
$|B|\le\tau$、$|C|\le2\tau+\tau^2$ 得粗界 $3\tau+\tau^2$。

与角向路径不同，(5.1) 把真实 curl 缺陷沿径向积分两次，不读取它的径向导数。数值上仍优先对实际构造的 $F$ 求角导数并直接计算 Gram，(5.1) 只作独立差额检查或在已有连续缺陷界时作上界。

## 6. 实际读出和仍需完成的几何

`parallel-geometry` 的外层 loader 已使用 actual state mesh 与 background Hermite 节点的公共细分，在各原子段取实际左右导数；它正在比较角向 $P$ 高度、角向积分 $K$ 高度以及本节径向坐标构造。所有新候选各保自己的高度来源、积分设置和源身份，不把一次有限 BVP 接受重标为这些新场已通过。

固定浅端外形与完整 trace 以后，R239 的共同平面配准适用于准确等距接缝。对有限误差场，实际两侧六 jet 仍需比较并由已登记 collar/Hermite 工具给出同一 C² 装配。闭面帽、held、全时 reach、Hausdorff 振幅和同一 $g$ 加密并未由单片曲面的闭圈或 (5.2) 自动完成。
