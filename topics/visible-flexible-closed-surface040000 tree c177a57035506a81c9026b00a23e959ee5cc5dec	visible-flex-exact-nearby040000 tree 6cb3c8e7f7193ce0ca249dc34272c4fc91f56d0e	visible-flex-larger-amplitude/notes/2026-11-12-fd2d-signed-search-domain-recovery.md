# R182 连续 K 域的明确恢复 schema 与窗口子集安装

状态：**沿 R182 §7 已证有限充分域重新实现的恢复源码；当前未执行 Python。**
旧 domain-02 的完整键内容和源字节在此次 executor 失联时不可见，且当时
尚未推入 main。不能把新源码或重新生成的包冒称旧 02 SHA。

新源 scripts/fd2d_gc_signed_search_domain_recovery.py，26607 B，
SHA256 4bd8bdd374ed4280f81f15264510f587ac2af47e2b7e401e71c9ee8c542e6c49。

## 1. 生成器及准确有限域

默认输入是已推 R182 行包和报告，SHA256 分别为
d7f990bcef75ec30311e23d3cf92dadf5736f871f141dd3f7fa62071f7793095
和 44d3d9318ffa7b70f7bcc59cebf81df09e72b9c37562c05e1410cdb65b627a68。

生成器核准确身份、每窗完整闭支撑覆盖和各源盒负 $a_{ss}$ 余量，
按真实 compact bump 支持端点再分子盒，不重算 profile 区间、ODE 或 F/J。
每个 bump 二导在子盒上是 degree 8 多项式。以准确有理算法转换到
Bernstein 控制行 $A_{b,k,j}$，沿用父盒 base 上界 $u_b$，
取父盒原负二导余量的一半 $\eta_b>0$。要求

$$
\sum_j A_{b,k,j}\delta_j\le-\eta_b-u_b
\qquad(k=0,\ldots,8)
$$

即连续保证子盒上 $a_{ss}\le-\eta_b$。证明由 Bernstein 基函数非负且和为一，
再用完整子盒覆盖；与 R182 §7 相同。新 schema 为
fd2d-R182-Bernstein-positive-K-domain-recovery-v1，显式保存全部 children、
九行控制系数、四端点、actual supports、原 binary64 0.08 盒及输入/QP 身份。

## 2. binary64 QP 行的充分性

对准确行 $A\delta\le b$，逐项取 binary64 的 $\widehat A$，在
$|\delta_j|\le M_j$ 上计算准确预算

$$
e=\sum_j|\widehat A_j-A_j|M_j.
$$

取不超过 $b-e$ 的 binary64 下取整 $\widehat b$，
保存矩阵行 $M=-\widehat A$ 和下界 $\ell=-\widehat b$。
若 $M\delta\ge\ell$，则

$$
A\delta\le\widehat A\delta+e\le\widehat b+e\le b.
$$

ordinary_lower 只是诊断，不作证明输入。生成器使用原准确 binary64 0.08，
不是擅自替换成 $2/25$。安装时对每个将追加的行再次核准确预算。
QP 的浮点容差仍不代替 candidate 的精确核；handle.verify_delta 单独消费准确行。

当前七参数盒给出 $a\ge4/5-\sum_jM_j>0$，原 radius39 域仍保留。
新物理设计列需要自己的完整域证书，不能借本 J7 包自动通过。

## 3. 按实际四端点选择窗口

API：

    handle = install_signed_search_domain(
        problem, windows=problem.signed_windows,
        domain_path=..., qp_path=...)

按四个准确 dyadic breaks 完全相同匹配，名称和迹符号不选择 K 行。
实际 name/sign 完整写入 subset definition，以免把另一字段定义冒成同一场。

QP row_owner 是 (child_index, Bernstein k)。
选中的窗口带入全部 children 和每个 child 的九行；未选窗口所有行排除。
完整 row_owner 的顺序、唯一性、计数与新 exact packet 相符。

middle-only 删除全部 late 行。middle 闭支撑在第七个 bump 左端之前，
所以剩余行第七列准确为零；不能让旧 late 约束残留锁住 $\delta_7$。
R186 的新系数射线与 middle-only K 域相容，晚正 K 行不能继续约束新负 K 设计。

安装器保留 problem.profile_domain 的其他键，只在原 matrix/lower 后追加行。
全局参数位置按 actual profile_parameter_slice 记录，不写死 47:54，不猜 tail 数量。

## 4. Context 的明确责任

handle.delta_absolute_bounds 给出原准确盒的 binary64 数组；
Context 的 profile_box 不能超过它。安装器不暗中重复添加 ±I 行，
不包装 problem.parameter_domain，也不改变原 active provider 方法。

每个实际 trial 和接受保存前，Context 应显式调用：

    certificate = handle.verify_delta(p[problem.profile_parameter_slice])
    accepted_domain = certificate["passed"]

函数以 Fraction 核实际参数的准确盒、全部选中行及充分半径下界，
返回 passed、准确 minimum slack、最坏 global child/degree、实际 delta 和 subset binding。
每次 checkpoint 要保存 handle.definition() 和当前真实 certificate；
不能从旧 warm 复制旧 tail 或旧 delta 的证明。

本模块不改变完整场、节点/单元残差或其 Jacobian。

## 5. 恢复后的真实生成命令

使用原 NumPy 环境，在 topic cwd：

    python scripts/fd2d_gc_signed_search_domain_recovery.py \
      --out-prefix notes/2026-11-12-fd2d-signed-domain-recovery-01

生成三个新文件：

- notes/2026-11-12-fd2d-signed-domain-recovery-01-domain.json.gz；
- notes/2026-11-12-fd2d-signed-domain-recovery-01-qp.npz；
- notes/2026-11-12-fd2d-signed-domain-recovery-01-report.json。

请求应指新 domain/qp，不能指尚未恢复的旧 02。
当前新包没有生成；预期 180 children/1620 行不当恢复后实际记录。
CLI 将报告实际数量、原中心准确可行性、新身份及耗时。
输出必须另名，不覆盖已有完成/失败包。

本源仅通过授权小文本 API 保存，没有传二进制或其编码。
若恢复后原 02 实体仍可读，旧主线可以继续原目标；本模块是明确的新恢复选择，
不授权静默替换已有 active source。
