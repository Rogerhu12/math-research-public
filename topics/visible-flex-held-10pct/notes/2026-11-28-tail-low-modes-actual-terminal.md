# 11 月 26 日低模 full-H 尾路线的真实终态

维护：Astra-held10-7c4e33ee-20261128 / tail_closure。2026-11-28。

**性质：恢复已发生的数值执行记录，不是新的求解或存在性证明。**
原 HANDOFF 在 fresh warm 请求启动前结束；当前 main 的
`ci/live-warm-result.json` 已保存该请求的真实末态。

## 来源与有限接受

GitHub Actions [run 45849403133](https://github.com/Rogerhu12/math-research-public/actions/runs/45849403133)，
job `140011492229`，2026-11-26 15:28:16—16:40:57 UTC。工作流的
`success` 只表示调度正常，数值子任务实际 `returncode=2`。
最终投影记录所标提交为 `cbbab0d6cad6e781bcb99288ebcb74fba25e8ae0`；
入口 `seam_recover_original_tail_modes.py` SHA256
`a9d3774fbd1878b96cb29b0349e829f34ed8fe8b5a84b3978ca2a5656cbc8910`。

实际恢复的原 λ=.002/M24 前缀通过原有限门：631 点，
RMS `9.927150345213775e-7`，metric `6.482415782905739e-7`，
physical BC `3.7178883222402893e-16`，mean 1168，
δ=`.06413464104697911`。
source run SHA `ef7b935b7a4e0d6cb1d0a417acc621aa30da4be624816cb1a1ab0373dd4a9b36`，
raw SHA `46519d74e4a498cdc1328a6d459cb9ed949becd93ca3b185a08136afbad10732`，
physical SHA `b47d73a3b88fa5635b2b59a6bf5f8957d8fa43dfe5b5ba863abe64d57ec71767`。
这些是该次恢复的身份，不冒充历史原 raw 的逐位复本。

以这个实际来源的前 8 个完整高度系数运行原 DN，N=128、spacing=3、
physicalDepth=8、shootingParts=16、1152 stages，所有请求 audit=true。

| 暖因子 f（各模为 H_j f^j） | 原 residual | sampled actualMetric | 原有限响应门 |
|---|---:|---:|---|
| .25 | 3.157564294922782e-10 | 4.1078515335079255e-14 | 通过 |
| .5 | 3.13112789502413e-10 | 2.5117685709298148e-11 | 通过 |
| .75 | 1.263319081141499e-9 | 1.310030750545366e-9 | 通过 |
| .9 | 1.1185637697607024e-9 | 8.867082845753771e-9 | 通过 |
| 1 | 1.89497862171225e-9 | 2.913369323565007e-8 | 通过 |

最后 M8 完整低模包 SHA
`52f921916d7579f638fe325a916282c65bc80abbcf95f0f41d184f5783866293`；
其 actualMetric 为采样审计，formalCurvature=`8.38502632876375`，
normalizedFullDefect=`.00030867850150746723`。不能把小 metric
或前八模请求称为原 M24 full-H，亦不构成连续全尾几何证明。

## M16 的真实失败与尚不能定位的原因

原 M8 包经原完整状态 remesh 作 M16/N256 的未接受初猜；第一次
M16 请求使用来源全部前 16 个高度，factor=1、audit=true。
客户端收到 worker 的 `failed` 响应并抛出 `FloatingPointError`：
包 SHA `97fd2b605832e9d70713f3282313aa322681671bfbd8de53866313d381c4dec5`，
`client_returned=false`，`converged=null`，`residual=null`。
保存包含 1153×32 checkpoint 的摘要，因此不是 worker 初始化即 EOF。
这个 checkpoint 是失败迭代的状态，不能作接受场。

异常文本只留 runner，SHA
`22faf425e9214215b84bbc937df5cf0234e8efd68e1fe3b6c77271a88df845d6`。
已发布投影将 worker 的 `failed` 字符串压成布尔值，未保留
`lastIteration`；该 job 日志也没有输出原异常文字。因此目前不能把
这次失败具体归因为 Frenet 域、内存或原 Newton 的某一种失败。
没有运行 M24 full-H/J，更没有前缀联立、λ=1 或闭面通过。

已读原 worker/client/remesh 源分别与历史 SHA
`41a3fc113a8565dc2382966ed0dd299532a0510bee279552fb191aca3cb99f45`、
`12ff3db3867f4f4919032199e5954b830180a9b3697ed53b6feae4ebca0f86b1`、
`91686f1c9e70c36ea53357101b619830015288354d1045116a75b5a9ce47667b` 一致。
原客户端先保存失败包，再抛异常；原 worker 只在 converged 后更新接受锚。

后续应优先利用仍可找到的真实 runner 文件读取失败字符串；如果文件已失，
保留未知原因，不原样重复该失败链。新尝试可用更细的模式升阶，或者在
M8 尚未到全幅时升 M，再保最终完整 H 与全部原门；这只是新的初猜路径，
是否成功必须由实际原求解返回决定。
