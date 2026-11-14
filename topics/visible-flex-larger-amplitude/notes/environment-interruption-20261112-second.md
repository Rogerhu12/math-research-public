# 2026-11-12 10:59 UTC 执行器再次切换：恢复账本

## 事实与可用基线

10:59 左右工具失去执行器；恢复后原计算树、发布树和 source 缓存均不存在。新执行器上重新 clone，并正式 `pull --ff-only origin main` 到 `95189144e667089085b8603b78822f88b92166c6`。根及本题 README 与上次已读 `06caef9e7f45a4976727978c29fdc1faa67b0b99` 均无差异。

最后确认发布的本题源提交为 `a5dd812603f9c815e1475859b0b3511e049de4c5`，对应 main `7246caa2ce3da61d127e049934c4847e1ec804ca`。该轮136件文件已在新 clone 取回，包括 q105 r1 的完整失败恢复点、q095 两级 neutral 诊断、R33 强参考全高块和 R37 §§8–9。这里记录之后尚未推送的工作；历史终态记录不替代重新生成的真实数据。

会话 `98619`（actual q105 r3）和 `90734`（完整 joint428）没有观测到正式退出或最终结果。向98619发出的中止请求也因 transport disconnect 未得到确认。两者均记终态未知，不记成功、数学失败或已成功中止。

源码与完整证明能从当前会话保全内容逐字重建时，必须核对旧 SHA。没有完整原数据的数值结果按原参数 fresh 重算，绝不依据下表中的几个数字合成 JSON。新文件使用新的前缀，不覆盖旧成功或失败记录。

## q105 实际分支

目标始终为 `q=.105, q4=-.006655700963004517, c6=-.0004116733380408847`；gauge `.09`。M24/N768、prefix tol `1e-7`、maxnodes2400、完整27参数/100BC；原真实尾 M24/depth8/steps12/parts8/N512/quadrature512/tol `2e-9`，physical BC `1e-10`。heap384/cache8/radial16/block12，BLAS 单线程。未改数学门槛。

| 会话 | 正式观测 | 发布与恢复状态 |
|---|---|---|
| 30348 / r1 | exit1；尾残差先到 `5.56049728e-11`，完整Jac复核前worker −9，原因未知；无prefix Newton | 完整恢复包已经在7246发布，可作为重算暖点 |
| 51033 / r2 | exit1；同24H/577×48状态守卫通过，首完整Jac返回前worker −9；264.972秒，345696KiB | 未推文件丢失；不把退出原因猜成OOM或超时 |
| 66750 / standalone audit-r1 | exit1、worker正常0；错误比较了旧M20配置与当前M24，差异仅modes | 已定位为本地守卫错误；修正为与接受的q095 M24 ready全配置比较 |
| 29674 / standalone audit-r2 | exit0、worker0；完整Jac及audit，重映射后的残差 `3.78100738755e-7 → 3.2267755969289545e-10`；456.5526793秒，436104KiB | 真响应未推、丢失，必须重算；不是重新沿用旧 `5.56e-11` |
| 7181 / lazy protocol | exit0；10项轻量协议检查，无Node/BVP；4.926秒，36428KiB | 完整检查源码可精确恢复；数值响应需先重算 |
| 98619 / r3 | 已准备并保存初始完整H已审计响应；未观测接受Newton步；终态未知 | 不记新prefix或成功解 |

r1 恢复包 `2026-11-12-strong-actual-q105-freeq4-m24-tol7-r1-tail-iteration.json.gz` 的 SHA 为 `9bfe41493d962208f9ede593f95b64a3393dc8c39afb76616640e877b92b7346`。它保存完整577×48状态、9 raw node/raw states；physicalDepth8与内部subsegments576不同，不能误读为新深度。

旧29674响应 SHA `7a4c1c2c5390dd997fcef71c58c3e483f31cecd06ce240863c44d929ad1951de`、ready SHA `3ab4396baa55cbafdb50064a30affbc7ad9913e20725305db95f7087db62a9fa`；这些仅是历史核验记录，丢失时不能宣称当前可用。

恢复源码：`strong_actual_same_height_tail.py` SHA `ef8ffa1ceaa813d3a04f3551c3b44111d0e0af2d60953a750e7ec25e46a72ea3`；`strong_actual_recorded_tail_port.py` SHA `7fc687bd4608f5656140dc19abebccfb66074684c46651513efe68818ec311f0`；protocol check SHA `e009628fe6a94f8537a6513c6a017e18948c4f9024b94c8dfe7660b627548f5d`。生产入口由已推87bb基底按精确补丁恢复到 `a84c8587c8ed605fdc0627c1183d79ff0afaa26d21f2b78e00c7091fa5ba6da4`。

新 lazy 入口只在显式参数下采用：首H逐位及所有源/配置/J/audit守卫核对后复用真正完整响应；每个新H仍启动原真实worker，完整Jac+audit并保存，然后退出worker再计算prefix大Jac。下一尾暖点仅来自最后一个真实完整响应。若最终同H复用已审计包，明确记 `reused_already_audited_packet` 和原包SHA，不称独立新计算。

同H重算命令（本题目录，原源恢复完成后）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python computations/strong_resource_run.py \
  --out notes/2026-11-12-strong-actual-q105-sameH-tail-audit-recovered-r1-resource.json -- \
  python computations/strong_actual_same_height_tail.py \
  --accepted-reference notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1.json.gz \
  --prior-config notes/2026-11-12-strong-actual-q105-freeq4-m24-tol7-r1-config.json \
  --prior-trace notes/2026-11-12-strong-actual-q105-freeq4-m24-tol7-r1-tail-trace.jsonl \
  --recovery notes/2026-11-12-strong-actual-q105-freeq4-m24-tol7-r1-tail-iteration.json.gz \
  --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
  --reference-ready notes/2026-11-12-root-vu032-q085-fixed-actual-m20-staged-audit-ready.json \
  --calibration-ledger notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out-prefix notes/2026-11-12-strong-actual-q105-sameH-tail-audit-recovered-r1 \
  --node-heap 384 --point-cache-limit 8
```

## 共同 strip 全 Green 与联合盒

52401 正式exit0：固定g、原τ，完整 cells12..23 ×46模四核，968.043秒、123424KiB。22069 正式exit0：完整213×213四核与四条far-z列，44.187秒、133788KiB；主包1521122B，SHA `d33768666cda08a4991d48911f276135b67aab4354b3d7bc6e83b491da655456`。这些未推数据全部丢失，须重算。旧33件稳定清单SHA `80f9a7a51af352560215ba5df33ae9bd528e5c2c17f7f364d171a33bb63cd037` 仅作为旧执行记录。

R42 是完整的条件证明，单独恢复登记；最终正文SHA `6b3d1a8e090295367e125714f52ebcb3dddb6f45e624bdcb40a0fb1d0ec98c98`，实际 rounded Q 系数须写 `a_n >= 1+2B_n/9`，不能错误写等号。它不声称428联合门已付。

`closure_weighted_panel_flow_v4.py` 与 `closure_panel_centred_low_green_v2.py` 可逐字恢复，SHA 分别 `c28b42101288c5ba43ca0814ff5ca596695979ffd8c2dfb6b94427f11c73b567`、`28766849994c88cbfbda385a38766c7d1171dca9070f9d29b0667b8d0fcb0e44`。assembler 数学循环完整恢复；旧末尾序列化并非全部保全，恢复版记录新SHA `9e420455ef59285219422bdbd1fc82d7d3f15a2af9178a25fd89a2c86faee809`，fresh重算，不能假称与旧源码逐字一致。

continuous strip 派生 cell014..023 原来按空间规则未提交；按 `2026-11-12-tail-r33-continuous-strip-panel-checkpoint.md`原命令与数学payload SHA重建，再执行 centred_v2，随后 assembler。实际输入/参数/命令另由本次恢复清单记录。源码及数学定义保持；时间/RSS等执行元数据不要求逐位相同。

90734 最后可靠记录仅为组装428维矩阵耗时5.53299秒、RSS152092KiB、最大对角 `1.492395e-5`，之后 dense Arb solve 没有最终盒、Lipschitz或正式exit。新的等价降维若采用，须回填并逐项检查原428所有门；没有完整输出前不登记联合成功。

## 外0..11与R41

R41 完整角connection反解与有限多项式缺陷界已经逐字恢复，17753B，SHA `ce3234ebe7f848b1aef0ac043015def2a83c35c5a1a7a237552d096c32ba129f`。它支付角向mean和所有带外模，不能把有限Galerkin根或13个径向端口当真实径向解。

旧13真实port工具72511正式exit0，.743708334秒/41772KiB；结果319136B、SHA `e41fa524b12f746218310a990445dbd1d1af86449821583a4e77436182ae5a48` 已丢失，只能按同输入真重算。cut的候选 τ=0 总范数 .01508961329363、τ=1/64 总范数 .01556987656240，均小于1/64；这不是连续外头验证。源码13764B、SHA `663e2f06db45ae701d6d04907231ad557d939951ec93db86f18a014ce2739e2e` 已精确恢复。

`tail_r41_connection_polynomial.py`（SHA `81d5da68b0065c9e24978875c0d03cb96b6600252634c6bb028294db8e955e1e`）与 `tail_outer_saved_segment_norms.py`（SHA `7c3f5f709a5204c3cbdc1e993e6f5286bff9e0fff251c1e7d61d8b05bb879bbb`）旧环境仅语法检查，109端口命令从未执行。通用根条件证明/helper旧时未记录SHA，恢复版按当前实际字节重新记SHA。

下一真实接口是外0..11完整连续径向候选/缺陷、真实2×2低频列与深图导数的联合边界门。R29/R33/R42现有Green覆盖12..224，不能仅重缩放强参考便声称覆盖外头；node12小trace也不能径向裸逆传到cut。全部高模及独立深端反馈共同求解，禁止在cut和deep端同时任意指定导致过定。

## root尚未执行的两个准备入口

`root_actual_geometry_field.py`（旧SHA `1fdfbe159203974cb68420bd3a1bcc1dd665a66f711f3431200db3d611fb9091`）及 `root_actual_freeze_design_view.py` 是未运行的准备源码。后者最终一次补丁后的SHA未记录；若无法逐字恢复，须按全部身份/配置/真实残差守卫重新实现并记录新SHA，不把旧hash借给新源码。

geometry_field 目标是同一计算t/η网格上的全场有符号主曲率与半径包络，完整保存所有模式与mean，供多控制几何比较；它不新求解。freeze_design_view 目标是在接受真实27参数设计后，把同一完整raw配点/物理五次与全部H固定为真正M24参数视图，重算原RMS/全部BC，保留所有源/8物理数据/图划分身份，不修改真实g或重采样。先对已接受q095 M24作身份核验，再用于实际接受的设计端点。

## 执行顺序与不变门槛

先推恢复文本、源码与完整证明，再独占重算同H尾，随后恢复q105真实prefix。Green/联合盒及外头低内存工作在明确资源窗口执行；Node与大BVP不并跑。每次pull立即比较两README、记录已读SHA，至少每小时一次。所有结果区分完整证明、有限系统验收、准备代码和未知终态；当前课题完成标准仍全部按README，继续研究。

### 新执行器13port真实重算

轻量13port重算已在新执行器正式exit0，原源及三完整数值输入SHA均同。新包 `2026-11-12-tail-outer-strong-m20-port-norms-recovery.json` SHA `fc75a411e96b01cbff0047783619b8193479f68ad97b437cb4fce8472f2910ec`；去时间/RSS的数学payload SHA `dd2048048f15640b1726a1585c06b2c171bcbd6ca1745064ee2b9eadddcb3323`。稳定9件见 `2026-11-12-tail-outer-restored-run-manifest.json`。109段和连续径向门仍未运行/支付。
