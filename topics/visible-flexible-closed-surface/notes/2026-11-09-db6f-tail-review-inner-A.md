# 内有限尾 A 临界值算法的独立审查

2026-11-09，审查者 `/root/tail_theory`。被审算法和数学推导由 `/root/independent_geometry` 新编写；审查者没有参与该实现。审查结论：**PASS，适用范围仅为所绑定精确有限背景的 cells 1–159 的 A 积分**。

## 1. 绑定和复跑

被审脚本为 `scripts/db6f-audit-inner-warp-variation.py`，SHA256 `aaa0c5da752d955a786c9ef8b563c218f5ad5988cdc35886435a5768744808ab`。正文为 `notes/2026-11-09-db6f-audit-inner-variation-and-elementary.md` §§1–3；§4 是对审查者所写初等组件的独立审查，本报告不把它重新包装为自己独审自己。

正式 checkpoint SHA256 `d23b03e4ce5cd7aaf4ac9d1134f8a23ee274be3a1d0a0192a7b294f1195e43f0`，有限 source 二进常数表 SHA256 `bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4`。沿用已经独审的初等组件 `88400506e7b660c328e03cb6547fe9056d2cde00963ebb16890d054169805145` 和基础区间后端 `e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d`。

独立执行：

```sh
python scripts/db6f-audit-inner-warp-variation.py \
  --checkpoint notes/2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine_tail_0017.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --out notes/2026-11-09-db6f-tail-review-inner-A-replay.json \
  --tail-start 40
```

重新读取两份 JSON 后做全对象相等比较，作者输出与本次独立复跑全部字段相同。包含正的剩余项后，认证结果为

$$A_{inner}\in[0.0706548168707253,\ 0.07065481687073313].$$

## 2. 数学与实现核查

对每个恒 cap 的 profile，raw log slope 的确化为 $C+\Delta S(x)-\lambda x$，其中 $\lambda=7\ell/\sqrt{12}>0$。$S'(x)=30x^2(1-x)^2$ 的最大值是 $15/8$，所以代码的零根与双根判定是穷尽的；不能严格确定根数时直接报错。双根公式先求 $u=\sqrt{\lambda/(30\Delta)}$，再取 $2u/(1+\sqrt{1-4u})$，与解 $x(1-x)=u$ 完全等价。

smooth cap 是 raw log 的非降函数，$f(w)=w/\sqrt{1+w^2}$ 也严格递增。故在相邻解析临界节点之间，$f(w)$ 单调，其全变差就是相邻函数值差的绝对值。代码的区间绝对值可以使下界变小、上界变大，保持包含性。若一个单调段的两个端点均落在完全饱和 cap 分支，整段是同一个精确二进 cap，直接记零没有遗漏中间振荡。有限求和只含 cells 1–39，其余并未按此式当作精确积分。

source 半径、长度、谷控制、pulse level、冻结 calibration 和 raw log 归一化逐项对应：奇数 n 的 $2^{-3n/2}$ 用精确二进幂除以 $\sqrt2$，两种指数写法一致；平台校准是固定二进几何参数，不冒充任何精确标定方程的根。

对 cells 40–159，已审正性证明给 $\operatorname{TV}f(w)\le5\cdot1280\,2^{-7n/4}$。除以曲率预算 6，并用 $2^{-7/4}<1/3$ 求几何级数，上界严格小于 $1600/2^{70}$。由于 $0\le\chi\le1$，这也包围 cell 159 保护端的 curvature-width 项。该端额外旧径向积分不超过

$$\frac{4}{75}\eta_{159}<\frac{1}{48000\,2^{238}},$$

由旧半径小于 $4/25$、$\sqrt{12}>3$ 和 $\delta_0c_0\le1/2560$ 推出。两项都作为正有理余量仅加到总上界，下界保留精算部分，方向正确。

所有参数盒及常数表覆盖/hex 检查均有执行；使用不同有限 source 控制时不能静默复用此结论。

## 3. 范围

本审查不认证 cell 0、B、紧全局径向归一化参数、非线性尾存在性、有限尾 metric/曲率或完整闭曲面。初等组件由算法作者独立审查，本报告只采用该已审组件；全局量应在另一个有明确余项和输入绑定的账本中组合。
