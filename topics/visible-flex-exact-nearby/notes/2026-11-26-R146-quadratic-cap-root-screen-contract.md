# R146：二次帽准确根容量必要筛查的单次公开计算

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

数学范围是 [R146 QP.1–QP.9](../results/R146-quadratic-cap-and-true-root-capacity-screen.md)。
旧 RS 线性帽和 R143 CV 体预算均已完成，原文件只读。本次不同目标是长度
3/200 的二次帽 f=(1-x/ell)^2_+ 的完整正积分 T₂，以及由它与已经选定的
CV 费用导出的单个必要二次型上界。它不是重做旧容量、旧积分或旧体预算。

## 输入及范围

完整 high41、signed96/97、X、GB 与其原执行收据分别来自
44750653724/1、44745192261/1、44737045152/1、44745355257/1。
R143 CV actual 与执行收据来自 45762052058/1。全部字节身份写进 manifest；
R143 新记录和旧 GB 的 aBB_upper 作为已选费用，不冒充实际误差的下界。

原 positive 四片、candidate 五片和 root germ 仍按原 axis restoration manifest
恢复相同十个历史 blob。独立 moving mean、4e-18 完整修补、所有 candidate/
intrinsic 接口、whole 真根区间和 (0,0,1/2) 中心均不变。引用 RN.9–RN.12
已证明的 ||omega_96||<1、||omega'_96||<377；不重新算原范数或根型条目。

科学 child 固定 python-flint==0.9.0、320 bits、numpy==2.3.5、
Python 3.12.14。每个原完整交段固定32子片；只从原 dyadic cubic 形成两个
反射轴的新测试投影，不调用旧轴传播。gamma/K/mean 保留原 parent 球。
首 germ 只在实际正侧使用 K≥0；扩大的根位置 padding 只增加非负费用。
完整子片总和先保存 decimal ball 并读回，然后计算 QP.9，再保存其完整球后比较。

## 结果和可得结论

两个新标量字段是 complete_test_integral 与 complete_optimized_test_upper；
第二个按上舍入计算
2-148/T2_plus-a_minus-b_minus^2/(4*(1-c_minus))。
测试 upper ≤ 0 时，严格排除当前 CV/RA 非负费用格式；为正时仅未排除。
148/T2_plus 来自准确自由外值容量的合法对偶测试，不从某个容量上界反推下界。
本计算在任何结果下都不宣称真实 BVP 奇异、全逆、根型已付或课题完成。

中途失败保留真实原始 prefix 和执行记录，不自动重跑。完整 false 是完整筛查结果。
只发布完整小标量文件、参数、哈希和执行收据；不发布数组、artifacts 或 Releases。
worker 继承既有公开执行和每次 pull 后 README 差异检查；无新增授权流程。

science CLI 共15个参数：--definition-source --positive --candidate --germ --high
--high-execution --two-mode --two-mode-execution --physical --physical-execution
--body-budget --body-execution --correlated --correlated-execution --output。
每个路径由 worker 的已核验输入快照提供；全部科学执行仅在本仓库公开 Actions。
