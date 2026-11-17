# R632　C² 半圆回头盖：凸平行体、全部同盖法向弦和实际直径

2026-11-17，Astra-larger-parallel-16f63c8b，geometry_amplification；并行构造讨论由 constructive_model、root 提供，源码与下列完整组件证明由本支线落实。

**状态：组件构造、凸平行体表示、reach/法向弦结论及直径公式已证明；示例整数/有理包围已实际计算。未将组件拼到任何活动体，未证明当前大幅闭等距族存在。**

实现：[2026-11-17-parallel-geometry-return-cap.py](../notes/2026-11-17-parallel-geometry-return-cap.py)。它提供明确积分定义、六个 Cartesian jet、含轴点的 Cartesian 顶盘、两个有开 cuff 的 OBJ 组件和有理直径包围；没有把有限非平 tail 自动封口。

## 1. 与既有结果的关系及明确对象

本次先检索了本题 `results/`、`notes/` 的 Minkowski、凸平行体、回头盖及 reach 登记。已有 [R1 §2](R1-two-mode-core-phase-gap.md) 用平面严格凸曲线的平行体证明其 reach；本文不重报那条定理。新对象是以下三维、带平顶盘的半圆回头盖；核心工作是证明**这个具体 C² 曲率 ramp 的内偏移确为凸体**，并把其全部内部法向弦责任交给同一凸平行体，而不是由曲率样本猜测全局 reach。

固定

$$
R>0,\qquad H\ge0,\qquad \rho>0,\qquad 0<\delta<\pi\rho,
\qquad L=\pi\rho+\delta.
\tag{632.1}
$$

$R,H$ 是待接上 cuff 的半径与高度；$\rho$ 为圆角半径，$\delta$ 为每端的曲率过渡长度。令

$$
S(t)=10t^3-15t^4+6t^5,\qquad
J(t)=\frac52t^4-3t^5+t^6=\int_0^tS(v)\,dv.
$$

曲率定义为

$$
\kappa(s)=\frac1\rho
\begin{cases}
S(s/\delta),&0\le s\le\delta,\\
1,&\delta\le s\le L-\delta,\\
S((L-s)/\delta),&L-\delta\le s\le L.
\end{cases}
\tag{632.2}
$$

两端各长 $\delta$，常曲率段长 $\pi\rho-\delta>0$。由于 $\int_0^1S=1/2$，总转角准确为 $\pi$。定义

$$
\theta(s)=\int_0^s\kappa(v)\,dv,\qquad
r(s)=R+\int_0^s\cos\theta(v)\,dv,
\qquad z(s)=H+\int_0^s\sin\theta(v)\,dv.
\tag{632.3}
$$

上回头面为

$$
F_+(s,\beta)=(r(s)\cos\beta,r(s)\sin\beta,z(s)).
$$

在 $s=L$ 接水平圆盘 $0\le r\le R$；其高度记为 $Z=z(L)$。所得带一个 cuff 边界的组件记为 $\Gamma_+$。$\Gamma_-$ 为其关于 $z=0$ 的反射。下文的闭凸面 $\Sigma$ 则是另给 $\Gamma_+$ 补上 $z=H$ 的**底平盘**得到的辅助对象；这张底盘不放入未来的活动体拼接中。

## 2. C²、空间范围与接缝 jet

由 $0\le S\le1$，$\kappa\in C^2$，且 $0\le\kappa\le1/\rho$。其端点值和一阶导数为零。对称性给

$$
\theta(L-s)=\pi-\theta(s),\qquad r(L-s)=r(s),
\qquad z(L-s)=H+Z-z(s).
\tag{632.4}
$$

因此 $r(0)=r(L)=R$；前半段半径增、后半段减，始终 $r\ge R$；高度单调，始终 $H\le z\le Z$。设

$$
e=Z-H-2\rho.
$$

因为 $ds-\rho\,d\theta=(1-\rho\kappa)ds\ge0$，其总质量为 $\delta$，而

$$
e=\int_0^L\sin\theta(s)(1-\rho\kappa(s))\,ds,
$$

故

$$
0<e\le\delta,\qquad Z=H+2\rho+e.
\tag{632.5}
$$

严格正来自任一开 ramp 中 $\sin\theta>0$、$\kappa<1/\rho$。因此内偏移体在竖直方向也有正厚度；本文不需要把它当成退化极限。

以 $e_r,e_\beta,e_z$ 表示柱坐标单位向量，六 jet 为

$$
\begin{aligned}
F&=r e_r+z e_z,\\
F_s&=\cos\theta\,e_r+\sin\theta\,e_z,& F_\beta&=r e_\beta,\\
F_{ss}&=\kappa(-\sin\theta\,e_r+\cos\theta\,e_z),&
F_{s\beta}&=\cos\theta\,e_\beta,&F_{\beta\beta}&=-r e_r.
\end{aligned}
\tag{632.6}
$$

$r>0$ 使回头面正则。起端 jet 为平面向外的 $F_s=e_r,F_{ss}=0$；末端为平面向内的 $F_s=-e_r,F_{ss}=0$，混合与角二阶 jet 也准确等于对应平面的 jet。因此底补盘、顶盘都以 $C^2$ 接合。盘中心使用 Cartesian 图 $(x,y)\mapsto(x,y,H)$ 或 $(x,y,Z)$，没有用退化极坐标宣称正则性。组件和闭凸补全面的嵌入将在下一节的凸体构造中同时明确。

未来活动体在 cuff 处必须提供相同的**完整平面二 jet**，不能只令高度差很小。若物理角为 $\phi$，极角为 $\beta=\Phi(\phi)$、$\Phi'=\eta>0$，调用者还须正确使用

$$
F_\phi=\eta F_\beta,\qquad
F_{\phi\phi}=\eta^2F_{\beta\beta}+\eta'F_\beta.
$$

这里 $\eta$ 只是角坐标密度，不是本条圆角半径 $\rho$。

## 3. 完整内偏移凸体 K

回头曲线向外的法向为

$$
n(s)=\sin\theta(s)\,e_r-\cos\theta(s)\,e_z.
$$

在同一子午平面内，作半径 $\rho$ 的内偏移

$$
q(s)=(q_r,q_z)
=(r(s)-\rho\sin\theta(s),\ z(s)+\rho\cos\theta(s)).
\tag{632.7}
$$

直接微分得到关键恒等式

$$
q'(s)=(1-\rho\kappa(s))(\cos\theta(s),\sin\theta(s)).
\tag{632.8}
$$

系数非负。整个常曲率中段被压到一个点 $C=(C_r,C_z)$；首、末 ramp 的 $q_z$ 严格增加。端点为

$$
q(0)=(R,H+\rho),\qquad
q(L)=(R,Z-\rho)=(R,H+\rho+e).
$$

因此 $q$ 定义在竖直区间 $[H+\rho,Z-\rho]$ 上的一张连续半径图 $q_r=f(q_z)$，中段压点不会使该函数多值。由 (632.8)，在两张开 ramp 上

$$
f'(q_z)=\cot\theta(s).
$$

$\theta$ 严格增加，故此斜率严格下降。跨过压点时，斜率由 $\cot(\delta/(2\rho))$ 跳到其相反数，仍是向下跳。于是 $f$ 在整个区间上凹。又 $q_r$ 先增后减、两端均为 $R$，所以 $f\ge R>0$。

定义真正的三维实体

$$
K=\{(x,y,z): H+\rho\le z\le Z-\rho,
\quad \sqrt{x^2+y^2}\le f(z)\}.
\tag{632.9}
$$

它非空、紧、有内点，且凸：对两点作凸组合，水平范数不超过其范数的相同凸组合，再由 $f$ 的凹性不超过新高度处的 $f$。这一步包含两张内平盘和中间压点处的整个法向锥，没有把 K 假定为光滑体。

原回头曲线同样满足 $dr/dz=\cot\theta$ 递减，因此它连同 $z=H,Z$ 两张半径 R 的平盘围成一个紧凸体 Q。对于每个非竖直法向

$$u=\sin\theta\,e_r-\cos\theta\,e_z,$$

Q 的支持点为对应 $p(s)$，K 的支持点为 $q(s)$；若在压平中段，$q(s)=C$ 的法向锥包含该段的全部法向。由 $p=q+\rho u$，

$$h_Q(u)=h_K(u)+\rho.$$

竖直两个方向由上下平盘得到同一等式。旋转对称性覆盖全部三维单位方向。支撑函数确定紧凸体，故准确有

$$
\boxed{Q=K+\overline B_\rho,\qquad
\Sigma=\partial Q=\partial(K+\overline B_\rho).}
\tag{632.10}
$$

由前节的明确图，$\Sigma$ 是闭 $C^2$ 嵌入曲面，$\Gamma_+$ 是删去底盘内部后的嵌入圆盘组件。不是先假设嵌入再用局部曲率论证它。

由 (632.6) 直接计算，两条主曲率的绝对值是 $\kappa$ 和 $\sin\theta/r$。又由内偏移半径 $r-\rho\sin\theta=q_r\ge R>0$，后者也小于 $1/\rho$；两张平盘曲率为零。因此整个 $\Sigma$ 的主曲率绝对值均不超过 $1/\rho$。下一节还支付局部曲率不能单独支付的全局最近点问题。

## 4. 凸补全面的准确 reach 与全部固定盖点对

先对任意非空紧凸 K 说明所需平行体事实。凸投影唯一：若有两个不同最近点，取其中点并展开距离平方会严格减小距离。记 $Q=K+\overline B_\rho$、$\Sigma=\partial Q$。

若 x 在 Q 外，其到凸体 Q 的投影唯一且位于 $\Sigma$，故最近边界点唯一。若 x 在 Q 内且距 $\Sigma$ 小于 $\rho$，则 x 不在 K：否则 $\overline B(x,\rho)\subset Q$ 给距边界至少 $\rho$。

因此设 $d=\operatorname{dist}(x,K)\in(0,\rho)$，k 为唯一凸投影，$u=(x-k)/d$。投影支持半空间条件使 $k+\lambda u$ 对 K 的距离等于 $\lambda$。于是 $p=k+\rho u\in\Sigma$，且 $|p-x|=\rho-d$。对任意 $q\in\Sigma$，

$$
\rho=\operatorname{dist}(q,K)\le|q-k|
\le|q-x|+d.
$$

等号若成立，三角不等式的等号条件强迫 $q=k+\rho u=p$。所以全部距 $\Sigma$ 小于 $\rho$ 的点都只有一个最近点，得到 $\operatorname{reach}(\Sigma)\ge\rho$。

对当前 ramp，压点 C 在任一固定方位上对应一整段非零长度的半圆弧，弧上各点距其共同内偏移点均为 $\rho$。该内偏移点在 K 内，距所有边界至少 $\rho$。故它在距离 $\rho$ 处有多个最近边界点，反向给出

$$
\boxed{\operatorname{reach}(\Sigma)=\rho.}
\tag{632.11}
$$

还可直接得到未来闭面要使用的**同盖法向弦**。若 p 是 $\Sigma$ 的外法向 n 所在点，则 $p-\rho n\in K$，其半径 $\rho$ 的球包含在 Q 中。对任意 $q\in\Sigma$，内球不越过边界，加上 Q 的支持半空间，给

$$
n\cdot(q-p)\le0,\qquad
|q-p|^2+2\rho n\cdot(q-p)\ge0.
$$

所以

$$
\boxed{2\rho|n_p\cdot(q-p)|\le|q-p|^2.}
\tag{632.12}
$$

将 p,q 限制到 $\Gamma_+$，此式原样成立；反射后 $\Gamma_-$ 同样成立。它覆盖圆角—圆角、圆角—顶盘、顶盘—顶盘的所有点对，而不只是曲率样本。

两盖的高度分别满足 $z\ge H$、$z\le-H$，所以任何跨盖弦长至少 $2H$。因此对

$$0<\tau\le\min(\rho,H)$$

全部同盖及跨盖点对均满足目标法向弦界；跨盖直接用 $|q-p|\ge2\tau$ 即可。特别地 H≥ρ 时，固定盖—固定盖责任可全部在半径ρ下支付。

**这不证明活动体—盖或活动体—活动体的点对。** 也不把有边组件自身的 reach 与闭补全面的 reach 混为一谈。未来完整场仍须真正给出 cuff 局部图、活动曲率及剩余完整点对覆盖，才可用 [R241](R241-immersion-cover-embedding-and-normal-cones.md)/[R422](R422-current-C-closed-pair-universe-and-reach-binding.md) 完成全局嵌入/reach。

## 5. 组件直径：通用界及可准确计算的公式

从 (632.3) 减去同转角的理想半圆点，差为

$$
v(s)=\int_0^s(\cos\theta,\sin\theta)(1-\rho\kappa)\,ds,
\qquad |v(s)|\le\delta.
$$

因此两盖（包括顶盘）的通用直径界为

$$
D_{\Gamma_+\cup\Gamma_-}
\le2\left(\sqrt{R^2+(H+\rho)^2}+\rho+\delta\right).
\tag{632.13}
$$

此上界是完整固定盖的界；若活动体未另被放进同一球，不能把它称为完整闭面 D。

令 $u=\delta/(2\rho)$，并设

$$
I_c=\delta\int_0^1\cos\left(\frac\delta\rho J(t)\right)dt,
\quad
I_s=\delta\int_0^1\sin\left(\frac\delta\rho J(t)\right)dt.
$$

整个常曲率中段是中心

$$
C_r=R+I_c-\rho\sin u,
\qquad C_z=H+I_s+\rho\cos u
\tag{632.14}
$$

的同一个半径ρ圆。若

$$R>Z\tan u,\tag{632.15}$$

则首 ramp 的范数严格增加，末 ramp 的范数严格减小。确实，范数平方的弧长导数除以2为 $r\cos\theta+z\sin\theta$；首 ramp 两项非负且第一项严格正，末 ramp 则至多 $-R\cos u+Z\sin u<0$。因此全段最大范数出现在圆形中段，而且该中段包含中心方向的最远点。顶盘范数不超过其外缘。上下两盖互为中心反射后的同一像，故其直径准确为

$$
\boxed{D_{\Gamma_+\cup\Gamma_-}
=2\left(\sqrt{C_r^2+C_z^2}+\rho\right).}
\tag{632.16}
$$

代码另给不用浮点三角比较的充分条件：$u<1$、$\delta<3\rho$，以及

$$
R(1-u^2/2)>(H+2\rho+\delta)u.
\tag{632.17}
$$

由 $\sin u\le u$、$\cos u\ge1-u^2/2$ 和 (632.5)，它推出 (632.15)。该条件可对准确有理输入直接计算。

### 5.1 不依赖 Gauss 误差估计的有理包围

在 (632.17) 下，$0\le(\delta/\rho)J(t)\le u<1$。对余弦取到六次/八次的交错 Taylor 下/上界，对正弦取到七次/九次的下/上界；将这些多项式准确积分，即得到 $I_c,I_s$ 的有理上下界。端点 $\sin u,\cos u$ 用相同交错界。代入 (632.14)，再用整数平方根向外包围 (632.16)。全部步骤只用有理数，证明不依赖两次浮点求积结果很接近。

## 6. 与未来固定标记的真实隔离接口

假设未来活动体确实位于 $|z|\le H$，并按真实平面二 jet 接上两个 cuff。顶平盘在 $z=Z$，且 $Z-H\ge2\rho$。对位于顶盘水平半径不超过 $r_*$ 的标记支撑，到活动体的距离至少 $2\rho$；到圆角部分的水平距离至少 $R-r_*$，因为圆角始终在 $r\ge R$；到另一盖的竖直距离更大。

因此若 $r_*\le R-2\tau$、$\tau\le\rho$，这个标记支撑到整面同一顶盘补集的隔离至少 $2\tau$，下侧同理。顶盘也是整面的真实支撑平面。由 [R629](R629-outward-supporting-caps-preserve-reach-and-held-distance.md) 的外推定理可给非负小标记支付隔离和握持单调性。这里**仍没有支付未标记活动体的全域 reach**，不能用本节倒置整个证明顺序。

## 7. 实际组件生成、API 与未完成项

本次以四个 binary64 参数的准确实数值定义演示组件：

$$
R=1.767318285443017,\quad H=1.2627007534707082,
\quad\rho=.145,\quad\delta=.002.
$$

H 取自已读小幅 weighted tail 的深度4数值均值，仅用于独立组件示范；它不是完整平 cuff 的已认证高度，也不是强前缀的 $\lambda=1$ 接合高度。

实际有理判据 (632.17) 的余量为

$$
\frac{25266713514072412005817542199054536941971141976297}
{14384249440493441431383641931959131871972950016000}>0.
$$

脚本由准确 Fraction 运算及向外整数平方根得到

$$
\boxed{
4.810430225196148268605699
\le D_{\Gamma_+\cup\Gamma_-}
\le4.810430225196148268605724.}
\tag{632.18}
$$

通用界 (632.13) 约4.8128650493。浮点评价还给 $Z\approx1.552701738691536$、最大水平半径约1.913318284981067；闭凸补全面的 reach 准确是该输入的ρ，约 .145。曲面 jet 的单位弧长/正交/角长恒等式实算误差均在 $1.4\times10^{-15}$ 内。

API 为 `ReturnCap.meridian(s)`、`jet(s,beta,side)`、`disk(x,y,side)`、`mesh(...)`、`paired_diameter()` 和 `rational_diameter_enclosure()`。顶盘使用单一 Cartesian 中心。上盖网格取向对应补凸体外法向，下盖在空间反射后反转三角形顺序。

实际生成的上下两组件 OBJ 有41,474顶点、82,688面、4,123,123 bytes；逐边复读确认124,160条无向边、256条边界边、零非流形边、零内部定向冲突、两个连通分支，Euler 总数为2。它们是两个**有边圆盘组件**，不是一张闭面。

```sh
OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-return-cap.py \
  --R 1.767318285443017 --H 1.2627007534707082 \
  --radius .145 --ramp .002 \
  --obj /workspace/scratch/16f63c8bce6b/parallel-return-cap-components.obj \
  --out /workspace/scratch/16f63c8bce6b/parallel-return-cap-components.json
```

源码 SHA256：`46257db172cade02793d7f2dcfec89475a35ca1cc7399ea200037384c4df1c49`。组件 OBJ SHA256：`ee8dba3abdc4d3f98fe04e90114dc0295d2f73942e1bf96245e67231bab3a9eb`。完整报告 SHA256：`b637e1c791b221ec5f7fc4e6290e466ded94e81df9c6310c67e7b162113b999e`。raw OBJ/报告只在仓库外，不提交；保留源码、参数和哈希即可重生。

输出持续明确 `source_cuff_gluing_checked=false`、`full_body_closed=false`、`full_body_reach_certified=false`。下一步是将真实活动体的平 cuff 二 jet、真实 H、活动体位置包围和剩余全点对责任交给该组件；本文没有替代这些条件，没有完成课题 README 的七项标准。
