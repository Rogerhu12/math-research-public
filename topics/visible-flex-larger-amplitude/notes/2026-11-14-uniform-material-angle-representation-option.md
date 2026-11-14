# 均匀材料角表示的可行性与实际成本

日期：2026-11-14。

## 判断

这是一个可定义的新有限离散方向，确有可证明的理想圆 coast 优点，但不是当前物理 phi 入口的直接换名。最重要的两件事已在 [R257](../results/R257-finite-unit-speed-Fourier-and-material-circle-Jacobian.md) 完整证明：

- 均匀 theta 的精确圆有限物理 Jacobian 在解析投影或 N>4M 的同一 DFT 下保留 R255 的全部模态块；
- 指定非圆平面入口若在 theta 中严格单位速，则其位置一般不能是纯有限 Cartesian Fourier。

所以应在“投影入口、付实际截断误差”和“完整解析入口 lift 加有限未知量”之间明确选择。两条路线都没有实际新解回执。当前 request17 的完整有限方程与 LSMR warm 主线继续，不因本 note 自动切换。

## 1. 连续重参数化保持什么

原实际 core 给出 theta=Theta_c(phi)，全圆 rho_c>0 时取真实逆图 Phi_c。对同一个完整连续场定义
$$
\widetilde F(s,\theta)=F(s,\Phi_c(\theta)).
$$
在 c 对 s 为常数的前提下，这是真正的同一像重参数化。若原 metric 为
$ds^2+a(s)^2\rho_c(\phi)^2d\phi^2$，它变成
$$
ds^2+a(s)^2d\theta^2.
$$
这里材料密度为 1 是坐标效果，不是把原 support rho_c 设为常数，也不是把旧 phi 曲线直接当成 theta 曲线。

若随后对 theta 做有限 Fourier 投影，得到的是一个新的有限场。不能因为前一步是重参数化，就把后一步仍称为同一有限几何对象。

## 2. 纯有限 theta 场：最省 RHS，但入口必须近似

写全物理场为旋转 theta 的有限 R/T/Z，保留完整 Z0。原 Frenet 曲率和 frame 公式本身可沿用，只把角节点、角导及 Fourier 投影真正改为材料 theta。

对原 support core，真实单位速入口是
$$
G_c(\theta)=\Gamma_c(\Phi_c(\theta)).
$$
在旋转 theta 基中先构造完整函数，再取实际指定投影，得到入口系数 $G_{M,N}(c)$。这个函数对全部 c 是非线性的；不能继续使用旧线性入口
$r_j=c_j,\ t_j=-2jc_j,\ r_0=1$ 作为 theta 系数。

特别地，theta 的 r0 不必等于原 support 的常数系数 1；固定前 K 个设计目标也应固定原 support c 的前 K 项，而不是误固定新 theta 位置的前 K 个 Fourier 系数。

可以令整个初始物理状态满足
$$
y_0=G_{M,N}(c)
$$
并保留 K 个 c 目标、c/p 常数行和全部 T 个右端方程。未知数计数仍为
$$
n(m-1)+(M-K)+k.
$$
当 T=M、K=k 时仍是平方系统。区别是入口 map 变为非线性，必须在每次 trial 真实重算，其 Jacobian 使用完整 $D_cG_{M,N}$，不能沿用 R256 的固定线性入口矩阵。

### 2.1 入口误差会直接进入原 metric 门

纯有限入口一般不严格单位速。若
$$
\|\partial_\theta(G_{M,N}-G_c)\|_\infty\le\varepsilon_1,
$$
则
$$
\bigl||\partial_\theta G_{M,N}|^2-1\bigr|
\le2\varepsilon_1+\varepsilon_1^2.
$$
这是原同一 canonical metric 的真实角度量误差，不是可以忽略的显示误差。仅有位置误差小不足以证明这一导数误差小。

径向加密不会消除一个固定入口 theta 截频的误差。若需同 g 精化，应冻结完整 scalar a(s)，并真实提高入口/场/求积分辨率，使这部分误差也受原 metric 验证控制。本 note 没有要求每个有限场字面精确等距；它只是不能把已改变的入口度量隐去。

rho_c 的小值会使 Phi_c 的角导大，可能需要高 theta 带宽。目前没有计算证明 M=112 是否足够。

### 2.2 入口导数并非必然因 1/rho 数值爆炸

R257 给出固定 theta 的完整位置导数
$$
\partial_{c_j}G_c
=\cos(2j\phi)e_r(\phi)-\frac{\sin(2j\phi)}{2j}e_\phi(\phi),
\qquad \phi=\Phi_c(\theta).
$$
这是两个复合导数项严格抵消后的公式，适合构造新入口 Jacobian，避免把两个大项先独立算出再相减。

连续位置 map 还有由 rho_min/rho_max 控制的 L2 下界。但这不保证截频后的有限 $D_cG_{M,N}$ 良态；高 theta 谱仍可能被投影丢掉。原右端 P 的病态不会因此被证明“到处消失”。

## 3. 完整入口 lift：能保原 core，但有限对象与 RHS 接口更复杂

一种明确的替代表示是保留原真实材料入口的全部角函数。令 $\mathcal G_c(\theta)$ 表示它在旋转 theta 基中的三分量，Z 分量为零。选择明确的有限合成 S 和投影 Q，满足 QS=I；Q 可以是固定的解析 Fourier 投影，也可以是明确记录的实际有限角求积投影。

取一个固定 C2 径向 cutoff chi，入口处 chi=1、chi'=chi''=0，在进入希望保留纯圆表示的 coast 之前 chi=chi'=chi''=0。定义
$$
B(s,\theta;c)=\chi(s)\,[\mathcal G_c(\theta)-S Q\mathcal G_c(\theta)],
$$
$$
\widetilde F_{\rm rotating}(s,\theta)=S y(s)+B(s,\theta;c).
\tag{U1}
$$
入口设 $y(0)=Q\mathcal G_c$，则完整场的入口恰为原 $\mathcal G_c$，不依赖 Q 对入口的近似精度。完整场已不再是纯有限 theta Fourier，这与 R257 的障碍一致。

相应投影演化应定义为
$$
y_s=Q[\mathcal V(Sy+B;a,\nu)-B_s].
\tag{U2}
$$
因为 c 对 s 恒定且 Q、S 固定，形式上 QB_s=0，但完整场的真实 s 导数仍是
$$
\widetilde F_s=S y_s+B_s,
$$
二阶导同样含 B_ss。不能因投影中的抵消就从 physical readout、metric 或曲率中删掉这些项。

这个方法有明确代价：

- 当 chi 非零时，RHS 显式依赖全部 c。当前 AugmentedFlow 把 core 列置零、R256 使用“物理 RHS 不显含 c”的稀疏块，都不能不改就沿用。
- 原 complex-step 不能直接穿过会强转 real 的材料逆图。需要完整解析 core 响应或明确有效的其他求导实现；R257 的位置导数公式能帮助第一阶响应，但角导、混合导及读取的完整 jets 仍须一并处理。
- 每个实际 RHS、域检查、collocation midpoint、固定 p residual 都必须合成整个 Sy+B，而不是只用未知 Fourier 系数 y。
- chi 的支撑、0/1/2 jets、Q 的实际规则及源身份构成新有限对象，不能混入同 g 精化而不声明。
- R251 现用纯有限 Laurent 带宽的 operator 证书不能自动覆盖 B 的无限角谱。需要该解析已知项的相应角包络；不能把旧有限带宽结论贴到新场。
- R254 的“解析开片加四点见证”原则仍可用，但其完整有限角网格的完备性依赖有限三角次数，不能自动用于这个 lift。实际四点若能精确或区间证明非零仍有效；不能虚报旧消费者已覆盖新函数。

当 chi 及其必要 jets 已归零，场恢复纯有限 theta 表示，所以理想圆 coast 的 R257 Jacobian 结构仍可保留。这里没有证明真实非圆解在该处已经变成圆，也没有保证该新离散存在接受解。

## 4. 右端 native DN 的简化是真实的，但只有这一部分

若 cut 附近场已是纯有限材料 theta，且高度非均值直接用全部 M 个 cosine 系数表示，则输入 native 尾的高度为
$$
H=\epsilon_h\,z_{\rm nonmean}.
$$
当 native T=M 时，原需要的 phi 到 theta 高度投影 P 变成直接系数读取，theta 斜率的回拉 S 也不再需要。右端为
$$
z_{s,\rm nonmean}-\mathrm{cut\_scale}\,D(H).
$$
全部 M 行仍保留，native 尾方程及真正非线性求解本身没有因此被替换。完整均值 Z0 仍存在，mean gauge、actual cut height 和最终 audit 均须使用新场。

这避免了那个特定的有限 P/S 右端坐标算子，却不自动解决：

- 新非圆内部 Frenet Jacobian 的域与条件数；
- 非线性入口投影的条件数；
- 长 coast 的非正规 shear；
- 真实 tail 对新 H 的可解性；
- 全 BVP 的全球化或收敛。

R257 的圆参考谱结论不能扩成以上任何一项的成功声明。

## 5. 闭面与 readout 不能继续误用旧逆图

新表示必须有新的 field_representation 身份，明确“系数角是材料 theta”。当前 SavedPrefix 读出若再次按 core 反解 theta->phi，就会对已是材料角的状态做第二次重参数化，得到错误曲面。

纯 theta 有限场的角 jets 很直接；完整 Z0 仍可按同一 shared-node Hermite 原则读取。但至少要明确调整：

- reader 的 inverse 为恒等，角密度为 1；原 support rho 只用于入口 core 的真实 map；
- 物理 node RHS/二阶 jets 的原公式和保存身份；
- 单一全局 SE(2)、height offset、实际 native H/config/response 的绑定；
- 全角 cut correction 与整个 closed assembly 使用的新完整位置及六/九 jets；
- R249 若作用于新场，所修改的有限 jets 与任何已知 lift 的入口 parity 应组合正确；
- 连续 metric、曲率/reach、真实全像 Hausdorff 与 marker 证据都要消费同一新场。

若采用 (U1)，还必须在上述每一个位置加入 B、B_s、B_ss 及角/混合导，不得只在显示时加 B。

使用精确入口 lift 时，入口像与对应 support core 相同，所以对该实际 c 已成立的像不变量可经重参数化保留；仍不能挪用另一 c 或另一整面 D。使用投影入口时，连 core 像也变了，原 core gap 证书必须计入真实投影误差后再用。

## 6. 换表示、设计与同 g 精化的分类

完整连续重参数化：同一场、同一像、同一 canonical metric。

固定同一 scalar 后的有限 theta 投影：新的有限近似，目标 metric 可相同，但必须实际量化新的入口和内部误差。

重新求 active controls p：新的设计过程；无论角表示如何，都不能自动叫作对旧 p 所给同一 g 的精化。

实际设计成功后冻结完整 a(s;p*)：才可按本题原标准研究同 g 的角/径向/尾部精化。原所有 scalar 段、bump、有限积分规则和身份都要保持，不能顺便换成另一条更方便的 profile。

当前有充分理由把均匀材料角作为有因备用方向，也有明确理由不把它当作免费修补。是否启用应由当前真实主线结果决定；本 note 没有派发计算、修改当前求解源或把理想圆推论当作新的接受结果。

