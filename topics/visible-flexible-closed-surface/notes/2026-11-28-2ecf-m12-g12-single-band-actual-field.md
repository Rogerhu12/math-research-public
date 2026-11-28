# M12：同一 G12 输入的单 band 重试已真实返回新场

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

此前旧入口 G12 在 612.993204925 秒被系统 SIGKILL，未返回场；实际 exit −9 已单列记录，没有称为数学失败，也没有冒称已证明 OOM。本次保留完全相同的原 Q-free source、g、参数、时间范围、grid、G12/G14 查询和暖输入场，改用已经实际核过的单 band 完整 Gram 入口。

## 实际输入与输出

真实暖父态是已保存的 M48/G6 `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`；新暖传递场字节完全相同。空间仍为 487 个 unique 物理元素、736×146=107456 个未知数、M48；只把训练径向积分 G6 → G12，独立 G8 → G14，角节点仍 N768/N1536。本次不是物理 h 加密。

真实新场 SHA256 为 `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`。lambda=1e−13，alpha=1 接受；原全部三 Gram 行、交叉 Fourier 通道和 H2 增量形式保留。

| 同一新点集上的实际对照 | 输入场 | 新场 |
|---|---:|---:|
| 训练 G12/N768 metric peak | 6.072532458837339e−10 | 5.376994763128501e−10 |
| 训练 weighted energy | 2.910730627956304e−21 | 2.806831384319289e−21 |
| 独立 G14/N1536 metric peak | 6.072528479124516e−10 | 5.438487573019811e−10 |
| 独立 weighted energy | 2.915079672947255e−21 | 2.8103873339483024e−21 |

独立峰位于 common q≈2.1209015697815095。原线性步的未正则 physical normal 相对量为 0.002214891676121542，正则 normal 相对量为 1.0098574040912444e−10；二者仍明确区别于新场的 nonlinear JT r。这些 normal 诊断不另立 README 完成门槛，主求解容差沿用已登记 B=2e−9。

## 真实内存与终态

完整 LM 自然 exit 0，1288.072795462 秒；其子进程峰 RSS 1,563,640 KiB（约 1.49 GiB）。完整 Gram band 是 753,051,648 bytes，H2 Cholesky 原位返回同地址，实际 factor 时间 2.883404833 秒。释放 band 与原物理 J 数组后，进入独立观察时 RSS 为 239,076 KiB。这是真实进程观测，不是静态数组估计。

R226 紧随同场自然 exit 0，8.101823501 秒；两端完整 correction 二 jet 仍为零。旧全局 geometry 消费者自然 0。写本条时旧 R236、microspan 与全部 ancestor union 尚在后继流水线上；不把这些未返回阶段冒为已完成。root 与 exact 消费者已收到本场准确身份，新的全域相关 Gram / 全时 reach 后验必须逐场支付，不能借用 M48/G6 或更早的证书。

有限独立峰低于 B 本身还不是 README 第5项的完整全域终值证明。现行 M64/G12 是从同一真实 M48/G6 父态独立启动的新角空间支；不是把本次 G12 场伪记为它的父态。后续真实物理 h 会使用实际诊断与同 g 后验继续。

## 可重生命令

先按同日 G12/G14 exact-query-extension 记录重生 grid / 13185 原 source 查询及 original-source-bounds，然后从已有 M48/G6 父场执行原 `6a65-m12-exact-radial-angular-warm-transfer.py` 到该 G12 grid。本次 LM 入口为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-h2-inplace-cached-lm.py --scripts scripts --data <M12-prefix-data> --grid <G12-grid> --query-report <G12-query-report> --query-cache <G12-query-cache> --transfer-receipt <actual-transfer.json> --initial-field <actual-transfer.json.field.npz> --initial-result <actual-M48-G6-result.json> --out <fresh-result.json> --lambda-step 1e-13 --steps 1 --hessian-step-cap .05
```

其默认 block=24、normal assembly block=8、独立角倍数=2 和全部其它参数与被中断输入相同。新私有 source packet cache 从准确原源重新生成，没有复用只有事后 SHA 的旧残包。

## 实际文件身份

- `h2-c2-m48-g12-04r1/result.json` SHA256 `ec5a051715e9609c07082924c7872dd3eec0e183bdc660139f452108644b1e57`。
- `h2-c2-m48-g12-04r1/result.json.field.npz` SHA256 `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`。
- `h2-c2-m48-g12-04r1/correction-bounds.json` SHA256 `d72e798d220014dbb553c4a54e06cf478a5f3be5154eacf78f67d2ffec2212a2`。
- `h2-c2-m48-g12-04/grid.json` SHA256 `94a48337aedccd79810e02928bbe920334440d14df1eb68435c7a252969c07f0`。
- `h2-c2-m48-g12-04/exact-tail-queries.json` SHA256 `1a222405e67641f5968c3bca36d50e372356ddc9508aeaf25e2267e51b0a698d`。
- `h2-c2-m48-g12-04/exact-tail-queries.json.npz` SHA256 `8c95cfeb3c5ebd186cf299d449d0835d718900c947669a8a862de6d68ff4eacf`。
- `h2-c2-m48-g12-04/original-source-bounds.json` SHA256 `e662014b75ada38faa10d34dcc425ab0275e0b7b660be29ed7f7eb236522cbc1`。
- `h2-c2-m48-g12-04/warm-transfer.json` SHA256 `f9983f25bea4404280473f3badeee548c11877ec8a3833bc8a67b6ee6075aece`。

## 后继阶段真实完成补记

同一 `5778bee4…bf5a5b8` 场的重试流水线现已全部 6 阶段自然 exit 0，`execution.json.finished=true`。

旧 R236 完整核自然 0，613.529267209 秒；连续 differential Frobenius 上界 2.4783049708267734e−5，旧无 source 抵消的 triangle 上界 4.959243609098787e−5。它没有通过 1e−6，后续新的相关 Gram 证明仍须按此实际场单独完成。

两个旧 microspan 窗口共 546 点 / N1536 自然 0，31.262303407 秒；同场峰 5.438488059979774e−10，在 r≈0.5134652116092632635、原 source span17479、当前元素187、角索引1157。两个窗口之间的空档没有冒为已观察。

真 parent/child ancestor union 对另外 3912 个旧半径仍分别使用实际暖输入与实际新场，角节点 N1536；自然 0，246.693804328 秒。当前 G14 的 6818 点连同这3912点共10730个独立半径，覆盖全部既有祖先观察；before-union峰6.072530818126161e−10，after-union峰5.438487573019811e−10。这里没有把额外旧点的 source-zero 值混入暖输入 before，也没有把 union 当作新积分规则。

- `metric-budget.json` SHA256 `51481bedd248c4b1ede5e25439e63f0fc8f4be8461c436a95fa2d2057d47a618`。
- `microspan-observer.json` SHA256 `2d4650f7bf8a40ea5a30d4dc43889d5b3b4b786330c4cad6661137d2f161f915`。
- `ancestor-observer-union.json` SHA256 `b45fd64e39eaefefda8dad9b9c30530bc2858439e4b413160fdaa019df372bf2`。
- `execution.json` SHA256 `3f548167459e266d12f5ebd73765aabb1a0c6f39d8fe06f23722599e03bc3c75`。
