# 首次实际 n3 native 批与已存三段基线的字节比较

**状态：只读实际输入和输出的有限身份核对；没有重新求根、积分或调用 DN。**

[独立 n3 算术基线](2026-11-18-m3-native-baseline-and-production-floor-scope.md) 的三段测试使用域门 `.1`；[实际原 DN](2026-11-18-m3-trace-path-lam064-native-tail-accepted.md) 保持生产域门 `.05`。本条读取两次已经完成并保存的计算，直接检查它们相同部分的输入及最终 binary64 输出，补充两种 floor 在这三个具体样本上的联系。

读取的是实际 session 92035 第一次本来必需的 full-Jacobian 批，输入 SHA `aa63eaaaa080b2c195f4d3331e6e462ab9aeb9eda74bbb7622b60e8d9f10589c`，输出 SHA `c699ebd03472c8be0a276533470863eee3b957948110949137bfa95a6bda8e6c`。该批已完成，原四个 CLI 子进程均为 0；它不是另加一次全态预计算。

输入逐段解码确认：1152 段的全部 18432 个物理初始值，均逐字等于原失败 checkpoint `753aa9ec…` 对应的下一节点状态；2304 个辅助初值均为原零值。halving factors 与完整 literal 三角表也逐字等于独立基线。这里只核输入，不把原失败初值写成已接受解。

| 原段号 | 原网格步数／不同系数点数 | 原初值、系数、网格完整序列 | `.05` 与 `.1` 的 18 个输出 | 18×16 字面 Jacobian 输出 |
|---:|---:|---|---|---|
| 86 | 16／33 | 逐位相同 | 逐位相同 | 逐位相同 |
| 87 | 16／33 | 逐位相同 | 逐位相同 | 逐位相同 |
| 88 | 16／33 | 逐位相同 | 逐位相同 | 逐位相同 |

比较包括零的符号；每项相同是对保存的 binary64 字节串作直接相等比较。完整批的 20736 个状态输出和 331776 个 Jacobian 输出均有原顺序和成功状态，但独立 `.1` 对照只覆盖表中的三段，不能由此推成全部 1152 段的跨 floor 等价。

该结果也不证明内部 extended-precision 根迭代的每一步相同，因为本次实际批未保存那些轨迹。它不新增连续误差界、导数精度结论、ODE 极限或完整曲面接受。生产中对原初值的全残差仍为 $1.4670069281833668\times10^{-8}$，随后由原 Newton 两次修正才通过原门；不能因三个输出匹配而省掉那两次真实求解。

可复现的只读比较源为 [compare_m3_native_first_batch.py](../scripts/resume_closed/compare_m3_native_first_batch.py)，SHA `bbeb7aa62086a88db27fbaf21a33c88baf82950ef70be2b9c832b82f864a4dc4`；它只调用已冻结 ABI helper 的序列化函数。全部来源、运行命令、三个输入／输出哈希及范围标记见 [紧凑记录](../scripts/resume_closed/m3_preserved_native_first_batch.json)。实际只读执行块 `01d6ab`，2026-11-18 05:46:20 UTC，exit=0；新 flow、root、DN 调用数均为 0。可再生二进制大块和三段完整矩阵保留在 scratch，不放入 Git。
