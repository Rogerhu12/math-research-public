# 实际 raw M8 控制在圆弧端点的两种宽度初值

维护：Astra-held10-7322d0de-20261118。**数值设计诊断**。输入为已求出的 raw `lambda=.02`、`q=.04`、M8 有限真联合态；该态的完整 metric 仍为约 `8.30e-5`，未通过本题门。本次只构造新的核心初值，不求解前缀或尾。

## 新问题与完整控制

此前 raw 宽度扫描固定的是旧 cosine 锚点的七个控制。这次使用实际 raw 联立态的全部七个物理系数，即 checkpoint 的 `parameters[1:]*central_correction_scales`，没有截掉末槽或沿用旧数值。保持 `q=.04`、`a=.21`、主圆化过渡 `b=.08`，把 `lambda` 明确改为 1，并分别设置控制过渡宽度 `.16` 与 `.4`。

控制仍是 `W(cos(3j phi)-低2×2投影)`，`j=2,...,8`，均值与主频为零，保护弧上全部控制及其二阶导为零。自由第一槽是物理 `cos(6 phi)`；底层通用类的旧 n4 描述标签不改变此频率。

| 端点控制宽度 | 原完整 rho guard 下界 | 完整 rho 采样最小值 | 完整控制 `b+b''` 采样峰 | 数值插值上估计 | 完整位置半径采样最大值 |
|---|---:|---:|---:|---:|---:|
| .16 | .6239086610189567 | .6626955930436814 | .10110606329501737 | .10110644951513233 | 1.0418478005823202 |
| .4 | .6501614920346478 | .6635509398438194 | .01471975960362743 | .01471978128453769 | 1.0418140372503613 |

两行均以原 512 点起步的完整正性门通过，阈值仍为 `rho>1e-5`，没有更改 guard。完整一周期诊断取 32768 点。保护弧上 `rho-(1+8q)` 的 1025 点采样峰均为 0；这里的精确圆弧来自 `lambda=1` 的积分定义，采样不是其证明。

记录中的 `support_condition` 是高频矩 Schur 矩阵的条件数，不是 raw 定义实际使用的低 2×2 投影矩阵；两者均不证明 BVP Jacobian 可逆。

数值插值上估计使用周期网格上 `max|b+b''|` 加

$$
\frac{h^2}{8}\sum_j |c_j|\,\|(B_j+B_j'')''\|_\infty
$$

以及原代码风格的系数误差与函数求值 allowance。导数系数界来自已登记的有理矩包络；三角函数的浮点求值仍使用数值 allowance。因此该列不是新发布的严格区间几何证书，也不直接支付 R32 的所有充分条件。两行的 q 都是 `.04`，不同于 R32 的 `.0849–.0851` 幅值窗。

## 对下一实际求解的作用

实际 raw M8 控制也呈现 `.4` 宽度下较小的完整曲率扰动，故该方向不只对旧 cosine 系数有效。改变 lambda 或控制宽度都是新的物理设计；本记录不把它算作同 g 精化，不推断联立后控制仍具有表中的大小。

正在运行的固定 `lambda=.02`、固定整 g 的 M16 真联合保持原参数。取得其完整终态后，要以它实际求出的全部控制重复本入口检查，再选择明确的 `lambda=1` 设计。R35 已说明，单独增大 `lambda<1` 不能代替真实保护弧缺陷检查。

## 复现与哈希

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/screen_raw_endpoint_from_checkpoint.py \
  --checkpoint /workspace/scratch/7322d0dee069/m3_work/beta4625-q040-raw-lam002/seed.json.gz \
  --control-transition .16 --control-transition .4 --homotopy 1 \
  --out /workspace/scratch/7322d0dee069/m3_work/raw-m8-endpoint-core-probe.json
```

- 实际输入 checkpoint SHA-256：`67bf84c2f485e500b92378dec67e2186ee0a874ab2f8d763a2a0855edc263607`。
- 新脚本 `scripts/resume_m3/screen_raw_endpoint_from_checkpoint.py` SHA-256：`8133e66018d2abe984681d22be4f6653106e58f1aeeae6b5c217ea1de2072b8b`。
- 发布的紧凑标量/设置记录 `scripts/resume_m3/raw_m8_endpoint_core_probe_record.json` SHA-256：`1274637ae8de448e13a597c7e434d9d6f7428146f44988845d8b9a3e54d8689f`。原执行记录 SHA-256 为 `b0851691494cebede16cf37d9f7bb688a55924134a597db79497f93a49c02a7d`；可再生逐导数/矩表已去掉并保留证书哈希，全部实际物理控制、输入 profile 和源文件哈希保留。

运行没有输出新的场数组或网格；可重算输入 checkpoint 不入 Git。
