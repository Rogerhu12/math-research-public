# 独立零闭合 SO(3) 分支：完整源码静态审查与纯报告读取

本记录只登记完整源码、符号链与实际纯文本检查。没有在本地执行场、残差、根、J/J*、曲率、QP 或科学 fixture；也没有一个实际零闭合方向可据此宣布成功。公开 Actions 的实际新 baseline、完整方向、失败和末场仍须另行返回。

## 1. 本记录精确绑定的完整源码

| 角色 | 完整文件 | 字节数 | SHA256 |
|---|---|---:|---|
| 固定直接参考 | `scripts/resume_20261126/so3_axisymmetric_reference.py` | 46198 | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| 直接完整基底算子 | `scripts/resume_20261126/so3_axisymmetric_meridian_operator.py` | 38974 | `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf` |
| 新完整隐式闭合算子 | `scripts/resume_20261126/so3_zero_closure_endpoint_operator.py` | 49540 | `5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46` |
| 新完整几何接口 | `scripts/resume_20261126/so3_zero_closure_geometry.py` | 45504 | `7698fd89e1b739391e2139c6c88dacd0c3b3d8be614fd65e435508420326b385` |
| 新完整求解器 | `scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py` | 53929 | `b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b` |
| 新启动器 | `scripts/resume_20261126/launch_zero_closure_so3_actions.py` | 11595 | `27414140270a0fb1a9533a21a0bd28a46988c55aecd9952c38e7c05512b64166` |
| 本记录的新完整纯读取器 | `scripts/resume_20261126/read_zero_closure_so3_report.py` | 26123 | `b25e5a5f370e69fe8164d835a608b1845db926d2488939dc9bafaa3bba0a6857` |

直接基底的科学定义仍是它自己的 `hΔ` 完整定义；零闭合算子通过明确的 `base_complete_model` 保存该真实来源，另立自己的新场与完整源身份。没有把旧算子的 source 标签贴在新函数上。读取器由完整 `read_axisymmetric_so3_report.py`（16133 字节，`0c44ed4962fa6812f91c888d869d50ab089a70438fc933d0fc5589a53a23700c`）作纯源码派生；旧文件未改。

本修订接入实际导入失败后的最小来源修复。[03 实际分卷](2026-11-26-public-actions-45811843606-1-part-001.md) 中，旧 `e3fb...` 准备在 5.938221273 秒以 exit 1 返回，未产生 reference/report；实际 traceback 随后的纯日志读取确认，它在加载未使用的 `hold` 模块时遇到 `ModuleNotFoundError: No module named 'parallel_20261117_profile'`。新 `4e65...` 继续核全部 7 个依赖路径与 SHA，只执行 4 个确实消费的模块；`FullHold` 仍按原真实路径自行加载 integer，并核 hold 文件身份。没有更改 scalar 定义或科学求值函数。

本修订的 zero endpoint 与 geometry 两完整文件逐字未变；driver/launcher 只更新完整来源常数。新读取器也只把旧 `6666...` 的 driver pin 改为 `b4d7...`，与旧 `ef042...` 全部函数/类的 AST 相同。旧锁定稿及旧来源未被修改。实际后继准备/根/方向是否成功，仍须读取公开运行的独立返回。

## 2. 实际静态审查范围

新场采用世界坐标左乘修正，原全量自由 core、全部共享五次旋转变量和 H 均保留。两个泡的轴由固定材料角图给出，不从当前旋转场重选。静态核对了泡的径向导数、轴随角度的一、二阶导数、完整 Rodrigues 一阶及二阶角导数、`T_s`，以及它们到 `F, F_s, F_phi, F_ss, F_sphi, F_phiphi` 的完整积分和拉回。

端点根数值迭代全部 detach。对给定原变量 y，数值根及其角 jets 构成 Z；完整约束为

$$
R_0=C,\qquad R_1=C_\phi+C_z z_\phi,
$$
$$
R_2=C_{\phi\phi}+2C_{\phi z}z_\phi
  +C_{zz}[z_\phi,z_\phi]+C_z z_{\phi\phi}.
$$

实现用该完整约束对 Z 的真实 6×6 或 9×9 数值 Jacobian，而不是只用 C 的 3×3 对角块。值保持的 surrogate 为

$$
Z_{\rm used}=\widehat Z-\operatorname{stopgrad}(R_Z)^{-1}
 \bigl(R(y,\widehat Z)-\operatorname{stopgrad}R(y,\widehat Z)\bigr).
$$

前向仍是已经求得的数值根；一阶参数导数为在该数值点求得的 `−R_Z^{-1}R_y`。这是完整隐式一阶链的数值实现，不是有限 Newton 步的导数。根残差、积分和舍入尚未包围，因此不能把它冒充精确根分支导数的已认证误差界。该 surrogate 不提供二阶参数导数；代码与读取器均明记这一范围。

当前 core 逆图也使用完整一阶隐式导数。core/H 到端点系统及全六 jet 的依赖没有冻结；固定 theta0 与当前 phi_c 没有混为一个变量。全三行 metric 残差保留，包括精确公式中恒零、数值计算仍读取的径向行。未将 `E=1` 当作省掉实际 E 读数的理由。

根缓存按当前全量点及 literal binary64 角身份保存；新点清空缓存，order 1 到 order 2 的升级补齐第二角导数与相应 Jacobian。静态核对未见以旧点根、6×6 Jacobian 或旧有限失败替代新点完整读数的路径。

## 3. 来源、初值与真实失败的边界

几何接口核对新算子的真实 `grid_fields/point_fields/point_vjp/prepare/domain` 的 codefile SHA，继续核对完整 base 模型、固定 scalar 定义和身份；原 192 行选择器只通过新世界坐标六 jet 与原全量自由变量的完整转置使用。新接口没有调用旧物理场拉回。

直接 `hΔ` 分支的完整末场可作为原变量 seed。seed 报告须属于精确完整直接求解器 `606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9`，真实 bundle、base 模型、固定 g、carrier 均核对；其历史地点进入新永久集合。seed 只复制原变量，新零闭合表示改变物理场，重新完整读取新 baseline，不继承旧 Phi、几何值或证书。

同零闭合模型的 restart 另走完整自身 schema/source/model/bundle 检查。工作积分精度和根求解策略仍如实记录，不能从 checkpoint 的旧读数直接宣告新读数。常数 H² 型范数与全量变量保持，阻尼数值及其单位由新完整 norm 记录承担。

初始根、metric 或完整几何读数若失败，求解器现在保存 `complete=False`、`actual_initial_read_error`、实际 root 诊断及 `initial_failed_candidate_is_not_an_accepted_field=True`，然后传播真实异常。该记录不是可接受场，也不是全局不可行证明。已读的完整公共 slack Phase I、逐方向 C 与真实线筛主体保持；顶层 `CommonSlackRows` AST 与直接完整求解器一致。

## 4. 找到并实际修正的报告阻断

零闭合层使用自己的完整 core 逆图。直接 base 的旧有限 Newton core 路径未执行，所以它的 `minimum_inverse_root_rho` 仍为初始化 `+inf`。原新稿直接把 `base.metadata()` 放入报告，会使 `json.dumps(..., allow_nan=False)` 在第一次保存时失败，连诚实的初始根失败报告也写不出来。

最终 `5b4c...` 仅在该嵌套 metadata 中把未执行的 base core 两个诊断置为 `None`，明记 `base_core_inverse_path_used=False`；没有用 wrapper 的成功数值冒充 base 路径执行结果，没有更改 base 定义、源文件或数学场。共享低层 counter 仍完整保存，并声明不作分源执行次数的分离归因。零闭合层真实 current/all-attempted core 统计另有字段。

## 5. 新纯读取器的合同

读取器只使用 stdlib；绑定完整 driver SHA，再从其字面 `SOURCE_PINS` 核每一实际完整源与报告角色。它逐层核对 zero model、`base_complete_model`、完整 axisymmetric reference 的 canonical identity 和固定 g；不通过改 schema、改标签或只取某个旧函数名来接父报告。

它保留每个 metric/restoration 方向的真实阻尼、QP 状态与 advances、末面 Pg/tolerance、工作行数与缓存成本、slack 与真实非线性违反值、已接受 bundle、所有原 trial。新增每个 trial 的真实 statistics、domain、完整 geometry 和 root 读数，避免把未作的检查填成通过。

根诊断分为三个清楚的范围：当前字段对应的 literal 全量点与当前 cache；全部尝试字段累计的成功根/逆图范围；全部尝试累计的调用与失败次数。`current_all_grid_angle_roots_available` 只表示数值 cache 存在，不表示连续角度分支存在。base 共享计数的 scope 原样输出。

完整预算和初始失败均可读取。若 `complete=True`，须有末场 statistics、末场几何、完整方向计数和真实端点 metadata；`--verify-final-bundle` 还逐字核 runner 上实际末 bundle SHA。初始失败不能同时携带“已完成”或末 bundle。只有同一报告中新初值到新末值的同 p/epsilon/scale/normalization Phi 才相减。

用法为：

```text
python read_zero_closure_so3_report.py --repo REPO \
  --report WORK/FRESH_ZERO_RUN/report.json \
  --output WORK/FRESH_ZERO_RUN/actual-readout.json \
  --verify-final-bundle
```

输出必须是新文件。读取器不会创建科学数组、重算 F/J、补跑方向或补做根验证。未返回的真实方向、初始根失败及迭代预算到限都不成为成功。

## 6. 实际检查与尚未支付的责任

最终新读取器已实际通过纯 AST parse、compile、重复字面键/关键字检查、无尾空白检查和 `--help`；完整几何归因函数与原读取器的 AST 相同。没有构造数值 fixture，也没有实际新科学报告可在此读取。静态审查未见余下所核接线的阻断；这不替代 Actions 实际执行。

以下字段始终明确为 false：连续 metric/几何证书、完整 uniform IFT 条件验证、连续闭合 root 分支、根误差包围、角 root jets 向外包围、积分误差包围、由根失败推全局不存在，以及原课题的完成宣告。精确径向恒等式只属于精确公式，不能抵消普通计算的根、积分、逆图、scalar carrier 或舍入误差。后续仍须在实际同场承担全角/全径向几何、幅度/reach、all-t、固定 g 的精化和足够小的 solver floor。
