# 全 Gauss 径向加权残差谱：下一次空间选择的实际依据

2026-11-20 UTC。读同一 [3a3 十二步终态](2026-11-20-curvature-qp-gauss-twelve-step-02-result.md)，不改候选或标量，不执行求解，也不认证连续频谱。该父有已知胞内曲率点超过求解器 `.98` 余量，以下谱不能解除那项几何责任。

## 精确有限目标的分解

保持 7377 个径向观察、2048 全角（513 个重数代表点），以及 $.5$ 原 Simpson 加 $.5$ 新 Gauss 的正径向权。对两个偶 Gram 分量作 type-I DCT，对奇的交叉分量作 type-I DST；端点与最高余弦采用其准确有限 Parseval 权，交叉分量保 Frobenius 因子2。浮点奇分量在端点的余量另计，不默认为零。

这里的 mode $j$ 是四分之一域余弦/正弦展开中的 $\cos(2j\phi),\sin(2j\phi)$。对每个模的平方能量使用同一径向正权求和，再乘原完整角点数。得到的只是原有限观察目标的恒等分解；不把它当成连续傅里叶截断误差界。

实际目标为 `.34559813964253105`，Parseval 重构为 `.34559813964253144`，差 `3.885780586188048e-16`。按每个真实胞的 Simpson 两端/中点及 Gauss 权重新分配，胞能量和为 `.3455981396425311`，没有把共享节点的两侧权都归给某一胞。

## 读出与直接含义

| 累计角能量 | 到达的 mode |
|---|---:|
| 50% | 2 |
| 90% | 7 |
| 99% | 15 |
| 99.9% | 35 |
| 99.99% | 96 |

mode>12 的总能量占 **3.1084458433%**；mode>24 占 **.1285702482%**，mode>48 占 **.0908900513%**。残差仍主要在当前物理方向已经包含的低角模中，不能据此优先无限增加角频率。高频仍非零，最终同 $g$ 精化当然仍须支付。

三项实际加权 SSE 为：

| 分量 | 加权 SSE | 物理意义 |
|---|---:|---|
| $r_{ss}^2$ | .20348205313701428 | 径向长度误差 |
| $2r_{s\phi}^2$ | .0626801677982228 | 非正交误差 |
| $r_{\phi\phi}^2$ | .079435918707294 | 环向长度误差 |

全点最大 Gram 在 cell839、新 stage6881：$s=1.2252440544749044$、$\phi=\pi/2$，三个相对分量为

$$r_{ss}=.05470303672415744,\qquad r_{s\phi}=0,\qquad
r_{\phi\phi}=-.006912033104673143.$$

因此当前最大值由径向伸长控制。相邻 cells832–847 的主要峰也在 $\phi=\pi/2$；这不是只有一个异常角点。最重的真实胞845为 $[1.3380077824366778,1.3580749679324564]$，独占目标的3.2528249%。

按观察位置分箱（仍是同一有限正权和），$s∈[1.1,1.6)$ 占49.3917837%，$s∈[2,S]$ 占17.6099027%；$s<1$ 合计约12.8067%。这些分箱不是另一连续积分，也不支持冻结前缀；它们只说明下一步应优先处理低模径向方向、物理平滑高度及实际曲率约束。完整自由空间方向仍保留全部变量。

## 源、输入和复现

小源 [read_gauss_residual_spectrum_20261120.py](../scripts/read_gauss_residual_spectrum_20261120.py)，SHA256 `1705bee9921b429152943f78065bc24f2b541898de71b5230d5deaa85ed1300c`。

输入 bundle SHA256 `3a3f77c9363ec866c4f8e12d294d226ef2f9d7bbabfbe258819a009177c8477c`；同标量 carrier SHA256 `71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`。源内绑定原 dense、batched 和全 Gauss 三个已刊源；实际报告记录它们的完整 SHA，没有新的标量查询。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/read_gauss_residual_spectrum_20261120.py" \
 --repo "$repo" \
 --bundle "$work/geometry_path/curvature-qp-gauss-twelve-step-02.npz" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --angles 2048 --legacy-fraction .5 \
 --out "$work/root/gauss-twelve-step-02-spectrum.json"
```

实际进程自然 exit0，约 .864 秒；报告 SHA256 为 `7f915a3f62e8ab2e5e97f03a0a082a8c23fc8fcac20316c17f3e23c87e433677`。raw 分量数组及完整报告仅留 scratch；源和以上参数可重建全部读出。下一步仍是实际约束求解，不把谱诊断或更多采样本身认领为误差收敛。
