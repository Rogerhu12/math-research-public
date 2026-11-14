# 固定物理 g 的有限前缀：高度均值的一、二阶连续比较接口

日期：2026-11-12。范围：两份有限 Fourier/物理五次场在同一物理 profile 和同一材料角图下的比较。当前 actual q096 已验收；M28 尚未运行。本条不重新求 q096，不改任何 MJS、真实尾、BVP 或验收门。

## 1. 与实际代码相同的均值定义

固定 source commit 为 869436630c99aa5a68afb55bd8877c826034d117。

- [adaptive frame / velocity_s](../../visible-flexible-closed-surface/scripts/950f-prefix-adaptive-chart-bvp-v2.py)，SHA256 958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe，第 54–85 行，给出实际 Frenet 法向速度以及在固定计算角 ψ 下的 s 导数。
- [cylindrical height_integral / frame_jvp](../../visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/curve_stable_prefix_bvp.py)，SHA256 e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2，第 124–137、244–263 行。实际诊断用 ψ 上等权离散平均和逐原区间 Gauss 积分；本条连续对象采用对应的精确平均和精确反导数：
\[
 H'(s)=\frac1{2\pi}\int_0^{2\pi}V_z(s,\psi)\,d\psi,\qquad H(0)=0.
\]
这里没有额外的角 Jacobian 权重 ρ。V 是代码在固定 ψ 下的完整速度，已含 vF_ψ。不能把法向部分单独平均，也不能换成物理 θ 的等权平均。

数值 Gauss 值和这些精确积分之间仍需独立误差支付；本条不宣称原有限诊断的位置与其独立记录的 jets 已成为一个经过认证的精确 C² 函数。

## 2. 与 frame 恒等的无单位向量表达式

令
\[
 d=F_\psi,\quad e=F_{\psi\psi},\quad
 f=F_{s\psi},\quad g=F_{s\psi\psi},\quad c=a'/a.
\]
这些角导数不含独立的高度均值。写
\[
 P=d\cdot d,\quad R=d\cdot e,\quad w=d\times e,\quad
 W=w\cdot w,\quad {\cal D}=W-c^2P^3.
\]
此处 \({\cal D}\) 是 Frenet 判别式，与整面直径 D 无关。当 \(P,W,{\cal D}>0\) 时，
\[
 T=d/\sqrt P,\quad
 N=(Pe-Rd)/(\sqrt P\sqrt W),\quad
 B=w/\sqrt W,\quad
 \kappa=\sqrt W/P^{3/2},\quad
 \alpha=-cP^{3/2}/\sqrt W.
\]
因此代码使用的正 β 分支恰为
\[
 \boxed{
 V=\frac{-cP(Pe-Rd)+\sqrt{\cal D}\,w}{W}+v\,d .
 }
\]
这是同一数学函数的恒等式，仅用于证书消费器；原数值 frame 的运算次序完全不变。margin=\({\cal D}/W\)，所以须在整个比较同伦内证明正性，不能只检查两个端点的离散 margin。

## 3. 同伦与四分量精确区间 AD

设 coarse/fine 的有限非均值场分别为 \(F^0,F^1\)，两者物理 g、角图和 gauge 完全相同。令 \(F^u=F^0+u(F^1-F^0)\)，\(0\le u\le1\)。对每个物理 s、归一角 \(\psi/(2\pi)\)、u 的完整矩形盒，输入：

- \(d_0,e_0,f_0,g_0\) 与完整差 \(\Delta d,\Delta e,\Delta f,\Delta g\) 的实区间；
- 共同 profile 的 \(a,a_s,a_{ss}\)，其中 a 的下界严格正；
- 共同角图的 \(v,v_s\)。

消费器自动由 \(a_s/a\) 算 c，并由同一个比值的 s 导数算 \(c_s=a_{ss}/a-a_s^2/a^2\)，不接受另一个可能不一致的自由 c_s。

每个标量带四个区间槽
\[
 (z,z_u,z_s,z_{us}).
\]
乘法和一元复合采用精确链式法则；例如
\[
 (xy)_{us}=x_{us}y+x_uy_s+x_sy_u+xy_{us},\qquad
 (\phi(z))_{us}=\phi'(z)z_{us}+\phi''(z)z_uz_s.
\]
全部端点为 BigInt 有理数。sqrt 先识别分子/分母均完全平方的情形，否则用整数平方根给二进制网格上的外包上下界。任何 a、P、W 或 \({\cal D}\) 未证正的盒立即明确拒绝，不借端点样本补过。

将上节 V 代入，所得 \(V_{z,u}\) 和 \(V_{z,us}\) 的区间包围完整同伦。依次对 u 和归一角加正权重：
\[
 \Delta H'(s)=\int_0^1\int_0^1
 V_{z,u}(s,2\pi x,u)\,du\,dx,
\]
\[
 \Delta H''(s)=\int_0^1\int_0^1
 V_{z,us}(s,2\pi x,u)\,du\,dx.
\]
角平均的 \(2\pi\) 恰与 \(d\psi=2\pi dx\) 抵消。消费器逐 s slab 汇总区间，不只把所有绝对值统一取最大。再从明确的高度锚差逐 s slab 积分，可得到 A0；较简便的后果仍是共同锚 H(0)=0 时 \(A_0\le L A_1\)。

这些均值项只加到有限场比较的 position、s、ss 行；theta、s_theta、theta_theta 不额外加均值。

## 4. 为什么还需 E12

完整保存五次场给出
\[
 \Delta g=q\sum_j\Delta Y'_j(s)B''_j(\psi).
\]
所以均值二阶证书需要 E12=\(\sup|\partial_s\partial_\psi^2\Delta F_{\rm nonmean}|\)。这不是六个总阶数不超过二的场差之一，但可直接从同一有限五次系数精确导出，不需要新 RHS。

本批对 strong_sameg_continuous_finite_field.py 的唯一数学输出扩充，就是在原全区间 Bernstein 循环内保存
\[
 E_{12}\le |q|\sum_j \|\Delta Y'_j\|_{\infty}
                  \sup_\psi|B_j''(\psi)|.
\]
原六项物理两阶误差矩阵、输入身份、全部 Fourier 行和旧 t 保留门均不变。旧准备源 SHA 为 687362608ccc71b0b22a296a908833385cefad70089b49b445f078dbe5e17828，新源 SHA 为 8ceb28045607f7c533c134bf2281a00c644c5728c2bb3714a51238a4c4eefa12；两版本都尚未对实际 M24/M28 输入执行。

若暂只已有全局 E01/E02/E11/E12，它们可给每分量的对称差区间；实际收紧宜由原多项式和角盒生成有符号区间。共同背景在差中消失，但 absolute coarse d/e/f/g 的界仍须付完整背景和全部有限模式。

## 5. 可执行消费器、已执行检查与明确缺口

新源：computations/strong_mean_homotopy_exact.js。接口：

    node computations/strong_mean_homotopy_exact.js --input <field-boxes.json> --out <fresh-result.json>

纯代数检查：

    node computations/strong_mean_homotopy_exact.js --self-check --out <fresh-check.json>

输入 schema 为 strong-mean-homotopy-interval-input-v1，精确数一律用十进制/有理数字符串，区间用两字符串数组；三网格为 physical_s_breaks、angular_turn_breaks、homotopy_breaks。每 box 给 index=[s,angle,u] 和第 3 节字段。源内 fixtureInput/selfCheck 提供协议示例，其盒只是代数夹具，不能借为任何曲面数据。

本次实际在 functions JavaScript isolate 中执行了 15 项检查，全部通过：非二进制有理平方根的轴向精确值、四分量 circle 混合导数恒等、三维有理旋转协变、sqrt 外包、退化/越域拒绝、完整八盒覆盖、零差精确均值、漏盒/重盒/非正半径拒绝、非零有限界，以及实际认证标志始终为 false。0 Node 物理 worker、0 RHS、0 BVP。完整执行 ledger 单独保存；Node CLI 尚未运行。

消费器**只证明输入区间蕴含输出界**，不生成或验证实际 coarse/fine 场盒。因此其 output 明确保持：

- source_field_enclosures_verified_by_this_tool=false；
- actual_prefix_C2_certificate=false；
- exact_knot_continuity_inferred=false；
- convergence_to_exact_solution_claim=false。

仍欠实际 M28 成功包、实际全部 s/ψ 盒的严格生成与覆盖、共同 profile/角图的盒证明、真实全同伦域，以及全局 knot 连续性或明确修复。对有限数值 Gauss/角均值诊断，还欠它们到本条精确均值的误差。现有两端样本或普通浮点 bounds 均不能填这些字段。

本接口严格只用于固定 g 比较。若换新物理设计，c、v 对 u 的导数及混合导数通常不为零，必须换显式新接口，不能沿用本消费器的零列假设。
