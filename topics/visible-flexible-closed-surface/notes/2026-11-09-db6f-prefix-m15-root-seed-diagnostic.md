# M15 保存端点的角向 root 初猜检查

状态：**只读浮点诊断，不是区间证明，也不含被拒 trial 或未保存 RK 内点。** 作者 `/root/coupled_prefix`，2026-11-09。

输入 `2026-11-09-db6f-prefix-m15-root-margin-input.json.gz` 是 M15 iteration 7 的逐字节副本（SHA256 `bd7ebfeab571198b50c909f5d614490de36ffd007846fcf754fd569284cda11c`），保持 UNCONVERGED 标记。选取全部 raw0 shooting 端点及若干深层端点，共 188 次角向方程求解。使用原 N256 角规则和 `projectionFloor=.05`，不改物理参数或 moment 目标。

默认 $L=\mathrm{target}$ 初猜的最小 $A$ 为 $0.30489119300379486$，解后的最小 $A$ 为 $0.09228309622876305$，188 个原 root 均成功。最小值在 raw0/segment4、raw $x=.25$ 的相邻子段共享端点附近。**这些保存端点不支持“默认初猜已靠近 .05 guard”作为现有失败解释。** 失败 trial 或 RK 内点仍可能表现不同，不能由这组端点排除。

另作独立候选初猜

$$
L_0=-w^2P_\theta,
$$

在实数模型中使 $A=1$，同时 $D=ES-w^2(1-EP_\theta)^2$。按原浮点模型逐点求值时，188 个端点的该初猜均过原 $D,S,A$ guard，最小初始 $D=0.9851573184651169$；从它求同一原 moment 目标也全部成功。两种初猜所得 root 系数最大差 $6.689093723366568\cdot10^{-14}$，与已审 R20 的条件唯一性相容。

这只是该候选初猜在当前保存端点上可行，未将它装入现有求解器，也不证明它能解除 M15 全 shooting 的线搜索失败。没有因本诊断降低 guard。

数据与脚本：`2026-11-09-db6f-prefix-m15-root-initial-margin.json`、`...-v2.json`；`scripts/db6f-prefix-tail-root-initial-margin.mjs`、`...-v2.mjs`。各 JSON 绑定输入、配置、脚本和原 root 源 SHA256。完整重跑参数如下（在仓库根目录，输出使用新文件名）：

```bash
node topics/visible-flexible-closed-surface/scripts/db6f-prefix-tail-root-initial-margin-v2.mjs \
  --source-root topics/visible-flexible-closed-surface/repro/source-root \
  --checkpoint topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-m15-root-margin-input.json.gz \
  --config topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from14-tail-config.json \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-m15-root-initial-margin-v2-replay.json
```

将脚本名的 `-v2` 去掉可重跑仅含默认初猜的一版；它需要另一个全新 `--out` 路径。两版数据均已由实际脚本运行得到，工具 exit 0。
