# 独立审查：weighted 旋转内尾与有限圆领包

2026-11-09，independent_geometry；未参与尾部形状选择、射击求解或原 packet 提取实现。

审查对象 `2026-11-09-db6f-tail-background-collar-proof.md`，冻结 SHA256 见同名审查 JSON。
第 1–3 节数学结论 **PASS，作为条件命题**；第 4 节数字依其明确的有限多项式范围通过独立复核。

## 1. 已要求并落实的小修

实际 `slopeCap=0.02` 是一个略大于 $1/50$ 的 binary64 有理数。原稿把 finite cap 精确写成 $1/50$，不能按字面覆盖该实际数。作者已改为 $0<c_{cap}\le1/49$，于是 $w/r<50/343<1/6<6$。此处没有修改物理参数，且其余估计不受影响。

## 2. 源码与连续曲率

已逐项核 `closing_recalibrated_tail.mjs` 的 cap、profileSource、integrand、physicalCell 及 `closing_weighted_tail.mjs` 的 weight 安装。

- raw node $N$ 位于 cell $N-1$ 的内端；$[a,r_N]$ 对 $N\ge1$ 不含 cell 0。当前特殊 pulse/valley cap、cut-preserving 修补及非单位 weight 全只作用于 cell 0，排除范围正确。
- 其余有限 pieces 的径向速度为 $|w_x|/(6E^{3/2})+\alpha |(r_o)_x|/E$，因此实际旋转母线曲率不超过 6，且正 free term 保持正径向速度。不能把该背景结论直接套给非轴对称实际图。
- 唯一保护混合位于 cell 159 第一个 flat port；其旧源导数 $w_r=-7w/r$ 的连续上界远小于 6，凸混合保留不等式。使用的是 cap 完全未激活的极小 slope 区。
- 正 cap 过渡的 log 导数介于 0 与 1，且 log 输出不超过 cap 值。内部 $w_x=0$ 的 cusp 不使 $w_r=w_x/v_r$ 不连续。跨 piece 的原斜率、原 $w_r$ 和 ports weight 配对一致，故两阶几何匹配。
- 深处用 $w,w_r\to0$ 给真实 $C^2$ 平圆领。没有要求 warp 的辅助参数化在所有 cusp 为 $C^2$。

R46 的根范围在这里仅用于原深 profile 的 $\alpha_n\in[1/2,2]$，不是用其非有效 47 参数定理给当前入口补无限延拓。稿中 $α>0$ 的 exact-integral 径向分配仍是明确假设；当前浮点 quadrature 的误差需在实际图认证中另付。

## 3. 独立有理复核

脚本 `../scripts/db6f-audit-tail-background-and-packet.py` 不导入原构造或原 Fraction 检查模块。它核对实际 packet 的参数、uniform box、所有深源粗界和有限 Fourier 三阶端迹范数。

以精确 Fraction 得 $B_{160}<0.065756467<0.066$；后续第一项的比由 $(6/7)(H_n+7/5)/H_n<1$ 控制，第二项也下降。保护端旧 $|w_r|$ 小于 $2\cdot10^{-79}$。因此不依赖径向采样得到全部原始深尾与保护端曲率界。

Hermite 估计的简化常数也逐项正确：$\sqrt5<9/4$，$\sqrt2<3/2$，以及在 $L/a\le1,LB\le1$ 时 $\sqrt{14^2+27}<15$。有限实 cos/sin 的坐标绝对值和支配原 R6 的向量 Fourier 主范数。

## 4. 实际 packet 重跑

独立重新执行 `db6f-tail-collar-packet.mjs`，从同一已存 depth12、M12、pure height $-0.0003$ 状态提取 raw node 8，使用 256 角节点和原差分步长。所有保存的系数、projection-change 量、端点诊断及物理半径与原 C3 packet **逐值相同**。

另外独立重算原 packet 的全部节点 4/6/8/10/12 的 Fraction 账本，与原检查吻合。node8 有
$$K_8<4.694359\cdot10^{-22},\quad e_g<5.357586\cdot10^{-24},\quad e_D<6.357734\cdot10^{-20}.$$
这些不是未知精确端迹的误差界，而是**所保存有限多项式作为精确定义时，Hermite 闭合层的条件上界**。其中 planar 二阶导数仍来自有限差分源值，不能把 Fraction 复算误称为其对未知精确 ODE 解的误差控制。

C3/reflection 投影公式正确：平面复分量只保留频率 $1\bmod3$；正实频率 $m\equiv1$ 时要求 $X_{\cos}=Y_{\sin}$，$m\equiv2$ 时要求 $X_{\cos}=-Y_{\sin}$；高度仅保留 $3\mathbb Z$ 余弦。每个投影改变量已保存。外域必须采用完全相同的 projected shared jets，且高度刚体规范必须统一。

## 5. 保留的缺口

本次没有证明真实连续 flow 的端点误差、完整外域 $C^2$ Cauchy 性、真正无限非线性尾或全局闭曲面。背景定理、有限 Hermite 条件账本和“当前截断值属于一个精确无限解”是三个不同命题；本次仅通过前两个。
