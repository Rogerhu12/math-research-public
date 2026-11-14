# 原 11 个高频比较窗的完整因果 Green 核保留

作者：geometry_audit（GPT-6 Astra Pro，AI 辅助），2026-11-13。

## 已完成的结论

这次运行保留了 R33/R50 原来逐窗计算、随后才取 `near/rest` 最大值的全部
11 个正核。每窗覆盖 cells 12–224 的全部 22,791 个因果 source/target 对，
合计 250,701 项。实际运行正式退出 0，耗时 136.858 秒，峰值 69,536 KiB；
没有重新积分 ODE、径向源或基本矩阵，没有构造新的频率窗。

原传播源码 `tail_r33_middle_causal_box.py` 的 SHA 为
`9b9c5b5fd0c76a853dc07aa6c4f5ceaea54594e445e961320c7debf3bd867346`。
原 R50 保存适配器的 SHA 为
`4dc17ec37763d533a2e7003df94698ab0d3b7ea544efb93569134f12c5f962d6`。
新保留器只扩展它的 `SplitCollector.record`，原传播、逐分量取最小值、
原 `near/rest` 最大值和原最终身份检查均照常执行。

原 22,791 个未压缩最大值逐项同 bit；完整原 far 列和较宽纯低源列也通过
原最终检查。新核的严格向上取整及全部保存项的因果覆盖、正性和 SHA
均已检查。主证书 SHA：
`3033c330ed219a1e87420818df8dd3d7bca44c246afe4f661d68870a783847b1`。

本结论只提供更细的同场正算子。原 nonlinear 场、参数域、完整 mean、
逆式余项、独立 far 输入及无限频带都没有被替换；此包本身不新增存在性、
联合收缩或闭曲面结论。

## 同场规范和缩放

原 q 密度为 `2026-11-12-tail-r33-plateau2-density-window.json.gz`，
强参考密度为 `2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz`。
后者明确保留前者的整个连续函数 \(\tau_q(r)\)，而不只是两个端点。
两份文件的全部既有门、213 个胞元覆盖，以及每胞元的 B、Q 系数、mu、w、
宽度、总变差、条带端点和参考条带逐项匹配，已实际检查。

令原精确定义的 dyadic 包络为 \(\overline X_{q,n}\) 和
\(\overline X_{s,n}\)，

\[
\sigma_n=\frac{\overline X_{s,n}}{\overline X_{q,n}},\qquad
S=\frac{257}{256},\qquad V'_n=S V_{s,n}=S\sigma_nV_{q,n}.
\]

新包中保存的每项已经是

\[
\Gamma^{\prime,b}_{nj}
\ \geq\ S\frac{\sigma_j^2}{\sigma_n}\Gamma^{q,b}_{nj},
\qquad 12\leq n\leq j\leq224.
\tag{1}
\]

源材料是

\[
d'_j=\frac{(V'_j)^2}{r w}
 +\left|\frac{w_r}{w}\right|\frac{(V'_j)^2}{w}.
\]

两个源正项都随 \(V^2\) 缩放，输出强范数随 \(1/V\) 缩放，故得到 (1)。
`defined_sigma` 完整保存 213 个准确有理比值。计算先用准确有理数建立
缩放因子，再由 192 bit Arb 向上包围，并保存 64 bit 有效位的向上 dyadic。
每条向上关系都在运行中严格核验。**消费者不得再次乘 S。**

输出使用 R33 的同一强 Fourier 范数：每个有符号模先对两个物理分量分别
取径向 supremum，再求分量和及模式和，并保留 \((1+|m|)e^{|m|\tau_q(r)}\)。
原程序的 `2*peak` 已支付“分量分别取 supremum”相对于联合 supremum
的费用。因此主证书中显示的联合 supremum 形式也被控制；用于原较强的
分别 supremum 范数时不需另乘 2。

这里的 \(\Gamma\) 只是单位共同材料源的线性 Green 核，**没有乘 DQ、
Q 或完整 T 的源常数**。它也不是两种径向材料分开的核。使用本包时仍须
先给一个逐模同时支配两材料的正源，或沿原两材料单独核消费；不得仅将
两个不相干的源总质量取最大值，假称获得逐模共同支配量。

## 原坐标变换完整保留

原窗口使用
\[
\nu_m=\frac{m^2(m^2-1)}{12},\qquad
\rho_\mu=2^{11/4}.
\]
在每个原胞元，状态为 \((Q,\Xi/\nu,Y)\)。原跨胞元传播继续使用
`inp=[Q,Z/rho]`；物理转换 `yq/yin/yout`、真实源积分上界、
\(e^{-m_{\min}(\tau_{\rm inner}-\tau_{\rm outer})}\) 以及 B 的界面费用
全部原样保留。

来源数据包含：全 213 胞元的前 9 个窗正矩阵、末 2 个窗在 cells 16–224
的已存正矩阵，以及 cells 12–23 的逐窗局部源/齐次列。后者的字段是
`canonical_Q_end`、`canonical_Xi_over_nu_end`、`local_gamma`、
`physical_norm_end`、`homogeneous_peak_over_V` 和
`homogeneous_physical_end`。

原程序先将两个有效方法转换至同一坐标，逐状态分量取最小值，再传播。
新适配器不改变这个顺序。所有原 source/target 次序也保留；本高频
初值 Green 只在 \(j\geq n\) 非零，输出矩阵的反向半三角是结构性零，
不是删除源。无限 \(|m|\ge8192\) 的另一个原算子保持独立。

## 频率窗映射

没有保存可分离的 94 与 96 单模核。两者继续共用原 `[94,96]` 上界。
同样，原 `[130,192]` 窗限制到两个不交真支撑时可各自使用，但完整共同
源质量必须保持同一预算。

| 消费者真支撑 | 本包窗编号 | 原比较窗 |
|---|---:|---|
| 94 | 0 | 94–96 |
| 96 | 0 | 94–96 |
| 98–104 | 1 | 98–104 |
| 106–112 | 2 | 106–112 |
| 114–128 | 3 | 114–128 |
| 130–184 | 4 | 130–192 |
| 186–192 | 4 | 130–192 |
| 194–256 | 5 | 194–256 |
| 258–512 | 6 | 258–512 |
| 514–1024 | 7 | 514–1024 |
| 1026–2048 | 8 | 1026–2048 |
| 2050–4096 | 9 | 2050–4096 |
| 4098–8190 | 10 | 4098–8190 |

例如在同一 V′ 规范中，source 13 到 target 12 的窗核依次为
29.997、23.134、12.639、7.326、2.827 以下（仅展示向外取宽十进制）。
这使更高窗口不再自动使用第一窗最坏值；它不能改善 94 与 96 之间本身
尚未分离的核。实际消费者应读取准确 dyadic，不能用这些展示数。

## 保存与完整重做

小归档包含新源、主证书、原冻结输入清单、正式资源记录、本证明和
稳定 manifest。11 个窗口派生文件合计 3,926,681 字节，保存在
`geometry-work/inner-window-gamma-r1/output/`，不额外提交可快速再生的数据。
原源码及科学输入均是既有仓库文件；私有冻结副本只建立硬链接。

每个 `window-NN.json.gz` 的顶层 `entries` 数组包含
`[output_cell, source_cell, upper_mantissa, binary_exponent]`。
数值为 `int(upper_mantissa) * 2**binary_exponent`。顺序是原传播次序，
消费者按两个 cell 字段索引；每窗恰有 22,791 个不同且正的因果项。
证书的 `files` 保存每个完整 chunk 的长度和 SHA。

重做时将冻结清单列出的 12 个科学输入和 6 个源码按原相对路径放入
新目录 `frozen/`。不改变其 SHA。新输出目录必须为空，然后运行：

```bash
python computations/inner_original_window_gamma_replay.py \
  --frozen /absolute/path/to/frozen \
  --input-manifest notes/2026-11-13-inner-original-eleven-window-gamma-r1-frozen-inputs.json \
  --out-dir /absolute/path/to/fresh-output \
  --rss-limit-mib 96
```

正式运行使用已存 `strong_foreground_resource_run.py` 记录 owned `wait4`
退出和资源。11 个窗口 chunk 的内容不含时钟或运行绝对路径；按上列
固定输入、固定原算术和64有效位输出可逐个核对既存 SHA。
主证书及原 replay 记录含实际资源/路径，不要求其整文件 SHA 在重做时相同。

不得将本结论转用于 q098、q106、q122 或其以后新的 H/g。这里只有原
R33/R39/R42/R100 的同一个真实内部场和原连续条带。
