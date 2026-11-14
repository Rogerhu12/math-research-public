# δ5 完整前向有限参考的实时像和 q

**状态：已证明，准确有限参考输入。** 全部 550 个准确闭时间段已经完成，
不是抽样、前缀或真实特征流结论。对象为 retarget descriptor
097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052：
保留完整 degree-7 时间 Bernstein 控制、全部有限 Laurent 乘积和准确首值修正。

完整 index：
data/phase_ring_continuation/type_fixed_step02_d5_step5_complete_reference_real_time_gates_forward.json.gz，
SHA256 d85e63c80c03700c1ac8826a6077563fc2a9b13ecb987106d1730659bf8b2dbd。

真正全局汇总：
data/phase_ring_continuation/type_fixed_step02_d5_step5_complete_reference_real_time_summary.json.gz，
SHA256 759b991463997494c66311a7741e61a0f29492120b01e79464264208010df3a6。
汇总源 fourfold_reference_real_time_complete_summary.py 逐一绑定叶文件、准确时间分割、
相同 reference/target 身份和所有闭控制，既不重算大参考，也不从缺段前缀外推。

## 全域实际界

对所有实时间及完整归一化标签圆的相应复条带，物理角像满足：

| 标签宽度 | 全 550 段的 $\lvert\operatorname{Im}Y\rvert$ 上界 |
|---|---:|
| $1/512$ | $0.001340973226$ |
| $1/256$ | $0.002687054592$ |
| $1/128$ | $0.005417114556$ |

在标签带 $1/256$ 上同时有

$$
\operatorname{Re}Y_x>0.03032266714,\qquad |Y_x|<1.016998470.
$$

数据文件保存更精确的有向端点；上表均向安全方向舍入。
特别地，全部像严格位于物理角带 $1/64$。
这个包含关系只为同一有限参考供域输入，不能免除真实 field 对象和域的身份核对。

## 连续性的支付方式

每个完整参考时间段有 8 个 Bernstein 控制。
在复标签边界上，$\operatorname{Im}Y$ 和 $\operatorname{Re}Y_x$ 的有限 Laurent 系数
分别含准确的 $\sinh(kS)$、$\cosh(kS)$ 因子。
512 个闭角单元各用 8 阶实 Taylor、多项式全部频率尾和有向运算支付整个单元，
并非只检查节点。Bernstein 的非负凸组合给完整实时间，
实性和调和最大/最小原理给两边界之间的全复标签带。
前向 550 个准确时间区间无遗漏；原始 U/Q 接缝已有独立的准确证明，仍保持原对象。

本项没有证明 $Y$ 接近真流、真实 flow Jacobian 非零、密度小或 KAM 成立。
这些继续由真正 field、R68 小缺陷、参数密度和完整积分支付。

## 重放

从本课题目录使用单线程 BLAS：

    python scripts/fourfold_complete_reference_real_time_cover.py \
      --leg forward --segments all --label-widths 1/512,1/256,1/128 \
      --q-widths 1/256 --nodes 512 --taylor-order 8 --bits 256 \
      --compare-physical-strip 1/64 \
      --out-directory data/phase_ring_continuation/step5_complete_reference_real_time_gates_forward \
      --index data/phase_ring_continuation/type_fixed_step02_d5_step5_complete_reference_real_time_gates_forward.json.gz \
      --resume
    python scripts/fourfold_reference_real_time_complete_summary.py \
      --out data/phase_ring_continuation/type_fixed_step02_d5_step5_complete_reference_real_time_summary.json.gz

完整归档清单见同日期 complete-forward-reference-gates-ready-manifest。
此前运行曾在同步期间短暂缺源，已经按相同源 resume 并完成；已完成叶均保留，
没有重造丢失数值或修改旧候选。
