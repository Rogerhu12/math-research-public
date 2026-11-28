# WMT14：原完整 Θ 的新 weighted-model 接收入口

2026-11-28，visible-exact-astra-b0d5a16-20261128。

[完整证明](../results/R149-supplement-complete-weighted-model-Theta-receiver.md)已经给出同一原 UACT/OT 算子的完整误差公式；14 个新数值目标只在本次公开 Actions 首次运行。原 global error 850.945862… 的整候选保留，新值完成之前不预报改善。

完整 manifest 为 [2026-11-28-weighted-model-Theta-receiver-inputs.json](2026-11-28-weighted-model-Theta-receiver-inputs.json)，45728 bytes，SHA256 `4913fe4ce57cd579741b65090cd5e6dae22392956545196c888c3061b8974ffb`。139 current + 6 historical 全部145件已完整准入，原UACT21 actual/execution及其validator保留，未数值导入或重算任何旧科学目标。

新目标是三个原 Y 的完整导数Gram norm、完整primitive strip vector bound、新8192点/2048head的全导数残差Gram、无限tail及真map error、真inverse的一导误差、原alpha的完整一导tail、原row的完整二导error、原model从1到2^20的完整weighted head与严格无限tail，最后合成同一全Θ误差。每个Gram保9216项；只新增8192 grid的4096奇节点，偶点读原whole4096 grid；原2240 model multiplier载体恢复须核whole SHA，然后只延伸缺少的2241..2^20。大中间数组只在runner private workspace，公开仅全hash/参数/自然完整结论。

真全空间H1 bootstrap采用同号压缩两块正交，不把dagger当L2 adjoint。原physical4、两个均值、真正相位、true inverse、全部产品误差和head/tail平方都保持。使用旧products的确定S>3/5只比较完整配权常数，不从upper推未知误差lower。全Theta误差不以low96误差代替。

新workflow `.github/workflows/fourfold-codazzi-weighted-model-Theta-receiver-public.yml` 采用原不可变Python容器/Haswell单线程以及Python3.12.14、NumPy2.3.5、python-flint0.9.0；仅该新workflow路径首次push触发，成功目标不自动重试。公开结论预算160000 bytes，额外reserve120000 bytes；scientific child timeout20100秒。

后置BFP消费仅在其19个目标和WMT14实际全部成功后允许：保整个96 signed centres、全部其余fees和原physical means，只替同一个完整global Θ slot，不重forward/pullback/pairing。该入口本身不授fullphysicalSchur、core存在或最终闭等距族。
