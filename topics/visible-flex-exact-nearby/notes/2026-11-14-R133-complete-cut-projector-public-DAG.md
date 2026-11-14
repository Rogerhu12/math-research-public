# 全部 5970 个连续 projector 格的互斥公开 DAG

原 frame 提案 run `43588509643` 完整成功；四格连续 pilot
`43591378059` 也已实际成功。后者的四个完整数学单元分别耗时约
12.35、12.23、11.85、12.20 秒，五个实际子进程均返回 0，七个公开
合成约定门也通过。原四份成功 native 保持准确 SHA，后续不重算。

本次新 workflow 是 `.github/workflows/visible-exact-complete-cut-projectors.yml`。
其科学输入 manifest 为
`2026-11-14-R133-complete-cut-projector-CI-pinned-inputs.json`，含原 pilot
全部 86 个原样输入及两个新增 consumer/worker 源，共 88 项。原局部
数学 validator、interval model、candidate、repair、frame 和已成结果
均不修改。

## Prepare

只在 prepare runner 下载一次原 916,497,210 字节 frame artifact。
全部原 chunk SHA 核验后，按原 chunk 原样复制成 16 个范围包；每包
保留完整原 proposal native、准确 rho mesh 和仅该范围需要的完整
193×96 原 frame chunks。没有重建或再 QR 任一原 frame。

同一 prepare 消费已经实际成功的四格及七个代数门，运行新的完整
weighted cut/waist 边界消费者。它保留 true cap 的所有 97 行、独立
mean、新 frame Gram 及 rho 费用，见
[真实两端合同](2026-11-14-R133-true-weighted-cut-and-waist-boundary-contract.md)。
科学大数组仅作为 Actions artifact 传递；小 native 和实际过程正常推送。

## 16 个互斥范围

第 k 包的原范围为 `[384k,min(384(k+1),5970))`，k=0,…,15。
其中准确排除已成功的 `0,76,3300,5969`，保留分割后的连续 CLI 范围。
新计算共 5966 格，原 pilot 复用 4 格，二者唯一并集恰为全部 5970 格。

16 个矩阵 worker 的 `fail-fast=false`，并发上限 16。单 worker 计算
窗口 170 分钟、完整 job 窗口 200 分钟；这些是保存实际断点的执行
边界，不能代替完整科学终点。每 10 分钟使用已审 publisher 真实执行
`git pull --rebase`，查看根 README 和课题 README 的实际差异，核对
已明确读过的规则身份，并推送实际 native 前缀。non-FF 立即 pull/rebase
再推；只要新 README 未被审读，就保留实际前缀并明确失败，不偷偷接受。

本次完整 math child 仍由固定源码在 checkout 外的不可变副本执行。
每格 native 原子写入，因此定期拉取不会改变正在运行的科学定义。
凡已成功格今后都只复用；如果一段因实际异常结束，恢复时须从其真实
原 native 前缀接续，不能重新派发包含成功格的整段。原失败信息保留。

## 自动完整消费者

只有 prepare 和全部 16 段真实成功后，最终 job 才消费四格 pilot 和
5966 新格。它核同一完整科学 identity、每个准确区间和 candidate piece、
全部 5970 个唯一 index、每个接口的相同原 anchor 字节 SHA，以及首末
anchor 与新 true weighted boundary 的完全一致。腰处最后一跳也包括在内。

完整输出保留每格的 Gram 下界、完整 generator 误差、signed mu/nu、
c/e、rho、真实 projector jump 和原 native/完整 row SHA。完整新 reference
的所有 dyadic 系数已在原分段 native 中各存一次；最终 profile 不重复
复制它们，仍可由准确输入引用逐格回查。

这一步完成的是全部局部连续 projector 证书及全部接口。全局正 Green
条件、独立源、未知 high 输入、真响应误差和参数 Schur 仍不由“覆盖
完整”自动成立，必须另用 signed Riccati/端口消费者实付。

## 后续相位所需范数域

完整 regular 边值问题及正帽源仍在全域求解。相位误差泛函实际只使用
完整负区 `[0,r_star(eta0)]` 的 ordinary physical pair L2（圈测度归一化，
保留 even mean）。可在当前固定背景使用包含全部当前根的安全理性
上端 `2383968743003/10000000000000` 累计范数，最后极短跨根段也保留。
依据为 `R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md`
的 (P.17)–(P.25)，其中 (P.21) 明确积分到 r_star。

这是原固定物理 eta0、原 nu 和准确连续修补背景的接线安排；原 ac1 到
修补中心的 operator 费用仍另付。以后转到显式 delta 族或真正 nonlinear
背景时，根的位置与相关常数必须重新控制，不能将这个固定上端直接外推。
