# 原有限尾内端至真正固定cuff的完整相关Gram界

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

原Q-free G12/M48实际场5778bee4…在整个内collar及全部角度的真实连续证书已自然exit0，33.943738564秒，得到

$$U=9692587795331142945/4951760157141521099596496896
<1.957402518\times10^{-9}<B=2\times10^{-9}.$$

这是此前18552个有限源单元之外的缺口。真实cuff是原binary64有理数2702159776422297/18014398509481984，有限源内端是2747847568824749/18014398509481984；不能用显示小数替换准确端点。整个闭区间均已覆盖，固定帽及其他前缀/有限尾仍依各自证明。

## 原内端源与完整图

原24个blob逐一核SHA256、Git framing SHA1、重复行、正长度、18552个准确节点及最终外锚。取第一行原141个通道的完整位置、一阶、二阶迹a0,a1,a2。令h=inner−cuff、t=(r−cuff)/h，原源即

V=(10a0−4ha1+h²a2/2)t³+(−15a0+7ha1−h²a2)t⁴+(6a0−3ha1+h²a2/2)t⁵。

这正是原accurate-query消费者和原连续source预算的quintic collar，没有替换输入。每通道准确转Bernstein并准确求Vr，完整竖向符号、真实u、实际W及其物理导数沿前条相关Gram恒等式保留。真cuff在共同材料坐标中准确为z=1；供应器在此端点使用该恒等式，不将桥参数区间的舍入扩包误作z>1的新B-spline区间。

## 区间覆盖与两种合法值界

先试原全背景|w|≤16/15的纯值区间。该范围只用于I值表达式，入口明确禁止把它当作w的高阶导数传入Jet；它不能冒称常值背景。若不够尖锐，则恢复前条明确背景多项式及独立均匀余项，按原C4/解析分支、准确逆残差和全局|w_r|<24处理。原深度8表最内侧以外的距离也通过全局物理Lipschitz残差支付，不能把表内profile当作真实深collar。

全过程按实际W结点与自适应物理r分片；104片最终覆盖该完整区间，其中11片用全局背景纯值区间，93片用背景近似多项式的完整直接区间。本轮不需要Chebyshev高阶余项。67次较粗预算失败全部保存在报告内；它们触发细分，不是实际图的失败结论。每片都先形成原背景精确抵消后的完整Gram，再付背景uniform误差、真实目标分母下界。原三折旋转/反射把基本角域扩为全角；相位仍按原orbit恒等式覆盖。

## 实际身份和可重生配方

- 本条入口 `2ecf-m12-true-inner-collar-total-gram.py` SHA256 `0ff01c477d95bfeb0c1511c65b4d0f0d5799aa0e04e3c572d612e6f17568bfa0`。
- v3完整尾消费者 `2ecf-m12-tail-correlated-production.py` SHA256 `d7b6c58f17c8b61e64eb2ad57ed21306abaf0a6633fdeb1299b410c7c167bcc7`。其另一实现优化只是最后请求单元之后不再累加未使用的141通道状态；所有原blob和准确径向归一化仍核回。该优化不用于改变本条collar源。
- 实际完整报告 `g12-true-inner-collar-total-gram.json` SHA256 `533d27c7d16f653dbb6426ea514f6ac0cf90e05a0c1371be0e90a77a98af9954`。
- 实际field、grid、data、result、R226分别按原G12身份；原背景表SHA256 `9f208c790470849af024bc15ac8bb961edc5dfb02f97332a1abef8b9a5a8c264`。报告逐一绑定，没有借M64后继场。

保留原三个冻结模块子目录，并把上述两个入口放scripts。S、INPUT、RAW、P沿前条定义：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python "$S/2ecf-m12-true-inner-collar-total-gram.py" --scripts "$S" --data "$INPUT/m12-prefix-data.npz.gz" --grid "$INPUT/h2-c2-m48-g12-04/grid.json" --field "$INPUT/h2-c2-m48-g12-04r1/result.json.field.npz" --result "$INPUT/h2-c2-m48-g12-04r1/result.json" --correction-bounds "$INPUT/h2-c2-m48-g12-04r1/correction-bounds.json" --raw-cache "$RAW" --primitive "$P" --angular 32 --radial-order 6 --angular-order 8 --max-radial-depth 12 --out /tmp/true-inner-collar.json
```

大报告留临时本地。此连续内collar已达B，全部有限尾和整个前缀须继续完整覆盖后，才可合成whole metric及既有同g G5链。
