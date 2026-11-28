# R87 新剖面：原 Python 找到线性 mode-3 种子

2026-11-28，/root/design_continuation。**实际找到新的线性种子
$\delta_*=0.06809451565377872$**，比例
$r_*=1.1349085942296453$，落在刚证明的
$[21/20,23/20]$ 内。这是浮点二维线性校准；尚不是严格包根、非线性
BVP 接受、$\lambda=1$ 的准确圆弧场或完整曲面。

独立 `calibrate_single_gentle_profile_v2.py` 读取扩大盒的小证书，
核原五个标量的直接源和输入 SHA 后原样继承，**没有重算旧五点**。
新增 .0675 与 .069 后，用原 .066 已有值及新 .069 组成 bracket，
调用原 BackwardLine / DOP853 和 Brent；保持原 multistage provider、
实际 port/chart 和 ShortBridge。未另写或采用 JavaScript 数值 ODE。

| 新算的 $\delta$ | 原 $\mathrm{core}_z/\mathrm{core}_R$ |
|---:|---:|
| .0675 | .0015191530913870636 |
| .069 | −.0022850361168740597 |
| .06811038446423419 | −.000040342443105107864 |
| .06809451408629733 | $3.984925612664704\times10^{-9}$ |
| .06809451565377872 | $-5.27806277290428\times10^{-13}$ |
| .06809451565277531 | $2.023516065000528\times10^{-12}$ |

根处原归一化 core 为
$[1.0,-5.27806277290428\times10^{-13}]$，首周期长度
.5282966321677179、含原桥总长度 1.4589889021013718。
Brent 使用 $\mathrm{xtol}=2\times10^{-12}$、$\mathrm{rtol}=10^{-13}$。
这些浮点容差及输出不构成严格根的误差包络。

## 实际返回

父进程从 **15:31:37.429149 UTC** 到 **15:31:41.924232 UTC**，
真实 join，子进程返回 **0**；用时 4.494780497996544 s。
`RUSAGE_CHILDREN.ru_maxrss=81792 KiB`，子 CPU user 4.363405 s、
system .104966 s。没有调用 BVP 或构造完整 Jacobian。

完整返回在工作根
`/workspace/scratch/7c4e33ee17de/held10-design-work/`
下的
`R87-single-gentle-linear-calibration-extended-20261128/calibration.json`；
实际参数种子在同目录 `linear-root-profile.json`。
launcher 为 `R87-single-gentle-linear-extended-launch-20261128.json`。
小 observed JSON 保存完整实际 argv、直接源码/input SHA、这些标量以及
种子 profile 的完整参数文本。原 $\delta=.0645$ 准备输入和首轮同号记录均未改。

| 项目 | SHA-256 |
|---|---|
| 新续校准入口 | d24b870e5853312c9dfb9d09580d51e0ef8f1cc7cc2fe33e6e6e04531de7d183 |
| 新完整 calibration.json | d2d00683ec1ef91ddc5b799835f57709f22315ba84a57faedc7b6979be0b1ad5 |
| 已 join 的 launcher | 680f26818e3a96507f01fc39926ca1fea2ae22822ef50cada2c72d1c36ce49df |
| 实际 linear-root-profile.json | bf3233a3d686a8b04be011cd857477e5ec49bd8200be3aaa5b36fa3ffc1546fb |
| 被继承的首轮实际 calibration.json | 1f2ea915c659fdd944d1c2310e75081737504bb402c9bb6583f85d8afce21dec |
| 扩大盒的实际有理证书 | 029a0d6cfe18b7e546a56422fd15b80089ad96c5276edc0f0dd404da1fdfc461 |
| 原实际 M24 port | 42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b |

下一数值输入须使用这一**新剖面**并明确标为未接受初猜，逐个通过原
完整方程、域、物理 BC、RMS 和 metric 门。即使低幅 $\lambda=1$ 接受，
还须重新核算并选择同一最终 $g$ 的全部 10% 目标；本条没有作此完成声明。
