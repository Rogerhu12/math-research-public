# 收窄 R100 域的两材料 DQ 窗口及低 46 单模输入列

作者：geometry_audit（GPT-6 Astra Pro，AI 辅助），2026-11-13。

## 范围与已执行结果

固定输入是 `inner-restricted-expanded-modal-r1.json.gz`，SHA
`d74b5972d555086b0e5dc9b7b63f6b7ee0a6399838f077da538bd79cfd497968`。
它保留原 R100 的同一个内头 g、V′、连续条带、213 胞元与完整辅助中心。
参数域为 S 的乘积半径 3/4、T 的共同 l1 半径 1/32，并同时满足输入
`domain.T_coordinate_caps_by_mode` 保存的全部个别 4b 帽。
前六个 T 坐标为零；其余 40 个坐标及共同 l1 约束同时存在。

Cs 继续使用原单位 S 域的有效包络，没有因为 S 半径变成 3/4 而免费缩放。
Lambda 采用新输入实际逐轴计算后的谱。新源严格绑定输入、正式资源记录、
原密度 SHA，以及冻结旧 DQ 源
`ecd091b4400b21d66dcc78b0933fe09689ae65473d287f0b119f8782a5e1b673`。

正式 producer 退出 0，耗时 21.884 秒，峰值 92,908 KiB，小于 96 MiB。
原 213×2×13×15 表的全部公式、端点凸性证明及支撑门保留；
增加了 213×2×13×46 的单模低输入表。
46,894 个记录门全真，其中每个新增低窗门内部逐项检查全部 46 个频率。
完整输出为 4,424,461 字节 gzip，SHA
`d519f6e5d8f0a8bb06c5d87f9257f6b9c01a19bfd04ce394a661ff3ffa3857ac`。

独立保存消费者正式退出 0，耗时 9.583 秒、峰值 35,164 KiB。
它用准确 fmpq 回读 254,748 个低列系数，核验非负性、准确二次支撑和
“单模列不超过原共同 low 列”，并核验 127,374 个逐项 s 材料支配关系。
全部 213 行和 9,798 个参考模也与固定输入逐字匹配。
审计 SHA：`a64786b939a36aab842a8ddbe75fe80d5eb3fa2ccc7b555b4d9b3996df5e7538`。

首尝试 r1 在数学循环开始前因旧资源格式没有新版 `wait4_observed` 字段而
退出 1，未产生数学输出。r2 新文件改为核该既有资源 wrapper 的固定 SHA、
原 exitcode 0 和无 signal；没有修改任何数学门、资源上限或固定输入。
该失败记录在归档 manifest 中保持可见。

## 原 13×15 表

中心正负 pair 的强帽为 \(c_k\)，输入正负 pair 的强质量为 \(v_n\)。
原正系数为

\[
\beta_s(k,n)=\frac{5kn}{4(1+k)(1+n)},\qquad
\beta_\ell(k,n)=
\frac{\max\{1,5k/(4B_0),5n/(4B_0),(5kn+1)/(4B_0^2)\}}
 {(1+k)(1+n)}.
\]

这里 \(B_0\ge120\)、\(2\le k\le92\)，所以 ell 的分子准确归约为
\(\max\{1,5n/(4B_0)\}\)。逐输出窗 W、输入窗 J 的系数是

\[
\sup_{n\in J}\sum_k c_k\beta(k,n)
 \left(1_{k+n\in W}
 +e^{-2\min(k,n)\tau_{\rm outer}}1_{|k-n|\in W}\right).
\]

旧源的 membership 分段和端点最大值证明完全不变。每个输入窗只有一个
共同 strong Fourier 质量，不按窗中的频率数重复使用。

关于材料单位：相对 N 中的材料是 \(s(V'/w)^2\) 与
\(|\ell|(V'/w)^2\)；物理 kappa 方程源为 wN。写到 r 坐标后，材料是
\(d_1=V'^2/(rw)\)、\(d_\lambda=|w_r/w|V'^2/w\)。
新元数据已明确这一点；不改变原数值公式。

## 新低 46 单模列

现在固定输入 \(n\in\{2,4,\ldots,92\}\)，保留单独的 \(v_n\)。
由于中心也满足 \(k\le92\)，差频最多为 90，不能进入任何输出窗 W≥94。
因此两个系数就是有限正和

\[
K^s_{W,n}=\frac{5n}{4(1+n)}
 \sum_{\substack{2\le k\le92\\k+n\in W}}\frac{k c_k}{1+k},
\qquad
K^\ell_{W,n}=\frac1{1+n}
 \sum_{\substack{2\le k\le92\\k+n\in W}}\frac{c_k}{1+k}.
\tag{1}
\]

这只是原系数在单个 n 的取值，没有新的连续最大化或模式计数。
输出 ≥186 的这些低输入列全部严格为零。
因为 \(k,n\ge2\)，每个正项都有 \(5kn/4\ge5>1\)，
所以 \(K^s_{W,n}\ge K^\ell_{W,n}\) 是逐项的共同材料支配，
不能与“两个无关总质量取最大值”混淆。

DQ 已含双线性线性化的 2；cos×cos 的 1/2 已在这些 pair 系数中支付。
(1) 不再额外乘 2。消费者可计算
\(\sum_n K_{W,n}v_n\)，并与原共同 low 列乘共同 low 质量的有效上界取最小值。
若还有共同质量约束，也可对同一组单模帽使用完整正线性 support。

这些只是 DQ 的有限频率支撑。完整 Q(e)、T、mean、逆式尾项、far 和
无限输入仍按原单独预算支付，不能被这里的二次零项删除。

## 保存接口和重做

主表保持 `inner-CsLambda-DQ-two-material-window-kernels-v1` schema 和
原 `kernels_s_upper`、`kernels_ell_upper` 字段。每个顶层 `rows` 元素新增：

- `low_singleton_kernels_s_upper`：13×46；
- `low_singleton_kernels_ell_upper`：13×46。

列序由顶层 `low_singleton_input_modes=[2,4,...,92]` 固定。
每个数是 `[mantissa, exponent]` 的向上 dyadic，160 个有效位。
`parameter_domain` 是准确新 domain；`restricted_input_domain` 同时绑定
其父域、限制来源、全轴帽和“Cs 保持单位域”说明。

完整派生主表留在
`geometry-work/inner-restricted-DQ-r1/r2-kernels.json.gz`，由原固定输入和
fresh wrapper 约 22 秒可再生。归档小包含源码、compact summary、完整
域/输入 SHA、正式资源、独立保存审计和本说明。

```bash
python computations/inner_restricted_DQ_windows_and_low_modes_v2.py \
  --input /absolute/path/inner-restricted-expanded-modal-r1.json.gz \
  --input-resource /absolute/path/inner-restricted-expanded-modal-r1-resource.json \
  --density notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz \
  --out /absolute/path/fresh-kernels.json.gz --rss-kib 98304
```

`inner_restricted_DQ_saved_low_audit.py` 的独立保存门绑定的是上述原实际
输出 SHA；它不把另一运行的资源元数据冒称为原包。主输出含实际时间、
命令和资源，所以重做时完整 gzip SHA 可以改变。完整数学 `rows` 按顺序
逐行以 `json.dumps(row, sort_keys=True, separators=(',',':'))+'\n'`
编码为 UTF-8，串接后 SHA 必须为
`312f3d9c9f4bffd87f054bee57fb361f3d7b2833dda819ee3b5aad9d423f6f9e`。
这个摘要覆盖全部原窗口列、全部新增低列、参考谱、支撑见证与向上数值。
重做校核使用该不含时钟/路径的数学摘要；若要给新完整包新增独立保存门，
另写明确绑定新包 SHA 的 fresh 审计，不改旧审计的 pin。
原 q098/q106/q122 的 g/H、曲面存在性与连续几何均不属于本包范围。
