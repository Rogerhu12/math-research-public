# small01 的完整连续前缀：联合 Bernstein 包围及单格替换

## 1. 对象、结论与范围

本记录消费已经闭存的 `2026-11-12-fd2d-metric-gc-p148-small01-native-field.json`、实际共享节点 C¹ 原生 
η/ζ 数组、准确物理 profile/clock `exact-profile-02.packet.json.gz` 和准确固定种子角图。
对象是 R119/R125 的**固定材料 u 的 ODE 定义映射**，物理弧长由准确 profile 决定。
它使用已说明的逐片五次 C² 校准时钟；既有浮点 body 的采样值没有充当这个映射的证明输入。

实际全 237 格、全径向和全角连续消费后，仅把第 103 格换成更强的多项式包围，得

\[
 \|g^{-1/2}(X^*e-g)g^{-1/2}\|_{\rm op}
 \le 9.82291790194277\cdot10^{-7}<10^{-6}.
\]

这里的 g 是准确物理 profile 规定的同一度量。此结论是 small01 **完整前缀**的实际
度量后验。原 small01 的 linear-tail 切口均值尚未闭合，所以它不是完整强目标闭曲面，
也不支付尾缝、固定帽、曲率、reach 或宏观轴幅度门。

## 2. 新包围为何严格

设已付截断余项之后的径向/角向多项式写为

\[
 P(z,\xi)=\sum_{j=0}^D\sum_k c_{jk}z^j\tau_k(\xi),
 \qquad -1\le z\le1,
\]

其中 τ_k 是相应偶/奇 parity 的完整有限 cos(2kξ) 或 sin(2kξ) 组。
实际系数被原区间矩阵包住；所有被移出的辅助系数仍在原有统一余项中。
令 t=(z+1)/2，并把径向幂系数准确转换到 D 阶 Bernstein 基：

\[
 P(z,\xi)=\sum_{i=0}^D B_i^D(t)b_i(\xi),\qquad
 B_i^D(t)\ge0,\quad \sum_iB_i^D(t)=1.
\]

对于固定完整角弧 I_ξ，先以向外取整区间矩阵乘法计算每一个函数

\[
 b_i(I_\xi)\subset
 \sum_k b_{ik}\,\tau_k(I_\xi)=[\ell_i,u_i].
\]

因 Bernstein 权重非负且和为一，同一个角 ξ 上的 P 是这些 b_i(ξ) 的凸组合，故

\[
 P([-1,1],I_\xi)\subset
 [\min_i\ell_i,\max_i u_i].
\]

原消费者先对每一 Fourier 系数取所有 Bernstein 行的 hull，再做角和；这也是有效包围，
但会独立化不同 Fourier 模态的径向变化。新实现把两个有效包围取交集，因而绝不扩大
原结果。交集空时明确报错，不用任意端点替代。没有角抽样、径向抽样、系数置零或
改变实际有限场。

实现是另名 `fd2d-metric-gc-primitive-joint-bernstein.py`。原消费者和区间后端保持原字节。
它只安装 `M.range_polynomial` 的新包围；无角标量模型仍走原函数。非线性级数、准确
物理段、q 的几何级数、原生 η/ζ 的有限 Fourier 模态与所有余项预算全部保留。

## 3. 为何只重算一个原生格就能合并

R125 的辅助 primitive 在**每一个原生格**的两个端点准确为零；一个原生格内的所有
物理子片共用同一辅助均值。因此相邻原生格可以采用不同有效包围或不同辅助表达，
只要各格仍完整覆盖其准确左右端点并满足 R125 的端点条件。

`fd2d-metric-gc-primitive-merge.py` 实际检查以下绑定和分区：

* 原消费者、区间模型及两个区间后端、normal-range adapter 的 SHA；
* 原生场、准确 profile、角图、μ 包和真实初值报告的 SHA；
* 所有辅助次数/角弧数与完整余项配置一致；
* 旧全报告确实完整覆盖 [0,237)，所有 gzip 行和报告清单一致；
* 替换格的准确有理左右端点与旧格相同，子片首尾完全相接；
* 每个新旧格都声明并保留全角、全径向和准确零 primitive 端点条件；
* 新 range adapter 本身由其报告绑定的 SHA 找回。

消费者不是拼接各局部报告的零初值后验。它重新读真实初值
`d0 ≤ 1.638645511272696e−16`、`k0=0`，从格 0 开始调用原 R125 的向外取整
`advance`，按原生格及其准确子片顺序重新传播全部 237 格。
最终 rows 为每格保存其所用连续包围和新传播后的后验。

## 4. 本次真正执行记录

`primitive-continuous-full-01` 的 exec session 44235 自然 exit 0，报告时间
590.76837874 秒。它复用此前完整 cell189，其余 236 格实际计算，保存全 237 行。
初次有效上界为 `1.291024458623155e−6`；`actual_metric_tolerance_passed=false`
如实保留，不能删掉或改称通过。

第 103 格的主要预算是 chart drift 乘 primitive 的角导。新 `joint103-01` 的 session
79564 自然 exit 0，13.42444897 秒（包括共同角表），完整消费这一格，43 次联合 range。
它的格内 `h B` 贡献从约 `1.12917873864e−7` 降到 `3.25143838733e−8`。
其他 236 格不重算。

`merged-01` 的实际进程自然 exit 0，报告计时 0.189248176 秒，结果为：

| 量 | 向外上界 |
| --- | ---: |
| 完整前缀 relative metric operator | `9.82291790194277e−7` |
| 终端 R125 d | `2.65134614323405e−7` |
| 终端 R125 k | `1.964583097940191e−7` |
| 相同输入若仅积绝对 Codazzi 残差 | `2.19752390521445e−5` |

最后一项只说明原生格内有意义的抵消已经被 primitive 付出；它不是另一个映射。
新上界与原上界都由相同准确 profile 和有限原生场导出。
所有源、输入、完整旧/新报告及 gzip rows 的身份由本组 manifest 绑定。

## 5. 可复现入口

从本课题目录运行，新文件名必须尚不存在：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/fd2d-metric-gc-primitive-joint-bernstein.py \
  --field notes/2026-11-12-fd2d-metric-gc-p148-small01-native-field.json \
  --profile notes/2026-11-12-fd2d-metric-gc-p148-small01-exact-profile-02.packet.json.gz \
  --start 103 --stop 104 --rows NEW-joint103.rows.jsonl.gz --out NEW-joint103.json
python scripts/fd2d-metric-gc-primitive-merge.py \
  --base-report notes/2026-11-12-fd2d-metric-gc-p148-small01-primitive-continuous-full-01.json \
  --replacement-report NEW-joint103.json --rows NEW-merged.rows.jsonl.gz --out NEW-merged.json
```

运行时间、文件路径等元数据可能不同；本次结论使用已闭存且 SHA 绑定的实际输出。
