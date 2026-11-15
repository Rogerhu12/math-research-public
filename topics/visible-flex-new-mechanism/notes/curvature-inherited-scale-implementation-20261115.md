# 从实际SOC成功继承主步尺度：16输入单 consumer

## 1. 只改变有实际依据的一项选择

公开 run43660745541 已在相同 $g$、固定 $b_0$ 和163个物理参数下，以 SOC 修正取得双网合格物理态

`b03c522ade58ec0c7a5a4bfb3af971a430adabf080cf0d8cdeabab4c0c3b4cb5`，

两网最大主曲率为 $59.71130117996687$，目标60完成。实际说明见 `notes/curvature-soc-first-actual-result-20261115.md`。

成功的模型5原步按参数盒宽归一的无穷范数为

$$
\nu_{\rm success}=0.0010787808045532301,
$$

最大坐标步为 $.017260492873$。切换目标55后，原 LP 解的归一尺度触到 $.01$ 上界，最大坐标步变为 $.16$、$\ell^2$ 约1.33；连续发现遗漏行，因此消耗剩余 LP 而尚未进入 SOC。

**旧控制器并没有在目标切换时重置 trust 的程序错误。** 它一直保留 $.01$ 上界，只是目标60的自然最优步远小于这个上界，目标55的自然最优步则顶到了它。本次新选择是把新运行的初始上界明确收紧到已成功步的量级：

$$
\rho_{\rm initial}=\frac1{1000}.
\tag{1}
$$

它略小于 $\nu_{\rm success}$，不是根据新候选几何再拟合的参数。后续缩步和阶段切换继续调用原冻结 SOC 控制器；阶段切换不会把较小上界改回 $.01$。

## 2. 保持不变的对象

唯一新源为 `scripts/frame_curvature_inherited_scale_audit.py`。已有 `frame_curvature_soc_steps.py`、其 controller 及全部几何源码均不修改。

完整 $g$ 仍为

`fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。

新 consumer 保留原163系数身份、固定 $b_0$、原共同高度原函数、GH/角均值/求积规则、所有参数盒与硬门。SOC 的一半实际原步半径、物理四分之一线性裕量、至少一半预测曲率 slack 改善、最多每原模型一次修正都不变。

仍共用12次原/SOC LP、40次粗细完整值、120秒活动时间。初始化与输入准备单列；最后只对同一保存态作原384/768两网独立审计。不存在旧优化器重放、额外重优化或新的物理变量。

已完成的60留作历史；本次目标序列从55开始：

$$
55,50,45,40,35,30,25,20,16.
$$

仅实际双网达到当前目标后前进。实际曲率下降但尚未达到55的合格态仍可保存，不能把它写成目标成功。

## 3. 尺度的来源绑定

16输入严格读取第16份完整报告的全部已保存状态与行池。新增输入为

`notes/actions-43660745541-1-curvature_soc_steps/curvature-soc-steps-audit.json.gz`，

解压后的 SHA256 为

`83d11b3bb645d1cc671653eeb4642187d8ccab9e881f2deadd443955dca4f426`。

实算入口要求该报告 source 为 `3fd3bbe8b281cd729b047984bbe46645507b0b0d`、run为43660745541，保存态为 `b03c…`，两网最终门通过，且它确来自接纳的 SOC 模型。原十五输入的各字节身份、源码、初始状态、物理族、$g$ 和原始网格继续严格回放。

设模型5保存的主 LP 系数为 $p$，保存的回溯因子为 $\alpha$，原参数盒宽为 $D_j$。consumer 仅由这些已发表数值重建

$$
\nu=\max_j\frac{|\alpha p_j|}{D_j},
$$

核对它与原 SOC LP 记录的主步范数一致，并保存其精确 binary64 有理数、完整主步向量的 hash、以及 $(1/1000)/\nu$ 的准确有理比。该过程不评价几何。它还检查 $1/1000<\nu$，因此“继承成功量级”是可追溯记录，不是一句没有来源的说明。

初态完整系数不因这个尺度选择改变。初态来源标签由小 subclass 改为保存的 `b03c` 成功态，避免沿用旧 controller 的 `d1ca` 起点文字；此修改不改变接受规则或物理场。

## 4. 全部行池继续保留

原报告最终粗池4198行、细池1118行完整继承，包括目标55那些失败大步发现的行。逐行平面索引、组顺序、径向/角向坐标、hash和容量均检查；还检查此前十五输入的池是新池的子集。

新的小步上界不作为删除旧行的理由。若仍发现遗漏行，继续使用原规则：保存它们、返回最后双网合格点、补池重建。不是在未查细网的点上做修正，也不把池内可行当完整网格可行。

最后合格点 cache 的复用继续受精确状态和池版本限制。新的尺度是求解配置/evaluation metadata，不进入物理 $g$ 或系数身份；旧 SOC 报告及全部失败试探保留。

## 5. 实现与必要人工检查

新 consumer 不复制求解 controller，只调用冻结的 `run_soc_steps`。独立 driver 负责第16输入回放、目标/尺度 metadata、原生摘要、异常保存和最终同态审计。

本地人工检查包括：

- 一个确实受 trust 约束的纯数组 LP：旧 $.01$ 产生归一步 $.01$，新 $1/1000$ 产生归一步 $.001$，最大坐标从 $.16$ 变为 $.016$。
- 从保存的人工 binary64 主步准确重建成功范数及比值；篡改该范数被拒绝。
- 人工16输入完整 IO、初态来源、同物理系数/$g$/$b_0$冻结、全部旧池继承、原两网末审计。
- 第16份错误 SHA、错误完整系数、错误原细网坐标均拒绝并保存失败摘要。
- 目标改变不重置尺度、也不额外评价几何。
- summary 与完整报告字节绑定；继续保留既有 SOC 的模型、修正、试探、接纳和事件表。

没有本地真实候选几何评价。原 SOC 的曲边界/预算/缓存人工检查不再机械重复；新回执仅覆盖新 consumer 和新尺度选择。

## 6. 部署接口

人工入口：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_curvature_inherited_scale_audit.py \
  --check-only --out "$RUNNER_TEMP/curvature-inherited-scale-development.json"
```

真实入口沿用原15组路径/SHA参数，再加入：

```bash
--soc-audit topics/visible-flex-new-mechanism/notes/actions-43660745541-1-curvature_soc_steps/curvature-soc-steps-audit.json.gz
--expected-soc-sha256 83d11b3bb645d1cc671653eeb4642187d8ccab9e881f2deadd443955dca4f426
--out "$RUNNER_TEMP/curvature-inherited-scale-audit.json"
```

只有公开 Actions 和正确 repository 能走真实入口。原生 summary 仍使用 `mixed_grid_short_step_stage`，同时保留 `correction_table` 和新的 `primary_scale_inheritance`；无需通用 brief 重写。

## 7. 结果解释范围

新半径可能减少每步预测收益，也可能减少大步引发的二阶度量违反和遗漏行循环；哪一种占主导，须由新的公开实际判定。它不证明目标55可达，不改变原 $\eta\le167/625$ 的近等距范围，也不把任何采样曲率或镜像条件当成完整 reach。所有候选仍须原两网真实物理门及实际曲率下降，才可成为下一步初态。
