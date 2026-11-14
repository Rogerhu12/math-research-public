# 仅末 bridge 的解析初猜补点与实际离散块比较

状态：**可复现算法准备；没有预报新的数值结果。** 所有科学计算只在 Rogerhu12/math-research-public 的 Actions。

## 动机与范围

[request13 的新物理角边界](2026-11-14-actual-physical-test-failure-and-bridge-resolution.md)已通过完整真实 J 的 FD，切口条件也明显改善，但完整联解首方向仍很大、17 次回溯均非有限。request15 检验末端短 bridge 的径向分辨率；同时运行的 [request14 原完整 QR](2026-11-14-new-physical-test-original-QR.md)保原699节点，两个选择分开读真实结果。

独立 source：computations/geometry_20261114_bridge_resolved_physical.py，Git blob 54522609670e4b1b20d4987b36cfac2a6c500a9f，24,348 bytes。它重建于终端 unavailable 期间，没有声称已本地 compile；Actions 首步 py_compile 后实际运行。

## 新网格与原数学身份

输入硬锁真 accepted96 b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff、真699 prepared 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714。原699每个节点及其全部453状态按实际数值逐项复制，端点/core/p=0/scalar/field source均保留；新点只由原 make_seed 的完整材料圆、原有限物理投影和同一背景 z0/高度均值评价。**不使用失败966插值。**

只在实际 profile.bridge_start 至 profile.end 的旧区间内加点。每旧区间17点采实际 a/ap/app，用

(2M/rho_sample_min)*sqrt(abs(app)/(a*(1-ap^2)))
+abs(ap*app)/(1-ap^2)+abs(ap)/a

作为选点参照；同时输出不含压缩因子的理想材料角尺度。这里 w=sqrt(1-ap²)，|ap*app|/(1-ap²) 精确对应 |(log w)'|，不是 meridian frame 的真实角旋转率（后者为 |app|/w）。原JSON字段 sampled_meridian_frame_rotation 的名字不准，其实际定义以上述明确数式为准；本勘误不改变已提交程序或选点，不因此重跑。依次试 reference phase budget 1/2/4/8/16，选首个落在 max_nodes−24 内的方案，max_nodes 固定1200。所有699旧端点精确保留；24点仅给原RMS域检查补点预留。该采样尺度既非连续上界，也非当前截频 Jacobian 的谱证书，不作为科学完成门。

同一完整原有限 RHS 重算全部节点/中点/两RMS查询。这个原域预检失败则如实失败；通过后保存完整新 prepared，仍明确 success=False、没有 coupled acceptance。所有旧状态逐项比对，原节点 RHS 的重算差单独记录，不冒逐位相同。

## 独立局部矩阵诊断

硬锁实际 request13 的全 step d7f6c5ec07990f2fc8948eb1371d54503d2ecaded978d7d7282a7640b487d2a2 与 RHS ebc3c2343eced8c9c21c51a1519c124e6c120ed02b6e609fec5f9e32771c9560。选实际旧方向峰附近及末区间，评价原完整增强 Jacobian 与原 cubic-Hermite/Simpson 离散的 L/R，比较原一步、2/4子步及实际新网格子步。

初猜始终为上述解析种子。只有用于比较的**旧方向**按 J*d 的原端点导数作 Hermite 延拓；不把它当新 Newton 方向。报告原 RHS 复现、旧方向原块缺陷、新子块缺陷、实际 L/R 范数/条件估计、实际中点 Jacobian 数值谱与有限传递矩阵。没有新全局 Jacobian/因子或 native tail 调用，也不把这些小矩阵估计称严格谱界。可选 eigensolve/局部 transfer 失败单独写 error 报告，不否决已通过的原RMS域或冒新的接受门。

## FD、完整联解及后续

response 子命令先严格核新文件保留全部旧节点/状态/scalar/source，再为明确的新 prepared SHA 重新执行原 R252 全真实 T112-J 仿射非零高度 FD；原5e−5标准不变。除了显式新的 prepared SHA，anchor/config/reduced 与原数学源身份均保。报告额外绑定新适配器及原 prepared 身份，没有伪造一份旧文件的哈希。

随后原 physical_test_full_dn.py 使用该新 prepared 及新 FD，完整 band LU、453行全部物理/core/scalar、原17trial/RMS=1e−6/BC=1e−11/max1200及 native new-H/final audit 均保。端点状态未改，原真实 exact-zero T112 缓存仍合法；非零高度仍真求。接受后同run继续完整实际尾闭合及R249；失败则原样保存 artifact/限额内结果。

执行接口为 prepare --accepted --warm --failed-dir --out --max-nodes 1200 --reserve-nodes 24 --jac-workers 2；response 另加 --source-warm 和原 response 的全部参数。workflow 精确路径见 request15 对应提交，不需要手动改数值文件。
