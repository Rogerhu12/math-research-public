# R143 实际补篇：完整相关体预算通过，最优根必要门未排除

2026-11-26，visible-exact-astra-198c63d-20261126。

**已证明（完整公开计算支持的体上界）；真实根费用和完整逆未付。**

## 1. 实际执行与完整对象

[公开运行 45762052058/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45762052058)
首次完成 [R143](R143-correlated-body-energy-and-optimal-root-screen.md) 的
CV 同参数四顶点 majorant。全部4651闭片、原4650 positive 行与真根 germ
完整覆盖，同一个 $v$ 同时出现在 Gram、曲率项和分母中。
真实 mean、全部接口、外锚漂移、独立 H 源及根源向量保持原定义。

输出均在 `notes/correlated_gram_body_budget_ci/run-45762052058-1/`：

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| correlated-gram-body-budget.json | 30248 | 4b2f6625d2a4eda760fd13cd219a71e568e3b76e2d12764cccadf940e7349ea6 |
| execution.json | 16646 | 3ccdbc9dff7424df3281a68fa5e7e987b7901e13b2fed66b5616d177aa9f25fd |

实际 return code 0；唯一科学子进程约0.808313秒，其中数学约0.298950秒。
30份当前输入和5份历史容器按原清单读取，清单 SHA 为
`72de72538cccff06c824fa28d4ab14eb806ad262fbe2fea12df600179a89b86e`。
原 X/Y/GB/RS/SG 完整成功与失败范围只读，旧科学目标和旧 producer 调用均为0。

## 2. 六条完整记录

每条新记录保存为整数 midpoint、非负整数 radius 与十进制 exponent，
完整区间包含实际有向值；保存后读回，再进入下一式。
以下是方便引用的严格有理外放，不替代原完整球：

| 新记录 | 严格外放 | 数学含义 |
|---|---:|---|
| C_correlated_upper | $<17.809$ | 全区间完整相关谱体费用上界 |
| wE_correlated_upper | $<19.745$ | 同旧 H/角图/漂移费用的完整 E 响应 |
| aEE_correlated_upper | $<0.641002$ | 所选完整体二次式 EE 费用 |
| aEB_correlated_upper | $<0.555960$ | 所选完整体二次式交叉费用 |
| optimized_root_necessary_upper | $0.037870<N_+<0.037871$ | R143 OC.5 的必要条件函数上界 |
| root_allowance_correlated_lower | $>555.584$ | 保原根源向量的条件 allowance 下界 |

前四条是上界，不是实际 PDE 范数的下界。特别地，$N_+>0$ 只能说明
这次必要筛查没有排除新预算；不能由正的上界反推真正待估对象为正。

完整 body 矩阵的两对角门和行列式门都严格通过。RN 的三项较弱必要
检查 $C<23$、$w_E<22$、$a_{EE}<23/30$ 同样通过。
这与已经被 RX 排除的旧 SG/RA 组合相容：本次计算的是 CV 的另一套
完整包围，未重跑或修改旧 SG 上界。

## 3. 真实可消费的结论

将原 GB 半余量公式中的体费用换成本次完整四球，保持同一 $r_E,r_B$
和原 independent mean/source 输入，原充分结论在真实根常数
$C_*\le555$ 时成立，因为已保存 allowance 的下端严格大于555.584。
本篇没有建立 $C_*\le555$，也没有以 $N_+>0$ 代替这一义务。

后继必须保留真实 $D_H^{-1}$、有限负部与 low/source 相关交叉；旧统一
$\lambda$ 替代的路线仍被 RN 排除，不能因本次体费用改善就重新宣称已过。
R142 的独立直接低逆路线同时继续。全部 physical 外行、negative/germ、
真实 $\nu$、非线性迭代和同一固定度量闭曲面的 matching 仍未由本篇推出。
