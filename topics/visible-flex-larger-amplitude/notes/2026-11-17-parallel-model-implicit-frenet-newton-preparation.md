# R647 独立 Y/U 全节点 Newton 入口：准备与完整初始残差

本条记录代码准备、实际初始化及随后唯一固定预算运行的启动。初始化报告本身的 fresh-J 次数为0；2026-11-17 17:51 UTC 左右另启唯一 `--execute` 运行，尚无新接受解。新源默认只准备；准备和运行输出分开。

## 1. 固定问题及全部方程

唯一暖场是原短准备输入 `parallel-hold-m160-short-bvp-warm.json.gz`，SHA256
`1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`。
不读取旧显式 BVP 的失败轨迹。保持 M160/N2048、原 `[0,1.03]` 的 **602 个节点**、同一 HoldProfile，以及原 325 左行、157 右行和非零 terminal target。

每节点独立未知为 $Y_i,U_i\in\mathbb R^{482}$。约束为 R647 的完整标量投影
$C(Y,U;k)=P_r(V\cdot F_\varphi,\;V\cdot F_{\varphi\varphi}+k|F_\varphi|^2,\;|V|^2-1)$，没有删掉其中的 Fourier 行。
每胞中点用实际共同 cubic Hermite 的

$$Y_m=(Y_i+Y_{i+1})/2+h_i(U_i-U_{i+1})/8,$$
$$U_m=3(Y_{i+1}-Y_i)/(2h_i)-(U_i+U_{i+1})/4.$$

全部计数为：

| 类别 | 条数 |
|---|---:|
| 独立 Y/U 未知 | 580328 |
| 602 节点的 482 约束 | 290164 |
| 601 中点的 482 约束 | 289682 |
| 原左右边界 | 482 |
| 总约束 | 580328 |

左边界从原固定结构与暖场前三 core 系数重建，右行和 target 直接从同暖场读取。组合矩阵 `(BA,BB,target)` 的 little-endian float64/C-order SHA256 为
`8c32e71e1fe5428ccb28a39f2314ab78dd4ff223309e1553f8d52e7675490910`；已经与原配套 `2d3c4133...` arrays 逐字核对相同。

## 2. 完整消元、复用和 merit

每次 fresh-J 保存全部节点的 $C_Y,C_U$、$C_U$ 的 LU，以及
$A_i=-C_{U,i}^{-1}C_{Y,i}$；所有中点的 $C_Y,C_U$ 同样保留。当前残差为 $c_i$ 时，**每次线性求解重新计算** $b_i=-C_{U,i}^{-1}c_i$，而不是沿用上次的节点右端。

把 $\delta U_i=A_i\delta Y_i+b_i$ 完整代入中点方程后，使用原 c76 DiskQR 对全部相邻 $482\times482$ 块和原分离边界求解；然后重构每节点 $\delta U_i$。既复核 c76 的凝聚线性残差，也使用保存的原 $C_Y,C_U$ 逐一复核 **未消元的全部节点、中点和边界线性方程**。实现中展开矩阵乘积只是节约运算，原块内容不删减。

满步后允许复用整个同一次 fresh-J；旧节点和中点 Jacobian 始终成套保持，不掺入当前新 Jacobian。复用因子不下降时，只在同一当前点刷新；fresh 因子 17 次回溯全部失败时保留旧点。

本入口使用新的 **raw 残差平方和**

$$\mathcal M=\sum_i\|C(Y_i,U_i;k_i)\|_2^2
 +\sum_i\|C(Y_{m,i},U_{m,i};k_{m,i})\|_2^2
 +\|B_A Y_0+B_B Y_{601}-t\|_2^2.$$

它与原显式求解器的 affine correction merit 不混用。回溯为 $\alpha=2^{-j}$、$j=0,\ldots,16$，接受条件为
$\mathcal M_{new}<(1-.4\alpha)\mathcal M_{old}$。预算固定为最多 20 步、8 个 fresh-J；节点与中点每一条 $P_r$ 残差容差 $10^{-8}$，每条原边界容差 $10^{-11}$。不加节点、不放宽容差、不扩大预算。 第 8 个 fresh-J 满步之后仍可复用该因子至总 20 步；只有确实需要第 9 个 fresh-J 时才由预算门停止，8J 后的 stale 无下降单独标明刷新预算耗尽。

多项式允许在 $H<0$ 仍被代数求值，故试探阶段不使用旧显式平方根域作为拒绝条件。非有限残差仍拒绝。终态必须另看正确正分支、未保留角模和实际度量；$P_r$ 变小本身不意味着物理接受。

## 3. 已实际完成的初始化

冻结源 [parallel_20261117_implicit_frenet_newton.py](../scripts/parallel_20261117_implicit_frenet_newton.py)，26420 B，SHA256
`5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac`。

实际准备报告 `parallel-model-implicit-frenet-602-preparation.json`，SHA256
`63c9bcd28fb25d22f7e56f874c210e597850b106e563d4e8567872e6321aa0ff`。

全部 580328 个初始残差实际计算，得到：

| 数量 | 实际值 |
|---|---:|
| 完整 raw 平方和 | 0.00015321026127227238 |
| 完整 raw RMS | 1.6248271377468946e−5 |
| 节点残差最大值 | 1.81895691394208e−5 |
| 中点残差最大值 | 0.0034869430671985377 |
| 边界残差最大值 | 4.163336342344337e−17 |

同时只对原节点及实际 cubic 中点作 N8192 诊断：$H_{min}=0.00021258785090751155$，正确分支的 $V\cdot(F_\varphi\times F_{\varphi\varphi})$ 最小为 `0.014580392999913752`；实际 cubic Gram 采样最大值 `7.5050072699644945e−6`，出现在末节点。它仍超 $10^{-6}$，且这些是样本读数，不是全域证书。

标量二次残差真实频率不超过 $4M=640$，N2048 已完整容纳这些二次频率，但 $P_r$ 仍只保留指定 482 行。报告另列 j161–320 的 **480 个遗漏实系数**：三组最大值为
`2.3891742954066948e−6 / 1.596808775008396e−5 / 1.491565891123872e−6`。真实角点约束最大值也单独保留；不以低模投影替代全角约束。

初始化实际约 4.98 秒、最大 RSS 136784 KiB；fresh-J 次数准确为 **0**。

## 4. 内存、磁盘及终态读出契约

为了保留全部原 Jacobian 用于线性复核，按当前尺寸预估：

| 工作数组 | 字节 |
|---|---:|
| c76 驻内存 U | 364445984 |
| c76 驻内存 transport | 118512392 |
| Y/U 两状态表 | 4642624 |
| 节点 A/LU/CY/CU 磁盘表 | 4475489536 |
| 中点 CY/CU 磁盘表 | 2234027584 |
| c76 L/R/LU/T 磁盘表 | 4468055168 |
| 主要磁盘表合计 | 11177572288 |

运行前要求至少 `13927949955` B 可用空间；准备时实际约 56.09 GB 可用。RAM 还需活跃块、FFT 和解释器等开销；表中是数组计数，不冒称已测完整求解 RSS。更新 fresh-J 前关闭自己的旧缓存，任一时刻仅保留一个完整因子；这些可再生表都在仓库外。

执行终态无论收敛与否均保存 `mesh/states/independent_velocities`、所有节点/中点/边界原残差、实际 `a/ap/app/k/k_prime` 和完整标量身份。它另在终态重算节点 Jacobian，记录 $C_U$ 的 LAPACK cond1 估计和

$$a_i=-C_U^{-1}(C_YU_i+C_k k'_i),\qquad k'=a''/a-k^2$$

的线性解误差。输出名为 `common_accelerations`，使后续读者可把这些 literal double 选作一个新的共同 C² quintic 二 jet。若 $C(Y_i,U_i;k_i)=c_i\ne0$，该公式给的是局部水平集 $C=c_i$ 的切向加速度，不能称为 $C=0$ 轨道导数。后续 quintic 必须计算其自己的实际一二导，不能继续使用本 solver cubic 的胞内速度。

新输出保当前真实 core，未伪造 `old_cut_jets`；也不把失败态、代数收敛或 8192 样本域正当作原 P RHS 的接受父。Cubic→quintic 的 R227 端二导修正成本仅作普通浮点诊断，仍由独立读者支付实际全域 Gram。

## 5. 准备和唯一执行命令

从仓库根执行，`WORK` 是仓库外目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_newton.py \
  --topic topics/visible-flex-larger-amplitude \
  --warm "$WORK/parallel-hold-m160-short-bvp-warm.json.gz" \
  --implicit-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_probe.py \
  --qr-source topics/visible-flex-larger-amplitude/computations/geometry_20261114_separated_qr_bvp.py \
  --hold-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_negative_hold_profile_ivp.py \
  --out "$WORK/parallel-model-implicit-frenet-602-preparation.json" \
  --work "$WORK/parallel-model-implicit-frenet-602-work"
```

实际修正时只增加 `--execute` 并把输出名改为
`parallel-model-implicit-frenet-602-once.json`，以保留此初始报告身份。所有问题来源都在入口/出口核 SHA。Newton 与物理诊断分别标记；没有自动续跑、自动精化或自动提高预算。

## 6. 唯一运行已实际开始

同一源 SHA、全部来源及预算不变，输出 `parallel-model-implicit-frenet-602-once.json`，stdout `parallel-model-implicit-frenet-602-once.log`，工作目录 `parallel-model-implicit-frenet-602-work`，唯一终态读者 constructive_model。首个完整因子的约化 cond≈1.412e6、全部未消元线性余项≤5.93e−14；第0步满步把 raw SSE 从1.53210261272e−4降至4.35947e−5，随后合法复用同一旧因子。这只是运行中的一次实际修正，未宣称代数收敛、C²几何验收或新的父。
