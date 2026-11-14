# 实际共同 prefix 的精确桥坐标轴点下界：完整独立审查

审者：`/root/independent_audit`，会话 `Astra-visible-flex-78718bd0`。本审者没有参与本轮主候选的构造、初猜、节点预算、频率、优化或见证点选择；这里审查作者已经冻结的程序、实际生产身份和精确标量证书。审者自己的原公开种子主计算仍由另一个独占观察单元持有，其运行状态不用于本证明。

**结论：完整审查通过，但严格式须使用订正后的安全十进有理数。** 对本轮实际共同 prefix 和该桥证书所定义的最终目标，在未被接缝修正的见证点有

\[
\left\|g^{-1/2}(F_*^*e-g)g^{-1/2}\right\|_{\rm op}
>7.74147506471938\times10^{-8}>2\times10^{-9}.
\]

这给出任何保留该 prefix 和该目标的闭扩张不能通过原 metric 门的严格证据。它不声称已经构造了完整闭曲面，不拒绝其它 prefix 或其它频率，也不把局部误差转成总体不可能性定理。正文原先把一个向下 binary64 端点的最短十进显示串直接用于严格式；该显示串作为精确十进有理数时略高于整个精确区间。作者已只订正文稿，并保持程序与真实报告冻结。此处完整记录该订正，不覆盖失败或原运行历史。

## 1. 对象、冻结身份与阅读范围

本轮审查全文读了以下新增正文与源程序、v1 到 v2 的完整差异，以及实际生产观察器和原精确桥证明的相关完整流程；既有 lossless reader、native-node 精确求值和共同修正定义仍在已经完成的完整独审范围内。本审查没有以局部抽查替代新程序全文审查，也没有把读源码当作实际执行。

| 对象 | bytes | SHA-256 |
|---|---:|---|
| 作者订正后正文 `2026-11-10-78718-numerical-common-axis-lower-v2.md` | 8,708 | `fd31879da8d9858df6ab0014d5c63a58fa76a189550ad394207780dd16480e67` |
| 新程序 `78718-prefix-common-axis-lower-v2.py` | 12,254 | `8bc77d7c14b68d4c1f13c5c595f227860f4cdefd433afac7606a536293a07e11` |
| 作者实际报告 `2026-11-10-78718-numerical-common-axis-lower-02.json` | 20,806 | `50c1633e3d42102d0b77f50480e5c81b11c9d9f25d995ec2452a9458b7deebc7` |
| 作者实际观察 `2026-11-10-78718-numerical-common-axis-lower-v2-observed.json` | 3,097 | `b59b011a72bab91751118e50e7c7813c675dcc33821dc8ad1b75f96eeec8c7db` |
| 审者独跑报告 `2026-11-10-78718-audit-common-axis-lower-02.json` | 20,806 | `6f13b5afc20b6ed4fdfa58d73783df3ba2512ac37e7adfb0a905851844420d90` |
| 审者标量及身份检查 `2026-11-10-78718-audit-common-axis-lower-check-01.json` | 1,370 | `64aaa071262c47211989f82b3574df7350412d797126e1aff137bb606ca7c96e` |

路径中没有 `scripts/` 的项目均在本题 `notes/`；新程序在本题 `scripts/`。原正文阅读版本为 8,297 B、SHA `ac91abf3d80d89018b1bc3b817f09f48ac0dcc3911d8c6003b7f7632c4b5e078`，实际全文阅读回执 `736384`；订正稿全文阅读 `2bdb6c`。本轮主要新源全文阅读回执为 `ea3a9f`、`e0e7e6`，v1/v2 全差异为 `d7f5ae`，实际生产观察器全文为 `d7115f`。原桥算术与证明流程的全文核对回执包括 `a25ee5`、`eedfd5`。这些是阅读记录，实际独立程序执行见第 8 节。

依赖的完整旧轴点审稿是 [audit-prefix-axis-lower-v1](2026-11-10-78718-audit-prefix-axis-lower-v1.md)，SHA `5658a242b85b0671209e84a2860dbb0eff2e687c7c3b022f490c5027b73b1f21`。那里已支付 finite shared-jet Hermite 的精确节点导数、Fourier 布局、对称轴角向项消失、lossless storage 和 common-cut 修正支撑的全部数学与源码。这里补付的是本轮实际生产身份、该实际桥的尺度和最终目标转移。

## 2. 真实生产链不能由旧图或未来计划替代

本轮实际目录为 `notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/`。必要对象为：

| 文件 | SHA-256 |
|---|---|
| `prefix-base.json` | `11cd5569b3c2218591a757aea966f9aa25963fa1a3ec69fbb0b6729cb141a42d` |
| `prefix-target.json` | `dbfb5c348a6921b078c1ee25c9aa5874856de303afd11b1e6277ac1eebdbbd8c` |
| `prefix-base-metric.json` | `b076c6c052a00d72d201ca9c76a3a5a724e9dc70350437cb14fa90d430f0c48a` |
| `tail-manifest.json` | `207a40b90ba65e2297c24c48b8d5848d3e18e6ed62ca77024ce71d7b3f68558b` |
| `tail-radial.json` | `de494da5a60a18f5e3735ef7a5a872ee51169923df2b678d04709622557175a3` |
| `tail-collar-check.json` | `93e0aaa0742a5110f936345997609460e8aa8f166a66f9418815370fc1306d85` |
| `bridge.json` | `da2c5f8cdfcba8aa68fb535ac981989cb041fab768d674f9037d570f4aa56b47` |
| `closed-map.json` | `6cd427ec5b4642a08ac64e9a1afbc5d4692ad5b449d305ffb10725f606e1eb83` |

本轮 base 的来源 CP 为 `4776c4c251c4bc6fdadda56aaed78f6fc02175483c5ad3a6fb3cf0359a49cd6a`；尾输入是该成功运行自己的 `_tail_0003.json.gz`，SHA `c253eedbf3a4711ad79740d655262a5991e803e38dab2b4a248c386db9efcb7d`。它们不是审者正在独跑的原公开种子，也不是旧 M8/M12 图。

作者实际生产的五个自然末回执依次是：tail-export `9ace36`、tail-radial `67348b`、tail-collar `a81eb2`、bridge `024ce0`、common-cut `a4bdf6`，均 exit 0。其固定观察文件保存实际 invocation、工具返回、actor、输入、输出和来源身份。审者在 `32aec7` 核对了这五份观察中的 complete 状态、stage、actor、真实工具末回执、exit、没有仍运行 session、expected output 存在，以及 recorder/source/invocation/plan 的当前 bytes/SHA 一致性。

最后 common-cut 观察 SHA 为 `aaad3e13dbbfe579ffab8954f6c60fd2c619b448cafdea52b0f90b4eb9287750`，闭合 42 个实际文件；新检查器在实际重放时重新读取并散列每个文件。审者没有声称自己执行了这五个 producer：这是已保存且逐项核清的真实作者生产证据。审者亲手执行的是第 8 节的完整新轴点检查器，它包含原桥证明重放、当前定义上的点值重算和生产闭包重核。

源代码明确要求 common map 的表示、implementation hash、tail reader hash、C2 by definition 与已有共同构造相符；要求 supplied geometry、tail、bridge 与 common metadata 中的路径解析一致，并比较对应散列。base、target、metric certificate、tail、bridge 的反向引用也逐项闭合。这防止把某次真实桥的尺度套给另一个 prefix，或用旧图的成功误差证书替代本图。

## 3. native-node 的精确点值为何是当前实际共同函数的点值

已有有限图将保存的 binary64 每个数解释为对应 dyadic rational；lossless storage 只改变容器，并保持字节。共享节点 Hermite 插值的端点一阶导数恰等于保存的一阶 jet，这不依赖浮点插值在端点附近是否接近。Fourier 表达式在 \(\psi=\pi/3\) 有 \(\sin(3m\psi)=0\)、\(\cos(3m\psi)=(-1)^m\)。径向导数的角向分量因此为零，故精确

\[
E=|\partial_\sigma F_0|^2=R_\sigma^2+Z_\sigma^2
\]

只需对有限 dyadic 系数作带符号求和、平方、加法。这里 \(\sigma\) 是旧冻结径向坐标。

当前检查器不把先前报告的近似显示数作为最终结论：它读取**当前共同定义所引用的同一个 defining base**，调用已审精确节点求值过程，重新得到见证 node 1518 的有理坐标和完整有理 \(E\)，再逐字与先前点报告的 exact 字段比对。坐标为

\[
\sigma_{1518}=\frac{2474546589463719}{9007199254740992},\qquad E>1.
\]

本轮 native node 总数 6599，defining base 是 24 个 Cartesian 三倍频模，common metadata 将表示扩到 64 模。扩基是补零；旧系数和由它们定义的函数不变。程序要求 base `ell=0`、mirror 开启、node count 一致和新模数不小于 base，以便应用原共用定义。mirror 的特定端点二阶 jet 处理不影响这个内部节点。

实际 common-cut 用原 binary64 width `.15`，原样计算
\(\operatorname{searchsorted}(mesh,mesh[-1]-.15)\)，得到 start node 6124。被冻结的 source 仅在从该节点开始的 spans 增加 quintic Fourier 修正。因此在 node 1518 的左右邻域，当前共同函数和旧 defining base 一致，其一阶导数也完全一致；这不是“差异很小”的估计。1518 严格小于 6124，程序也检查该整数关系以及内部节点范围。共同 producer 已实际产生 manifest 并构造、核查其端点区间数组，所以这里适用于一个已经确定的共同 prefix 定义，不以未来 producer 成功为条件。

## 4. 原精确桥完整重放与 v1 的真实失败

原已审桥程序是 `db6f-root-exact-bridge.py`，SHA `f5d10784f58fa5008220354665de710ab4991b795f1b902e26a70ca44f382fd1`。它以 Decimal 近似定位一个小 bracket，但 Decimal 仅提供种子。接受门由 Fraction 区间和有理余项支付：有向区间加乘除、带符号幂、外向 dyadic hull、平方根整数夹逼、Machin 恒等式的交错 arctan 余项、相位的有限 Bernstein 分段、sin Taylor 余项和端点 gap 符号均有明确界。长度处在 \((3/5,7/10)\)，所需相位范围和导数单调性由原门给出，原唯一 root/metric transfer 仍按已经完成的 R21 审查范围接受。

v1 的 SHA 是 `4f656d8d57b8d90b7d02556ced3e09cc002f18b12abd9297d2df08f043bd1550`。其真实 `263567` exit 1，没有成功报告。原因不是数学桥失去根：原程序在内部 bracket 端点算 gap，然后将 bracket 外向取 256-bit dyadic hull 输出。v1 又在重新解析的**外向端点**计算 gap，并错误要求这次 gap 编码与原**内部端点** gap 编码相等。两个不同端点没有这种相等义务；失败必须保留。

v2 的完整文本差异只修这个重放办法与相应版本字段：它不修改原桥源，不删原桥符号门，也不把两个不等的 interval 草率视为相等。它在临时目录里以同一 actual geometry、target、metric certificate、tail 参数完整调用原桥 `main()`，随后将新生成的整个 certificate 与实际 `bridge.json` 逐字段相等比较。`sys.argv` 在 finally 中恢复，stdout 被捕获而不把证书送入对话；临时结果仅为小文件。只有完整原桥重放和整份证书比同成功，才读取实际证书的尺度区间。

这次独立执行确实运行了上述原桥证明，不能表述为“0 root 计算”。正确范围是 0 BVP、0 DN、0 tail solve、0 exporter、0 geometry producer；存在一次完整的原有理桥证书重放和有限精确点值求值。`db6f_tail_integrated.py`、原节点检查器、production recorder 与旧六个 storage/reader/common/supplier 依赖一共 10 个唯一源码绑定，均按现存字节验证。

## 5. 尺度转移和 Rayleigh quotient 的完整推导

令旧冻结总长为 \(S_0\)，该实际唯一精确桥定义的总长为 \(S_*\)，并令

\[
\lambda=S_0/S_*>0,\qquad \sigma=\lambda s.
\]

最终图在 prefix 上的定义为
\(F_*(s,\psi)=F_0(\lambda s,\psi)\)。链式法则给出

\[
\partial_sF_* = \lambda\,\partial_\sigma F_0,
\qquad |\partial_sF_*|^2=\lambda^2 E.
\]

所以旧数 \(E-1\) 不能不带尺度地移交给最终目标。这里不借旧图的 \(\lambda\)，而使用本轮 actual bridge 经完整重放确认的 \([\lambda_-,\lambda_+]\)。正比例变换同时将 witness 和 correction start 除以 \(\lambda\)，不改变两者的严格先后关系。

最终目标按已审弧长定义为 \(g=ds^2+a_*(s)^2d\theta^2\)，旧角 chart 是

\[
\theta=\psi-\frac{e(\sigma)}3\sin(3\psi).
\]

固定 \(\psi=\pi/3\) 时，\(\sin(3\psi)=0\)，因而
\(\partial_s\theta=-\lambda e'(\lambda s)\sin(3\psi)/3=0\)。无论 \(e'\) 和 \(a_*\) 的值如何，这个径向向量 \(v=\partial_s\) 恰有 \(g(v,v)=1\)。目标正定性和 chart 有效性已在先前完整点证书及本轮输入身份中支付，不以零角导数代替整个 chart 门。

对任意正定 \(g\) 与对称二次型 \(h=F_*^*e-g\)，取 \(w=g^{1/2}v\)，有

\[
\frac{|h(v,v)|}{g(v,v)}
=\frac{|w^Tg^{-1/2}hg^{-1/2}w|}{|w|^2}
\le\|g^{-1/2}hg^{-1/2}\|_{\rm op}.
\]

因此此处相对 metric 误差至少为 \(|\lambda^2E-1|\)。这是一个方向的严格下界，无须计算混合项、另一个特征值或全域上界。用一个点否决统一上界是充分的；它不能推出整个图的其他几何性质。

## 6. 精确有理区间和十进显示订正

实际证书中的 `arclength_rescale.lo/hi` 是外向 dyadic 有理数。程序以 Fraction 精确解析，而不是使用其 `display` 浮点数。由于 \(E>0\) 且 \(0<\lambda_-\le\lambda_+\)，平方在该范围单调，故

\[
L=\lambda_-^2E-1\le\lambda^2E-1
\le U=\lambda_+^2E-1.
\]

本例精确验证 \(0<L\le U\)。审者另以展开式

\[
\lambda^2E-1=(E-1)+(\lambda-1)(\lambda+1)E
\]

重新核对报告中完整 exact 分数分别等于两端的值，未通过 approximate lambda 或打印小数重算。该 actual lambda 约为 \(1+3.62\times10^{-16}\)，只是说明尺度很小；严格证明用的是完整有理端点。

程序将 \(L\) 转成 binary64 后，用 Fraction 检查并向下调整 `lower_display`；所以该**binary64 数本身**确实不大于 \(L\)。但是 shortest round-trip 字符串不是该 binary64 的完整十进展开。实际 `32aec7`、`ab9c57` 及再次 `66f7e3` 检验显示

\[
\operatorname{Fraction.from\_float}(\texttt{lower\_display})\le L\le U
<\operatorname{Fraction}(\texttt{'7.741475064719386e-8'}).
\]

因此不能把最后这个显示串直接放在严格实数不等式右侧声称 \(\ge\)。该缺口只在正文显示，不在 exact interval 或否决原门的计算。订正后的安全数为

\[
q=7.74147506471938\times10^{-8}
=\frac{387073753235969}{5000000000000000000000}.
\]

完整 Fraction 比较给出

\[
\frac1{500000000}=2\times10^{-9}<q<L.
\]

将这个严格小于 \(L\) 的有理数代入第 5 节，得到首页的严格 \(>q\) 结论。作者的正文订正为 `fd31879d…`，精确说明 binary64 与 round-trip 十进串的区别；冻结 v2 源与两份真实报告均没有被编辑。旧 frozen-target 点证书所用十进下界经另核仍在旧 exact 下界以内，不需要追溯修改旧审稿。

## 7. 新程序所有接受门的范围

按执行顺序全文核对如下。

1. 输出路径必须新建；四个直接 source pin 与原节点程序的六个依赖 pin 均验证。storage 读取器验证当前 payload 的实际字节，而不是只看 JSON 声称的散列。
2. common representation、implementation、tail reader、C2 定义、base/mirror/ell/node/mode 关系以及当前 geometry/target/metric/tail/bridge 的路径和哈希链逐项检查。
3. 原桥来源与 unique-root 成功字段必须存在，并完整重放原 proof 后逐字段比较整份实际证书，才接受最终弧长尺度。
4. common-cut 观察必须 complete、正确 actor/stage、具有真实末工具返回与 exit 0、实际 expected outputs；检查器重散列其 42 个闭合文件。审者另核其 invocation/plan/recorder 的实际来源，不将日志静默或文件存在当成自然退出。
5. 核 base 的真实 CP 和 tail input 身份；当前 payload/mesh 的有限性、shape、严格递增与 native node 关系保持。按原 `.15` width 重新得到实际 start，并要求见证点严格位于修正前的内部节点。
6. 在当前 defining base 重新求 \(E\)，比同 exact coordinate、exact point value，证明零填充和支撑外导数不变。以真实 \(\lambda\) 作 Fraction 区间转移，验证正性、原预算超越与有向 binary64 显示。
7. 报告保存完整输入及源身份和明确 scope；末尾再核当前 source/input bytes/SHA。失败不会生成一份虚构成功结果，也没有启动任何曲面优化。

这些门恰足以认证本次局部 metric 下界。它们不包含整个曲面的 reach、闭合、嵌入、全时间、可见幅度或无限尾证明，因此不会冒用作完成题目的总证书。独立入口和观察的真实性仍属于本次保存的实际记录；并非声称任意外来 JSON 单凭相同字段就能证明外部事件。

## 8. 审者实际完整重放及复核

审者用 primary Python，在本题目录执行作者原样 CLI，只把 `--out` 换成独有的新路径。实际启动工具 **`2c3562`** 返回 **session `59662`**，随后实际末工具 **`966f6a` 自然 exit 0**。这是一次实际完成的运行，不是计划、后台存活推测或源码读审。

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-prefix-common-axis-lower-v2.py \
  --common-map notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/closed-map.json \
  --geometry notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json \
  --target notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-target.json \
  --metric-certificate notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base-metric.json \
  --tail-manifest notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/tail-manifest.json \
  --bridge notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/bridge.json \
  --point-report notes/2026-11-10-78718-numerical-prefix-axis-lower-01.json \
  --common-observation notes/2026-11-10-78718-production-storage-common-cut-01-observed-exit.json \
  --out notes/2026-11-10-78718-audit-common-axis-lower-02.json
```

状态为 `ACTUAL_COMMON_PREFIX_EXCEEDS_ORIGINAL_2E_MINUS_9`。独立报告与作者报告的递归逐字段比较在 `907cef` 得到**仅 `/seconds` 不同**；全部数学字段、源绑定、输入绑定和 scope 相同。该工具同时重新核对正文、源及两份报告大小和散列。

实际 `66f7e3` 自然 exit 0 另核当前 **10 个源绑定、48 个输入绑定**全都与独立报告相等，并以 Fraction 验证 **14 项**独立列出的标量关系：正尺度、正 \(E\)、展开式所得两端、区间正序、binary64 两端外向、旧显示十进串在整个区间上方、安全有理数严格小于下界且大于预算、见证点在支撑前、完整桥重放标记及没有曲面 solver/producer 调用。报告保存为第 1 节的小型 `audit-common-axis-lower-check-01.json`。这些有限补核与全文数学推导共同使用，不把检查数量当作证明完整性的替代。

审查过程中没有输出候选数组，没有将数据文件经 GitHub 集成传输，没有生成 PDF，没有改变生产源、旧失败记录或主求解参数。终端同步后实际 `f19e21` 对两份 README 做 diff，均无变化。

## 9. 可正式采纳的准确范围

本轮共同 prefix 的身份已经实际落地；见证点在共同修正支撑外；最终目标的实际 \(\lambda\) 已经原桥全证明重放；因此不是“若将来 bridge/common-cut 成功”的条件证据。其严格结论是首页给出的一个实际点相对 metric 下界，以及对保留这一个 prefix/目标的任意闭扩张的原门否决。

该结论不会被进一步收紧这同一个有限函数的径向残差或上界报告推翻，因为下界取自当前定义的精确节点导数。改变函数可以改变这个结论的适用对象，但如何改变候选、选择频率或预算不属于独立审者角色。原题是否存在合格曲面仍未由此解决。本文件通过的是一个新的已核中间模块，主任务继续。
