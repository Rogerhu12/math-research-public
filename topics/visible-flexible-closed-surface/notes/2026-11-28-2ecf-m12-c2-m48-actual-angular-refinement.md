# M12：C2 原源同态 M32 → M48 的真实角向加密返回

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。本条登记原 Q-free M12、同 g/参数/时间范围的实际非线性角向加密及所有既有观察点；不以正则方程解代替原问题收敛。

## 输入与空间

从已真实返回的 C2 M32 场 `201de8909dc707c7d91749d812585233d49120c076468e9f2aebe97271114aed` 暖启动。487 个 unique 物理元素、736 个径向自由系数和完整内三重 knot multiset 不变；真实角空间从 98 通道升到 146，未知数 72128 → 107456，训练角节点 384 → 768。原源、g 和原时间范围不变。原傅里叶系数逐通道嵌入，新通道为零，exact transfer 在二进制存储前准确；本次实际传递场 SHA 是 `b5a4ab4a115ae57ce7dcbb4ba5344199c64da3fb272108ddc0840e6802d5a33b`。

## 实际直接步

lambda=1e−13，H2 只罚增量，alpha=1 接受。新 N768 训练本身重新评估同一个输入场，不借 N384 的旧峰。

| 同点观察 | 实际输入场 | 实际新场 |
|---|---:|---:|
| 训练 G6/N768 metric peak | 8.053471336924477e−10 | 6.072529916228335e−10 |
| 训练 weighted energy | 4.296692300728237e−21 | 2.9062628724535783e−21 |
| 独立 G8/N1536 metric peak | 8.057573884765639e−10 | 6.072530818126161e−10 |
| 独立 weighted energy | 4.306355815385382e−21 | 2.9136597711256023e−21 |

原物理 unregularized normal 的相对值仍为 4.599815544135226e−5；正则 normal 的相对值 2.9858290638661076e−12。后者只说明这次 H2 步方程的线性解，不能替代前者或原非线性收敛。增量第二 jet 的浮点筛选界为 0.02127958755；本条不把筛选当严格 C2 几何证书。

完整求解真实自然 exit 0，1053.819668517 秒，进程自身峰 RSS 1985632 KiB。完整父 grid、source、query、basis identity 均由实际消费者核对。

## 所有既有观察与连续预算

两个原窗口共 546 个 microspan 点，角节点 N1536；新场峰 6.072513710005026e−10，在 r≈0.513405745757767 / 原源 span 17478。没有把两个不连续窗口之间的间隔冒作已观察区间。

祖先观察并集仍补齐缺失 16 个旧半径；全部点都使用同一新保存场。after union 峰 6.072530818126161e−10。旧消费者的 source-zero extra-point before 与 warm-field current-point before 混合结果已丢弃，本条不拿它作 before 比较。

R226 连续六 jet 已真实自然 0；旧 R236 的无抵消三角界仍为 4.212168822431749e−5，不能当作 1e−6 通过。新的同场完整 cross-Gram 与局部/区域二 jet 连续几何由独立 R252/R253 记录消费，不借用旧场证书；它们的完整回执与严格界见相应记录。

此条证明同一个原 g 的一次真实角空间加密降低独立误差；尚未满足 README 第5项的整条径向/角向收敛要求。G12/G14 是后继积分加密，不能把它称作物理 h 空间细化。

## 实际身份

- `grid.json` SHA256 `5f366284b435c8911fa1bddcc9bef4cc92c646f06730a959bd4c773b4c3cd7cd`。
- `warm-transfer.json` SHA256 `bc51f8498e4205da161e6f349c6fa2bf96135463d1e5cede3ec426791bfc2cce`。
- `result.json` SHA256 `c0ca3ce3832b12c188dca87218d87639cbe266c27c129323505ad1d12225b9c2`。
- `result.json.field.npz` SHA256 `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`。
- `correction-bounds.json` SHA256 `565a8a5b49e3352cbf09cb5f0bfed4cd0c37ea8348cc1299d46256979bd57d0d`。
- `metric-budget.json` SHA256 `8e0924c0e0cc52d926342adfb4547d717bfdbfb4982a3ecf8e031b63f2b2bc88`。
- `microspan-observer.json` SHA256 `42bf77d75e3f9076bfaf53559d9116b710dd4e9c789cf9e1317ba9311c1a20ec`。
- `ancestor-observer-union.json` SHA256 `bc71e0f26fe374d3a9bb565a0914614a2d999746e002a9f68652785a0f2e0cb2`。
- `execution.json` SHA256 `52d1892dc9d1b5e4eefd32d1e3ad12fb821df9da36a2b968a71b3eaf3effc1e5`。

7 个实际阶段（transfer、LM、R226、旧 geometry、R236、microspan、ancestor union）均自然 exit 0；`execution.json.finished=true`。所有大场/原始数组只留临时本地缓存；不进入 Git。

## 公开重生配方

S为本课题scripts目录，W为按先前已公开配方重生的m12-work目录，C2_GRID为真实 `h487-local-c2-grid.json`，O为一个新的M48输出目录。先保原G6、原query集合及全部物理knots，仅提高角阶：

```bash
python3 "$S/6a65-m12-frequency-only-grid-prepare.py" \
  --old-grid "$C2_GRID" --order 48 --angular 768 --out "$O/grid.json"
python3 "$S/6a65-m12-exact-radial-angular-warm-transfer.py" \
  --scripts "$S" \
  --old-field "$W/h2-c2-02/result.json.field.npz" \
  --old-grid "$C2_GRID" --old-result "$W/h2-c2-02/result.json" \
  --old-correction-bounds "$W/h2-c2-02/correction-bounds.json" \
  --new-grid "$O/grid.json" --out "$O/warm-transfer.json"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 "$S/2ecf-m12-h2-cached-direct-lm-v2.py" \
  --scripts "$S" --data "$W/m12-prefix-data.npz.gz" \
  --grid "$O/grid.json" \
  --query-report "$W/h487-base/entire-half-exact-tail-queries.json" \
  --query-cache "$W/h487-base/entire-half-exact-tail-queries.json.npz" \
  --transfer-receipt "$O/warm-transfer.json" \
  --initial-field "$O/warm-transfer.json.field.npz" \
  --initial-result "$W/h2-c2-02/result.json" \
  --lambda-step 1e-13 --steps 1 --hessian-step-cap .05 \
  --out "$O/result.json"
```

实际默认block=24、normal-assembly-block=8、gradient-tolerance=1e−8、独立角2倍。源query/cache和全source-bounds直接沿用h487-base，没有从G12后继源回借。之后原5个后验入口按下表执行；每一个都传本次真实field/grid/result，不能改旧结果标签。

| 后验 | 已公开入口与关键输入 |
|---|---|
| R226 | `6a65-m12-entire-half-continuous-correction-bounds.py`；原data、本次field/grid/result |
| 原全时几何 | `6a65-m12-entire-half-actual-field-geometry-transfer.py`；原h487 source-bounds、本次R226/field/grid/result |
| R236 | `6a65-m12-local-bernstein-angular-metric-budget.py`；原data、本次R226/field/grid/result |
| 两原微窗 | `2ecf-m12-declared-basis-observer.py --kind microspan`；原data/query/cache、本次field/grid/result |
| 全祖先并集 | `2ecf-m12-declared-basis-observer.py --kind ancestor`；同上，只消费同场after |

原弱几何/三角报告按原值保存；本次另付的完整cross-Gram与R249/R253及三时刻完整闭网格见[同场连续度量](2026-11-28-2ecf-m12-local-p-slope-cross-gram.md)和[同场全时几何](2026-11-28-2ecf-m12-m48-full-geometry-and-closed-meshes.md)。这些新证书不会回写旧后验字段。
