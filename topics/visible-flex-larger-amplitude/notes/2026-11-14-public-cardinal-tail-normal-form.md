# 原始四角节点小包：精确 C² Hermite 非平面性接口

2026-11-14，geometry，AI 辅助研究。**状态：原始数据字节已保全；几何检查器已写，实际有理几何计算交给公开仓库 Actions。** 本接口不重新求解 ODE、非线性 DN 或 RK48 全读出，也不把精确规范化的场偷偷当作旧渲染器每一步舍入所得的字面二进制系数字段。

## 1. 仍然存在的完整源与保全部分

旧工作目录仍保有以下完成读出及全部节点：

- RK24，radial 8：`/workspace/scratch/ffc1334c1988/exact-work/closed-local-r1/A-RK24-resolved-r2/readout/complete-8.json`，4609 个节点。
- RK48，radial 16 加真实 source-cusp 节点：`/workspace/scratch/ffc1334c1988/exact-work/closed-local-r1/A-RK48-cusp-resolved-r4/cusp48-sixteen/complete.json`，9245 个节点。其中 9217 个常规节点仍在相邻 `regular48/nodes/`，另有 28 个实际 source-cusp 节点。

这次选择后一份。它的完整 manifest SHA256 为 `2f27e53cc6880cade99ebd52eb137d1d3fd6e901c4faa2e04c2571f3ad73f118`，并与同一旧 RK48 闭 plan 的输入哈希相符。不要因它与新公开重算的 manifest 路径、来源记录不同，就把二者的整文件哈希混用。

纯字节提取器 `computations/geometry_20261114_cardinal_tail_packet.py` 逐个检查原压缩和解压 SHA256，只复制每个原 512×12 节点数组中角索引 $0,128,256,384$ 的四行，未作 FFT、有限差分、ODE 或新的非平面性判断。数据保存在 `notes/2026-11-14-public-RK48-cardinal-tail-packet/`：

| 文件 | 字节数 | 内容 |
|---|---:|---|
| `cardinal-node-rows.f64le.gz` | 2446961 | 9245×4×12 原始 binary64 数据的原字节 |
| `source-node-index.json.gz` | 1294672 | 每原节点的压缩/原始/四角字节哈希及精确二进半径 |
| `manifest.json` | 见文件 | 旧 complete、plan、profile、输入哈希和精确端点参数 |

全部原始 9245 个节点均通过字节校验。每文件均小于 5MB。旧目录保持只读。

## 2. 四角足够做非平面性判断，但不自动定义整个曲面

对每个半径令四角为 $\theta_j=j\pi/2$，保存差向量

$$D_j(r)=F(r,\theta_j)-F(r,0),\qquad j=1,2,3.$$

所有角均值以及任意共同的背景高度原函数都在这个差中准确消掉。如果一个关于角度实解析的曲面在某个径向开区间和角向开区间中位于一个平面，其平面方程按角向恒等定理延拓至完整纬圈，因而

$$P(r)=\det(D_1(r),D_2(r),D_3(r))=0$$

在该径向开区间成立。若每个径向片段上的 $D_j$ 是至多五次多项式，则 $P$ 至多十五次；一个确切非零的有理评价便排除整个片段内任何平面开片。

因此只保存四角足够提供这个特定证明的全部输入。它不等于删除其他角模态或用四角近似完整物理场；结论适用于所有与四条已给轨迹一致、且关于角度实解析的完整场。

## 3. 精确共享节点 Hermite 规范化

`computations/geometry_20261114_cardinal_tail_exact_check.py` 在 Actions 中将原始 binary64 节点字节视为精确二进有理数。位置及一阶径向导数取原四行差；高度二阶导数取原第9列的四角差。共同的 $w,w_r$ 正好在差中消掉。水平二阶导数仍按原 `RefinedTail.node_coefficients` 的相邻径向速度有限差分规则定义，但把半径差及权重运算改为精确有理算术。

每个节点只产生一份共享的二 jet。对两端数据 $(y_0,v_0,w_0)$、$(y_1,v_1,w_1)$，设 $h=r_1-r_0$、$t=(r-r_0)/h$，精确五次 Hermite 系数由

$$\begin{gathered}
c_0=y_0,\quad c_1=hv_0,\quad c_2=h^2w_0/2,\\
A=y_1-c_0-c_1-c_2,\quad
B=hv_1-c_1-2c_2,\quad C=h^2w_1-2c_2,\\
c_3=10A-4B+C/2,\quad
c_4=-15A+7B-C,\quad c_5=6A-3B+C/2
\end{gathered}$$

给出。所有相邻段准确重用同一节点 jet，因而四角轨迹在内部节点严格 $C^2$。内 collar 从平圆周及其前两阶径向 jet 连到同一个内端节点，外 correction 从零二 jet 连到所提供的前缀切口差 jet。修补起点在有理域中定义为 $r_{\rm cut}-W$，保证终点准确是 $r_{\rm cut}$；不再使用两次浮点减法后可能相差一 ulp 的端点。

每一段加上外修补后仍至多五次，只需在外修补起点分段。检查器优先试两个端点及中点；必要时补足超过15次多项式零点数的互异有理节点。若所有候选值为零，只报告该四角行列式恒为零，**不**反推曲面有平面片。

## 4. 公开 Actions 最小消费配方

只需检出小包、当前 computations、原接受前缀及三个系数块、端口文件，并用现有 `exact_20261114_public_resume.prepare_public_source` 恢复同一公开源。随后运行：

```bash
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261114_cardinal_tail_exact_check.py \
  --packet topics/visible-flex-larger-amplitude/notes/2026-11-14-public-RK48-cardinal-tail-packet/manifest.json \
  --checkpoint topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-q126-m32-tail2-actual-r1.json.gz \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --port topics/visible-flex-larger-amplitude/computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --out "$RUNNER_TEMP/visible-cardinal-tail/R238-exact-C2-normal-form.json"
```

这里前缀切口的非均值 Fourier jets 由原 `prefix_cut_coefficients` 接口直接转换，然后用有理数在四角评价，不重新积分高度均值。未来新大核闭面可以提供 `--target-json` 代替原 SavedPrefix 接口；其 `radial_difference_jets` 字段为形状 3×3×3 的有理数字符串，三个下标分别为径向导数阶数、相对于零角的三个差向量、笛卡尔坐标。原字节提取器也可直接消费新完整读出，只要求原角网格能被4整除。

## 5. 结论范围和剩余接口

该规范化有意消除“把舍入后的 Hermite 系数解释成精确数时，各段可能不再恰好 $C^2$”的问题。但它与旧渲染器中的两类舍入仍有区别：旧渲染器先算浮点 FFT，再算 longdouble Hermite 系数；这里使用原角节点所定义的精确三角插值，以及精确共享节点 Hermite。二者的表示差尚未在本检查器中定量支付，不能把新规范化的非平面性结果冒充旧字面二进字段的结果。

同样，切口目标 jets 的浮点到精确前缀转换误差、共同高度均值的 $C^2$ 拼接、完整角场的识别、闭嵌入和真实像变动仍分别记录。某个非零行列式可以极小，也可能来自有限精度节点的数据，不保证在无限精确非线性极限或下一次求解后仍保持非零。

所以检查器即使全部片段通过，也保留 `actual_delta_E_certified=false`、`exact_nonlinear_limit_nonplanarity_certified=false` 和 `task_completed=false`。这是可复用于新大核闭面的最小有限场接口，不是以小幅 A 的额外检查代替主线任务。
