# R133：真实保存的 M256、alpha=.75 主体几何诊断

**完整运行的浮点诊断；不是连续几何证明。**
`fourfold_codazzi_reciprocal_frame_probe.py` 读取先前 M256 `accepted000` 的所有
保存三次系数，在实际全长 $0\le r\le25/8$ 上，用每四分之一圆 2048 个角点，
径向最大步长 .001 加全部原节点，以 RK4 积分完整位置与标架。起始标架在
实际保存的右端使用旋转参考；两条真实物理 $B,C$ 迹的失配原样测量，未投影
为零。先向腰部积分得到高度平移，再独立重复一遍向内计算全部几何量。

输入仍为未宣称有限 BVP 收敛的那个准确保存中心，固定参数为
$\alpha=3/4$、$\nu=-2443457753738987/72057594037927936$。
整段共用同一个新度量参数；未拼接旧 $g_0$ 的几何数字。

| 实际采样量 | 数值 |
|---|---:|
| 名义反射样本直径 $2\max|F|$ | 2.5510906727069504 |
| 所选相位腰部见证到主体样本的最近距离 | .12648040123085832 |
| 上两者比值 | .049578951694668916 |
| 候选第二形式的最大绝对主曲率 | 8.72292958247977 |
| 重建位置微分得到的最大绝对主曲率 | 8.72351225311392 |
| 重建位置与实际法向的最小支撑 | .9086428390868262 |
| 最大相对角向度量误差 | $8.209324\cdot10^{-8}$ |
| 最大位置角约束误差 | $6.870437\cdot10^{-7}$ |
| 最大标架角约束误差 | $2.241791\cdot10^{-5}$ |
| 腰部高度范围 | $[-5.995709,4.510518]\cdot10^{-10}$ |
| 腰部经向标架距垂直方向 | $<3.041206\cdot10^{-8}$ |

进程正常完成，耗时约 324.35 秒。完整报告为
`2026-11-13-R133-reciprocal-m256-alpha075-accepted000-full-geometry-floating.json`；
其中保留所有依赖、实际原始输入、输出几何哈希及范围限制。
可重建的几何数组在 scratch 中，不重复提交大中间数据。重建命令如下：

```sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_codazzi_reciprocal_frame_probe.py \
  --candidate /workspace/scratch/ac0d699811ad/reciprocal-m256-alpha075-accepted000-candidate.json \
  --anchor regular --angles 2048 --step .001 --coefficient-batch 8 --save-radial 24 \
  --out notes/2026-11-13-R133-reciprocal-m256-alpha075-accepted000-full-geometry-floating.json \
  --geometry /workspace/scratch/ac0d699811ad/reciprocal-m256-alpha075-accepted000-full-geometry.npz.gz
```

该输出保护原文件；复跑应另用新输出名。输入如丢失，按原 accepted000 的
无损重建记录恢复，不能从少数标量或截断曲线猜测完整场。

## 对实际任务的含义与精确限制

所选见证的样本比值尚低于 .05，因而没有给后验修正留下所需的可见性余量。
这不是对所有可能见证的排除证明，也不是 .75 幅度绝不可能合格的定理。
下一次数值延拓将增加实际振幅，并重新支付该候选的完整几何。

有限样本最近距离是到连续主体最近距离的上界；在没有覆盖网和连续导数
误差前不能把它作 held 的下界。这里也没有包括最终闭帽、固定非共面曲率
marker 及全部无限尾，名义反射仍受非零腰部约束误差影响。采样曲率和支撑
因此不授予闭面 reach、全环境不全等或最终闭合结论。

脚本的腰部相位原函数按全部采样 Fourier 模用 FFT 计算。最高 sine 是完整
角网格的 Nyquist sine，恰在所有网格点为零；没有删去一个非零采样值。该
等价重排避免构造稠密“频率乘角点”矩阵，不是连续尾证书。
