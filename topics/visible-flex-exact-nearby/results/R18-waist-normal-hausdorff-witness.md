# R18：相差四分之一周期的腰圈法向 Hausdorff witness

2026-11-10，geometry-transfer。

**状态：已证明；主课题的精确几何接口。** 本文把四重主体的两个
明确腰圈点转成到另一整张闭面的真实距离。径向差严格小于
另一闭面的 reach 时得到准确距离；第 10 节的法向空球下界还允许
径向差略超过 reach。不要求腰圈截面凸，不用材料位移替代 Hausdorff
距离，并给近似点值、法向和精确解之间的显式误差转移预算。

这个接口可用于 R16 的有限阶近似几何；有限阶度量残差不会因本接口
而消失。R16 的当前数值对象没有真平帽，也没有经认证的全局 reach，
所以不能仅代入浮点数便声称完成验收。

## 1. 主体的坐标、对称和相位约定

只需在腰圈附近有 $(x,\theta)$ 坐标，$x=0$ 是经线反射的固定圈。
在圆柱标架 $e_r(\theta),e_\theta(\theta),e_z$ 中写真实主体为
$$
F(x,\theta)=a_0(x)e_r+z_0(x)e_z
+\sum_{k\ge1}\left[
 U_k(x)\cos(4k\theta)e_r+
 T_k(x)\sin(4k\theta)e_\theta+
 W_k(x)\cos(4k\theta)e_z\right].
\tag{1.1}
$$
可以是有限和；无限和时要求在该邻域按 $C^2$ 收敛。
四重及角反射对称对应上面的余弦、正弦形式。经线反射要求
$$
a_0,U_k,T_k\text{ 为偶函数},\qquad
z_0,W_k\text{ 为奇函数}.
\tag{1.2}
$$
因此腰圈的高度为零；这个高度规范可以通过一次固定平移设定。

令 $\mathscr R_\alpha$ 是绕 $z$ 轴的环境旋转，角度 $\alpha$。
固定材料坐标下的相位族定义为
$$
F_\alpha(x,\theta)=
\mathscr R_\alpha F(x,\theta-\alpha).
\tag{1.3}
$$
由于旋转同时把移动标架变为 $e_r(\theta),e_\theta(\theta)$，
(1.3) 正好把 (1.1) 中的每个 $4k\theta$ 换成
$4k(\theta-\alpha)$，没有另加切向项。

在原来轴对称且固定的帽区，(1.3) 等于原参数化，故平帽可以点态固定。
R17 的静态标记也可保持原位置，只在移动主体上使用 (1.3)。
此时完整带标记闭面的像并非一次整体环境旋转，但腰圈公式不变。

若 $F^*e$ 准确不依赖 $\theta$，则
$$F_\alpha^*e=\tau_{-\alpha}^*(F^*e)=F^*e,$$
其中 $\tau_\alpha(x,\theta)=(x,\theta+\alpha)$。
这是相位族取得同一精确度量所需的实际条件。
若只有非均值残差很小，这里得到的仍只是近似同度量族。

## 2. 两个腰圈点及完整法向条件

取 $\alpha=0$ 和 $\alpha=\pi/4$，并在两张面上都取材料点
$(x,\theta)=(0,0)$。令
$$
r_+=a_0(0)+\sum_{k\ge1}U_k(0),\qquad
r_-=a_0(0)+\sum_{k\ge1}(-1)^kU_k(0).
$$
由 (1.2) 和
$\cos(-k\pi)=(-1)^k,\ \sin(-k\pi)=0$，
$$
P=F_0(0,0)=r_+e_x,\qquad
Q=F_{\pi/4}(0,0)=r_-e_x.
\tag{2.1}
$$
所以均值和全部偶数 $k$ 模准确相消：
$$
P-Q=\Delta e_x,\qquad
\boxed{\Delta=2\sum_{\substack{k\ge1\\k\ {\rm odd}}}U_k(0),\quad
d=|\Delta|.}
\tag{2.2}
$$

还必须付清法向条件，而不能只因两点共线就使用法向管。
对 $\alpha\in\{0,\pi/4\}$，写
$c_k=\cos(4k\alpha)\in\{1,(-1)^k\}$。
在对应点处直接微分得
$$
(F_\alpha)_x=
\left[z_0'(0)+\sum_{k\ge1}c_kW_k'(0)\right]e_z
=:C_\alpha e_z,
\tag{2.3}
$$
$$
(F_\alpha)_\theta=
\left[a_0(0)+
 \sum_{k\ge1}c_k\bigl(U_k(0)+4kT_k(0)\bigr)\right]e_y
=:B_\alpha e_y.
\tag{2.4}
$$
经线偶性消掉所有径向、角向的 $x$ 导数；
角向正弦零值和 $W_k(0)=0$ 消掉其余分量。

只要
$$B_\alpha C_\alpha\ne0, \tag{2.5}$$
该点就是正则腰圈点，其法线直线恰为 $\mathbb R e_x$。
在已经假设为嵌入的真实面上，(2.5) 自动成立；
对近似对象则应计算它，不把坐标退化误认为合法法向。
若该点 $r_\pm>0$ 且外法向满足正支撑，则外法向准确为 $e_x$。
以下距离结论只需要法线直线，不依赖所选法向的正负号。

## 3. 法向管给到另一整张面的准确距离

**命题。** 设包含上述点的两个像 $S_0,S_{\pi/4}$ 都是闭 $C^2$
嵌入面，并满足第 2 节的正则条件。若
$$
0<d<\operatorname{reach}(S_{\pi/4}),
\tag{3.1}
$$
则
$$
\boxed{\operatorname{dist}(P,S_{\pi/4})=d,\qquad
d_H(S_0,S_{\pi/4})\ge d.}
\tag{3.2}
$$

**证明。** 由 (2.2)—(2.5)，对 $Q$ 的某个单位法向 $\nu_Q$，
有 $P=Q+t\nu_Q$、$|t|=d$。闭 $C^2$ 嵌入面的 reach 同时是其全局
法向管半径；在 $|t|<\operatorname{reach}$ 内，最近点投影满足
$\pi(Q+t\nu_Q)=Q$。因此到整个 $S_{\pi/4}$ 的距离就是 $|t|$，
而不只是到腰圈或到某个局部图的距离。$P\in S_0$，遂有双向
Hausdorff 距离的下界。证毕。

若能证明的 reach 是 $S_0$ 的下界，也可交换两相位及两点。
若相位参数包含这两个时刻，以 $S_0$ 为初始像，则
$$\delta_{\rm hold}\ge d.$$
因此可见性验收只需在同一实际对象上付清
$$
d\ge\frac{D_0}{20},\qquad d<\rho,\qquad
\operatorname{reach}(S_{\pi/4})\ge\rho.
\tag{3.3}
$$
严格上界 $d<\rho$ 是这里准确距离等式证法的条件；即使某个截面
已经非凸，(3.2) 仍然成立。需要允许 $d\ge\rho$ 时，可用第 10 节
较小但仍有用的真实距离下界。

## 4. 对有限阶或收敛阶数展开的准确读取

若振幅展开为
$$
U_k(x;\varepsilon)=\sum_{j\ge1}\varepsilon^jU_{j,4k}(x),
$$
则一般的准确公式仍是
$$
\Delta(\varepsilon)=
2\sum_{k\ {\rm odd}}\sum_{j\ge1}
 \varepsilon^jU_{j,4k}(0).
\tag{4.1}
$$
“四重和反射”本身不强迫 $j,k$ 同奇偶。只有当实际构造另外满足
R16 递归使用的阶数选择规则
$$
U_{j,4k}=0\quad\text{除非 }1\le k\le j,\quad k\equiv j\pmod2,
\tag{4.2}
$$
才可化为
$$
\boxed{\Delta(\varepsilon)=
2\sum_{\substack{j\ge1\\j\ {\rm odd}}}\varepsilon^j
 \sum_{\substack{1\le k\le j\\k\ {\rm odd}}}U_{j,4k}(0).}
\tag{4.3}
$$
必须保留每个奇阶产生的全部奇数 $k$ 模，
不能只读取最低第四模。均值以及所有偶阶项都在该公式中准确取消。
有限阶多项式取有限和；对真正收敛族使用相应收敛和。

R16 的五次样条诊断应从实际候选的系数、值和导数读取
(2.2)—(2.5)，而不是把仅满足重构 ODE 的导数替代真实样条导数。
即使这个近似对象在几何上满足 (3.2)，其非均值度量残差仍是
精确等距求解必须处理的另一个量。

## 5. 保持对称的精确校正：只需点值预算

设真实校正保持 (1.1)—(1.2) 的全部对称，
且近似两点 $\widetilde P,\widetilde Q$ 与真两点 $P,Q$ 满足
$$
|P-\widetilde P|\le\eta_P,\qquad
|Q-\widetilde Q|\le\eta_Q,\qquad
\eta_\Sigma=\eta_P+\eta_Q.
$$
记近似径向差为 $\widetilde d$。则
$$|d-\widetilde d|\le\eta_\Sigma.$$
真实法向依对称仍准确径向，因此若已另证真实另一闭面的
reach 至少为 $\rho$，并满足
$$
\widetilde d+\eta_\Sigma<\rho,\qquad
\widetilde d-\eta_\Sigma\ge D_*/20,\qquad D_0\le D_*,
\tag{5.1}
$$
就得到
$$\delta_{\rm hold}\ge\widetilde d-\eta_\Sigma\ge0.05D_0.$$
这里没有借用近似面尚未认证的 reach。
$D_*$ 必须是同一精确初始面直径的上界，不能用环宽或局部半径替代。

## 6. 一般精确校正：点值与法向误差预算

不假定校正严格保持对称。设近似数据满足
$$
\widetilde P-\widetilde Q=
\widetilde d\,\widetilde\nu+e,\qquad
|\widetilde\nu|=1,\quad\widetilde d\ge0,\quad |e|\le\beta.
\tag{6.1}
$$
这里可以取实际近似单位法向，令 $\widetilde d$ 为法向投影的绝对值，
用法向符号吸收投影符号，$\beta$ 则是余下切向误差。
再假设真实 $Q$ 的对应有符号单位法向满足
$$
|\nu_Q-\widetilde\nu|\le\nu,\qquad
|P-\widetilde P|\le\eta_P,\quad
|Q-\widetilde Q|\le\eta_Q.
\tag{6.2}
$$
若真实另一面 $S$ 的 reach 至少为 $\rho$，且
$\widetilde d<\rho$，令 $N=Q+\widetilde d\nu_Q$。
由真实法向管，$\operatorname{dist}(N,S)=\widetilde d$；
而 (6.1)—(6.2) 给
$$|P-N|\le\eta_\Sigma+\beta+\widetilde d\nu.$$
距离函数为 1-Lipschitz，所以
$$
\boxed{
\operatorname{dist}(P,S)\ge
\widetilde d(1-\nu)-\eta_\Sigma-\beta.}
\tag{6.3}
$$
这是到整个真实闭面的下界，不只是法向分量估计。
由此一个可直接代数验收的预算是
$$
\boxed{
\frac{D_*/20+\eta_\Sigma+\beta}{1-\nu}
\le\widetilde d<\rho,\qquad
0\le\nu<1,\quad D_0\le D_*.}
\tag{6.4}
$$
在精确近似对称下 $\beta=0$。若两点各有同样 $C^0$ 误差 $\eta_0$，
则 $\eta_\Sigma=2\eta_0$。

法向费用也可由一个明确的 $C^1$ 预算得到。
在 $\widetilde Q$ 处用近似诱导度量测量切向量，
若
$$
\|dF-d\widetilde F\|_{\rm op}\le e_1<1,
$$
则选相容方向后
$$
\boxed{\nu\le
\sqrt{\,2\bigl(1-\sqrt{1-e_1^2}\bigr)\,}.}
\tag{6.5}
$$
证明是令 $\nu_Q$ 为真实单位法向：因 $dF^T\nu_Q=0$，
$$\|d\widetilde F^T\nu_Q\|
=\|(d\widetilde F-dF)^T\nu_Q\|\le e_1.$$
$d\widetilde F$ 在近似度量下是等距切平面嵌入，所以左端是两法向
夹角的正弦。选同向法向，再用弦长公式即得 (6.5)。
若只有局部点值、局部导数预算，本节仍成立；全局性由另付的真实
reach 下界承担。

## 7. 与固定曲率标记联用

若 R17 的低峰标记在全过程固定，实际主体逐时满足 $G<4$，
且已得到一对满足 (3.3)、(5.1)、(6.4) 或 (10.4) 的相位，
则同一对像首先有正的 held 距离；R17 的四个非共面曲率标签
进一步排除所有环境全等，故 $\delta_{\rm E}>0$。
若只能支付 $G<13$，可改用 R17 的高峰版本，并使用相应真实 reach。

逻辑顺序是：先认证实际闭面和全局 reach，再用本法向 witness
支付真实 Hausdorff 可见量，最后用固定标签支付非全等。
近似候选上的浮点数用于选择参数和误差预算；
它们不提供尚未证明的精确解、帽端匹配或全程等距。

## 8. 中心对称时直径可准确化为半径上确界

如果 (1.1)—(1.2) 的奇偶结构延伸到整个主体，且两个闭帽也由镜像
构造，则
$$F(-x,\theta+\pi)=-F(x,\theta).$$
因此未标记完整像满足 $S=-S$。对任何非空中心对称紧集，
$$
\boxed{\operatorname{diam}S=2\max_{P\in S}|P|.}
\tag{8.1}
$$
上界由三角不等式给出；最大半径点 $P$ 与 $-P$ 同属 $S$，给出
等号。这把直径认证化为同一个半径函数的全局上确界认证；
有限网格的最大半径仍不自动是该上确界的上界。

加入 R17 标记后，中心对称通常不再保持，但其最大点位移
$U_{\max}\le2R^2/3$ 已明确支付。因此一个直接的初始直径预算为
$$
D_0^{\rm mark}\le2R_{\rm body,*}+\frac43R^2,
\tag{8.2}
$$
其中 $R_{\rm body,*}$ 是未标记完整面最大半径的严格上界。
若还已证明最大半径的一对对称点都在未改主体内，且全部新标记点的
半径不超过该主体上界，就可直接使用 $2R_{\rm body,*}$。

## 9. 纯相位结构如何覆盖全部时刻

对未标记的完整面，(1.3) 给像集合
$$S_\alpha=\mathscr R_\alpha S_0.$$
绕原点的旋转保持主曲率、Gauss 曲率、正支撑 $X\cdot n$、
直径和 reach。因此若在同一真实闭面 $S_0$ 上已认证这些全空间界，
它们对全部连续相位同时成立，不需要把有限相位采样冒充全程证明。

固定轴对称平帽在每个相位具有相同位置与法向，R17 的静态标记
预算也与 $\alpha$ 无关。其法向图嵌入论证、曲率和支撑估计因而
逐时统一适用。配合真正径向的公共度量和 $C^2$ 相位作用，就给
连续全相位的几何验收接口。真正的径向精确解及帽端接合仍是前置的
实际求解任务，不能由这一旋转恒等式代付。

## 10. 法向空球：径向差略超过 reach 的可见性预算

### 10.1 全局距离下界

**命题。** 设 $M$ 是闭 $C^2$ 嵌入面，
$\operatorname{reach}(M)\ge\rho>0$，$Q\in M$，$n(Q)$ 为任一方向的
单位法向。对 $d\ge0$，令 $P=Q+d\,n(Q)$。则
$$
\boxed{\operatorname{dist}(P,M)\ge b_\rho(d),\qquad
b_\rho(d):=\max\{0,\rho-|d-\rho|\}
=\max\{0,\min(d,2\rho-d)\}.}                 \tag{10.1}
$$
尤其 $0\le d\le\rho$ 时下界为 $d$，且因 $Q\in M$ 得到等号；
$\rho<d<2\rho$ 时仍得到正下界 $2\rho-d$。
这是对整张闭面的距离结论，不只针对局部图或截面。

**证明。** 对每个 $0<\rho'<\rho$，真实法向管给
$$\operatorname{dist}(Q+\rho'n(Q),M)=\rho'.$$
因此开球 $B(Q+\rho'n(Q),\rho')$ 与 $M$ 不交。
对任意 $Y\in M$，取极限 $\rho'\uparrow\rho$ 得
$$|Y-(Q+\rho n(Q))|\ge\rho.$$
此处允许 $\rho$ 等于实际 reach，不要求端点的最近点唯一。
三角不等式遂给
$$
|P-Y|\ge\rho-|P-(Q+\rho n(Q))|
=\rho-|d-\rho|.
$$
对所有 $Y$ 取下确界并与零取最大，即得 (10.1)。证毕。

### 10.2 精确校正的通用转移

保留第 6 节的近似点与误差约定 (6.1)—(6.2)，
但不再要求 $\widetilde d<\rho$。
在真实另一面 $S$ 上令
$$N=Q+\widetilde d\,\nu_Q.$$
由 (10.1) 与距离函数的 1-Lipschitz 性，
$$
\boxed{\operatorname{dist}(P,S)\ge
\max\!\left\{0,\,
b_\rho(\widetilde d)
-\eta_P-\eta_Q-\beta-\widetilde d\,\nu\right\}.} \tag{10.2}
$$
证明中使用的仍是
$$|P-N|\le\eta_P+\eta_Q+\beta+\widetilde d\,\nu,$$
因此没有把近似面的法向空球当成真实面的空球。
真实 reach 下界 $\rho$ 必须另行支付。

令
$$c:=D_*/20+\eta_P+\eta_Q+\beta,\qquad D_0\le D_*.$$
若 $0\le\nu<1$，以下两条纯代数不等式足以给
$\delta_{\rm hold}\ge .05D_0$：
$$
\widetilde d(1-\nu)\ge c,\qquad
2\rho-\widetilde d(1+\nu)\ge c.             \tag{10.3}
$$
等价地，
$$
\boxed{
\frac{c}{1-\nu}\le\widetilde d
\le\frac{2\rho-c}{1+\nu},\qquad
\operatorname{reach}(S)\ge\rho,\quad D_0\le D_*.
}                                                         \tag{10.4}
$$
该区间非空恰需 $c\le\rho(1-\nu)$。
它包含管长以内的原预算，并在有余量时允许
$\widetilde d>\rho$。对称保持时可取 $\nu=\beta=0$；
若两点各有 $C^0$ 误差 $\eta_0$，这里仅出现 $2\eta_0$。

### 10.3 当前加权候选的浮点预算示例

下面只展示 (10.1) 对实际待求候选有用，**不是几何认证或精确解**。
来源是
[同一实际样条诊断](../notes/2026-11-10-fourfold-body-geometry-diagnostic.md)
第 7 节及其小型 JSON；对应 $\mu=4\sqrt2$、物理振幅 $\varepsilon=.06$
的 weighted-radius Newton 检查点。
完整有限 body 的 1344 个径向点、512 个角点读数为
$$
2R_s=2.314818623525,\quad
d_s=.126394312682,\quad
K_s=8.078395721864,\quad
\sigma_s=.820112498934.
$$
因此普通腰差比例为 $d_s/(2R_s)\approx5.4602253\%$。
把采样极值代入的
$$\rho_s=\min\{\sigma_s,1/K_s\}=.123786954048$$
只是 reach **代理**，并非 reach 下界；而且 $\rho_s<d_s$。
但空球公式的相应代理给
$$
\frac{2\rho_s-d_s}{2R_s}\approx5.2349499\%.
$$
在这些代理点值、直径下，达到 $5\%$ 需要的真实 reach 预算为
$$
\rho\ge\frac{d_s+.05(2R_s)}2=.121067621929,
$$
对应曲率上限约 $8.259846721$；
当前空球距离代理超过 $.05(2R_s)$ 约 $.005438664237$。
未来精确校正的点值、法向、直径与 reach 费用都必须放入 (10.4)，
不能将这段浮点余量直接当作验收。

该候选已采样到 $G\approx4.336828314>4$，所以这一路线应改用
R17 峰值 $13,14,15,16$ 的高峰固定标记，并另行证明真实移动主体
$G<13$；不能沿用要求 $G<4$ 的低峰标签。采样最大值小于 13
本身也不是这一连续全域上界的证明。
当前完整实际非均值度量残差约 $.006970496060$，Newton 尚未收敛，
有限体也未接成带固定平帽的闭面；以上示例不改变这些求解状态。
