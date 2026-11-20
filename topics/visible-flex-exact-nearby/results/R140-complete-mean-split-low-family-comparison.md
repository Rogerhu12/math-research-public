# R140：完整192/mean1低频族差比较及保核权的源段压缩

2026-11-20，`visible-exact-astra-ac637-20261120`。

**状态：本文的算子分块、四项完整误差界和源段压缩命题已证明；尚无新的科学数值。** 这是同一 W2C 低频族差项的另一套完整上界配方。它不改变原参数域，不删 mean，不删 primitive，不授有限逆。若旧配方触发 R139，只排除旧配方；本文的新完整上界仍须首次公共计算。

依赖为 [完整 W2C 候选](R133-supplement-complete-collar-Volterra-dual-feedback-candidate.md)、[固定配方必要预算](R139-necessary-budget-for-fixed-W2C-comparison.md)、原全实 delta 正侧证书，以及下述现有完整源公式。新的比较只替换 W2C family 和式中的低频项 `L`；其余 cross、trial、dual/primal 乘积及完整 signed centre 均不删。

## 1. 现有 AL 费用从哪里来

实际参数族仍为

\[
Q^\delta=Q^c+\delta Z,\qquad |\delta|\le10^{-8},
\tag{M1}
\]

固定原内禀参数 `eta_0` 和原 `nu`。`Z` 是同一个完整193状态方向，含独立偶 mean。它不是193个可独立选择的物理参数；`delta` 也不是允许随径向点改变的函数。中心与方向的65/193个系数、原连续修复和所有独立 affine jumps 保持其原定义。

现有 [assembly](../scripts/fourfold_codazzi_collar_dual_feedback_math.py) 的 `_family_panel_values` 对 AL 使用

\[
f_{AL}=384 f_d+f_{\rm local}+f_{\rm primitive}+f_{\rm mean\,column}.
\tag{M2}
\]

body 的 [完整 collar/family 模块](../scripts/fourfold_codazzi_true_collar_signed_packet_math.py) `complete_body_family_positive_fees` 原字读取每个旧 row 的 `local_a,local_e,local_b,drift,drift_phi`，并用完整正和

\[
\begin{aligned}
f_{\rm local}&=a+e+(1+k)b,\\
f_{\rm primitive}&=\frac B2\{E_1[U+E_0+k(V+E_0)]
 +(U_1+V_1)(1+k)E_0\},\\
f_{\rm mean\,column}&=\Gamma(1+k)E_1.
\end{aligned}
\tag{M3}
\]

记号定义见下一节。`384=4*96` 是输入最高角频率。随后 assembly 在每个 reference parent 上取所有相交旧 row 的最大费用，右乘同一 `S^{-1}` 的范数，并与一个同时包含192 nonmean和1 mean的标量 `G_f` 比较核复合。

原 body 输入的来源链是 [full_delta_positive_high_Volterra](../scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py) 的保存行：

\[
E_0=10^{-8}(H_0+\text{direction repair}_0),\qquad
E_1=10^{-8}(H_1+\text{direction repair}_1).
\tag{M4}
\]

`H0/H1` 是原完整响应包络。其 [原 source](../scripts/fourfold_codazzi_complete_response_repair_source.py) 的 `cubic_pair_norms` 对全部193实振幅求和，`H0` 还保留独立 mean 修正；这些量支配两分量的完整 Wiener 正和。完整系数差的旧 `local_*`、`drift`、`mean_own_rate` 由 [inflated](../scripts/fourfold_codazzi_repaired_positive_high_Volterra.py) 保存，当前消费只读复用，不重跑这个旧 producer。

这里至少有三种可区分的外包损失。

1. 对真实固定参数族的逐点包络，允许在不同位置取得各自最坏上界，是证明中的外包；不能把它解释为真的改变参数域。
2. parent 的 row 最大值把小段峰值赋给整段。第6节在保留完整 `(r,s)` 核权后压缩这一损失，绝不把乘法算子的 `L-infinity` 范数无条件换成 RMS。
3. 一个193维总费用配一个总 `G_f` 上界，允许最快角导项与最慢 mean 接收器同时取最坏值。实际角导在 mean 输入上为零，而 mean 输出有自己的完整方程。本节以下对这一损失作完整正交分块。

即使新配方更尖锐，也不能预先保证其数值通过 `1/128`。比较公式变尖锐与真正固定参数域变小是两件不同的事；本文只做前者。

## 2. 同一真实对象与所有 mean 项

本节始终使用**原 WVC 的角变量 `phi`**及其原归一化测度，Fourier波数为 `4j`、坐标周期为 `pi/2`。它是原 moving-angle 表示，不能直接等同物理角 `theta`；本文不作这两个角变量之间的替换，也不产生新的物理角 readout 界。所有下面的均值、`A0`、`L2`及角导都在同一原 `phi` 表示中。写

\[
\mathcal H_{96}=\mathcal H_N\oplus\mathcal H_0,
\qquad \dim\mathcal H_N=192,\quad\dim\mathcal H_0=1.
\tag{M5}
\]

`H_N` 包含 odd1..96和even1..96，`H_0` 是原系统保留的独立 even 常数。mean 基函数的范数为1，非零正弦/余弦基为 `sqrt(2) sin/cos`。这些是正交分块，不是删去一个变量；它也不把完整问题中的其他物理 density-mean 行与这个角零模混为一谈。

写中心为 `(u,v)`、完整误差为 `(e_u,e_v)=delta Z`，并记

\[
m=\langle v\rangle,\qquad e_m=\langle e_v\rangle.
\]

这里必须固定“中心算子”的精确定义。令 `G(Q;eta)` 表示把原 raw generator 的角主部速度槽显式写成 `eta` 的算子，且

\[
\mathscr G(Q;\eta)=\eta J_K\partial_\phi+\mathscr R(Q),
\qquad J_K=\begin{pmatrix}0&-K\\1&0\end{pmatrix}.
\]

其余项 `R(Q)` 包括由物理 mean 变分产生的 rank 列、全部有序 primitive及独立 mean 方程。原 W2C 使用的是同实际速度的 **hybrid trial**

\[
\begin{aligned}
\mathscr A^\delta&=\mathscr G(Q^\delta;\eta_\delta),&
\mathscr A_c^\delta&=\mathscr G(Q^c;\eta_\delta),&
\eta_\delta&=-\gamma(m+e_m),\\
\Delta A_L^\delta&=\Pi_L(\mathscr A^\delta-\mathscr A_c^\delta)\Pi_L,
&\Pi_L&=P_N+P_0.
\end{aligned}
\tag{M5a}
\]

**本文所有四块费用都只用于(M5a)的 `Delta A_L`。** 这个 trial 并不是把 `Q^c` 当作另一个物理背景后自然线性化所得的 `G(Qc;eta_c)`。实际 eta 函数相同是 trial 的定义，不能由两个 interval 数值相等反推。也不因此把自然背景线性化的能量结论授予该 trial。

现有源码对这一点有直接绑定。

- [signed packet模块](../scripts/fourfold_codazzi_true_collar_signed_packet_math.py) 的 `_complete_centre_packet(...,actual_eta,...)` 分别保存 `mc=vr[0]` 和显式输入的 `eta=actual_eta`；它不从 `mc` 重建速度。
- 同模块 `complete_true_collar_packet` 从原完整 full-family optical-speed记录给这个参数，保留 `actual_eta_identity='-gamma*m_delta; same function in A and A_c'` 以及 `centre_mean_is_separate_from_actual_eta=True`。
- [assembly](../scripts/fourfold_codazzi_collar_dual_feedback_math.py) 的 `prepare_complete_kernel_context` 在body把 `row['complete_delta_bounds']['radial_speed']` 传入上述 packet，中心 `u/v` 则来自原 repaired cubic。`_complete_family_increment` 因此明确令增量 `eta=0` 并要求 `actual_eta_is_identical_in_both_operators=True`；其有符号 family entry消费这个资格。body费用入口也显式要求 `same_actual_eta_retained=True`。

为排除记号误读，若改成比较两个自然 raw generators，则确实有

\[
\mathscr G(Q^\delta;\eta_\delta)-\mathscr G(Q^c;\eta_c)
=(\mathscr A^\delta-\mathscr A_c^\delta)
-\gamma e_mJ_K\partial_\phi,
\qquad \eta_c=-\gamma m.
\tag{M5b}
\]

这个额外主部差在nonmean输入上通常不为零；完整低频界需另付至多 `384 Gamma kappa Em`，不能套用本文(M13)而把它删掉。本文不执行(M5b)的比较。即便采用(M5a)，下面(M8)的真实 **mean-input rank 差仍完整保留**。

令 `I=partial_phi^{-1}`，只对中间零均值函数作用，且

\[
\|I\|_{L^2_0\to L^2_0}\le1/4.
\tag{M6}
\]

`Delta A_L` 所来自的同eta余项中，完整 primitive 差仍是三个有序项

\[
-2\beta\{\partial_\phi e\,I(u x_u+Kv x_v)
 +\partial_\phi(u,v)\,I(e_u x_u+Ke_v x_v)
 +\partial_\phi e\,I(e_u x_u+Ke_v x_v)\}.
\tag{M7}
\]

每次 `I` 都先去掉其**整个实际输入**的零频；中间频率可以从1开始，故此处只使用1/4，不能套用旧 high-band 分母。最终 low 投影在整个有序乘积之后。二次全96误差仍在(M7)第三项及下面的反应系数中。

mean-input列的额外项是

\[
\gamma\,(K\partial_\phi e_v,-\partial_\phi e_u)
\,\langle x_v\rangle.
\tag{M8}
\]

它的输出均值为零，但完整非均值输出必须支付。mean **输出**则是同一原 `phi` 表示中的完整原方程

\[
\langle\mathscr A_Qx\rangle_v
=\beta(1-\langle u_Q^2+Kv_Q^2\rangle)\langle x_v\rangle
-2\beta m_Q\langle u_Qx_u+Kv_Qx_v\rangle.
\tag{M9}
\]

这与现有 `_centre_mean_row` / `_family_mean_row` 的归一化矩阵逐项一致。它包含 drift、local和有序 primitive 在输出均值上的完整相消；不能把 mean 当作零输出。

## 3. 每个完整旧 row 的四个上界

下列均为同一闭 row 上的完整非负上界；旧记录只读消费。

| 记号 | 所控制的真实量 / 现有字段 |
|---|---|
| `B,Gamma,k` | `abs(beta), abs(gamma), abs(K)` 的原 intrinsic 包络 |
| `U,V,U1,V1,Vperp` | 中心 `u,v,partial_phi u,partial_phi v,v-m` 的原 `U_A0,V_A0,U_phi_A0,V_phi_A0,V_nonmean_A0` |
| `M` | 原 `abs(mean_v)` |
| `E0,E1` | 原 `full_delta_A0,full_delta_angular_A0`，支配完整两分量正和 |
| `Em` | 原 `independent_mean_variation_bound`，且也可取与 `E0` 的较小完整界 |
| `a,e,b,d` | 原 `local_a,local_e,local_b,drift` |
| `c00` | 原完整 `complete_delta_fees.mean_own_rate` |

设

\[
\begin{aligned}
\kappa&=\max(1,k),& E_N&=\min(E_0,E_1/4),\\
C_0&=(U^2+k^2V^2)^{1/2},& C_1&=(U_1^2+V_1^2)^{1/2},\\
C_\perp&=(U^2+k^2V_\perp^2)^{1/2}.
\end{aligned}
\tag{M10}
\]

`E_N` 支配两分量非均值误差的 `L2` 正和：全部非零频率至少为4。`Em` 与 `E_N` 各自保留，未宣称两者独立或同时达到最坏值。

局部2×2乘子界可取

\[
\ell=\sqrt{\max(a+kb,b+e)\,\max(a+b,kb+e)}.
\tag{M11}
\]

这是正矩阵 `[[a,kb],[b,e]]` 的完整行列 Schur 界。它不超过(M3)所用四项总和。完整三项 primitive 的全输入界可取

\[
P=\frac B2\{E_1(C_0+\kappa E_0)+C_1\kappa E_0\}.
\tag{M12}
\]

**命题1。** 精确定义为(M5a)的同一完整 `Delta A_L` 在(M5)上的四个块可由

\[
\begin{aligned}
c_{NN}&=384d+\ell+P,\\
c_{N0}&=\sqrt{(kb)^2+e^2}
 +\frac{Bk}{2}\{E_1(V_\perp+E_N)+C_1E_N\}
 +\Gamma\kappa E_1,\\
c_{0N}&=2B\{(M+E_m)\kappa E_N+E_m C_\perp\},\\
c_{00}&=\text{原完整 mean\_own\_rate 差记录}
\end{aligned}
\tag{M13}
\]

同时支配。所有式子都适用于任一固定的原真实参数值，且上界统一于整个原域。

**证明。** 对 `NN` 块，`partial_phi` 在输入带1..96上的范数为384；(M8)因输入 mean=0而严格为零。局部乘子用(M11)。对(M7)，向量乘子的范数用两分量欧氏范数，右侧行乘子用同样的欧氏范数，再用(M6)，得(M12)。这里用了 `||(e_u,Ke_v)||<=kappa E0` 和 `||partial_phi e||<=E1`，未把每分量都另收费一次完整 pair bound。

对 `N0` 块，输入是单位常数 even1，故角导项**严格为零**。局部列的两分量界为 `kb,e`。在(M7)的右乘子中，`I(Kv)` 实际只看 `v-m`；`I(Ke_v)` 实际只看 `e_v-e_m`。应用(M6)、完整 `Vperp` 与 `E_N`，给出(M13)第二行的 primitive 费用。(M8)的完整向量范数由 `Gamma*kappa*E1` 支配。最终 nonmean 投影是压缩，不会增加这些范数。

对 `0N` 块，(M9)展开为

\[
-2\beta\{(m+e_m)\langle e_u x_u+Ke_vx_v\rangle
 +e_m\langle u x_u+Kv x_v\rangle\}.
\]

输入 `x_v` 的均值为零，因此上述 `v,e_v` 在内积中分别仅为 `v-m,e_v-e_m`。Cauchy–Schwarz给出(M13)第三行。

对 `00` 块，精确差为

\[
-\beta\{\langle\Delta(u^2+Kv^2)\rangle
 +2K(2m e_m+e_m^2)\}.
\tag{M14}
\]

这正是旧 `mean_own_rate` 差记录所界定的完整量；该记录直接消费。至此四个块齐全。证毕。

### 根 collar 的同式实例

根 collar 仍用现有完整 signed packet，真实根不改成端点。原 `full_family_U/V_angular_norms` 是完整正和，因而支配中心相应范数；原方向数组与相同 `delta` 给出 `E0,E1`。完整193误差 packet 的 `em` 给出 `Em`，原中心 `mc` 给出 `M`。`Vperp` 可由完整中心非零 `v` 系数求正和并与原 `V` 比较取小；这只是新私有系数包的一个范数界。

根的 `a,e,b,d` 由原完整 family 差的相同二次公式形成；(M14)用其 `S_mean`、`em` 和同一中心 mean 完整包围。这里不把旧193个误差上界恢复成带符号的真实方向，也不从一个总和范数反推出中心范数。即使 intrinsic `K` 的包络跨零，上式使用 `k>=abs(K)` 仍有效。

## 4. S 与全部193观察的准确分块

固定参考在不同非零 `j` 上是原2×2块，而独立 mean 的参考生成器为0。因此

\[
G_f=G_N\oplus G_0.
\tag{M15}
\]

`G_N` 的输出包括192维 body和原96 root-odd、96 weighted-outer-even观察，共192个原观察。`G0` 的输出包括真实 mean body和原独立 root-mean观察。二者的原子输出正交，合计仍为193。

若参考 `S` 的偶分量尺度为原 `q(s)`，则右输入变换的完整块界为

\[
\sigma_N(s)=\max(1,q(s)^{-1}),\qquad
\sigma_0(s)=q(s)^{-1}.
\tag{M16}
\]

令 `a_{alpha beta}=c_{alpha beta} sigma_beta`。只有输入端乘(M16)；输出端的原 `S` 已在 `G_N/G0` 核内，不能再乘一次。

mean 接收器的精确 body 核为

\[
G_0(r,s)=-q(r)\,\mathbf 1_{r\le s},
\tag{M17}
\]

其 root-mean原子核为 `-1`。这里的单向 primitive 到真实 `R`，没有用 collar 长度代替整个 mean 接收域。

nonmean whole-box 核沿原96模态取完整2×2算子界，但不再把(M17)混入同一个 `max`。每个模态的 root与weighted-outer两行一起估计，再沿模式取最大，仍为整个192维 Hilbert 观察块的界，绝不是抽样列检查。

## 5. 完整192/mean1正比较

将既有径向域记为 `I_i`，数量不超过155。选择对**完整产品盒**及原子行有效的上界

\[
g^\alpha_{ik}\ge
\sup_{(r,s)\in I_i\times I_k}\|G_\alpha(r,s)\|,
\qquad
t^\alpha_k\ge\sup_{s\in I_k}\|G_{\alpha,\rm atoms}(s)\|,
\quad\alpha\in\{N,0\}.
\tag{M18}
\]

同 cell 的原三角区域可以用完整矩形外包，但不能漏掉另一个实际方向；对 mean 可用 `g0_ik=0` 当 `i>k`，其余为原 `q_i` 上界，且 `t0_k=1`。

如果先用整个 source cell 上各块的 supremum `a^alpha beta_k`，则四块 kernel 为 `g^alpha_ik a^alpha beta_k`，两组 atoms为 `t^alpha_k a^alpha beta_k`。对完整两分量径向正比较作 row/column Schur，即得

\[
\|G_f\Delta A_LS^{-1}\|\le L_{\rm split}.
\tag{M19}
\]

两输出分量和两组 atoms 全部参加最大行、最大列及平方根；输入也包含两个完整分量。不能只报告 `NN` 块或只报告 mean-self 标量。

## 6. 保完整核权的 source交段RMS

下面不是一个乘法算子范数结论。一般而言 `||M_a||=||a||_infinity`，不能直接替换成 RMS。

对每个 body `I_k`，保留它与全部原4650闭 row 的精确交段 `J_kr`。各交段上有(M13),(M16)的完整统一费用 `a^alpha beta_kr`。定义

\[
m^{\alpha\beta}_k
=\Big(\sum_r |J_{kr}|(a^{\alpha\beta}_{kr})^2\Big)^{1/2}.
\tag{M20}
\]

**命题2。** 把(M18)的完整核权保留后，对任一输入分量 `f_beta` 有

\[
\begin{aligned}
\|\int_{I_k}G_\alpha(r,s)
 (\Delta A_LS^{-1})_{\alpha\beta}(s)f_\beta(s)\,ds\|
&\le\int_{I_k}g^\alpha_{ik}\,
 a^{\alpha\beta}(s)\|f_\beta(s)\|\,ds\\
&\le g^\alpha_{ik}\,m^{\alpha\beta}_k
 \|f_\beta\|_{L^2(I_k)},\qquad r\in I_i.
\end{aligned}
\tag{M21}
\]

**证明。** 第一行使用完整 `(r,s)` 产品盒核界而非某个点值。第二行是只在整个 source cell 上应用的加权 Cauchy–Schwarz；积分中的 `a^2` 由全部交段正和(M20)覆盖。对输出 `r` 再完整积分，body块多出 `|I_i|^(1/2)`；对 atom行用原 `t^alpha_k` 作同样处理。证毕。

因此完整算子由如下 `(2N+2) x (2N)` 非负有限矩阵支配：

\[
\begin{aligned}
M_{(\alpha,i),(\beta,k)}&=|I_i|^{1/2}
 g^\alpha_{ik}m^{\alpha\beta}_k,\\
M_{(\alpha,\rm atom),(\beta,k)}&=t^\alpha_k m^{\alpha\beta}_k.
\end{aligned}
\tag{M22}
\]

这里的两 atom行分别代表完整192维和1维观察 Hilbert块；不表示原观察只有两条。

等价地，可置 `b^alpha beta_k=m^alpha beta_k/|I_k|^(1/2)`，对 piecewise-constant的**抽象核比较**求以下连续 Schur 界：

\[
\begin{aligned}
R_{\alpha i}&=\sum_{\beta,k}|I_k|g^\alpha_{ik}b^{\alpha\beta}_k,\\
R_{\alpha,\rm atom}&=\sum_{\beta,k}|I_k|t^\alpha_k b^{\alpha\beta}_k,\\
C_{\beta k}&=\sum_\alpha b^{\alpha\beta}_k
 \Big(\sum_i|I_i|g^\alpha_{ik}+t^\alpha_k\Big),\\
L_{\rm split,RMS}&=\sqrt{\max R\;\max C}.
\end{aligned}
\tag{M23}
\]

该抽象核与(M22)在规范化分段常数基下同构。(M21)已证明它支配完整真实算子；不能反向把 `b` 宣称为真实乘子逐点范数。若保完整 source-cell核上界，(M20)不需要生成一个4650²核表，仍只保155²的核权。

body的长度为原精确有理数，(M20)可直接按精确交段比例求平方平均。真根 collar 仍使用其整个原统一费用，避免以未知真实长度的错误分母作归一化；最终 Schur 中各长度使用原完整向外上界即可。cutoff新增分界也必须与原行准确相交。所有行与独立 jumps仍保留，不能因交段压缩删除一个接口源。

作为单块特例，若只对旧完整193维费用执行同样的(M21)压缩，则新的source RMS不大于原parent最大值；它给同一旧 scalar核比较的另一完整界。此结论依赖(M21)的核组合，仍不是乘法算子的 RMS 估计。

## 7. 新算法边界、成本与成功记录复用

实现只需读取原完整行及新私有中心包。body的旧 local/drift/mean-own目标均原字消费；新生成的是(M13)和(M20)的完整组合，不调用旧系数 producer、不重算旧 norm。

可以按如下单向顺序实现。

1. 从已完整 admission 的同一153-parent/155-panel context读取原 `q`、同一实际 reference profiles、全部4650旧行和根 signed packet。
2. 逐原闭交段形成四块(M13)，累加(M20)；只需一个当前row的私有缓存。
3. 对同一155²完整核盒计算(M18)的 nonmean块；mean块用(M17)的显式完整公式。储存规模是标量155²，未分配193²逐盒矩阵。
4. 用(M23)完整计算并依次保存 row、column、norm三个**新配方**标量。任一步中断都不登记完整 `L_split,RMS`。
5. 若原 `L` 已成功保存，可原字消费其记录，与新的完整上界取小。两个界必须针对同一完整算子、同一根域、同一参数域及同一 WVC 接收器；不从一条旧上界减掉一个正费用。

核侧至多约 `96*N^2` 个模态比较，source侧为原row/panel交段的线性遍历；不引入原 graph4的大矩阵路径。这是结构成本说明，未许诺实际运行时长。

若新完整上界仍达到R139阈值，则它也可能排除相应新配方；若它更小，只是 family预算的一项更小。完整 cross、trial、dual/primal乘积、signed centre、有限rho和端点费用、无限高块逆、两RHS及七个独立port均仍须按原义支付。负侧、真实物理列、非线性与闭合可见几何义务均不由本文完成。
