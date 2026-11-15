# 独立 native-live SDK 完整锁构建：Actions 草稿

类型：依赖构建与源码接口；作者：ChatGPT / amplitude；日期：2026-11-15 UTC。

## 唯一入口和范围

请求字符串为 `storage-sdk-build-20261115`，不占科学请求编号。仅当main分支上的 `topics/visible-flex-larger-amplitude/computations/public-native-live-sdk-build-request.json` 改变时触发唯一独立workflow；没有手动第二入口，没有原73成功锚、native、prefix、FD或supervisor调用。

提交位置：

- `.github/workflows/visible-larger-public-native-live-sdk-build.yml`
- `topics/visible-flex-larger-amplitude/computations/public-native-live-sdk-build-request.json`

本目录 `sdk-build-driver.mjs` 是workflow内here-doc的逐字审阅副本；静态检查已核二者一致。它不需要额外提交为计算源。workflow首次在Actions输出目录保存此原脚本及完整workflow/request字节，绑定实际触发commit。

## 实际构建顺序

固定包为 `@actions/artifact` **2.3.2**。Node固定 **24.22.1**，沿本题原71/73入口；npm使用该Node分发自带版本并保存实际完整版本，不猜一个尚未执行的npm版本。

1. 在全新 `lock-generation` 目录写没有scripts的实际package.json，只含该精确直接依赖。
2. 真正执行 `npm install --package-lock-only --ignore-scripts --no-audit --no-fund --registry=https://registry.npmjs.org/`，保存stdout/stderr和实际exit/signal。
3. 原样保存真实package-lock.json，不本地伪造锁、版本或integrity。核非root包条目的version/resolved/integrity完整，记录实际包数及声明安装脚本的包名/版本；声明有脚本不等于构造器必须执行脚本。
4. 将原package和完整lock逐字复制到另一个全新 `clean-ci` 目录，执行 `npm ci --ignore-scripts --no-audit --no-fund --registry=https://registry.npmjs.org/`。前后package/lock原字节必须相同。没有复用先前node_modules。
5. 仅加载安装的SDK、核包名/版本和构造器类型，再 `new DefaultArtifactClient()`。不调用upload/download/list/get/delete，不启动scientific模块或后台supervisor。artifact runtime和API token在此探针环境中移除。

如果安装或模块加载失败，保留原错误、原日志、lock和已完成阶段。不会自动启用脚本重试或换SDK版本。若存在具体依赖问题，应据真实失败回执处理；当前不宣称ignore-scripts已经被实际验证。

## 固定Action来源

| Action | 完整提交 |
|---|---|
| checkout | `11d5960a326750d5838078e36cf38b85af677262` |
| setup-node | `49933ea5288caeca8642d1e84afbd3f7d6820020` |
| ordinary upload-artifact | `ea165f8d65b6e75b540449e92b4886f43607fa02` |

权限仅 `contents: read`，无Git publisher、branch写入、PAT或部署逻辑。并发组独立且不取消已有运行，job20分钟/build15分钟为工程预算。

官方SDK source commit为 `c40bccc9c31c29df15c93abbea5b18bb474a4add`。已有7份官方小源的字节receipt，以及本次读取的 `packages/artifact/src/internal/client.ts`，支持2.3.2 API检查。该class没有自定义constructor；网络方法在各方法体内，当前探针不调用它们。本地官方client源9161 B，SHA `a3afe95a3bc50cf9cec82d3ba83ab56a57d84e45b0560f4b3258413992d53df0`。这不是对未来npm完整树已验证的声明。

## 保存输出与失败范围

普通固定 `upload-artifact` 的 `always()` 步骤仅保工程输出目录，命名 `visible-native-live-sdk-build-<run>-<attempt>`。它用于保存构建证据，不是用被测试SDK试运行新的artifact API。

输出包含原package、完整真实lock、实际Node/npm和平台版本、完整命令exit/log、原workflow/request/inline脚本及SHA、lock依赖与script声明摘要、ci前后字节身份、已安装SDK package/入口源码及SHA、constructor结果、最终build-result和输出清单。

`lock-generation` 与 `clean-ci` 不在上传路径内，node_modules不会归档或提交。没有人为截断完整锁的大小门。完整输出清单不自引用自身SHA。成功范围只是一种实际运行时/平台上由真实锁得到的一次干净安装；不冒第二次跨job复现、跨平台验证、artifact传输或完整supervisor恢复成功。

如果setup-node本身失败，job仍保已创建的purpose小文件和Actions原失败日志；不假装产生了锁或构造器结果。其余驱动异常均在finally保存明确失败阶段和已有输出。

## 静态状态

本地只进行了源码写入、YAML解析、2段Shell的 `bash -n`、inline逐字比较和Node语法检查。未运行npm安装、未生成package-lock、未加载或构造SDK、未上传/下载artifact、未执行科学、未改仓库或dispatch。完整静态回执为 [原静态回执](2026-11-15-native-live-sdk-build-static.json)；真实锁及其SHA必须来自之后唯一公开Actions运行。

主控已完整审读工作流、实际driver与request，单独复核2段shell/inline字节及Node语法。以上未运行陈述指准备阶段；发布后以实际Actions原回执记录锁构建结果。工作流6be68b21和请求0346c555保持原字节，唯一请求路径触发；不部署supervisor、不调用SDK artifact方法、不运行科学。
