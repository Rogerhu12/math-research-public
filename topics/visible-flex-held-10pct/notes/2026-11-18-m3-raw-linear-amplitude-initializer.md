# 原始补弧控制的线性物理增幅初猜

状态：**初猜算法和有限实现检查**，不是新的幅值解或同 $g$ 精化。当前 $\lambda=1$、二阶数值正性界入口的实际求解未导入本安装器，也没有改动运行源。

## 1. 为什么单独改初猜

原自适应重启对第 $j\ge1$ 个参数槽使用

$$
c_j^{\rm init}=c_j^{\rm old}r^{j+1},\qquad
r=\frac{q_{\rm target}}{q_{\rm old,actual}}.
$$

该初猜来自原余弦幅值支的阶数习惯。对 `raw-mean-primary-compact-v1`，各 $c_j$ 是完整补弧支撑函数的独立物理控制，不能假定仍按 $q^{j+1}$ 分级。这里准备另一种明确初猜：

$$
c_j^{\rm init}=r c_j^{\rm old},\qquad
p_j^{\rm init}=\frac{c_j^{\rm init}}{\mathrm{pscale}_j}.
$$

它只是新的数值预测器，不宣称这一缩放满足非线性方程。后续仍由原完整前缀、真实尾和全部门判断。只有取得合适的精确圆弧锚点后，才把它用于新的实际增幅。

`install_raw_linear_amplitude_restart.py` 在独立 BVP 子类上读取原 `restart`，唯一替换控制表达式 `ratio**(j+1)` 为 `ratio`，并沿用已登记的共享 $C^2$ 入口修复。相对于已有 $C^2$ 重启，材料角回拉、场的幅值预测、规范换算、网格、$\delta$ 初值和修复窗全部保留；残差、Jacobian、核心定义和任何接受门都不改变。安装器要求原两个字面位置各恰出现一次。

入口修复仍为

$$
a(s)\chi(s)\,[Y_{\rm inlet}(p)-Y_{\rm pulled}(0)],
$$

其中 $\chi=1$ 至 $.5L_{\rm prefix}$，从 $.9L_{\rm prefix}$ 起为零，中间采用同一个五次 smoothstep。改变控制预测器会改变入口修复量；不把新的初始整图称为旧整图。

## 2. 一次有限初猜检查

使用已登记的 raw $\lambda=.02$/M16 真联合有限态。它的原有限门通过，但完整 metric 为 $9.357262954\times10^{-5}$、未过 $10^{-6}$；本检查不改变这一分类。

- 输入 CP：`beta4625-q040-raw-lam002-fixed-m16-neighbor/seed.json.gz`，SHA-256 `6f5a973c746e1112f827e5478432b9abe9d14931df90157f2a19381cc670b91e`。
- 原规范幅值 $.04$，实际幅值 $.03991248545080898$；新初猜规范/实际幅值均为 $.045$，故 $r=1.1274667435948393$。
- 原 $\lambda=.02,a=.21,b_{\rm primary}=.08,b_{\rm control}=.16$，M16、角节点 512；指定径向初始点 257，合并原断点后为 271。
- 执行句柄 55550，实际观察到退出码 0；无 BVP 或新尾调用。

| 检查 | 结果与范围 |
|---|---:|
| 回写物理控制与 $r c^{\rm old}$ 的最大差 | $1.3234889800848443\times10^{-23}$，浮点规范往返误差 |
| 原、线性预测器的初始尾高度 $H$ | 全分量逐位相同 |
| $.9L_{\rm prefix}$ 以外的有限系数字段 | 全部逐位相同 |
| 两初始字段之差与入口差乘同一修复窗之差 | $1.4132914131527452\times10^{-16}$ |
| 原幂次初猜的数值 $\rho$ 下界 | $.5760301953703294$ |
| 线性物理控制初猜的数值 $\rho$ 下界 | $.620548734019846$ |

最后两项只是原数值核心正性检查；没有复算全域 Frenet/metric，也不意味着新的 Newton 收敛或幅值容量提高。不同初猜间尾 $H$ 相同来自修复窗在末端为零，不等于相对旧幅值解的 $H$ 不变。

## 3. 复现与来源

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/probe_raw_linear_amplitude_restart.py \
  --source-topic /workspace/scratch/7322d0dee069/m3_work/shared-neighbor-source \
  --short-bridge /workspace/scratch/7322d0dee069/m3_work/recovered-valley-design/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py \
  --restart /workspace/scratch/7322d0dee069/m3_work/beta4625-q040-raw-lam002-fixed-m16-neighbor/seed.json.gz \
  --linear-port /workspace/scratch/7322d0dee069/m3_work/beta4625-q040-raw-lam002-fixed-m16-neighbor/prefix-port.json \
  --amplitude .045 --nodes 257 \
  --out /workspace/scratch/7322d0dee069/m3_work/raw-linear-amplitude-initializer-probe.json
```

源、参数、实际退出状态和全部输入分块哈希见 `scripts/resume_m3/raw_linear_amplitude_restart_record.json`。完整诊断仅留 scratch，SHA-256 `a7be5f0c1ed5174ba3ec951629cb666863be6e596e75aa26034d47e2f67a260d`；不向 Git 放径向字段或可重算数组。

安装器 SHA-256：`5d83c9836b8627e59406308015fa848f66b1588e578b33fc54de0ccf933067d6`。
探针 SHA-256：`97e8744e02c0a0df1e752708d20113c9bb1189847c5fc4f5b1fc3b96e74a2180`。
