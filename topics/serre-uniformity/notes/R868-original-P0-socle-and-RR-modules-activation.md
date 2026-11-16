# R868 原P0准确核与两图RR模块：首轮真实激活

日期：2026-11-16。本次激活原P0的271秩子式、完整K核、两图单极元及五个原Lj的254次点扭转模块。实际run在本push后查询；不得先填成功向量或128维RR基。

数学依据是[原R868证明](../results/R868-original-P0-pole-generators-and-degree254-RR-certificate.md)。首发表版本148d1e44到当前98e15284只更正YP/FM两条相对链接，数学逐字不变；方法的对应首链接也已改到正式results路径。

## 冻结源码与请求

- core：53344字节，cdac462c9f96011e4526cd7ad209e5fbd443d4c0e62e38cf31c04219ca525270。
- wrapper：42438字节，9115331ea60213edef3a3066c82aad4abd43e344dc566a5c5a8be8297ada9033。
- 证明：14742字节，98e15284b0c8c080eb01f1a53add7c4eef9ae56e8f10f02c4b8105fc7408d246。
- 方法：7977字节，aa91885fd2b652096e159ba5b00cca70849203e2d0e60d19624efb27bbdafb89。
- workflow：6853字节，c1dbef03116442ab4e46f651c6554d23a2a564aaacddcf72814356f8775ec8c6。
- 请求：32362字节，5020a1d7ee1ee643cb7789bbeaa06f555b510bba5c4e0113c395928cdadb5f85。规则已读提交1e82334d0a25510a822d3bf543a092ac8c5c0943；数学tag为d89c0ed6cbf0869191daed5c5e9a6075f4638140b5c9a89f1c486b4e818cda92，规则读号不进入数学tag。

首预算300分钟，最多8个合法候选素数和8192个Dixon位，仅为本轮控制。保留同tag全部已成列组/两模逆/当前残差和位，不因预算退出而重做。

## 当前真实输入

恰选80原件：R8057、R80645、R84910、R8569、R8609，总113762955字节，已按真实schema与原SHA核输入闭包。

- R805/R806仍保原producer身份，从当前R860 run43811325290的61成员载体109142444字节/5414b58f取出；61成员全部逐SHA核，未选的原R853件不另作为本次数学输入。
- R856只消费当前run43805659598的原P0两图值及既成点理想，不重新求点。
- R849原523节点图从当前R850 run43796696213的40成员载体398650918字节/a4c38c0e取得。该载体内旧395MB opaque成员仅流式核SHA，不打开其内部算术，也不续进本次80件最小载体。
- R849真正的eta_degree_zero_fractional_ideal根与原p/q、负Picard类号保留；不换成三倍的real_descent对象。

root已读完整core、标准库wrapper、方法、workflow及来源/请求。仅源码阅读、AST/YAML与真实IO；新矩阵、模秩、逆、Dixon、有理重构及K运输只由本公开Actions执行。

## 准确出口

一个合法有限素数上的同271子式在两K嵌入均非零，配原P0左评价给准确rank271。两个271阶模逆固定后，仅续一条542有理坐标Dixon。完整重构必须乘回全部272个原K方程并恢复每列尺度。

随后同一准确h给sigma运输、完整重叠多项式及两图
I_P0^-254=(1,f_chart^254)，再保十个原Lj目标模块。无巨型特征零det、无第二个独立kernel。

首成功旗标只覆盖真实socle、两图点逆理想和五个模块DAG。degree254_RR_basis_128_computed与original_connection_or_height_computed保持false；下一R872继续真正两权截面与128维核。机器产物与必要80原件仅一日artifact，Git不存raw。
