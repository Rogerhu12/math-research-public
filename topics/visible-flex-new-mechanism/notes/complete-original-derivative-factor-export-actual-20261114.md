# 完整第四导数原因子的公开实际导出

日期：2026-11-14。**公开 Actions 已完成。** 本轮补齐此前未独立保存的全部原 $N^{[0]},N^{[2]}$ 以及完整两相位 $v^{[2]},v^{[4]}$；尚未将它们代入具体 profile，也没有用原几何系数个数代替实际成本维数。

来源为 [公开 run 43651096112](https://github.com/Rogerhu12/math-research-public/actions/runs/43651096112)，source commit `2259b57065cfad67682f4c4319885fd5334c4f76`，lane `local_fourth_derivative_factors`。生产者为 [literature_local_fourth_derivative_factors.py](../scripts/literature_local_fourth_derivative_factors.py)，22205 bytes，SHA-256 `02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf`。

## 1. 已付的完整原式范围

本次保留 [R109](../results/R109-local-density-of-the-complete-fourth-quotient.md) 所选实际局部势

$$
N=P_{\rm acc}+P_h+F_*,\qquad (h_*,k_*,\omega_*)=(1,1,1),
$$

没有先模第三可调空间 $W$，也没有删除 $P_{\rm acc}$。实际检查 $N^{[2]}=P_{\rm acc}$ 的完整差为零。准确因子为

$$
L^{[2]}=v^{[2]}-\mathcal B_{m^{[0]}}N^{[2]}
-\mathcal B_{m^{[2]}}N^{[0]},\qquad
L^{[4]}=v^{[4]}-\mathcal B_{m^{[2]}}N^{[2]}.
$$

两模式 $-4,-2$ 的完整相位组合都已导出，具体完整 $\mathcal B_mN$ 尚由后继消费组成。本轮没有把某一个模式的因子当作完整两模式成本。

| 原因子 | 几何系数根数 |
|---|---:|
| 原 $N^{[0]}$ | 79 |
| 原 $N^{[2]}$ | 93 |
| 模式 $-4$ 的 $v^{[2]}$ | 665 |
| 模式 $-4$ 的 $v^{[4]}$ | 1236 |
| 模式 $-2$ 的 $v^{[2]}$ | 665 |
| 模式 $-2$ 的 $v^{[4]}$ | 1236 |
| 全部原根 | **3974** |

完整导出的原 profile DAG 有 3521 个原 atom。这里的根数是完整表达式记录数，未作真函数独立性或几何可实现性断言。

## 2. 真微分与十个几何坐标

先完成低阶场全部真实 cov 导数及 history ODE 代入，再将累计 history 的值置零。实际编译含 768 个低阶 history，零值专门化触及 732 个；第四局部目标没有新增累计第四 history。历史导数始终没有随值一起置零。

几何键准确为

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}).
$$

两模式各自在展开之前扫描完整原系数 DAG：

| 模式 | 可达原系数节点数 | 实际最大 $s$ 导数阶 |
|---|---:|---:|
| $-4$ | 32968 | **3** |
| $-2$ | 65229 | **3** |

两者均实际出现 $h,k$ 的零、一、二、三阶以及零阶 $\omega$。三阶项完整保留，旧八键的 $N,m$ 仅在末尾补两个零。没有根据总导数权就预先删掉高阶 jet。

新原势的局部第三重构准确通过；没有重编 $W$ 模板、重新求 $W$ 基或重复此前的 36 个原 $W$ 哈希成员检查。没有重编旧静态第四目标。完整原始代码哈希和所有来源均在主报告中。

## 3. 完整公开输出与准确身份

目录为 `notes/actions-43651096112-1-local_fourth_derivative_factors`。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| [主报告](actions-43651096112-1-local_fourth_derivative_factors/local-fourth-derivative-factors.json) | 5477 | `42289590f4e8319d2bd4b138497702b701a11c4bcf39ba4c7ed0c2616f3aa927` |
| [公开人工检查](actions-43651096112-1-local_fourth_derivative_factors/local-fourth-derivative-factors-development.json) | 2759 | `2222a9becfa1ecfa5e83e432d7c1f7db53ad1022ca08bc5831d3e37e0ad06b00` |
| [完整原因子](actions-43651096112-1-local_fourth_derivative_factors/local-fourth-derivative-factors-original-expressions.json.gz) | 2132064 | `9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a` |
| [独立原势](actions-43651096112-1-local_fourth_derivative_factors/local-fourth-derivative-factors-potential-original-expressions.json.gz) | 32482 | `aa0c1b9c6bab211bbb9b69ae28e5fdd2a43d7b8a22dc3fdabbb20c02d6c6a586` |
| [终端发布回执](actions-43651096112-1-local_fourth_derivative_factors/receipt.json) | 33580 | `6857ea6edb3b8132147e3c0c698f79aa6f29e3b59272850267875f45a07fe95e` |

完整因子原文 11864540 bytes，SHA-256 `58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3`。独立原势原文 169470 bytes，SHA-256 `6bc66569f9317d3090c6afe4e2001c2b60d179f1e3b98ffc4f4fc84afe124575`。

两个导出 schema 均为 `visible-flex-local-fourth-derivative-original-factors-v1-original-expressions`。完整导出的 content_scope 为 `unreduced-N0-N2-and-complete-two-mode-v2-v4`；早期原势的 scope 为 `unreduced-N0-N2-only`，不能用来冒充整个导数成本已导完。

下游沿用冻结 `old.decode_expressions`，逐根核对全部原内容 SHA。大 gzip 只由公开 Actions 在自身工作目录消费；本次对话只读小主报告、人工检查及回执，不读取大表达式正文。

## 4. 实际资源与下一准确目标

公开八项人工检查全部通过，0.001507334 秒。研究导出耗时 **433.383822157 秒**，峰值 RSS **587.92578125 MiB**，完成时有 151651 个系数节点；主报告 completion 为 complete，完整导出已由本仓库 Actions 终端 Git 发布。

主报告、receipt 的 source commit/run/driver 与两项输出字节身份已一致。下一准确目标是消费整个 $L^{[2]}+\Delta L^{[2]}+L^{[4]}$，其中 $\Delta L^{[2]}$ 使用 [R124](../results/R124-zero-matrix-static-tail-payment-and-remaining-derivative-costs.md) 已发的全部 18 个 packet，再按 [R129](../results/R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 处理真实水平几何分部积分。

当前成功完成的是缺失原式的导出。它不宣称这些几何系数可以独立实现，也不宣称第四周期、完整成本商、符号锥或 ruling 已经支付。
