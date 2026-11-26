# Run05 实际阶段 7：完整历史并集与真实初点字节指纹

日期：2026-11-26。

公开 Actions [45870334713/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45870334713) 的实际阶段7完成了已刊 e54c 纯读取入口。它直接读取本 runner 已存在的完整 JSON/NPZ 字，绑定完整来源和当前 carrier，返回完整历史地点指纹及真实初始自由向量摘要；没有重算场、根、Jacobian或几何。

实际步骤为
`pure-complete-SO3-location-and-initial-fingerprints-v2-through26-20261126-05`，
completed/0，10.791307409000183秒。完整公开依据是
[第2卷中的阶段7对象](2026-11-26-public-actions-45870334713-1-part-002.md)，
Git blob `ef8c8f3cfcdf1b0a27a6e1c068c3c2f6ed3b7883`，
实际UTF-8 24892 B。所有大原报告仅在runner由纯入口读取。

## 1. 实际来源、输出和绑定

纯源码
`read_complete_so3_location_and_initial_fingerprints.py`
的完整 SHA256 为
`e54cad5e7e78f3576412fef82701a3b276fb9af8795ca16d3e016cb9bc0382e7`，
实际源码提交
`e859da95dbe623cf3cec020d1c554d63cfb2028d`。
完整 pure 输出
`postprocess/complete-location-and-initial-fingerprints-v2-05-through26.json`
为
`ba07ed11e0516e6b2ce090990ac88103e41b61cf1ccf5e0dfada629cd9127825`，
28346 B；schema
`complete-existing-SO3-history-and-initial-point-fingerprints-v2`，
complete=true。

| 实际绑定对象 | 身份 |
|---|---|
| reference bundle | `59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f` |
| observation carrier | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| reference model | `035b6f6d19f76b2e3c8f97c4d85922734e1f63b3ea9ab2a57c23630b3c697b7e` |
| 固定 scalar profile | `e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350` |
| 固定 chart/core 数组 | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |
| mesh 数组 | `eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262` |
| reference history 文件 | `15cf439ca4ce5edbde22c5216c0ce0c3bf1ca2a0a800b28c19bd5d4026ce2143` |
| 原准确 scalar 参数 | `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` |
| warm bundle | `3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c` |

实际 M160、J923、N2048、P7377。整个入口在这些真实绑定下消费已声明五个完整输入；pending grid地址数0。future_reports_included=false，没有将尚未返回的后继当作已读。

队列路径提交为
`c0721f484afbbf693eb7cd7e8cac26996bbf158e`，
checkout提交
`696592db95155b128e40e16736927cbade1b32fa`，
所读完整队列SHA256
`d401fcb167064242eb0534c37a6557e9c776f1b7fba8d88eb7596f77697b5287`。
完整argv在该公开阶段对象逐字保留。

## 2. 真实完整 walker 集合，不只是末态 memory

e54c调用已刊完整4d9地点语义，先收完整JSON来源，再在本carrier/N解析grid地址。字面cell/u/phi身份与原walker的tuple语义保持；canonical指纹使用源码声明的准确binary64 hex编码，不做十进制取整。完整集合还包括合法的原selected/trial/SOC等地址，不能用某份报告的final memory计数替代。

| 输入次序 | 完整来源 | 本输入curvature | 本输入radius | 本输入protected | 累计并集curvature/radius |
|---|---|---:|---:|---:|---:|
| 0 | `axisymmetric-R690-reference-v2-first/locations.json` | 1250 | 208 | 18 | 1250/208 |
| 1 | `axisymmetric-so3-complete-v2-first/report.json` | 1544 | 1544 | 28 | 1544/1544 |
| 2 | `axisymmetric-so3-prior-separation-SOC-first/report.json` | 1632 | 1632 | 32 | 1632/1632 |
| 3 | `angular-unit-complete-first/report.json` | 1621 | 1621 | 29 | 1709/1709 |
| 4 | `axisymmetric-so3-integral-norm-first/report.json` | 1763 | 1763 | 36 | 1763/1763 |

表中的protected列属于各独立输入，不是尚未返回的累计protected读数。实际最终并集为curvature1763、radius1763、protected36。

| 最终完整并集指纹 | SHA256 |
|---|---|
| curvature | `80b0ee8910148da0dafbf7fbb5bfe0ea168885d061ab70ea8fe8c5ac92acd5db` |
| radius | `80b0ee8910148da0dafbf7fbb5bfe0ea168885d061ab70ea8fe8c5ac92acd5db` |
| protected | `b7496115713280dca342cdaea59d4e456e356d26f366f6990c24c4cea6a3e488` |
| combined | `bd169e75ba4d8abdf666f7f37bd95b48b72350bf3f5a818dbdc39e2daac5c22e` |

curvature与radius在本次canonical输出的摘要相同，是实际纯读取的返回；不将此事实推广到其它输入、其它运行或任意表示。这里只保存可恢复的紧凑指纹，raw_locations=false，没有把完整地址raw重新包装发布。

### 输入 0：axisymmetric-R690-reference-v2-first/locations.json

- 完整输入 SHA256：`15cf439ca4ce5edbde22c5216c0ce0c3bf1ca2a0a800b28c19bd5d4026ce2143`。
- schema：`independent-axisymmetric-SO3-literal-position-input-v1`；完整来源 SHA256：`4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`。
- 本输入 curvature 指纹：`0d18c105c0899f463979a1a99b28c7c74cc26dd3f3132ad58bae8803374ba9a8`。
- 本输入 radius 指纹：`1758d6f5c7376dacf573d8495f576e62d06277f0b3be158e7b7b444def79d471`。
- 本输入 protected 指纹：`4959a1e7725524fee90517420406f6d3c1e1d12c1ca2255967d5b6056b43872a`。
- 按声明顺序加入后的完整前缀 combined 指纹：`0f3db19a91b1c527f9a1596df2a1e8615f9348fcb43e2067b8fa695d4ab6e67e`。

### 输入 1：axisymmetric-so3-complete-v2-first/report.json

- 完整输入 SHA256：`687b343c79997b2a00dd81969a84a599cd4b81565596b6a25ecbd03788667ad2`。
- schema：`complete-independent-axisymmetric-fixed-deep-so3-meridian-QP-v1`；完整来源 SHA256：`606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9`。
- 本输入 curvature 指纹：`8f3d6b3e24cbedb3a26399a29a7c61f48f86e6ee5033c84391cf6f37ef2ee38f`。
- 本输入 radius 指纹：`8f3d6b3e24cbedb3a26399a29a7c61f48f86e6ee5033c84391cf6f37ef2ee38f`。
- 本输入 protected 指纹：`103441c7042a94ea7b878cd210e4b80ad2a800f724a7c096bba458737e41fd68`。
- 按声明顺序加入后的完整前缀 combined 指纹：`2ba7e318421e4cd338ec3c9afa16a7985aa908d90e9ca16e269cb9dbaf759e5b`。

### 输入 2：axisymmetric-so3-prior-separation-SOC-first/report.json

- 完整输入 SHA256：`caec9ab3436480294ef53202faa521aab4e542270b588f9346bb0b8bf03e2dcb`。
- schema：`complete-independent-axisymmetric-fixed-deep-so3-prior-separation-and-SOC-v1`；完整来源 SHA256：`359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d`。
- 本输入 curvature 指纹：`ba60a4d640599da6120da50c52d5aa9ca2fb91300aef6ef146833b9f85984994`。
- 本输入 radius 指纹：`ba60a4d640599da6120da50c52d5aa9ca2fb91300aef6ef146833b9f85984994`。
- 本输入 protected 指纹：`2b3f399bbe9484a4c59e6a97089802052128e0ff2691a0dcaf20f85d0998fb99`。
- 按声明顺序加入后的完整前缀 combined 指纹：`f3df8fe94376020ceea58ee95f4ff290d220929dfdde4674e36f8e47b8b20109`。

### 输入 3：angular-unit-complete-first/report.json

- 完整输入 SHA256：`de556b4bb006d6add0014d710a6032a7551ca2030d06920ad24c76e336e27db7`。
- schema：`complete-R696-angular-unit-fixed-deep-QP-v1`；完整来源 SHA256：`7b7cc0c9b27a0339debab0319c6854323dfc6c21f3e92c64946cbffc70824c7d`。
- 本输入 curvature 指纹：`66967736395cc8558c8792f082214c4c31ddbb892bc3b9706617c825fc7d8575`。
- 本输入 radius 指纹：`66967736395cc8558c8792f082214c4c31ddbb892bc3b9706617c825fc7d8575`。
- 本输入 protected 指纹：`d2f7075cf4a4712eeb386951cd7e5680583220d6e698ef97888f7f68b233422b`。
- 按声明顺序加入后的完整前缀 combined 指纹：`1f8a88f799d3385337becd6802282f80b2173592a52227f4a44df008a138c16d`。

### 输入 4：axisymmetric-so3-integral-norm-first/report.json

- 完整输入 SHA256：`7f3d9ca95e8e2010760ccd9578c467c8d00ba52ea32b5430d40f8112e31b46b1`。
- schema：`complete-independent-axisymmetric-fixed-deep-so3-meridian-QP-v1`；完整来源 SHA256：`606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9`。
- 本输入 curvature 指纹：`80b0ee8910148da0dafbf7fbb5bfe0ea168885d061ab70ea8fe8c5ac92acd5db`。
- 本输入 radius 指纹：`80b0ee8910148da0dafbf7fbb5bfe0ea168885d061ab70ea8fe8c5ac92acd5db`。
- 本输入 protected 指纹：`b7496115713280dca342cdaea59d4e456e356d26f366f6990c24c4cea6a3e488`。
- 按声明顺序加入后的完整前缀 combined 指纹：`bd169e75ba4d8abdf666f7f37bd95b48b72350bf3f5a818dbdc39e2daac5c22e`。

本次返回通过真实完整来源补齐了此前仅有计数的范围。旧03b对应fingerprint没有执行，不能给它补造一个旧集合hash，也不能因为原命令相同就宣称旧03b和05的全部地点逐字相同。后继05读取本次真实完整报告并集；后续方向新发现的地址仍要追加，而不能把through26当作永久终止边界。

## 3. 真正读取的初始自由向量

本次纯读取的完整first606初始NPZ：
`axisymmetric-so3-complete-v2-first/initial-new-field.npz`，
SHA256
`9bf940b0d826e92c698d3ade82f80fa0ed043d4bd5cf8f52feb5dc6c3f600e76`。
对应完整报告SHA256
`687b343c79997b2a00dd81969a84a599cd4b81565596b6a25ecbd03788667ad2`，
model
`9b4958325403bd74616c5875ca54f027981d2d55c9c56634dc81f8cd0d2123c7`。

纯入口实际读取了该完整初始NPZ和完整reference中的相关原字，按7f完整free-coordinate顺序重建用于hash的字节流。它读取所有原free core、全部自由omega槽与H，不调用q.initial或任何物理场求值，也不以几个参数的相同替代完整向量读取。

实际结果：

| 初始点对象 | 实际结果 |
|---|---|
| 完整自由量个数 | 1333370 |
| 完整初始free-array SHA256 | `cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3` |
| core数组 SHA256 | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |
| 完整omega数组 SHA256 | `e59a83cf7ef59b2f1b20436f065c4453248795a5e30782ff25be0dbe24406bdb` |
| H字 | `0x1.f27228dabd944p+0` |
| 实际完整初始NPZ已读取 | true |
| 实际完整reference已读取 | true |
| core与reference同字 | true |
| omega全部正零字 | true |
| H与reference同字 | true |
| initial_recomputed | false |

这里的 `cd530c…` 现在是**本次实际NPZ读取**所得摘要。它与已刊旧18字参数文件
`computations/frozen-zero-moment-Q-actual16-parameters.json`
中 `definition.trace_initial_full_point_sha256` 的完整字串相同；该旧小文件SHA256为
`df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c`。
这是已经读取的两个摘要字串的比较，不是从旧SHA重建数组。它也没有把本run变化的reference/model/profile文件身份改成旧身份，或证明所有工作scalar载体字节相同。旧4dc/44ac的完整reference守卫仍保，采用新实际reference的入口仍必须走其明示新绑定合同。

同一数学g的结论来自
[完整来源定义比较](2026-11-26-run05-actual-input-identities-and-same-mathematical-target.md)，
不是由一个初点摘要推出。此处只把原来尚未实际读取的完整初始free-array摘要责任补成真实返回。

## 4. 纯读取范围和后续责任

实际fields/J/JT/roots/scans/QP计数全部为0，summary_errors和missing_outputs均为空。没有另起field/root/数值fixture，也没有声称本次hash是几何、闭合、度量或可行性证书。

该结果为后继提供精确来源、已读初点与完整地址指纹。原报告和可再生raw仍由runner保留；大文件没有经连接器整读。下一份through30纯结果只有在其真实完整输入和source绑定返回后才能登记，不能从当前摘要提前推算。
