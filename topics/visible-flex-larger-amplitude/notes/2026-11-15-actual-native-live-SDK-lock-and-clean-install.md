# 原生 live 存储 SDK：实际 lock、干净安装与构造器回执

- 日期：2026-11-15 UTC。
- 作者：geometry。
- 分类：工程依赖构建与原件字节审计；没有数学结果或新的科学验收门。
- 状态：真实公开 Actions 工程构建完成；本地仅原件读取、SHA、JSON 与源码字节比较。

## 1. 实际结论

`@actions/artifact@2.3.2` 已在实际 Node `v24.22.1`、随该发行版记录的 npm `11.19.1` 环境中生成完整真实 lock。随后在另一个新目录从该 package/lock 执行 `npm ci --ignore-scripts --no-audit --no-fund` 成功，package 与 lock 前后字节完全不变。安装后的 `DefaultArtifactClient` 模块加载和构造器成功。

这些是本次原 `build-result.json`、两个 npm 阶段回执、`install-source-preservation.json` 和 `constructor-check.json` 的直接记录，并由完整 artifact 字节核相互确认。没有使用手写 transitive lock，也没有为了完成构造器而启用 lifecycle scripts。

本次 producer 没有调用被测 SDK 的 upload/download/list/get/delete API，没有运行归档 supervisor、restore 程序、native 求解器或任何科学模块。普通固定版本 `actions/upload-artifact` 步骤保存了工程回执；不能把该工作流上传步骤误算为被测 SDK 的集成测试。

## 2. 唯一公开运行与原包身份

- [实际运行 43668049747](https://github.com/Rogerhu12/math-research-public/actions/runs/43668049747)。
- 工作流 `.github/workflows/visible-larger-public-native-live-sdk-build.yml`。
- Source commit `7181b75a7fdee17989c7f619d480770eae503560`。
- Job `132671745626`，名称 `Generate a real SDK lock and check a scripts-disabled clean installation`。
- 官方 run 创建时间 `2026-11-15T02:29:47Z`，最终更新时间 `2026-11-15T02:30:11Z`；run/job 均 `completed/success`。
- Artifact `14142453799`，名称 `visible-native-live-sdk-build-43668049747-1`。
- 官方 ZIP 大小 **50,209 B**，SHA256 `b142c1862116defc2f44f0c7f98337e5d613e0f0f45830f7706d371e9ae705be`。

官方元数据通过 GitHub 的 run/jobs/artifacts 只读接口取得。主控唯一下载并核 ZIP SHA/CRC；本次审计没有再次下载。原包实际目录为 `/tmp/visible-larger-recovery-2207/actions-debug/visible-native-live-sdk-build-43668049747-1`。

工作流原件 **16,508 B**，SHA256 `6be68b21a7491e4908f064a18ae68edd457b3b5a6e19e4fca176924657e382c5`；request 原件 **2,072 B**，SHA256 `0346c555ef79bc5f9da7e87b36e8ce08935d2e7b970db1fb1b19b009ec1a2f3a`。两者均与该 commit 的真实 Git 对象逐字相同。实际执行的 `sdk-build-driver.mjs` 是工作流 heredoc 的完整原字节：**12,357 B**，SHA256 `9fe4f7290fe76e1584adfee64587b63d7a7b18441c521cb4322892d188235dc9`。

本 note 不用 workflow 的 success 代替工程细节；以下结果均来自其完整实际原件。

## 3. 真实运行平台

原 `runtime-versions.json` 记录：

| 字段 | 实际值 |
|---|---|
| Node | `v24.22.1` |
| npm | `11.19.1` |
| platform / architecture | `linux` / `x64` |
| runner OS / architecture | `Linux` / `X64` |
| runner image | `ubuntu26` |
| runner image version | `20261111.196.1` |
| V8 | `13.6.233.17-node.58` |
| OpenSSL | `3.5.9` |

完整 `process.versions` 已原样收入 literal readout；此处只列识别本次环境需要的项目。`runtime-versions.json` 为 **909 B**，SHA256 `4869327a0f2e373273968cff22fef7bb9d964f60bdf796255711057a0aa46500`。没有在本地另运行 Node/npm 去替换这些原值，也没有安装另一版本 npm。

## 4. 实际 package 与完整依赖 lock

新 package 的唯一直接依赖为精确 `@actions/artifact: "2.3.2"`，`engines.node` 是精确 `24.22.1`，private 为 true。

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| `package.json` | 197 | `3876fc4e5627d91624338ee976b4d101d40a58df58a6809b45912a9cd5fa001c` |
| `package-lock.json` | 128,535 | `9451fd2e058f7c0334b233bfc3ffa7a11d81c812cd26f8d4d245eb9ca5a0a4e7` |
| `lock-verification.json` | 627 | `bd74148e959361f22aae68f26715a7882275a2f07af23950d905d340c7705fef` |

原 lock 的 `lockfileVersion` 为 **3**，除根包外有 **266** 个 `packages` 条目。完整解析全部条目后，version / 非空 integrity / `https://registry.npmjs.org/` resolved 字段缺项列表为空；这与原 producer 的 `entries_missing_required_registry_integrity: []` 一致。`packages_declaring_install_scripts` 原记录和完整 lock 中的 `hasInstallScript === true` 清单均为空。

上述是完整 lock 的结构和来源身份结果，不是各依赖代码的安全审计，也不是对所有可能 package scripts 的一般结论。实际 npm 命令明确带 `--ignore-scripts`，本次没有启用安装脚本。完整 128,535 B 原 lock 保留在工程 artifact，没有重序列化；以这份原件的 SHA 作后继依赖输入身份即可，不应再凭本文重建 lock。

## 5. 两个实际 npm 阶段

第一阶段在独立 `lock-generation` 目录执行：

```text
npm install --package-lock-only --ignore-scripts --no-audit --no-fund --registry=https://registry.npmjs.org/
```

原 receipt：exit code **0**、signal `null`、launch error `null`。stdout 原文为 `up to date in 5s`（含原换行），stderr 为零字节。原结果还明确记录此阶段没有生成 `node_modules` 目录；后续安装使用另外的新目录。

第二阶段在独立 `clean-ci` 目录，先复制刚生成的 package/lock，再执行：

```text
npm ci --ignore-scripts --no-audit --no-fund --registry=https://registry.npmjs.org/
```

原 receipt 同样是 exit code **0**、signal `null`、launch error `null`。stdout 原文记录 `added 266 packages in 3s`。stderr **277 B**，保留了原 npm 对 `glob@10.5.0` 的 deprecation warning；这不是本次安装失败，本文也不将关闭的 `npm audit` 冒充已完成。

两个原 command/exit/log descriptor 与 final result 的 `stages` 项逐字段一致。阶段回执 SHA：

- `lock-generation.json`：`3159ffc1e15288587834dc1bb960f66ae58f2b81ceb7b311d6ca97b11d378f2b`。
- `clean-npm-ci.json`：`f2717564c1a629121ddd56af870d4462d98d112c1ae3240be2182a166656da58`。

`install-source-preservation.json` 显示 package_before=package_after、lock_before=lock_after，全部长度/SHA 同第 4 节原件，并报告两次完整 byte equality 为 true。本审计再次将这些 descriptor 回核实际 artifact 原 bytes。该 preservation receipt 为 **694 B**，SHA256 `80ac5af53b6baea0c2f243c696289cbef8f6bfdd2904a85596ccec8c3693b514`。

## 6. 安装后构造器的精确范围

实际安装包 metadata 为 `@actions/artifact` / `2.3.2`。producer 保留了该安装包的 package 和真实解析出的入口文件副本：

| 原安装对象的保存副本 | 字节数 | SHA256 |
|---|---:|---|
| `installed-sdk-package.json` | 1,782 | `0452d4f819353b9b92bcdac189fc3221d5c16ddf4bacba2ad8e4c23d238212b7` |
| `installed-sdk-entrypoint.js`（原入口 basename `artifact.js`） | 1,096 | `1badcb30279b273f258ea73fabf9805d886225b0e74b62caa8cbec923890d271` |

真实模块导出包括 `DefaultArtifactClient`；它的类型为 function，`new sdk.DefaultArtifactClient()` 和对应 `instanceof` 检查成功。原 `constructor-check.json` 为 **1,008 B**，SHA256 `781991e893e2835aa19d93e41bc7daa1277c8580821d5d80be835f872ea7e1b8`。

原 producer 在 SDK load 前移除了列明的运行时 artifact/API 凭证环境变量；其 `artifact_API_methods_invoked` 为 `[]`，`runtime_artifact_credentials_inherited`、`lifecycle_scripts_enabled`、`scientific_module_imported`、`supervisor_launched` 均 false。完整工作流和 inline driver 已作真实源字节比对，实际执行范围与这些字段相符。

所以本次已支付的是：**这一记录平台上，从实际生成 lock 的一次干净、禁脚本安装及模块/构造器加载**。没有支付第二次独立安装或跨平台复现，也没有支付上传、下载、校验回取、文件回收、后台 supervisor 和科学进程并发时的资源表现。

## 7. 本地只读字节审计与原结果身份

完整 manifest 含 **20 个原工程文件**，另有 manifest 自身。所有文件的完整长度/SHA 均回核，输出目录中没有未说明的工程 payload 或 node_modules；主控下载完成标记作为 transport 记录单列，不混入原 artifact 清单。

本次脚本还检查了：精确 triggering Git source、实际 heredoc、完整 package/lock 结构、原 npm stage 与 log descriptor、前后 source-preservation、安装包/entrypoint alias、constructor 与 final-result 字段、全部 runtime 原值。**120 项检查全部通过。** 全过程只用文件、JSON、SHA、字符串与只读 Git 对象；没有执行 npm、安装依赖、导入 SDK 或运行科学。

主要原结果：

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| `build-result.json` | 4,948 | `f75b426f0b8929a21c953b28c09b6f9182845ee8b355f67991c36ce0a7ad8465` |
| `build-output-manifest.json` | 3,409 | `5c9e69d1bd7994d450501c5dfe9883a310bc4e33890f11cfdec45b206aac1bf9` |

伴随交付：

- `2026-11-15-actual-native-live-SDK-byte-audit.json`：完整 120 项检查及逐原件身份。
- `2026-11-15-actual-native-live-SDK-literal-readout.json`：实际 result、request、版本、package、lock-verification、constructor、两阶段原日志等字面读数；完整 lock 的原 bytes 仍在 artifact，不改写为新的 lock。
- `official-metadata.json`：本次 run/jobs/artifacts 官方只读回执范围。
- `read_sdk_build_bytes.py`：本次纯字节审计脚本。

依赖 lock 这项工程缺口已经得到真实回执，可以把精确 package/lock 作为后继独立工程接线输入。现有原 native 科学失败、成功 anchor 要求、每次完整数据保全与 fullDN 资源成本没有因此改变。
