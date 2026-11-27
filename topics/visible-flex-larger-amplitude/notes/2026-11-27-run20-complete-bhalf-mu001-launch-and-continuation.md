# 20：同一完整 bhalf 输入、较小恢复阻尼的独立续求

会话 Astra-larger-e4e2a2bf-20261126（AI-assisted）。准备时间 2026-11-27 22:54:51 UTC。本提交同时提供完整源码绑定、全部原参数和公开 Actions 启动；真实 run、job、实际源提交和新输入/场身份须由实际返回另记，不能从计划倒填。

## 当前依据与唯一科学参数变化

[完整来源分析及严格比较](2026-11-27-full-restoration-scale-and-mu001-branch.md)已从实际10fa driver、fb4e QP和全坐标源给出：只要完整有限几何违反仍正，程序处于恢复阶段，QP目标没有Phi项。原相同线性可行集的精确QP最优解在降低mu时，其最优非负公共松弛量不增；64步截断、非线性全几何、root/alpha和实际收敛没有因此得到保证。

本独立分支保持19的b/S=1/2、delta=1/32和原同一g，唯一科学标量把argv37 `.01` 改为 `.001`（`--restoration-damping`）。metric damping仍 `.01`，完整坐标范数、1/4个metric/restoration方向、16/64内迭代、15全线搜索、32normal stages以及全部其他域/参数/预算不变。argv71只改独立输出namespace `fixed-fejer-meridian-batched-bhalf-mu001-first`。运行中的19不修改。

19实际bhalf初六族reach=.9684249942095058、distplus=.005863061771032241仍正，Phi3825.0583894874153、Gram.6460503011117507；相较18初reach/distplus/Phi下降而最大Gram误差升高。完整数值与界线见[19实录](2026-11-27-run19-complete-bhalf-launch-and-continuation.md)。这里仅据已经实际返回的有限结果选择独立方向，不继承它的场、接受点、参考报告身份或准确证书。

## 全部交付与原字身份

[完整参数包](../computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json) 50679 B / SHA256 `ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4` 含全137角色、18原运行源、原120对、三份完整19父文件、所有旧metadata/失败/typed未知和精确delta。当前10fa/8027/f600及其他原运行体没有代码变化。

| 角色 | 完整文件字节 | SHA256 |
|---|---:|---|
| science | 97019 | `89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca` |
| pure | 86221 | `f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64` |
| display | 32429 | `1fef7603002bdfbac58623b1d7c8b1cd0492d050f42c22acfd1ce11c3597278e` |
| parameter_constructor | 15064 | `acd5d19439d9a6b00216bb6bfee2fab46087356a3580b97b946961fb6e83daa9` |
| source_analysis_and_choice | 15526 | `42ef2c9012b6c76439f09d0255392eabda6a27d240737e22e1bd74e3a914e313` |
| 完整参数总表 | 50679 | `ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4` |

完整文件路径与Git blob在上述参数包与[启动总表](../computations/fixed-fejer-bhalf-mu001-complete-launch-delivery.json)。science157/pure7词、458/445 formal、48live完整保，不裁成“运行最小集”。旧408/395formal及原18+30 live来历也完整保。

## 真正执行顺序

初始队列 73243 B / SHA256 `9d82aeee09115e026edb61f997ccde501004f05c602e3fdf4811373c4c7aff23` 包含两项原必要完整输入构造和整个科学step。输入1保持父对象所有字，输入2仅id的run19变run20、26参数及全输出/摘要不变；新runner独立重建参考、原923节点、全7377观察、2218标量叶。原input构造的accuracy_reached若false仍真实保，构造成功不冒科学成功。

两完整science/pure队列带包装共117276 B pretty / 104048 B compact，均超控制器95000上限。两step本身数组103956 B同样超限。因此先整运行science；真正自然返回后保存完整旧对象和全部真实输出身份，再退只已返回的对象、接入完整pure7词/445selectors。没有增加数学或审批门，也没有缩减任何原参数。完整normal/geometry/closed、R716和全mesh后续保持未付责任，在各自完整真实材料具备后接着执行。

## 控制与规则

控制器 19984 B / `1d790c7c805c26762bd982e1cfcd00f3c38d774e272468529af823966557d629` 只把原19四处H槽标签改成20；完整执行逻辑、真实pull/rebase及双README差异检查不变。workflow 2219 B / `7ee7db6e9b1c6d763439e0967ae974661c4facb8ca90c4a67eb945d4bb6aadbc` 只改名称、request/controller路径和独立concurrency标签，原partial checkout、所有原依赖、permissions及350分钟预算保持。

请求 44226 B / `965c1cbf18be6f9314ef6a15019e498ae1a71dc5a00489c90a0e1911b356c39a` 完整保19原请求的历史metadata并明确当前真实10fa/8027/f600与bhalf参数；旧19请求中沿用的bquarter描述只留历史，不冒当前参数。controller20000秒是后续接纳预算，不将活动child超时杀掉；job结束仍非研究完成。17–19现有队列和源保持，16官方cancelled及末科学未知另保[终态](2026-11-27-run16-official-terminal-and-unreturned-observed-solve.md)。

只在授权公开Actions做科学；全部科学raw/逐胞/mesh/checkpoint只runner，Git保全源、全参数、证明与实际小记录。根终端仍不可用，cloud freshHEAD核对并普通非force推送不冒真pull；控制器每次实际pull即比较双README，只读变化并记已读commit。启动前双README已读基准 `1e642976aec7c6e620da2e2bab3112e6ee30ee56`，实际发布时fresh检查；当前hash见request。

新实际run/job/model/point/科学report/accepted/final/所有fee和mesh均未知。该完整分支不是完成结论；继续到README全标准。


## 22:56:26 UTC：官方运行已真实启动

上述完整launch提交 `85cd235221ace28158625a7ced52a24551b509eb` 实际触发 **run46079535427/1**，官方created_at/run_started_at均为 **2026-11-27T22:55:41Z**。Job **140775034500** 当前in_progress；checkout、Python和全部原依赖安装已success，完整公开研究步骤5正in_progress。此时未读到任何完整新input或科学自然返回；提交HEAD只标启动，不倒填各step实际source或未来field。

根还在精确发布父 `52ec703c1a995c63c8af83175045c5de0c43e0f6` 读完整workflows Git树 `82a183256a747fc2758adaeb9a7304609f72864b`（1266项，truncated=false），该父无parallel20路径。先前contents接口的1000项不被当作完整缺席证据；完整Git树身份才确定此次新增路径。

```json
{
  "observed_utc": "2026-11-27 22:56:26 UTC",
  "official_discovery_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs?head_sha=85cd235221ace28158625a7ced52a24551b509eb",
  "official_discovery_complete_response_bytes": 13375,
  "official_discovery_complete_response_sha256": "628611b15556cd013bfb8301ed52776b20e47f778ec8e0a8f5aca0d4c615ae38",
  "selected_official_run_fields": {
    "id": 46079535427,
    "name": "Visible larger amplitude complete bhalf restoration damping 20261127 20",
    "head_branch": "main",
    "head_sha": "85cd235221ace28158625a7ced52a24551b509eb",
    "path": ".github/workflows/visible-larger-20261127-parallel20.yml",
    "run_number": 1,
    "event": "push",
    "status": "in_progress",
    "conclusion": null,
    "workflow_id": 433228578,
    "created_at": "2026-11-27T22:55:41Z",
    "updated_at": "2026-11-27T22:55:44Z",
    "run_started_at": "2026-11-27T22:55:41Z",
    "run_attempt": 1,
    "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46079535427",
    "jobs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46079535427/jobs"
  },
  "complete_bounded_official_jobs": {
    "jobs": [
      {
        "id": 140775034500,
        "name": "Construct the same fixed target and solve the complete bhalf smaller damping",
        "status": "in_progress",
        "conclusion": null,
        "run_id": 46079535427,
        "logs_url": null,
        "steps": [
          {
            "name": "Set up job",
            "status": "completed",
            "conclusion": "success",
            "number": 1
          },
          {
            "name": "Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
            "status": "completed",
            "conclusion": "success",
            "number": 2
          },
          {
            "name": "Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
            "status": "completed",
            "conclusion": "success",
            "number": 3
          },
          {
            "name": "Install the recorded numerical and automatic differentiation dependencies",
            "status": "completed",
            "conclusion": "success",
            "number": 4
          },
          {
            "name": "Execute public research and publish independent compact records",
            "status": "in_progress",
            "conclusion": null,
            "number": 5
          },
          {
            "name": "Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
            "status": "pending",
            "conclusion": null,
            "number": 9
          },
          {
            "name": "Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
            "status": "pending",
            "conclusion": null,
            "number": 10
          }
        ]
      }
    ]
  },
  "initial_commit_is_not_each_future_step_source_commit": true,
  "new_input_reports_observed": false,
  "scientific_natural_return_observed": false,
  "complete_model_or_point_known": false,
  "goal_completed": false
}
```
