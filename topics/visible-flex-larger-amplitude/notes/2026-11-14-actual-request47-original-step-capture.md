# Actual request47：原 stage43 / step11 四级矩阵捕获与字节核对

2026-11-14，/root/geometry，GPT-6 Astra Pro，AI 辅助。科学调用只发生在本公开仓库的 GitHub Actions。本地只读取原报告、核对 SHA256、形状、IEEE754 字和元数据，没有重新计算 RHS、Jacobian、矩阵作用、残差、范数或谱。

## 1. 实际运行与对象

[公开 run43630351235](https://github.com/Rogerhu12/math-research-public/actions/runs/43630351235) 的 source commit 为 c9c466f468d49e3f4699d0e0247109e83047bdb5，job 为132555346727。根会话唯一下载 artifact14127582983，ZIP为3,530,956 bytes，SHA256：

~~~text
02973eefffbd82f57dcee02776f2ed7a28c41fe750f73ec7930ff07d2f9fa400
~~~

本说明只负责四级捕获和字节身份。后续精确三作用与 new519 行账有独立报告，本文不重算那些科学结果。

输入定位为旧 stage43、原 flow step11、新 shooting stage519、入节点520；保持原普通 RK12 schedule 的这一已有步。原 h 为0.08333333333333333，binary64 字为555555555555b53f；原 port ratio 为1；原 sigma 为3.0069370042341896e-16，字为27c23cdad1aab53c。数值与位串均抄自实际记录。

| 原件 | bytes | SHA256 |
|---|---:|---|
| [result.json](public-actions-43630351235-1-stage43probe/native-stage43-local-j-probe/result.json) | 62,966 | da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403 |
| [summary](public-actions-43630351235-1-stage43probe/native-stage43-local-j-probe/stage43-local-j-summary.json) | 40,357 | 9ffb7b4d7f26ff61642d2949862931aafcc4d1ef132e0394730d821572e00e1f |
| [array manifest](public-actions-43630351235-1-stage43probe/native-stage43-local-j-probe/stage43-local-j-array-manifest.json) | 13,971 | c4201dd4f3581025cee579dd5c992458759ce6313f9a5afffe2f98c30edee7f7 |
| [window identity](public-actions-43630351235-1-stage43probe/native-stage43-local-j-probe/stage43-local-j-window-identity.json) | 4,384 | 2608bb3b27cfd16020fcdbaf2bae6c8c9b63cb85146d6c5198d1905b4f64e450 |

## 2. 实际执行范围

producer 真实记录给出：

- 原请求1次；已有 RK 步1次；前面的步没有求值。
- 原四级输入4次，返回完整局部 Jacobian4次。
- 原完整 native solve、整尾 Jacobian、旧长 stage Jacobian、no-J evaluate、非线性 trial、endpoint/J audit 均未执行。
- 没有新增 ODE 步，没有重参数化 profile，也没有清空正在携带的两个 mean 状态。
- 全部577原 seed 节点、原 H、graphs、gains、far 和 sigma 的身份检查通过。
- 观察到计划中的 Error: VISIBLE_NATIVE_STAGE43_LOCAL_J_PROBE_COMPLETE_V1；worker exit0。这是捕获完成后的诊断停机。记录 capture_completed=true，native_accepted=false，task_completed=false。
- Python 外层实际耗时20.133772782999984秒；局部捕获 summary 自己的计时为0.19秒。二者计时范围不同。

source roundtrip 记录的原函数、actual41 prepared 函数与单步选择函数依次为：

~~~text
177cf5f563aecdcab4431d842d8dfdd7f7915667b73fe956c87c48c1571c9fe4
447590785c402226adef6af880a44f8da6e2831786724d2762ab6c2c0addf5ab
31fbe3413b0c8d4e171edb4f06410ee531afe764e5ea4cafe321b6c98a2a3bf6
~~~

新 Python、hook、window 的冻结 SHA256 分别为：

~~~text
1185bbda5390c7ef3a9043ac59139b9359fececc802146f4be64aa7639730b21
8992f3920729b0f6eabf7a1e15520290fc47942c72c0c4d6433d8ac6cb291059
966ddc4946cc63f69260dd1871c2ac31ad0383eb5593f6c3a0b45b0cfcdef5ec
~~~

## 3. 四级复现与完整原件核验

逐一比较本次四级报告与已固定的 [actual44 四级原件](public-actions-43627297724-1-receipts/stage43-step11-fields.json)，后者完整 SHA256 为d7d00de365b2118e1346e8f8630d5bad408957da91fdf51f38496f73b0e0c5f2。结果：

- 四个完整226项 stage 状态均与 actual41 的原状态哈希一致。
- 四级所有 geometry_number_fields、原 x/h、root_minA、root_minD、root_error、root_scale 记录完全一致。
- 最终完整226状态、经原 port 后的224项 shape、完整224×224 shortJ、完整2×224 mean tangent rows，全与 actual41 原数组逐字节相同；每类不等 IEEE754 字数均为0。
- 本次只读审计独立核对了这些原始数组与报告布尔标签的一致性。

| 完整输出对象 | 新/旧共同 SHA256 |
|---|---|
| 完整226状态 | cebb738222e5314cb1439cd6cb1ca7aa0b6050326e5043594dfdbe1c8808be12 |
| 最终224 shape | 90bfaafffe40aa31ab47ce2f45867d4f9f714e2e546b471f21185836497c75b9 |
| 完整 shape shortJ | 422109745d733e4dfba2c1ce76354facd80e069fedaf6e540e178d69607bafc0 |
| 两条 mean tangent rows | dd4b05889acd856dc00edee31eae61775f95f383e6fa5ec03614c8e3e86317cc |

本次首次保全四个局部矩阵，各为完整226×224、404,992 bytes：

| RK field index | 局部矩阵 SHA256 |
|---:|---|
| 0 | a5692f926f949c2e9e9b00a5a7d49c1a7cf3614e31aa2a614bef90e3257d0d8e |
| 1 | 9fc8e3c1d15978ca62a2d6b143b394a4cc777bdc570779ed6eb1512655d5b025 |
| 2 | c3992df806c014fa7f0b0ced309ad6fe4450f8515d9a6a6046bad89f45b8126a |
| 3 | ce708068ceef33e43eb60dba19b03c8a8f1de634259032f641194d7d896aa0ca |

field1与field2虽然使用相同几何记录，矩阵哈希不同，原完整状态也不同；后续保留四个独立矩阵，没有合并中间两级。

只读审计完整覆盖 result 所列27个小文件与 manifest 所列21个数组文件，数组合计2,453,424 bytes。逐文件 bytes/SHA256、完整行列形状、全部 IEEE754 字有限性均核对；这21数组中的非有限字和负零字计数均为0。审计没有重新求矩阵范数或科学 dot。

[完整字节审计](2026-11-14-actual-request47-capture-byte-audit.json) 为18,042 bytes，SHA256：

~~~text
da0d81cc8e7a7ffaf5dc4e4a55b787d3241757c5f38483fb637f7ed4d041dd1b
~~~

新大数组保持 artifact-only，小 manifest 和审计给出完整身份。

## 4. 对误差拆分的准确含义

把保存的数组视为精确实数，完整 shapeJ 和 mean rows 逐字节相同，直接意味着两份226×224线性映射相同：逐项相同的系数与同一224维输入作乘加，得到相同的实数结果。因此 [R272](../results/R272-native-RK-reference-and-propagation-error-split.md) 中“旧41保存映射与本次 observed 映射之差”在这一已捕获步上是零映射，不只是在三个测试方向上碰巧为零。

这仍没有旧41四个局部 A 的字节证据，因为当时未保存它们。现有事实是原函数、状态、geometry 的复现证据，以及旧、新完整输出矩阵的实测字节相同；不自动证明局部 A 是精确连续导数，不给出真 DF 误差界。

本次明确取得四个 A，已可对同一次调用的 observed shortJ 与这些 A 所定义的有理 RK4 action 作完整有限数组比较。它与原 new519 残差的数值关系，由同一 job 的 exact consumer 和行账单独报告。本文没有据 workflow 成功宣称 native 尾已接受、原1372系统已得到准确方向或课题完成。
