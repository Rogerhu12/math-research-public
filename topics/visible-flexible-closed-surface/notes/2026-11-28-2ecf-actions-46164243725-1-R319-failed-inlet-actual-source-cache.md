# R319-failed-inlet-actual-source-cache

**数值记录。** 2026-11-28 17:36:17 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `7f8643375d9b66300cab339b5ab374485133eb04`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

对已经退出的真实三剖面入口查同job实际源码缓存与已保存状态的存在/身份；不重算已成功数值。结果用于恢复具体失败原因与缺依赖，不能作为数学障碍。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R319-failed-inlet-actual-source-cache；实际源码逐文件摘要列于下方。开始 2026-11-28 17:36:12 UTC，结束 2026-11-28 17:36:17 UTC。退出码 0。

```json
{
  "schema": "actual-source-cache-after-failed-entry-v1",
  "sources": [
    {
      "name": "2ecf-r262-adjacent-cut-true-normal-angle-cauchy-refinement.py",
      "exists": true,
      "sha256": "4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa"
    },
    {
      "name": "2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py",
      "exists": false,
      "sha256": null
    },
    {
      "name": "2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py",
      "exists": true,
      "sha256": "494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae"
    },
    {
      "name": "2ecf-r262-cut-same-metric-banded-direct-newton.py",
      "exists": true,
      "sha256": "dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2"
    },
    {
      "name": "2ecf-r262-cut-frozen-native-and-true-material-position.py",
      "exists": true,
      "sha256": "d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f"
    },
    {
      "name": "2ecf-r299-actual-thick-arms-and-tapered-central-belt-v3.py",
      "exists": true,
      "sha256": "5b708cd97132731a995c0eb2a9aaf04b1dc9ce679ee0910ccd2305001b978d99"
    },
    {
      "name": "2ecf-adjacent-low-ports-0350-physical-belt.py",
      "exists": true,
      "sha256": "98cc2fcc1192195ac0615a4ce752e541665f1d64f775ff9cf92ee80e2e5957bc"
    },
    {
      "name": "2ecf-r262-true-three-arcs-cut-directed-position-kernel.py",
      "exists": true,
      "sha256": "ce0593ff10e6b0b07d2d4cae0eceaf649bc44d42785fd25f9cc161350a0a87d1"
    },
    {
      "name": "2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py",
      "exists": false,
      "sha256": null
    }
  ],
  "missingSources": [
    "2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py",
    "2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py"
  ],
  "outputs": {
    "adjacent-low/fixed-h1.npz": true,
    "adjacent-low/h1-physical-inlet.json": false,
    "adjacent-low/h1-physical-inlet.npz": false,
    "adjacent-two-moment/fixed-h1.npz": true,
    "adjacent-two-moment/h1-physical-inlet.npz": false,
    "adjacent-two-moment-060/fixed-h1.npz": true,
    "adjacent-two-moment-060/h1-physical-inlet.npz": false
  },
  "scope": "Filesystem metadata only; no successful scientific calculation repeated."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-live-failed-entry-source-cache.py: SHA-256 `2f323e113ecdd565f7909f4e214d8d30db0506b8c2830eb9c7eb317aa4b0f618` (1760 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `82a1e922cb947b8f7986d7b6a123c9bbed2ed878e85b1c0a2dedce3159e6ee97` (78638 bytes).
- 2ecf-live-failed-entry-source-cache.py: SHA-256 `2f323e113ecdd565f7909f4e214d8d30db0506b8c2830eb9c7eb317aa4b0f618` (1760 bytes).
- failed-inlet-sources.json: SHA-256 `dc55e715ad3fa8fe5df98e68a058d1e57bf3c3f88577699e5fea30770198874c` (2296 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
