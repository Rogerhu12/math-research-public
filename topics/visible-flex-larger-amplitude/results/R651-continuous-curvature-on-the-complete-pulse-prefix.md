# R651：同一归一化 pulse 前缀的全连续主曲率界

**当前强化：同一场全域曲率已收紧为 K≤7.04608，见最后一节。** 以下保留原818固定计划的完整终态。

**已证明。** 在 R643 所声明的 IEEE binary64 向外舍入模型下，同一实际归一化 pulse 前缀的全部径向位置和全部角度满足

$$\boxed{\max_{i=1,2}|\kappa_i(G)|\le7.21309.}$$

全部818胞均已完成，0失败、0异常、fatal=null；以下是同一固定对象的连续曲率证书，不是仅有限点的最大值。

## 固定对象与结论范围

沿 R638/R642/R648 的同一输入 `parallel-pulse-a5-complete-base.json.gz`（SHA `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`），取全部819个保存节点、818个共同五次胞，M320、构造角4096。保存的 Y、D、DD 均按准确 binary64 数定义共同五次，不重新调用 RHS 改左段二jet。令

$$
b=\frac1{4096}\sum_j|F_\phi(s,2\pi j/4096)|,\quad
\lambda=a/b,\quad c=(0,0,Z_0),\quad G=c+\lambda(F-c).
$$

参考 a 仍是 R648 所声明的精确 C² 标量；有限 Gauss 值不是另一个定义。以下包围覆盖同一个实际 G 的欧氏主曲率，并经正角重参数化传给 R638 的同像材料图 Fhat。它不是背景形式的曲率，也不是原 raw F 曲率。

报告原 binary64 曲率上界十进制显示为 `7.213088042997572`；框中的准确有理数 `7.21309` 已向上放宽。全域最大值取自全部818份真实报告，最坏是**胞816**，并非预先复用的817代表。其闭范围为 `[0.9999687499999884,0.9999843749999884]`，上界盒地址为8个径向子胞中的第7号、Q4096角节点第76号；该地址识别的是最宽曲率包围，不宣称真实曲率在某个单点达到此上界。面仍有边界；本条不单独推论 reach 或闭合。

## 逐胞实际六jet与严格包围

R643 的有限节点 λ核使用 b 的本来定义：b及前两阶导数都是固定4096节点的准确有限和。因此每个构造节点的径向 Bernstein 包围及 R/S/均值抵消即可严格支付 λ、λ_s、λ_ss，无须把构造节点间的速度近似当作 b 的定义。准确 scalar oracle、a与其导数误差及所有舍入均按已刊 e6ddb核支付。

旧五次、解析段及 pulse段沿固定完整计划分配。最后原胞817跨准确分界 $1-5/2^{60}$，两片都调用既有正确 scalar 公式，取三项绝对误差盒的逐项并集覆盖整个817原胞；不删除末尾 after 小片。

写 r=F−c。每点真实六jet为
$$
\begin{aligned}
G_s&=c_s+\lambda r_s+\lambda_s r, &G_\phi&=\lambda F_\phi,\\
G_{ss}&=c_{ss}+\lambda r_{ss}+2\lambda_s r_s+\lambda_{ss}r,
&G_{s\phi}&=\lambda F_{s\phi}+\lambda_sF_\phi,\\
G_{\phi\phi}&=\lambda F_{\phi\phi}.
\end{aligned}
$$
λ的三个 jet 在每个 s 是已付均匀盒中的参数。将原几何导数升阶到径向degree5后，这些式给 Bernstein 参数族的统一凸包；没有将 λ 当成 s 常数求导，也未漏掉 λ_ss(F−c)。

旋转正交架中各真实分量的普通物理角频率至多640。角导数的架连接项已包含在实际 Gφ、Gsφ、Gφφ中；R643§8再对这些分量作普通角 Taylor 覆盖。若 δ=π/Q，则每个角节点两侧闭角段用径向凸包、$\delta\|p_\phi\|$ 及 $\delta^2\|p_{\phi\phi}\|/2$ 的有向余量覆盖。第二导数的连续上界来自该真实带宽的 Bernstein/过采样不等式，全部区间 FFT 与向外舍入沿 f512 源。

本计划每个原胞分8个闭径向子胞；Q=4096，唯一原先已付的817用Q=8192。所有选择在全批开始前固定；没有在失败后改变网格。对每个连续盒以真实六jet计算第一基本形式、法向、第二基本形式及对称形算子。严格 E>0 与 det(g)>0给正则性，形算子的区间范数给该盒内两条实际主曲率的绝对上界。没有用目标g替换实际第一基本形式，也没有截断这些非线性乘积。

## 有限并集、全部相位及镜像

完整终态的地址已核为准确0..817，无缺胞、重复替换或异常。每份胞报告覆盖该闭胞的全部 s 与全部角度；共同五次及精确标量的二jet连续使端点重合处同属一个C²场。因此取818个K_i的最大值便覆盖全部[0,1]×S¹。

R642给同一G的嵌入，R638正角重参数化不改变像的欧氏主曲率。R648的相位族由绕z轴刚体旋转与材料重参数化生成，因此每个t保持同一K*。R644的准确core镜像二jet给下半场的C²接合，正交反射也保持绝对主曲率；同一界适用于整个镜像开放带。

## 实际运行与证据

唯一第二续接 session80092 已自然退出0。最终结果计数为818/818、0剩余、0失败、0异常、`fatal=null`，`complete_scope_certified=true`。所有818份完整报告都逐一读取并核对输入、六jet生成源、λ核、连续分量核、径向范围及冻结Q/8sub；全部哈希与索引一致。817份用Q4096，只有原计划中的817用Q8192。

全体连续盒的实际坐标第一基本形式下界至少为

$$E\ge0.9943730>0,\qquad\det I\ge0.02754673>0.$$

上述两值均经准确有理比较向下放宽；报告原 binary64 下界十进制显示为 `0.9943730166429494`、`0.027546731377081086`，最坏胞分别为480和0。最坏曲率胞816实际使用的三项比例误差界为
`1.5725326786165024e−12, 1.7664259584196163e−10, 3.5950211233825055e−5`。

完整报告的实际来源为：原批56份新胞报告、既付代表458/817两份、第一次恢复628份、第二次恢复132份，总数818。两次中断都只续接缺项；第二次复用686份完整G并复用已成λ685，故本段恰131次λ调用和132次G调用。最终续接耗时741.805107402秒、峰值RSS277324KiB；这是本段资源，不冒充从空目录执行全部818胞的总耗时。旧进度保存的第一恢复已完成部分耗时3461.207221006秒，当前未用它代替任何终态账。

| 仓库外实际证据 | SHA256 |
|---|---|
| `parallel-pulse-curvature-second-recovery/result.json` | `696e057c509a7b4ad6a074c5ba64934bc71ea40364085394f3f951d9c2350388` |
| 最坏胞 `curvature-cell-0816.json` | `24148b49ed759593c677780a3b98ac2ff5817c5c272f8c77573ee7428ab42d4c` |
| 完整读取摘要 `parallel-model-full-curvature-terminal-summary.json` | `94b68d0efb12d0df4cc4dd7c10cff978492720f5e9c37491e982987b625e6eb1` |
| 第二续接 manifest | `dc74a04ae6d916e486a1c96e61c08369783faefffa3159573658218eab6dbc4a` |
| `overlay-execution-binding.json` | `d3321ba22170353ee98e16d9b363a971ec3d812bbdd2712e2ab94f769b5566f1` |
| 最后续接日志／journal | `4863e5c96fcc0e66a20a61b3f6315fbc3aee9e6738c896fd0d934f35510e2161` |

数学入口仍为已刊 λ有限节点核 e6ddb、G六jet生成器582b22、分量曲率核459dc与区间算术f512。原唯一完整计划由eb2b4e驱动（计划SHA `df745a9b3c204aaea2f1fee568282be24a13b1db7245095a743b52690fbf6602`）。第一次缺项恢复用e024；第二次20c03胶水只复用先前报告后调用同e024.execute，未改变科学函数。完整源SHA、参数和实际CLI见本题已有《两固定几何批在19:49附近中断后的仅缺项续接》；从空目录复现也可直接使用原eb2b4e固定计划及其已有上游26e53生成配方，无须人为制造中断。

报告含计时和路径，重跑整份JSON不承诺字节SHA相同；上述SHA识别本次实际证据。原raw、manifest与单胞数据均保留仓库外，只刊源码、参数和结果身份。

本条尚未给出闭合尾、固定H、整闭面D、reach与held/E3指标或 README第5项固定问题求解加密。若将来另给完整闭C²场及R650的同一全域加权支持，才能把本条实际曲率作为其中一个输入。

## 固定六胞新包围：全域 K≤7.04608

原818胞终态完整保留后，只对其中原上界>7.05的811–816六胞另定Q8192、原径向8sub，固定执行一次。其余812胞全部复用；构造角仍4096、同26e53及a、实际G、共同五次和全部λ三jet均不改。六份已有λ报告直接消费，不重复λ计算。root唯一读取这次报告，session9293自然exit0，56.331699323秒。

| 原胞 | 新连续主曲率上界 |
|---|---:|
| 811 | 6.8983837556032 |
| 812 | 6.923121120927226 |
| 813 | 6.947821776106028 |
| 814 | 6.972476478129543 |
| 815 | 6.997076277291384 |
| 816 | 7.021612242801343 |

六个新界均小于7.022。完整旧终态索引696e中排除这六胞后，剩余812胞的最大值为原817的7.046075380943313，完整旧报告SHA `12b4b170eb121e03558221a954288ccc730e856c843ff6c6dd03b39086eb34b9`。精确核胞号0..817各一次、旧全部certified、六新E/det正并按原闭范围替换，故有限并集直接给

$$\boxed{\quad\max|\kappa_i(G)|\le7.04608=88076/12500.\quad}$$

这次仅改证书角盒大小；不是原求解网格/频率精化，不满足README的实际固定问题求解加密门，也不是新曲面。R651原同像、相位与C²镜像的传递理由原样适用。

新完整六胞报告 `parallel-root-pulse-curvature-six-cells-q8192.json`，9707B，SHA `8158e5d7d2735c5fe03df5528fe963a0cd728ab7034a4f7d1af5bc11c8c3728b`；新增展开kernel SHA `a06a2d95a4b8b94e7db53b7adf4262c506dff77b3a72d54965739b0db3d0b2ce`。纯元数据并集报告 `parallel-root-pulse-curvature-refined-union.json` SHA `2ef001024b936f4181ce89b79cc94bb7b20a622379e19b01d270264005730a92`；六λ完整身份与exact闭范围均在新报告。原报告中的seconds为从单个main开始的累计计时，不能把六行seconds相加当总成本。所有raw仓外。

实际CLI（原已有源码不改）为：

```sh
T=math-research-public/topics/visible-flex-larger-amplitude
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python "$T/notes/2026-11-17-parallel-root-normalized-component-curvature.py" \
 --input parallel-pulse-a5-complete-base.json.gz \
 --interval-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" \
 --raw-source "$T/notes/2026-11-17-parallel-root-pulse-curvature-component-box.py" \
 --out parallel-root-pulse-curvature-six-cells-q8192.json \
 --scaling-reports parallel-pulse-curvature-second-recovery/lambda-cell-0811-all.json \
 parallel-pulse-curvature-second-recovery/lambda-cell-0812-all.json \
 parallel-pulse-curvature-second-recovery/lambda-cell-0813-all.json \
 parallel-pulse-curvature-second-recovery/lambda-cell-0814-all.json \
 parallel-pulse-curvature-second-recovery/lambda-cell-0815-all.json \
 parallel-pulse-curvature-second-recovery/lambda-cell-0816-all.json \
 --cells 811 812 813 814 815 816 --angles 8192 --radial-subdivisions 8
```

作为未来闭图的条件预算，若整张实际闭面支持≥1/K且其余部分曲率亦≤K，则R650给reach≥3125/22019；当其实际完整D≤312500/66057时才可推出reach≥.03D。目前没有以参考直径或未造尾部填入这些条件。
