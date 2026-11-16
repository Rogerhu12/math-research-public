# 原参数模三步作业的 Python gzip 运行时差异与窄修复

作者：Astra-ISP-789f / normal_annihilator；根代理独立复核。AI-assisted GPT-6 Astra Pro。

## 1. 实际执行范围

本记录对应 `invariant-subspace-r150-original-parameter-module-session.yml` 的 run `43876083196`、job `133329388393`。该作业实际使用 Python `3.14.4` 和 python-flint `0.9.0`。第一步完整重建原十行模型及 116 个带原 18 来源的种子成功；第二步在读取父 manifest 的精确物理 SHA 门处失败；第三步未执行。因此本次没有进入 Singular 自测、`slimgb`、单列 `lift` 或特征零来源提升。

| 实际步骤 | 执行源码提交 | exit | wrapper wall 秒 | 临时 raw bytes / SHA-256 |
|---|---|---:|---:|---|
| `original-ten-parameter-model116-180` | `1e6fea624ca81e448ad1263cb68efbb46eea6ed1` | 0 | 8.935467307999943 | 30924 / `de576deea6ebab864d37c668a731675175f5a11179e080c20a9ce62e780adac4` |
| `original-parameter-seed-compression50-180` | `9ac311d289b9be06dae36fb92b8c2770911adfc6` | 1 | 0.06426209699998253 | 739 / `af0bf11a943a93eabf20a692cb1d759c4c6bd154e91d2edfdab4b2bca53e13c7` |

第一步报告的计算时间为 `8.834459829000025` 秒，全部 116 种子、全部 50 原边界、11 原生成元、六均值源、34 坐标逆、578 Jacobian 及 17 梯度运输门均为真。第二步的错误完整文本为：

~~~text
ValueError: whole exact file original-parameter-module-manifest.json
~~~

第二步 elapsed 为 `0.0005072110000128305` 秒，`completePhases={}`、`nativeWholePhases={}`、`childPeakRssKiB=0`，故不能把该错误称作模压缩失败或数学负结果。两步的原执行身份分别已保存在：

- `notes/r150-original-parameter-module-execution-789f/43876083196-original-ten-parameter-model116-180.json`；
- `notes/r150-original-parameter-module-execution-789f/43876083196-original-parameter-seed-compression50-180.json`。

## 2. 全 118 文件的精确差异证明

已验证的本地构造使用 Python `3.12.14`。父 binding 在两次构造中完全相同：

~~~text
7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4
~~~

本地和远端父 manifest 均为 30466 bytes，SHA 分别为：

~~~text
本地：9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2
远端：fdbd94a274511f26446ef9091cdad291661d262908019c439d888f77a4b37c4b
~~~

根代理对原 118 个 gzip 文件共 8524425 bytes 做独立只读审计：先核每个本地完整物理 SHA 与解压逻辑 SHA，再仅在内存把 gzip header 的零起始第 9 字节从 `3` 改成 `255`。118 个所得完整文件 SHA 全部等于该次远端日志中的描述符，解压字节逐一保持相同。以这些描述符按原 canonical JSON 规则重建 manifest，恰得远端的 30466 bytes 与上述完整 SHA。根审计实际耗时 `0.626393157` 秒、exit 0；本代理另做同一完整比对，实际耗时 `0.564178188011283` 秒、exit 0。旧文件未修改。

本代理另由完成 job 日志恢复原第二步 raw 的 JSON 浮点身份，精确重得 739 bytes 与 `af0bf11a...53e13c7`。这只是原失败记录的字节回读，没有改写原回执或制造新执行。

Python 官方文档说明：3.11 起 `gzip.compress(..., mtime=0)` 可委托底层 zlib，从而使用其 OS 字节；3.13 起此 API 保证 OS 字节为 255。该版本行为与上述全文件实际比对完全一致。参见 [Python 3.13 gzip.compress 官方文档](https://docs.python.org/3.13/library/gzip.html#gzip.compress)。

## 3. 修复范围与新执行门

仅在既有 workflow 的 checkout 与 pip 安装之间增加：

~~~yaml
- name: Select the exact original model Python runtime
  uses: actions/setup-python@v5
  with:
    python-version: "3.12.14"
~~~

[`actions/setup-python` 官方说明](https://github.com/actions/setup-python/blob/main/README.md) 支持明确的 `python-version`；本次固定完整补丁版本，以原已验证构造环境重新生成整个父模型。

原数学 producer、compression driver/native/header、positive consumer、session wrapper、request、所有输入字节 pin 与 binding 均不修改。下一次真实独立 job 须重新通过旧父 manifest 的完整物理 SHA 门及后续全部原来源门；固定运行时本身不代替这些门。如果其余运行时差异仍导致字节不一致，仍按实际失败记录处理，不自动规范旧产物、不放宽校验。

本记录只确立运行时差异的准确原因和可复现窄修复。116→50 的既有本地数学结论保留；本次远端未产生新的压缩、单位理想或 Bell 自然幂结论。数组、raw 回执及完整 job 日志只保留于临时执行环境；仓库保留源码、参数、执行身份与 SHA。
