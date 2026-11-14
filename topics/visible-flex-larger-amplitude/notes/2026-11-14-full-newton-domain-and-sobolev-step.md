# 完整 Newton 步的 Frenet 定义域与 Sobolev 方向约束

日期：2026-11-14。

## 结论与下一最小选择

真实节点上，完整试探步的 Frenet 域分子是步长的至多八次多项式；材料密度 rho 沿步长为一次函数。因此可以在调用昂贵的无效试探之前估计一个有依据的初始步长。这个估计必须再经过原 collocation 的真实非线性中点、原边界函数和原 merit 检验。

单纯把允许回溯次数加大不能解决一个几乎只容许极小步长的方向。若 bridge 新网格仍失败，下一次最小诊断应先区分：方向进入域的步长上限太小、域内仍不下降、或实际 Jd 与残差不一致。这三个问题需要不同处理。本文给出一个可选择的频率加权方向阻尼方案；它不修改状态表示、RHS、尾部、有限 BC 或最终验收容差，但迭代方向和对应 Armijo 下降项必须一致调整，不能偷用原 Newton 专属的下降预测。

没有运行新数值；不声称任何步长、方向或新候选已经成功。没有给原完整场增加新的最终验收门。

## 1. 已核对的公开源码

本次通过 GitHub 小文本接口只读了以下具体实现；列出的是 Git blob 身份：

| 源 | Git blob SHA | 本文使用的事实 |
|---|---|---|
| geometry_20261114_full_dn_augmented.py | 05608a21d822a3150d0ac4fba656909f85c33b6d | scalar_jets 对每个节点的全部 controls 仿射；物理 RHS 不显含附加 core；c、p 行导数为零 |
| geometry_20261114_r225_free_core_bvp.py | 64ad4f0b9ca6b1edb4a46d27ff5f6b87154e3a95 | BatchedFFTFlow 的完整角一、二导、Frenet frame 和原投影 |
| geometry_20261114_projected_core_bvp.py | 2d3e7a072a94855cb92ba458b4d9e779a5fe1946 | released_newton 的 17 次试探、原 factor merit 和最终检查 |
| geometry_20261114_lifted_modes_prepare.py | a587f1f2d6578a676ee96360e06a0e99fef97e90 | domain_minimum、真实 cubic-Hermite RMS/Lobatto 检查 |
| geometry_20261114_actual_direction_probe.py | 5d09c812bdf2d535e05879809756328138220244 | 原完整 collocation_fun 合成、实际方向的独立 Jd 检查、真实试探 midpoint |
| geometry_20261114_full_dn_solve.py | 2a988fa4767c63dea0caca5ab3032e10d64d4388 | endpoint rho guard、原 complete solve 与 RMS/BC 门 |

本文的链接对象是 computations 中这些原源。终端 Rphi 修补改变的边界行应使用其本身的当前实现；本文不把上表旧材料测试入口冒充已修补的实际边界。下列物理域和中点推导只依赖仍在使用的 AugmentedFlow 与原 collocation 定义。

## 2. 使用原 scalar_jets，不更换 scalar

写完整增广节点状态为
$X_i=(y_i,c_i,p_i)$，其中物理维数为 $3M+2$，$c_i$ 有 $M$ 个分量，$p_i$ 包含全部实际 active controls。

给定线性求解器产生的完整方向
$D_i=(d_i,d_i^c,d_i^p)$，试探为
$$
X_i(\alpha)=X_i-\alpha D_i.
$$
在固定位置 $s_i$，原代码严格使用
$$
(a_i,\nu_i,\gamma_i)
=\mathrm{base\_jet}(s_i)+
  \mathrm{control\_jets}(s_i)\,p_i.
$$
这里 $\nu_i$ 表示原 scalar_jets 的第二列，$\gamma_i$ 表示第三列。不得把它们替换成另一次精确积分、另一条 profile 或用不同公式求出的导数。

故同一原公式下
$$
a_i(\alpha)=a_i-\alpha\,\delta a_i,\qquad
\nu_i(\alpha)=\nu_i-\alpha\,\delta\nu_i,
$$
其中两项方向量分别由 controls 的第零和第一 jet 乘以 $d_i^p$。每个节点须使用自己的实际 $p_i,d_i^p$；在增广常数行尚有残差的试探期间，不能先冻结为终端 p。

原 AugmentedFlow 的实域额外要求
$$
a>0,\qquad |\nu|<1,
$$
以及 scalar jets 有限。有限 Fourier Frenet 公式还有下述角曲线域条件。

## 3. 节点上的精确域恒等式与次数

在一个实际物理角 $\phi$，记原 BatchedFFTFlow 合成的世界角导数（以旋转正交基表达）
$$
d=F_\phi,\qquad e=F_{\phi\phi}.
$$
两者都是完整物理状态 y 的线性函数，包括 R/T 旋转基的一阶和二阶项。完整 z0 被保留在状态中，虽然它不进入这两个角导数。

定义
$$
A=d\cdot d,\qquad B=d\cdot e,\qquad C=e\cdot e,\qquad
W=AC-B^2=|d\times e|^2.
$$
在 $A>0,W>0$ 时，
$$
\lambda^2=A,\qquad
|e-(B/A)d|^2=W/A,\qquad
\kappa=\frac{\sqrt W}{A^{3/2}}.
$$
原 Frenet 系数及其定义域为
$$
\alpha_{\rm Frenet}=-\frac{\nu}{a\kappa},\qquad
\beta^2=1-\frac{\nu^2 A^3}{a^2W}.
$$
这里把步长仍记为 alpha；alpha_Frenet 是不同的量。

可用以下无除法分子描述严格光滑域：
$$
G=a^2W-\nu^2 A^3>0,\qquad A>0,\qquad a>0.
\tag{D1}
$$
在这些条件下 W 自动为正，且 beta 严格为正。仍需原附加条件 $|\nu|<1$。beta=0 可能使一次 sqrt 返回有限数，但原 Jacobian 包含其导数，不能把它当作光滑 Newton 内点；零曲率也不能因 nu=0 就忽略原 0/0。

沿节点试探，$d(\alpha),e(\alpha),a(\alpha),\nu(\alpha)$ 均仿射。因此
$$
\deg A\le2,\qquad \deg W\le4,\qquad
\deg G=\deg(a^2W-\nu^2 A^3)\le8.
\tag{D2}
$$
这些是同一原连续代数公式的恒等式，不是声称浮点 FFT 与多项式根隔离有机器严格证明。最终每个试探仍须调用原 RHS。

理论上，有限角采样集合上的第一个域边界可以由这些多项式的首个正根隔离。对全部节点和数百万角点逐点解八次多项式通常不是最小计算；下面的保守界更适合初始步长预估。

### 3.1 只需角一、二导方向的便宜下界

在一个实际节点/角点记
$$
D_0=|d|,\quad E_0=|e|,\quad C_0=|d\times e|,
\quad D_1=|\delta d|,\quad E_1=|\delta e|.
$$
则对 $0\le t\le\alpha$，
$$
|d(t)|\le D_0+\alpha D_1,\qquad
|d(t)|\ge D_0-\alpha D_1,
$$
$$
|d(t)\times e(t)|
\ge C_0-\alpha(D_0E_1+E_0D_1)-\alpha^2D_1E_1
=:C_-(\alpha).
$$
同时取
$$
a_-(\alpha)=a-\alpha|\delta a|,\qquad
\nu_+(\alpha)=|\nu|+\alpha|\delta\nu|.
$$
若
$$
a_->0,\quad \nu_+<1,\quad D_0-\alpha D_1>0,\quad C_->0,
$$
并且
$$
a_-(\alpha)C_-(\alpha)>
\nu_+(\alpha)(D_0+\alpha D_1)^3,
\tag{D3}
$$
则整个 $[0,\alpha]$ 的该节点/角点均在严格 Frenet 域内。证明是代入
$\kappa\ge C_-/(D_0+\alpha D_1)^3$。左侧随着 alpha 非增、右侧非减，所以可以用短二分找保守 cap，而不解数百万八次方程。

采用实际 FFT 合成 $\delta d,\delta e$ 可使界比只用最高频系数范数更紧；这些合成不需要再分解全 Jacobian。若用它作数值 cap，须留舍入余量并以原 RHS 复核，不将三角不等式计算冒充新的连续曲面证书。

## 4. core 的 rho 约束另行处理

在 AugmentedFlow 的物理 RHS 中，附加 c 行不显含于 frame：它们的微分方程为零。原完整 y 包含真正的几何状态；c 通过左端识别和右端材料坐标参与边界。

右端的材料密度为
$$
\rho(c,\phi)=1+\sum_{m=1}^M(1-4m^2)c_m\cos(2m\phi).
$$
所以
$$
\rho(c-\alpha d^c,\phi)=\rho(c,\phi)-\alpha\,\delta\rho(\phi).
\tag{D4}
$$
对原 guard 的每个角采样点，只有 $\delta\rho>0$ 的点给出正向步长上限 $\rho/\delta\rho$；其余点不在这个方向下降。应使用实际 endpoint 的 c 和方向，而不是从某个旧 core 读一条密度。

若另有当前全圆严格下界 $\rho\ge\rho_*>0$，则
$$
\alpha\sum_m(4m^2-1)|d^c_m|<\rho_*
\tag{D5}
$$
是全圆安全的充分条件。它可利用已有合法的全圆下界；不能把一个新加而很保守的 l1 证书当作当前迭代或课题完成的强制门。仅在原角采样点为正也不自动证明全圆为正。材料逆图和实际新 Rphi 边界仍需原函数真实计算，逆图失败仍是无效试探。

## 5. 核心区别：真实 Hermite 中点不是线性状态

原 collocation 先在试探节点重新求
$$
f_i(\alpha)=f(s_i,X_i-\alpha D_i),
$$
再构造
$$
m_i(\alpha)=
\frac{X_i-\alpha D_i+X_{i+1}-\alpha D_{i+1}}2
+\frac{h_i}{8}\bigl(f_i(\alpha)-f_{i+1}(\alpha)\bigr).
\tag{D6}
$$
随后求 $f(s_{i+1/2},m_i(\alpha))$。因此即使所有试探节点通过 (D1)，中点也可能出域。把 m_i 写成旧 midpoint 减去端点方向均值是错误的；使用旧 nodal RHS 构造试探中点也改变了原方程。

设 $J_i=D_X f(s_i,X_i)$ 是同一原 augmented RHS 的完整节点导数。则真实中点路径的一阶方向为
$$
m_i'(0)=-D_i^{\rm mid},\qquad
D_i^{\rm mid}=
\frac{D_i+D_{i+1}}2+
\frac{h_i}{8}(J_iD_i-J_{i+1}D_{i+1}).
\tag{D7}
$$
这个公式包含所有 physical 与 active scalar 控制的导数。原 c、p 的 RHS 恒为零，所以它们的 midpoint 值确实分别为端点均值、沿步长仿射；非线性集中在物理 midpoint 的 RHS 修正，不能把整增广中点都当仿射。

更明确地，若
$$
f_i(\alpha)=f_i(0)-\alpha J_iD_i+r_i(\alpha),
$$
则
$$
m_i(\alpha)=m_i(0)-\alpha D_i^{\rm mid}
+\frac{h_i}{8}\bigl(r_i(\alpha)-r_{i+1}(\alpha)\bigr).
\tag{D8}
$$
若在完整安全路径上另已知
$|r_i(\alpha)|\le\alpha^2 L_i/2$，则中点余项至多
$h_i\alpha^2(L_i+L_{i+1})/16$。这里的 L_i 必须在实际所用角导或加权状态范数中给出；不能从旧点态 Jacobian 或一次共点检验自动获得。靠近 beta=0 时 RHS 的高阶导数可很大，因此只用 (D7) 的线性预测不足以保证中点。

对任意 Hermite 分数 tau，原曲线为
$$
H_{00}(\tau)X_i(\alpha)+H_{01}(\tau)X_{i+1}(\alpha)
+h_i\{H_{10}(\tau)f_i(\alpha)+H_{11}(\tau)f_{i+1}(\alpha)\}.
\tag{D9}
$$
所以同一问题也出现在原 RMS 的两个非中点 Lobatto 位置。需要时应复用同一组新 nodal RHS，按真实 Hermite 公式检查这些点；不能只核节点和一个线性 midpoint。

### 5.1 一个定性但有用的结论

若当前全部原查询节点、中点、需要的 RMS 点和边界图均严格在域内，原函数在它们附近连续，而且这些查询集合有限，则必有某个正步长邻域使完整试探仍在域内。这只给存在性，不给有用的步长大小。若节点方向或中点二阶响应很大，该邻域可以小到数值上无法取得实质进展。

## 6. 建议的最小域步长接口

在新的实际 bridge 网格结果出来后，若仍需诊断，只针对它的实际第一次失败方向即可；不必重做旧 A、旧 P 或旧尾锚。

1. 保留同一实际完整当前状态、方向、源及因子身份。先用当前原 col_fun、bc 重现残差，确认当前状态本身有完整有限残差。
2. 用节点方向合成角一、二导，计算 (D3) 的保守 cap；同时处理原 a、nu 条件和 endpoint rho 的方向 cap。记录限制步长的实际节点/角度及各原 margin。
3. 从该 cap 内部开始，用原 col_fun 重算试探节点 RHS、真实 midpoint 和 midpoint RHS，再调用当前真实 BC。需要避免 solve_bvp 结束后的 RMS 域问题时，复用这次 nodal RHS 检查原两个 Lobatto 点。
4. 对每次试探报告 nodes、midpoints、Lobatto、rho、BC 哪一项失败。有限域通过之后才评价原 factor merit；不能把“有限”当作“接受”。
5. 必须记录有效更新量与实际残差下降，而不只记录 alpha。若只有 alpha 极小时才有限、更新已接近浮点分辨率，或下降不能超出数值噪声，结论是该方向停滞；不称收敛，也不循环无期限缩步。

单凭新的预估 cap 不保证比原 17 次试探更快：它的价值是避免明知不可能的试探，并定位节点与真实 midpoint 谁在限制。若它只得到极小 cap，下一项应改变方向或更换有依据的 warm，而不是无解释地扩展回溯到更小 alpha。

## 7. 一个不改变最终方程的 Sobolev 方向备选

### 7.1 为什么欧氏系数长度不足以描述域风险

定义物理方向的加权系数范数
$$
\|d_y\|_{\mathcal H^3}^2=\sum_j(1+\omega_j^2)^3 |(d_y)_j|^2,
$$
其中对 r_m、t_m 可取 $\omega_j=2m+1$，对 z_m 取 $\omega_j=2m$。对 ell=1,2，由旋转基的 Fourier 展开及 Cauchy--Schwarz，
$$
\|\delta F_{\phi^\ell}\|_\infty
\le
\left[\sum_j\frac{\omega_j^{2\ell}}{(1+\omega_j^2)^3}\right]^{1/2}
\|d_y\|_{\mathcal H^3}.
\tag{D10}
$$
括号中的数随 M 增大仍有统一有限上界，因为最坏 ell=2 的尾和按频率平方倒数收敛。实际基函数可能给出更紧常数，但不影响该保守界。只控制无权系数二范数则不能同样控制一、二角导。

完整 z0 不被删除；它不影响角域，但仍属于真实状态、边界和 merit。core 的 rho 响应按 (D4) 另有频率平方权重；scalar controls 按原 control jets 缩放，不把它们塞进错误的 Fourier 模式。

### 7.2 便宜的加权方向阻尼

令 P 表示本次固定完整线性因子的求解算子，当前残差为 R，
$$
s=PR
$$
是原 Newton 搜索方向。选择固定对角非负权重 W，考虑
$$
d_\lambda=(I+\lambda W^TW)^{-1}s,\qquad \lambda\ge0.
\tag{D11}
$$
这是严格凸局部问题
$$
\min_d\;\frac12|d-s|^2+\frac{\lambda}{2}|Wd|^2
$$
的唯一解，也对应一个加权 trust ball 的拉格朗日形式。它只改变本次搜索方向，不截断状态、不投影掉高模式、不改变任何方程行，也不把旧尾移植成新尾。所有实际试探仍由原完整 RHS、当前 BC 和原真实尾接受程序处理。

如果希望在当前已满足的线性入口和常数行上保持方向关系，应给同一 m 的 r_m、t_m、c_m 同一阻尼系数，并在所有节点使用同一行权重。这样在原方向满足
$d^t_m+2m d^r_m=0$、$d^c_m-d^r_m=0$ 及常数行时，这些关系仍成立。z 入口齐次关系也保留。若当前线性行已有残差或数值方向没有满足它们，不能声称阻尼自动修复；所有完整行仍须进入真实 merit 和最终检查。

权重的整体单位可以统一归一化；它只重参数化 lambda。不能以硬截断高模或用新的 reference field 替换实际有限场。

### 7.3 必须匹配阻尼方向的下降检验

原实现的固定因子 merit 是
$$
C(X)=|P\,R(X)|^2.
$$
对任意方向 d，
$$
\left.\frac{d}{d\alpha}C(X-\alpha d)\right|_{\alpha=0}
=-2\,s^T P J_{\rm actual}d.
\tag{D12}
$$
若 P 恰为真实 J 的逆，则对 (D11)，
$$
s^Td_\lambda=\sum_j\frac{s_j^2}{1+\lambda w_j^2}>0
$$
只要 s 非零。因此每个有限 lambda 给出严格下降方向。这个数学结论依赖同一个真实 J；不能因已有 LU/QR factor 就忽略实际 Jd 的误差。

在实际代码中应测
$$
\chi=s^T P J_{\rm actual}d.
$$
J_actual d 可沿原 actual_direction_probe 的方式取得：对整个 col_fun 组成，包括非线性 midpoint，做已有合法 complex 方向微分；边界用当前真实 Rphi 的完整实 Jacobian。无需重新组装另一个全 Jacobian来得到这个方向乘积。若 chi 非正，应先处理方向/线性化，不把更多回溯当作补救。

原 Newton 的接受式为
$$
C(X-\alpha s)<(1-0.4\alpha)C(X).
$$
对阻尼后的 d，正确的同一 Armijo 常数对应式是
$$
\boxed{C(X-\alpha d)<C(X)-0.4\alpha\,\chi.}
\tag{D13}
$$
在精确 Newton 情况 d=s、PJ=I 时，它恰还原原式。若把 d 改了却保留右侧 0.4 alpha C(X)，在强阻尼时即使方向严格下降，也可能对所有足够小 alpha 都不满足错误的下降预测。

(D13) 只改变迭代算法的匹配下降条件，不降低最终原方程的 RMS 或 BC 容差。应如实记录 damping、chi、实际 residual、实际步幅；强阻尼造成的微小下降不能称最终接受。阻尼后是否重用旧因子、何时重线性化也须显式记录，不继承原 alpha=1 就是未阻尼 Newton 的隐含判断。

## 8. 目前最有因的决策顺序

当前还没有新实际域/方向测量可以宣布哪种备选成功，故不提前启用阻尼、不替换现有 bridge 联解。

若新实际方向的独立 Jd 已明显不符完整残差，先解决真实线性解或实际离散块；域 cap 只能暴露问题，不能修复错误的 Newton 方程。

若 Jd 一致，但域 cap 极小且高角导响应主导，可在**同一实际场、同一当前真实尾图**上比较一次原方向与少量 (D11) 的方向：真实中点和原 BC 全重算，以 (D12)--(D13) 判是否取得可用的完整残差下降。这个比较不需要另求零尾，不因显示网格或有限场模式改变对象。

若存在合理步长且全部真实查询点在域内，却 merit 仍失败，节点定义域不是主要障碍。应看实际下降率、线性模型误差及当前 warm，而非继续扩大 rho/beta 的安全余量。

若只剩极小 alpha 或极大 lambda 能通过，且完整残差无实质下降，就如实记录停滞。本文不提供一个靠缩步便必定解出该 BVP 的收敛定理。

## 9. 原运行结束后的接续说明

request15 的实际终态已归档于 [末桥段加密失败](2026-11-14-actual-bridge-resolution-failure.md)。本轮下一主线选择精确入口/常数约束下的正阻尼 LSMR warm，使用与其残差权重一致的 merit 与实际方向导数；不是直接启用本文 (D11) 的过滤 Newton。本文的节点域、中点非线性及 Armijo 一致性推导仍适用。没有额外最终验收门，也不以任一 warm 下降冒完整联解接受。
