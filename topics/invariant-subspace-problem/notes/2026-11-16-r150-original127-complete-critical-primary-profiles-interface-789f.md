# 原 F127 完整临界主分量：广义检测精度的实际接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

本入口只读已经验证的完整 299 维 torsion 作用 $J$，确定原 $F_+,F_-,E_8$ 的五个不可约约化因子的**全部**循环指数和原坐标主分量。它不扫描素数，不重做原 NF、GB 或 whole torsion，也不将有限域主分量解释为特征零来源。第一系数连接的正负值属于后继任务。

## 1. 固定文件及 CLI

| 相对课题路径 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| notes/2026-11-16-r150-original127-complete-critical-primary-profiles-789f.py | d4425caa6811c11aced3da9d3d3661b0ca09b7dc | 13133 | 5b9b656473766069ff34df2e25f5f56cadda452cc504dd13094360d09abf3dea |
| notes/2026-11-16-r150-original127-complete-critical-primary-profiles-inputs-789f.json | 5020cc52f2e6806be07468525910af379530c91d | 2708 | f4fbdad39f25e3d082a3615cde97b69dbe08c8618e09c30d68372df6aeba23fc |

只读辅助源为已经实际运行过的九目标消费者：

- notes/2026-11-16-r150-original127-nine-target-cyclic-module-789f.py，blob b4e735dc12e8dee8b483728b895677dcfff23a09，20947 字节，SHA256 d520b190ac84f1990ed8ee84d405cc34c31d09e140ad26b8442c099872d26ed3；
- notes/2026-11-16-r150-original-hstar-integer-parameters-789f.json，blob bb66e2938a2625aa67059cea7f35a4816b64f4bc，1286 字节，SHA256 e04560989cfe0d888995290fa917b457f09f6caa975f59889ee0864e5b82ae31。

辅助源仅被 import，用其已付二进制 reader、域矩阵序列化及整数因子核验函数；不会调用其 main 或重建目标 Krylov 数据。主入口不需要九目标临时输出。

建议新 step 为 original127-complete-critical-primary-profile60，数学预算 60 秒、地址空间 512 MiB、外层 90 秒。唯一数值依赖为已成功 original127-complete-whole-torsion60。

~~~text
python {scripts}/2026-11-16-r150-original127-complete-critical-primary-profiles-789f.py
  --whole-out {work}/original127-whole-torsion
  --hstar {scripts}/2026-11-16-r150-original-hstar-integer-parameters-789f.json
  --sources-root {scripts}
  --out {work}/original127-critical-primary-profiles
  --seconds 60
  --memory-mib 512
~~~

输入 JSON 冻结全部三个实际临时文件的字节数及 SHA256。核心状态为 torsion-whole-state.bin：1,414,575 字节，SHA256 948d6e78dc96e8d9e367797d33919ce4c1e1deb406dee346505200da00ea4d60；其完整父 binding 为 05c13d9a57fee12f0751d40feccbfb601686b3d02f497d0e8a99092c44db4211。原 GB binding 及全部 6188 来源、自由方向和 whole 完整性标志也逐项检查。

没有声明本地执行或 AST 已通过；第一次 Python 解析与算术执行发生在真实 Actions 任务。

## 2. 从真实特征多项式选择完整主分量

先重新核原 $h_*$ 的全部 24 整数系数及其原三个因子，再在 $\mathbb F_{127}[s]$ 中将 $F_+,F_-,E_8$ 首一分解。必须得到五个互异不可约因子，每个在相应原多项式中指数为 1；每个都须出现在已付完整 $\chi_J$ 的因子表中。

将完整因子表重新相乘，必须逐系数等于原 300 个特征系数。对一个被选因子 $h$，记

$$
d=\deg h,\qquad m=v_h(\chi_J),\qquad H=h(J).
$$

程序不预填最大循环指数。它从 $a=1$ 起实际计算 $H^a$ 的秩及

$$
k_a=\dim_{\mathbb F_{127}}\ker H^a.
$$

其他主分量上 $h(J)$ 可逆，所以该核只含 $h$-primary。每个实际增量必须是 $d$ 的正倍数，且

$$
b_a=\frac{k_a-k_{a-1}}d
$$

按 $a$ 不增。$b_a$ 恰为循环指数至少 $a$ 的块数。只在实际 $k_a=dm$ 时停止，记此时 $a=r$。因此整个 primary 已覆盖，而不是只计算参数点上的 eigenspace。精确指数为：指数 $a$ 的块有 $b_a-b_{a+1}$ 个，其中 $b_{r+1}=0$。程序再核块数、最大值和指数总和 $m$。

这一阶段最多用到 $H^m$；$m$ 来自完整特征多项式，不是经验精度。

## 3. 原 299 坐标中的完整核、作用与乘回

在饱和的 $H^r$ 上作一次 RREF，以其实际非主元原行坐标规范出

$$
U_h\in\mathbb F_{127}^{299\times dm},
\qquad (U_h)_{\mathcal F_h}=I_{dm}.
$$

$\mathcal F_h$ 是实际 RREF 的原自由坐标集合。必须核全部原坐标身份：

$$
H^rU_h=0,\qquad
JU_h=U_hJ_h,\qquad
J_h=(JU_h)_{\mathcal F_h}.
$$

第一个等式、自由坐标单位阵及已知 $k_r=dm$ 共同证明 $U_h$ 是完整核基；第二个等式证明它是在**已付完整原 torsion** 中的参数不变子空间。不得把某个点空间中的基当作此对象。

再独立核

$$
\chi_{J_h}=h^m,\qquad
\operatorname{minpoly}(J_h)=h^r.
$$

最后把全部五个 $U_h$ 拼接，实际核其秩为各完整 primary 维数之和。每个 $U_h$、$J_h$、$\mathcal F_h$、全秩/零乘积统计和系数 hash 存在该 job 的临时 phase 文件。最终小回执只保存指数、秩、完整性与临时文件 descriptors。

## 4. 检查点和后继接受门

每个 primary 完整核验后独立原子保存。manifest 的语义 binding 包含本源码 SHA、辅助源 SHA、原 whole/GB binding、全部父文件 SHA 与原整数因子文件 SHA。同源码、同 out 可续接，只有完整匹配的 phase 才复用；本入口没有未绑定的隐式缓存。

SIGTERM 或预算只在完整操作边界请求退出。已完成的 primary 保留；未完成的 factor 不计为已付结论。所有异常的 type/message 同时写入 parameters.error，以免外层摘要过滤掉顶层诊断。

后继若在 $h$ 的有限扩域上构造 $t$-jet 泛函，应依据本次实际 $r$ 选择精度，并用原 $K_{805\times299}U_h$ 检验这些泛函限制在**整个** $dm$ 维主分量上的秩。仅有一个最高指数链或点值非零/零都不足以给完整负结论。尤其多个循环块时，必须覆盖每个块；所有 1834 个原全参数 Z 来源仍须保留。

本入口不计算任何第一系数 $127$ Bockstein，不给 $\mu$ 的新次数，也不声称该 primary 是算术扭或真 Q 参数扭。其作用是使后继精度及覆盖范围由真实完整数据确定。
