# 同一固定高度函数的查询无关原函数评价

日期：2026-11-14。状态：独立新 evaluator 和只读 Actions 审计；不改原物理函数、不优化、不修改已发表源码或原实际输出。

## 1. 修正的实际问题

公开 run 43618467921 的同一冻结状态，在原四点 chart `[0,tc,tf,L]` 得到帽高 `.007381758284337014`，而原 121 点 fine chart 得到 `.05223073558757131`。这是同一准确 $b_0$ 积分采用不同长区间 Gauss 分割的评价差，不是两种合法的独立高度选择。

旧 fine chart 的径向 Gauss 8→12 差很小，只说明那个细分割的两种规则接近，不能支付四点 chart 跨整个主体长区间的积分误差。旧端口比较又使用各自 chart 得到的共同 h，因而会抵消累计常数误差；端口局部二jet接合好，并不保证该 h 的数值已正确。

## 2. 数学函数不变，评价分割固定

仍定义

$$
z(t)=z(0)+\int_0^t b_0(r)\,dr+\sum_jg_jI_j(t),
\qquad I_j(t)=\int_0^t C_j(r)\,dr.
$$

其中 $b_0$ 是原固定 c0 自然场的准确完整角平均；当前 u/v/height/body 参数均不改变它。九个 $I_j$ 原本已经由同一个 B 样条原函数给出，并不依赖查询径向网格，本次不改这些函数或它们的评价。

新增固定分割取以下**准确有理点的并集**：

- $jL/120$ 的均匀细分；
- core、三个参考分段及 flat buffer 的端点；
- 固定 c0 的完整径向样条 knots；
- 已发表入口 Cauchy cutoff 的末端；
- 自然帽 patch 的起点、plateau 分界及活动尾端。

先对这些固定整 panel 求积并累加一次。对任意查询 t，只取其所在固定 panel 左端的同一 prefix，再加该左端至 t 的局部 Gauss 积分。查询中加入、删去或重排其他点，不改变整 panel 积分或当前 t 的规则。

默认 GL8；GL12 保持同一个固定分割。另用 GL8 加密到 $jL/240$，单独核固定分割精化。这两种比较不能混合为一次不知来源的差。

## 3. 物理身份与参数导数

`FixedPrimitiveProblem` 包裹原 `IndependentHeightProblem`。它保持原完整 physical identity、准确系数、固定 g、核心、帽和固定高度来源，仅更新 evaluation definition。

它重新计算共同中心后，直接按 $X_z=a(\Pi T)_z+z$ 写位置，避免 `oldX + (newZ−oldZ)` 的舍入抵消。$X_s,X_\theta$ 及全部其他位置导数保持原表达式。有限求积只是同一准确函数的近似评价，不是把新的分片数值原函数定义成物理 C2 曲面。

本次**所有当前参数 Jacobian 可以保持**，原因限于这一具体修正：被替换的 $\int b_0$ 不依赖任何当前参数，九个 $g_jI_j$ 及其共同原函数完全未改。特别是 `jac_X` 的高度列仍为 $I_je_z$。这条结论不能推广到下一步入口修复：若把高度自由基改为 $W_4C_j$，则它的原函数和 `jac_X` 必须同步更换。

## 4. 严格冻结状态 loader 与只读流程

新 `frame_fixed_height_primitive_audit.py` 先核：

1. 原已发表 18 件求解源码 SHA；
2. 原 enriched c0 的字节 SHA、原 loader 全部身份和完整有理系数；
3. 公开初态的整个 `state_record`；
4. selected 的每个 binary64 系数与其准确有理数、布局、完整模型、metric 及 evaluation；
5. 冻结 g 后的完整 physical identity 与公开 final metric 定义。

然后输出原四点、原 dense、新四点、新 dense 四组审计。另在新固定原函数下对 dense 并入真实端口，比较共同点全部位置二jet。GL8→12 与固定分割 120→240 最后分别执行，全程不换任何系数或 g。

每个阶段原子保存，任何后续失败保留已经得到的旧/新证据。脚本没有优化器，也不会应用线性方向或重选初值。

## 5. 同时报告的高度条件

本轮只读诊断加入：

- 全采样 `side*Xz−w` 最小值。要求其非负是本构造便于镜合的一项选择，不声称这是所有嵌入的普遍必要条件。
- 镜合两只 held 平盘同位置点的法弦半径为 $|h|$，所以完整闭面 reach 不可能超过这个准确 h 的绝对值。
- 当 $0\le B-\tau\le r_c$ 时，核心点 $(0,B,w)$ 的内向半径 $\tau$ 法球中心 $(0,B-\tau,w)$ 位于 held 盘的水平投影。若 upper cap 在核心上方，必要条件为 $h\ge w+\tau$。

默认设计目标 $\tau=61/1000$。此处报告的 h 仍是有限求积值，尚无连续误差区间，所以只列数值 margin，不据一个浮点数宣布严格 reach 排除，更不从这些必要门推出全闭面 reach。

## 6. 人工开发验证

仅使用人工温和椭圆和显式可积分的标量函数。

- 固定 primitive 稀疏/密查询及反向查询差为 0；显式积分误差 $4.45\times10^{-16}$ 以内，导数差约 $1.29\times10^{-10}$。
- 完整 wrapper 对稀疏/密共同点的六个位置 jets 差为 0；非位置导数及原参数 Jacobian 均保持 0 差。
- 直接 metric/shape 方向 Jacobian 相对差约 $4.56\times10^{-9}$；同 g 冻结后的六个位置 jets 回放差 0。
- 新 auditor 的**同一个实际主流程**已经用人工 carrier/selected report 跑通，包含严格 loader、四组 chart、共同端口、两种独立精化及 JSON roundtrip；篡改准确高度系数被拒绝。

人工旧稀疏/密 h 差约 $-0.004174$，新差 0，说明测试确实覆盖了原问题而非只碰巧选择同一分割。以上只是接口和评价一致性检查，不是研究候选几何检查或连续积分证书。

## 7. 公开 Actions 命令

```bash
python topics/visible-flex-new-mechanism/scripts/frame_fixed_height_primitive_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --uniform-panels 120 --primitive-order 8 \
  --refined-panels 240 --refined-order 12 \
  --radial-nodes 121 --angular-nodes 384 \
  --out "$RUNNER_TEMP/frame-fixed-height-primitive-audit.json"
```

真实调用只允许公开仓库自己的 Actions；本地只运行两个 `--check-only`。本次没有入口基场变更，也没有新 B 设计，便于把纯评价修正单独归档。后续入口成套修复应在这个共同高度接口之上另建新模型身份。
