# R133：完整 5970 个真实接口的已缓存正 Green 冲量响应

## 实际公开运行与范围

公开 Actions [run 43649423561](https://github.com/Rogerhu12/math-research-public/actions/runs/43649423561) 已成功，实际数学子进程退出码为 0，11 个科学门全部通过。数学用时 123.37206419700001 秒，子进程用时 130.00390503900002 秒。本次只消费既成完整 finite193 Green 与 ordinary-$L^2$ 核；新增 6391 个局部齐次上界、两次完整标量扫和 5970 个单接口增益，**没有新 target、frame、旧端口、矩阵或标量指数、Lyapunov Gram 积分计算**。

这给后续矩阵 Green 后验校正中的真实状态跳提供逐接口增益。它没有把四格同一传播子的矩阵 Gram 扩为完整矩阵 Green，也没有证明未知无限高块逆、完整 PDE 参数响应或最终 Schur 门。

## 固定输入和实际证据

固定数学源为 scripts/fourfold_codazzi_finite193_cached_interface_impulse_gains.py，SHA256
`12e40b3849f4c1f29b1c0da0a52825afd710ab4cb70e09b539760d6672295439`。
CI 源 SHA256 为 `f7def106a57225f5a456f37da90df73947b3eb57c89dafa280592f170c983a69`，
101 件输入 manifest SHA256 为
`75b9039039a663a5fb8aad5a7f719e5fcea9edf648096441bc0777e25240a44c`；原 97 件数学输入没有变化。

实际旧输入保留其原 artifact 过程字节：

| 原输入 | SHA256 |
|---|---|
| 完整有限193 Green native | fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6 |
| 原 Green artifact process | 297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c |
| 完整 ordinary-$L^2$ kernel native | ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448 |
| 原 kernel artifact process | 641c0ca655a9f0ac7c49a30c4b5fd44a4b79552d7c8f8f4533f086d6d2f88800 |

新输出目录为
notes/finite193_cached_interface_impulse_ci/run-43649423561-1-all5970-cached-interface-impulse-gains/。

| 输出 | 字节 | SHA256 |
|---|---:|---|
| native/complete-all5970-cached-interface-impulse-gains.json.gz | 14168739 | fbba350708fb89366272641433e9c2899c4ec04027616650b4317969105bcd37 |
| process.json（公开仓库快照） | 8423 | b55c2df02439b910c1e6e46fb78c2391ca135138421e2f05ee05a14dcb5de468 |
| evidence/complete-all5970-interface-impulse-summary.json | 3828 | 990aaa1c6412af3de454eaf7ec248257eaa7fb390b155daab72a609c43c82f17 |
| evidence/selected-actual-interface-impulse-rows.json | 9030 | 18a9b3a1d24920d0a6d6f4e9ac625ec24402c4d997941db52b9a5221c196e3d9 |

完整 native 已按原字节拆成 8 份保存，逻辑文件名、整体 SHA 和分片 SHA 均在同目录 lossless manifest 中。公开 artifact 14135173447 的实际压缩包大小为 13683038 字节；本结论仅读取上述小文本和 artifact 元信息，未经连接器搬运二进制。

## 单接口增益的数学单位

原加权状态为 $y=R(r)h$，原反射类的全部 193 槽及独立 even mean 保留。对原事件 $i$ 的真实跳 $j_i=y(r_i+)-y(r_i-)$，输出采用归一化圆周的 ordinary pair 范数。每个保存的 $g_i$ 满足

$$
\|G_{\rm finite}(0,0,0,j_i)\|_{L^2_r L^2_\phi}
\le g_i\,\|j_i\|_{\ell^2}.
$$

输入已经是加权状态跳，不能再次乘 $R$。全内段为 $[0,9/10]$，相位所需固定负窗采用原严格有理上端

$$
r_{\rm ph}=\frac{2383968743003}{10000000000000}.
$$

两窗各自按真实 $dr$ 积分。原全部 6391 连续子格、5970 个 sec/tan 投影接口、腰端零长接口、真实腰闭合分母和均值都在两次完整扫中。

合同 notes/2026-11-14-R133-cached-signed-Green-all-interface-impulse-contract.md 的两侧平方递推适用：左侧输出与右侧输出只对**同一个接口冲量**有不交径向支集。原 signed rate 仍在已存积分中，局部整格增长使用安全上界，未用负 rate 乘单向积分上界反造指数上界。

## 实际完整上界

对所有 5970 个接口逐项计算后，实际最大值满足

$$
\max_i g_i^{[0,9/10]}<121146.604996,\qquad
\max_i g_i^{[0,r_{\rm ph}]}<56766.695864.
$$

两者的最大接口均位于
$2147184947341121/9007199254740992$。以下是已保存逐行证据的部分严格上舍入值：

| 原事件编号 | 全内段增益上界 | 固定负窗增益上界 |
|---:|---:|---:|
| 1 | 1745.209992 | 817.704086 |
| 153 | 2537.055872 | 1188.709514 |
| 2001 | 21318.875909 | 9988.982988 |
| 6621 | 121146.604996 | 56766.695864 |
| 12358 | 5372.213999 | 2517.720597 |
| 12360，腰端零长接口 | 5370.095139 | 2516.727764 |

这张小表只作查看入口；完整 native 保留全部 5970 行、12361 个左扫事件和 12361 个右扫事件，最终门核验了精确事件身份、完整覆盖和两窗真实测度。summary 的 actual_progress 字段是最后一次中途快照，不能替代最终 complete_individual_interfaces=5970 及全部完成门。

这些是合法上界，不是响应下界，也不表示每个局部误差都会达到最大增益。后续矩阵舍入的多个接口跳由同一个原源产生，不能把它们的输出平方直接相加；可先用 $\sum_i g_i\|j_i\|$，或另证完整相关 Gram。

## 实际规则检查与后续接线

实际 worker 在 22:42:31、22:42:32、22:44:45、22:44:51 UTC 完成 4 次真 pull 和两份 README 差异核验，四次 actual_diff 均为空。最后已读提交为
`b7e434dfa289ea50505421c59a84ad77819499d6`；
独立人工规则审阅提交仍为
`ee26c0a65a2e63c15f2ccfba6714181584416542`。

本结果可直接支付完整矩阵方向方案中 $V$ 的独立舍入所引起的真实 $Q\,\Delta V\,q$ 跳。共享同一 $Q$ 和同一物理 $R$ 的纯补空间换基只是准确坐标事件，不能把它当新的物理跳；其余真实边界差、body 模型差、均值、帽两行及未知高块反馈仍须在同一后验恒等式中分别支付。
