# 新单核心候选的参数方向诊断

状态：**普通浮点、有限体与有限加权线性系统的探索**。

本记录只使用 `data/phase_ring_continuation/type_fixed_step02.npz`
（SHA256 `05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883`）
与其同图 Schur 三列（SHA256
`941c19642b4e74cbe5d68c311629bbe66f05df16fca26692c541ed61d6f29629`）。
这不是先前 canonical phase24；旧图的外负环与旧参数导数不迁用。

## 1. 最软方向仍主要包含尺度变化

在已补正非均值的三列中，实际 $J\delta$ Gram 最小特征值约
7.58325e-12，对应单位 mean 组合
`(-.99480722,.00368043,.10171062)`。
用真实相位表示的变分
$V=\delta a\,P(T)+aP(\delta T)+\delta Z e_z$，逐径向点作最优
角向 $L^2$ 投影 $V=\xi F_x+V_\perp$，并在同一区间再拟合一个
常数缩放 $\lambda F$。分母是该方向自身的 $dx\,d\theta$ 向量
$L^2$ 范数，没有把几何度量权混入范数定义。

| 区间 | 仅径向重参的相对余量 | 加一个常数缩放后的相对余量 | 拟合缩放系数 |
| --- | ---: | ---: | ---: |
| $[0,.25]$ | .908172 | .0220058 | −.0967198 |
| $[0,.35]$ | .859265 | .0333615 | −.0953211 |
| $[0,3]$ | .978342 | .254375 | −.1989091 |

因此最软列仍不能解释成纯径向重参数。在内部窗口中，它接近缩放与
径向重参的组合，但仍不是精确对称方向。以 $[0,.35]$ 为例，实际
法向分量最大样本.112944，$|\delta E/E|$ 最大.380168，
$|\delta a/a|$ 最大.0990310。

必须继续保持以下区分：同步改变输出轴对称度规时，缩放和径向重参
可能不改变主特征返回；固定同一目标度规的齐次线性核还要求
$\delta E=\delta a=0$。这个最软方向不满足后一个必要条件，
也不能单凭有限矩阵小特征值授予非零返回 twist。

中间 Schur 方向在 $[0,.25]$ 上去掉缩放与径向重参后相对余量
.337946，主兼容方向则为.861210。它们的形变成分更大，但返回导数
仍须用此图的实际修正算子和同步参数度规直接计算。

## 2. 保存与重做

完整报告保存为
`data/phase_ring_continuation/type_fixed_step02_gauge_diagnostic.json`，
含输入哈希、源脚本哈希、六个 mean/Schur 组合在四个径向区间的
全部投影量。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_gauge_diagnostic.py \
  topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02.npz \
  topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
  --angles 256 --out /tmp/visible-exact-mean/type-fixed-gauge.json
```

这是只读诊断，没有产生新的 Newton 状态，也没有改变振幅、角频
数量、保存的 `radius_shift` 或两步校正候选。
