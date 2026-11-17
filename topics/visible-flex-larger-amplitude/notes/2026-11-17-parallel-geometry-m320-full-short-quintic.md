# M320 真短 IVP：N4096 重积分与全短段共同 quintic

日期：2026-11-17。维护：`parallel-geometry-amplification`。

**状态：明确的局部 C² 映射及数值证据。N4096 重积分后，全短段采样 Gram
约 `5.092e−7`，采样曲率约 `5.7993`。与旧 prefix 的 C² 接合仍未完成；
无完整尾、连续区间证书、全相位 reach 或完成标准声明。**

## 1. 实际重积分及节点两 jet

固定真 .995 M112 初值，零补到 M320；原 core 的 `rho`、inward scalar
不变，分别用 N2048、N4096 的完整有限 RHS 真积分到 .997。
参数为 DOP853，`rtol=1e−13`、`atol=1e−16`，显式首步和步长上限
`.000015625=.002/128`。两次均成功到达末点。

每个保留节点存储实际 state、该 N 下的完整 RHS，以及

\[
y''=D_yf(y,k)y'+D_kf(y,k)k',\quad
k=a'/a,\quad k'=a''/a-k^2.
\]

同一节点的 0/1/2 jets 供相邻胞共用，逐胞定义唯一五次 Hermite 多项式。
实际 `F_s,F_{ss}` 由这条多项式字面微分得到；不把 RHS 重新代入内点读数。
原切口 jets 单独保存供后续接合比较。

## 2. 必须保留的末端微胞发现

DOP853 的直接节点表含倒数时刻 `.9969999999999953`，再到真末时刻
`.997`，最后一胞只有约 `4.7e−15` 宽。若保留这 130 个节点直接构造
共同 quintic，实际插值图出现 Gram 约 `.0320865`、曲率约 `1.23e13`。
这是该插值构造本身的坏几何，不能靠忽略这个胞的读数消除。

本次明确采用**新的重建节点集**：只删除距末点小于 `64*ulp(end)` 的
倒数节点，保留真末点以及它的真实 0/1/2 jets，再由最后正常宽胞连接。
本次恰删除上面一个节点，剩 129 节点、128 胞；没有改变 IVP 积分。
删除政策、阈值和被删时刻均存入 raw。初版坏微胞 raw 也保留，
源的 `--keep-terminal-microcells` 选项可重现该构造及坏峰。

因此以下读数属于这条明确定义的新 C² quintic，而不是对初版读数做裁剪。

## 3. 全胞元字面几何

两种 RHS 角数都以 N8192、每胞 4 等分的同档读者检查全部 128 胞，
每份 5,242,880 点。参考 metric 使用同一原 core `rho` 和真正 scalar evaluator。

| 全短段采样指标 | RHS N2048 | RHS N4096 |
|---|---:|---:|
| 最大相对 Gram op | 5.09551535106e−7 | 5.09183166881e−7 |
| Gram 最坏 s | .997 | .997 |
| Gram 最坏角 | .434883553366 | .434883553366 |
| 最大主曲率绝对值 | 5.79927993277 | 5.79927993456 |
| 曲率最坏 s | .995 | .995 |
| 最小采样 Gram 行列式 | .037624780293 | .037624780293 |
| 最小采样 Frenet H | .000119898375 | .000119877959 |
| 最大点球范数 | 1.75450974982 | 1.75450974984 |
| 对原 core 见证的最小距离 | .962313759142 | .962313759142 |

Frenet 域量是 `Q=|F_φ|²`、`W=|F_φ×F_φφ|²`、`H=W−k²Q³`。
两份全胞采样的 Q、W、H 都正；表中 H 不表示帽高度或握持集合。
N4096 的 Gram 最坏点三项为
`rr=−3.71612e−9`、`cross=8.26279e−9`、`angular=−5.09048e−7`。

N4096 相对 N2048 是实际重新积分，未只在同一场上加密末点角样本。
两份末点系数的值、一阶、二阶最大差分别为
`4.53608e−12`、`2.44539e−8`、`.0001709573`；没有把它们写成相同的轨道。
这验证了本次局部候选对这一次 RHS 角加密的数值稳定性；不宣称无限维
收敛或全角/全径向连续认证。

## 4. 接旧 prefix 的条件仍未支付

原切口值由零补相同，但 N4096 新节点实际 jets 相对原 M112 的采样差为
`max|ΔF_s|=5.15602357915e−5`、`max|ΔF_ss|=.0202677715860`。
此处没有修改这些差量，没有完成 Hermite 接合，也没有把该短段作为
已接受的完整 BVP 父。新 raw 明确标 `bvp_accepted=false`、
`complete_prefix=false`、`old_prefix_C2_join_completed=false`。

## 5. 重现与冻结数据

新源：[`2026-11-17-parallel-geometry-short-ivp-field.py`](2026-11-17-parallel-geometry-short-ivp-field.py)。
SHA256：`ed0de0d513f28e1d227ba4f49a2ac2b2379107ca200c50f0d43f933e0edfd924`。
复用已冻结 `short-ivp-refine` 的有限 RHS 和标量定义。
reference / scalar 载体 SHA 仍为
`d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f` /
`11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327`。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  notes/2026-11-17-parallel-geometry-short-ivp-field.py \
  --reference "$SCRATCH/parallel-continue0995-m112.json.gz" \
  --metric "$SCRATCH/parallel-inward0997-m112.json.gz" \
  --output-stem "$SCRATCH/parallel-short-ivp-m320-cleanfield" \
  --modes 320 --angles 2048 4096 --read-angles 8192 \
  --radial-subdivisions 4 --end .997 --max-step .000015625 \
  --rtol 1e-13 --atol 1e-16
```

| scratch 数据 | SHA256 |
|---|---|
| 新 N2048 公共节点 jets | `59ee7b1adb42bd83028f05957bd1cafa4a43fcb40143d4caf2e5e447605052ae` |
| 新 N4096 公共节点 jets | `507cab03af49bf58305cd9e91421e2b91c0071cc4115dd8e1f6d1f047ad9389a` |
| 新完整读出报告 | `933101a71d7ea294480dc4b39aaa5ed77aa4f71e6bd7ff3e03b9de39a468b0f8` |
| 初版含微胞 N2048 jets | `4ff5cfa2744eee29169cadbab0d8432464c8d0843c0c69dfe9def270ec8b06c6` |
| 初版含微胞 N4096 jets | `7bc3fd931b8781f71a62bdde88819ba8f3736c93d3cd518c617fd99ced57a8a3` |

新 jets raw 含 `mesh/states/rhs/d2`、`old_cut_jets`、
`original_core_coefficients`、明确 scalar metadata 与所有输入身份。
raw 不入库。
