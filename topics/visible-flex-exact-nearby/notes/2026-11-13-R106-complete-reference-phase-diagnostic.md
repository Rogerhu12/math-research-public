# R106：完整有限参考轨道上的真实非均值相位诊断

2026-11-13，phase_inverse。本记录是实际运行后的诊断，**不是有向区间相位证书，也不是 R104 的完整算子逆**。

## 1. 输入与完整性

程序为 scripts/fourfold_subprincipal_full_phase_diagnostic.py，源 SHA256：

    46539317a2fa26f807785017433a7a628974ebc254b36631b98516d171520dd7

它读取同一真实仿射对象的中心参数

\[
p_5=-7789843107295549/4611686018427387904
\]

和完整 550 段历史参考。描述符、U/L manifest、Q manifest 的 SHA 分别为：

    097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052
    43cbffb2e0b924b6d69608df54e0acf3cf8ecd66c030b7343e84864ad6eb81a0
    f1e7556a13aef2a4e5661fc00c1e9c4eda961335fb8685d26bcef550b7b147ce

本次先通过仓库现有完整 forward bootstrap 恢复全部历史文件，再验证其旧哈希。诊断入口本身再次逐个检查全部 23 个 U/L shard 和 12 个 Q shard 的字节数与 SHA；任何缺段都直接拒绝。恢复记录另见 notes/2026-11-13-historical-forward-reference-cache-recovery.json。它保留每个有限 Fourier 模态，包括真实乘积 Q*a 的全部频率，未用单独的 549 段包替代全程。

实际参考位置和导数是

\[
Y(\tau,x)=x/4+U(\tau,x)+Q(\tau,x)a(x),
\qquad
Y_x=1/4+U_x+Q_xa+Qa_x.
\]

初始物理角为 H5(x)/4。每个 Fourier 频率在网格上求值时作精确有限折叠；角导数先乘该项的真实频率，再折叠，因此没有把高模态简单丢弃。

根场使用同一参数中心的 80 阶七场参考及完整正则化：

    data/R106/root_seven_center_degree80/report.json
    SHA 7307c9581b631353680f01eb733b6f8662b566b2074d7e8918223b6080fbc997

    data/R106/root_regularized_center_degree80_plus/report.json
    SHA f89e21d3e97e14348a56702834275dd4185a6a75abb915de6ccac592b5d005ce

正则源含全部 81 个径向行，程序验证每个 coefficient shard。此处读取的是其有限系数中点，完整误差尚未计入此次诊断。

## 2. 实际计算的函数

沿全部参考轨道计算 R106 原高度规范的几何相位，先使用已证明的 strict/root cut-flux 精确抵消。严格区积分为

\[
\frac12\int D(Y)Y_x\,dr+
\frac12\partial_x\int S(Y)\,dr.
\]

两根都保留完整正则源、根端项和 transport：

\[
\int H_\sigma(s,Y)Y_x\,ds,\qquad
Y_x(c)\left(B_{-3}(Y(c))/c^3+B_{-1}(Y(c))/c\right),
\qquad Z_\sigma(Y(0)).
\]

反向根和正向根使用各自真实方向及 sigma。平均没有提前取出，没有只计算 beta。所有参考 time knot、几何 scalar knot、两根与 cut 都用于分片，最终共 884 个积分片。

几何有限 primitive 使用 512 个 Fourier 输入节点；完整有限几何在 4096 点 FFT 网格上建立 14 阶局部 Taylor 求值。结果采用浮点中点，Gauss 求积误差和无限几何误差尚未定量计费。作为公式核对，在 r=.101 的六个实际物理角上，同一浮点 D 值均落入原 directed FastBulkTarget.fast_density 的有向包络中；这项核对不扩充下面的证明范围。

## 3. 两次完整执行的结果

| 量 | 512 label / 6 阶 Gauss | 1024 label / 10 阶 Gauss |
| --- | ---: | ---: |
| 前向均值 | 18.512522704377638 | 18.512522522311620 |
| 前向采样最小 | 17.926641833421684 | 17.926572340464475 |
| 前向采样最大 | 19.550050409871915 | 19.554005841512320 |
| 前向去均值采样 sup | 1.037527705494277 | 1.041483319200701 |
| 前向离散非均值 Fourier l1 | 1.338571433630337 | 1.338571444978921 |
| 前向上四分之一频率 l1 | 5.275194522691324e-5 | 3.963589814284186e-8 |
| 名义两腿均值 | 37.025045408755280 | 37.025045044623230 |
| 名义两腿去均值采样 sup | 1.788654631951040 | 1.790945592183697 |
| 名义两腿离散非均值 Fourier l1 | 2.280610491326269 | 2.280610509793224 |

两腿栏计算 h(x)+h(x+d*)，仍在当前参考 label 中；真正最终 label 的 Psi=J o Phi 变换尚未纳入，所以该栏不能直接命名为最终 R104 的 b。

把 1024 网格限制到与 512 网格相同的节点，得到：

\[
\begin{aligned}
\max |h_{1024,10}-h_{512,6}|&=1.915154825837817\,10^{-7},\\
\operatorname{mean}(h_{1024,10}-h_{512,6})&=-1.820666810647964\,10^{-7},\\
\|h_{1024,10}-h_{512,6}\|_{\text{sample }L^2}
 &=1.821058626914745\,10^{-7}.
\end{aligned}
\]

前 32 个正频率系数（含零模）的最大差为 1.8206602447889964e-7；前 128 个正频率对称加权 l1 差为 1.9820248249232243e-7。网格加密会捕获新的采样极值；不能把两次极值差当作同节点误差。

这些是两次近似计算之间的实际差，不是对真相位的严格误差界，也不能以数值收敛替代全角和全族证明。

## 4. 抵消的实际大小

1024/q10 的有符号分项为：

| 完整前向分项 | 均值 | 去均值采样 sup | 离散非均值 Fourier l1 |
| --- | ---: | ---: | ---: |
| strict primary | -308.28869757280745 | 15.96847039625618 | 20.61809642356898 |
| strict angular divergence | 2.03e-20 | .01110255863360101 | .02266159217589308 |
| 两根 regular source | 1.5802930655117318 | .09695240776157599 | .22197327114891002 |
| 两根 transport 与 root endpoint | 325.22092702960737 | 16.999928684707697 | 21.87891050408884 |
| 合成完整前向 | 18.51252252231162 | 1.041483319200701 | 1.3385714449789212 |

这回答了本轮的诊断问题：完整真实公式中存在显著的 strict/root 抵消；此前 13205 的前向模量包络和 26410 的两腿包络不能反映实际角向振荡。下一份严格 Fourier 证书需要在实际有符号合成后支付误差，而不是继续将四个分项的绝对值独立相加。这里仍没有据此宣称一个更小的严格上界。

## 5. 精确重现命令与保存范围

在课题目录，环境为 Python 3.12.14、numpy 2.3.5、scipy 1.17.0、python-flint 0.9.0。所有命令须使该 Python 能 import flint；本次使用外置 scratch 依赖路径，不将依赖打包进仓库。

如果完整 forward reference 未恢复，先运行仓库既有入口：

~~~sh
python3 scripts/fourfold_ci_forward_reference_bootstrap.py --no-archive
~~~

若中心七场系数缺失，精确入口为：

~~~sh
python3 scripts/fourfold_subprincipal_root_fourier_v2.py \
  --domain-report notes/2026-11-13-R106-seven-field-boundary-v2-native-2048.json.gz \
  --include-root-aux --half-width 1/1000000000000000000000000 \
  --degree 80 --precision 92 --angles 2048 --keep 650 \
  --working-radius 7/25000 --working-strip 1/400 \
  --out-dir data/R106/root_seven_center_degree80
~~~

中心正则化源的完整重现命令：

~~~sh
python3 scripts/fourfold_subprincipal_root_regularized_fft_v2.py \
  data/R106/root_seven_center_degree80/report.json \
  --sigma 1 --working-strip 1/800 \
  --cut 268136140016943/1125899906842624 \
  --bits 256 --rows-per-shard 2 \
  --out-dir data/R106/root_regularized_center_degree80_plus
~~~

两次完整诊断：

~~~sh
python3 scripts/fourfold_subprincipal_full_phase_diagnostic.py \
  --labels 512 --quadrature-order 6 \
  --out notes/2026-11-13-R106-full-phase-diagnostic-512-q6.json

python3 scripts/fourfold_subprincipal_full_phase_diagnostic.py \
  --labels 1024 --quadrature-order 10 \
  --out notes/2026-11-13-R106-full-phase-diagnostic-1024-q10.json
~~~

两个报告分别耗时 221.434 秒和 440.511 秒，SHA256：

    512/q6:  2dfc12ab2bb4f5fa5484420755ae0365ca135ac01a623d5250cf875421c977ba
    1024/q10:79178a72368d5273c43a0600f73df8dc970630b31e8bc5db6344002ca2521640

报告保存全部实采样、前 32 个正频率和每个分项的摘要，单份小于 60 KB。可快速重新生成的中心正则化大系数块不必随此次诊断另行提交；保留源、参数、完整 report 和其中所有 coefficient shard 哈希即可。

## 6. 尚未由这次运行支付的量

真实流减有限参考的误差、Gauss 求积误差、几何无限 primitive 与舍入、全参数变化、最终 Psi 标签变换，以及该几何相位与完整 R104 算子 b 的识别都仍须独立支付。正侧 Ai/contact、全矩阵 R*、强源与有效 cutoff 也未由本次诊断推出。

因此本次可保存的结论仅是完整有限参考计算的实际数值和可复现性，及其显示的有符号抵消。它提供进一步构造严格非均值 Fourier 证书的数值依据，不替代主问题任何完成门槛。

