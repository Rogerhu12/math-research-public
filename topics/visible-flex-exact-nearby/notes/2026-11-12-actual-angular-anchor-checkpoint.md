# 实际角锚与 D 零点检查点

完整证明见 R70。这里绑定重跑入口和有限实际范围；全两腿的1/64覆盖仍后台继续。

## 已完成

- δ5 第419段同一个实际主 germ，在完整 time R3/S4、物理 θ 带1/48上通过：
  实际 u0 harmonic anchor >.3141642545，扣全部真实时间／角尾后 D>.0720111770，
  Re(−K0)>.5769464296，两个支的 |dθ/dτ|<15.428783。
- 1/40、1/32、1/20 的选定实部锚策略失败，全部报告保留。失败没有被作为零点证明。
- 针对固定真实中心，另以8192个节点的**完整单元**二阶 Taylor 模界支付真实
  D 边界与准确 dyadic midpoint polygon 的无零同伦。最小裕量>.16952667，
  ∑Im log(z次/z前)/(2π)只包含整数−4；由真实实轴无零与环域辐角原理，
  上半物理带0<Imθ<1/32每π/2周期恰有4个D零点（按重数）。
- 新 static FFT 的 D 与真实角导 Dθ 已在4个独立节点用直接 Fourier 全和、
  无限 primitive 误差及完整相位公式核对重合。角导不是采样 DFT 的导数。

R70 明确：D 的复零点不自动证明某个特征速度有不可去极点，还缺分子检查；
更没有非线性 PDE 或闭面族不存在结论。1/40 的零点数量未判定。

## 精确重放

在课题目录设置 `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`。
共同 descriptor 为
`data/phase_ring_continuation/step5_retargeted_reference/descriptor.json`。

宽角失败组：

```bash
python scripts/fourfold_phase_actual_angle_anchor_domain.py \
  --retarget data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --widths 1/32,1/20 --wide-widths 1/20,1/16 \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_actual_angle_anchors.json.gz
```

通过1/48、保留1/40失败组：

```bash
python scripts/fourfold_phase_actual_angle_anchor_domain.py \
  --retarget data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --widths 1/48,1/40 --wide-widths 1/32,1/24 \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_actual_angle_anchors_narrow.json.gz
```

真实边界绕数：

```bash
python scripts/fourfold_phase_angle_boundary_winding.py \
  --retarget data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --width 1/32 --nodes 8192 \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_D_winding_1over32.json.gz
```

这些报告有 elapsed 字段；真正重跑可改变整文件 SHA，不能从摘要拼回报告。

## 输入到实际场构造

同一准确函数现在有两个不同已证双圆盘：
`(time R3, physical θ1/48, M15.428783)` 和
`(time R6, physical θ1/64, M32.586821)`。
同一 time/Fourier 系数可取这两个完整 Cauchy 界的较小者；不能擅自取它们的
矩形包络 R6×θ1/48。更窄角带的导数界可以由实际 M 的 Cauchy 不等式支付，
不必使用很大的 coarse frame 导数，但仍不是已经验证的流导数。

新整核心窄参数盒 θ1/48探针与全两腿覆盖都保持 live，未放入本冻结清单。
