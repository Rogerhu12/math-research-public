# longdouble 角缓存 v2：排除 padding，不舍弃数值精度

日期：2026-11-28。首个实际 H2 cold 运行的 v1 缓存返回值全部通过原长 double evaluator 的精确比较，但实际生成了 84 组缓存，而数学上仅有 N384/N768 两组角数组。原因是 x86 extended longdouble 的 16-byte 存储含 padding：相同 80-bit 数值的原始 bytes 可不同。这是缓存命中问题，未改变首场计算或 g。

新 `2ecf-m12-h2-cached-direct-lm-v2.py` 保持全部乘法结合与求和顺序，只以全部 longdouble **数值相等加 signbit 相等**查找已有角数组；既不向 binary64 舍入来制键，也不把正负零混合。每个真实角网格和导数阶的首次调用继续与原 evaluator 比较返回数值及生产 binary64 bytes。

实际针对上述缺陷检查：平台 128-bit storage、63-bit fraction；N384/N768 两个非均匀角向量，各取三个原源 cache 系数行、位置及一/二角导数，将每个 longdouble 后六个 padding bytes 分别写为 0/173/81，完成 54 次调用。全部长 double 值相等，生产 binary64 bytes 相等；实际只建 2 组缓存。耗时 2.991938905s。该检查没有生成新的非线性场；新的 C2 实步将另行报告。

- 新入口 SHA256：`b69d67754d935a4e4342c934f80e5272d520f86164804c710350cf412a805745`。
- 针对缺陷检查回执 SHA256：`ed1a36a2b8c436e1507c11c2799a0c376025d154ace42fb407219cc43f79c5ce`。
- 原 source evaluator SHA256：`7214054f65bfbd1055122dddf235074bc812c88cdf5d418b630877bf8b21880b`。

v1 首场与其报告不作回写。v2 仍依赖已登记 H2 核与 C2 adapter；参数接口及其检查保持不变。
