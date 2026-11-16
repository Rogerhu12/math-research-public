# 末槽恢复第二次实际：旧输入适配缺字段，LP64仍未启动

日期：2026-11-16。本文只消费唯一公开原运行的实际结果；没有新执行或重放原研究。

## 1. 原运行与准确到达点

[run43787979008](https://github.com/Rogerhu12/math-research-public/actions/runs/43787979008) / job133039809172，source `e9902534a82602c5a30c07093e48923c5c38ce67`，结局为 failure。

原请求40238字节，SHA256 `25822ee45cc6a5739911a8b7b3ac60db887fac581d94e0c7827a25716d4e5801`。原日志161704字节，SHA256 `acba51ac65206c2c34fc7f8761fdba1fa49ad88625f0839fd67cc279adf0d9b2`。根已读原规则、复用、错误与COMPLETE字段；REQUEST的168绑定及COMPLETE的158 Python来源逐项与已审请求相同。

原10.0时限已经通过修复后的数值检查。DEVELOPMENT_REUSED准确确认首轮旧源码11项全部通过；本轮开发组、检查、stub、旧优化与科学重放均为0。当前core不是被重新测试的旧core，逆文本类型补丁核对通过。原9项也只沿原source回执读取。

PRIOR_WORK_REUSED确认原MODEL28资格通过：63次LP=62 primary+1 SOC，58个value，原27个已接受点的标量轨迹保持；最后未用第64名额仍最多只授一个新primary，没有新的SOC机会。

## 2. 请求适配错误

调用栈准确到达：

```text
terminal_paid_slot_audit.main
→ terminal_paid_slot_transfer.prepare_transfer
→ frame_metric_expanded_pool_soc_transfer.reconstruct_checkpoint_field
→ request["source"]["coordinate_definition_sha256"]
```

原helper在第130行核对重建field与请求的coordinate定义身份。新terminal请求的source只带原run/原日志对象指纹，没有提供该旧helper要求的同名coordinate字段，因此抛出 `KeyError: 'coordinate_definition_sha256'`。

必要原输入准备函数已返回，错误发生在随后field重建接口的请求schema核对中；不能把这次失败称为原point或新候选没有下降。终端objective尚未成功恢复，新增普通value、J、模型、LP、SOC和接受点均为0。原COMPLETE的model_count为0、solver为空、selected point为空，新candidate也为空。

下一修复必须完整检查该helper以及后续调用实际需要的字段，把已验证原checkpoint/冻结身份通过明确适配传入；不能仅把首个KeyError隐藏掉、跳过身份校验或改原field/cfg。

## 3. 全部新增费用继承

| 费用 | 秒 |
|---|---:|
| 原direct完成累计科学时间 | 257.595331213 |
| 第一末槽类型失败后的累计 | 260.479586314 |
| 本次schema停止新增科学时间 | 10.578692648000015 |
| 当前同任务累计科学时间 | 271.05827896200003 |
| 本次进程总时间，单列 | 11.951187912999998 |

峰值RSS为295396 KiB。原63 LP/58 value没有变化，原64 LP/160 value/1800科学秒/单LP10秒上限不变。下一入口从271.05827896200003继承逻辑科学钟，在任何必要失败回执和原source读取之前开始计时；不能再次减去257.595或260.479来漏记这次费用。

本次进程总时间含导入等开销，独立保留，不再次叠加到科学钟。旧11和旧9不得重新执行；原关闭epoch及更早失败的账继续沿原note保留。

## 4. 原记录定位与规则读取

原JSON加LF的可核对指纹：

| 记录 | 字节 | SHA256 |
|---|---:|---|
| REQUEST | 28349 | `4c32d3abb5aeefbe93561a9be1005db97440fff735adfe821e222cfef89683b2` |
| DEVELOPMENT_REUSED | 5167 | `a62b33d5bbccd80e7e875a7b304487ebd78c510d75c1e941e1c4d6c042d6f97c` |
| PRIOR_WORK_REUSED | 8385 | `6151623d177c31d73a281b914e678da1badcf1ff0be4da096cd2a50095d35ee7` |
| COMPLETE | 30257 | `0eaeefa6f63acd661a06278e1f884c6f22f4d4813f3954afe7917c4e8826de8f` |

原audit临时文件31880字节，SHA256 `4186ca0a8de394fa0788eb6ceab63602ce8b170bbe7d0e6067192922eb8d5e5d`；其摘要33007字节，SHA256 `9f83439fc6f11fc155dd3be9ad8c17af15de9075d8b26a401d3f4a317d14434b`。这些对象只留原runner/stdout，不提交原payload。

公开实际pull时间01:44:35.239235→01:44:37.213931 UTC，head由 `e9902534a82602c5a30c07093e48923c5c38ce67` 到 `995be60842e3e118663bbea7187b6a4a51dbe6cd`。根与本题README原blob/hash均同、diff为空。

私有实际pull时间01:44:39.905599→01:44:40.866513 UTC，before=after `1d554734d1652efd655eeaf40d762e551234f736`；根README同、题README无，QUEUE中本session唯一进行中。根于01:46:33前读完，下一次实际pull最迟02:44:35 UTC。

当前没有新候选或改善，也没有消耗末槽。修复未完成的输入适配后继续；主README所有完成门仍须支付。
