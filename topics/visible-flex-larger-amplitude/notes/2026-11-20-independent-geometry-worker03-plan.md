# 独立公开 Actions 几何 worker 03

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

**状态：完整调度配置随本结论发布，由request03的push触发新job；实际run/启动与数值结果以Actions回报另记，本条不冒已有科学返回。**
这里只把当前 run2 队列中尚未开始的四项独立几何工作准备为另一个公开 worker。
run2 已经启动的求解任务不改、不取消；root 在本次普通提交中同时撤下queue2对应尚未开始条目并发布本组配置；已经运行的原六方向保持。

## 1. 三个完整文件

| 草稿 | 建议仓库目标 | 字节 | SHA256 |
|---|---|---:|---|
| `visible-larger-resume-20261120-geometry03.yml` | `.github/workflows/visible-larger-resume-20261120-geometry03.yml` | 1746 | `04fee548978d072a320980dc222f1b6e61511a9d8dac3abe45742098e8a733ba` |
| `resume-20261120-actions-request-03.json` | `topics/visible-flex-larger-amplitude/computations/resume-20261120-actions-request-03.json` | 1139 | `1cdb803324c5cefb9aa50a74340afddcda996c12709901de22c673f6b4853c53` |
| `resume-20261120-followups-03.json` | `topics/visible-flex-larger-amplitude/computations/resume-20261120-followups-03.json` | 10284 | `ad8c7f476e31bf00ec55986517392067ef7770bef9945d599f3412c79a768455` |

草稿读取的实际本地 main 为 `ff06cce6391db39bb38274f08df9d2afc0cf09df`。
源 `visible-larger-resume-20261120-next.yml` SHA 为
`8c11ecd347f1a0825159dc3c753e0969ca4884129e0877b433e63ebf2d47df32`；
request02 SHA 为
`0fbfd86075136c5c9c606da00bd093e8bff343229499fc267abe2daec0ea964c`；
提取四项时 queue02 SHA 为
`cb890df4b4354b3d5f0e6198e734165a0ae5e14e7973460e6752d75ef0bb1904`。

仅进行了 JSON 解析、文本复制和字段相等比较，没有执行任何科学脚本或 workflow。

## 2. workflow 与请求身份

workflow 完整沿用 next.yml 的固定 checkout/setup-python action SHA、Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、线程配置、350分钟 timeout、稀疏部分检出和 `public_actions_controller_v2.py`。
改变的是显示名称、request03 的 push 触发路径、独立 concurrency group
`visible-larger-resume-20261120-geometry03`，以及临时工作目录的可读前缀。
`cancel-in-progress: false` 保持原值。
不同 run 的完整路径仍含 run ID 和 attempt，因此所有原科学输出相对路径可以不变，不与 run2 互相覆盖。

request03 使用：

- `request_id = visible-larger-resume-20261120-03`；
- 原 `rebuild_a04_chain.py`，`stop_after = continue`；
- `followup_file = .../resume-20261120-followups-03.json`；
- 原 controller budget 20000秒；
- `prior_run_id = 44758209061`，只作来源记录，不移用其实际场哈希或证书。

双 README 的当前字节与原请求记录一致；request03 将实际已核读提交记为上述 ff06cce。
根 README SHA 为
`581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102`，
课题 README SHA 为
`3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d`。
controller 原有按阶段发布、pull 后规则核对和定时同步行为保持不变。

## 3. 四个科学步骤逐字保留参数

按原先依赖顺序复制：

1. `reconstructed-current-direct-first-geometry-03`：当前重建场的完整 first geometry；
2. `continue-radius-target-41-over10-03`：只续化妨碍 D≤4.1 的原胞；
3. `continue-complete-sixjet-curvature-03`：完整六 jet 曲率覆盖；
4. `continue-exact-same-candidate-geometry-combination-03`：同场准确有理几何合并。

每条除了 `id` 的02后缀改成03之外，`script`、`parent_bundle`、全部 `args`、`outputs`、`summary` 与 `scope` 和提取时 queue2 对应条目完全相等。
因此没有更换 candidate、简化几何域、降低分辨率计划、改变目标或继承未经本轮支付的界。
queue03 的 `parent_request_id` 与 request03 一致，`finish_when_done=false` 沿用现有持久 worker 行为，root 可在剩余作业时段追加已授权工作。

没有加入清单 compaction 阶段。原命令中出现的 manifest 参数原样保留，由必要重建链直接生成的完整清单供应，不额外生成新的清单或改写位置内容。

## 4. 并行的作用与输入责任

根 README 第13条已经指定公开仓库 Actions 作为本题计算环境，并记载4核、16 GB和最多20个并行任务的使用条件。
本草稿利用已有授权，让独立几何覆盖不再排在求解任务后面；没有新增权限或审批步骤，也没有声称消除了科学计算成本。

新的 runner 不拥有前一 job 的 raw，因此必须按原配方重新生成其四项几何消费者所需的实际输入。
这只是输入材料化，不把已经登记的旧结论重新认作新发现。
若硬件浮点造成 bundle、node 或其它自产数据 SHA 改变，所有消费者都绑定 **新实际文件** 并重新支付其本轮范围；旧候选的数值证书不能移用。
源码与参数保持完整，可重生 raw 不入 Git、Release 或分块传输。

完整曲率、D、握持、marker和reach都仍由原四个消费者的实际返回决定；迁移队列本身不支付任何数学目标。
job预算与硬上限也不是课题完成条件，已返回与未返回必须按 controller 的真实状态继续记录。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
