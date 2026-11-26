# 原完整 SO(3) 积分范数的带状 QR 实现与接入合同

日期：2026-11-26。状态：完整源码已写，已作纯源码、stdlib AST/compile、字面重复键与尾空白检查；没有在本地构造坐标因子、求解向量、读 F/J 或执行科学 fixture。新源是原 integral 分支的独立数值因子实现，不是已经发生的原分支失败的修复。当前没有从实际返回证据确认原 integral 因子失败。原分支的真实完整方向可以直接继续，不等待本组件。

完整数学证明见 [SO(3) 积分母范数：准确正定、白化/转置与流式带状 QR](2026-11-26-integral-so3-norm-positive-whitening-and-banded-qr.md)。本说明记录已经写出的源、接口、所有变量与来源守卫，以及尚未支付的数值责任。

## 1. 完整来源和适用范围

新源为 [so3_integral_qr_coordinates.py](../scripts/resume_20261126/so3_integral_qr_coordinates.py)，24980 B，完整 SHA256 为 49a1701f0ee63cc0d0c539b1f438f964e0ff564e61a0718c8bbdf703b9839594。它只接受以下两个完整、未换标签的物理 operator：

| 实际物理源 | 完整 SHA256 |
| --- | --- |
| so3_closed_meridian_operator.py | 234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42 |
| so3_axisymmetric_meridian_operator.py | 7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf |
| 原完整 Hermite 核 gauss_observed_closed_gram.py | 26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d |

两个 operator 的原 RotationH2Coordinates 整个类 AST 相同。新类不会实例化旧因子，也不改写旧物理类、_parent、场、J/J* 或缓存；它核实际类所属模块的完整字节、该模块原坐标类的三方法代码来源、q.model 的 schema/source/canonical identity 和真实 Hermite 函数身份。

自由布局必须逐项一致：前 M−K 个自由 core，随后 radial-major 的完整旋转节点 jet，最后 H。radial_free 必须恰为按原次序排列的 0,…,3J−1，除去原表示已经固定的三个槽 0、3(J−1)、3(J−1)+1。其余槽、全部 x/y 奇频与 z 偶频、旋转规范冗余都保留。

R696 新角向表示有额外纯径向 profile 自由块，不属于这个布局。zero-closure 包装器及其他来源也不在这两个完整源码合同内。本组件明确拒绝这些输入，不能改 __module__、model 标签或尺寸字段来冒充已支持来源。未来若需要这些表示，应完整定义相应新合同。

构造和 lift/transpose 的科学运行均同时要求 GITHUB_ACTIONS=true 和 GITHUB_REPOSITORY=Rogerhu12/math-research-public。只有读取、哈希、AST 和 compile 不构造科学对象。

## 2. 同一完整积分范数

正宽度 h_j 上，六个端槽按 Y0、U0、A0、Y1、U1、A1 排列，Hermite 核给物理径向导数行 W_r(h_j,u)，r=0,1,2。固定 ell>0 与角过渡参数 tau>0。完整径向二次型为

$$
G=\sum_{j,a,r}h_jw_a\,\ell^{2r}
E_j^T W_r(h_j,u_a)^T W_r(h_j,u_a)E_j,
$$

其中 a 遍历全部六个正 Gauss 节点，E_j 只嵌入原自由槽。六点 Gauss 准确积分最高十次的完整多项式乘积，因此准确算术下这是原完整积分 H² 型范数；质量、斜率和曲率三项都在。

每个实际旋转通道频率 k 的角权为 sigma(k)²=1+(k/tau)²。自由 core 的原尺度是 1/max(1,abs(1−nu²))，H 尺度为 1。当前固定 K=3 的实际来源自然使用相同前缀，所有其余 core 都自由。没有把旧 q 系数空间的母范数误称为这个 SO(3) 坐标范数。

定义完整矩形行

$$
A_{j,a,r}=\sqrt{h_j}\sqrt{w_a}\,\ell^r W_r(h_j,u_a)E_j.
$$

于是 G=AᵀA。每胞恰 18 行，所有角通道共用同一径向因子；新源不建立密集矩形 A、不形成 Gram G，也不逐角通道重复分解。

准确正定性只需质量项：若每胞多项式的平方积分均为零，则每胞多项式恒零，其共享端三 jet 全零，因此完整自由向量为零。这个准确结论不等于任意浮点精度下的分解成功保证。

## 3. 已写出的两遍流式算法

第一遍按 cell、Gauss 节点、导数阶 0/1/2 的固定顺序消费全部 18(J−1) 行。每一列用 math.hypot 逐项累积二范数，随后取 D_j=1/||A[:,j]||₂。它不先形成列平方和，也不先构造 Gram 对角。实际范数或其倒数若非有限、非正，明确失败；不添加 ridge/jitter、不截秩、不删列、不换回另一范数。

第二遍以完全相同的顺序重新产生每行并乘 D。按原自由槽压缩后，一胞的完整局部支撑跨度最多为 5。R 的行带存为 row_band[k,j]=R[j,j+k]。对当前行从 first 到 last 逐列调用 LAPACK DLARTG，并用同一份旧 R tail 与旧 row tail 同时更新：

$$
(R_t,v_t)\leftarrow(cR_t+sv_t,-sR_t+cv_t).
$$

已消槽设置为零、对角使用 DLARTG 返回的 r，是这次已执行的消元表示，不是按阈值丢元素。若该实际待消元素已是精确浮点零，只跳过这一平面旋转，整行仍计入完整消费数；原列和自由变量仍在。

此前胞的最大列不超过当前胞 last，故本次所有新非零项都在跨度至多 5 的局部 front 内。实现对既有带内数据越过当前 last 的任何非零项明确报错，不能默默裁掉它们。最终若需要正规化正对角，就同时翻转整个有关 R 行，而不是只改对角。

当前完整 J=923 场的半带宽是 5。一般尺寸的代码用 min(5,nrad−1)，只改变存储所需的有效带宽，不改变任何槽、行、因子或二次型；这也避免在完整空间很小时产生不合法空切片。所有实际 J=923 的数学和操作次序不受此边界处理影响。

总存储 O(6 nrad)，局部消元结构工作量 O(18(J−1)·6²)。这些是算法结构界，不是一次实际耗时、峰值或条件数读数。源码将在真正构造时记录两遍耗时、行数、旋转次数、正对角最小/最大值及因子字节数。

## 4. 完整 lift 与 transpose

准确 QR 满足 AD=Q_R R，故 DGD=RᵀR。按原 radial-major 方式把旋转向量恢复成 nrad×nmode 矩阵，新的两映射为

$$
T_{\rm rot}(Z)=D R^{-1}Z\Sigma^{-1},\qquad
T_{\rm rot}^{*}(V)=R^{-T}DV\Sigma^{-1}.
$$

第二个式子是第一个对完整欧氏参数配对的真实代数转置：D 必须在求解 Rᵀ 之前作用于输入，而不是只缩放 Cholesky/QR 数据后漏掉链。core 在两方向都乘同一原 core_scale，最后 H 原样保留。

SciPy 下带数组直接取 row_band，它表示 Rᵀ；上带转换为 upper[bandwidth−k,k:]=row_band[k,:nrad−k]。lift 解上带 R，transpose 解下带 Rᵀ，均保完整多右端角通道。使用 [solve_banded 的官方存储合同](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_banded.html)，不依赖试猜转置索引。

DLARTG 的实际返回顺序是 cs、sn、r，已核 [SciPy 官方接口](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lapack.dlartg.html)；其缩放算法与普通 QR 的数值路径不构成向外区间证书。

模型、mesh/width/free-slot/角尺度以及 D、上下因子数组都进入真实记录。构造后这些数组设为只读，带状解保留 overwrite 的默认 false，避免将一次固定线性坐标映射悄悄改成随调用变化的对象。

## 5. 可供完整 solver 接入的 API

```python
coordinates = qr_module.RotationH2IntegralQRCoordinates(
    q,
    radial_length=0.05,
    angular_transition=24.0,
    original_coordinate_source=physical_operator_path,
    progress=progress_callback,
)
z_size = coordinates.size
physical_direction = coordinates.lift(z)
coordinate_covector = coordinates.transpose(physical_covector)
```

公开字段为 problem、size、record、norm_kind='integral'、factorization、counts，方法为 lift、transpose、metadata。metadata 含完整 coordinate_norm、实际 factorization 与两种坐标动作次数。progress 可省略；若提供，在每 128 个完整胞和最后胞返回完整进度，不改变算法。

record['norm_identity_sha256'] 是全部固定来源、定义、实际因子/尺度摘要的 canonical JSON SHA256。耗时、调用次数和进度不混进该固定身份。record 另保数学范数定义的单独摘要，所以能够区分“同一准确 integral 定义”和“不同实际数值因子/实现身份”。

IntegralQRFactorizationError 的 diagnostic 明确本次 complete=false、不作几何不可行或不存在判断、不宣称原 integral 已失败。其他实际输入或浮点错误也直接报出；没有异常后自动改范数的分支。

这个小源不接管原 solver 的物理模型、目标函数、阻尼、约束或接受判据。后继完整 driver 必须显式把它列为新的坐标源，重建所有经过 T* 的原行、幅度行及 SOC 行，并把实际 record/factorization 纳入自己的来源与报告。当前一些完整 SOC helper 严格要求 coordinate.source_module 为原 234ac/7f；不能仅把新对象的模块标签改成旧值来绕过这个来源守卫。

从旧 jet-sum 初始化 integral 时，mu 的新坐标单位与同物理点新 norm 初始化须由完整 driver 明说。QR 与原 integral 的准确规范相同，但实际浮点因子和 norm identity 不会被冒称为逐字相同；旧 norm 下的 C、投影缓存、预条件器或续接比较也不能未经完整新绑定复用。本组件既不选择 mu，也不隐藏重标 mu。

## 6. 准确物理域和工作数值的责任

源码取 hhat=np.diff(q.mesh) 的实际正浮点字为这里有限维算法范数的宽度参数，并分别记录 mesh 与 width 的摘要。即使两个 mesh 字被当作准确实数，它们的差也不必等于已经舍入的 hhat。因此这里的准确代数只声明该已选正宽度参数上的范数，不把它冒称为真实 symbolic 物理胞宽已无误差。

同样，完整六点 Gauss 的多项式积分恒等式是准确数学定义；实际 leggauss 节点/权重、Hermite 值、sqrt、hypot、Givens、列缩放、角尺度与带状解是普通浮点工作值。源码记录这些实际数组的摘要，但没有给它们的 interval enclosure。

若工作因子是 Rhat，则其真实 Gram 缺陷 E_G=RhatᵀRhat−DGD 与准确求解映射 That=D Rhat⁻¹ 满足

$$
\widehat T^T G\widehat T-I
=-\widehat R^{-T}E_G\widehat R^{-1}.
$$

这既说明因子误差的责任，也说明尚需逆因子/实际解算误差，不能把一个普通 QR 算法称为严格白化证书。当前源没有估计本场条件数，没有实际方向改善，没有连续曲面、reach 或度量误差结论。

## 7. 当前验证与后续使用边界

已完成完整源的解析阅读、原来源/布局对照、两遍行顺序和带索引推导、完整 lift/transpose 推导、AST/compile、重复字面键与尾空白检查。geometry 代理独立完整静态审读同一锁定源，核了 full18 行、全部自由列、局部 front、双 tail、整行符号、带转换、真实转置及模型/函数来源，未发现阻断问题。没有 import 后执行构造器，没有数值随机向量校验，没有实际因子或几何 fixture。

如果后续实际求解选择此新源，应在完整真实父上直接执行全部变量、全部目标和原全部几何责任的完整方向，并如实报告实际因子和方向结果。是否值得采用由真实返回决定；当前原 integral 首次完整方向不因这个备选源的准备而推迟。

## 8. root发布时实际证据更新

2026-11-26 17:31:42 UTC：上述完整24980B新源按原字发布。root读全源码与完整接口、核两遍18行/full列/局部front/整行符号/上下带布局及D先于转置求解的公式，另实际AST/compile；未导入构造或执行科学fixture。geometry原独立完整审保持。

准备稿中的“原integral尚无失败证据”现已由[实际26/27](2026-11-26-actual-integral-SO3-first-direction-26-27.md)加强为明确真实事实：原606完整band/Cholesky已成功并接受一个完整方向；该结果归属于原实现，不归本QR。本源码仍未执行，也没有接管当前655d后继。未来若选用须独立完整driver显式支持新source/norm身份并全重建T*行；当前新gamma/零端点包装器不在本组件受检范围，不得改标签硬接。
