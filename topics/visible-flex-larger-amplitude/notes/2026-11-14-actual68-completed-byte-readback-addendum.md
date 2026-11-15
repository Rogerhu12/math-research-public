# 实际68附记：公开Actions完整原件字节读回已完成

分类：原科学产物保全与只读审计；没有重新运行科学计算。  
作者：ChatGPT（amplitude，AI辅助）。  
日期：2026-11-15 UTC。

## 1. 后续读回及范围

[实际68正式结论](2026-11-14-actual-request68-twenty-one-query-nearest-left484.md)
先依据CLI取得的五个原报告/父场文件记录了真实结果，并明确当时尚未读取
全部大数组。随后本仓公开只读工作流已经完成此范围：

| 身份 | 值 |
|---|---|
| 只读run/job | `43655562831` / `132633181022`，全部步骤success |
| 只读source commit | `61551535031de3bced001d7fb4926938c708a028` |
| reader | `root_20261114_read_completed_twenty_one_prefix.py` |
| reader SHA256 | `0feeb16e350d06ed03abb93c8ff80dd6e9e10a2703d47135f3c36ee3c289ea3a` |
| 原science run/source | `43653811809` / `9ad4c5d56a85ba952d6e9a538c49fbd3aae4fa14` |
| 原artifact | `14137921466`，`visible-followup-condensedqp-43653811809-1` |
| 原ZIP | 590574983B；`0fe545ea42c48bb2d5551afddb86190af3c7ff1a14509b9f1ed5a6e5d0e53784` |
| 只读完成时刻 | `2026-11-14T23:55:23.225488+00:00` |

工作流按显式原run/artifact/source/SHA下载并校验完整既有ZIP，再只读原报告、
producer和数组字节。使用冻结transport
`51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。
没有重新构造科学RHS/J、进行矩阵动作、求解、优化或native调用。

[已发布完整小summary](public-actions-43655562831-1-receipts/request68-readback/completed-prefix-readback.json)
为60364B、SHA`f7b050ce2f8c16e5ad0307aaa00a204db49150e89cce69238ad47e06d9d7179b`，
明确`completed=true`、`byte_audit_completed=true`、`phase=complete`。
本附记直接读取该原小文件及另两份独立小报告；没有再下载590MB原ZIP，
没有经connector传输大数组或完整723KB详细审计。

## 2. 已完成的原字节范围

原Actions回执记录以下实际范围：

| 已审对象 | 原回执数量/身份 |
|---|---|
| domain NPZ/NPY | 190个NPZ、1226个NPY数组 |
| 原B模型 | `7e5512fa872b45e87fd88e5a2a0c4857ab8881fef8a2e47b3d78b77075486bcc` |
| 完整typed query/列映射 | 21组全部通过原global→local整数映射核 |
| condensed NPZ/完整数组 | 108个NPZ、38个完整数组、42个数组引用 |
| R270 root/affine/recovery raw | 14个文件，共415120992B |
| source SHA | 62个源逐字核；缺少的源声明为0 |
| 原midpoint文件 | 每个实际文件均有原descriptor |
| 完整QR因子文件 | 原producer没有导出；未宣称独立因子payload审计 |

实际68仍是旧21-query布局：声明7101列，实际B编译列并集6763，node484
的338列在该旧模型中为零；实际端点20个。reader已核这两套索引、零列
身份及21组block映射，未从零列推出原H不包含该节点，也未重新计算H。
这个历史事实与后续拟增加left484的22-query实现有明确区别，不能把新
模型身份写回实际68。

完整明细`large-arrays/complete-original-byte-audit.json`为723383B，SHA
`2e5b678efa113789649c15b893e07d93fdd94fef4ab44086e308a1d11e0e8abb`，
保留于只读artifact`14137659013`：
`visible-completed-readback-43655562831-1`，784011B，API记录ZIP摘要
`e148edcd9304342042fd311a768dfb1b43f6837b5345693f8da621367822bc5c`。
本附记只引用该artifact身份；不把未重新下载的只读ZIP描述为本地再次
验过的完整包。

## 3. 与先读原件的交叉一致性

已发布summary重核actual66父warm/status为`80b4590f…`/`04ace795…`，
整个历史producer保留；实际68新warm/status仍为：

- 原压缩warm：4827392B，
  `3f45b939752cbe338ab5037a481ee2639b40783950ca4664d23c8ff168f4d535`。
- 原JSON status：2007513B，
  `f4de267f1630201fb077b9d6245016760868f9a20a5b4624db08e780ce2f90e9`。

原status、新warm及FD的完整producer绑定通过，success及
new-coupled-finite-acceptance继续为false。本地将已保存的先读原数值与
新公开小报告作131项逐值/字节身份比较，全部一致；仅比较保存值，没有
本地新dot/norm/权重或科学计算。两种小报告对observer字段的压缩方式
不同，交叉核使用相同原字段及数组身份，不要求它们整份JSON结构相同。

接受步仍为$\alpha=1/8$，当前固定权重merit从`43.75526502490638`
到`43.704499218930515`。最近$\alpha=1/4$所有原节点、中点及21个
建模网格有效，实际merit下降`0.09253669240028017`，但原双RMS唯一
失效left484的$\beta^2=-0.04104689346427315$。只读结果没有改变先前
的下一模型选择，也没有把新增left484当成已经成功的科学结果。

新warm物理col最大值仍为`0.007108973872610448`；原observer定位
interval461、radial mode1、row155819，原固定权重
`199.05060973500673`。FD误差仍为`9.83834122423049e-10`，通过原
`5e-5`门，但明确使用完成的零H全J之affine图，未求解当前非零H的
native尾。完整联解、闭面和研究目标均未由此获得验收。

## 4. 小文件来源及可复核记录

- [QP原标量](public-actions-43655562831-1-receipts/request68-readback/completed-prefix-QP-scalars.json)：
  16908B，`179ec1bc58b70ca410f21052327403bb10b86c54ff720b063bc058c0276fd3e7`。
- [FD原标量](public-actions-43655562831-1-receipts/request68-readback/completed-prefix-FD.json)：
  12683B，`928520c2214574f403db729a5feeb7f2ee638b0c769db71c703bd3183f40610c`。
- [只读请求/源绑定](public-actions-43655562831-1-receipts/completed-readback-request-identity.json)：
  2292B，`fcd969b8bb298e2a096f735f50de40465ee6a1631fc8e3f3fed4ce9da69fca2a`。
- [本地小文件交叉核回执](2026-11-14-actual68-completed-byte-readback-crosscheck.json)：
  23448B，`4a6bc88a31303a9391597c6b99813493623a8e08b194f2b87a304ad9c028d766`。

四个已公开小UTF8文件在本地保存后的SHA和字节数与其publication逐一
吻合。大数组审计已由这次公开Actions一次完成，本地没有重复该工作；
这些身份核查也不是新增的数学或非线性接受门。
