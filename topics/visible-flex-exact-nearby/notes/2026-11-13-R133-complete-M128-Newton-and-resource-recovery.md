# R133：完整 M128 有限 Newton、原始失败及资源恢复

2026-11-13，newton_source。

本次实际完成 M128 的全部有限 Codazzi 边值方程：保留128个物理
正频率 $4,8,\ldots,512$、其负频率、$C$ mean 及度量参数 $\nu$。
完整无截断有限 Jacobian 用残差核验的 GMRES 求解；Fourier 带限制
只用于 LU 预条件。最终651节点的有限求解标记为成功。

**这仍是浮点有限边值结果。** 独立加倍角网格和径向四分点只给出
诊断残差；没有据此授予连续全域或无限 Fourier 的 PDE 证书。
真正 nonlinear regular 外尾、非第四模细小入口费用、mean height/flux、
全曲面几何及两端匹配仍未由本次有限计算闭合。

## 1. 实际对象和边界保持

原对象 SHA256 是
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
浮点计算取原准确仿射区间的中心点。明确新度量族仍是
$$
E_\nu=E\exp(\nu h),\qquad
h=4096t^6(1-t)^6,\quad t=(|r|-1/20)/(13/100)
$$
在 $0<t<1$ 非零，其余为零。$a$ 保持原函数。
因此本次没有将旧 $g_0$ 的 waist/core 证书偷换给 $\nu\ne0$。
在 $r\ge.18$ 的帽上目标准确相同，这才允许独立帽定理消费。

完整状态是
$$B=\alpha b,\qquad C=C_{\mathrm{ref},\nu}+\alpha c,
\qquad \alpha=.65.$$
所有 $b$ sine 模和 $c$ cosine 模包括 $c_0$ 都进入求解。
左端要求 $b_m(0)=0$、$c_4(0)=-1$；右端要求 $c_0(R)=0$ 和全部
保留模的线性 stable-center 条件 $b_m(R)+q_*c_m(R)=0$，$R=25/8$。
该最后一行明确只是原生产者的有限线性外端条件，不是已经匹配的
真正 nonlinear regular DN。相反端的 waist mean 缺口另行打印。

body $[0,3]$ 与实际 natural graft $[3,25/8]$ 分别调用正确 provider，
没有把 body profile 外插到整个帽。

## 2. 完整有限 Jacobian 的准确公式

归一化的实际非线性为
$$
\mathcal A=-\ell c+
 {\alpha(b^2+\ell c^2)\over C_{\mathrm{ref},\nu}+\alpha c},
\quad b_r=-\gamma M\mathcal A_m-2\beta b_m,
\quad c_r=\beta(\mathcal A-c)+\gamma M b
$$
（最后的 $M b$ 只在非零 cosine 行出现）。记
$D=C_{\mathrm{ref},\nu}+\alpha c$。完整导数乘子为
$$
\mathcal A_b={2\alpha b\over D},\qquad
\mathcal A_c=-{\ell C_{\mathrm{ref},\nu}^2+\alpha^2b^2\over D^2},
$$
$$
\mathcal A_\nu=-\dot\ell c+
 {\alpha\dot\ell c^2\over D}
 -{\alpha(b^2+\ell c^2)\dot C_{\mathrm{ref}}\over D^2}.
$$
这里点号表示对参数 $\nu$ 的一阶导数，源码名字分别为
`dl`、`dCr`。全部 $\dot\gamma$ 项同时保留，
$\beta=a'/a$ 不随该 $\nu$ 改变。

对任意全部状态方向 $v$ 和参数方向 $p$，先在整个角网格重建
有限 sine/cosine 函数，计算
$\mathcal A_bv_b+\mathcal A_cv_c+\mathcal A_\nu p$，再完整投影。
乘子是实际采样的有理函数；作用过程中没有将其远 Fourier
耦合截成预条件带。

快 Jacobian 的 Toeplitz/Hankel 公式也保留。若 $f_b(j)$ 是
$\mathcal A_b$ 的归一化 FFT 虚部，$f_c(j)$ 是
$\mathcal A_c$ 的归一化 FFT 实部，$s_0=1/2$、$s_j=1$（$j>0$），
则对应 cosine 输出行是
$$
J^{(b)}_{jk}=s_j[f_b(j-k)-f_b(j+k)],\qquad
J^{(c)}_{jk}=s_j[f_c(j-k)+f_c(j+k)].
$$
它来自两条积化和差恒等式，并与原三指标角收缩逐项核对。
该公式加速的是同一个离散投影，不改变角网格的有限 scope。

径向仍使用原完整三次 collocation。令端点 RHS 为 $f_i$，则
$$
y_{i+1/2}={y_i+y_{i+1}\over2}-{h_i\over8}(f_{i+1}-f_i),
$$
$$
\mathcal R_i=y_{i+1}-y_i-
 {h_i\over6}(f_i+4f_{i+1/2}+f_{i+1}).
$$
矩阵自由作用先求全部 $\delta f_i$，再求
$\delta y_{i+1/2}=(v_i+v_{i+1})/2-h_i(\delta f_{i+1}-\delta f_i)/8$，
最后代入上述残差。所有边界行和完整 $\nu$ 列独立加入。
因此它是原有限 collocation 的完整导数。

最终版本用真实 FFT 重建和投影，减少重复稠密角乘法。
对 $b_j\sin(jx)$ 的正频率系数放 $-ib_j/2$，对 $c_j\cos(jx)$
放 $c_j/2$，mean 放 $c_0$；inverse real FFT 乘原网格长度。
投影取 FFT 实部，mean 除以网格长度，非零 cosine 系数乘二。
所有保留频率严格低于 Nyquist，故这与原有限角求值/投影完全
同一代数，只有常规浮点舍入差。

## 3. 实际独立审计

以下报告全部保留完整输入/source SHA，没有只保一个通过标记。

| 独立核对 | 实际结果 |
| --- | ---: |
| 未截带 chunked collocation 与原 scipy 矩阵 | 最大差 $2.09\,10^{-17}$ 以下 |
| 原有限非线性中心差分对 chunked 方向导数 | 最佳相对差 $1.13\,10^{-11}$ 以下 |
| M128 快 Fourier Jacobian 与原全角收缩 | 相对差 $5.26\,10^{-15}$ 以下 |
| 完整 matrix-free 作用与原 scipy 全矩阵 | 最大差 $8.89\,10^{-16}$ 以下 |
| 独立小完整 GMRES 解的原全矩阵后验残差 | $1.58\,10^{-11}$ 以下 |
| FFT 完整作用与原 scipy 全矩阵 | 最大差 $8.89\,10^{-16}$ 以下 |
| FFT 小完整 GMRES 的原全矩阵后验残差 | $1.58\,10^{-11}$ 以下 |

参数列测试选择覆盖紧支撑度量变化的径向区间 $[.04,.18]$。
完全位于 $.05$ 以下的区间会让参数列准确为零，不能用来测试
带未知 $\nu$ 的非奇异求解。

GMRES 每次计算完都另用完整算子重新求残差，要求成功返回、
有限结果以及相对后验残差小于 $5\,10^{-8}$。预条件器残差小
不能替代这个门。Newton 的实际 $C/\nu$ 区域、完整非线性残差、
affine-invariant 线搜索及原容差门不变。

## 4. 失败历史完整保留

| 实际版本/规模 | 实际结束状态 |
| --- | --- |
| v2，879节点，原全矩阵 | exit137，没有最终报告或候选 |
| v3，879节点，band16 分块 | 第一个接受步后 exit137；未保存完整接受状态 |
| v4，879节点，快 Fourier Jacobian | 第二次分解期间 exit137 |
| v5，879节点，band16、主动释放旧 LU | 第一次分解期间 exit137；只释放旧 LU 不足以解决规模问题 |
| v5，879节点，band4 直接近似 Newton | 完成并保存完整候选；第二步24次回溯无接受下降，明确 false |
| v5，440节点，band16 | 两次完整接受步后，细化到650节点时 exit137；当时没有状态 checkpoint |
| v6，879节点，band4/full GMRES | 预条件组装后 exit137，尚无完整 GMRES 或接受步 |
| v6，440节点，band2/full GMRES | 384步后完整算子相对残差 $.0157589$，真实 gate 拒绝；完整 false 报告和候选已存 |
| v7，440节点，band8/full FFT GMRES | 一次真实 Newton 整步接受；所需节点超过 max_nodes600，完整 false 报告和候选已存 |
| v7，明确内存护栏，band4，继续细化 | 最终651节点，全部有限方程成功；两个接受步完整保存 |

exit137 是实际进程状态。没有 OS OOM 日志，因此记录将内存资源
问题作为诊断，不声称已经证明系统杀进程的具体原因。
scipy 在自定义 guard 返回失败时可能打印通用的 “Singular
Jacobian”；完整报告保存真正原因，不将它解读为实际算子有奇异谱。

另有实际 sparse ordering 试验。对同一个111节点、band16
预条件矩阵，COLAMD 的 fill 约3.923、MMD_AT_PLUS_A 约6.344、
MMD_ATA 约4.046、NATURAL 约4.56；各线性后验残差通过。
所以本次没有凭经验切换到实际更费内存的排序。

## 5. 最终成功数据与真实检查点

最终保留的准确 float 参数是
$$
\nu=-6837290349363917/288230376151711744
\approx-.023721616162222504.
$$
原有限输入是 M64 完整候选；中间 v7 的440节点候选也原样保存，
再用它继续到651节点。实际角网格1024，独立诊断角网格2048；
径向诊断包含全部节点及每片 $1/4,1/2,3/4$ 点，共2601点。

| 最终有限/诊断量 | 实际值 |
| --- | ---: |
| `finite_BVP_success` | true |
| 最大相对 collocation residual | 约 $2.00\,10^{-6}$ |
| 最大边界 residual | 约 $1.06\,10^{-32}$ |
| 采样完整实际 $B$ 残差 | $5.72194777477\,10^{-6}$ |
| 采样完整实际 $C$ 残差 | $3.00636398678\,10^{-6}$ |
| 采样实际 $A$ 投影缺口 | $1.94142066868\,10^{-9}$ |
| 采样 $C$ 范围 | $[-3.745516325,-.1710391677]$ |
| 采样 $|B|$ 最大值 | $.49922759735$ |
| waist mean 闭合缺口 | $2.56388243969\,10^{-11}$ |
| 外端线性高度的齐次 $\dot A^2$ 诊断 | $1.61613072690\,10^{-12}$ |

此表的小数是浮点实际输出，不是外向区间数值；原报告中角/径向
连续证书旗标均明确为 false。帽的 $\dot A^2$ 是 $M^2$ 权，
不能不付因子而冒用为 $(1+M)^2$。

独立 launcher 对最终进程实际设置
`RLIMIT_AS = 1536 MiB`，记录源码、参数和资源状态；该门限制
地址空间而非 RSS。最终正常返回，实际峰 RSS 为
1,026,064 KiB。MemoryError 分支只会记录资源失败和已存状态，
不会给一个未完成结果补 success 标记。

每个接受步立即保存完整节点、全部状态、实际 RHS 径向导数及
元数据。440节点一步、650及651节点各一步的原始 npz 在 manifest
中有压缩归档，归档解压后的 SHA 与原运行记录逐项相同。
这些数据可准确重建完整有限 Hermite 三次多项式。最终 PPoly
则另以无损径向 shards 保存，所有端点、四组系数和全部模式保留。
每个单文件均小于仓库5 MiB限制。

可复跑的最后一段命令为
```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_bounded_process.py \
  --producer scripts/fourfold_codazzi_compact_metric_branch_refine_v7_probe.py \
  --resource-report notes/2026-11-13-R133-m128-bounded-v7-b4-process.json \
  --max-address-space-mib 1536 -- \
  --guess notes/2026-11-13-R133-compact-metric-outer-mean-m128-v7-b8-n1024-candidate.json \
  --modes 128 --angles 1024 --mesh-stride 1 \
  --jac-band 4 --jac-drop 1e-13 --jac-chunk 8 --max-nodes 1100 \
  --out notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-floating.json \
  --candidate notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-candidate.json
```
所有 producer 都拒绝覆盖完成报告；独立复跑需改输出文件名。

完整文件清单、源码递归依赖、候选 shards 及所有失败报告在同名
M128 manifest 中逐项绑定 SHA。后续几何、振幅延续和真实非零
中心帽残差将使用新文件，保持这批实际失败和成功结果不变。
