# R706 — 再生输入保持同一准确度量的完整来源条件

**状态：已证明（相同完整准确参数及同一来源定义下，数学g与材料图相同）；实际工作包围与数值记录按原文范围。**

本文件按根README3、8、12正式登记已有完整证明；没有重做科学计算或把旧结论算作新进展。[原完整笔记](../notes/2026-11-26-run05-actual-input-identities-and-same-mathematical-target.md)保持原字节（SHA256 `cee67928fe9f1cde846885bc47ad269e472b70c0e077a909aa2242b59079248d`）。原文中实施/运行状态以其记录时点理解；当前真实结果见[HANDOFF](../HANDOFF.md)。没有将条件界、失败或数值证据升级为所求闭族的存在证明。

日期：2026-11-26。这里登记 run `45870334713/1` 第 1–3 步的真实新返回与原 run03b 的来源对照；不把必要输入再生重复宣布为新科学进展，不把同命令、相同摘要值或 metadata 的 hash 变化冒作完整逐点再生或更换数学 g。

证据：[run05 part-001](../notes/2026-11-26-public-actions-45870334713-1-part-001.md)，读取时 Git blob `027dc5bf0146667fa8d7cdb7a4897d6ac4679ac7`；原对照为 [03b part-001](../notes/2026-11-26-public-actions-45820592817-1-part-001.md) 的实际第 2、3 条。

## 1. 新准备器和载体确已实际返回

run05 warm 130.617365684 s。完整 warm bundle SHA256 为
`3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c`，
与原03b实际字节相同；不能据此把所有其他输出也称相同。

第 2 步完整 4e reference 准备器 308.66245129099997 s、completed/0；source SHA256
`4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`，
实际源提交 `be84fce832419adb10f0b714633a254943f88ade`。科学 report 为 29,795 bytes，SHA256
`9a97bb6a615618c0be5e5e87f2cc059e292e548451ca23ccc4889a8b9cb3f846`。

| 项目 | 原03b | Run05 实际 |
|---|---|---|
| reference bundle | `0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1` | `59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f` |
| observation carrier | `b0257d9e03da36a422eab4e424942d38ccf817ac40ceb3b42be4378b1260966f` | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| node report | `9066125cc62b2ad911704e739cf8646e502f44b26fd42df532ff608418d35b26` | `2ec37435284048be6fbcde71c03d462692bfc708103ef553a35c570d51b3ee3c` |
| scalar 文件 | `d35379dc7a7f83f48acc601116f94049a00f66e4eb0a11b15fba00331e27f830` | `0ee422aef7efcf8f307a3bd4c58f7f1bffd9bb581d889b1ce509167253d7a535` |
| reference model identity | `3f62a03da637495af340f8da6ac31f0d7993fa6e769f7bcab1ed45b8dc7f19b2` | `035b6f6d19f76b2e3c8f97c4d85922734e1f63b3ea9ab2a57c23630b3c697b7e` |
| scalar profile identity | `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb` | `e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350` |

实际 M160/J923/N2048/P7377 同；new_height 的 binary64 数值同为 1.9470544370684175，warm_height 同为 1.9479520470229232，radius carrier hex 同为 `0x1.2124d67c6a7adp-1`。

不能说所有变化都“只有元数据”：时间限内标量积分叶从 1448 变为 2397，准确包围宽度实变，radius_error 从 2.3765777896593284e−13 变为 2.363596792320704e−13；两次 requested scalar tolerance 都没有达到，但均完整包含无限尾。工作包围变窄或其他数值误差变化不等于数学积分定义被换掉。

## 2. 相同数学 scalar law 的完整来源理由

两个实际准备报告都返回原 scalar 参数的 canonical identity：
`e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`。

4e `scalar_parameters(data)` 明确包含 `analytic_extension_origin` 和完整 `fixed_scalar_profile.geometry`。完整 a1ed FullHold 构造器只从输入数据读取这两部分：全部 knots 的 s/a/ap/app、initial_law 的 length/velocity/k0 以及 analytic origin；它不把报告路径、执行时间或整个压缩 JSON 的 SHA 当数值参数。它们经原整数/有理源、固定 Hold 常数和相同函数公式定义同一前缀/延续/Hold。两次完整 a1ed/babd/ed6 源绑定相同。

完整 e091 DeepValleyTail 的数学 beta/cutoff/radial integral 公式相同，width 和 kappa 来源相同；其 `definition.original_input` 另记录 scalar 文件及三个来源 SHA。scalar 文件 SHA 变动会改变整个 profile identity，即使被 FullHold 真正消费的准确参数保持相同。该字段是输入来源身份，不是新的 beta(s) 项。自适应积分叶/误差宽度不进入精确 law 的定义。

相同完整 warm bundle 又固定相同初始 core 系数与冻结材料图，故两个输入定义相同的
$$
g=ds^2+a_{\mathrm{deep}}(s)^2\,d\theta_0^2.
$$
这只是在已有完整源/实际参数身份内证明数学定义同一；不宣称两次观测数组或算术包围逐位相同，更不证明该 g 已有所求非平凡等距闭族。新输入 binder 不得把 profile hash 的变化当清除同目标永久点责任的理由。旧 strict identity guard 也不能被伪造：新实际 model/reference/profile 确需显式诚实绑定。

## 3. 新实际首方向与原摘要的对照

第 3 步 source `606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9`，实际提交 `606a2c638f9baf633f287340686d558ebd5b7342`，485.28528193700004 s、completed/0。新 base model：
`9b4958325403bd74616c5875ca54f027981d2d55c9c56634dc81f8cd0d2123c7`。

新科学 report SHA256
`687b343c79997b2a00dd81969a84a599cd4b81565596b6a25ecbd03788667ad2`，
12,489,618 bytes；新 initial NPZ
`9bf940b0d826e92c698d3ade82f80fa0ed043d4bd5cf8f52feb5dc6c3f600e76`；
新 final NPZ
`c21240788e0a342a4cea6378b6e9b93b83cb72750b41bdcb875f83ba81e947f6`。
两 NPZ 均 10,720,284 bytes，旧对应 NPZ 为 10,720,288 bytes。它们含完整 model/source/provenance 字串，NPZ bytes 变化不能直接推出自由点变动。

初末已公开数值逐值对照：

| 实际量 | 两个 run 的对应摘要值 |
|---|---:|
| 初 Phi | 213.89131075534186 |
| 末 Phi | 212.14818770844644 |
| 初 max relative Gram | .5170375580125983 |
| 末 max relative Gram | .5154401838413587 |
| 末有限 K product | .749220230610006 |
| 末最大物理 g | −.024554299879619434 |
| 末曲率 / 半径地址数 | 1283 / 262 |
| 末 μ | .01 |
| 实际 metric 接受 / restoration 方向 | 1 / 0 |

其余已公开的五类幅度值、root residual/rho、调用计数、全点/双支标志也逐值相同；有变化的是来源/父/模型/NPZ身份、setup/总时间与 RSS。这样的紧凑一致性仍不能替代完整向量或地址集合的实际 hash。

7f 的初自由点构造是固定 core 的自由后缀、全 literal zero omega 和 H。由同一完整 warm core 与同一 binary64 H，源码上可推出两次此构造的原自由字相同；原03b相应整点 hash 为 cd530。**当前 run05 compact 未独立返回该自由向量的 array_sha**，故本段明确是绑定源码的构造推论，不冒称已经从新初始 NPZ 重新读取并实算了那个 hash。末向量没有仅凭摘要推为相同。

## 4. 地点责任与纯 fingerprint

准备器返回相同地址计数 1250/208/protected18、0 pending、1782 occurrences，但 `locations.json` 的完整文件 SHA 新为
`15cf439ca4ce5edbde22c5216c0ce0c3bf1ca2a0a800b28c19bd5d4026ce2143`，
旧为 18fcc...；该文件也含新的 carrier/reference/provenance。不能仅由总文件 hash 不同或计数相同判定地址三集合不同/相同。

完整纯 fingerprint 入口已准备：严格绑定当前实际 4e preparation、现有 carrier 和完整 driver 源，直接调用原 4d9 walker，对完整报告的全部记录地址、protected 标志和实际 grid 解码作 canonical hex/hash。它不读 F/J、不求根、不写地点表。计划在 run05 实际26与30后各作一次新纯读取，保每份来源和每个前缀的地址身份。

原03b该入口没有运行，旧实际 canonical 地址 hash 不存在；不得在新摘要中补造。完整3/17/21/26/30再生链仍承担同目标历史责任，新报告若再产生地点就持续保留。初根失败28/34/36的空 walker 贡献另由完整来源结构证明，不能把该特殊结论扩张到有真实几何试步的报告。
