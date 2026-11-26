# 97q pending279：真实 14d1 终态、一次物理交换与 pending298

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

**这是唯一原自然终态的收据，不是重算或新的连续证明。**
实际 eta 从 `4.8302220914394944e-5` 降到
**`4.2622659748238665e-5`**，新增 9 次真实 metric 接受。真实 p 仍 `.181`，
当前 stage eta goal 为 `2.5000000000000047e-7`，尚未通过该 stage；
没有把辅助 e、较小但被拒的 fine 值或单段时间截止冒充完成。

## 身份、自然终态与规则 pull

- run [45895078668](https://github.com/Rogerhu12/math-research-public/actions/runs/45895078668)，job `140166868607`。
- 触发及实际 public pull 提交均为
  `021c6d790ac7e6e2b163fe9db7870a28f3640ec1`；根 / 课题 README 均匹配，差异为空。
- private 实际 pull 到 `95ae3967c20d32745f8439da6a098e77a317bdf9`，根 README
  匹配，QUEUE 唯一且为本会话进行中。
- wrapper `scripts/r582_physical_pending279_resume_20261127.py`，11,630 B，
  SHA-256 `6122c313082e96eb2826beface953d963e82bb517a16bb1d3e14423ab5c3a03b`；
  实际科学 driver 仍为原完整 physical epigraph 实现。
- 原 request 380,989 B，SHA-256
  `c7ba6dcdacbe6982f9f09414d3275f26b8ffc8dfba509e6c1f54a76595186b05`；
  lane `actual-a237-pending279`，stdin 367,270 B，SHA-256
  `1c6249edb3a98e28735869d63cbd629e313b0ef0673042484b72789b527395d0`。
- job `21:00:36–21:40:42 UTC`，Actions success；科学子进程
  `21:01:02.731412–21:40:38.849590 UTC`，returncode 0。
- 新科学 **`2375.001235837` 秒**；原 FINAL 为
  `scientific_clock_checkpoint_not_complete`，stage 0 / outer 1 / metric。
  没有自然 OptimizeResult；outer 0 因真实缺失 fine 物理峰完成交换，outer 1 未结束。
- 完整原 stdout **4,790,919 B**，SHA-256 `a64bda0946806404c9a4d5777a0a57215061519cbf4bbab1dc9f5cb4ae6d7708`。
- 逐字 FINAL JSON **380,450 B**，SHA-256
  `84707de70bbaf0cdb270f2363b112e33c32d2f810a0ee2f3055dfbfd1d9d43a7`。

原日志只从已完成 job 下载一次。原 FINAL hash 使用原子串字节，未重新
序列化。所有本地处理仅是原日志 / JSON / hash / 坐标记录解析。

## 实际 97q 与完整 fine 资格

真正保留 q 的 SHA-256 为
`14d1a961e41fa87c152eb81f22837e5e54ba5014bdc5f92f05d70dc5fb5a4445`。
它明确 `qualified_on_this_fine_grid=true`、accepted_as
`complete_fine_feasible_metric_improvement`；真实 p `.181`，完整 fine
**11100×3072**，actual coarse **296×1536**。

| 量 | 实际已完成原观察 |
|---|---:|
| eta | `4.2622659748238665e-5` |
| eta attainer | `s=.532177734375`, `theta=4.6305766716974555` |
| physical geometry violation | `0.0` |
| working geometry margin violation | `9.776581757700575e-10`，原 tol `1e-8` 内 |
| 曲率最大值 | `16.452569186061563` |
| 曲率 attainer | `s=.8695363569939005`, `theta=4.71238898038469` |
| mean-E 最小 / 最大 | `.6436102202691757` / `1.1736777298558985` |
| det 最小值 | `.6435974562705526` |
| area 最小值 | `.21999999999999997` |
| ball 半径最大 | `.7737519908863636` |
| abs(y) 最大 | `.39260282738882435` |
| 最低高度 | `.02` |
| cap height 参数 | `.6955843847203279` |

共同端点 62,878 个，原 knots 和全部端点 jets 的材料 mesh SHA-256 仍为
`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。
这只是同一个材料 seed；97q 本身从 a237 改成 14d1，因此原 a237 的 mean
参考与全域 delta/alpha/K/reach **不能转借到这个新 q**。

| 原数组 | 长度 | binary64 SHA-256 |
|---|---:|---|
| actual coarse | 296 | `fc6bb96e5ebfb8cf65c72ebce9cab8522236a2fc8d6a6236e7f4bf8b71f7ca73` |
| actual complete fine | 11100 | `d0d440392b18e0cda2277fc1756f62dffe3342286013b8b6852564b160d45004` |
| original proposed coarse | 298 | `766fddc2d159f0c70316aa64a6e14705d6b0add23333361e1bc846cb7f8b4dfd` |

## 两个真实网格入口与一次被保留的物理拒绝

入口首先采用源 proposal **279×1536**，fine 是原 11025、proposal279 与
新中点的完整并集 **11076×3072**（SHA
`9133e509ccd9560bf12fe0d87ce28a5eea84a379669b9467b3d728b39760720e`）。
旧 q a237 在这个新数组上新付一次完整 fine，eta 仍
`4.8302220914394944e-5`、margin V0，耗时 `38.062332388000016` 秒。
它没有冒用源 11025 资格。

outer 0 callback 11 的独立候选 `7b23b6edca65…` 有更小的 fine eta
`4.244188358518617e-5`，但原 working strip margin 违反
`1.924882145765052e-5`，超过原 tolerance，故 **拒绝**。
该真实缺失峰 `s=.6717773437500001` 触发立即交换；18 个原 pending 径向
记录按原 append 规则贡献 17 个新 coarse 坐标，得到 actual296。
原 backend 没有自然返回，trust 仍 2，没有伪称一次自然收敛。

新 coarse296 导致永久 fine 扩到 **11100**。当时真实 best `537fbdd7c35a…`
在完整新 fine 上重新付资格，eta `4.273857147493052e-5`，margin V
`1.9547446985720973e-9` 在原 tol 内，新扫描 `37.52125050699988` 秒。
其后才在该新库继续原完整门，最后得到真实 14d1。

## 全部 13 个独立完整候选

raw optimizer 序列与独立物理候选分开。下表 q 是真正送过完整 fine 的
物理候选，不是自动把 raw q 记作合格。9 次接受各自严格降低真实 eta；
其余 4 次完整 fine 候选明确拒绝。

| outer/callback | 候选 q SHA 前缀 | fraction | 独立 e lift | coarse e | 真 fine eta | working margin V | 结果 |
|---|---|---:|---:|---:|---:|---:|---|
| 0/1 | `455fbca5553f` | `0.5` | `4.504179443702183e-06` | `4.8294113422370524e-05` | `4.829713876637864e-05` | `0.0` | 接受 |
| 0/2 | `9bb0fc59b265` | `0.25` | `3.970638035806593e-06` | `4.769690961800933e-05` | `4.7699929195145854e-05` | `0.0` | 接受 |
| 0/3 | `8828e0265442` | `1.0` | `4.032261119628427e-06` | `4.756024551315119e-05` | `4.7561686055996546e-05` | `0.0` | 接受 |
| 0/4 | `baab5e9327f9` | `1.0` | `1.8564400205162637e-06` | `4.500294113880506e-05` | `4.504692186864017e-05` | `0.0` | 接受 |
| 0/5 | `57016a438b16` | `1.0` | `9.701748103490093e-07` | `4.4068790712980334e-05` | `4.408864281734367e-05` | `0.0` | 接受 |
| 0/6 | `28ebb21ac60b` | `0.5` | `2.9490394499015043e-07` | `4.318730894112221e-05` | `4.3230559849730246e-05` | `0.0` | 接受 |
| 0/7 | `2310f8bb4bc6` | `0.03125` | `4.160924942333527e-07` | `4.322024264910879e-05` | `4.32320194036263e-05` | `0.0` | 拒绝 |
| 0/8 | `02cd391b7fad` | `0.5` | `1.8001532978465743e-07` | `4.287555241649044e-05` | `4.306413262719317e-05` | `0.0` | 接受 |
| 0/9 | `3f6d26a26be6` | `1.0` | `4.818983879639334e-07` | `4.303076019254594e-05` | `4.3305174746138274e-05` | `0.0` | 拒绝 |
| 0/10 | `537fbdd7c35a` | `0.5` | `2.9102022841254015e-07` | `4.25836573427425e-05` | `4.273857147493052e-05` | `1.9547446985720973e-09` | 接受 |
| 0/11 | `7b23b6edca65` | `0.5` | `3.242271224333066e-07` | `4.2264102627121645e-05` | `4.244188358518617e-05` | `1.924882145765052e-05` | 拒绝 |
| 1/1 | `f6896e0fbe92` | `1.0` | `1.8007208338984335e-07` | `4.271380125056592e-05` | `4.287542581862051e-05` | `0.0` | 拒绝 |
| 1/2 | `14d1a961e41f` | `0.5` | `1.2591154407538623e-07` | `4.262265975199815e-05` | `4.2622659748238665e-05` | `9.776581757700575e-10` | 接受 |

coarse e 在若干行低于实际 fine eta；这是原算法的完整 true-eta 下降 / 峰
交换策略，不是“所有 fine metric 行≤coarse e”的承诺。原 geometry、box、
fine 完整性、工作 margin 和真实 eta 接受门均保持。
13 次 raw callback 全部完成当前全行检查且 raw 不可行；没有把抬 e 或
缩步副本反写成其原 raw / BFGS 状态。所选 fraction 分布为
`1:5`, `.5:6`, `.25:1`, `.03125:1`；一共 26 次新物理回退行评估、
13 次 halvings 和 13 次独立 epigraph lift。

## 最后 raw 与实际 best 的区别

最后 raw q：
`6f82fa536bca3ab27f014f152d4b7e38382d4ab9444d2f63bff3b32eb3cef1c0`，
raw e `4.2496748207922764e-5`，当前 complete row violation
`8.732223143831738e-7`，box V0。它没有完整 fine 资格，也没有作为 raw 接受。

其独立 `.5` 回退得到真实 14d1，e lift
`1.2591154407538623e-7`，完整 coarse e
`4.262265975199815e-5`；全部实际 coarse 行 / box 及完整 fine 通过后，
才以 eta `4.2622659748238665e-5` 成为新实际 best。
原后台工作数组没有输出，后继可分开继承该 raw warm proposal 与真实 best，
不能声称恢复其未保存的 BFGS 历史。

## 原 pending 与正常下一输入

剩下两个准确 binary64 径向坐标：
`0.4427117500000007`、`0.65859375`。
两个都在 actual11100 fine 中；原 proposal 为 **298×1536**，原 pending angular
upgrade 为 false，角 fine 3072 全保。
实际 / planned / proposed trust 都为 2；末次 active outer 未完成 adaptation。

原 source fine11100 ∪ proposal298 ∪ 新中点得到 **11103** 个准确坐标，
binary64 SHA-256 为 `a83d3bf9aa2d37d8a7742efcfab2aceecc4d2f459a724e1854ef4cdefdda6a61`。这只是本地对原坐标并集的
记录，不是新值计算或已经合格的网格。下一正常输入需在这个新完整数组
重新支付 baseline 资格；原全部 11100 个点和两个 pending 坐标都不能丢。

## 新费用与来源链

| 账项 | 原终态 |
|---|---:|
| 科学秒 | `2375.001235837` |
| 真 metric 接受 / restoration | 9 / 0 |
| 完整 fine | 15 = 13 callback + 2 新数组 baseline |
| 完整 fine 径向块 | 1305 |
| fine 径向评估 / 空间点观察 | 166212 / 510603264 |
| 完整 Jacobian | 12 = 10 retired + 2 active |
| 已完成方向块 | 162 = 130 retired + 32 active |
| active 32 块中的未闭合 Jacobian | 完成 6 块，另 26 块属于 2 个完整 Jacobian |
| backend value keys | 65 = 56 retired + 9 active |
| 完整 Jacobian 秒合计 | `762.132183138` |
| 单个完整 Jacobian 秒 | `61.68833195900015` 至 `66.5051814049998` |
| complete backend row checks | 13 |
| 新物理回退评估 / halvings | 26 / 13 |
| 独立 epigraph lift | 13 |
| 完成 outer / backend natural return | 1 / 0 |
| 新 model grid constructions | 4 |
| 新 geometry value calls / AD blocks | 1340 / 162 |
| 旧方向检查 / 7 点诊断复跑 | 0 / 0 |

未闭合 Jacobian 6 块及所有当时已花工作留在新 elapsed 与 active cost 中，
不伪报完整、不清零。必要原材料再生、全 source ledger 与较早未知费用
保持原样；没有把子计数重复加进总科学秒。

同一完整 scan 顺手累积的旧冻结圆参考有限范数（非新科学门）为：
delta `.024893843415172253`、alpha `.1767930750868537`、
导数比 `1.1661640659647707`、法向投影差 `.06865450948065072`、
cap 高度差 `.020882679140549643`。它们相对于旧原始 81q mean，
不是当前同 mean 圆参考，也不是连续上界；不能替代独立完整几何证书。

后继直接继承实际 14d1 / coarse296 / fine11100 / pending2 / proposal298，
保留 raw 6f82 的未合格身份；没有旧 fine / Jacobian / 诊断回放。
