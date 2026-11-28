# R85 的完整 24 列响应基：实际返回

2026-11-28，本次对已保存、已登记的完整 M24 CSR 矩阵实际计算了全部
24 个端口响应列。唯一数值进程为工具 session `5290`，真实 exit `0`；
程序记录耗时 `6.976032956998097 s`，自观测 `ru_maxrss=401576 KiB`。
此前 `/usr/bin/time` 不存在导致外层命令 exit `127`，当时 Python 未启动，
不是一次数值重算或数学失败。

入口是已发布的
`scripts/resume_20261128/analytic/complete_terminal_response_basis.py`，
SHA256 `4e212d96a75d9fdc6ed864707c615c6471d98864079eb9c245fc4afee48976de`。
本次没有重新组装 J、导入物理 Flow、请求尾响应或求解 BVP。
每列计算的是原完整矩阵的 `BlockQR.solve(U e_j)`，保留全部
`N=73*879+24=64191` 个未知量及原完整矩阵残差。

## 实际来源与结果

完整来源和每列文件 SHA、原残差见同名 `.json`。核心身份如下：

| 对象 | SHA256 |
| --- | --- |
| 已登记完整 CSR `actual_direct_csr.npz` | `1814497d5cb4d5159b3f90eb52be4ff276cf281cb4a05cc29547b2b4a179265c` |
| 原 J 输入 `lambda002_m24_jac_input.npz` | `c9c4906fb944a82d59f752d74332157dc564b841d269148de20206d937a4edde` |
| 原接受解 `lambda002_m24/run.json` | `1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891` |
| 本次 `response-basis.json` | `e066c3d1a1d509d0955eedd1427fb1849018930b42faeef5b8b2e5b2af2940f7` |

本次响应目录为
`/workspace/scratch/7c4e33ee17de/held10-analytic-work/lambda002-m24-terminal-response-basis-20261128-a`。
24 个完整 `response-000.npy` 至 `response-023.npy` 均已返回并逐文件再核 SHA，
合计 `12327744` 字节（含各 NPY 文件头）；同名 JSON 的
`storage.total_response_file_bytes` 保存此实际合计。数组只留 scratch，不进入仓库。

24 列中最大原完整矩阵残差为
`1.199040866595169e-14`（无穷范数），最大二范数为
`1.3144390305906736e-14`。这些是完整浮点残差观测，尚不是严格误差界。
因子保留原统计：`solve_calls=24`、`refinement_steps=19`、
`minimum_relative_R_diagonal=5.5954091728240306e-5`、
最大 normwise backward error `2.5065492864508704e-17`。
原最大 componentwise backward error 为 `1.0`，照实保留；
不能用其余较小数值把它改写为统一的逐分量证书。

## 旧点与接受点的完整坐标核对

真实保存的 J 输入和接受 raw 的全部 `x`（879 项）以及全部 `pscale`
（23 项）形状、dtype、字节逐一相同。全部 `y` 和 `p` 不相同：
`max|Δy|=6.98562548930589e-6`，
`max|Δp|=418.73151328774316`，后者是原归一化参数坐标。
原 p0 为 `-9.684446197347202e-6`，接受 p0 为
`-9.683937550986032e-6`。

因此本次响应基是已知完整**旧点弦线矩阵**的响应基。它与后续初猜共享
计算坐标、网格、参数单位以及同一字面模型定义；不声称两个 p0 所定义的
物理 s 图相同，更不把旧 J 当成接受点 J。

## 已付与未付

R85 的完整有限秩更新现在有了真实全部 V 列，可按既定完整残差恒等式
构造端口初猜或再做小矩阵分析。尚未支付当前点完整 J 差、响应列的严格
误差包络、全 DN 逆界、非线性余项或原 BVP 的全部接受门。
本条不产生新接受曲面、不产生固定 g 精化、不代表 λ=1 已返回。
