# Run06 首次启动失败：规则来源提交不可fetch

日期：2026-11-26。本条记录的是控制器首次同步失败；科学recipe尚未启动，不是新PCG、几何或模型失败。

## 1. 实际运行和完整日志身份

- 公开run：[45903578703/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45903578703)。
- job：`140194901807`；workflow `visible-larger-normalized-parent-20261126-06.yml`。
- push HEAD：`7a771e602bbdb8ee25a845d8d690b27e2e4896bd`。
- GitHub记录created_at为22:15:14 UTC、updated_at为22:16:01 UTC；run/job结论failure。
- checkout、Python安装及依赖安装均success；第5步完整控制器failure。
- 实际短job日志为**32413B**，SHA256 **`0ecd1e8e0fe228d13c3944135dec1c6e841dfca84b6e4e13ec2d8c45b1bf0d04`**。

读取前先用HEAD确认完整长度小于100KB，随后核完整短日志SHA。本说明只保留下面定位失败所必需的准确摘录和完整来源身份；完整日志及其临时分析摘录不提交Git、Release或artifact，API凭据与临时signed URL均不写入文件。

## 2. 真正的退出原因

22:15:58 UTC实际stderr明确是：

```text
fatal: remote error: upload-pack: not our ref 3f766c95e204380341c7b562512d935ccfb165ae
```

完整栈依次落在：

```text
main(), line 247: publisher.sync()
sync(), line 60:
    self.git('fetch','--filter=blob:none','--depth=1','origin',self.rule_commit,capture=False)
CalledProcessError: git fetch ... origin 3f766c95e204380341c7b562512d935ccfb165ae
returned non-zero exit status 128.
Process completed with exit code 1.
```

首次request的 `rules_read_commit` 使用了本会话曾实际读取双README的本地提交 `3f766c95...`。该对象在后续非快进处理/rebase后不是此处可由公开origin fetch的提交。这是规则来源元数据不完整闭合的错误；不能把本地曾存在的HEAD自动当作公开可fetch身份。

request同时保存的两README字节SHA没有因此改变：根 `581402c2...`，本题 `3c1c03b3...`。但只有字节SHA不能支付原控制器显式获取 `rules_read_commit` 的前置责任。因此失败不能通过放宽fetch、跳过README比较或伪造旧提交来处理。

这次真实错误**不是HANDOFF大小拒绝**。根端另已将HANDOFF压到8938B以为06槽留足空间，该维护仍有必要，但不能把它写成本次实际栈原因。

## 3. 科学执行的准确边界

完整控制器source为 `public_actions_controller_parallel06_compact_metadata.py`，19006B、SHA256 `acff1a861a5e080fc014627b8021ff40c4fa9848e36ebfec91c4e5b49e1b256f`。

其main在首次 `publisher.sync()` 成功之后，才创建detached source worktree、核输入README、构造recipe命令和执行 `subprocess.Popen`。实际异常正发生在这次首次sync。因此本run没有启动原28段recipe，也没有执行bootstrap十二科学依赖或新PCG方向。这里不靠“公开索引缺记录”推断，而是由真实退出栈和完整控制流共同确定。

没有可继承的新科学场、目标精化、缓存、永久地点或数值结论；本失败不重复宣告任何旧数学结论。

## 4. 精确修复与续行规则

根代理应先真实pull并核双README，再选择**已经公开且可fetch、其README字节已实际读取**的提交，更新request唯一的 `rules_read_commit` 元数据，普通push触发新run。两README若有真正变化，则照既定规则只读差异并立刻遵从，不能机械保旧SHA。

完整controller、recipe、十二bootstrap对象、科学argv、预算、父输入及历史责任均不需要因这次错误修改。旧失败request与本记录保持可追溯；新run身份独立记录，不能把修复后的结果补到本失败run名下。

本说明写成时只登记实际原因与修复规则，不先写新run已经启动或成功。原科学未开始这一事实允许必要输入重建继续，但不构成课题完成。

## 5. 根实际修复

根已真实pull至公开提交 `28dbb9b17a47476f41d83782b90e059a6c0e0c67`，核根和本题README相对H所记提交无差异，两blob与已读SHA均一致。完整request仅把`rules_read_commit`从不可公开获取的3f766改为这个真实公开HEAD；修复后2860B、SHA256 `4dffef76945fcb596b88201bf83fb8d41a2b12bde28f95ca2e523792aead5c8d`。controller、recipe、完整queue、科学参数和两README SHA没有变化。与本说明同一普通commit推送request路径以触发独立新run；新run编号和实际结果待真实返回，不补写到首失败run。
