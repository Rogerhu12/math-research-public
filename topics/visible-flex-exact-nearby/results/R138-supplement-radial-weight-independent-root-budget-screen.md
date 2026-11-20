# R138 补篇：独立于径向权的完整根接收器必要筛查

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

本篇给 LC 局部 η 平衡容量路线的一项**尚未求值的新标量筛查**。
所用原结论分别为[LC 平衡能量与准确容量](R138-supplement-localized-eta-balanced-energy-and-root-capacity.md)、
[完整 relative 根接收器](R138-supplement-original-high-compression-and-relative-root-receivers.md)、
[实际原 high97 下界与41球](R138-supplement-actual-original-high-root-lower-bound.md)、
[实际 signed96/97 根型](R138-supplement-actual-negative-original-root-96-97-form.md)、
[实际 GB 体吸收](R138-supplement-actual-capped-Hhalf-body-absorption-and-root-allowance.md)，
以及[X 完整物理预算](R138-supplement-complete-physical-residual-multiplier-budget.md)。
它不重新计算原96/97三个矩阵项、原high41个scalar或任何旧几何目标。
准确原算子仍为同一 Qrepair 的真实 $DF$，原 low1..96/high97 边界保持不变。
下述排除若被新完整积分触发，只排特定能量接收器充分门，绝不排原边值问题、
真实可达根迹或其有界逆。

## 1. 正高压缩的加权消元也保留同一必要负部

令原根对称型在 normalized real $z$ 坐标的算子为

$$
K_* =\begin{pmatrix}A_L&C^*\\C&D_H\end{pmatrix},\qquad D_H>0.
\tag{RS.1}
$$

取原 $z_{96}=\sqrt2\sin(384\phi)$、$z_{97}=\sqrt2\sin(388\phi)$。
原完整两模结果给同一实际算子的三个球，并已严格推出

$$
M_{12}>189/10,\quad M_{22}<601/250,\quad M_{11}<457/1000.
\tag{RS.2}
$$

这些数据是完整原球的有理放宽，而不是重算它们。任意 $0<\vartheta\le1$、
任意有限接收器 $W$ 若用于准确完成平方，必须至少满足

$$
W^*W\succeq C^*(\vartheta D_H)^{-1}C-A_L.
\tag{RS.3}
$$

特别地，任何 $\mathfrak b_*(z)\ge-\|Wz_L\|^2$ 的全根数据下界，
先对真正 $z_H$ 取最小值便要求(RS.3)的 $\vartheta=1$ 版本。

由 $D_H$ 的 Hilbert 空间 Cauchy--Schwarz，

$$
\langle C z_{96},D_H^{-1}Cz_{96}\rangle
\ge \frac{|\langle Cz_{96},z_{97}\rangle|^2}
               {\langle z_{97},D_Hz_{97}\rangle}
=\frac{|M_{12}|^2}{M_{22}}.
\tag{RS.4}
$$

因而准确的压缩乘子逆、其有限 rank 修正及真正 $D_H^{-1}$，均不消去

$$
\|Wz_{96}\|^2>
\frac{(189/10)^2}{601/250}-\frac{457}{1000}
=148+\frac{79843}{601000}>148.
\tag{RS.5}
$$

这里没有先把 $D_H$ 降为统一 scalar $\lambda_H I$。
若使用更保守的正下界算子替代 $D_H$，其逆更大，(RS.5)仍然成立。
该估计保留全部 high 输出；没有把 $C$ 截成单一97模。

## 2. 同一根代数测试函数的完整范数

对完整根公式取 $z=z_{96}$、$\mathsf H=0$，只将其当作根代数测试。
不声称这个数据来自某个正区齐次解。记 $n=384$、
$R=\sqrt2\cos(n\phi)$，以及已付的

$$
b=\rho Y,\quad g_m,\quad D>17/20,\qquad
b_0<1,\quad b_1<2,\quad b_2<2,\quad (g_m)_0<3.
\tag{RS.6}
$$

下标表示对应完整 $C^j$ upper；这些有理放宽只读原high41个保存球。
原 mean rank 和两个 primitive 公式给

$$
\ell_{96}=D^{-1}\langle b'R\rangle\cdot\ell,\qquad
\omega_{96}=-bR+I(b'R-g_m\ell_{96}),\qquad
\omega_{96}'=b(nz_{96})-g_m\ell_{96}.
\tag{RS.7}
$$

所有角积分均为 $d\phi/(2\pi)$；$I$ 是删除环境零模后的真正 primitive，
其 $L^2\to L^2$ 范数为1。原对称性保证这里 $\langle bR\rangle=0$；
非齐次 $\mathsf H$ 的 mean 并未由此删除。

对平均 functional 先在已知系数上积分分部，得到

$$
|\ell_{96}|\le \frac{20}{17}\min(b_1,b_2/n).
\tag{RS.8}
$$

对 $I(b'R)$ 用输出近远分块，分界 $n/2=192$：近输出为 $|k|\ge192$，
远输出为 $0<|k|<192$；$k=0$ 被 $I$ 准确删除。近输出有
$\|I\|\le1/192$。远输出与每个输入符号的谱隙至少192，
Sylvester 积分给每支 $b_2/192$；两个输入符号合成付 $\sqrt2$。
两输出子空间正交，所以

$$
\|I(b'R)\|_2
\le\left[(b_1/192)^2+
  \min\{b_1,\sqrt2 b_2/192\}^{2}\right]^{1/2}
<\frac{\sqrt{12}}{192}<\frac1{50}.
\tag{RS.9}
$$

这是对已知 $b'$ 的导数费用，不对未知输入求导。环境零模在 $I$ 中自然为零；
远区未把全部环境频率错误地限为四的倍数。由(RS.8)，

$$
(g_m)_0|\ell_{96}|<3\frac{20}{17}\frac2{384}
=\frac5{272}<\frac1{50}.
$$

因此可以固定使用下面两个新的**纯解析有理放宽**，无须求值新的范数目标：

$$
\boxed{\quad \|\omega_{96}\|_2<26/25,
       \qquad\|\omega_{96}'\|_2<385.\quad}
\tag{RS.10}
$$

## 3. 任意径向权所必须承担的准确容量费用

取任意局部根段 $[r_*,r_c]$，其外值自由；任意正径向权 $\alpha$。
沿用 LC 的真实 $\eta=-\gamma m>0$、$K\ge0$，以及

$$
p=\alpha/\eta,\quad q=\alpha\eta K,\qquad
C_E\ge\sup_{r,\phi}
       \frac{\alpha(r)(1+u^2+Kv^2)}{\sigma|v|}.
\tag{RS.11}
$$

$C_E$ 可以是任何实际采用的完整 upper；不假定它等于最优 supremum。
对任一反射轴 $\phi_+=0$、$\phi_-=\pi/4$，$u=0$，且
$\Theta(r,\phi_\pm)=\phi_\pm$。设

$$
v_\pm(r)=v(r,\phi_\pm),\qquad G_*={222}/{125},
\quad h(r)=G_*\min_{\epsilon\in\{+,-\}}
              \frac{|v_\epsilon(r)|}{1+K(r)v_\epsilon(r)^2}.
\tag{RS.12}
$$

原同一 $p=\tfrac12e_z$ 已付 $|G|<G_*$ 和 $\sigma>0$。逐径向点直接给

$$
\frac{\alpha(r)}{C_E}
\le \inf_\phi\frac{\sigma|v|}{1+u^2+Kv^2}
\le \min_\pm\frac{\sigma(r,\phi_\pm)|v_\pm|}{1+Kv_\pm^2}
\le h(r).
\tag{RS.13}
$$

因而无需新几何 ODE、无需重新认证旧轴坐标或 support，就已给任意权的共同限制。
两个 $v_\pm$ 是同一完整 Qrepair 的轴投影，包含独立 moving mean 和全部32模。

固定一个严格正有理长度 $\ell_0<R-r_*^{\rm hi}$，令

$$
f(r)=\left(1-\frac{r-r_*}{\ell_0}\right)_+.
\tag{RS.14}
$$

$f(r_*)=1$；它是合法 $H^1$ 比较函数。若 $r_c<r_*+\ell_0$，只限制到原局部段，
其外值仍自由；若 $r_c\ge r_*+\ell_0$，其后准确为零。
没有给原方向添加任何外 Neumann 或 Dirichlet 条件。

设某个新完整正数 $T$ 满足

$$
\boxed{\quad
T\ge \int_{r_*}^{r_*+\ell_0} h(r)
 \left[\frac{(26/25)^2}{\eta(r)\ell_0^2}
       +385^2\eta(r)K(r)
          \left(1-\frac{r-r_*}{\ell_0}\right)^2\right]dr.
\quad}
\tag{RS.15}
$$

它是单一新径向积分目标；原根位置保持真实区间，不能用 midpoint 替代。
把 $f(r)\omega_{96}(\phi)$ 代入准确加权能量，由(RS.10)、(RS.13)得到

$$
\frac{\mathcal G_{p,q}[f\omega_{96}]}{C_E}\le T.
\tag{RS.16}
$$

该式对所有局部段同时有效，因为截短只删除非负能量。
它也对所有正径向权同时有效；没有为某个选择的 $\alpha$ 偷换另一权的容量。

取 $c=Wz_{96}/\|Wz_{96}\|$。原准确 dual root 公式在 $\mathsf H=0$ 时给

$$
|\langle P_c',\omega_{96}\rangle|=|\rho|\|Wz_{96}\|.
\tag{RS.17}
$$

$P_c'$ 因周期导数严格 mean-zero，故 LC 完整容量对偶（或任一合法的更大有限
Gram upper）必须满足

$$
\mathcal N_{p,q}(P_c')^2
\ge\frac{\rho^2\|Wz_{96}\|^2}
           {\mathcal G_{p,q}[f\omega_{96}]}.
\tag{RS.18}
$$

若所采用接收器仍以 LC.18 的原全域 $\Gamma$ 转授，第一能量系数因此有必要下界

$$
\boxed{\quad \alpha_E(W)^2>
                  \frac{148\Gamma^2}{T}.\quad}
\tag{RS.19}
$$

所有额外 $H$ source、mean 与 $P_c$ 的 $H^{1/3}$ 费用均为非负，不能抵消这个下界。
若改用另一套已付的两个 scalar Jacobian 比较，令它们平方根之积为 $\Lambda$，
同证给 $148\Lambda^2/T$。通常这两个全圈双向 Jacobian upper 都至少1，故
$\Lambda\ge1$。针对特别接收行的非 scalar 角变换估计属于另一个预算，未在此排除。

## 4. 可以直接检验的两项严格必要门

旧 GB 所选完整预算球给 $a_{EE}^{GB}>11/10$；旧 X 给实际采用的
$\Gamma>59/50$。这些是已经选择并保存的 upper 数值的事实，
**不宣称原实际误差的下界或所有可能预算的最优值**。
原第一吸收门需要 $a_{EE}^{GB}+\alpha_E(W)^2+\cdots<2$。

若新的完整积分上界满足 $T\le225$，则

$$
\alpha_E(W)^2>\frac{148(59/50)^2}{225}>\frac9{10},
\qquad 148\cdot3481=515188>506250.
\tag{RS.20}
$$

所以使用原 $\Gamma$ 与原 GB 预算的整个 LC 径向权/自由截段接收器路线不能过第一门。
这包括准确有限 Gram、真实高压缩逆和其压缩乘子修正；不需再制作那些矩阵来判断此事。

若更强地 $T\le160$，则不论另付的 scalar Jacobian 因子是否比原 $\Gamma$ 更紧，

$$
\alpha_E(W)^2>148/160=37/40>9/10
\tag{RS.21}
$$

仍排除同一 GB 预算下任何 $\Lambda\ge1$ 的这类 scalar 能量转授。
改变 GB 体误差预算、使用原 PDE 的更多可达根约束、联合处理根/体有符号型、
或走直接逆构造，不受本结论自动排除。

若 $T>225$，只说明本充分筛查未排除路线；不证明任何矩阵门、容量门或全逆成功。

## 5. 最小新消费者范围

一个可审的首目标可固定 $\ell_0=1/100$。它只消费原完整 positive4650 闭行和
whole-root germ 的 intrinsic/mean signed records；从原 exact dyadic candidate cubic
只形成两个新的线性投影 $\sum_jv_j$ 与 $\sum_j(-1)^jv_j$，并支付同 Qrepair 的完整
uniform $A_0$ 费用。它不调用旧轴、mean、X/Y、high41、两模或原 positive producer。

按所有原 intrinsic/candidate 接口拆分真正 $[r_*,r_*+1/100]$；首尾长度和
$r-r_*$ 保留 whole root 区间。每个完整 cell 的正 integrand 取有向 upper，
乘真实长度 upper 后求和，可直接得到(RS.15)；需要更紧时只能在首合同预先声明
固定子分片，不把半段成功当作完整目标。计算中始终有 $K\ge0$、$\eta>0$、
$v_\pm<0$ 的真正已付范围或新的显式 whole-cell admission。

最终只公开完整 $T$ 球、两个门的严格整球比较、覆盖/计数/hash、参数、原 whole
输入的只读引用和明确范围。候选投影系数、cell 数组、私有中间值不公开为新科学数组。
原已成结论全部保持其身份；新的成功运行亦不得被解释为本课题完成。
