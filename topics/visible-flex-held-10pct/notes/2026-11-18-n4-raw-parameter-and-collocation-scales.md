# raw λ=.02 的实际 M20：边界参数尺度正常，单独 H² 变元未改善全系统条件估计

维护日期：2026-11-18（UTC+8）。接
[同几何 M20 终态](2026-11-18-n4-raw-lambda002-fixed-m20.md) 与
[完整缺陷定位](2026-11-18-n4-raw-defect-localization.md)。
证据为
[raw_lam002_m20_condition_diagnostics.json](../scripts/resume_n4/raw_lam002_m20_condition_diagnostics.json)。
这次没有重解 BVP，也没有采用新的圆化基。

## 所测状态与方向

输入 checkpoint 哈希
`37a7a0b90398e34ece155a00c14414b4197b24debf013ab3c8e8deabd0aee04a`。
仍为新 $w_{\rm cut}=.16$、$\eta=.1$、$\lambda=.02$、原锚 $J=16$，
物理 $\delta=.030158202455449618$、$v_d=.25018727173023186$。
所有 $c_8,c_{12},\ldots,c_{80}$ 都是实际固定几何自由参数；未删掉首列。
原 correction scales 全为 $q_*=.0125$，第一个变量是
$p_0=\log(q/q_*)$。

读取全部实际参数，经已登记的 `build_seed` 重嵌入完整核心和材料图。
这是同一完整映射的浮点重建；并非宣称逐字节复用了旧求解最后的 LU。
核心与材料图身份误差保留在记录中。局部方向包括实际入口参数矩阵、
完整边界参数矩阵、19 个实际径向位置的 flow 参数偏导，以及完整核心
$(F,F_u,F_{uu})$ 对物理参数的解析导数。核心范数用 4096 个材料角样本，
$u$ 与记录键 `Ft/Ftt` 一致。

## 局部块的结果

令 $S$ 堆叠 $q_*^{-1}\partial_{p_j}(F,F_u,F_{uu})$ 的样本，除以
样本数平方根。用数值 SVD $S=U\Sigma V^T$ 定义
$T=V\Sigma^{-1}$，考虑明确的坐标变换
$p=p_{\rm anchor}+Tz$。这只是在同一个完整控制空间里换变量。
这里的 $H^2$ 是采样二次范数，不是连续区间认证。

| 矩阵块的 2 范数条件数 | 原坐标 | 上述 H² 坐标 |
|---|---:|---:|
| 入口参数块 | 4.4965 | 486.883 |
| 完整边界的参数偏导块 | 4.4965 | 486.883 |
| 采样完整核心二阶方向 | 475.532 | 约 1 |
| 采样 flow 参数偏导块 | $4.83922\times10^5$ | $1.17545\times10^4$ |

原入口参数列范数在 $[.99429,1.38740]$，没有明显的尺度失衡。
归一化核心二阶方向有助于那个特定范数，却同时恶化入口参数块。
这些偏导块本身都不能替代完整 BVP Jacobian 的条件判断。

## 完整配点 Jacobian 的只读检查

使用安装环境中原 SciPy `prepare_sys`、`construct_global_jac` 和原 `splu`，
在全部 2282 个径向节点组装一次原矩阵 $A$。
维数为 139222，非零条目 19,769,524。物理和离散方程均保持原样。
参数变换对应完整列变换
$A_z=A\operatorname{diag}(I,T)$；使用同一 LU 及精确链式代数比较逆算子，
没有新求解、截断方向或丢掉条件。

| 项目 | 原坐标 | 仅参数 H² 坐标 |
|---|---:|---:|
| 完整矩阵 1 范数 | $1.64693\times10^5$ | $1.64693\times10^5$ |
| 逆矩阵 1 范数估计 | $2.59771\times10^7$ | $2.66120\times10^7$ |
| 条件数乘积估计 | $4.27825\times10^{12}$ | $4.38283\times10^{12}$ |

逆范数来自 `onenormest`，属于数值估计／下估，**不是严格上界**。
数值大小依赖当前节点、行列单位和坐标；不把它写成几何不变量。
这个实际完整矩阵上，单独上述参数归一化没有改善条件估计。

重建状态的完整配点残差最大值为 $2.48\times10^{-11}$，原 LU 回代的
相对残差为 $4.17\times10^{-15}$；对应完整 Newton 修正范数仅
$7.03\times10^{-11}$，实际 correction 参数最大变化约
$3.76\times10^{-16}$。坐标变换前后的物理参数修正相差
$4.04\times10^{-28}$。这些是有限线性系统的观测量，不是连续误差界。

## 对下一次实际计算的含义

原 M20 终态的完整 metric $3.4342\times10^{-6}$ 仍未过课题门。
上述结果不支持把它归因于入口参数列尺度失衡，或以尚未解准有限配点方程
为理由忽略完整 metric。现有缺陷定位仍指向保留频率之外的高频风险。
因此本次不启动一个仅更换上述参数坐标的重复 BVP。

可复现程序分别为
[diagnose_raw_parameter_scaling.py](../scripts/resume_n4/diagnose_raw_parameter_scaling.py)、
[diagnose_raw_collocation_condition.py](../scripts/resume_n4/diagnose_raw_collocation_condition.py) 与
[record_raw_condition_diagnostics.py](../scripts/resume_n4/record_raw_condition_diagnostics.py)。
完整执行命令、输入／输出／源码哈希及 SciPy 实际组装源哈希都在记录中。
所有矩阵和变换数组留在 scratch，不进入仓库。
