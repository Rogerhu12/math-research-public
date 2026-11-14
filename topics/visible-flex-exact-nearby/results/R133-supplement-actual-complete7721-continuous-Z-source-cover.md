# R133 补充：全 7721 格连续方向 Z 源的实际公开验收

## 1. 完成对象和真实运行

公开 Actions [43613560173](https://github.com/Rogerhu12/math-research-public/actions/runs/43613560173) 的 plan、四个互斥 range 和 finish 全部成功。finish 的六项门全部通过，实际 child 返回 0，child 用时 10.000715529 秒；native 记录最终消费算术用时 3.748047709 秒。

本结论针对固定物理 $\eta_0$、原 $\nu$，即仿射参数偏移零。中心是 ac1 的完整连续 M32 修补，方向是完整 193 槽连续 $Z$。下文是其完整已知源上界，尚未施加 Green 逆；均值补偿方向 $q^*$ 没有改名为 $Z$。

| 数学身份 | SHA256 |
| --- | --- |
| 连续中心定义 | 440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47 |
| 原完整响应 trial | ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6 |
| 同一连续 $Z$ 定义 | 6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04 |

完整覆盖保留原 7721 个真实闭区间，首点为 0、末点为 $25/8$。常数 Fourier 槽按原归一化圆周测度保留真实 signed even mean；第一分量为 odd。完整输出、低 193 槽及已知高输出 $97\le j\le160$ 分别记录，未知高输入反馈没有置零。

## 2. 实际完整范数

下表均为从有向 native 向外取整的严格上界。范数为真实径向测度与归一化圆周测度上的普通两分量 $L^2_rL^2_\varphi$。低 193 槽含独立 even mean。各列是独立合法上界，不要求它们的平方和等于 full 列。

| 径向范围 | 完整源 | low193 | 已知 high97–160 |
| --- | ---: | ---: | ---: |
| $[0,25/8]$ | $2.725862\times10^{-6}$ | $2.723698\times10^{-6}$ | $1.961163\times10^{-6}$ |
| $[0,9/10]$ | $1.574741\times10^{-6}$ | $1.570993\times10^{-6}$ | $1.155273\times10^{-6}$ |
| $[0,R_{\rm phase}]$ | $3.125876\times10^{-7}$ | $2.931414\times10^{-7}$ | $2.308005\times10^{-7}$ |

这里
$$
R_{\rm phase}=\frac{2383968743003}{10000000000000}.
$$
此上端只对应当前固定背景的已证根包络。改变 $\nu$ 或非线性背景时，不能直接转授这个积分窗。

同一 native 还给出 $L^\infty_rL^2_\varphi$ 上界：全段完整源与 low193 均小于 $1.257182\times10^{-5}$，已知 high 小于 $9.133245\times10^{-6}$；固定负区窗完整源小于 $4.800009\times10^{-6}$，low193 小于 $4.785841\times10^{-6}$，已知 high 小于 $1.864706\times10^{-6}$。逐格上界完整保存在 native，后续 Green 消费必须继续使用真实逐格分布。

## 3. 没有重复已成数学行

原 plan 来自运行 43612904296：数学 child 已返回 0，七项门通过并生成完整 native，随后摘要路径拼接发生 TypeError，导致发布阶段失败。v2 实际核验原数学输出并逐字节复用 plan，SHA256 保持
`26a488b4347e0e30106e67dcd18b54e211dba6adecd7d2c029a4dc6ba097d95a`。旧失败过程保留，没有把发布失败说成数学失败。

四个 range 实际新行数分别为 288、289、285、285，总计 1147；它们覆盖 $[597,1753)$ 中尚未完成的紧支撑源行，并排除原 pilot 已成功的九行。原 pilot 的全部十四行及已成功 fixed-$\eta$ 子格继续消费。finish 的准确并集门检查原行身份、四个实际成功过程、相同 plan 和同一冻结源码，无重复行。

新计算只在既有完整 scalar jets 上采用原精确 Fraction bump 展开和有向余项处理；新 target-provider 调用为零，旧候选、目标系数、响应和 mean 流重建为零。其他原行通过真实 nonmean 残差与 signed mean 的正交平方合并，再加完整中心及方向修补费用，得到合法全 $Z$ 基线。整个区间仍在每次积分时检查到 $25/8$，没有把紧支撑范围当作全部 body。

## 4. 原件与可读取证据

验收目录为：

`notes/complete_Z_source_v2_ci/run-43613560173-1-complete-Z-sources-finish/`

| 原件 | SHA256 |
| --- | --- |
| native/complete7721-mixed-Z-sources.json.gz | 365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e |
| process.json（本次读取的仓库快照） | 0cc2e8f876261c0fa86c0547b1400d47ad71759f43c7001b6359049827017f48 |
| evidence/complete-Z-source-finish-summary.json | e1ae6bd3ae8b9f04297fb2c9664d249c15ffe9366d15a4504444f06f08b727ac |
| 冻结科学源 | 90c90fb1b21806e803e61d5f850b1d8057fcadc577452d3454b05348500a697f |
| v2 worker | c0654466f3451b38f469c00f7286a0f450db0bd52cc62973f72838ac1528e411 |
| v2 输入 manifest | 05178f530e1fbc9be1016faa52cb9f5773e199915ab7bfcae1ad187609e7e0ac |

完整 native 为 2657471 字节，保留全部数学行；小摘要为 21085 字节。artifact 名为
`visible-exact-complete-Z-v2-finish-43613560173-1`。
仓库 process 与 artifact process 的 checkpoint 出版快照可能不同；后续消费者必须按实际下载的原 process 身份核对，不能猜测二者 SHA 相同。

数学合同见
[完整混合源合同](../notes/2026-11-14-R133-complete-mixed-Z-source-cover-contract.md)，
科学源为
[complete_mixed_Z_source_cover](../scripts/fourfold_codazzi_complete_mixed_Z_source_cover.py)。
公开过程中执行了真实 pull 和 README 差异检查；最后记录读取提交
`e142a68e2d758720f708d78ced44289dab3efc91`，两份 README 均无变更。

## 5. 结论的使用范围

本结论付清同一连续中心、同一连续 $Z$ 的完整已知 body 源。它可直接送入原连续 Green ports 的低 193 槽源通道，并以独立已知 high 通道保留高输出。后续仍须消费同一个 $Z$ 的真实腰迹与完整帽 cut 来源、全部投影跳、独立 mean，以及未知高输入反馈。这里没有证明真 PDE 响应误差小于 $1/200$，也没有把有限 193 态逆升级为完整无限维逆。
