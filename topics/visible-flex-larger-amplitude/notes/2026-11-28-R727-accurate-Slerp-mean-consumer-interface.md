# R727 准确 Slerp 均值后验、两角误差与完整分支接口

日期：2026-11-28。状态：完整源码与正式定理的数学接口论证；没有运行准确费用、科学求解、AST、fixture 或 benchmark。本说明不改变已经发布的 R726 工作源、run29 参数、接受规则或任何在跑任务。准确消费者源码由 geometry 独占实现；这里给出可直接实施的公式和责任边界，不重复实现该消费者。

## 1. 明确结论与实际来源

R727 可以为当前 R726 Slerp 均值提供局部准确正根和完整三维逆界。它不要求旧 R726 急角方案的 \(|K|>b\)，也不继承 R709 的欧氏闭球势或 R722 的归一化线段公式。两阶角导数误差可以在已证真根包围上直接评价完整导数方程残差，再乘 R727 的逆界；不必为了套用旧公式而引入候选点到真根的第三阶 chord 常数。

这个接口还有三项独立责任：完整中央幅度分支、投影径向框架的非零分母，以及相邻/字面/周期角域的同根接合。R727 的冠内唯一性本身不支付这三项。

本次实际全文读取并核对的来源如下，路径均相对本 topic。

| 完整文件 | 字节 | SHA256 | Git blob |
| --- | ---: | --- | --- |
| results/R727-symmetric-spherical-boundary-posterior-root-without-acute-cap.md | 20494 | cee8be0bc6084ed4091cdc68b368311c58715560ddc87086c514e52d7acf1d0f | dd61ad82ca2e982845214686f827035e3cee4dcd |
| results/R726-spherical-boundary-strong-monotonicity-and-positive-mean-root.md | 27362 | faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b | 1397c01f1155ebda224441039a3950ce03c2417a |
| scripts/resume_20261126/fixed_fejer_R726_spherical_seed_mean_jets.py | 48226 | 2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23 | 9f7ea1805326a317a281e8c3f6c7cb6ef9709890 |
| scripts/resume_20261126/fixed_fejer_R726_spherical_halfwave_meridian_reference.py | 52457 | 176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a | 231bad2fba5f80ade672703114fe5bd776512baf |

R726 当前整族登记在 computations/fixed-fejer-r726-current-complete-runtime-binding.json，55517 字节，SHA256 6e5480838f54ecb50ce8baa085ebabed37504a3ba759d1ed958ec28c6d9df059，Git blob 159d8c56b1b966cf5de5d19bceec68db3630144b。它有 137 个完整当前 source roles、23 个当前运行体，已由 7acb89983fe616fbba85cef74811625b357942e4 发表。本说明没有改变其中任一字节。

## 2. 必须包围的实际完整方程

令 \(E\) 为当前四个完整端层之并，物理总长度为 \(b\)，中央总长度为 \(L_c\)。准确参考切向为 \(u(s,\phi)\)，cutoff 为 R725 的准确三片 \(C_\epsilon\)，本族 \(\epsilon=1/8\)。定义
\[
 B(d,\phi)=\int_E S_{\chi(s)}(u(s,\phi),d)\,ds,\qquad
 F(v,\phi)=L_cv+B(N(v),\phi)-K(\phi).
 \tag{1}
\]
这里的 \(S_\chi\) 是准确最短球面弧，\(N(v)=v/|v|\)。保存的工作 v 只是 (1) 的候选；工作 Newton residual 不是准确积分残差上界。

实际 seed 的 _means 明确构造
\[
 K=(R-I_b)e_0+(H_0-I_c)e_z-\Gamma,\quad
 K_\phi=(R-I_b)e_1-\Gamma_\phi,\quad
 K_{\phi\phi}=(R-I_b)e_2-\Gamma_{\phi\phi}.
 \tag{2}
\]
\(I_b,I_c\) 是完整非中央、非端层补集的水平/竖直积分。\(H_0\) 是固定 seed 的 self.height；源码明确记录 fixed_original_core_H_used=True 和 current_outer_free_point_not_used=True。不能将当前 normal 点自由变量末字 \(H\) 代入 (2)。固定 seed 与当前自由场的关系由原完整 normal/raw-defect lift 处理。

_prepare_plan 从完整原 affine 节点集出发，加入支持端点、两中央的全部六片边界及每端层的两内部 cutoff 切点。它保留完整补集、原标量全尾、正长度和原 Gauss 规则；中央积分另用原完整十二辅助片。准确消费者应使用同一个完整准确分割和物理测度，并支付完整参考标量/求积误差；不能把工作有限节点表本身当作准确 cover。

当前 run29 计划的 \(b/S=1/2\) 给每端层准确长度 \(S/8\)，两中央各 \(3S/16\)，总 \(L_c=3S/8\)。这些是预定定义关系，未填写任何新的实际 S、工作长度字或数值根。R727 公式对原允许的其他正长度同样成立，应从实际完整 seed 定义读取，不把这一计划值写成通用消费者的唯一硬编码长度。

每完整端层都有准确反射 \(\tau\)，保持 ds 且满足 \(\chi(\tau s)=1-\chi(s)\)。因此 \(\int_E\chi\,ds=b/2\)。这来自三片完整多项式定义；无需假设参考方向 \(u(\tau s)=u(s)\)。切开的积分叶片可以分别求积，但应用 R727 配对下界时必须已覆盖整个四层，不能仅在一片上声称对称总质量。

## 3. 可直接实现的准确零角系数核

令
\[
 q=1-u\cdot d=\tfrac12|u-d|^2,\qquad
 f_a(q)=\frac{\sin(a\theta)}{\sin\theta},\quad
 \theta=\arccos(1-q),\quad 0\le a\le1,\ 0\le q<2.
\]
在零角使用同一解析延拓。其全级数为
\[
 f_a(q)=\sum_{n=0}^{\infty}c_n(a)q^n,\quad c_0=a,\quad
 c_{n+1}=\frac{(n+1)^2-a^2}{(n+1)(2n+3)}c_n.
 \tag{3}
\]
准确区间核可以对 (3) 做向外舍入并附完整尾，或使用同一准确函数的有证三角包围。不能直接调用工作 degree32 后将其返回值标为准确 Slerp。

### 3.1 完整尾与 a 导数

由 \(0\le a\le1\)，递推比非负且不超过 \((n+1)/(2n+3)<1/2\)，故
\[
 0\le c_n(a)\le2^{-n}.
\]
写 \(g_n=\partial_a c_n\)，则
\[
 g_0=1,\qquad
 g_{n+1}=\frac{(n+1)^2-a^2}{(n+1)(2n+3)}g_n
 -\frac{2a}{(n+1)(2n+3)}c_n.
 \tag{4}
\]
令 \(h_n=2^n|g_n|\)。由 (4)，
\[
 h_{n+1}\le h_n+\frac4{(n+1)(2n+3)}
 \le h_n+\frac4{(n+1)(n+2)}.
\]
后一个和望远镜相消，因此 \(h_n<5\)，即 \(|g_n|<5\,2^{-n}\)。这是对同一系数递推的导数，不是另一张舍入导数表。

截断至 n=m-1，取 m>=3、\(\rho=q_{\max}/2<1\)，则整个区间的准确绝对尾界可取
\[
\begin{aligned}
 E_0&=\frac{\rho^m}{1-\rho},\\
 E_q&=\frac12\,\rho^{m-1}
        \frac{m-(m-1)\rho}{(1-\rho)^2},\\
 E_{qq}&=\frac14\,\rho^{m-2}
 \left\{\frac{m(m-1)}{1-\rho}
       +\frac{2m\rho}{(1-\rho)^2}
       +\frac{2\rho^2}{(1-\rho)^3}\right\},\\
 E_a&=\frac{5\rho^m}{1-\rho}.
\end{aligned}
 \tag{5}
\]
(5)分别来自对几何尾的一、二次 q 导数及 (4)。在 q=0 按连续极限解释，不执行负幂或 0/0。m=33、qmax=1/4 时恢复已刊统一 2^-98、2^-91、2^-84、2^-96 界；一般 q 不能把 Eq 的 \(1/2\,\rho^{m-1}\) 误写为 \(4\rho^m\)，也不能将 Eqq 的 \(1/4\,\rho^{m-2}\) 一律写为 \(16\rho^m\)。

这些界只支付无限级数的截断。系数和 Horner 的有理/区间舍入、参考端向量、根包围、整个积分及工作图比较仍由各自记录支付。接近反极时 rho 接近1，尾可能很宽或需更多项；没有实际运行数据，不能声称这种准确评价很快。

准确 q 已知非负且受已证角域约束。将粗区间与这些证明给出的约束相交是合法的集合收紧；无证明地把工作 dot/q clip 到 [-1,1] 或 [0,2) 则不是。

### 3.2 与实际完整微分图的关系

2513 完整体的 _spherical_state 对输入 T0 和原三维 v 都归一化，再形成
\[
 R=f_{1-\chi}(q)u+f_\chi(q)d,\qquad T=N(R).
\]
准确 Slerp 时 \(|R|=1\)，输出归一化为恒等；工作多项式/三角与舍入时并非可以删除。准确包围可以保留同一完整归一化延拓，并用准确单位关系收紧。_spherical_y_jacobian、_spherical_angle_jets、_spherical_radial_jet 已明确保两输入及输出的完整导数，不能在新准确实现中只保系数导数而删归一化项。

固定 cutoff 对 phi 无导数，故 mean 两角只需 \(f,f_q,f_{qq}\)。真实 s 导数还需 \(f_a\) 的 a 导数及原参考 Ts：
\[
 A_s=A_q q_s-A_a\chi_s,\quad
 B_s=B_q q_s+B_a\chi_s,\quad
 R_s=A u_s+A_su+B_sd.
 \tag{6}
\]
若将来允许 chi、长度或测度依赖 phi，必须重新加入它们的一、二阶项；不能沿用当前固定参数特殊式。

## 4. 将保存的真实候选变成 R727 的完整后验输入

从实际完整 mean NPZ 按其字节读取 \(\hat v\ne0\)，把 binary64 词解释为准确二进有理向量，定义
\[
 d_0=N(\hat v),\qquad \alpha_0=L_c|\hat v|.
 \tag{7}
\]
归一化、平方根和准确 Lc 均向外包围。这样 \((\alpha_0/L_c)d_0=\hat v\) 在准确数学中成立；不能另拿工作 central_length_hex 替准确 Lc，造成未记账的长度误差。保存的 d 向量不被直接假定准确单位长。

选记录在本次证书中的 \(\eta\in(0,\pi/2)\)。对每个完整径向×角胞给
\[
 \operatorname{angle}(u(s,\phi),d_0)\le\beta,\qquad
 \theta_*=\beta+\eta<\pi.
\]
也可以通过已证 \(\beta\) 的余弦点积不等式检验此界，而不在零角附近盲用浮点 acos。任何方法都必须包住完整 s/phi 胞和当前准确参考，不能只读 sampled_acute_pairs。

用准确 (1) 积分得到
\[
 R_0=\alpha_0d_0+B(d_0)-K,\quad |R_0|\le e,\quad
 |(I-d_0d_0^T)R_0|\le e_T.
\]
安全取 \(e_T=e\) 可用；若支付更紧切向向量盒，可用该更小界。定义正式 R727 的
\[
 m=\tfrac b2\cos(\theta_*/2),\quad
 L=\tfrac b2\,\theta_*/\sin\theta_*,\quad
 a_-=\alpha_0\cos\eta-L\eta-e,\quad
 a_+=\alpha_0+L\eta+e,\quad \kappa=m+a_-.
 \tag{8}
\]
只有
\[
 a_->0,\quad a_+<L_c,\quad e_T<\kappa\eta
 \tag{9}
\]
全部按向外包围后的严格方向成立，才得到该冠内准确正根。角域可非急角；这里使用沿球面弧的 \(L\eta\)，没有把它换成未证弦长 Lipschitz 项。

计算上用 m、a-、kappa 的下界及 L、a+、e、eT 的上界。最终比较须用 Lc 的下界等足以蕴含 (9) 的方向。不能拿区间中点过门。候选 norm 位于 (0,1) 的证成与 (9) 也应保留同一全词来源。

令
\[
 \bar r=e_T/\kappa<\eta,\qquad
 M=\frac1{L_c}\sqrt{(1+L/\kappa)^2+(a_+/\kappa)^2}.
 \tag{10}
\]
R727 保证真根方向位于中心半径 barr 的小冠，\(\alpha\in[a_-,a_+]\)，且真根处完整 \(J_v=D_vF\) 的逆范数不超过 M。原 v 的候选误差可用
\[
 E_v=\frac{e+L\bar r+\alpha_0(1-\cos\bar r)
                    +2\alpha_0\sin(\bar r/2)}{L_c}.
 \tag{11}
\]
这里最后一项确为两个已知单位向量的弦长，合法；它不改变 (8) 必须用弧长的事实。若 eT=0，则 barr=0，按原式得到有效包围，不人为引入除以 barr 的式子。

M 是对已证真根的逆界，并非整个 Cartesian 包围盒内任意向量都满足该界。后续区间评价需要一个含真根的集合；可以同时保 (11)、准确 norm 壳 \([a_-/L_c,a_+/L_c]\) 和方向小冠。粗轴盒若包含零或反极，不应因此删除真问题条件，也不能把盒外点假装成真根；可用已证约束收紧或细分准确包围。

## 5. 两阶角误差：直接消费完整残差，无第三阶 chord 常数

本节固定当前参数和准确 Lc，令 \(v_*(\phi)\) 为已经接合到指定冠的真根，\(J_*=F_v(v_*,\phi)\)。工作保存的 \(\hat v_1,\hat v_2\) 分别是 v_phi、v_phiphi 的准确二进有理候选。它们不必被假定为“跨角胞插值候选中心”的导数；以下是对真实隐式根导数的逐点误差式。

### 5.1 第一阶

定义完整已知残差
\[
 E_1=J_*\hat v_1+F_\phi(v_*,\phi).
 \tag{12}
\]
真实 \(J_*v_{*\phi}+F_\phi=0\)，相减得
\[
 \hat v_1-v_{*\phi}=J_*^{-1}E_1,\qquad
 |\hat v_1-v_{*\phi}|\le M\,|E_1|.
 \tag{13}
\]
因此在整个含根集合 V 中包围 (12)，得到 e1 后，用以 \(\hat v_1\) 为中心半径 M e1 的盒 W1 包住真实一阶。J* 和 Fphi 均以准确 Slerp/参考/完整积分评价；不能只把保存的工作 mean_jacobian 和工作 residual 直接塞入 (12)。

等价的实现是把完整边界两角接口的原 v 参数换成 V，T0/T1 取完整准确盒，v_phi 用 saved_v_phi，v_phiphi=0；其第一阶积分加 Lc*saved_v_phi-Kphi 正是 (12)。这一方式自然保所有输入归一化与参考角项。

### 5.2 第二阶

真实隐式方程是
\[
 J_*v_{*\phi\phi}
 +F_{\phi\phi}
 +2F_{v\phi}[v_{*\phi}]
 +F_{vv}[v_{*\phi},v_{*\phi}]=0.
\]
取
\[
 E_2=J_*\hat v_2+F_{\phi\phi}
       +2F_{v\phi}[v_{*\phi}]
       +F_{vv}[v_{*\phi},v_{*\phi}],
 \tag{14}
\]
其中真 vphi 在已经付清的 W1 中，而不是仍裸用 saved_v_phi。于是
\[
 |\hat v_2-v_{*\phi\phi}|\le M\,|E_2|.
 \tag{15}
\]
可以对完整边界两角链直接输入 (V,W1,saved_v_phiphi)，加 Lc*saved_v_phiphi-Kphiphi；因为二阶全导数关于 vphiphi 线性，所得恰为 (14)。所有归一化加速度、qphi²、qphiphi、参考/均值 mixed 项和系数二阶导都保留。

这条路径不需要先证明 J 或 Fphi 在候选到根之间的额外 Lipschitz 常数，也不需要引用旧 chord 三阶界。但它并不免去 (12)/(14) 全积分、算术和区间宽度费用。M 仍只在真根使用；V/W1 中其他组合用于保守包围右端，不被宣布是方程的解。

当前 seed 的 phi-固定 Lc/cutoff/测度与该特殊式相符。若这些量依 phi 变化，Fphi/Fphiphi 必须包含 Lc'v、Lc''v、2Lc'vphi 及真实测度/cutoff 导数；不能让接口静默删除它们。

## 6. 完整 seed 还需幅度与框架，均值冠不替代这些费用

原工作 _solve 在均值后继续完整中央幅度 bracket、原十二片矩、64 次允许二分和 profile 两角方程，随后构造
\[
 q_0=e_0-(e_0\cdot d)d,\qquad w=N(q_0).
\]
准确消费者同样需要以下两项：

1. 用当前真 r=|v*| 的整个包围和准确完整 \(A_\delta\) 支证明所用幅度根。保存的有限 working bracket 成功不自动等于准确 bracket 证书。可消费已经证明的 R711/R724 真支，但其输入必须是本次真实 r、delta、完整十二片和误差包围；不能搬旧机制 lambda。
2. 另付 \(|q_0|>0\)。R727 非急角定理没有推出 d_z>0；旧 R722 依靠正 zeta 的充分分母界不能无条件继承。对准确单位 e0,d，可以用 \(1-(e_0\cdot d)^2\) 的严格正下界，或另一独立已证下界。然后再对 q0 的完整一二角式作 N 的两阶微分。

对应原量可直接由 V/W1/W2 算出
\[
 d=N(v),\quad d_\phi=DN(v)v_\phi,\quad
 d_{\phi\phi}=DN(v)v_{\phi\phi}+D^2N(v)[v_\phi,v_\phi].
\]
r、lambda、w 的完整两角链继续原定义，不把原工作单位缺陷或 sampled minimum 当作准确正界。若幅度/框架费用未支付，仍可保已获得的 mean root 证书并将下游明确记 partial；不能把它升级为完整 sixjet。

原 paired halfwave 的 transverse mean 只在两个等长中央区间一起精确相消，单个中央段一般不为零。保全部中央片、bubble、原 raw-defect lift 及三分量闭合残差，不凭全均值消掉某一前缀位移或工作缺陷。

## 7. 逐胞、字面角、周期与对称的同分支接合

每个完整角胞的 R727 冠先只证明该冠内唯一，不证明球面全局唯一。对相邻胞 i,j 的共同参数点，必须先核完整准确 B/K/Lc/cutoff/源/参考模型同一。若已证
\[
 \operatorname{dist}_{S^2}(d_{0,i},d_{0,j})+\bar r_i<\eta_j,
 \tag{16}
\]
则 i 的真根位于 j 的唯一性冠，两根相同。也可用 i 的真根方向盒与 d0,j 的准确点积下界严格大于 cos(eta_j)，实现同一个包含证明。仅“两小冠相交”或“两胞各自 exists=True”都不够。

字面角的保存候选、全胞分支与两端 0/2pi 也需同样接合。周期整数据相等以后，必须把一侧已证根包含到另一侧冠或采用同一已证冠。对反射/半转 Q，先完整核准确数据协变，再将一侧根的 Q 像包含入另一侧唯一性冠；phi 反射的一阶符号和二阶符号须分别正确。不从 sampled_acute 或工作 Newton 初值猜同支。

若每胞用固定的保存候选中心，胞内该中心连续，严格 R727 余量与隐函数定理给 C2 根；跨胞中心不必相同，(16)使局部根在共同处同一，配合同一可逆方程接合其导数。任何实际选择不同候选/盒时，都保候选全词与该胞证书自己的来源，不拿最新候选覆盖历史胞。

这是准确 reference mean 的分支接合。全部 normal 的32阶段根盒、stage 控制、邻接 frame、当前 point 与 packet 的完整同支合同仍独立保持。mean Jv 的 M 不被称为 normal Cu 或全场 Jacobian 逆界。

## 8. 最小下游实施顺序与结果语义

不需要改 R726 当前工作源或给 run29 增加前门。准确后继可按以下完整依赖实施：

- 独立准确 Slerp 系数/jet 核，明确式(3)–(6)与全部 tail/舍入责任；验证实际2513/1764完整来源和保存 raw v 的真实数组记录。
- 在完整 radial/phi cover 上算 (1) 的 R0、非反极域与 R727 条件；记录 e/eT、alpha0/d0、eta/thetastar、m/L/a-/a+/kappa、真根集合与 M，未满足时保失败/不足原因，不冒无根。
- 用式(12)–(15)的完整积分生成 v 的两角误差，再接原完整 amplitude/frame/central/lift/sixjet；全部准确分割、tail 和32阶段责任保留。
- 用式(16)及完整源同一性接合每个相邻/字面/周期分支，之后才能将逐胞结果交给整圆几何、闭面、相位和矩消费者。

上述输出字段是所需数学信息的合同，不宣称当前某个新准确文件已使用这些精确字段名。geometry 拥有实际准确实现与最终 schema；以后以它完整锁定的文件/接口为准。本说明不给旧 chord/R722 schema 换名，也不把工作 sampled boolean 变成准确 existence。

如实际只有局部证书，则保其 own interval、own candidate、own source/model/target、完整分割及真实 partial 状态。全角 mean/jet 支付完成也不等于全场连续 Gram/reach、闭面 cap/phase、R716 十二矩、未标记 deltaE 或真实空间/频率/时间精化已完成。

本说明只有完整源码阅读、符号推导和精确文本记录，没有新实际场数值，没有生成未来报告身份。所读 run29 参数中的实际 run/model/point/packet/accepted/final/费用结果仍为 null；root 负责真实执行和发表，原科学预算与返回顺序未改变。
