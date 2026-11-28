# M12：完整角 Gram 的稀疏 Cartesian 分配律消费者

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

实际 M64/G12 已显示完整 Gram 装配用 1149.683 秒而原位 band factor 仅 5.625 秒，角收缩是当前真实瓶颈。强支的 sparse-jet 分配律实现提供了有效线索；M12 的接口不同，不能直接借其数值核或报告：这里是两个一阶 jet × 三个 Cartesian 分量，且每个 planar 系数耦合 cos/sin 的 xy 方向。

## 保留的完整数学式

原 full covariance、实际权重、所有三 Gram 残差行、径向累积、未知列、H2 增量范数和线搜索完全不变。对每个径向 block，新角核仍计算

$$
Q^{de}_{ij}=\sum_{\sigma,\tau,c,k}
 z^{d}_{\sigma,i,c}z^{e}_{\tau,j,k}
 \sum_\ell C_{dc,ek}(\theta_\ell)
 e^{i(m_{\sigma i}+m_{\tau j})\theta_\ell}.
$$

只是按已声明角列的结构零 Cartesian 系数选取活跃槽，避免生成含大量零项的完整 3×3 gather。所有非零 xy/xz/yz 交叉项、两个 signed Fourier 槽、height 常数与离散 alias 的 wrap/conjugate 都保留。它不按数值小量阈值删除任何 covariance 或 Fourier 模式。

分配律改变 floating 加法归并，因此这里明确不声称新 raw Gram 与旧入口字节相同。原 J/JT 的物理逐块消费者完全不改；实际每步仍用它支付 normal 检查，原能量和实际线搜索决定接受，连续场证书仍另算。

## 已真实执行的 M12 核

非零 C2 有限核：121 列、2304 行、2 个内三重结点，实际 alias 非空，完整角混合矩阵的非对角占比约 0.7895。自然 exit 0。新完整 Gram 相对原完整 contraction 的差为 1.0581472873671766e−16；独立 dense Cartesian J/H2 所得步相对差 1.3387707904672781e−14；实际正则 normal 为 1.4909279421339555e−15。重装原 Gram 后的 lambda 重试也通过。相同实际方向上的 disk/original physical Jd、JT r 和 JT(Jd+r) 仍逐字相同。

另在真正 M64/G12 暖输入 `06871d00d7c7c893b3e432da14ba358d2f1893a55ca021b428b533badf8ab4e5` 上核 6 个分开的真实 8 半径 block：训练 radial index 8、376、2000、2256、4496、5800，覆盖 prefix、有限 tail 和深 collar。每块 N1536、194 个实际 angular channel；完整 complex Q 逐项比较，不只比较其一个向量或 diagonal。

| 实际 block 起点 | 完整 complex Q 相对差 | 原角核秒数 | 新角核秒数 |
|---:|---:|---:|---:|
| 8 | 1.03075196968e-16 | 1.323607 | 0.215871 |
| 376 | 9.65155898434e-17 | 1.326116 | 0.333547 |
| 2000 | 1.85263316022e-16 | 1.600518 | 0.354816 |
| 2256 | 1.71759824474e-16 | 1.508860 | 0.317548 |
| 4496 | 7.26562594732e-17 | 1.811970 | 0.417394 |
| 5800 | 6.9495956802e-17 | 2.173105 | 0.275622 |

这六个真实块合计原角核 9.744175972s → 新角核 1.914797886s，约 5.0889 倍；只报告该次实测，不冒作整片预测或所有机器上的保证。完整 audit 自然 exit 0，34.655190348s，峰 RSS 483336 KiB。

## 实际消费边界与复现

新的 `2ecf-m12-h2-sparse-disk-normal-cached-lm.py` 供下一真实 physical h 使用，保留已经实核的单 band、disk physical rows、增量 H2、完整真暖输入 binding、单 N source cache、被动实际 nonlinear JT r 和原独立观察。正在运行的旧 M64/G12 入口未改；不回填旧 source SHA 或借其求解结论。

有限核命令：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-sparse-angular-c2-fixture.py --scripts scripts --out /tmp/m12-sparse-angular-fixture.json
```

实际 M64 block 核的完整命令如下；field 是上述真正 M64 暖转移场、parent-result 是真正 M48/G6 父场，G12 query 指已准确扩充的原源。入口内固定上述六个真实 block 起点，每块8点；所有输入SHA都在实际report核对。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-sparse-angular-actual-block-audit.py --scripts scripts --data <M12-prefix-data> --grid <M64-G12-output>/grid.json --field <M64-G12-output>/warm-transfer.json.field.npz --transfer-receipt <M64-G12-output>/warm-transfer.json --parent-result <actual-M48-G6-output>/result.json --query-report <actual-G12-source>/exact-tail-queries.json --query-cache <actual-G12-source>/exact-tail-queries.json.npz --out /tmp/m12-sparse-actual-block-audit.json
```

- `2ecf-m12-complete-sparse-cartesian-angular.py` SHA256 `a5c2715adaf7653f4e79f90c475c88f122bd0d08bbe0a9e901c006dbef606a64`。
- `2ecf-m12-complete-gram-sparse-assembly-only.py` SHA256 `2f0c09fec4cd047b47591b9c82d28ad631d1f600934ea5e2a2ebb9a6666fc409`。
- `2ecf-m12-h2-sparse-disk-normal-lm.py` SHA256 `cea3f36265a4a95e744b15d78e2d83512b7dd202e9038af4e15016d41d05ce9c`。
- `2ecf-m12-h2-c2-sparse-disk-normal-lm.py` SHA256 `88c64735695d67ca41623a32ad377dc77055aeec79b355f92b685f7e6c8b2313`。
- `2ecf-m12-h2-sparse-disk-normal-cached-lm.py` SHA256 `b9c3c361bdad2d2271bbd00e771a44dcfd02b20bb304b56d7f4198c65e2827ba`。
- `2ecf-m12-sparse-angular-c2-fixture.py` SHA256 `8cb4cbc7ef3a0299c6f84002d614b904e3bac3ded4f9a5acb9c708a3845957f4`。
- `2ecf-m12-sparse-angular-actual-block-audit.py` SHA256 `1cf4879c5326ff6c5ef5847c1dd3f1f256ee5b3d1ab1dab51b69a7f30f62af2f`。
- `sparse-angular-c2-fixture-final.json` SHA256 `c02cf8a9f22c021a55442d89b033c0698bd746c3cf597587073d9af9edc695d1`。
- `sparse-angular-actual-m64-block-audit.json` SHA256 `7892d20019336b7fc3d97096dfbf02aa00a7ade7db04a5c91c979f490cc901a6`。
