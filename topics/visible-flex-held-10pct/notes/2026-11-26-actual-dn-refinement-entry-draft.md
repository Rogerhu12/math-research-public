# 原非线性 DN 同问题精化入口草稿

会话：Astra-held10-06bbeb39-20261126。日期：2026-11-26。

**状态：独立 staging 源码草稿，未部署、未执行、最新字节尚未 compile。**
本地执行环境 09:18 UTC 断开，root 授权只在
held10-astra-actual-refine-20261126 保存这些新文件，供后续恢复、
实际编译及独立审读。main、CI、HANDOFF 与 log 由 root 独占。
目前没有真正通过的 λ=1 原非线性 DN 输入，不能运行或虚构接受结果。

## 固定问题与真实来源

新结果模型名为
warm-supported-material-phase-fixed-metric-actual-dn-refinement-v1。
输入必须通过原 actual-DN 集中接受门，或新同问题精化接受门。
新增 actual_source_run/sha256、actual_source_raw_sha256、
actual_source_physical_sha256、actual_source_full_height_sha256
绑定前一份真实已接受非线性场。

原 linear_source_* 字段保留其真实 λ=1 几何锚来源，绝不将后来的
actual raw 改写为“已接受线性解”。内部 geometry_spec 只给原
v2/v3 build_model 传固定几何字段，不具有线性 solver/pass 声称，
也不调用线性 BVP。完整固定字段包括 actual δ、全 anchor support、
真 phase_basis、零控制 v2 锚、材料图、原径向图、gauge .06、
mean1168 与 BC .02。

同 M 严格收紧 radial tol 后再升两次 M；每次保留完整 p 的原坐标，
新增控制置零，完整 3M+1 Fourier blocks 零延拓。必要加网格读取
原 physical quintic，并逐点恢复原 raw 节点值；新增初值投影差
使用原 R48 lift，系数为 1。该转移初猜不会被称为已接受场。

## 真尾与接受门

新 M 只重建该分辨率所需的原 startup port/native provider；
port 不替换非线性 terminal。原 finite depth、shootingParts、steps、
几何参数和原 native/source/binary 合同固定，quadrature 只随 M
保留原严格下界。原完整已接受 shooting checkpoint 交给原
remeshCheckpoint，随后重新求完整 H/J/audit 和八轮外迭代。

源代码使用 799c0d 的 fresh-directory 修正：native evaluator
创建自己此前不存在的 native-runs；调用者不预建它，也不删除
历史目录。每个真实返回先保存 raw/SHA/status/RMS/完整 H，
再执行可能失败的 core/物理重建。

每层原 RMS、实际 scaled/physical BC、2e-9 原尾容差、完整 J、
真实 packet/state、完整 finite metric 双角网格和全部身份均须通过；
失败场不会晋升为下一层初猜。新集中门递归核前一真实场，原
λ=1 线性锚仅用作固定几何来源，不用线性残差替代 actual DN。

## 比较的精确范围

完整六个 Cartesian jets 指 core+prefix+bridge 的
F, Fs, Fp, Fss, Fsp, Fpp，保留同一个 mean1168 与真 primitive 定义。
两个正 Gauss 数值规则的差只是诊断；有限角/径向取样不是连续
C2 界，不是 Cauchy 或极限证明。完整尾面六jet比较仍须另接
同一 shared-R 表示，不能用 cut jets 代替；相关 flag 保持 false。

phase 差首先核完整 baseline/window/λ/同一基底。literal Δd
以精确有理数相减，另报 j 权重的序列 l1 距离。v3 的真频率
ω_j=jπ/(π/3−S) 用向外 π 区间包住，不使用浮点频率来定义目标。
以 D1=630/(256b)、D2=2520/(64b²)、
D3=(7560/16+5040/64)/b³ 及
C_r=Σ|Δd_j| (ω_j^+)^r/(ω_j^-+D1)，得到 phase 的
0/1/2/3 阶统一上界 C0、
C1+D1 C0、
C2+2D1 C1+D2 C0、
C3+3D1 C2+3D2 C1+D3 C0。
这是同一有限 phase 族的乘积求导与三角不等式界；
不证明完整图 C2 收敛，也不支付未算的尾部。

## 当前草稿文件

- warm_actual_dn_refine_model.py：显式真实来源、固定问题、完整 lift。
- warm_actual_dn_refine_acceptance.py：真实 nonlinear raw/full-H/state 门。
- warm_actual_dn_refine_step.py：原 full-H/J 与 actual 外迭代，旧部署入口不变。
- warm_actual_dn_refine_compare.py：完整前缀六jet与真 phase 差。
- 三层 controller 仍在编写/恢复中，未在本次草稿提交声称可运行。

需要执行环境恢复后实际 compile、CLI/拒绝错误来源的小检查、root
独立审读，并且真正 λ=1 原 nonlinear DN 通过后才可启动数值精化。
