# 相位图的有限 Schur 方向与 M24→M32 的 C² 检查

状态：**浮点诊断；未证明精确等距族、无穷频率收敛或统一右逆。**

基准始终是已保存
`data/fourfold_phase_m24n201_q256_checkpoint.npz`，
SHA256 `63b5513befcf44ce907b047dbeb41a7e143431211d20e3cbb103a081cbef0a0e`。
它的真实表示、原函数预算与误差口径见 `2026-11-12-unit-tangent-newton.md`。

## 1. 保持实际相位振幅的 Schur 方向

`scripts/fourfold_schur_directions.py` 可识别旧位置图和新 R33 相位图。
在当前相位图，固定保存的 `radius_shift`，并保持
$\delta\beta_4(0)=0$。对每一个规定的 unit-mean 列，先求非均值控制点
的正规方程补正，再用原实际 Jacobian 重新计算剩余量。
径向每单元3点 Gauss、Q256；列归一化正规矩阵的 Tikhonov 参数1e-10。

所报 L2 是有限 Gauss 加权残差向量的 Euclidean 范数。
没有施加 mean 高度、直径、action 或真实返回数约束。

| 规定的 mean 列 | 裸列加权范数 | 补正后加权范数 |
| --- | ---: | ---: |
| 0 | .03927965407525 | .008265809275666 |
| 1 | .6992876134602 | .1328430121543 |
| 2 | .3738583905999 | .07569873523478 |

三个补正列的实际剩余 $J\delta$ 的 Gram 谱为

\[
(1.85565097\cdot10^{-11},\quad3.24127033\cdot10^{-6},\quad.0234426467).
\]

最软 mean 组合约
`(-.994734076190,.003528309200,.102428847011)`。
这些数据说明需要讨论兼容组合；三个单列都没有消尽线性 PDE 残差。
正规方程内残差约3.69e-15，振幅约束误差小于9e-19，Robin 变分残差
小于5.21e-15。线性代数精度不等于连续方程精度。

相位变分必须使用真实公式

\[
\delta F=\delta a\,\mathcal P T+a\,\mathcal P(\delta T)+\delta Z e_z,
\]

其中 $\delta T=T_\beta\delta\beta+T_\gamma\delta\gamma$。
旧位置图的加法字段 $\delta a\,e_r+\delta Z e_z$ 不适用于此图。
脚本的旧 `linear_candidate` 已显式拒绝 phase 输入，以防错误迁移。
这些完整方向已交给同一图的实际转折/返回图评价器使用。

保存文件：

- `data/fourfold_phase_m24n201_schur_directions.npz`，306617 bytes，
  SHA256 `2c6e5eb5c17578baf08f43a3d6b39e1699b5fd7dd0c17aae02047f0ba2fd158a`。
- 同名 JSON 保存范数、Gram、参数、源检查点和脚本哈希。
- `directions` 的每行是一个完整 phase 控制点/mean 变分；
  `candidate_vector` 是同一基准图，不能换到另一个候选上解释。

重做命令：

```bash
mkdir -p /tmp/visible-exact-schur
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_schur_directions.py \
  topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
  --regularization 1e-10 \
  --cache /tmp/visible-exact-schur/phase-directions.npz \
  --out /tmp/visible-exact-schur/phase-directions.json
```

旧位置图的重做入口是同一个脚本，将输入改为
`data/fourfold_overcollocation_m16n151_graded_checkpoint.npz` 即可。
新带状算法对旧图的回归与原稀疏 LU 的变分控制点最大差5.14e-12，
三个实际剩余范数一致至所列数字。

## 2. 已保全的 M32 三步状态

在相同201径向控制点、Q256下从基准图升M32；采用带状+三mean Schur
求解，初始正规化1e-6。三次接受后代价6.19159417e-12；随后进程
exit137，未得到正常结束报告。逐改善 checkpoint 保全了这三步。
当前没有认定这次内存退出的具体原因，也没有继续盲目扩大维数。

保存为 `data/fourfold_phase_m32n201_interrupted_checkpoint.npz`，
121860 bytes，SHA256
`20081f6a7118ee8d5c266e20adf8bd75e1ede37c1ad65644eeb735439a8ed315`。
同名 JSON 含事后同一实际有限原函数的完整二jet检查。

| 实际样本量，1798径向点、Q256 | M32 三步状态 |
| --- | ---: |
| 完整相对非均值 metric 算子范数 | 2.4141687660040725e-5 |
| 两倍最大模长（直径代理） | 2.578898062530205 |
| 腰圈径向差 | .13284432932547197 |
| 腰差/直径代理 | .05151205131199948 |
| 最大绝对主曲率 | 7.769410559515704 |
| 腰圈 $N$ 范围 | [-9.019972,-.500906] |
| 腰圈 $\det II$ 范围 | [-1.602197,-.986443] |

腰圈 $\beta_{100}\approx6.06\cdot10^{-4}$、
$\beta_{128}\approx2.92\cdot10^{-4}$，新增相位块还不能忽略。
最高已表示相位之外的第132模 metric 系数约1.89e-6。

## 3. 同一核心上的 C² 差没有变小

使用 `scripts/fourfold_phase_compare.py`，在共同区间 $[0,.6]$、
601个均匀径向点并入两图 Greville 点、Q512角点上，对同一有限
原函数的实际导数逐点比较。下面是坐标二jet差的 Euclidean 范数
最大样本，不是连续 C² 范数上界。

| 量 | M32−M24 完整变化 | 冻结 mean 后的变化 | 单独新增25–32相位块 |
| --- | ---: | ---: | ---: |
| $F$ | 3.21318e-4 | 2.88728e-4 | 2.75888e-5 |
| $F_x$ | .00860954 | .00861298 | .000997352 |
| $F_\theta$ | .0107243 | .0107235 | .00281525 |
| $F_{xx}$ | .622772 | .623131 | .119578 |
| $F_{x\theta}$ | .460736 | .460726 | .109116 |
| $F_{\theta\theta}$ | .861741 | .861066 | .316920 |

mean 的变化仅为
`(.001101785704,-8.932736283e-6,-7.172368019e-5)`；
它单独造成的 $F_{xx}$ 差约.00627、$F_{\theta\theta}$ 差约.000675。
因此上述大二阶差主要来自非均值相位重新调整。旧1–24模也在改变：
单个共同 $\beta$ 系数的值/一阶/二阶最大变化分别约
`.002384,.11363,7.9335`。这不是仅添加一个可忽略尾项的过程。

有限 M32 的 metric 样本改善不能推出这个序列在 C² 中收敛。
表中“新增相位块”也是有限差，不能用它估计未知的所有后续模。
当前应先处理同一实际图的返回数、参数兼容和高模近共振，再判断
如何继续角截断或振幅延拓。固定原 mean 作用量不能替代实际非径向
返回数条件。

完整比较与各峰位置保存在
`data/fourfold_phase_m24_to_m32_comparison.json`。重做：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_compare.py \
  topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
  topics/visible-flex-exact-nearby/data/fourfold_phase_m32n201_interrupted_checkpoint.npz \
  --core .6 --samples 601 --angles 512 \
  --out /tmp/visible-exact-schur/phase-c2-comparison.json
```

两个原始向量、完整均值半径偏移及原函数表示均已保存，
不需要把未完成的大计算末态当成一个不可恢复的黑箱。
