# 实际101：同η=.01的八次接受，继续由真实末参数计算

**类别：数值证据；不是原完整求根成功，也不是闭曲面构造完成。**

公开 Actions [run43679869518](https://github.com/Rogerhu12/math-research-public/actions/runs/43679869518)，source `17a07c22ef60eb2f913703956c1284b8da533f32`，job132707948751。所有工作流步骤成功；科学 status 的 `success`、原 unit 停止条件、full112 右残差小量条件和 native/full nonlinear 成功均为 false。唯一停止原因是 `explicit outer direction budget completed`。

## 脚本、参数和输出身份

生产源仍是 `computations/geometry_20261115_small_core_inexact_p3_eta_0p01.py`，SHA256 `f43c20ea6b8a5616b4330870897a1d0b6bd2c157435544366af1fe70dcdff7bd`。完整脚本闭包、四原数学输入、父99和CLI参数位于 source 提交的 `computations/public-small-core-resonance-request.json`；执行接线是同提交 `.github/workflows/visible-larger-public-small-core-resonance.yml`。η固定0.01，外8×20、内12×20；原三方程 merit、实际 d3、Schur/normal 方向、.2 Armijo、原域、unit/full112、FD/Arb/circle 条件均未改动。初猜只取实际99的真实末参数；本轮初始值和Jacobian均fresh求值。

原临时 status 为871932B，SHA256 `8044b98a981920f3b9d51a6d08533effdcd2965b4a46ddce4caafa3a0b66a017`。原评价账本2398925B，SHA256 `77f78d208b8d6f395e5a153c834d717e7874651ad31ba8ad851ec32082e6469d`。job日志中 `BEGIN_VISIBLE101_SCALAR_SUMMARY` 至 `END_VISIBLE101_SCALAR_SUMMARY` 之间的完整UTF-8 JSON加末换行共53803B，SHA256 `d03b285893c2bd728532f44bb9a6438a5a789d91570e259b3364da5cbb1fbcbf`；root实际读取且按这段原文本核同该SHA。保留这些来源和复算配方，不将可重算原输出另存repo、Release或artifact，遵守根README137c5a新第15条。

## 原始实际读数

完整三方程 merit 从 **14191.4364621677** 降至 **13116.49060429981**。40个真实候选中8接受、32因原full-three Armijo拒绝；八轮都在第5个试步α=1/16接受。没有评价异常。依次接受后的原 merit 是：

| 外轮（从0起） | α | 原 merit | 内层原1e-8近似根标记 |
|---|---|---|---|
| 0 | 1/16 | 14101.618030487782 | false |
| 1 | 1/16 | 13997.335628842366 | true |
| 2 | 1/16 | 13877.798629983798 | false |
| 3 | 1/16 | 13744.283399996873 | false |
| 4 | 1/16 | 13598.967167176981 | true |
| 5 | 1/16 | 13444.311449749814 | false |
| 6 | 1/16 | 13282.741882599263 | false |
| 7 | 1/16 | 13116.49060429981 | false |

40个内层调用中9个达到其原近似根标记，其中2个由outer接受。其余6个接受点仍带实际d3参加原完整三方程merit；该标记没有重新变成outer资格门，最终原求根门也没有放宽。

真实末参数：
$
p=(0.5003346243435612,;-0.2840549745844459,;0.5965308971991595).
$
末 unit residual 为
$
(-152.40839651746847,;54.814796173786185,;-4.8252861791289736\times10^{-8}),
$
完整112右残差前三项为
$
(-70.39855846403938,;-3.2721425332770164,;-7.590202482662636\times10^{-10}),
$
其余109项为原零值。它们明确尚未达到原目标。

最后一次fresh参数差分检查，在步长2e-5、1e-5、5e-6处原maximum relative error分别为6.63162250463617e-9、1.6563304012759879e-9、5.09921134941033e-10，三项valid均true。原评价次数1447（859 real、588 complex），196次Jacobian，零评价异常、零observer错误。末source-circle node/mid最小beta²为0.005153125315679574、最小radius为0.2999999984285029；scalar node/mid最小radius为0.30000000000000027。这些有限检查不是整个闭曲面或全部t的证书。

## 已决定的续接

本轮仍有真实下降且只因预算结束，下一轮保持η=.01和全部原算法/预算/终止条件，由上述实际末p继续。新第15条禁止保留可重算大status，故105采用明确独立的短参数recipe入口与新schema，记录本轮run/source/status SHA/log-summary SHA，只把三个literal参数用作初猜；不伪造完整parent-status，也不复制本轮J、merit或成功标志作新计算。下一轮必须fresh评价/J，并由自己的原最终检查决定结果。

完整BVP、非零振幅解、高模非共振/区间横截性及本课题README闭面、全t、reach、整面metric和同g加密标准均仍未完成。继续科学计算，不以八次接受或绿色工作流收尾。
