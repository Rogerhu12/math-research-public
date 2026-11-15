# 原惰性 Gaussian 八项固定源运输：公开执行契约

2026-11-15。状态：工程已准备，只有公开 Actions 的真实成功输出才登记为已算。

## 1. 本次实际范围

消费[原固定角色分解](2026-11-15-sigma-inert-Gaussian-rayclass-source.md)。
只在固定模六的36个特征上形成八个源矩阵，验证角色与偶奇关系，
在原六截面基 $(S,F,H,R,J,G)$ 中运输，并输出八项 FG/HJ 系数。
不存在素数参数、素数扫描、sigma高阶窗口或新的CM值计算。

八列依次为F3的oldform指数1/2/4、F7的1/2/4、G1、G5。
原函数对应 $J_f(t^d)/d$，不能删去oldform尺度。
真实目标保公共 $c^2/32$；本次计算的是 $\widehat U M_\nu\widehat U^t$，
没有将 $c$ 或未知的八个缩放CM值设为一。

零FG或HJ系数是合法结果；成功条件不要求它们逐个非零。
完整运输矩阵可逆也不等于指定CM线性组合非零。

## 2. 必要的旧输入恢复

原R812 run43713181015/source2b7183a313ddb04eb67bea37107830674511c49a
已完整完成六个split Frobenius案例。本任务不重跑那些案例。
其冻结core SHA256为
e7bac15678e6d0d30a30e54edd41a2d34a053b766da97efa7771278827e87ab2。

逐字检查该core和wrapper的最终输出可知：旧JSON只保存U的归一化主元、
公共分母、determinant的Norm以及六个FG的12有理坐标，
没有保存U的36个准确条目、U逆、HQ/HP或其特征列。
因此不能从已有raw恢复新的完整U坐标，也不能由Norm任取一个矩阵。

新core只复用原6×6 Miller/Heisenberg构造恢复这一个必要的Uhat输入；
保原方向、Miller常数、正实周期和同一首非零主元归一。
不计算旧Theta5或六个Frobenius案例，不重新计算旧已登记的非零结论。
请求同时固定原core、原R812证明、harmonic-seven证明和新角色分解的全文SHA。
完整新Uhat写入本次产物，后继不得因缺少它而重算。

## 3. 准确算术与必须保存的输出

域为Q(alpha,sqrt3,i,sqrt2)，alpha³=4，三平方根分别平方为3、−1、2。
所有准确条目使用同一24维幂基sqrt2^d alpha^a i^b sqrt3^c，
次序d<2、a<3、b<2、c<2，与core序列化严格相同。

新core必须验证：

- 原六阶Heisenberg作用与Uhat可逆、明确偶奇反射；
- 全36特征的准确角色变换、GC20逆变换和oldform常数；
- 原八维源矩阵与八维运输矩阵均可逆；
- 源基determinant的分母和整Norm只含2，实际计算而非预填；
- 所有输出Norm由同一24维乘法矩阵准确取得，零输出保留为零。

为直接供后继，输出完整Uhat 6×6、源基8×8、原运输8×8。
每个条目保存全部24有理坐标，每个矩阵保存准确行列标签。
另输出八个FG/HJ条目的坐标、清分母及整Norm，并保规范主元和共同尺度说明。
这些坐标与矩阵是公开Actions的实际算术结果，本地或连接器只做文本/IO。

## 4. 运行、来源绑定与核验

core与wrapper只允许在本公开仓库GitHub Actions运行。
官方sagemath/sagemath:10.6镜像先记录真实digest，数学容器network=none，
源码只读挂载；记录run/attempt/source commit/core SHA及Sage版本。
预算30分钟，外层45分钟；有限任务若未完成就保失败回执，不登记成功。

wrapper在执行前按SHA核core、wrapper、原R812与harmonic证明、新角色分解、method及workflow；
先AST再数学。成功后严格解析原stdout和canonical result SHA，
核八列标签、三矩阵形状/全部24坐标、原基次序、来源metadata和每个certificate字段。
最终verify只做同一结果和完整manifest的IO/一致性检查，不重新执行数学。

必要raw仅一日active artifact；Git只保存代码、请求、证明、方法和真实run/SHA摘要。
不把原未知CM值、未筛非零、primitive/Legendre同h或主一致性定理置为完成。
