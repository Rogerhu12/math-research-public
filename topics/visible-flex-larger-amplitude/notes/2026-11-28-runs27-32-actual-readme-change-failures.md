# 五个旧运行的真实 README 核查异常

2026-11-28，Astra-larger-e4e2a2bf-20261126。**实际运行证据，不是新的科学数值结果。**

## 已确认的原因

公开诊断 run46137684288/1 已自然成功，在 runner 逐一读取27、28 R729接续、29 retry、31、32各自的完整官方 job 日志。五者各自的完整 traceback 都从真实进度发布调用到其自身控制器的 Publisher.sync，最终因 README 变化抛 RuntimeError 并退出1；已读的根§16变化另见 HANDOFF。这里的归因来自五份独立日志，没有借旧33的错误代替。

它们没有给新的自然科学final。原accepted/current/trial、全部K地点与六族、未返回final/typed/后继pure的边界仍见原own note和固定旧open；一次控制器异常不能补出被打断子进程的结果，也不证明数学目标不可解。新33 retry、34、35已用当前读过的规则继续完整求解。此前“原因待自身日志”是当时状态，本条补上现在已实际查明的原因，保留旧原字。

## 全部原证据身份和真实拉取记录

每份元数据完整保留官方run/job/steps、全部原错误行与完整trace、实际恢复run/source、每个已读规则commit及原raw日志身份。原raw只留runner，不上库。下列固定whole字段是完整来源，不是摘要报告的替代。

```json
[
  {
    "run_label": "27",
    "run": 46105138690,
    "job": 140856083740,
    "execution_step_end": "2026-11-28T09:42:12Z",
    "official_job_end": "2026-11-28T09:42:20Z",
    "whole_failure_metadata": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run46105138690-job-failure-metadata.json",
      "bytes": 9599,
      "sha256": "aa1c10caeef91c4256ce3520086e44cb7e9471a6d7f5b1249667cb6f5a233ac8",
      "git_blob_sha": "06b92eebfe6845f5e5bf85ae198d5c8950f02ebf",
      "fixed_commit": "6565f666877ddd1a5bc03fe0b9e9a313f8906052"
    },
    "whole_original_log": {
      "bytes": 852323,
      "sha256": "e2da6d352c0c3e79d320b2c2e5957de32ded20a6a82f29e4276bba948d5dfa86",
      "line_count": 8097,
      "complete_log_only_on_runner": true,
      "raw_log_committed_or_uploaded": false,
      "decode_replacement_used": false
    },
    "rules_read_commit": "23ef2bf82f5ac7ed5e82082526a7004535ad7410"
  },
  {
    "run_label": "28 R729接续",
    "run": 46108296054,
    "job": 140865899880,
    "execution_step_end": "2026-11-28T09:39:52Z",
    "official_job_end": "2026-11-28T09:40:01Z",
    "whole_failure_metadata": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run46108296054-job-failure-metadata.json",
      "bytes": 9599,
      "sha256": "a51eaa2b0c93a39a6f91ce57f1d3da5fa312a0f116ddda014bb1c73834aba8af",
      "git_blob_sha": "d6bfd092c38ec03b474b4fa6be4672a7e59dd166",
      "fixed_commit": "6565f666877ddd1a5bc03fe0b9e9a313f8906052"
    },
    "whole_original_log": {
      "bytes": 803407,
      "sha256": "6a52d249fd87b01c55e8b580916e323fdf7e732569ad0979d4bab3fe06a0792d",
      "line_count": 7078,
      "complete_log_only_on_runner": true,
      "raw_log_committed_or_uploaded": false,
      "decode_replacement_used": false
    },
    "rules_read_commit": "33d2901d95dd221c30bfdefaa6f572047a4a7620"
  },
  {
    "run_label": "29 retry",
    "run": 46112781312,
    "job": 140879807850,
    "execution_step_end": "2026-11-28T09:40:43Z",
    "official_job_end": "2026-11-28T09:40:48Z",
    "whole_failure_metadata": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run46112781312-job-failure-metadata.json",
      "bytes": 10051,
      "sha256": "e86dfcde1e533d16f46392ab7a464791cd3815feb8f8fa6ceafdfe7efd7c027e",
      "git_blob_sha": "43278510e704cbc951b74eb712b4b980aa7328f7",
      "fixed_commit": "6565f666877ddd1a5bc03fe0b9e9a313f8906052"
    },
    "whole_original_log": {
      "bytes": 721948,
      "sha256": "a946438eb52e19acc86b41ce18675a21bdb62b0906fbde925113e839ed327e5e",
      "line_count": 6874,
      "complete_log_only_on_runner": true,
      "raw_log_committed_or_uploaded": false,
      "decode_replacement_used": false
    },
    "rules_read_commit": "d0510b17ef41ac14709474746563dec022f4d902"
  },
  {
    "run_label": "31",
    "run": 46122200592,
    "job": 140908938124,
    "execution_step_end": "2026-11-28T09:40:18Z",
    "official_job_end": "2026-11-28T09:40:24Z",
    "whole_failure_metadata": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run46122200592-job-failure-metadata.json",
      "bytes": 10051,
      "sha256": "4b2646637ed0255cc5050891a8c941cb51616a81178ba1e79fdde2192bd5c068",
      "git_blob_sha": "c533f998dcda27e843b6f152d06bf54e537ea075",
      "fixed_commit": "6565f666877ddd1a5bc03fe0b9e9a313f8906052"
    },
    "whole_original_log": {
      "bytes": 433426,
      "sha256": "459e8c42defa3595b3ddc43087e46530e53f34bbf859a1fe9fdfcb52486f694d",
      "line_count": 4129,
      "complete_log_only_on_runner": true,
      "raw_log_committed_or_uploaded": false,
      "decode_replacement_used": false
    },
    "rules_read_commit": "50ab45ef37db6678f59719354f4394ad3496b4a3"
  },
  {
    "run_label": "32",
    "run": 46125006601,
    "job": 140917553486,
    "execution_step_end": "2026-11-28T09:41:49Z",
    "official_job_end": "2026-11-28T09:41:53Z",
    "whole_failure_metadata": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run46125006601-job-failure-metadata.json",
      "bytes": 10051,
      "sha256": "eda095b6d286b30d6046fbbea975951a1ab42b02bd81fbcaf55ce34c571c8632",
      "git_blob_sha": "6c702e4c528b68e8d9fdc534d6cf9d435818c6b4",
      "fixed_commit": "6565f666877ddd1a5bc03fe0b9e9a313f8906052"
    },
    "whole_original_log": {
      "bytes": 313125,
      "sha256": "cda0f8ca5f2b27506a53a826b4ce75188612ae780259371fa8c1011eeb8a4ee1",
      "line_count": 3016,
      "complete_log_only_on_runner": true,
      "raw_log_committed_or_uploaded": false,
      "decode_replacement_used": false
    },
    "rules_read_commit": "9667d571a2f7d4af8f9791c05ccff8ea296da8fb"
  }
]
```

后继：继续当前完整科学计算，不重跑已终态的旧配置来重复其已登记结果；有必要续接时仍遵守自身完整final/typed/source的合同。
