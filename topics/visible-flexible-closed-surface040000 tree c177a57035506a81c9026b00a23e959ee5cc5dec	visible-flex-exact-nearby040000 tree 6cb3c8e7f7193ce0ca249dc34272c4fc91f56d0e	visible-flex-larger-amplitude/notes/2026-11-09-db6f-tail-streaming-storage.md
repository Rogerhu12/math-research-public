# 连续尾验证器的逐跨存储：同一算术、较低内存

2026-11-09，independent_geometry。本文是实现说明和回归记录；新存储方法由 root 另作独立审查。

## 1. 冻结旧后端，新建适配器

旧后端 `scripts/db6f-audit-tail-metric-curvature.py` 仍为 SHA256 `ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670`，没有编辑。

新适配器 `scripts/db6f-audit-tail-stream.py` 的 SHA256 为 `adfcfbfe03643cf8a4284c078edb13d5caa49ad5eb7f94ce822ba8c27354a456`。它仍调用旧后端的完整 run、metric、两种实际曲率公式、区间/Fourier/Bernstein、物理半径及柱坐标转换。仅替换几何数据的存储方式。

旧类同时保存所有跨度的 F、G=Fr、Gp=Frr 区间幂系数。新类全域只保存每跨左端 V0 的上下端点，当前 span 的 F/G/Gp 即时生成并缓存；相邻背景子盒属于同一原 span 时复用缓存。整个有限图以及每个系数包围均未改变。

## 2. 原顺序累计不变

所有精确 Fraction 半径、正跨度与 anchor guard 沿用旧定义。长度区间与旧构造完全相同。以128跨为一个工作批次计算

$$
\Delta V=L\left[\frac7{30}(u_0+u_1)+\frac8{15}u_m+
\frac1{60}(v_0-v_1)\right],\qquad v_j=L f_j.
$$

每个分量的括号与乘加次序不变；批次只改变向量化数组的外层长度。节点状态仍按 i=0,1,… 顺序逐项执行区间加法，保存后再加本跨增量，既没有树状 reduction，也没有跨批次重置。故 V0 的上下端点逐位应与原实现相同。

即时 F/G/Gp 的公式、每个运算符的顺序和广播后的各分量都与旧类取出该 span 的结果相同。长度保留为一列的单元素区间，匹配原广播。collar 的系数表达式及运算顺序直接沿用。`fields` 的 compose、expand 没有改动，缓存返回的系数也不被这些只读操作修改。

## 3. 输出绑定

原数学后端仍在报告的 script_sha256 中绑定；新报告另有 `streaming_geometry_adapter`，保存本文件哈希、旧后端哈希、block_size、存储说明和实测进程峰值 RSS。适配器哈希在开始运行前冻结，不能因仅看到原后端哈希而忽略这个新实现。

## 4. 完整 M8 回归

使用原 M8 manifest、原完整 tight packet、相同 angular128/radial1/direct-threshold8.5，独立输出到 `2026-11-09-db6f-audit-tail-stream-m8-full.json`。

全部5,237行与旧结果逐项相同，压缩行数据 SHA256 仍为

`46702bb0f50d99a0dfc728b669e726c942cdd6791751587a83ccb2d263baba83`。

所有原数学报告字段相同；差异仅为耗时、输出行文件名和新增适配器元数据。metric 上界仍为9.968938237875866×10⁻⁷，实际主曲率上界仍为8.46544537300005，10个直接曲率调用仍相同。比较记录为 `2026-11-09-db6f-audit-tail-stream-m8-comparison.json`。

本次耗时约232秒，峰值 RSS 为76,111,872 bytes，约72.6MiB。该内存数是此次 M8 运行的实测值；新 M12 运行应另报告自己的实际峰值。

## 5. 独审与后续

root 已逐行独立审读存储适配器与旧类的运算等价性，并完成 M8 绝对半径格式、M12 增量半径格式的全部 F/G/Gp、V0 端点、collar 和精确 r/ell 的逐位比较，全部通过。独立报告为 `2026-11-09-db6f-root-review-tail-stream.json`，SHA256 `79f815c6037afec29d28ebc8d8678247ae6fc1bbb2335362a1eda58dcaefbc93`。两项回归均完成后才启动 M12 critical 第一档的完整连续认证。

低内存实现只改善可执行性，不提高数值界，也不改变 source、g、有限几何或独立审查的范围。更紧背景包和新的频率/网格近似仍须分别认证。
