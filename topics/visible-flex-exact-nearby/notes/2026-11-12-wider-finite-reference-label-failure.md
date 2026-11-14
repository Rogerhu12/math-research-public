# 扩大有限参考标签带的实际失败

2026-11-12。以完整当前准确参考，调用 `fourfold_packaged_reference_bidisk.continuous_bidisk`，
segment=6、419；(R,T)=(2,1/16),(3,1/16),(6,1/16),(2,3/32),(2,1/8)，
每格 nodes=512、taylor_order=8、bits=256。全部参数、identity及有向输出见
`2026-11-12-forward-wider-finite-label-gates.json`。这些更宽q门均失败，不能用于密度重构。
有限高频项在较宽复带会放大；这是所选有限参考的此项粗门失败，不是实际几何返回不解析的证明。
继续使用已经证明的标签带和R6真时间扩域，没有静默扩大工作域。
