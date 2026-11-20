# R138 补篇：互补 Gram 的谱范数与原体能量

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

本篇只改善同一真实 Qrepair 的原 $p=1,q=K$ 体能量比较，保持原角图、
drift、完整 mean、$H$ source、外端提升和所有原边界。
它不给任何新数值常数置 true，也不重算旧 X 的 `C_E=32.133...`。
所用原式是[V.10–V.15](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)、
[LC 的互补矩阵](R138-supplement-localized-eta-balanced-energy-and-root-capacity.md)、
[X.21 的实际闭行预算](R138-supplement-complete-physical-residual-multiplier-budget.md)
以及[GB.18–GB.24](R138-supplement-capped-curvature-Hhalf-Grushin-and-root-budget.md)。

## 1. 同一个未加权能量的准确最大特征值

沿用 $s=\Theta_\phi=v/m>0$、$\eta=-\gamma m>0$、$\kappa=Kv^2\ge0$、
$M=1+u^2+\kappa$、$\sigma=G\cdot n>0$。设
$\delta=b-uc$、$Q=\delta^2+\kappa c^2$，$w=\omega\circ\Theta$，
$D_rw=(\partial_r-d\partial_\phi)w$、$H^\Theta=H\circ\Theta$。
所有背景系数在 moving 表示时按同一 $\Theta$ 拉回。

V.10 和原角式为

$$
D_rw+\gamma uH^\Theta
 =e[-\delta X+(u\delta-\kappa c)Y],\qquad
w_\phi-sH^\Theta=sa[-cX+(\delta+uc)Y],\qquad e=a\gamma.
\tag{SG.1}
$$

将两个平方 $|D_rw+\gamma uH^\Theta|^2$ 和
$K|w_\phi-sH^\Theta|^2$ 的 $d\phi$ 积分换回真正 $d\theta$，
相对于原密度 $ea\sigma Q$ 的两个 Gram 为

$$
\frac{1}{\sigma|v|}\{\eta A+\eta^{-1}B\},\qquad
A=\begin{pmatrix}1+u^2&-u\sqrt\kappa\\-u\sqrt\kappa&\kappa\end{pmatrix},
\quad
B=\begin{pmatrix}\kappa&u\sqrt\kappa\\u\sqrt\kappa&1+u^2\end{pmatrix}.
\tag{SG.2}
$$

这里 $A,B\succeq0$，$A+B=MI$，$\operatorname{tr}A=M$、$\det A=\kappa$。
所以它们同向对角化，两个 $A$ 特征值为
$(M\pm\sqrt{M^2-4\kappa})/2$。两个 Gram **合起来**的准确最大特征值是

$$
\boxed{\quad
c_{\rm sp}(r,\phi)=
\frac{M(\eta+\eta^{-1})+
 |\eta-\eta^{-1}|\sqrt{M^2-4\kappa}}
 {2\sigma|v|}.
\quad}
\tag{SG.3}
$$

$M^2-4\kappa\ge0$ 来自 $M\ge1+\kappa$。
根端 $K=0$ 按连续极限解释，不需要除以 $K$，也不改变有限能量域。
本次没有给梯度能量加入径向权 $\alpha$ 或新的角依赖权，
所以不引入权的径向/角导数或任何新接口项。

旧 V.11 逐点用的是两个 trace 之和

$$
c_{\rm tr}=\frac{M(\eta+\eta^{-1})}{\sigma|v|}.
\tag{SG.4}
$$

例如 $\eta=1$ 时，(SG.3)准确为 $c_{\rm tr}/2$。
一般由 $\sqrt{M^2-4\kappa}\le M$ 得

$$
c_{\rm sp}\le
\frac{M}{\sigma|v|}\max(\eta,\eta^{-1}),\qquad
\frac{c_{\rm sp}}{c_{\rm tr}}
\le \frac{\max(\eta^2,1)}{1+\eta^2}.
\tag{SG.5}
$$

因此，若已经有同一完整真实正区的 $r^{-1}\le\eta\le r$、$r\ge1$，
可纯解析取

$$
C_{\rm sp}\le\frac{r^2}{1+r^2}C_E^{old}.
\tag{SG.6}
$$

这里需要 actual $-\gamma m$ 的全区间两侧界；metric 参数 $\eta_0$、
reference speed、仅负区 optical speed 或几个采样点均不满足该前提。
当前检查过的 WHVA/WOBSA/GH 小摘要未给这一 whole actual 两侧 scalar，
故本合同不把(SG.6)登记为已付数值改进。

## 2. 完整 H source 保持原常数

原两个梯度的 $H$ 修正组成同一 Hilbert 直和，其准确平方积分为

$$
\int\bigl(\gamma^2u^2+Ks^2\bigr)|H^\Theta|^2\,drd\phi
=\int\left(\frac{\gamma^2u^2}{s}+Ks\right)|H|^2\,drd\theta.
\tag{SG.7}
$$

所以直接沿用旧完整 $C_H$，不重求 mean、source、physical angle 或任何旧传播。
若 $C_{\rm sp}\ge\sup c_{\rm sp}$，在同一 Hilbert 直和使用 Minkowski 得

$$
\boxed{\quad
\left[\int\bigl(|D_rw|^2+K|w_\phi|^2\bigr)\,drd\phi\right]^{1/2}
\le\sqrt{C_{\rm sp}}\sqrt{\mathcal E}
       +\sqrt{C_H}\,\|H\|_{L^2_rL^2_\theta}.
\quad}
\tag{SG.8}
$$

归一化角积分时两侧同除 $\sqrt{2\pi}$；常数不变。
独立 $H$ mean 仍在(SG.7)–(SG.8)中。这里的向量范数没有环境维数损失。

原同一 drift $\psi_r=-d(r,\psi)$、$\psi(R)=\mathrm{id}$ 及
$\Gamma^{-1}\le\psi_\xi\le\Gamma$ 给

$$
\mathfrak G_{\rm cap}[v_*]^{1/2}
\le\sqrt\Gamma\{
 \sqrt{C_{\rm sp}}\sqrt{\mathcal E}+\sqrt{C_H}\|H\|_2\},
\qquad v_*=(\omega\circ\Theta)\circ\psi.
\tag{SG.9}
$$

这是原 GB.18 的相同 $p=1,q=K$ 能量，只把系数比较的 trace 换成谱范数。
原截顶曲率、环境零模、外端 $8/5$、composition 因子、原弱核能量资格均原样适用。
没有从 R141 hybrid 取得任何真实几何身份。

## 3. 一个完整闭行的可算谱上界

对一个原闭行，使用原同 Qrepair 的完整上、下界

$$
|u|\le U,\quad v_-\le|v|\le V,\quad
0\le K_-\le K\le K_+,\quad
0<\gamma_-\le\gamma\le\gamma_+,\quad
0<m_-\le|m|\le m_+,\quad\sigma\ge\sigma_-=2/5.
\tag{SG.10}
$$

定义仅为新目标私有中间量的

$$
t_-=\gamma_-m_-,\quad t_+=\gamma_+m_+,\quad
\overline M=1+U^2+K_+V^2,\quad
\underline\kappa=K_-v_-^2,\quad
\overline\Delta=\sqrt{\overline M^2-4\underline\kappa}.
\tag{SG.11}
$$

则该整行可取

$$
\boxed{\quad
C_i=\max_{t\in\{t_-,t_+\}}
 \frac{\overline M(t+t^{-1})+
           \overline\Delta|t-t^{-1}|}{2\sigma_-v_-}.
\quad}
\tag{SG.12}
$$

**证明。** 对固定真实 $A,B$，$\eta\mapsto\eta A+\eta^{-1}B$ 是 Loewner 凸函数，
所以其最大特征值在 $[t_-,t_+]$ 的最大值由两个端点支配。
固定正 $t$ 后，(SG.3)的分子对 $M$ 单调增加、对 $\kappa$ 单调减少；
故可用 $\overline M$ 与 $\underline\kappa$。最后用 $\sigma_-,v_-$ 支配分母。
这不是分别对 $t+t^{-1}$ 与 $|t-t^{-1}|$ 取不同端点后拼装，
也没有把独立背景参数误当成彼此有利相关。

因为 $\overline M\ge1+\underline\kappa$，根号内非负。
数值时可先把有向上端与0取最大，再开方形成 $\overline\Delta$ upper；
不能因整个 rounded ball 的下端稍负而把真实正项删掉。
所有 denominator 先以原完整 signed lower 核严格正。

在根 germ 只对真正 $r\ge r_*$ 的正侧取 $K_-=0$，$K_+$仍用原完整 real球的绝对上界。
对 body 的4650行，$K_-$可取其原正下端；这一步利用的是已有 $K$，不是重做曲率目标。
新系数最大值可保守覆盖 $[r_{lo},R]$，但没有把真正根替换为 $r_{lo}$。

## 4. 与旧 X producer 的精确对应

旧 `fourfold_codazzi_physical_energy_budget.py` 的 `original_background`
及 `repaired_background` 从相同输入取

| 字段 | body 原记录 | root germ 原记录 |
|---|---|---|
| $U,V$ | `bounds.U_A0`, `bounds.V_A0` | `moving_U_derivative_Astrip[0]`, `moving_v_derivative_Astrip[0]` |
| $v_-$ | `bounds.real_physical_inverse_gap` 的 lower | `angle_inverse.bounds.v_gap` 的 lower |
| $m_-,m_+$ | `bounds.mean_v` 的 signed real球 | `moving_mean_v.real` 与已有 `modulus_upper` |
| $\gamma_-,\gamma_+,K_\pm$ | `intrinsic.gamma`, `intrinsic.K` | `complex_intrinsic_coefficients` 的对应 real球 |

同修补费用 $\varepsilon=4\cdot10^{-18}$ 只按原证明施加：
$U,V,m_+$ 加 $\varepsilon$，$v_-,m_-$ 减 $\varepsilon$；$\gamma,K$ 是同一 intrinsic，
不另改变。全部已付 signed记录只读，不重新求旧 Fourier/A0 norm、primitive、mean、
metric derivative、angle inverse、frame 或 residue。

旧 X 主循环的 `ce` 恰是

$$
C_{E,i}^{old}=\frac{\overline M}{\sigma_-v_-}
                    \left(\gamma_+m_++\frac1{\gamma_-m_-}\right)
=\frac{\overline M}{\sigma_-v_-}(t_++t_-^{-1}).
\tag{SG.13}
$$

新目标是(SG.12)，不能在新 consumer 中再求(SG.13)并将其 max 重新发布为旧 `C_E`。
旧全域 `C_E` 已完整保存，只以整个 X 对象读取和保留。
由于 pointwise 谱范数不超过 pointwise trace，旧 `C_E` 本身也仍是新目标的一个合法 upper；
整4651片的新 $\max_iC_i$ 完成后可与该**已保存** upper 取较小值作为最终 $C_{\rm sp}$。
这不把未完成片补成旧值，亦不允许跳过新目标的任何一片。

本目标不需要原7722 angular行或 candidate shards：它不包含旧 residual/defect传播，
只消费已完整保存的4650 positive行与一个 whole-root germ。
故最小 historical restoration 是原 positive4+germ1，共5件。
原 positive 完整容器、4650 cover、3594接口及原真实根/参数身份仍必须全读核定。

## 5. 只改变原 GB 中受 C_E 影响的量

全部所需旧 scalar 仍来自完整 X、Y、GB actual及其 execution，不用浮点展示值：

- X：`new_scalar_suprema.C_H`、`A_Theta`，`complete_derived_energy_bounds.Gamma`、`h_B`；
- Y：`new_scalar_suprema.E_0`、`E_1`，`complete_derived_energy_bounds.h_E`、`r_E`、`r_B`；
- GB：`new_records.wB_half_upper`、`aBB_upper`；原 body三门与完整 scope保持。

将新完整 $C_{\rm sp}$ 保存并读回以后，定义

$$
w_{E,\rm sp}=\frac52\Gamma\sqrt{A_\Theta}
                    (\sqrt{C_{\rm sp}}+\sqrt{C_H}h_E).
\tag{SG.14}
$$

$w_B$ 不含 $C_E$，因此直接读取旧 GB 的 `wB_half_upper`，不重算此旧目标。
新的两个体费用是

$$
\begin{split}
a_{EE,\rm sp}&=E_0w_{E,\rm sp}^2+E_1w_{E,\rm sp}h_E,\\
a_{EB,\rm sp}&=2E_0w_{E,\rm sp}w_B
                +E_1(w_{E,\rm sp}h_B+w_Bh_E).
\end{split}
\tag{SG.15}
$$

$a_{BB}$ 同样不变，只读旧 GB `aBB_upper`。原 $r_E,r_B$ 使用 Y 已付
$H^{2/3}$ 路线的原值；本次没有将新 $H^{1/2}$ 体量冒充新的 root trace量。
如需以后改善那些 root量，应另声明相应目标，不能默默重写旧 Y。

读回全部新球后，取新旧各自保存的 upper 构成

$$
M_{\rm sp}=\begin{pmatrix}
2-a_{EE,\rm sp}&-a_{EB,\rm sp}/2\\
-a_{EB,\rm sp}/2&1-a_{BB}
\end{pmatrix}.
\tag{SG.16}
$$

只有其三项严格正门实际通过，才能另外形成

$$
C_{{\rm allow},\rm sp}=
\frac{\det M_{\rm sp}}
 {2(r_E,r_B)\operatorname{adj}(M_{\rm sp})(r_E,r_B)^T}
\tag{SG.17}
$$

的有向 **lower** 并保存读回下端。原 GB.24 的半余量证明原样适用，
没有新增根端边界条件。分母非正、真门未过或未完成时不能发布该条件目标。

## 6. 新完整组合合同及用途边界

新最小数值合同可以只声明以下4个完整 upper：
`C_spectral_upper`、`wE_spectral_upper`、`aEE_spectral_upper`、`aEB_spectral_upper`，
以及条件性第5个 `root_allowance_spectral_lower`。
完整新谱上界的4651片逐片消费并保存累计 max，全部完成才读回形成下游；
下游各球也必须保存并读回后参与后续严格门。
旧 `C_E`、$C_H$、$w_B$、$a_{BB}$、$r_E,r_B$ 及原成功/失败门均仅读引用。
没有旧 producer、geometry/residual ODE、旧 target重复求值或新数组发布。

这些是改变了明确能量比较的新预算，所以固定原 GB 的 RS.20–RS.21 不会自动将它排除。
不过 RS.19 的根必要下界仍然存在；若实际单积分 $T$ 已使根系数本身超过2，
即使令全部非负体费用为0也无法通过同一标量接收器门。
在评估新大矩阵或新体预算之前，应先消费那个完整 $T$，避免重复一条已被精确必要条件
排除的路线。联合使用更多真实 PDE 可达迹关系或原直接逆构造不受这种充分预算排除。
