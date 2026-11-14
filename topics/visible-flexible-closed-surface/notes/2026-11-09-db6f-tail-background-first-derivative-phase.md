# 保留径向相关性的一阶 phase 界

状态：**条件引理完整证明；新脚本与完整 pilot 待独立复跑审查。** 本方法只改善同一背景的区间证书，不改变 primitive、精确 $\alpha$、物理网格、源状态或有限图。

作者：`/root/tail_theory`，2026-11-09。

## 1. 诊断：宽界来自后备算法

跨 cap 的 C4 pilot 在 raw0 的 `[4568,4572)` 上给出 90 个盒，其中 9 个未达 $10^{-9}$ 的 $w$ 工作宽度。这 9 盒的系数宽都很小，余项主要来自径向 phase。独立 M12 uniform 高度权重预算确认它们的宽度也确实超过当前 $2\cdot10^{-10}$ 的供应误差分配，因此需要改善这些盒。

`db6f-tail-background-residual-diagnostic.py` 进一步确认：9 盒全都触发了旧供应器的“近似反解跨过 64 个以上 primitive 叶时退回全盒单调界”，最多跨过 1,735 个叶。这种后备合法，但丢掉 source 半径与目标线性半径之间的相关性。已审 primitive 的单点半径包宽最多 $1.333\cdot10^{-15}$；五点数值 phase 的中心差最多 $2.941\cdot10^{-16}$。这些采样本身不是新证书，只用于识别粗界来源。

因此不应把旧约 $9.012\cdot10^{-9}$ 的 phase 上界解释为 primitive 或近似反解的真实误差下界。下面直接给一个不需要跨叶多项式逐个展开的严格界。

## 2. 端点与一阶导数引理

设 $R(x)$ 是某个固定 source profile 内的真实物理半径，$X(\tau)$ 是原已审构造的精确三次 Bezier 近似反解，$0\le\tau\le1$。它的控制点有序，因此

$$
X([0,1])\subset[x_0,x_1],\qquad X(0)=x_0,\quad X(1)=x_1.
$$

目标物理盒是 $[r_l,r_r]$，其长度 $\Delta r=r_r-r_l>0$ 为精确有理数。定义

$$
\rho(\tau)=R(X(\tau))-r_l-\tau\Delta r.
$$

若两个端点误差均不超过 $E$，且整个区间上 $|\rho'|\le M$，则

$$
\sup_{0\le\tau\le1}|\rho(\tau)|\le E+\frac M2.
\tag{1}
$$

**证明。** 对任意 $\tau$，从 $e=0,1$ 中选择距离最近的端点，故 $|\tau-e|\le1/2$。沿连接区间积分导数，得到

$$
|\rho(\tau)|\le|\rho(e)|+\left|\int_e^\tau\rho'(s)\,ds\right|
\le E+M/2.
$$

连续且分片 $C^1$ 时逐片积分给出同一结论。证毕。

## 3. 两个量的严格供应

原 primitive 已严格供应 $R(x_0)$ 和 $R(x_1)$ 的区间。因此令

$$
E=\max\left(\|[R(x_0)]-r_l\|_\infty,
             \|[R(x_1)]-r_r\|_\infty\right)
$$

就是两个真实端点误差的上界。这里使用的是 Bezier 定义上的精确端点，不能用另一个近似点替代。

在同一个精确 $\alpha$ 与冻结 source 定义下，

$$
R'(x)=A(x)+\alpha B(x).
$$

已审 order-0 source 评估给整个 $[x_0,x_1]$ 上的 $A,B$ 范围；它们的值域 hull 在 cap/绝对值分支界面仍合法，完全不要求 `validA` 或 `validB` 的高阶解析标志。特别是 $A$ 中的 $|w_x|$ 连续，因而真实 $R$ 至少 $C^1$。本方法不对 $A$ 求高阶导数。

把精确 Bezier 多项式的系数区间逐项微分，使用原已审 Bernstein 变换得到 $X'([0,1])$ 的包。链式法则给

$$
\rho'(\tau)=(A+\alpha B)(X(\tau))X'(\tau)-\Delta r.
$$

区间乘法与减法因此供应整个 $\rho'$ 的合法范围。对它取绝对值上端就是 $M$。$\Delta r$ 始终从精确物理节点与局部二进端点经 `Fraction` 算出，再用 `qbounds` 向外转换；不使用显示半径相减来定义长度。

最终用向外区间加法计算 (1)。把这个界与原有的 primitive 多项式/全盒单调界取最小值仍然合法，因为它们同时是同一个 $\sup|\rho|$ 的上界。其后的 $24\delta_r$ 背景斜率转移及全部多项式余项处理不变。

## 4. 冻结实现及 pilot

新脚本 `scripts/db6f-tail-background-packet-phase.py` 的 SHA256 为

```text
97b8cd525586851c1e726e101db0f586518d260898fcaa6842c363ca050bc807
```

它由已独审的 `db6f-tail-background-packet-c4.py` 派生，仅新增 `first_derivative_radial_residual`、将原 phase 上界与其取最小值、增加作用域/方法字段。cap C4、$w_r$ 逻辑、物理覆盖、hash 绑定与所有旧源文件均未改动。

对旧 9 盒的先行公式诊断给出：新 phase 上界最大 $1.725\cdot10^{-11}$，端点误差最大 $8.882\cdot10^{-16}$。它说明有充分余量，但正式输出仍以下述完整同参 pilot 及其独审为准。

```bash
python scripts/db6f-tail-background-packet-phase.py \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --primitive notes/2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --out-prefix notes/2026-11-09-db6f-tail-background-phase-pilot-raw0 \
  --span-start 4568 --span-stop 4572 \
  --w-width 1e-9 --wr-width 1e300 --radial-residual 1e-8 --max-depth 10
```

这个后备界独立于 primitive 叶数，避免为穿过许多很小的叶而丢掉相关性。它既不更改背景，也不构成源 ODE、完整 metric 残差或无限尾存在的证明；实际后端仍必须使用所有保存的系数区间及余项。
