# 第56批：旧启动及窗口描述的完整保全

日期：2026-11-28 UTC。状态：完整附件已保护为远端未引用 Git blobs；本说明不声称已经改动 main。最终发布与精确删除仅由 root 实施。

## 1. 范围与字节边界

本批只整理189个已经公开的描述性 JSON，毛字节为1,805,389：

| 原文件组 | 数量 | 毛字节 | 原写入时点 |
| --- | ---: | ---: | --- |
| actual41 的 step-window identity 与 actual54 的 direct-LD-window identity | 144 | 671,052 | 实际窗口积分之前 |
| 原 TailClient 的 *_intent.json | 32 | 807,926 | subprocess.Popen 之前 |
| 十三次 condensed 请求的 followup-request-identity.json | 13 | 326,411 | 科学步骤之前的请求／源字节检查 |

三组都已经完整读取各自的小文件。189个原 SHA-256、Git blob 和字节数全部来自实际原字节，没有填猜测值。所有原 JSON 字段都完整保存在四个参数分卷；重复字段只存一次，逐项变动仍全部列出。原字节也有固定 Git 对象恢复位置。

本批不退原始状态、检查点、完整科学响应、矩阵、field packet、stage report、原配置、原请求、spec、科学代码、证明、活动输入或新准备的 ready。18个 M94/M96 检查点、canonical live identity、parent91、未闭合的 ports／Nelder 对象均不在删除表。目录下未列出的文件一律不动。

## 2. 完整恢复锚

固定恢复提交为 `93c07e09fc0fe7b161a1f1ec313f2b712771096d`。收尾另在真实 main `9a9868c5e67083a3bd07563d0d8d2853a8bff52a` 的课题树 `74c4a0218ec11e0e3d483b8c71840645ee8642ae` 逐条核了189个 path／Git blob／bytes，全部仍与固定恢复锚相同。这是元数据观察，不代表随后 main 不再前移。root 发布时仍按最终鲜明路径逐项匹配，不按目录或文件名前缀删除。

完整删除表在：

- `computations/legacy-prelaunch-window-metadata-retention-56-provenance.json` 的 `delete_entries`。
- 每条包含准确仓库路径、原字节数、原 Git blob 和原 SHA-256。
- 对应的完整字段表、原 writer／reader 说明及原参数来源均由同一 provenance 绑定。

旧 reader 若要求原路径和原 whole SHA，必须恢复原 Git blob。规范化分卷保存全部字段，却不是原文件的替代 byte identity。重新序列化字段表不被宣称能产生原 whitespace、键顺序或原 SHA。

## 3. 两组窗口 identity 是什么

原 `geometry_20261114_native_rawcell0_step_capture_hook.mjs` 先由完整窗口 factory 生成 `windows.identity`，写出 `stage-NNN-step-window-identity.json`，之后才创建并填充完整状态、shape output、shape Jacobian、mean tangent 的流，并调用 `windows.run`。identity 本身没有这些数组或实际积分结果。

原 `geometry_20261114_native_rawcell0_direct_ld_capture_hook.mjs` 先读真正的 actual41 window、report、field packet 和完整数组，与新窗口的原参数逐项比较，然后写出 direct-LD window identity，之后才进入真实逐步运算。它的描述不能替代被读取的226维状态、local-A、Jacobian 或完整 step evidence。

两组各72个对象只有六类字段随原段变化：

- `stage`、`rawSegment`、`part`；
- `rawLeft`、`rawRight`、`original_port_ratio`。

每个 number record 的十进制值、完整 little-endian hex 和分类都原样保存。两组逐段这六字段实际相同，因此完整72行参数只存一次；两套完整 source／schema／guards／原源码插入文本分别保留。共同 `mu`、完整 profile/function SHA、真实 grid 来源、原坐标范围、state/shape 维数及所有声明一个也没有删除。

这里的 scalar port 参数是描述的完整原字段；并未移动任何 ports 数值 raw，也没有重新计算 port、步长、状态或雅可比。

## 4. 原窗口读者确实仍需要它们

不能因为文件是描述就声称从来不被消费。

`exact_20261114_rawcell0_step_system.py` 通过 `self.json_descriptor(report['identity'])` 读取原 window，并核完整源、grid 和阶段义务。direct-LD capture 也会读取旧 window，与真实 stage/input/source 逐项比较。后继 direct-LD system 保留完整原 base reader 与每个实际 step／array 的守卫。

因此可选历史恢复必须先从本批固定提交或原 Git blob 恢复准确 old pathname。原 metadata 分卷不能绕过这些守卫。只恢复描述也不等于拿到了原完整数组：actual28/41/54 的完整原输入、artifact／raw 恢复与既有缺失边界继续由 retention40、53 的完整台账负责。本批没有重新下载这些 binary，也没有声称远期 artifact 仍可取得。

原 actual41 的868个局部映射捕获、以及 actual54 的完整1372阶段方向与实际错误／未通过结论，仍由原完整说明和 retention53 行保留。这里没有将其升级为全局求解或研究目标通过。

## 5. TailClient 启动描述的真实边界

已完整取回的原 `exact_20261114_true_tail_client.py` 为19,526字节，SHA-256：

`1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`。

它先保存完整 runtime config，建立源文件／ready／配置身份和 node command，写出 `*_intent.json`，随后才执行 `subprocess.Popen`。这十字段描述中没有数值状态、solve response、J、norm、accepted iterate 或 checkpoint。

32个完整原 runtime-config 文件都仍在原目录；每个实际 whole SHA 同 intent 的 `config_sha256` 和 `source_sha256.runtime_config` 一致。31个实际原输入配置候选也完整读取，32个 intent 每个都找到本原 run 目录下 SHA 相同的完整输入配置。原配置文件全部保留。

89个共用的源／ready 身份与 retention55 已刊117-pair 来源表逐项相同。每个原 `input_config` 与 `runtime_config` digest 另按本对象保存。78个实际核过的公开文件名、原输入恢复 scope、原 commit、mode／quadrature 全量保留，不把旧78-of91的明确边界改写成新的全91读取结论。

## 6. Base command 不能冒充加 hook 后的实际命令

原 intent 的 `command` 是 TailClient 在调用 Popen 前记录的字面数组。若原调用者用 `observed_popen` 插入 import hook，实际执行的数组会多出该 hook。新参数表保留前者的原义，不把它贴成后者。

retention55 的各完整 native run 行保留了真正 augmented command、writer／hook、原请求及完整先前台账指针；actual41/54 的原 workflow、请求、spec 与完整调用者源也由已刊 retention40/53 保存。这里未删或修改这些真实命令和全部预算。

`actual_nonlinear_solve_started=false` 也是原 pre-Popen 写入值，不能据此断言整个旧 run 没有运行、失败或成功。原科学结果与失败责任不从这一个标记推断，完整已有结果台账继续原义保留。

## 7. 原 native history 读者的恢复合同

`exact_20261114_seeded_zero_tail_client.py` 会读取原 intent，并对 response/source/runtime/command 等身份做真实对照；`geometry_20261114_zero_rk_native_probe.py` 也硬钉原 `true-tail_intent.json` 并重读其 runtime 与完整源目录。

因此本批显式保留这些依赖，不声称“只有写者、没有读者”。历史重现若需要原描述，恢复准确文件即可；不改原 codefile/source/hash guard，不用归一化 JSON 冒原 whole SHA。当前新科学入口不因此新增任何恢复测试、重跑或准入步骤。

原配置、原科学数据与原 source 都不在本批删除表；其中曾由更早保全批迁出当前树的材料继续沿原完整恢复台账，不能因为本批字段完整就宣称那些数值材料已经重新取得。

## 8. 十三个 condensed 请求包装

十三个完整原 `.github/workflows/visible-larger-public-condensed-qp.yml` 都按其真实 source commit 取回，并分别核对 whole bytes／SHA。每个 workflow 中 wrapper basename 只出现于一次 pre-science write；其记录构造正文逐字相同。之后的科学命令读取原 accepted、prepared、anchor、config、parent warm／status，不把 wrapper 当数值输入。

但先前台账、来源读者仍可能引用 wrapper 的原路径和 SHA。它们继续指原对象，不能因整理而静默别名。

两份新 condensed 参数卷完整保留：

- 每个原 request 的所有字段与完整 source pin map；
- `verified_sources` 的每条文件名、字节数、SHA及原顺序；
- 原 repository／source commit／README Git identities；
- 原 raw request digest、wrapper digest 与二者不同的字节语义；
- 每次原完整 workflow、全参数 context、真正父 warm/status、真实结果与未完成责任在 retention41 中的精确引用。

request 对象本身没有裁预算、删字段或用摘要代替。原 `computations/public-condensed-qp-request.json` 及所有原科学 spec/config 均不在本批删除表。历史原 request bytes 仍由其真实 source commit 与原 digest 定位。

## 9. 四个完整参数分卷如何读

`window-parameters.json` 中，每条 record 指定 kind 和72行参数表的一个索引。其完整原对象就是对应 `common_fields_by_kind` 与该行的无冲突合并。每套原 top-level key order 也保存。

`client-parameters.json` 中，每行完整变动字段与共同字段合并；`source_sha256` 单独由89个完整共同 pairs 与本行两个配置 pairs 合并。原输入与 runtime config 的完整恢复 record 就在该行。

`condensed-parameters-a.json` 保存共同 root／request／source 表、完整 verified-source 行表与前六个请求；b 卷通过 a 卷的准确 whole record 引用同一组表，并保存其余七个完整请求。各 request 的新增 source map、完整变化字段及 verified-source 索引顺序均原样保留。

189个完整对象已按这些声明规则在纯文本／JSON 层逐字段比回原已读对象。没有数值运行、数组运算、原代码执行或新科学 fixture；这只是保证本次归档不丢字段。精确原 byte restoration 仍以 Git blob 为准。

## 10. 不以未知补成功

本批没有重新审计所有旧科学数学，没有测试旧 artifact 下载可用性，没有复现原优化器或取新的科学范数。旧 source inventory 的明确范围、未完成的 native/BVP/global goal、独立原失败及不明结果都继续保留。对于没有在本次范围内重读最终结果的早期 constructor intent，报告为未新增判定，不按 prelaunch false 推定终态。

所有既有完整 source／input／parameter／conclusion catalogs 只作准确记录引用，不另造近似数学输入，不将旧 g、旧场值或旧证书搬到当前活分支。

## 11. 发布方式

root 对完整189条逐 path／blob／size 实施普通提交；任何 freshness 不符的项应保持原树并重新核定，不能按 basename 扩大删除。只删除明确原描述文件，不能删除它所在目录。

所有新增附件每件低于100,000字节，保持完整原字段。source registry 中重复的全 workflow 命令和原参数通过既有 whole-record＋JSON pointer 引用；原文件本身不删，避免把保全账重新膨胀成另一份重复数据。

最终新增总字节及净释放量由 complete-delivery 总表给出。此前已刊 ret55 的文件、189项之外的原科学材料和当前活 runner 没有因本工作发生任何变更。

## 12. 执行与权限

本工作仅做远端小文本读取、Git元数据核对、字节摘要和完整 JSON 字段的无损组织。没有本地 science、AST、compile、benchmark、fixture、科学 replay 或额外独立审查门。未写 ref／queue、未运行任何求解、未删除远端文件。未引用 blobs 仅用于把完整可复核附件交给 root；是否已经真正发布必须以 root 后续普通提交为准。
