# v4 浅回转物理参数：完整 C² 家族与 BVP JVP

2026-11-12，constructive_geometry。此文是可直接消费的外层设计输入，不是等距相位族结论。
母线参数 T 改变 g；必须在真实非线性匹配和几何条件得到后固定一个 T，再验证该同一个 g。

## 1. 已冻结 v4 与唯一变化参数

冻结文件 `2026-11-12-fd2d-ellipse-b05-frozen-candidate-v4.json` 的 SHA256 是
`1180a59ddea1a62036b04e814fbf2f4b7aa419efc71c0035a49ace722a552a9d`。
`2026-11-12-fd2d-ellipse-b05-frozen-v4-input-manifest.json` 指定同 a0 的 R118 balanced seed。
v4 文件保持不变；任何新的 T 必须作为新候选另存，不覆盖 v4。

v4 保持原 .2 中央柱及 .33 冻结前缀，随后以共享两 jet 的加速度段
（entry=.04，plateau 加速度 −2.5，exit=.04）到 a′=−.98。
以 |meridian phase derivative|≤6.8 的 C² 转角段回到相位 −.1，
走一段浅 coast，再深转到 −π/2+.001，走深 coast，最后走原 cut brake。
cut 仍为 r=.4、w=.1、wr=−7/4，cuff=.32。

唯一外层参数为浅 coast 的准确长度 T。记

\[
v_m=-\sin(.1),\quad c_m=\cos(.1),\qquad
v_d=-\cos(.001),\quad c_d=\sin(.001).
\tag{1}
\]

所有其余相位函数、段长、加速度段和初始 a0 保持 v4 原样。
浅 coast 增长使半径多下降 \(v_m\,dT\)，让最终深 coast 长度补偿

\[
L_d(T)=L_d(T_0)-\frac{v_m}{v_d}(T-T_0),
\tag{2}
\]

其中

\[
T_0=.016570820467696108,\qquad
L_d(T_0)=.0374855869469202.
\tag{3}
\]

(2) 准确保持末端 brake 的初始半径；其相位与长度都固定，故 cut 的 a、a′、a″ 全部不变。
共享两 jet 定义和每个转角段的端点 a″=0 保证全部接点仍 C²。
这是整个后缀及其真实 cut 两 jet 的参数族，不是只改一个末端边界数值。

## 2. 参数范围与背景高度

深 coast 非负当且仅当

\[
0\le T\le T_{\max}=T_0+L_d(T_0)\frac{v_d}{v_m}
\approx .3920519916344375.
\tag{4}
\]

实现取右端严格不等式以保留非零深 coast。
浅 coast 在 T=0 退化为零长度，拼接曲线本身仍 C²；分段求解器如要求每段严格正长，
可使用 0<T<Tmax。整个后缀半径最小值仍为 cut=.4。

总弧长与**旋转背景**高度的准确参数导数为

\[
L'(T)=1-\frac{v_m}{v_d}=.9001665334364427\ldots,
\]

\[
Z_{\rm bg}'(T)=c_m-c_d\frac{v_m}{v_d}
=.9949043318281012\ldots.
\tag{5}
\]

加入原尾背景高度之后，实际评估给

| T | 旋转背景含尾高度 |
|---:|---:|
| 0 | 1.1986054691310362 |
| T0 | 1.2150918501962928 |
| .08 | 1.2781978156772844 |

因此 [0,.08] 是供当前外层设计使用的一个具体保守范围，其背景高度仍低于 R113 的 zc。
**这不是非圆核实际 cuff 高度界，也不是实际主曲率界。**
R120 允许最终真实 Z∈[.9,zc] 后直接平移完整帽，不再额外强制 Z=zc。
实际 Z 仍需由 BVP 的真实空间重建得到。

## 3. 各段固定参考坐标上的完整径向两 jet 导数

在每一段使用自己的固定坐标 \(\tau\in[0,1]\)，物理弧长为
\(s=s_j(T)+L_j(T)\tau\)。下面所有 ∂T 都在固定段号与 τ 下取。
这是 BVP 使用固定分段网格时的自然 JVP；不能把它误作固定全局 s 的偏导。

记 \(a_T=\partial_Ta\)、\(L_{j,T}=\partial_TL_j\)。除浅、深 coast 外段长均固定。
完整表为

| 段 | a_T | (a′)_T | (a″)_T | L_j,T | s_j,T |
|---|---:|---:|---:|---:|---:|
| 前缀及首次浅回转 | 0 | 0 | 0 | 0 | 0 |
| 浅 coast | v_m τ | 0 | 0 | 1 | 0 |
| 后续深转段 | v_m | 0 | 0 | 0 | 1 |
| 深 coast | v_m(1−τ) | 0 | 0 | −v_m/v_d | 1 |
| 最后 cut brake | 0 | 0 | 0 | 0 | 1−v_m/v_d |

**证明。** 前面各段不依赖 T。浅 coast 的半径是其固定初值加 \(v_mT\tau\)，故得第二行。
深转段只继承浅 coast 的半径初值变化 \(v_m\)，其相位函数与长度都固定。
深 coast 则为该初值加 \(v_dL_d(T)\tau\)，用 (2) 得第四行。
第四行末端的 a_T=0，所以最后 brake 的径向初值及整段两 jet 独立于 T。
所有 coast 相位恒定，所有其余段相位和长度固定，所以 a′、a″ 的该偏导始终为零。
累加段长导数给最后一列。证毕。

如果实现需要固定全局 s 的导数，则必须补偿坐标移动：

\[
\left.\partial_Ta\right|_s=a_T-a'\bigl(s_{j,T}+L_{j,T}\tau\bigr),
\]

\[
\left.\partial_Ta'\right|_s=-a''\bigl(s_{j,T}+L_{j,T}\tau\bigr).
\tag{6}
\]

在每段内部，a″ 的同类公式再包含该段 a‴。
本族的共享二 jet 保证 a 关于移动接点仍 C²，不要求 a‴ 在各接点相等。
分段 BVP 直接使用上表即可避免在接点给 a‴ 施加多余条件。

## 4. Gauss–Codazzi RHS 的物理 JVP

对 \(K=-a''/a\)、\(c=a'/a\)，在固定段坐标下有

\[
K_T=\frac{a''a_T}{a^2},\qquad c_T=-\frac{a'a_T}{a^2}.
\tag{7}
\]

固定种子法向角 φ 的度量因子为
\(b=a\rho_{\rm seed}(\phi)/a_0\)，故

\[
b_T=(\rho_{\rm seed}/a_0)a_T,\qquad
(1/b)_T=-(1/b)(a_T/a).
\tag{8}
\]

如果物理方程写为 \(Y_s=F(a,a',a'',Y)\)，规范段方程为
\(Y_\tau=L_jF\)。在固定 Y 时 T 的显式作用是

\[
\partial_T(L_jF)=L_{j,T}F+L_jF_a a_T,
\tag{9}
\]

或按 (7)–(8) 将 F_a 展开为对 K、c、b 的导数。
还须加普通状态 JVP \(L_jF_Y\dot Y\)；(9) 不包含实际解随 T 的隐式响应。
忽略第一项 \(L_{j,T}F\) 会漏掉浅、深 coast 的时间变化，不能只改半径。
cut 的径向数据固定，并不表示其外在 II 或尾非线性残差固定；这些正是 BVP 要求解的量。

## 5. 实现与已完成的核对

`../scripts/fd2d_partial_return_parameter.py` 的 `PartialReturnParameter` 提供：

- `bundle(T)`：完整新径向输入，保留 canonical 共享两 jet，标明尚未冻结；
- `candidate(T)`：与既有 `Candidate` 相同接口；
- `piece_jets(index,tau,T)`：上表的 a、a′、a″ 及参数导数、段长和起点导数、K/c 及其导数；
- `summary()`：准确公式的数值范围和不可混淆的状态标记。

v4 的浅 coast、深转、深 coast、cut brake 段号分别为 85、86、87、88。
实现以 label 查找，不硬编码这些序号。
`2026-11-12-fd2d-ellipse-partial-return-parameter-check.json` 保存真实中央差分检查：
step=1e−6，每段 17 点；a JVP 最大差 `1.12e−10`、a′ `2.78e−10`、a″ `4.89e−9`，
K `7.0e−9`、c `6.75e−10`。这些是浮点差分误差，解析 JVP 由上面的逐段公式证明。
文件同时绑定 v4 输入与 `Candidate` 源 SHA，不依赖一份未闭存的新 profile。

目前 v4 仍只是有限线性 m2 方向匹配候选：其方向残差约 `1.243e−10`、末端 gain 约 `−.0487182`。
大幅非圆闭解未必在这个离散线性共振的同一个 g 上存在；因此 T 是明示的物理外层设计参数，
可与中央非圆幅度约束一起求一个真实非线性闭合候选。
最终选定 T 后要另存新的 v5（或其他未占名称），再在那一个 g 上进行加密、连续后验和全时几何检查。
