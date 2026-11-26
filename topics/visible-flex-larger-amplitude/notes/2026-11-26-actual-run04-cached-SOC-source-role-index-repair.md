# Run04 cached SOC 的实际来源角色索引故障与完整最小修复

日期：2026-11-26。范围：已返回的来源初始化故障、完整源码修复及同一实际父的重新排程；不登记新的数学、收敛或几何结论。

## 1. 真实失败及其范围

公开 run `45857104277/1` 的 stage41 使用 launcher `d0ba8ccd02a811c51cd7006f1c299ad4b7eff57c195ee3a772c38fef1431a434`、完整 driver `01b2a7777fea1979083c95d881da006d11885014c90c7f2dba7afd53d283aea9`，在 5.942594131000078 秒以 returncode 1 返回。只产生 command 记录，没有 report、initial-new-field 或 final。stage42 因其原 admission parent 是不存在的新 final 而 setup 失败，未启动纯 reader 子进程。

随后 stage43 以已存在的 actual40 final 作 parent，运行既刊纯归因器 `ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338`。它读取这次已返回子进程的实际日志尾部，明确得到：

```text
fullclosed_so3_cached_interior_separation_soc.py, line 405
soc_module = load('_so3_complete_fixed_parent_separation_SOC',
                  paths['complete_soc_rows'])
KeyError: 'complete_soc_rows'
```

实际日志仅 766 bytes，SHA256 为 `2f35867fc04d92328734c329c06c7489ff3915eedc412ebb2566765efb260000`。纯归因 report 为 1948 bytes，SHA256 为 `ea5dac76ce4e4a13fa3f01f2b0723f2a3ee411e24f59b5871e3b7decf446eea0`。子进程真实 source commit 是 `6dbfd17cb68f54fc4d9b6dfe7c6923291449a67e`。完整紧凑事实见 [实际运行第4卷](2026-11-26-public-actions-45857104277-1-part-004.md) 的 40–43 项；本次没有从连接器读取 actual40 的 23 MB raw report，也未读取任何科学数组。

这个失败发生在构造新 meridian/operator、初场残差、几何筛、方向或 SOC 之前。不能据此归因为几何不可行、迭代失败、缓存损坏或数学构造障碍。

## 2. 唯一 driver 功能更正

原完整 `SOURCE_PINS` 已登记角色：

```python
'complete_soc': (
    'scripts/resume_20261126/complete_normalized_parent_so3_rows_soc.py',
    'e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021'),
```

后续 restart 归因也已用同一 `complete_soc`。加载行误用了未登记的 `complete_soc_rows`。本修复只更正这一处索引：

```diff
-    soc_module = load('_so3_complete_fixed_parent_separation_SOC', paths['complete_soc_rows'])
+    soc_module = load('_so3_complete_fixed_parent_separation_SOC', paths['complete_soc'])
```

28 个来源角色及其路径和 digest 整段逐字不变。AST 提取整份 driver 的全部 21 个字面 `paths[...]` 消费角色，均属于该登记表。没有新增别名、放松任何 source guard，或把未知来源映成另一角色。

从紧接该行的 `reference_cache_module = load(...)` 到文件 EOF，完整字节与原 01b2 相等，该后缀 SHA256 为 `4a0984110b0c189813c874bc6eefafd11db0f1c74723b1599e62a0887678be20`。包括实际父/target 重建、全部原自由量、原 H² 坐标与阻尼单位、全部正权三 Gram 行、原 192 selector 和幅度前缀、Phase I、完整永久地址记忆、原 ray 回溯、最近较大合格拒绝 ray 的固定 SOC anchor、每轮所有 C 和独立 A z、两候选按同一 Phi 排序后的全新记忆真复筛，均没有修改。

原 helper e716、projection a2c6、cache 50a9、operator 234ac 和 provider d3f25 的完整身份也没有变化。该 cache 的同来源/模型/父/查询/字节绑定继续生效，未知或缺失 cache 项继续调用原 provider。

## 3. 完整来源链

四个文件沿原公开 basename 发布新普通提交；旧提交中的完整失败源码和实际记录保留。完整终版如下：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `fullclosed_so3_cached_interior_separation_soc.py` | 75059 | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| `launch_so3_cached_interior_separation_soc.py` | 11596 | `6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e` |
| `derive_normalized_parent_cached_soc.py` | 47221 | `424311d2a85ab74e14a8aeb3bdb3a0bf4f4cad07fd0abee6e4c4adef6113bacd` |
| `read_so3_cached_interior_separation_soc_report.py` | 55153 | `009e1e1d54ccd41e8ac2b4e6efe43541ebc327b7a6f3d4fa743e145517c897e6` |

完整 deriver 的对应 literal replacement 改为正确角色，并更新它绑定的 driver/launcher SHA。launcher 仅更新 driver SHA；reader 仅更新 driver/deriver SHA。完整 parser、source/body binder、归因算法和所有 actual output 语义保留。

## 4. 已实际完成的纯源码核验

恢复执行环境后只运行 Python 3.12.14 stdlib：

- 四份完整源码 AST parse、compile、重复字面 dict key/keyword 和行尾空白检查均通过；没有 import 数值模块。
- 新 deriver 对原完整 174b driver、9b87 launcher、完整 e716/50a9 输入实际执行 `--verify-existing`，14 个 driver edits 和 6 个 launcher edits 逐项唯一、完整重建结果与本次两个源逐字相等。
- 整 driver AST 的所有字面路径消费者均有已登记角色；launcher 去掉其专属 print/install 两 flag 后，完整参数 parser AST 与 driver 相同。
- 以上只验证完整源码、参数和来源接线，没有运行科学 fixture、F、J、root、QP、科学数据读取或几何复算。

核验不能代替下一次实际 Actions 返回。本 note 编写时修复后的科学方向尚未执行。

## 5. 同一真实父的新输出排程

完整两步参数见 [role-index 修复 ready](../computations/so3-cached-backtracked-SOC-role-index-fix-run04-ready.json)。

科学 parent 继续用本 run actual40 的完整已返回场：

- final `51c8b09be1b1d5baef8c0f5b18f294130727429aeb01485e1b78a72d442d509a`；
- report `78fa207b9032f3455ab3037189f0896f2533e4534c8e573d67a326444f442b22`；
- model `ac2cfc0d46a75a2070dfd9b208e3802c895a7bd35a9df5ab60d1016c81aebf19`；
- fixed scalar profile `2612418a7f6dd3718ec340a37e7793bbedee0a3423f90a4a15c028cdb80492df`；
- coordinate norm `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa`。

运行时仍由完整绑定器从实际文件独立复核这些身份。完整数值 argv 与 actual41 相同：metric 1×64、restoration 4×64、mu .01、15 ray、8 轮同父固定 anchor SOC、原 p4/epsilon .001/scale .05、原几何/幅度预算和全变量；唯一科学 argv 差别是 fresh 输出目录改为 `so3-closed-actual-profile-cached-backtracked-SOC-v2-first`。原同 runner `so3-closed-actual-profile-first/frozen-parent-meridian-cache` 和其真实 producer report 继续作为明确 cache 输入。

纯 reader 的 admission parent 也使用已返回 actual40 final，不依赖新 final 已经存在才能启动；reader 对 complete report 的 final 字节和 cache 字节验证保留。若新 report 本身缺失，纯读应如实失败，不伪造空成功结果。阶段41没有产生物理场或新的物理地址，保留实际失败 provenance；全部已有实际父、位置 manifest 和 donor report 的永久地址仍照原完整循环读取。

新的返回结果将另行记录，不能由本修复推定收敛、可行、连续证书或完成课题。
