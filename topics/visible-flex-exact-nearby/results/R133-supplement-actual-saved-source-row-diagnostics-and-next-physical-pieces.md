# R133 续篇：六个完整原案例的实际源行诊断与下一真实片

2026-11-15，visible-exact-astra-0df9。

**实际诊断已完成。** public Actions run
[43679322008/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43679322008)
的真实子进程退出码为0，六条身份门均通过；诊断过程耗时
2.354193127000002 秒，父 wrapper 的子进程等待墙钟为
2.5193259910000023 秒，两者不混用。

这是一次新增的已存行诊断消费。它只用标准库 Fraction 读取原 ball
已经保存的有理上端并排序，**没有**重新计算旧 operator norm、
interval integral、target、FFT、ODE 或原78个成功科学阶段。
排序也不提供实际误差的下界。

## 1. 脚本、完整参数与原件身份

实际脚本：
[scripts/fourfold_codazzi_saved_adjacent_source_row_diagnostics.py](../scripts/fourfold_codazzi_saved_adjacent_source_row_diagnostics.py)，
SHA256
b7884944d246c85ff546eb20d4a4b012097fee912887eb94072f52b1e875349c。

完整参数：
[2026-11-15-R133-saved-adjacent-source-row-diagnostics-CI-inputs.json](../notes/2026-11-15-R133-saved-adjacent-source-row-diagnostics-CI-inputs.json)，
6951 bytes，SHA256
09b2f621824078c3b10093e4963f4ce80b6a482197e33f667a055d06dd13769e。

实际 CLI 为
**--repo <immutable-science> --manifest <上述完整参数文件>
--manifest-sha 09b2f621824078c3b10093e4963f4ce80b6a482197e33f667a055d06dd13769e
--out-dir <runner-temporary-output>**。

11个 pin 包含这个脚本及原 run43676926141 的 native、process、
publication、worker和六个完整案例。已入原Git的输入从准确历史提交
a3d84d905ce72e3a854874bbe98d119623f3f8de 逐项 git show 到临时目录；
自然5500010-byte的最后案例从原artifact14146726654临时读取，
仍核原SHA256
cce603603bbbc35e32897a36a570b98dbb993b8e80396862a7f330c98965264c。

输入共4383行，4215行是逐字保留的原外行，每个案例各保28个已选
邻片新源行。全部原真实径向权、1079物理seam、653 normalized ledger、
九个非局部词和五个独立偶mean保留。原实际14门、原28继承阶段和
78阶段总身份由本脚本逐项检查。

## 2. 真正最大的已存行

下表是每个案例、每个侧的既存上界排序结果；没有以某个局部项
替换完整源界。

| 原半径 | 负侧完整／local | 负侧nonlocal／mean | 正侧全部四通道 |
| --- | --- | --- | --- |
| 1/1000 | piece2547，common-row752 | piece2547，common-row752 | piece2551，common-row796 |
| 1/500 | piece2547，common-row752 | piece2547，common-row752 | piece2551，common-row796 |
| 1/200 | piece2547，common-row752 | piece2547，common-row752 | piece2551，common-row796 |
| 1/100 | piece2547，common-row758 | piece2547，common-row752 | piece2551，common-row796 |
| 3/200 | piece2547，common-row758 | piece2547，common-row752 | piece2551，common-row796 |
| 1/50 | piece2547，common-row758 | piece2547，common-row752 | piece2551，common-row796 |

所有这些最大行的原角色都是 copied_original_complete_row。
在最小半径，负侧原serial75/root-row725和正侧原serial120/root-row768
的 local 平方积分界都大于各自 nonlocal 及独立 mean 的平方积分界。

两侧最大非局部词均为 **complete_RQ_J_gd**；
最大独立偶mean词均为 **complete_uJ_gd**。
其余八个非局部词与四个mean词仍完整留在实际结论中，
未将某个最大词解释成唯一项或真正残差的下界。

原 ball、完整区间、径向权及逐词值见
[实际结果](../notes/saved_adjacent_source_row_diagnostics_ci/run-43679322008-1/actual-result.md)。
该文本13843 bytes，SHA256
1ed5c3914a7434c9335d44ee07b7c360ff2c31c387c508cee3a00366ef1eaa42。
两条完整原行的payload SHA256分别为：

- negative：e4a59187c128def23d30a46c125255960423362b7e3042a3209036c31ed5b714；
- positive：3ad9422e06722b10077db72627f8a8b1b5f47f83b175291fbe7621d0a496e4c9。

## 3. 输出哈希与最新储存规则

[实际execution记录](../notes/saved_adjacent_source_row_diagnostics_ci/run-43679322008-1/execution.json)
为12402 bytes，SHA256
622bfabc71cf2f51749dcb15f8225ba58a4615fc6d94064c41a77bfe5fab7624。
它记录脚本、参数、实际命令、run、全部输入和输出SHA256及六条门。

完整诊断native在临时目录产生，2917 bytes，SHA256
4c763fec183402896882bf524da82406f384ec9f2dd77063d4bf74539a9f9f2f；
实际子进程receipt为7818 bytes，SHA256
3a6b963383f24701705aa89ee3447b2d4b2e6113b2570bd164619daaa604ed23。
六个完整诊断stage同样只在临时目录产生，全部哈希见execution记录。

按最新根规15，这些可重算输出没有提交Git、没有上传新Actions artifact，
也没有上传Release。保存的是脚本、完整参数、run、输出哈希和本实际结论。

runner于05:03:02.005593及05:03:12.505994 UTC执行真实pull；
两次到05f9c27ed946be658dc46b5d84a8a9d952a99e8f，
两份README差异均空。现行已读规矩提交仍是
137c5a877fb387a82cbde01f084d1fa67ee717aa。

## 4. 这条结论推进的范围

下一项处理已经由原案例定位的piece2547和piece2551。
先核原Rg/RHO是否完整覆盖其两条真实ray；若覆盖，才按原完整相关
比较合同继续，保留非零entry、径向积分常数、真piece接缝和完整
九词／五mean。如果该旧域不覆盖，须实际支付共同T径向参考及
旧circle primitive的改变，不能外推原root Taylor球。

本条没有提高任何原源上界，也没有证明修正seam算子、
正区weighted两端端口、strong-return或cutoff97的充分性。
这些仍在open.md中持续完成，最终PDE族和参数Schur尚未由本诊断取得。
