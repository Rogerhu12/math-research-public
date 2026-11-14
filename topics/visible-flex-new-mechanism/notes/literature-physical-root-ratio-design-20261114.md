# 实际物理 C 根的负 W/C′ 可达性设计

日期：2026-11-14。状态：独立运行器及合成接口检查已经完成；本稿不声称研究优化已经运行。

## 1. 这次具体检验什么

[固定 q2 曲线的实际 Actions 审计](literature-physical-C-actions-43597247312-audit.md) 已发现两个数值物理简单根，但其 $W/C'$ 分别约为 $.79326$、$.84581$。因此物理域内 $C$ 可以变号，尚无证据证明根比值普遍非负，也没有现成的负比值几何种子。

通用局部 D=0 相位定理的一个充分条件是

$$C(\xi_*)=0,\quad C'(\xi_*)\ne0,\qquad
-9/4<W(\xi_*)/C'(\xi_*)<-5/4,$$

再加该定理显式 jet 中的非零量 $\mathcal K$。本运行器只检验实际闭曲线几何能否到达其中一个比值，例如默认 $R_*=-7/4$。它不会把全部八系数拟合成 R22 的特定抽象例。

**这不是两个四阶外尾的完整 profile 设计。** 新的 C4 恒相位结果已经排除了它所覆盖的简单四阶双外尾类；即使本次局部几何目标成功，也不会使那个被排除的完整类重新成立。仅 C3 的内部退化、不同外端正则性、全局总矩、有限等距路径及闭嵌入厚度，都仍是另行未解的问题。

## 2. 冻结的设计与残差

脚本：[literature_physical_root_ratio_design.py](../scripts/literature_physical_root_ratio_design.py)。本次冻结源 SHA-256：

`6fa9ce44bfe28cbafc1156c7c69227513fb6c5a480899b6b802dcfe27135f37f`

它复用已有 `literature_closed_codesign.geometry`：闭合指数 tilt 每个设计点由同一标量方程求解；参数仍为四个径向 Fourier 坐标、角参数及 log 速度的自由 Fourier 系数。研究计算仅允许在本公开仓库的 GitHub Actions 环境。

额外变量是一个显式实数 $\xi/\ell_\xi$。这使平滑残差中没有随几何移动的 `min(omega)` 或 `max(omega)`。初始物理根从已公开的固定初始参数的 $C$ 多项式中选择，正、负物理半线各作一个独立设计；每例的初始根、全部实根和参数来源均保留。

固定尺度为

$$\ell_\xi=\max\{1,\operatorname{ptp}\omega_0,|\xi_0|\},
\qquad d_* = |C_0'(\xi_0)|.$$

两项主残差为

$$\frac{C(\xi)}{d_*\ell_\xi},\qquad
\frac{W(\xi)-R_*C'(\xi)}{d_*}.$$

保留初始 $C'$ 的符号，并要求其有符号值至少为 $.1d_*$，避免用 $C'$ 一同消失来制造比值的假通过。这里的保护是设计条件，不是已证明存在精确非零根。

物理保护直接在固定角网格上检查

$$\operatorname{sign}(\text{side})\,(\xi+\omega)/\ell_\xi\ge .01.$$

同时保留 log 速度和球面方向曲线速度的采样下限保护。所有保护行都先对未截断的平滑观测作有绝对下限的中心列差分，再乘当前 hinge 分支导数；沿用已定位过的分块方法，避免跨阈值差分被误称为平滑 Jacobian 错误。

参数盒和 $\xi$ 盒在 JSON 中完整记录。这是一项改变基底的几何设计，不是固定度量的精化。

## 3. 最终验证不更换候选

每例结束时一次冻结：几何参数、$\xi$、tilt、速度归一化、全部尺度和导数符号。随后在 768、1536、3072 角点上只重新计算同一个候选。

验证报告包含：

- 固定 $\xi$ 上的 $C,C',C'',W,W'$、两个未换尺度的主残差，以及导数保护。
- 固定 $\xi$ 的全部采样分母及物理 $u=\sqrt v/(\xi+\omega)$ 范围。
- 实际多项式的全部数值实根及各根的比值，单独标为诊断；它们不会替换已经冻结的 $\xi$。
- R26 的指数、显式局部 jet 和 $\mathcal K$，仅作条件诊断。近似的 $C=0$ 和非零 $\mathcal K$ 不是精确存在证书。
- 实际闭合、完整周期系数、原有多项式恒等误差、有限网格正则性、独立方向导数误差及 hinge 分支切换次数。

全部连续物理域、精确根、完整 profile、有限等距族、reach 和总题完成标志仍为 false。

## 4. 完整复现命令

以下从公开仓库根目录运行；研究命令交公开 Actions，不能在本地伪造 Actions 环境执行。

```bash
python topics/visible-flex-new-mechanism/scripts/literature_physical_root_ratio_design.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43591099281-1-closed_design/nine-coefficients-closed-design.json \
  --q 2 \
  --parameter-state initial \
  --sides positive negative \
  --modes 12 \
  --theta-n 768 \
  --validation-n 768 1536 3072 \
  --guard-angles 192 \
  --max-nfev 180 \
  --target-ratio -1.75 \
  --derivative-floor 0.1 \
  --physical-gap 0.01 \
  --logh-bound 1.0 \
  --speed-floor 0.08 \
  --xi-bound 4.0 \
  --out "$OUT/physical-root-ratio-design.json"
```

`OUT` 是工作流已经设定的本 lane 输出目录；脚本会每完成一例保存完整 JSON，并另写带“未完成”标签的中途最佳点检查记录。中途记录不等于求解成功。

## 5. 已实际执行的轻量检查

[合成检查 JSON](literature-physical-root-ratio-synthetic-20261114.json) 记录源哈希、执行命令和 UTC 时间。唯一执行命令为：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_physical_root_ratio_design.py --developer-check
```

它使用 R22 的有理系数对应的二进制浮点合成多项式，检查 C/W 重建、局部 jet、$\rho=9/2$、正物理半线分类及完整 hinge 行索引/导数。局部 jet 最大误差为 $1.39\cdot10^{-17}$，其余布尔检查通过。

这个检查没有调用任何真实几何、闭合优化或研究 ODE，也没有证实负根比值可达。实际 Actions 返回后应独立审计两个主残差、非零导数、冻结精化和全部物理保护，再决定是否存在值得严格验证的局部种子。

独立只读复核：repo_sources核对C/W的11系数索引、闭合几何导数、平滑列差分后施当前hinge、Cp有符号尺度保护、负侧物理u分支及冻结xi/tilt/normalization。root另逐段读审运行器与实际输入范围；没有进行本地研究求解。
