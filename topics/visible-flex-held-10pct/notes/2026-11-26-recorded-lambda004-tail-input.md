# 已保存 λ.004 完整高度的独立原非线性尾输入

当前material runner仍运行其M16 cold任务，不被取消或修改。它自然返回后，worker可处理下一请求 `held10-recorded-lambda004-fullH-20261126-01`，利用该runner已绑定的原native继续一个不同实际输入。

输入为 `2026-11-20-m3-newg-lambda0004-m24-execution.json` 的完整24维candidate_H，记录SHA256 `6d774ea36c069d0dd991aa4e2e9ed74aed8d91723b10b5ad4d5d1cd72250b7de`。该历史前缀原metric未通过；本输入不被当成合格前缀、λ.002的matched fullH或闭面。任务只问该完整高度的原非线性有限尾是否能求出，以及是否能成为明确同背景下的完整暖输入。

入口 `tail_solve_recorded_height.py --repo REPO --work WORK --outdir WORK/recorded-lambda004-fullH` 逐字绑定记录、完整原背景、M24/N512/steps16 native及两worker源；原solveTolerance、Jacobian和audit门不变。依次用H_j f^j、f=.25,.5,.75,.9，随后完整f=1且请求原1776项heightJetJacobian。每步必须真实converged、finite residual≤原tol及audit返回；所有完整checkpoint只留runner，只有实际小结果回传。

原client的保存路径已核：output=OUT/tail，保存OUT/tail_NNNN.json.gz，其内保原request/response/config/source_sha256；不自行伪造accepted包。准备入口通过编译与CLI检查，尚未执行这条新尾。lowq独立runner `45772029917` 已于06:59:35 UTC真实启动，仍按旧成功checkpoint路径恢复与自身实际prefix匹配的fullH。两路对象分开，不交叉拼接证书。
