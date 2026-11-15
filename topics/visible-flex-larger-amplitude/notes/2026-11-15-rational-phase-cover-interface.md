# R281 两图有理相位覆盖：独立执行接口

2026-11-15。数学证明已完成；本次只交源码和静态检查，没有本地科学执行、Git修改或伪造的闭场输入。

## 文件与依赖

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| geometry_20261115_rational_phase_cover.py | 14474 | f6214d1dc66f9890e99f5d9bbbc93fa0e6524acd6ac879f0058ea023ebc17537 |
| R281-exact-rational-phase-disjunction-and-finite-cover.md | 13934 | 112d49e942c4a6728baf7f683d53dedf04a63f5efc4786c9e2b02a111cc0d6ee |
| 冻结 R280 源 geometry_20261115_joint_phase_normal_balls.py | 8454 | c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466 |
| 冻结 R62 源 root_mixed_phase_normal_balls.py | 9012 | ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6 |

三件 Python 源位于同一 computations 目录，只需 Python 标准库。加载原 R280 之前逐字核两依赖；原 R280 再按其既定函数加载原 R62。没有复制或重写原 Sturm/余式/平方根内核。

## CLI 与明确预算

    python computations/geometry_20261115_rational_phase_cover.py \
      --input "$RUNNER_TEMP/phase-cases.json" \
      --out "$RUNNER_TEMP/phase-cover.json" \
      --sqrt-bits 128 \
      --max-depth 16 \
      --max-cells 8192

科学 main 同时要求 GITHUB_ACTIONS=true 和 GITHUB_REPOSITORY=Rogerhu12/math-research-public。输出文件必须尚不存在。

输入保持 R62/R280 的完整 cases 数组，每组科学值仍仅接受整数或准确有理/十进制字符串；中心、法向与四个连续误差半径的实际责任不变。预算为每个 case 的最大 dyadic 深度与已测试单元数，默认16和8192；sqrt-bits仍为原16..4096范围，默认128。

两张图均从闭区间[-1,1]开始，所有二分端点用 Fraction 精确形成。两个根区间会占两次已测单元预算；max-cells至少2。新算法不会改变输入半径或自动降低tau。

## 执行对象

先按原 R280 全圆入口得到完整旧记录。若原距离、移动端、固定端或联合全圆门已通过，直接保留该原证书，phase_cover.performed=false；没有执行的严格分区不报成已执行。

只有旧全圆门全部未付时，构造四项的两图目录：

- distance：原中心距离平方减去完整 $(2\tau+e)^2$，乘正的公共分母形成四次；
- moving、fixed、joint：直接使用原记录中的三个多项式；
- 每个第一图系数先补足五项，再倒序得到第二图；
- 第一图的三个已有 Sturm 链直接使用原记录，新距离和第二图使用同一原 R62 Sturm 函数；
- 每闭区间分别检查四项的两个严格端点值及全部内部实根，保持 OR。

广度优先处理。每次失败若预算允许则保存准确中点并同时入队两个闭子区间。深度或单元预算不足时，全部未付叶及尚未测队列完整输出，未测项的 exact_gate_tests=null。

## 输出

schema 为 R281-exact-rational-two-chart-phase-cover-v1。

每个 case 包含完整原 R280 记录、四个旧全圆布尔量、两图多项式及准确 Sturm 链、完整分区树和叶、每叶四项区间证据、原证书与新覆盖分开的结果。

主要字段：

| 字段 | 范围 |
|---|---|
| legacy_full_circle_certificate_pass | 原冻结全圆门实际结果 |
| polynomial_catalog | 只有执行新分区时形成；两个图各四项完整系数和Sturm链 |
| phase_cover.performed | 是否实际执行新分区 |
| phase_cover.complete_strict_phase_cover | 两张图的全部终止叶是否都严格支付 |
| phase_cover.complete_terminal_partition | 所有成功、未付及因预算未测的叶 |
| phase_cover.complete_split_records | 已二分单元、准确中点及两个孩子路径 |
| all_phase_distance_or_no_double_normal_pass | 原证书 OR 新完整覆盖 |
| unresolved_means_geometric_failure | 恒为false，不把预算不足当几何否定 |

源码始终不宣称连续球本身、完整空间块覆盖、实际曲率、嵌入或整面reach已经认证。原法向弦不等式诊断不会被混入排除零弦的门。没有任何native/fullDN/RHS/J/ODE调用。

## 新解析执行配置

证明 §281.6 定义唯一新配置：

- $p_0=(1,0,0)$，$q_0=(1/2,0,2)$；
- $n_0=(-3/5,0,4/5)$，$m_0=(3/5,0,4/5)$；
- 四误差半径均0，$\tau=6/5$。

它的全部旧全圆门失败。解析预期为：max-depth=2、max-cells至少8时，处理8个单元、二分3个单元、共5个终止叶，全部成功。第一图一叶和第二图两个外叶由moving支付；第二图两个内叶由distance支付。固定的门选择顺序是distance、moving、fixed、joint，只用于给多个已通过门选择一个日志标签，全部四项仍逐一计算。

max-depth=1且cell预算足够时，解析预期是第一图一叶成功、第二图两叶未付；它不是实际几何失败。这个预算受限读数可以与完整二级读数配对执行，直接检验资源范围表述。

上述均为解析/源码树推导，未填真实run或结果SHA，未在本地执行。

## Rule15 与静态范围

实际完整条件结果只在runner临时目录保留；公开源、配方、真实run、输出SHA及紧凑结论，不上传可重算raw到Git或Release。

本地只做源码AST、冻结依赖SHA与结构检查，不import数学模块，不调用evaluate、Sturm、有理根号、多项式求值或任一案例。R281登记不等待后续request111的执行。
