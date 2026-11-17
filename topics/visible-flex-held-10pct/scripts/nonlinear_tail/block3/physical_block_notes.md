# 前三 cell 高谷块：几何可行，但真实正分支容量变差

本记录冻结物理标签 `finite_block_tail_v1 / block3_peaks085_030`。它与此前 beta8 单 cell 尾、真平谷 `.00358` 尾、后续保振荡脉冲尾都不同。唯一冻结源为本目录的 `hybrid_outer_factory.mjs`，参数为 `block3_peaks085_030_m8_config.json`；哈希见 `frozen_physical_manifest.json`。本记录不是闭曲面完成声明。

## 固定物理定义

从源提交 `46fe93d4bb708fdfb7935e91b8141ea77586f0d2` 的原实际 weighted tail 出发，保留全部 `n>=3` 的物理 cell 对象、其动量归一化 `mu` 和原深尾来源，仅替换 `n=0,1,2`。原每 cell 的九段结构与 source normalization 保留，新的第一 cell 五个斜率层为

`(.04, .3, .04, .85, .08)`；两个内侧 cell 的五层全为 `.04`。偶数段为常斜率，奇数段以 `S5(x)=10x³−15x⁴+6x⁵` 插值 `log w`。最外和最内全块端口另以 S5 接回原 `log w` 及其导数。相邻内部端口都取同一常斜率，因此 `w_r=0`，没有旧小谷留在这两条新接缝处。

采用物理径坐标 `r`、`w=z_r>0`，背景度量是

`g=(1+w²)dr²+r²du²`。

设 `K=10`，在每个源段参数 `x` 上定义

\[
A_{\min}(x)=\frac{\sqrt{w_x^2+\epsilon^2}}
 {K(1+w^2)^{3/2}},\qquad \epsilon=10^{-10}.
\]

内部段取 `r_x=A_min+alpha B`，这里 `B` 是正的自由径向权重。两个受保护端口用

\[
A=A_{\min}^{new}+(1-b)
 \bigl(|r_x^{old}|-A_{\min}^{old}\bigr),\qquad B=b B_0,
\]

其中 S5 因子 `b` 在全块端口为零，在内侧为一。在原受保护段曲率不超过 K 的条件下，括号非负；实现会在评价点检查该余量。由此整个新段有 `r_x>=A_min>0`。在端口，`w,w_x,r_x` 恰回到原值，所以 `(r,w,w_r)` 同时匹配。S5 的零一二阶端导数也保留所需的高阶兼容性。

在上述旧段余量条件下，新的子午曲率有解析界

\[
\frac{|w_r|}{(1+w^2)^{3/2}}
=\frac{|w_x|}{r_x(1+w^2)^{3/2}}\le10.
\]

固定总径宽 `W` 后，正的自由系数由唯一公式

\[
\alpha=\frac{W-\sum\int A\,dx}{\sum\int B\,dx}
\]

确定。角向曲率 `w/(r sqrt(1+w²))` 另行采样检查，不能由子午界直接代替。本记录尚未为旧段余量和全角向曲率单独做区间包围。上述控制是轴对称背景的物理度量设计；非线性尾实际曲率还需要独立计算。

## 已得到的几何数值

本块固定内外径约 `.08394950463043212` 与 `.3000000000000001`，总可用径宽 `.21605049536956794`。最小曲率径宽为 `.1711325020124078`，故 `alpha=.0017276151291215477>0`。新块高度 `.060669106837900444`，有限已建全尾背景高度 `.060955238366039874`；采样背景主曲率最大 `9.889774368114194`，最高斜率 `.85`。

最内/最外 `(r,w,w_r)` 与原背景的差均为零，只有外径浮点差 `5.55e−17`；两个新内部接缝的三项差都是零。几何重建记录见 `geometry.json`（scratch）；导出摘要只需保留这些标量及其文件哈希，完整可重算端口/网格数据不提交。

初版曾错误地把曲率所需的最小径速也乘上端口混合因子，采样得到曲率 `12.58`；冻结版已使用上面的正余量公式修正。中间等价实现因嵌套求积过慢而被主动中断，不能将它记成数学失败。冻结版直接从原 integrand 计算旧物理径速，避免不必要的旧径坐标积分；没有改变物理公式。

## 真实有限非线性计算

生成的 worker 只替换实际物理工厂并将相对 import 定位到原恢复源。完整零模、非零模、动量方程、Newton、shooting、D/S/A 正分支守卫及审计保持原样。物理 warm 的严格比较额外包括完整 `outerCellDesign`，且原 `constructor` 比较仍在，因此旧 beta8 warm 不能混入此物理块。

从固定 q18 完整 20 模 H 中取 M8 截断，以 `+lambda H` 作为明确的 forcing 方向，求真正非线性尾。正号与这条新线性前缀的主模反号相符，但这个旧完整 H 并没有重新匹配到新前缀；不能据此称实际接缝已成立。

| lambda | 结果 | min A | 实际度量误差 | 曲率审计 |
|---:|---|---:|---:|---:|
| 1e-6 | 接受 | .9608532893 | 2.89e-15 | 9.8897017 |
| 1e-5 | 接受 | .5771006439 | 2.90e-15 | 9.8897042 |
| 1e-4 | 原 D/S/A guard 拒绝初值 | — | — | — |

最小 A 已转移到未改动的 cell3、segment4，`r=.07546835004675057`、`w=2.97080994480089e−6`。在 `lambda=1e−6` 时该点 `K_g=−1.0142691e−10`、混合二阶形式约零，而实际 Gauss 标量残差仅 `2.84e−25`；这不是低模几何误差冒充平滑。将前面两段改成长高谷确实失去了原有振荡衰减，新的几何预算并未带来振幅容量。

这三次求解只记录该有限截断和求解分支；`lambda=1e−4` 的拒绝不是所有等距嵌入的非存在结论，也不证明精确的非线性上限。后续设计转回保留各 cell 两次脉冲的参数族。

## 实际线性端口及前缀重配

完整 M8 worker 初始化给 `D1=−46.33462846244871`，材料频率为 `2,4,...,16`。相同 cutoff、v55/v60、ShortBridge peak fraction `.2` 的线性前缀根是 `delta=.17185390184913849`，`H1/q=−.00285233024901301`；这是新度量的重新求根，不能使用旧 prefix 的 DN。

1024 步 M32 扩展保留 canonical M8 和 cut 的字面值，新文件 SHA256 为 `b804d2b0e8654604ffd40a078f63b5f49016eaf045e2cf0f6b9e5d99617efc2c`。首八列直接 512 至 1024 步的最大相对差 `7.2241e−7`，所以它仍是有限线性输入，不是精确无限 DN 证书。

原通用导出器曾硬编码 `constructor=hybrid_outer_cell_v1`，已修为显式 `--constructor` 参数。正确 `worker_port8_block_canonical.json` 的 SHA256 是 `f849e6f40b0826d693087388ac0704bb7a553c6aeb3df1ef589e2365579e452c`；它仅更正标签，完整 worker D/cut 不变。严格参数 guard 在任何新尾计算之前拦住了错误标签，没有混用 beta8 数据。重算时应直接给 `--constructor finite_block_tail_v1`，无需保存数组作为输入。

可重算入口均使用已发表恢复清单中的同一 source topic：

```sh
python make_hybrid_worker.py "$SOURCE_TOPIC" "$RESULTS/hybrid_tail_worker.mjs"
python export_hybrid_ready_port.py --source-topic "$SOURCE_TOPIC" --worker "$RESULTS/hybrid_tail_worker.mjs" --config block3_peaks085_030_m8_config.json --constructor finite_block_tail_v1 --out "$RESULTS/port8.json"
node hybrid_linear_port.mjs "$SOURCE_TOPIC" "$RESULTS/hybrid_outer_factory.mjs" block3_peaks085_030_m8_config.json "$RESULTS/port32.json" 1024 32 "$RESULTS/port8.json"
```

先将冻结的 `hybrid_outer_factory.mjs` 复制到 `RESULTS`。非线性 trial 继续使用已发表 `continue_tail.py`、原 fixed q18 checkpoint 运行时再生的 H、此新 worker 和独立输出目录。所有 checkpoint、完整端口和网格数组留在 scratch；提交源码、参数、标量结论和哈希即可。
