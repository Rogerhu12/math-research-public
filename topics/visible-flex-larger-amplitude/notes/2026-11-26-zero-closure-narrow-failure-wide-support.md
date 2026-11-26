# 真实零闭合首根失败后的宽支撑输入

## 实际失败边界

[公开运行 45820592817/1，part 001](2026-11-26-public-actions-45820592817-1-part-001.md) stage 5 执行完整 `27414140…` launcher / `b4d71ade…` driver，真实 11.00651035199985 秒后 exit 1。报告为 `00a00590f7b38a3067220d9addfeba7ea2ef8bcc8343d3b9806a20a9e0b2a6a5`（81746 bytes）。

真实输入是同 run 的独立参考 bundle `0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1`，固定 scalar 身份 `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb`。实际命令没有 `--seed-so3-checkpoint` 或 `--restart-checkpoint`，所以没有使用先前 hDelta 优化末父。

失败发生在首批 8 个角度的真实端点根求解；失败索引为 0、1、7，原因是 “No actual endpoint-root backtrack decreased the same complete equation”。该失败记录中的最大 residual 为 0.37016474660679566，最大 correction 为 0.07228725875791846。它们是实际失败过程的工作值，**不是**真实初始 $\Delta=C(0)$ 的区间下界，也不是根不存在的证书。报告没有新 initial/final 场，J/J* 调用计数均为 0；已完成角根计数为 0 不应被误解为没有尝试 Newton/backtrack。

原 root tolerance $2\cdot10^{-12}$、最多 24 次 Newton、18 次 backtrack、Armijo $10^{-4}$、endpoint-coordinate ball 半径 $.5$ 都如实保留。原报告明确不宣称 uniform IFT 失败或全局不存在。

## 支撑长度的解析约束

固定一个角度和原全变量向量，令未纠正的单位 meridian 为 $T_y(s)$，两段 bubble 的支撑并集为 $U$。在 $U$ 外 $W=0$，故旋转纠正完全为恒等。对任意参数 $z$，正交旋转保持单位长度，因此

$$
\begin{aligned}
C(z)-C(0)
&=\int_U\bigl(\exp([W(s)z]_\times)T_y(s)-T_y(s)\bigr)\,ds,\\
|C(z)-C(0)|
&\le \int_U\bigl(|\exp([Wz]_\times)T_y|+|T_y|\bigr)\,ds
=2|U|.
\end{aligned}
$$

这个界不需要小角、rank、IFT 常数，也不依赖 endpoint-coordinate ball 的半径。若另有同场严格输入证明 $|C(0)|>2|U|$，则仅用这些固定支撑上的旋转参数 $z$ 无法闭合；当前实际失败 residual 本身没有提供这个前提，本文不据此判定当前场不可闭合。

首试两段支撑分别为 $[S/64,3S/64]$ 与 $[61S/64,63S/64]$。每段长 $S/32$，故总支撑长 $S/16$，上式给出最多 $S/8$ 的端点积分改变量。该有限容量为扩大实际支撑提供具体依据；它与增加 Newton 次数或放宽根误差是不同的输入选择。

## 新输入与模板合法性

下一条完整入口只将两个精确相对三元组改为

$$
(1/32,\ 1/4,\ 15/32),\qquad
(17/32,\ 3/4,\ 31/32).
$$

每组仍严格满足 $0<a<c<b<1$，第一组右端严格小于第二组左端。两组关于 $s/S=1/2$ 互为镜像，且均与 core/cap 留有正距离，满足原 `5b4c3921…` constructor 的原有条件。原数学模板仍是 $S_5(u)=10u^3-15u^4+6u^5$ 上升、$1-S_5(u)$ 下降，在支撑外为零。因 $S_5$ 两端的一、二阶导数均为零，扩大支撑不改变其 $C^2$ 拼接和端部零 jets。

新每段长度为 $7S/16$，总长 $7S/8$；相应容量上界为 $7S/4$。这只是上界，不能反推 rank、局部收缩、根可解或几何可行。

原公式自动由新 bubble 计算数学质量 $m_i=(b_i-a_i)S/2$。本次两质量从 $S/64$ 改为 $7S/32$，各增加 14 倍；同一固定材料图下，原公式给出的 $Q_i$ 矩阵相应缩放为原来的 $1/14$。这一变化属于已声明 bubble 输入及其原有定义，不是替换 Newton 或隐式 J/J* 算法。实际工作值仍是原浮点实现，未付的积分、root 与舍入费用不会因此消失。

原 canonical zero 模型包含完整精确 bubble 三元组，因此这次是同一固定 $g$、同一原变量种子上的**新明确表示身份**。未来 model hash 必须由真实运行返回；不会预填旧 `7b399eab…` 身份，也不会把旧失败目录冒作新初场。

## 完整执行责任

`resume-20261126-zero-closure-wide-support-steps.json` 提供完整 solver 与纯 reader 两步。除了六个 bubble 参数和 fresh outdir/step id，已逐字符串核对全部科学 argv 与已实际运行的首试一致。五个科学/读取源均逐字核为原身份：

- endpoint：`5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46`；
- geometry：`7698fd89e1b739391e2139c6c88dacd0c3b3d8be614fd65e435508420326b385`；
- driver：`b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b`；
- launcher：`27414140270a0fb1a9533a21a0bd28a46988c55aecd9952c38e7c05512b64166`；
- reader：`b25e5a5f370e69fe8164d835a608b1845db926d2488939dc9bafaa3bba0a6857`。

全部原 free core、omega、H、数值三条 Gram 残差、完整隐式 J/J*、原 192 C 行、幅度行、全网格/永久位置双符号真筛均保留；root ball/tolerance/预算、几何阈值和优化预算均未放宽。新初场必须实际完整读取，若根再次失败仍诚实输出 incomplete 并继续据实际原因选下一输入。

纯 reader 仍绑定已存在的 reference bundle，因而可如实读取新的 initial root failure；verify-final 仍只在完整报告分支执行。新增六个 bubble summary 均为字符串叶子，其他 scalar-only summary 保持。没有在本地执行科学计算；本项只完成参数准备、原源码身份与 argv 差异核对，以及上述解析界。
