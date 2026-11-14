# 振幅延拓中的 warm 选择器：静态观察

可信度：**已核源码行为；后续 predictor 仅候选**。coupled_prefix，2026-11-09。

当前原方程恢复由 root 运行。本记录不修改任何 worker、controller、配置或活动状态，不启动第二条数值路线。

## 当前实际行为

冻结 `scripts/db6f-prefix-tail-trial-worker.mjs` 的 SHA256 是 `6d53b430a956ba688122cafd11f6e4033f9716ea4d9f4989871f324ac900d837`。它复用成功 warm state 时，先取

$$
R=H_{1,\mathrm{new}}/H_{1,\mathrm{old}}.
$$

只有 `harmonicAmplitudePredictor === true` **并且新请求的所有高阶 cut heights 都精确等于零**，才把第 $j$ 个 Fourier 模式的 Q 和 momentum 均乘 $R^j$，这里 $j=1,\ldots,M$。否则所有模式先统一乘 $R$。之后原 `correctInitialBoundary` 机制给 cut-height 差加上精确的有限线性响应；原非线性方程最终重新判定成功。

当前 affine 目标的 14 个高阶 heights 均非零。因此，路径

$$
H_j(s)=s^jH_j(1)
$$

在成功点之间继续时，现有 worker 实际采用的是**统一倍率 warm 加线性边界修正**，并不会自动进入已有的 harmonic multiplier 分支。这不是方程错误，也不影响方程、guard、最终原 residual 或实际 DN 的定义。首个 $s=1/4$ 从线性初猜开始，当前中断后在同一 $s$ 恢复的倍率为 1；两者均不能用本观察解释阻尼。

## 可能的后续初猜，尚未实施

若以后有相邻已成功的 $s_0,s_1$，可在一个独立、显式绑定这条路径的初猜程序中，尝试把第 $j$ 模式的两类状态先乘 $(s_1/s_0)^j$，再执行原线性 cut-height 修正。必须保留原 physical-H 单位和原 momentum 的归一化；倍率只作用于相同模式的已保存未知量，不对 $r,w$ 或 metric 参数作改动。

这个候选来自有限模非线性问题的角向次数结构：在零解附近，若存在对复振幅解析且相位等变的局部分支，则第 $j$ 个谐波的最低次数是 $j$，更高项相差偶数次数。该条件下 modewise multiplier 保留最低阶行为，却不会精确搬运高阶非线性项。本文没有证明该局部分支覆盖当前 $s$ 范围，也没有比较两种初猜的实际 residual 或收敛成本。

即使以后采用这一候选，它也只改变搜索起点。每次成功仍须原真实 RK、moment root、正性 guard、归一化 residual 和容差核验；$s<1$ 仍只是 warm。不能把这个选择器观察归因为当前强阻尼、舍入问题或已找到修复，也不能在原活动代码上就地改变已冻结的行为。
