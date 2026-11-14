# checkpoint 到一般 core 角图的物理拉回与高度均值

2026-11-10，visible-larger-astra-20261110 / geometric_amplification。

**状态：拉回与二阶链式公式已证明，实现已在两种真实 checkpoint 上运行；输出只是初猜，不是新解。** 代码为 `computations/geometric-checkpoint-core-pullback.py`。

## 1. 为什么不能只补零或重投影同一个数组

旧 Fourier 数组描述旧辅助角 $\eta$ 和旧参考图下的扰动。新角图为 $\theta_{\rm new}(s,\psi)$ 时，表示同一个物理点的旧角必须满足

$$
\theta_{\rm old}(s,\eta(s,\psi))=\theta_{\rm new}(s,\psi).
$$

旧、新数值角的正导数保证这个逆唯一存在。转换器在完整未取模角上用带括区间的 Newton 法求它；代码没有用 $\eta=\psi$ 或索引补零冒充角图转换。

在同一个真实径向坐标 $s$ 上，先重建旧实际位置

$$
F_{\rm old}(s,\eta)=X_{\rm ref,old}(s,\eta)
+q_{\rm old}Y_{\rm old}(s,\eta)+H_{\rm old}(s)e_z.
$$

拉回后减去新参考，再对新角 $\psi$ 投影。**这个减参考步骤本身不改变像；有限 Fourier 投影一般会改变像，代码单独报告其误差。**

当前接口要求新旧物理径向长度相同，拒绝静默把 $s$ 换成不同长度的归一化坐标。设计延拓若要改变度量或长度，应另外明确那一步是初猜变形。

## 2. 隐式角变换的二阶导数

在旧角 $\eta(s,\psi)$ 处记 $\rho_o=\theta_{o,\eta}$，在新角 $\psi$ 处记 $\rho_n=\theta_{n,\psi}$。由隐式微分：

$$
\eta_\psi=\frac{\rho_n}{\rho_o},\qquad
\eta_s=\frac{\theta_{n,s}-\theta_{o,s}}{\rho_o},
$$

$$
\eta_{\psi\psi}
=\frac{\rho_{n,\psi}-\rho_{o,\eta}\eta_\psi^2}{\rho_o},
$$

$$
\eta_{s\psi}
=\frac{\rho_{n,s}-\rho_{o,s}\eta_\psi
-\rho_{o,\eta}\eta_s\eta_\psi}{\rho_o},
$$

$$
\eta_{ss}
=\frac{\theta_{n,ss}-\theta_{o,ss}
-2\rho_{o,s}\eta_s-\rho_{o,\eta}\eta_s^2}{\rho_o}.
$$

于是 $\widetilde F(s,\psi)=F_{\rm old}(s,\eta(s,\psi))$ 满足

$$
\widetilde F_s=F_{o,s}+F_{o,\eta}\eta_s,\quad
\widetilde F_\psi=F_{o,\eta}\eta_\psi,
$$

$$
\widetilde F_{ss}=F_{o,ss}+2F_{o,s\eta}\eta_s
+F_{o,\eta\eta}\eta_s^2+F_{o,\eta}\eta_{ss},
$$

$$
\widetilde F_{\psi\psi}=F_{o,\eta\eta}\eta_\psi^2+F_{o,\eta}\eta_{\psi\psi},
$$

$$
\widetilde F_{s\psi}=F_{o,s\eta}\eta_\psi
+F_{o,\eta\eta}\eta_s\eta_\psi+F_{o,\eta}\eta_{s\psi}.
$$

这些是实际保存曲线的导数。转换器使用旧保存 PPoly 的一、二阶导数，不把原 RHS 的速度直接替换保存曲线的导数。单独高度均值按旧源的 antiderivative 定义以指定角求积和逐 span 六点 Gauss 积分重建；该数值求积没有区间证书，参数在记录中明确保存。

## 3. 不能遗失的竖直均值

旧表示中的非零高度 Fourier 模在 $\eta$ 上平均为零，但拉回到 $\psi$ 后通常不再如此。新参考图没有竖直分量，因此必须定义

$$
H_{\rm new}(s)=\frac1{2\pi}\int_0^{2\pi}\widetilde F_z(s,\psi)\,d\psi,
\qquad \Delta H=H_{\rm new}-H_{\rm old}.
$$

同样记录

$$
H'_{\rm new}=\operatorname{mean}_\psi\widetilde F_{s,z},\qquad
H''_{\rm new}=\operatorname{mean}_\psi\widetilde F_{ss,z},
$$

以及 $\Delta H'$、$\Delta H''$。固定新角下的 Fourier 投影与 $s$ 微分交换，所以保存的 state、state 一、二阶 jet 正好是同一投影规则作用在上述拉回导数上。

输出 NPZ 包含：

- `s,y,ys,yss`：新参考下的投影扰动及径向两 jet；
- `height_original,height_original_s,height_original_ss`；
- `height_correction,height_correction_s,height_correction_ss`；
- `height_new,height_new_s,height_new_ss`。

新完整图由新参考、`y` 和 `height_new` 重建。只保留旧 $H$ 会制造一个随 $s$ 变化的竖直平移，通常改变度量和像，不能仍称同一图。

## 4. 已实际运行的两类输入

### 旧单余弦图到一般图

输入 `numerical-m2-v55v60-m16-q20.json.gz`，取该 checkpoint 的完整实际核心作为新参考，升到 M24；角求积 1024，径向 81 点加所有物理断点，高度角求积 256。

输出 `geometric-old-m16-to-general-m24-warm.npz/.json`，数据约 159 KB。采样重构误差：

| 项 | 最大误差 |
|---|---:|
| 位置 | $2.682\times10^{-11}$ |
| 径向一阶 | $1.200\times10^{-9}$ |
| 径向二阶 | $3.418\times10^{-7}$ |
| 角向一阶 | $1.374\times10^{-9}$ |
| 角向二阶 | $7.049\times10^{-8}$ |
| 混合二阶 | $6.092\times10^{-8}$ |

高度均值修正及一、二阶导数最大值分别约为

$$
0.00678596,\qquad0.03111265,\qquad0.27065458.
$$

它们远大于投影位置误差，实际说明均值问题不可忽略。新入口扰动最大约 $4.45\times10^{-8}$；旧有限图本来只是核心的近似，所以同图转换不能强行将它设零。

### 新一般图到更大振幅参考

输入已成功的 `root-dual-q006-m8.json.gz`，把数值参考改成 q=.012 的两模参考并升 M12。**旧物理曲线本身仍是 q=.006 的那一条**；转换后入口扰动不为零，之后为 q=.012 的 BVP 重设入口会是另外一次真实初猜变形。

输出 `geometric-dual-q006-to-q012-m12-warm.npz/.json`，数据约 110 KB。位置投影误差约 $3.11\times10^{-13}$，径向二阶约 $3.30\times10^{-11}$。高度修正及两 jet 约为

$$
1.2502\times10^{-5},\quad5.8153\times10^{-5},\quad6.6220\times10^{-4}.
$$

新入口 state 最大约 $.499419$，正是“换参考但仍保留旧物理核心”的结果，不是转换失败。

## 5. root 的 restart 接口

可直接 import 后调用 `load_saved(...)` 与 `convert(saved,new_chart,M,q,s,...)`，或使用命令行生成 NPZ。

```bash
python computations/geometric-checkpoint-core-pullback.py \
  --source-topic /workspace/scratch/78718bd0c4a9/math-research/topics/visible-flexible-closed-surface \
  --checkpoint notes/root-dual-q006-m8.json.gz \
  --port computations/numerical-m2-port24.json \
  --amplitude .012 --modes 12 --gauge .012 \
  --out-prefix notes/geometric-dual-q006-to-q012-m12-warm
```

对升 M 且同物理核心的转换，用 `--use-old-core`；也可用 `--core-json` 读取本文其他生成器的支撑系数。当前只实现 base_mode=2 或 3 的已知源适配，拒绝未知 metadata，避免猜测坐标含义。

root 可在新 BVP 的数值径向网格上插值 state；若随后强制新的核心边界或更换 profile，须在输出中标明那是 warm 初猜修改。这里没有做 nonlinear tail DN、闭合或任何新的径向求解。
