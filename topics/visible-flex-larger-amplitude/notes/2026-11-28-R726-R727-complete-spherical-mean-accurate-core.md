# R726/R727：真实 Slerp 全角均值、后验局部根和完整两角费用核心

2026-11-28。此处交付完整独立准确核心，不修改正在运行的科学源，不把准备或可变进度当成完整场。当前科学来源是已刊 R726 家族：完整 137 个科学角色、23 个当前运行体，完整来源表为 `computations/fixed-fejer-r726-current-complete-runtime-binding.json`，55,517 B，SHA-256 `6e5480838f54ecb50ce8baa085ebabed37504a3ba759d1ed958ec28c6d9df059`，Git blob `159d8c56b1b966cf5de5d19bceec68db3630144b`；完整科学交付表 24,238 B / `f3e2e6b31fa9b59af013c4a8fc048e55858eb32279638a4f11368cf2dd2917f9` / blob `5200b7728c55e192821f0f4f29578bc5d22f4524`。科学原包已在 `7acb89983fe616fbba85cef74811625b357942e4` 保存。

本准确分支绑定真实 mean 2513、seed 1764、base bb045、normal 335e、packet 9da、driver 58630、reader 1aae。另一候选 source 或相同公式不能自动进入此分支。没有填入任何 run29 完整 report、immutable snapshot、point、accurate root 或费用结果。完整现有 batch/packet 符合输入合同后才可评价。

## 1. 完整来源和职责

| 完整文件 | bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `fixed_fejer_r726_normal_packet_accurate_field_input.py` | 52462 | `4082fb95d3e90b90701c893236b7a958d16cd883e3af280f65714245c58c2fd5` | `2c4ea794fd4bd2abfedbdb206f46d3ed0b8c64d7` |
| `fixed_fejer_R726_exact_spherical_boundary_boxes.py` | 15754 | `c7ba94caa8a527981a6a41caf53af7f3e34e50946b90cf8247dc029710d29409` | `bf22d7862c79b9598ca92c1be103d1a260158741` |
| `fixed_fejer_R727_posterior_spherical_mean_cap.py` | 16340 | `c110ecba9019818cc5922ba12611868e0f2ebc1ada4b7c57f26b607b19c18e1d` | `3a88dc2b2d0e037060f52e046759dc0fd1d5bb0a` |
| `fixed_fejer_r726_R727_posterior_mean_jets.py` | 80321 | `bd252a0778e25ad04133c88a5b43d927bf17a4c5e2a5b09022b32198bfc63595` | `04117790bdb6e14376e409a5fbeca55c7fb5e943` |
| `fixed_fejer_r726_R727_accurate_reference_control_radial_boxes.py` | 62323 | `67c1e38b2b0251dbafb5cb832f3400ade2b3c3baf5ab0decf6ff8ca003fb4e00` | `76199393271708ed3d6a0a2653afff93ebc6eb36` |
| `reproduce_fixed_fejer_r726_exact_spherical_foundations.mjs` | 47169 | `46252e1b0b3140ffe96f362866ab674226af1704e2ce17b51a11340d48c3e78a` | `70e2908046215a696b78f4896942d2e267218f9c` |
| `reproduce_fixed_fejer_r726_R727_complete_mean_radial_sources.mjs` | 82789 | `a9b10dcb6cf397d0fd75ae2b14ecaa7caafe592daaf80ef95f441c19219e1aed` | `9f8774384b64b4ea13a35edd114381597634e4eb` |

五个运行体的真实职责分别为：完整实际输入、准确 Slerp 解析函数、R727 局部后验冠、实际均值/两角费用与来源归因、完整径向参考/六控制/物理六 jet。每体独立小于 100,000 B。两个 MJS 只读取固定完整父文件并生成完整新文本，绝不 import 科学模块或执行准确算术。

三个完整父体仍保留：R725 input 46,944 B / `6f279ee6eb65a946e1980a44020dfb3f11e42e6eb7bc99e4e9d336c19994e9d4` / blob `82e337ae877428e2cd05fc6603f48bef6f989b0a`；R725/R722 posterior 70,729 B / `e290512f974d96a02764722660c818519a926a9a7cfac1c0abd9639d9e2cdbd0` / blob `5d56464731e8a4684070189e97648d5989ba2371`；R725 radial 54,251 B / `4158a7f0ef6e76ff3f28cb52063045df34e8a960daf6370fd844db89c229ed88` / blob `73c554768d79dee24701f14133c45d55154842a6`。

完整共享算术为 72,182 B / 0471c626… 的 `fixed_fejer_reference_seed_angular_profile_error_bounds.py` 和 41,476 B / ae67ecac… 的 `fixed_fejer_reference_accurate_mean_residuals.py`。其旧 literal CLI、旧 provider guard 和旧 R709 存在性入口不改。新 WholeMean 只显式复用其完整准确 scalar/context、全 cut 计划、二叉细化、完整区间求和、K 和 residual 公式；端层函数和根域另由本文完整新源实现。

## 2. 真正准确的 Slerp，而非工作多项式

对两个准确单位向量 \(u,d\)，设
\[
q=1-u\cdot d=\tfrac12|u-d|^2,\qquad 0\le q<2,
\]
并令
\[
f_a(q)=\frac{\sin(a\arccos(1-q))}{\sin(\arccos(1-q))},\qquad
S_\chi(u,d)=f_{1-\chi}(q)u+f_\chi(q)d.
\]
在 \(q=0\) 采用解析延拓 \(f_a(0)=a\)。准确输出已经单位，不再把工作 degree32 图中的最后归一化当成准确函数的额外分母。

### 2.1 完整级数的身份

\(f_a\) 满足
\[
q(2-q)f''+3(1-q)f'+(a^2-1)f=0,\qquad f(0)=a.
\]
将 \(f=\sum c_nq^n\) 代入逐幂比较，得到
\[
c_0=a,\qquad
c_{n+1}=\frac{(n+1)^2-a^2}{(n+1)(2n+3)}c_n.
\]
当 \(0\le a\le1\)，有 \(0\le c_n\le2^{-n}\)。所以在任意 \(q\in[0,Q]\)、\(Q<2\) 上级数及两阶 q 导数绝对一致收敛，满足上述微分方程和零角解析初值，故等于准确 Slerp 系数。该结论不以工作小角切换点或 degree32 误差设零。

令 \(g_n=\partial_a c_n\)。完整递推是
\[
g_0=1,\qquad
g_{n+1}=r_ng_n-\frac{2a}{(n+1)(2n+3)}c_n .
\]
若 \(h_n=2^n\sup_{0\le a\le1}|g_n|\)，则
\[
h_{n+1}\le h_n+\frac4{(n+1)(2n+3)}
\le h_n+\frac4{(n+1)(n+2)}.
\]
望远镜求和给 \(h_n\le5\)，即 \(|g_n|\le5\,2^{-n}\)。因此 a 导数也可逐项求导。

### 2.2 全尾和方向

令 \(t=Q/2<1\)，有限项取到 \(N\ge2\)。完整尾界为
\[
R_0=\frac{t^{N+1}}{1-t},
\]
\[
R_1=\frac12\left[
\frac{(N+1)t^N}{1-t}+\frac{t^{N+1}}{(1-t)^2}\right],
\]
\[
R_2=\frac14\left[
\frac{N(N+1)t^{N-1}}{1-t}
+\frac{2(N+1)t^N}{(1-t)^2}
+\frac{2t^{N+1}}{(1-t)^3}\right],
\qquad R_a=5R_0.
\]
前三尾非负，a 导尾有符号；实现分别加入 \([0,R_j]\) 和 \([-R_a,R_a]\)，所有有限递推、Horner 和尾端点均向外。\(Q=0\) 直接使用这些非负整数幂的连续值。一般 \(1/2,1/4\) 前因子完整保留，不沿用特定 \(Q=1/4\) 的缩写。

默认 64 项是准确包围算法，不是把解析场换成有限多项式。全部余尾仍保。盒宽或已声明预算不足时只能未付，不能称根不存在。预算检查沿外层同一个 WorkBudget，不新增一项科学准入测试。

### 2.3 全角、径向和 raw-v 微分

完整代码先对两组 raw 输入分别取准确归一化和一二角 jets。设 \(e=u-d\)，则
\[
q_\phi=e\cdot e_\phi,\qquad
q_{\phi\phi}=|e_\phi|^2+e\cdot e_{\phi\phi}.
\]
令 \(A=f_{1-\chi}\)、\(B=f_\chi\)、\(C=A_q u+B_qd\)。代码完整保留
\[
S_\phi=Au_\phi+Bd_\phi+q_\phi C,
\]
\[
S_{\phi\phi}=Au_{\phi\phi}+Bd_{\phi\phi}
+2q_\phi(A_qu_\phi+B_qd_\phi)
+q_{\phi\phi}C+q_\phi^2(A_{qq}u+B_{qq}d).
\]
端层 \(\chi\) 不依材料角。径向微分独立保留原参考转向和 cutoff 转向：
\[
q_s=(u-d)\cdot u_s,\quad
A_s=A_qq_s-A_a\chi_s,\quad
B_s=B_qq_s+B_a\chi_s,\quad
S_s=Au_s+A_su+B_sd .
\]
raw-v 三列矩阵是
\[
D_vS_\chi=
\big[B I-C(u-d)^T\big]\frac{I-dd^T}{|v|}.
\]
每个分量、交叉项和真实归一化半径都在完整区间图中。材料二阶位置只需要 \(T_s\)，而混合位置导数使用 \(T_\phi\)；没有为了六 jet 遗漏所需角项。

## 3. 完整实际输入和三次全径向积分

输入类继续逐字读取完整 scientific report、pure readout、完整 immutable point 和 required-angle root packet。保全部 137 科学源、完整当前 M160/N2048/J923、所有 core/omega/H、原 32 阶段、所有缓存角、实际完整 mean batches 和每个 9-vector/6-scalar 候选字。source、model、point、snapshot、target、固定参考和六文件均交叉绑定。原数组读取前后以及最终所有使用字节均重核。

额外读取真实1764/2513的完整 spherical working definition：degree32/切换及其未付误差也是工作模型身份；它不作为准确 Slerp 核。旧 R709/R722 存在性继承必须明确 false。当前自由 H 不进入 seed 的 K。准确 K 始终是
\[
K=(R-\int_{\mathrm{outside}}b)\,e_r(\Theta_0)
 +(H_0-\int_{\mathrm{outside}}c)e_z-\Gamma .
\]
全部 outside 和无限 scalar tail 均保，\(H_0\) 是真实 seed 初始高度。

第一遍在固定实际 \(\widehat v,\widehat v_\phi,\widehat v_{\phi\phi}\) 上积分完整 Slerp 图，得到全部三个组合 residual。R727 存在性只使用它的准确零阶残差和全端层 \(u\cdot N(\widehat v)\) 下界。候选 normalization 由三个原 binary64 字准确重算，不使用仅工作近单位的 saved d。

根域证明后，第二遍在真实 \(v_*\) 的已证盒中、以 saved \(\widehat v_\phi\) 为形式一阶输入，积分全一阶方程残差 \(E_1\)。第三遍以真实 \(v_\phi\) 的完整已证盒为一阶输入、saved \(\widehat v_{\phi\phi}\) 为形式二阶输入，积分全二阶残差 \(E_2\)。

三遍保同一完整活动径向 partition 和同一原补集/K；第二、三遍复用补集完整原叶，其余每片完整再包围，不采样替代。candidate 分片和原 maximum_splits 共用同一个计数；三个积分遍历和所有解析运算都使用原外层时间/leaf预算。没有增大预算或删掉尚未支付的片。初次非反极范围若未分离，仅按完整二叉切分细化或返回未付。

两中央区间只以合并的准确 \(L_cv\) 计入总均值；各自横向均值绝不置零。全部六加六物理中央 cuts、R725 四端层的八个内部 cuts、全部原 scalar cuts 和精确 affine 端点都保。外层 working whole-cell Gauss 的准确性不因此获得任何默认证书。

## 4. R727 局部根冠和真实两角误差

[完整 R727](../results/R727-symmetric-spherical-boundary-posterior-root-without-acute-cap.md) 的实际 proof record 为 20,494 B / `cee8be0bc6084ed4091cdc68b368311c58715560ddc87086c514e52d7acf1d0f` / blob `dd61ad82ca2e982845214686f827035e3cee4dcd`。新 cap 模块逐项向外计算 \(m,L,a_-,a_+,\kappa,\rho\)，采用 \(L\eta\) 球面弧长，绝不使用先前未证明的弦长版本。

所有角度和长度条件都在完整角胞、完整端层上支付。候选方向 \(d_0=N(\widehat v)\)，\(\alpha_0=L_c|\widehat v|\)；准确完整 residual 的切向部分也有独立区间。模块只有在严格
\[
0<\eta<\pi/2,\quad\beta+\eta<\pi,\quad
a_->0,\quad a_+<L_c,\quad\varepsilon_T<\kappa\eta
\]
时返回局部唯一根。根半径、方向误差、alpha误差、v盒和
\[
M\ge\|J_v(v_*)^{-1}\|
\]
都来自同一完整证明。M 只宣称在已证真实根有效，不宣称包含该根的每个 Cartesian 盒点都有相同逆界。

令 \(\mathcal V\) 含真实根，第二遍计算
\[
E_1=J_v(v_*)\widehat v_\phi+F_\phi(v_*).
\]
直接得 \(|v_\phi-\widehat v_\phi|\le M|E_1|\)。得到完整 \(\mathcal W_1\) 后，第三遍计算
\[
E_2=J_v(v_*)\widehat v_{\phi\phi}+F_{\phi\phi}(v_*)
 +2F_{v\phi}(v_*)[v_\phi]+F_{vv}(v_*)[v_\phi,v_\phi],
\quad v_\phi\in\mathcal W_1,
\]
故 \(|v_{\phi\phi}-\widehat v_{\phi\phi}|\le M|E_2|\)。实现把这些完整项通过 Slerp 的第二总导数一起计算，没有丢 mixed 项，也不引入旧 chord 的三阶运动常数。

对盒与已证 \(|v_*|\in[r_-,r_+]\)、\(q\le1-\cos(\beta+\eta)<2\) 的相交，只表示同一个真实根/参考点满足这些数学约束；不是把盒中所有点都宣称为根。完整 attribution 记录每遍输入 jets、每片解析图、全叶覆盖、每个和、cap、全部输出边界及真实输入来源。纯消费者重新读取原 candidate batch 并重算这些完整条件。

## 5. 独立的投影架与完整 profile

R727 不给 \(d_z>0\)。代码单独包围准确 \(e\cdot d\)，并仅在
\[
1-\sup|e\cdot d|^2>0
\]
时支付 \(w=N(e-(e\cdot d)d)\) 的完整分母及一二角 jets；否则该准确分支未付。没有把 old zeta 留作一个默认正数。

[R711](../results/R711-smooth-triangle-central-profile-and-geometric-comparison.md) 完整17893B/7df73fc1…及 [R713](../results/R713-exact-smooth-triangle-moments-and-actual-fees.md) 完整10284B/ed9c96e7…由原完整 source records 核。准确反射给 \(A_\delta(0)=1,A_\delta(\pi)=0\)，所以已证 \(0<r<1\) 时存在唯一 \(\lambda\in(0,\pi)\)。这是准确完整十二片恒等式，不把实际工作π端moment设零。

完整 R711(11)/R713(10) 地板、全部十二片精确有理矩、Taylor全尾、actual工作三moments误差以及 lambda 两角费用保留。没有沿旧 chord 正z或旧(0,π/2)范围推导。profile准确存在来自本次真实根半径，working candidate 仍需实际位于(0,π)且费用完整。

## 6. 局部冠接合是尚待下游接入的真实责任

每个完整角胞的 R727 唯一冠只证明一个局部根，不能直接置原 `full_R722_unique_reference_mean_and_projected_frame_are_two_pi_periodic` 为 true。新 cap 模块给一个明确单向充分式：若源根在以 \(d_s\) 为中心、半径 \(\rho_s\) 的已证小冠，目标在以 \(d_t\) 为中心、半径 \(\eta_t\) 的完整唯一冠，且
\[
\eta_t-\rho_s>0,\qquad
d_s\cdot d_t>\cos(\eta_t-\rho_s),
\]
则源真根严格落入目标唯一冠。结合共同端点的同一完整方程，才能认定两真根相同。

`directed_cap_containment` 完整向外计算该式并保存源/目标整个domain摘要。它不替调用者证明相同 equation、source、point、seed、全径向覆盖、共同角/周期数据。必须由新的 normal/leaf 消费路径逐相邻闭角胞及周期端点调用；仅独立两个通过的局部冠不够。R716 半转还需要真实变换后的同源方向包含，不能凭偶 Fourier modes 自动迁移。

本核心交付尚未将旧 R725/R722 normal、leaf、G、R723、P/U 或 mesh 改名为 R727。它们的旧存在性/全周期断言不接受当前新schema。后续明确新入口必须加入本段的完整根支接合和所有源记录，然后保留全部32 normal阶段及原六jet/Gram/曲率/帽/全相位责任。准备核心没有提前支付任何这些结果。

## 7. 为什么不能只算一个母角再旋转

已全文读实际1764的 `_chart` / `_means` 和完整 ae67.chart。参考确有
\[
u(s,\phi)=Q(\Theta_0(\phi))u(s,0),
\]
且 cutoff、测度、固定 H 不依角。但是完整 K 含真实非圆核心
\[
\Gamma=h\,n_\phi+h'\,t_\phi,\qquad
\Gamma_\phi=\rho\,t_\phi,\qquad\Theta_0'=\rho .
\]
若 \(\Gamma=Q(\Theta_0)\Gamma_0\)，则必
\[
\Gamma_\phi=\rho J\Gamma=\rho(h\,t_\phi-h'n_\phi).
\]
当准确 \(\rho>0\) 时，比较两个独立方向强制 \(h\equiv1,h'\equiv0\)。当前固定 Fejér 配方有非零 Fourier 首模，故不成立。因此 K 不是同一旋转轨道，不能从一个准确母角宣布全部角的均值根/角jets。代码保全原1024闭角胞接口及所有实际saved words。这是已读完整实际公式的因果，不是对未来数值的猜测。

## 8. 具体读取接口与执行边界

- `ActualNormalPacketPoint` 是上述新完整input；complete source/model/point读取合同沿父全体，另外核实际 spherical graph。
- `ExactSphericalBoundary.boundary` 接完整 raw reference/mean 三jets、chi、两完整norm约束，可选真实q上界；径向必须同时提供原 T0_s 与 chi_s。
- `posterior_root_domain` 接准确 Lc/b、实际三个v字、完整零残差与全端层参考/候选dot下界；返回完整局部冠及其所有严格余量。
- `PosteriorMeanKernel.candidate_domain` 先核真实input、完整候选、全径向binary cover和全部总和，再调cap。
- `true_root_first_residual_jets`、`first_residual_bounds` 给两次新残差积分的完整输入盒；不是新working求解。
- `validate_root_domain_attribution` 在原参数之外明确新增 `jet_residual_evidence`，必须传first/second两遍完整总方程和所有活动叶。会核全部9个完整源/定理record、重读实际batch、重算局部cap/全E1E2/profile/frame边界。
- radial evidence 的 `complete_posterior_mean_root_domain` 是新R727 attribution，`complete_jet_residual_evidence` 保存额外两遍；`old_R709_or_R722_existence_inherited=False`，`adjacent_or_periodic_reference_mean_branch_certified=False`。调用者不能将最后一项自动翻true。

两个完整再生器分别接 `--source-directory` 与 `--generated-directory`。第一份生成input、解析Slerp及cap三体；第二份从固定完整R725父生成完整mean/radial。精确文本span以固定父whole SHA和被移除完整span SHA绑定；新文本完整内嵌，反向重建完整父。它们不构成科学入口的前置gate，也没有在本地执行。

本次实际只做 V8 源文本构造、完整文本身份与 remote blob保护。没有执行 AST、compile、科学模块、Fraction评价、均值/normal根、F/J、数值fixture或额外Actions科学重跑。run29官方已启动的事实与其尚未返回的完整科学输入/费用分开，所有本交付未来结果保持null。
