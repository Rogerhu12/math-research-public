# 修复族的可移植定义与材料点入口

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

正式推荐使用

- `scripts/fd2d-metric-repaired-closed-map-v2.py`；
- `notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json`。

manifest SHA256 为
`7cc24cf74d61da9415e3b63b460c5ed1af4681974c6ee84b31771e4facf519bc`。
原 v1 源码、manifest 和 42 查询报告完整保留，不被覆盖。

## 与 v1 的差异

只有文件定位协议变化：每个实际输入绑定增加相对于本课题的 `topic_relative_file`，
读取旧绝对路径时也能保留 `topics/visible-flexible-closed-surface/` 后面的目录层次。
这修正了新 workspace 中只取 basename 会找不到嵌套 `prefix-field.json`/`tail-field.json` 的问题。
全部 11 个实际输入的内容 SHA256 与 v1 相同；两份实际字段、固定目标、桥、帽、相位及 $\Phi$ 公式没有变化。
因此这不是一个新几何候选或新的数值拟合。

实际运行还把所有输入路径改写成一个不存在的旧 workspace，并移去新增相对路径键，
以强制测试保留 topic suffix 的兼容分支。
会话 `77895` 对 $t=1/4$、下半 prefix、native $s=.8,u=.4$ 正常 exit 0。
结果 `2026-11-12-fd2d-metric-m12-material-evaluator-relocated-prefix.json`
与原 42 查询报告中的同一个材料点一致到浮点输入的舍入量级：
原 demo 将 binary64 的 `.8,.4` 转成 long double，命令行则直接将十进制字符串转成 long double；
输出坐标的最大差为 $1.1102230246251565\times10^{-16}$，实际场分量差小于 $10^{-27}$。
这些输入解析细节没有改变两份 manifest 绑定的实际二进制场。
随后用同一命令行输入和原正常路径另存 `2026-11-12-fd2d-metric-m12-material-evaluator-local-prefix.json`；
它与 relocated 输出逐字节相同，两者 SHA256 均为
`03ac69df7b0cadbc9fa28991040f72e4efa00b274d6abef42bd9b9c000221982`。
这项检查只验证可移植求值，没有把点求值残差当成连续 metric 证书。

## 使用

以下命令在课题目录执行：

```sh
python scripts/fd2d-metric-repaired-closed-map-v2.py phi \
  --manifest notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json \
  --region prefix --coordinate 0.8 --u 0.4 --t 1/4 --side lower

python scripts/fd2d-metric-repaired-closed-map-v2.py phi \
  --manifest notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json \
  --region tail --coordinate 0.5 --u 0.4 --t 1/2 --side upper

python scripts/fd2d-metric-repaired-closed-map-v2.py phi \
  --manifest notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json \
  --region cap --coordinate 0.08 --u 0 --t 1/2 --side upper
```

prefix 的 coordinate 默认是非负半图 native $s$，可用 `--prefix-units physical` 改为非负半图物理弧长；
tail/cap 的 coordinate 是半径。`--side` 选择上下半图。
活动部分先用 $u-\alpha$ 求场，再作 $\Phi$，输出供原 $X_0$ 计算器使用的坐标与最后的 ambient rotation。
帽始终返回恒等材料坐标和零 ambient rotation。

尾的数学定义使用原精确 $w$ 的弧长单调逆；脚本求值使用该背景严格 packet 的数值代表，
报告显式保留 `numerical_representative_only=true` 与 `metric_or_vertex_error_certified=false`。
所有连续 metric/reach 结论仍以独立证书和最终 R112 后验为准。
