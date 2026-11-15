# 原七方向可恢复稀疏 Dixon：第一轮实际1085位

2026-11-15；Astra-ISP-789f；AI-assisted，GPT-6 Astra Pro。

**状态：实际整步进度已验证并保存，有理重建尚未完成。** 这不是七个真核或有理秩的新结论。完整算法与原来源运输见[接口](2026-11-15-r150-seven-sparse-dixon-original-interface-789f.md)。

## 实际运行

同一临时session run43679903558，step seven-sparse-dixon-original，execution source 1226d97d6af3b5fdd0a76422b08fd0f449d9bf61。自选数学600秒、每进程2048MiB、编译30秒、外部680秒；原生实际编译1.767998863秒，头/运行库均FLINT3.4.0，数学实际580.880945931秒，其中native577.454505061秒，外部未强制终止。

原生内部单位素数为536870923。它只用于本次精确求解，不作为另一条原矩阵模秩论据。已从0完整接至1085位，精度31466bit，全部每位2751×7整数除法验证成功。18次有理重建未返回满足当前完整单位等式的解；没有据此否定有理解。

对实际 $g_i=1$，状态保持
$$
A'Z_k=E-p^kN_k.
$$
每个完整位及重建前都保存真实 $Z_k,N_k,p^k$。本次状态为budget-exhausted，当前单位解和全原4367验证均为false；原4318密集调用、1567旧主元和既有正规形都未重做。

## 真实恢复身份

绑定 d687c38c8d9e70aea9bba5d981c2d86eeb34673999f4273badb5b3d8e4504017。

| 同job临时文件 | 字节 | SHA256 |
|---|---:|---|
| actual-scaled-sparse-seven.bin | 62404407 | 67f750606cc769cab84c05931d177a43aa2e6843a5042750973007b574830710 |
| native/inverse.bin | 30272084 | 276976d7b24894bce81811bccc8567d54af36ab1e4368fbbf740cc211849a70e |
| native/checkpoint-0.bin（当前活动槽） | 78339894 | bfdd9fa52c288019dedb860d4d4e9d94e119db954da9e24b2e4323e38376b026 |
| native/checkpoint-active.txt | 169 | e1dcb6aea053169849d42905f4b4e4341320a65c9995da9fcbf576bea08000bd |
| native/inverse-meta.txt | 166 | e57ce6012833b68ccb8d2d47ea25ffa9fd19b9aaf9fed18442bc6c3d12d1f284 |

上述均在 {work}/seven-sparse-dixon-original 下。完整临时总回执4152B，SHA256 02473b3383fc8d277a38bdeee52fd2a263e5393a806fe8ce550af1c2d09e7efa；[已推送小回执](r150-infinity-remote-session-789f/43679903558-seven-sparse-dixon-original.json)保源码、实参及各层身份。

包装器SHA256 c1e5c4e8fd03d852a08150f7cf70d65769f3b17c640e870d7cc7389f7eeda5a0，native源码SHA256 0bad7fcf2973d9a8d1f76250ca40f93bcdaaab8abeaea884ab4deba5d02824e7。原输入、列内容、行尺度和旧消费者的全部绑定保持。

## 接续决策

下一步先检查同一4354选列的纯切向小投影秩。若该有理上界已能与原模31下界夹成完整常项秩，就先使用这个完整证明，而无需等待巨大显式有理来源；这不把未返回的native标为成功。

若仍需显式七方向，使用同一源码、同一out和同一绑定恢复1085位，复用实际模逆和完整输入，绝不从零重启。只有恢复原列坐标、1567逆代及全部原4367残差后，才按这条数值来源路线记新真核。所有可重算大数据仅留本job临时，不上传Git或Release。

