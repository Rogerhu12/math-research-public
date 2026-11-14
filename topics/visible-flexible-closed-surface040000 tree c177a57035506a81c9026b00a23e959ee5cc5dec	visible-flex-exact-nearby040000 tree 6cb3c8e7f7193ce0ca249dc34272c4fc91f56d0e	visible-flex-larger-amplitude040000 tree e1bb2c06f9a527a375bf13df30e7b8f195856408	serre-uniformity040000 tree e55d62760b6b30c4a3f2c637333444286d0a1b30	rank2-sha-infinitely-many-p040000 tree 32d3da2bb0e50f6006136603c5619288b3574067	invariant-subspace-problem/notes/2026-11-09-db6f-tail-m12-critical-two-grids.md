# 同一 M12 CP 的两档 critical 尾表示

状态：**有限显式图的数值比较与连续一阶证书；不是精确 ODE 或无限 Cauchy 定理。** 两档完整导出均实际退出 0，原文件冻结。作者 `/root/tail_theory`，2026-11-09。

## 1. 冻结问题与两档输出

两档均使用最终真实联解
`db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64_tail_0018.json.gz`，输入 SHA256 `6241c30aa25355b73af2ed154e58dbc25297f7e11d97bfe040c64eb4e57458e2`。物理背景、原生 CP 的 parts4/steps64、N512 角重构及 planar degree192 都相同。仅 raw0 的表示网格加密；深部保持每 stage 64 步。

| 项目 | 第一档 | 第二档 |
| --- | ---: | ---: |
| critical ratio | .1 | .05 |
| raw0 基本网格 | 64 | 128 |
| 总共享节点 | 18,553 | 20,953 |
| 压缩分片数 | 24 | 26 |
| sampled actual XYZ metric | $1.96721814\cdot10^{-8}$ | $1.96724320\cdot10^{-8}$ |
| sampled fullTensor | $8.183040\cdot10^{-5}$ | $8.197479\cdot10^{-5}$ |
| sampled actual curvature | $6.428977$ | $6.428979$ |
| 阶段端 $F_r$ 补偿最大值 | $8.898\cdot10^{-12}$ | $3.872\cdot10^{-10}$ |
| 阶段端 $F_{rr}$ 补偿最大值 | $1.939\cdot10^{-8}$ | $2.232\cdot10^{-7}$ |

第一档 stem 为 `db6f-tail-inc-flat17-m12-critical-r01-s64-q512`，manifest SHA256 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。

第二档 stem 为 `db6f-tail-inc-flat17-m12-critical-r005-outer128-q512`，manifest SHA256 `79e0ebcdca1654e4186eb245c02ce89d0fd6c88cd174a3317d30bbd798d47c69`。最大压缩分片为 4,419,822 bytes。`independent_geometry` 已用独立流式读取器核第二档 26 分片、25 个逐字节共享接口、全部正增量与精确有理归一和，报告 `db6f-audit-critical-r005-data.json`。

更细的导出网格改变内部 RK 评价的位置和小步长，没有重新求原生 CP。阶段端补偿随之改变，特别是第二档的补偿增大；这些量是该有限图定义的一部分，必须与网格误差同时列出，不能把第二档称作重新 shooting 收敛。

## 2. 各自的连续一阶证书

已审低内存脚本 `db6f-tail-first-bounds-stream.py` 分别完整运行，包含每档自己的 R6 collar。它只按相同原顺序累加精确表示区间，独立审查曾在 uniform M12 全量输出上验证与原脚本逐字段一致。

| 全尾量 | 第一档严格上/下界 | 第二档严格上/下界 |
| --- | ---: | ---: |
| $|V_h|$ 上界 | $.000139094980367$ | $.000139094981407$ |
| $|V_z|$ 上界 | $.000835047906757$ | $.000835047950133$ |
| $J_{xy}/r$ 下界 | $.99492337301653$ | $.99492338049907$ |

报告分别为 `db6f-tail-first-flat17-m12-critical-r01.json`（SHA256 `5c2ddbfc230416cf7805bf84ea5686ed9db1427c2df2b8f1b3a8379b453e848d`）与 `db6f-tail-first-flat17-m12-critical-r005.json`（SHA256 `4d37795f5db9669dcfb5f49d75b36199f213d1b06707b203d85d7009f0b73c23`）。每档各自全部横截面严格星形且水平 Jacobian 为正，因此各尾块的水平投影嵌入；全局与前缀/帽的组合仍使用同一档闭图的独立账本。

## 3. 连续 C² 比较与剩余定位

`coupled_prefix` 用原已审 Fraction 共同分割及向外 Fourier/Bernstein 算法，通过独立审过的流式存储层，对两档共同外域作完整比较，实际退出 0。39,503 个公共物理跨上的上界为

$$
\|\Delta V\|\le5.648\cdot10^{-11},\qquad
\|\Delta V_r\|\le3.604\cdot10^{-9},\qquad
\|\Delta V_{\theta\theta}\|\le3.670\cdot10^{-8},
$$

而径向二阶差仍有

$$
\|\Delta V_{rr}\|\le6.120923\cdot10^{-4}.
$$

报告 `db6f-prefix-tail-m12-critical-r01-r005-c2.json` 中最坏区间为 $r\in[.5277879619574253,.5277881171726982]$，不同于先前约 $.520937$ 的尖峰。独立在该小区间上采样确认实际 $rr$ 差达到 $1.891935\cdot10^{-4}$，位于 $r=.5277881139390467,\theta=0$；因此剩余差异不全由区间包装造成。后续先核该局部 source 与插值一致性，不盲目加密整个尾部。

比较只包含共同外域的扰动。同一旋转背景相消；未比较 R6 collar、闭图高度归一或无限截断尾。两次有限比较不是 C² Cauchy 极限证明。

## 4. 对 README 完成门的含义

critical 第一档已经把原 uniform 的 fullTensor 约 $6.42\cdot10^{-4}$ 降到 source fullD 约 $8.24\cdot10^{-5}$ 的水平。第二档保持这一水平，actual metric 也稳定于当前 M12 角频误差。fullTensor 是另一个二阶张量诊断，不能称为 metric 残差。

这些数据支持把表示欠分辨率和源频率误差分开处理，但本身尚未支付 README 的全部固定度量精度收敛门。尤其上面的有限 $rr$ 差仍需定位；真正高模源联解由另一条工作线继续。
