# 自然帽/body初态的部分实际回执、分布接口修复

日期：2026-11-14。root与repo_sources独立核公开来源/输出；只分析已经发布的数据。本次没有本地真实候选评价或优化。

## 1. 执行状态与保存边界

公开 [run43616419217](https://github.com/Rogerhu12/math-research-public/actions/runs/43616419217)，执行source2641fce00a9b6d30c9c877803dfe579b6d14f606。三个人工检查及两个输入SHA门通过；真实原c0的粗网格与两类线性诊断完成并原子写入。16:36:37 UTC在第一个case的细网格分布调用中抛出TypeError，作业failure；publisher成功保全4份输出。

错误调用将NaturalCapGrid对象与整数8传给了要求radial、theta数组的distribution接口。未改变任何数学参数，也不是一个几何不可解的结论。该时刻保存的main JSON只有original_c0一个case，不含GH加密、fine、distribution或c1键；已算但未原子落盘的中间量不作为本报告证据。

root从实际source commit逐件git show核83份来源的原字节、长度、SHA；4份输出stored/raw全部匹配。source独立再核16个实际依赖、完整model/bundle、234个原c0准确有理系数与5个准确零body控制。receipt最后已读规则提交f08dda0dc41140948b88209a74b8fb94bda8d733，两个真实pull均核双README无差。

| 输出 | bytes | SHA256 |
|---|---:|---|
| body-metric-development-check.json | 4212 | c12094529c860040fc58c8cfa83e516fb23814c2ced6ddd2fe160fe50934a34d |
| frame-natural-body-initial-audit.json | 101993 | be51c22169950f499e10b23d6a9ab6972c2f037548aee68281710155644f6e1e |
| natural-body-frame-development-check.json | 18185 | df6ae351d84f50155b89021c6c0381f39b9a3f35a4cebb8f8afaf6e788634a5a |
| natural-cap-development-check.json | 6099 | 14c68ff9ca6a7394ecec7424d5d8a9e5a549687d1974982fa2c23acbbcbef11f |

## 2. 已保存的原c0粗网格结果

61个非均匀径向层、192角、径向求积4、GH32；主体metric五控制全0。补丁起点.746以前七个位置二jet/R摘要与相同网格的原enriched精确浮点重放差全0，a/a′/a″逐位同。自然尾基场改变，所以新成本与旧模型的成本不能当作一次优化下降。

- 旧R加同形状目标成本：.0666948567137877。
- 直接metric加同形状成本：.07674959354412324；形状软成本5.58e−32。
- 直接operator最大采样误差1.7294426920420927，在当前粗网格t=.17095833333333332、theta0；最大|F/a|=.6373864894426818。
- 仅5个body列的直接metric线性预测成本.040594344933025966，rank5，奇异值1.680268294到.394837145；未应用步长最大绝对值.13362482196、二范数.25374056077。
- 全239列的直接metric线性预测成本.004326753842755247，数值rank212，最小奇异值1.8137e−16；但未应用步长最大绝对值66082.66467、二范数131901.46920。这个无约束结果高度病态，不能当作有限可信步或可行下降。
- 旧R目标只用body列时线性预测成本.05742317301676409；与直接metric的预测分账。

所有线性步均未应用，没有新设计g或新的优化状态。未完成的fine/c1/GH诊断仍须补齐；以上不是连续误差界、嵌入或reach证书。

## 3. 人工输出差异与具体修复

body helper和natural-cap helper两输出与开发原件原字节相同。full runner人工JSON只在5项方向差分的最后浮点位变化，量级3.0e−9至8.6e−9，其他来源、模型及全部字段相同；不能写为整个JSON逐字节相同。原人工检查覆盖核心数学类但漏了main这条分布调用，本次补上对应路径。

修复新增统一residual_distribution_for_grid适配器，明确传grid.radial、grid.theta以及具名quadrature_order。main和人工两侧检查都调用这个适配器，人工实际执行分布API并与独立当前审计的最大R摘要比较，两侧差均0；全Jac与端口检查继续通过。旧13个求解依赖原字节不变，所有物理定义、c0/c1、g和评价档不变。

修复runner SHA256：8185d72b866f17703c5abd5224fedfc57d197712a60ad021f246d46fd8521c3d。

新人工检查文件frame-collar-natural-body-audit-distribution-fix-check-20261114.json，SHA256：4fd1075a5a457797526b4a26c9cf5ca4ec8925c579f0795afbfe3d7a6655e452。

## 4. 接续

只重跑有具体接口错误的同一初态诊断，完成缺失的GH/fine/c1，不增加求解器预算。后续根据完整真实数据选择有界直接metric设计及独立一维中心速度；不得把当前巨大的无约束239维预测当成一次有效更新。所有真实评价继续只在公开仓库Actions。课题未完成。
