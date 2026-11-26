# 同一实际恢复场的三路后续入口

2026-11-26，Astra-held10-06bbeb39-20261126。当前只完成源码准备和语法验证，公共首M24恢复尚未返回；新command排在它之后，必须实际通过原prefix/raw门才运行。

入口 `scripts/resume_20261126/material_parallel_continue.py` 使用同一个runner内的 `m24-direct-recovery/run.json`，保存三个独立问题的身份：

1. 原M24 λ.002场接完整真实DN：.25/.5/.75/.9使用H_j f^j，随后fullH和最多原8outer；保留全部原门。仅作同原方程的设计求解。
2. 固定该实际场的完整δ、尾背景、材料图、圆化数据、mean1168和BC归一化.02，按R63将核心视作未知解，做M24原tol、M24加密tol1e-8、M32 tol1e-9三档，并比较完整六个Cartesian jets及精确有限weighted-l1系数差。完整说明见fixed-metric-three-stage note；三档不自动证明C²极限。
3. 原设计从M32及λ.016开始，向.032/.064/.128/.256/.512/.75/1继续；δ和核心系数仍可变。失败的已收敛场只能用作升谱初猜，不能当metric通过；域/求解失败只从最后accepted场细分λ步长。频率不足时按32/40/48/64/80/96/128升谱；保留原完整lift系数1，不乘λ。

三个子进程独立，不因某一方向失败而取消其他方向。M32端口使用已验证shared exporter生成，只有数值模式数变化，物理尾参数不变。每个真实accepted尾包的response.jets可直接给连续cut审计：全角S/D/A、转角积分的解析条带误差和精确Laurent Darboux；真实背景与端口/登记原数据逐项绑定，mpmath固定1.3.0。全部数组仍只在runner。

fullH入口现可显式指定同源完整accepted warm packet作初猜（`--initial-tail`），原worker继续核物理几何并重新验全部门；从.5续时可显式仅请求.75/.9/fullH。默认请求不变。新版源SHA为 `b1c40d7c35138687d31b6ec68f9258539741860fad4f91782d01ed5f64b4226a`。

这些入口不能将不同λ、δ、mean规则或不同场的已付界拼成一个闭面。各自实际run、hash和终态由summary记录；没有本条源码之外的新数值通过结论。
