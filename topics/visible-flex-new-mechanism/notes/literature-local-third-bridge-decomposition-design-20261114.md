# 真实第三桥局部项的准确分解：公开 Actions 实验入口

状态：实现与待执行的研究代数。依赖 R73 的准确分解，本次目标是对角三次项 $\mathcal C_s(q;q,q)$。它决定纯模式的第三整体响应；未以对角项替代整个非对称三线性算子。

源码：[literature_local_third_bridge_decompose.py](../scripts/literature_local_third_bridge_decompose.py)。

## 1. 真正新增的计算目标

上一纯 bulk 实验已在公开 Actions 43628716304 完整执行：在当时不完备的 right-IBP 代表上，28 个可达响应的秩为 18，未得到准确身份。这不是函数不存在定理。本次不加大同一任务的预算，不重复 profile 拟合，而是加入 R73 已明确分离的真实局部三次密度。

先用 R56 原始 compiler 生成

$$
B=\mathcal I H(Y_q,Y_q),\qquad R[H(Y_q,B)].
$$

保留真实 history RHS 完成全部协变导数与恢复后，再把 history **值**置零。由 R73，这恰为

$$
\mathcal C_s(q;q,q)
=\ell_s(q;q,q)-\Psi_s(q,\Phi_{M(s)}(q,q)).
$$

这里的 $\Psi$ 一般非零。此入口没有在微分前删除 history，也没有把桥的基准第三项设零。

全部系数准确展开为 $h,k,\omega,h_s,k_s,h_{ss},k_{ss}$ 的 Laurent 多项式，$h$ 可有负整数次幂。$\omega_s=k_s/(2h)$ 始终保留。对固定 $s$，profile 表达式的普通复乘法、真实右原函数及左尾均保持。

依赖绑定：

- R56 compiler git blob 01c7424af3a96f2c2a0f0cb0c782b2037ff3ec74；
- accurate profile helper git blob f1b4f5fc69dd14c72fbbd02fd7e5347b0345657a。

执行时重算两个 blob 身份与 SHA-256。当前 helper 的 right-IBP 有效但不完备；所有阴性与代表秩都保留此范围。

## 2. 速度与加速度的精确拆分

设 $v=h_s,w=k_s$。R56 的场与导数结构使 $\mathcal C_s$ 对反转为奇，最多含二阶几何导数，允许的几何微分权重为 1 或 3。入口准确检查这一结构；不满足时作为实现检查失败报告，不删除异常项。

写加速度部分为

$$
B_{hh}v h_{ss}+B_{kh}w h_{ss}
+B_{hk}v k_{ss}+B_{kk}w k_{ss}.
$$

系数是依赖 $h,k,\omega$ 的完整三次 profile 算子。取

$$
P_{\rm acc}
=\frac12B_{hh}v^2+\frac12B_{kk}w^2
+\frac12(B_{kh}+B_{hk})vw,\qquad
\mathcal A=\frac12(B_{kh}-B_{hk}).
$$

真正沿几何求导、含 $\omega_s=k_s/(2h)$，得到

$$
\mathcal C_s
=D_sP_{\rm acc}
+\mathcal A(w h_{ss}-v k_{ss})
+\mathcal V_3(v,w)+L_hv+L_kw.
\tag{1}
$$

$\mathcal V_3$ 为齐次三次速度多项式。这个等式由原始表达式准确重建核对。它不会把 $B_{kh}$ 与 $B_{hk}$ 擅自对称化；其差正是可能保留的速度面积项。

若要求 $\mathcal C_s=D_sP$ 对任意几何控制路径成立，且 $P$ 是当前几何及有限阶 jets 的局部函数，那么最高 jet 的自由度先迫使 $P$ 至多依赖 $v,w$；加速度系数又决定其速度梯度。因此 $\mathcal A=0$ 是必要条件。减去 $P_{\rm acc}$ 后，剩余速度势只能是静态几何函数，故 $\mathcal V_3=0$ 也是必要条件。这里只研究“是否自动化成局部端点势”，没有把非零项说成无法控制，也没有排除整体桥匹配。

## 3. 线性一形式与接触关系

先取以 $h=1$ 为锚的准确原函数

$$
P_h(h,k,\omega)=\int_1^hL_h(\eta,k,\omega)\,d\eta.
$$

Laurent 的 $h^{-1}$ 项准确产生 $\log h$，不作浮点近似。因而

$$
\mathcal C_s
=D_s(P_{\rm acc}+P_h)
+\mathcal A(w h_{ss}-v k_{ss})+\mathcal V_3(v,w)
+k_s\mathcal R,
\tag{2}
$$

$$
\mathcal R
=L_k-\left(\partial_k+\frac1{2h}\partial_\omega\right)P_h.
$$

(2) 是本次后续控制设计的完整有限表达。对于互反 bulk 的内部连接桥，两端 $h=1$ 且为常值 germs，$P_h$ 与 $P_{\rm acc}$ 的端值都零；所以本次抽出的势不会产生未记录端项。

若面积项和三次速度项都准确为零，剩余静态端点势存在的必要结构是

$$
\mathcal R=a(k,\omega)+\frac{b(k,\omega)}h,\qquad
\partial_\omega a=2\partial_k b.
\tag{3}
$$

原因是未确定的积分常数 $C(k,\omega)$ 必须满足 $C_k=a,C_\omega=2b$。入口计算

$$
\partial_h(h^2\partial_h\mathcal R),\quad
a=\mathcal R+h\partial_h\mathcal R,\quad
b=-h^2\partial_h\mathcal R,\quad
\partial_\omega a-2\partial_k b.
$$

若所有必要身份都在准确表达式中消去，程序积分重建 $C$，再从原始 $\mathcal C_s$ 验证完整势恒等式。不把某几个点的零值当成势存在。

若确得到势，还会准确代入互反端点 $(h,k,\omega)=(1,1,1)$ 与 $(1,-1,-1)$，报告其整个 profile 函数端值差。不同 scalar 端点的势值不会自动丢掉。

## 4. 非零算子的准确 witness

正规化后的表达式非空本身不保证函数非零。本入口另外提供一个固定、事先公开的准确检验集合：

$$
q(x)=
\begin{cases}
(x-1)^8(2-x)^8,&1\le x\le2,\\
0,&\text{其余},
\end{cases}
$$

共同右端 $r=3$；$x$ 取 $5/4,3/2,7/4$，$h$ 取 $1,2$，$k$ 取 $0,1$，$\omega$ 取 $1,2$。这些状态的 $x+\omega$ 均正。所有 polynomial、嵌套右原函数、几何 Laurent 值和最终结果均用 Fraction 精确计算。含 $\log h$ 时只在 $\log1=0$ 的准确状态评价，其余情况跳过，不伪造有理近似。

此 $q$ 为紧支撑 $C^7$，代码拒绝超过 6 阶的所需 jet。有限个 jet 与右 Volterra 积分组成的算子对相应有限 $C^j$ 范数连续；紧支撑光滑函数逼近因此把任一严格非零 witness 传到某个 $C^\infty$ 紧支撑 profile。这个论证只用于证明算子不恒零。

没有找到 witness 不能证明算子为零。witness 不参与 span 拟合。所有这些实际 profile 评价，仅在公开 Actions 的研究分支执行。

## 5. 可选的完整函数上界空间

--include-pure-upper-span 额外提取 (2) 右侧余项的有限 profile 算子系数。由于任一具体真实桥的几何积分只是这些系数的实数权重，整个局部第三响应必落入这个**有限形式上界空间**。它与 R71 的 28 个准确可达交换子一起，给一个明确的新完整函数测试目标。

对其中每个三次算子 $\tau$ 计算

$$
\mathcal H_A(\tau)=\frac{D\tau(q)[A(q,q)]-2A(q,\tau(q))}{8},
$$

并问它们是否准确覆盖互反纯 bulk 的 $\mathcal P[q]/16$。此测试完全使用函数表达式，不使用上节 witness 的点值。阳性须再次从原始目标与实际列表达式复核。

**形式局部列尚未逐个证明可达。** 即使产生阳性函数身份，仍须用同一真实桥的参数实现相应有限系数，支付 frame/scalar/矩阵条件，再处理其他 phase、$P_0$ 与第四 ruling。输出字段 local_density_columns_proved_reachable 恒为 false，避免把上界当可控空间。

## 6. 已完成的开发验证与执行命令

本地只运行了小型人工 toy：人为给定一个二次速度势，加入 $5q^3(w h_{ss}-v k_{ss})$、$7q^3v^3$，准确恢复各项；另重建一个已知静态势，并核对一个 polynomial 右原函数身份。未在本地调用研究 compiler、评价实际 $\mathcal C_s$ 或运行任何几何/profile 搜索。

开发回执：

[literature-local-third-bridge-decompose-development-toy-20261114.json](literature-local-third-bridge-decompose-development-toy-20261114.json)。

建议公开 lane 先执行：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_local_third_bridge_decompose.py --toy-only --out output/local-third-toy.json
~~~

再执行真正目标：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_local_third_bridge_decompose.py --include-pure-upper-span --out output/local-third-decomposition.json
~~~

默认研究预算：240 秒、60 万 coefficient nodes、8 万 profile atoms、每表达式 10 万项、30 万 right-IBP 调用、Linux RSS 2 GiB 软轮询阈值、有理 span 消元 8192 bit。实际分支同时检查 GITHUB_ACTIONS 与公开仓库名。summary 硬限 95 KB；预算或实现失败保留阶段 JSON，分别 exit 2/1，不伪装数学阴性。

没有改变任何已冻 producer，没有重新积分旧失败 profile，也没有把旧长圈算子实验提升为主课题的厚度候选。


## 7. 公开开发实际通过

run43629844644/source6eceaa90的higher_range_development已成功，六项人工势/速度/原函数检查全true，未调用研究compiler。该run整体失败来自另一个height loader；本lane通过。现在请求local_third_exact，含真正局部密度、准确profile witness及纯响应形式上界检查，未宣称形式列可达。
