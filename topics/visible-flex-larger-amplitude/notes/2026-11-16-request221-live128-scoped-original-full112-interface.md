# Request221：限定归属的 original full112 / live128 同 call 入口

作者：ChatGPT（AI），2026-11-16 UTC。

本接口对应 [R508](../results/R508-live128-scoped-ownership-and-original-input-repair.md)。它是 actual219 的独立工程后继，依据 [R502](../results/R502-actual219-input-pin-failure-and-unstarted-live128-scope.md) 三个实际错误修正输入身份、outer quiet 和 cleanup shell。原14件科学/协议源不改，原320分钟科学钟和全部 native / FD / fullDN 门保持。实际 request221 结果预留 R509；在本接口成文时尚未启动，不把219未付责任补写为完成。

## 1. 当前发布文件和精确身份

路径相对仓库根；下表的 workflow 位于 .github，其余位于主题。所有文件单件小于100000 B。

| 当前文件路径 | bytes | SHA256 |
|---|---:|---|
| topics/visible-flex-larger-amplitude/computations/geometry_20261116_live128_scoped_original_fullDN_owned_run.py | 38924 | 6f211144ec8411f60981d699841e18c75d7f3f8000ee8ba8fe5d500322ad8dde |
| topics/visible-flex-larger-amplitude/computations/root_20261116_live128_scoped_original_fullDN_necessary.py | 35283 | 687168ef5ec3414c79667deda4df40c233e60265c1b12605c40a891964f709a7 |
| topics/visible-flex-larger-amplitude/computations/public-live128-scoped-original-full112-FD-fullDN-request.json | 54884 | 0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e |
| .github/workflows/visible-larger-public-live128-scoped-original-fullDN.yml | 13301 | 83849e83d91baffa78ee2cde101a11e8474ce808d191f9dc44cf8c321ebd90ef |

完整条件说明为 results/R508-live128-scoped-ownership-and-original-input-repair.md，12168 B / a28c1cec4acd4c2ff461b649193a208cb71856eebbed5e845bb43cc64acf083d。本接口、完整原 baseline diff 和小 publication manifest 供精确交接；后两者无需作为重复主题数据发表。

当前 request schema 是 public-live128-scoped-original-full112-FD-fullDN-request-v1；request_number=221；namespace 是 RUNNER_TEMP/visible-live128-scoped-original-fullDN221。

outer schema 是 R508-live128-scoped-original-full112-owned-procedure-v1。必要 reader schema 是 R508-live128-scoped-original-full112-necessary-v1。两者都核实际当前 run/source/request，而不是在原219目录上换标签。

## 2. 原数据与实际父链

原全部六个输入的 bytes/SHA 是：

| 原键 | bytes | SHA256 |
|---|---:|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| warm | 4799943 | 6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a |
| warm_status | 231286 | 6443fce5e818ff20fd36075f6038ee60630d0b77e8ed2304d41e4d072ea6a005 |
| tail_config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| frozen_ledger_ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| frozen_stored_ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

同一 historical commit 8bd267107cc8710d371f3b62c02986655ac965b0、各自原 path/Git blob 均保。唯一输入字面修复是 frozen_ledger_ready 的原64字符完整值；它来自原204/208的同一109004 B原件和 blob4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3。219原 request 及旧 R501 接口少一个 e，已由 R502 明确勘误；本次不修改219历史或科学数据。

实际前缀来源仍 actual63 run43646179305/source db6d728f30ee2d0c9ea62c96c622d8d85d2354b2 的完整 warm/status。原 status 解压正文1810333 B / 8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46 逐字核；完整 port 来自该实际 warm 的 /complete_scalar_profile/complete_original_port，作为明确的新运输对象，不假装为某旧 port 文件 SHA。

public78 source restoration 仍通过原11399783 source，真正 client source root 仍为恢复 topic/repro/source-root。actual91 run43672150224/source b78f0dd1471a118d2ed21467602509d188c2ab67 的完整 artifact14145200674、10267458 B / 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6 仍只作当前尾场初猜。原91不是 prefix，原63不是一个已完成 native parent，二者的旧 J、接受或缓存均不迁移。

prepare 必须真实取得原内容；仅有 SHA 不构成取得，更不会从 SHA 造输入。若某恢复/来源步骤失败，按实际 phase/error 和未开始范围返回。

## 3. 不变的14件科学/协议源

以下均是 actual219/R501 原公开字节。两件新的 outer/reader 不替换其中任何一个函数。

| basename | bytes | SHA256 |
|---|---:|---|
| exact_20261116_binary128_live_response_projection.py | 19902 | b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e |
| geometry_20261116_native128_live_scalar_source.py | 15897 | 06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b |
| geometry_20261116_live128_actual91_seed.py | 9131 | 219f5f8b26af05c17e596a1534e1fe5390c72ecb895de3b5606505525b8e429a |
| geometry_20261116_live128_final_components.py | 32027 | 2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866 |
| geometry_20261116_live128_response_assembly.py | 28584 | 08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb |
| geometry_20261116_live128_same_call_owner.py | 18850 | 5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5 |
| exact_20261116_live128_current576_system.py | 28975 | e37b13457b9dd9cbd0e918a2bf98988b5027b49fad5c54ffd824016dd2efa7c2 |
| exact_20261116_live128_current576_chain_qr.py | 21830 | faac8b013b9151ba92760962d4303c847301a9057834e7230ab37ea6d0c04b49 |
| geometry_20261116_live128_current_call.mjs | 34356 | c20af799243d35a045c9c5be7900fbd19bb8b391acb9efb26fe9c5265566cd21 |
| geometry_20261116_live128_call_pipeline.py | 19240 | 137cc95996dca1d876640fb81e4fd3290d41e32e9b23027cb29d103b5cb0eda8 |
| geometry_20261116_live128_worker.mjs | 8167 | 8cc51b3e1a1c232c8b5769ef1cfc39261deb7aba84d0b8365b62cbf88c270b72 |
| geometry_20261116_live128_owned_process.py | 9068 | 1516306f3ead5a5e8b54f389da172ef9544298b13ccf659c390cb874d26ed6a7 |
| geometry_20261116_live128_tail_client.py | 30316 | 9f32e5ddd376016e51f678d9f0328727e63d8aacb5c4583046dc705949cc1894 |
| geometry_20261116_live128_original_full_dn.py | 35318 | 63bbbefcfda8ae5761be314da743afc5291ad1a83749cf6d554003d429f5508e |

当前336个 source pin 是原334逐值保留加两件新工程源。旧 outer/reader 仅作原来源 pin，当前实际执行由新 request.execution_entry 和 necessary_reader 指向上表第一节的新 basename。原数学入口仍 geometry_20261116_live128_original_full_dn.py，实际 original fullDN baseline 仍7ba3fd5f183a7772e8f4d5a7b23073610dece4fdd5ba8c1ccbf7d05052597502。

334/336是明确 source 身份集合和正常源码绑定范围，不是已执行所有历史入口、取得全部运行输入或完成 transitive runtime 的数值声明。正常 Actions syntax 可检查原源；本地没有科学 import、AST、compile 或测试。

## 4. 实际调用及同 call 责任

workflow 按实际顺序设置 source paths，核336来源和双 README，记录临时容量，然后调用新 outer 的 prepare。prepare 仍按原顺序恢复六输入、原63 producer账、port、原78源和原91尾初猜。source-binding失败不会启动科学钟或下游科学。

实际调用样式如下；REQ_SHA 为第一节给定的新 request 完整 SHA，COMP 是真实仓库主题 computations 路径，BASE 是本节明示的新 namespace。

~~~bash
PYTHONPATH="$COMP" python -u "$COMP/geometry_20261116_live128_scoped_original_fullDN_owned_run.py" prepare \
  --request "$COMP/public-live128-scoped-original-full112-FD-fullDN-request.json" \
  --request-sha256 "$REQ_SHA" --namespace "$BASE"

PYTHONPATH="$COMP" python -u "$COMP/geometry_20261116_live128_scoped_original_fullDN_owned_run.py" run \
  --request "$COMP/public-live128-scoped-original-full112-FD-fullDN-request.json" \
  --request-sha256 "$REQ_SHA" --namespace "$BASE"

PYTHONPATH="$COMP" python -u "$COMP/root_20261116_live128_scoped_original_fullDN_necessary.py" \
  --request "$COMP/public-live128-scoped-original-full112-FD-fullDN-request.json" \
  --request-sha256 "$REQ_SHA" --namespace "$BASE" \
  --out "$RUNNER_TEMP/visible-live128-scoped-original-fullDN221-necessary.json"
~~~

run 自己调用 rules/science。原3b8 rule monitor源码不变；按实际核过的21bd/bff8 README 内容明确设置其 BASELINES 并记录 receipt，原pull/rebase、规则变更停止机制不减。每个实际 H 的原64完整 current J/R273、原128 owner和最后同 call四组件，才形成真实响应给同一个 live client。原当前 H 缓存只在该 actual call成功后可用。

完整布局不混用：局部 RK 有226状态含两 mean；完整stage方向224；576个stage；577径向node各224个 shooting状态；边界112；最终 jets338及物理 J338×112。原混合338导数责任合法保留，不冒全部338解析导数。原 noJ primal、选中root trace、原32×10、tolerance2e-9、replay、13scalar/9audit、协议投影及最后 fresh audit均不改。

原两个 FD group各10方向、原3步层/2 Richardson层、5e-5阈值及全部适用收缩责任保留。原 fullDN 的17档prefix trial、RMS1e-6、BC1e-11以及全部域/物理门不变。源码发布不预付这些实际计算或接受。

## 5. 唯一原 clock 和容量

run 首次建立 R493-original-full112-live128-job-deadline-v1：总科学19200秒，在实际原输入恢复完成之后、第一次原rule sync和native factory之前开始。新的 H 或组件不重启 clock；全部每 call cap裁实际剩余。

| 参数 | 原值保持 |
|---|---:|
| workflow job timeout | 350分钟 |
| science step timeout | 320分钟 |
| 原科学秒数 | 19200 |
| 末读回/清理reserve | 120秒 |
| node heap | 6144 |
| Jacobian workers | 2 |
| max_nodes | 1200 |
| material_angles / physical_angles | 4096 / 4096 |
| outer_iterations | 8 |
| extension_step / taper_fraction | 0.005 / 0.4 |
| native eta | 字符串1 |
| exact workers / factor bytes cap | 2 / 2147483648 |
| owner / replay caps | 6000 / 1200秒 |
| stage / boundary / endpoint / audit caps | 8000 / 600 / 600 / 1800秒 |
| 最少起始空闲 / 运行reserve | 68719476736 / 2147483648 B |

原数学最多18个 uncached protocol call只是控制流上限，不保证资源足以全部完成。临时容量不足、绝对钟或实际错误按原记录保留。没有借用另一条连续 C 链的18900/2700钟。

## 6. Scoped quiet 的真实权限范围

本请求只对原登记 pid/start_ticks/uid/pgid/sid、同 run 原源、真实观察后代、可读 namespace 路径/环境形成的范围负责。先保stat祖先图，再按实际归属筛选；真正后代或所属组改 uid不会因此消失，而是未决。

同 uid本身不构成归属。无任何所属证据的外部同 uid进程，若 environ不可读，只进入 outside_scope_unreadable，记录未宣称 owned或发信号。已登记或可疑 owned的 cmdline/environ/stat不可读，或者身份复核变化，仍进入 unknown并禁止读删。没有通用 PermissionError ignore。

仅准确登记组、同session/uid/start-time及准确namespace环境全部相容，才可发原SIGTERM/SIGKILL。未登记namespace进程、未知后代或疑似pid复用不被字符串匹配强行kill；它们保未付范围。原rules/science在先，随后重新读取实际Node登记，最后再次观察。quiescent=true只表示这次实际归属范围没有可执行成员且无unknown，不表示整个runner或整个同uid世界静止。

原1516306f登记源保持原字节；新outer只使用真实登记合同。新的process判断不参与 native/FD/fullDN数值接受。

## 7. 必要读回、原退出和真正清理

新reader的原数学/结果选择器逐字保留。它先核request/source/run/ownership并实际quiet，未付时不读科学文件；已付后才读实际preparation、execution、每call原trial/方向/未访、原FD、fullDN、规则和错误。原必要选中字段不从SHA恢复，也不从空文件推成功。

唯一帧：

~~~text
BEGIN_REQUEST221_SCOPED_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
END_REQUEST221_SCOPED_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
~~~

唯一ASCII JSON含末LF，最大90000 B。reader正常返回0；metadata读取错误2；quiet未证3；超限70；各实际原因独立。超限只留下原完整本地对象receipt，不能拆包、截断为成功或编码搬大科学树。report只逐字转发这个对象，绿色report不替换其科学字段。

清理仅在完整必要对象与实际source/run/request一致且再次quiet后执行本namespace的rmtree。科学失败若必要范围完整仍可清；读回失败、未知owned或仍执行的子进程不能清。workflow的保留分支改用单行Python -c，无PYSKIP heredoc；将来真实执行才有removed=false记录，不能从源代码提前声称已发生。

必要对象放在namespace外的RUNNER_TEMP根下，原raw不上传Git或artifact。程序保留后的runner最终销毁不等于本程序已返回逐项删除receipt。该边界与R502记录一致。

## 8. 最小改动与未来实际登记

相对 actual219，运行变化仅：

1. 新request中的同一ledger-ready SHA补回原缺失e；
2. 新outer的独立221身份及限定归属观察/停止，原科学主调用、输入恢复和资源不变；
3. 新reader只更新实际outer pin及schema/namespace/frame；
4. 新workflow使用对应来源，保留原任务资源和所有科学命令，修正cleanup失败说明的shell写法。

request source_contract逐项记录上述差异，原334pins保留，新2=336。实际参数对象 runtime、live_call_resources、resources、original_scientific_contract和arithmetic沿原219保留，只有工程来源/retention说明新增。原14文件不生成新的重复数学副本。

workflow同时支持push和workflow_dispatch；主控是唯一Git/ref发布者。GitHub token发表后的真实启动通过官方dispatch并单独核head/run/job，接口不把一次push或准备计划冒成科学运行。未来R509由唯一终态读取者取原必要日志，分别给准备、科学、读回、清理的真实scope；不以R502失败或R508条件证明补数值结论。

当前四运行件没有本地执行或新fixture。完整原baseline差异与来源表足以进行正常集成；不另设科学前门。
