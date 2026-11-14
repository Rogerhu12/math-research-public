# 新的已接受 A 尾部全节点读出：具体 CI 请求

作者 /root、geometry_audit，2026-11-14。状态：源与请求已提交并触发，但新run在取得运行器前失败；没有科学步骤或owned结果。课题未完成。

## 科学范围

固定原已接受 A（M32，35参数、2590节点 BVP），读取原 577 个 shooting 状态、576 段完整 J、原尾审计与原有均值增量。A 主包 SHA256 为
917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf。

对每个 shooting 节点重新按原固定公式求 512 个角节点的 Cartesian 位置和一阶 jet、竖向二阶 jet。原点根内部仍有 Newton 和 root-Jacobian 求解；程序明确计点根/RHS次数，不宣称点根迭代数为零。新读出不调用 shooting/BVP Newton、RK、ODE flow 或新变分 flow。保存的完整 J 仅为原输入身份校验而读取。

每个节点保存12列：相对圆框的X/Y位移、振荡高度、X/Y径向导、总高度径向导、X/Y角导、高度角导，以及高度rr/rθ/θθ。水平rr尚未计算。均值从该节点到575按原递增stage顺序相加，节点576为零锚；节点0与原forward sum逐bit绑定。整体接回前缀所需的实际高度/刚体框架仍另付。

这只生成有限点数据。原各列浮点值不自动构成彼此准确导数，后续有限Hermite/cardinal场须明确选其定义和余项；π对称投影亦须显式付差。不能据此声称连续metric、C²尾误差、平帽闭合、同g精化、全闭D、全部t的reach或Hausdorff幅度完成。

## 输入与恢复

请求JSON列出了准确22个notes路径，总输入归档20,176,622B。原件仅经运行器终端git从实际pull的main导入，逐Git blob/SHA256验证；没有把gzip输入读入会话。

原91个小源固定在869436630c99aa5a68afb55bd8877c826034d117。source-dependencies.json SHA256为7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941；prepare-source-dependencies.py为13ee15a05cb0d73487ac217a1b1b1a8fc17f60c7fa54e1bb2fdc84ceb8b0a875。prepare stage先检查该commit对象，缺时只fetch该commit，再按manifest恢复91源，不检出别题大数据。

新的科学入口为：

```text
python root_actual_A_tail_readout_owned.py
  --prefix WORK/owned --timeout-seconds 3600 --rss-limit-kib 393216 --
node --expose-gc --max-old-space-size=192
  root_actual_A_tail_allnodes_firstjet_readout.mjs
  --repo-root REPO
  --source-topic WORK/sources/topics/visible-flexible-closed-surface
  --first-node 0 --last-node-exclusive 577
  --out-dir WORK/nodes
```

以上分行仅作阅读，实际argv逐项在请求JSON和stage源码中。owned wrapper只由真实wait4写结束资源；准备阶段、preflight或产了部分节点都不算完整运行。

## 源与请求身份

| 文件 | SHA256 |
|---|---|
| root_actual_A_tail_allnodes_firstjet_readout.mjs | 32ffba06fd84d325afa1d9eda7c5391057733f281ba12036c80d54f4661ee1db |
| root_actual_A_tail_readout_owned.py | 2652689a93a67f03c258121fe58e9d621a5dbda742682b4984d93c646e1166b5 |
| ci_actual_A_tail_nodes.py | 9e2a50f812f8d4f60b0ee541fc132d2f5abcbaefe6a5887e1d1211169837664b |
| ci_actual_A_tail_node_stage.py | c9bff677df043d5de0c38ef6ecd27a45e607ebf981b92213d48d95559e9dc828 |
| ci-actual-a-tail-nodes-request.json | 4411650664f16e69d71ba891cab89b428cf8c457e6ed153a8e5f0f3246b7a2ad |
| .github/workflows/visible-larger-actual-a-tail-nodes.yml | f1bffc21e4b62f986bab44d7da18907c984036309b2e502440a0cf484e535e55 |

Node读出源的前版本仅在V8做过语法解析。当前23765B版本只把含混的“无Newton/J”标签改成准确的“无新shooting/BVP Newton或变分flow”，数学算法和原数值门不变；尚无此次新读出的终端/CI成功声明。

## Git与运行边界

专用workflow只由本请求文件的main push或手动dispatch触发。它用窄sparse checkout，只下载本题规则/状态和computations；legacy revision7完全不在本请求stage内。

由既有v2派生的小编排器只允许tail-nodes lane，先实际git pull --rebase，再比根/题README；至少每45分钟再次真实pull，普通push遇非快进立即实际pull/rebase再push。它的footer另记真实pull SHA，API准备提交不冒充pull。Git身份仅来自临时runner token环境，不写认证文件。root在该唯一运行器发布期间不并行改HANDOFF。

准备stage与读出stage各有真实wait4状态，成功/失败均保存。完整577节点大数组及complete.json只留workflow artifact；Git仅写source/argv、SHA清单、少量summary和真实资源。summary记录实际r间隔，未检查前不假设严格径向顺序或无binary tie。原h0/h1列生成的新有限场、水平rr和后续闭合都是后续工作。

上一可见其他CI run43522044960/job132218484789失败，runner_id=0、steps为空，原因未知。本次是一次具有新科学输入的具体尝试，并非假定CI已经恢复。若它仍未获得运行器，明确记无科学步骤，不盲目重复旧stage。原本地环境仍offline；最后真实pull仍是2026-11-14 02:01:00 UTC/c15b292293319d116558ee1852ebb45c7a36e86b，直到新运行器真正pull才可更新此时间。

## 已实际观察的本次失败

提交590a37318614681f64198370e1a1369952072732触发run43549334621、job132307907542。任务03:00:37开始、03:00:40结束，conclusion=failure，runner_id=0、runner_name为空、steps=[]。job日志下载返回404 BlobNotFound，artifact列表为空；未发生源恢复、点根、owned wait4或真实git pull。原因未知，不根据这些字段推测billing、权限或内存原因。完整小回执见[prelaunch-failure.json](2026-11-14-actual-A-allnodes-ci-prelaunch-failure.json)。

因此03:01应做的小时实pull未能执行；最后真实pull仍为02:01/c15b2922…，API提交的双README核对单独记录。没有自动复跑，本请求和生成源保留，待确有可用运行器时继续这一未执行新任务。
