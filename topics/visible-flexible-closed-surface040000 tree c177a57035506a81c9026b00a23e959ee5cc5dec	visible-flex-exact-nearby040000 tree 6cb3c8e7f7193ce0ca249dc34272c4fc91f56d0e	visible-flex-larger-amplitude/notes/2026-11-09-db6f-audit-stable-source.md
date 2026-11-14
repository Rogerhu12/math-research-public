# Cap 导数正因子式的独立复核

2026-11-09，`/root/independent_geometry`。已独立核读 `scripts/db6f_tail_interval_source_stable.py`，冻结 SHA256 为 `8d485eb6f9cead594ed22ce491d363a3916a418404f905645c7f0eec0bafdcac`。本次修改只改善区间求值，不更改 source、目标度量或任何解析导数，结论 **PASS**。

精确有理系数乘法给出恒等式

$$
1-t^4(35-84t+70t^2-20t^3)
=(1-t)^4(1+4t+10t^2+20t^3).
$$

两边的幂系数均为 $(1,0,0,0,-35,84,-70,20)$，见独立机器记录 `2026-11-09-db6f-audit-cap-derivative-factorization.json`。这不是浮点拟合：恒等式在所有实数 t 上成立，其全部 normalized derivatives 因而相同。原模块与新模块使用同一个已审 Jet、I 和初等函数组件。

记该多项式为 d。由于

$$
d(0)=1,\qquad d(1)=0,\qquad
d'(t)=-140t^3(1-t)^3\le0\quad(0\le t\le1),
$$

middle cap 分支上 $0\le d\le1$。新实现仅将 d 的常数项区间与 [0,1] 相交；高阶槽仍采用原有区间 Jet 递推。整个盒属于 middle branch 时，这一相交包围每个真实值。跨分支盒中，tc 的值范围已经被限制在实际 middle 子集，外侧分支另作 hull，因此相交仍合法。没有把导数的高阶槽截断或强行设零。

审查者另以 Python AST 比较了原 `FrozenSource.evaluate` 与继承类的新方法：除 d 的这一个等价赋值和常数项区间相交之外，所有语句的语法树完全相同。构造函数、有限 calibration、参数守卫和 cell 缓存继承原实现。记录见 `2026-11-09-db6f-audit-stable-source.json`。

配套 builder `scripts/db6f-tail-build-background-primitive-stable.py` 的 SHA256 为 `5843f0b9898ac101a516e6eacadd9cb3ab529b94cda3f0bb4164a5e6ac6da465`。它与已审原 builder 的差异只有导入 stable model，以及同时记录原/新 model 的 hash；积分、锚点和区间 primitive 算法未变。其 Jet 类型与 primitive 使用的旧模块 Jet 是同一个类，不存在复制类型导致的混用问题。

原 tight-alpha 证书保持原文件和原 hash，不用本修改追改历史。新 primitive 的完整运行、覆盖和由它产生的物理 r 背景包仍须检查；本次恒等式审查不单独支付这些输出。
