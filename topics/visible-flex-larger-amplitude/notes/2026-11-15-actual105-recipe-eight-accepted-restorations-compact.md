# 实际105：显式参数recipe正常运行，八次原Armijo接受

**类别：数值证据；原unit/full112/native目标和课题闭面目标均未完成。**

公开 [run43680931993](https://github.com/Rogerhu12/math-research-public/actions/runs/43680931993)，source `28b59a6f4ac64fdf1614773d9ca46aab8000ae9e`，job132711175414。工作流全部步骤成功；原科学success=false，停止原因仅 `explicit outer direction budget completed`。

## 可复现来源

本轮使用 `computations/geometry_20261115_small_core_inexact_p3_eta_0p01_recipe.py`（47106B，SHA256 `3169b2d3ea821a244d9f27611cd6c5cb3b239cf0e7f9bbbd7f49ac9d5f1dc9ee`）及同source的完整request和workflow。参数recipe为1249B/98209dc9d214041865fea6cd2d5db34cfe7fdccc37ac3095e86e739cd2534091，只复制实际101三个末参数；本轮没有读取原101status/log payload，来源hash不冒已消费文件。fresh评价/J、原η=.01、外8×20/内12×20、原完整三方程Armijo以及全部最终检查均实际执行。

临时原status835048B，SHA256 `2f8ad3440983f11c33ba630856439a1637a5563bcb6caa786c449f679d631cb7`。原评价账本2091019B，SHA256 `248208de1d4089fc4ca8a287d437b708781b3165392eb991ba724273f70f605e`。日志两个VISIBLE105标记之间原JSON加LF共59328B，SHA256 `73774bce7071455595bc339d56ba8fccfa1000787c1e48b1ba05b67cb4cd377e`；root实际读到并核同。按新第15条，只留脚本、参数、run、SHA和本结论，不保存可重算raw输出。

## 实际搜索

同101末参数的fresh初始merit为 **13116.490604299248**；101原末记录为13116.49060429981，末位差异如实保留，不把父值贴入本轮。末merit为 **11845.748285989865**。38个真实候选中30个由原full-three Armijo拒绝、8个接受；没有评价异常。前六次接受α=1/16，后两次α=1/8。

| 外轮（从0起） | 接受α | 原接受后merit | 内层原1e-8标记 |
|---|---|---|---|
| 0 | 1/16 | 12947.528364705913 | true |
| 1 | 1/16 | 12777.545813989367 | false |
| 2 | 1/16 | 12607.961057765162 | true |
| 3 | 1/16 | 12439.940410677165 | false |
| 4 | 1/16 | 12274.42489743835 | false |
| 5 | 1/16 | 12112.158302296817 | false |
| 6 | 1/8 | 11995.587515924399 | false |
| 7 | 1/8 | 11845.748285989865 | true |

38个内层调用有13个达到原近似根标记，八个outer接受中3个达到。其余接受仍保留真实d3参加原完整三方程merit，不放宽最终unit/full112条件。

实际末p=[0.4976392922339909,-0.2670862030502635,0.5984780843750176]。末unit=[-144.75696204631936,52.31556662313988,2.0239218417525406e-9]。完整112右残差前三项为[-66.86430464824504,-3.1229522437215222,3.183640517384005e-11]，其余109项为原零值。第三分量变小仍不能替代其余分量及完整门。

末实参数FD在步长2e-5、1e-5、5e-6处原maximum relative error分别为6.686386702428272e-9、1.6704945184382573e-9、4.859825427857713e-10，valid全true。1298次评价（728 real、570 complex），190次J，零评价异常/observer错误。

## 原最终检查的准确范围

原零core圆参考检查finite=true，physical collocation max=4.440892098500626e-16、BC=0；node/mid与原两组RMS查询的域失败均0。其reference_is_not_a_nonzero_parent=true，不能拿这个圆充当已接受非零原尾。reference原文件SHAf8d02d6c6303ac84811cdc4320583eb7eab02c4a3a58d481ad89d1060881bfe8。

原scalar Arb检查984叶、541次split、unresolved0，声明的实a/ap表达式域certified=true；它明确不包binary64逐操作舍入，不证明有限Gauss a的导数等于返回ap，不是C²接口证书，也不覆盖整个source-circle/Frenet域。末node/mid beta²最小0.0051531253136101185、radius最小0.29999999842881486，scalar最小radius0.30000000000000027，仍按原有限检查范围陈述。

## 继续

105验证了短recipe入口可以在不保留大parent-status的情况下实际续算。106从上述真实末p、run/source/statusSHA和原日志摘要SHA形成首recipe，连续执行最多64个同源八步批次；每批保原算法/预算/最终门、fresh评价，由真实原预算停止决定是否继续。非预算停止、异常或原unit停止如实报告。即使低三方程达标，非零BVP、高模条件及闭面全t/reach/metric/refinement任务仍须继续。
