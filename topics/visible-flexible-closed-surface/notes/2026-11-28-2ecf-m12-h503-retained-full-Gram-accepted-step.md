# 同一原 g 上 h503 真实物理加密的全训练步

数值证据。原M64/G12的487个物理跨度中16个各在中点插入三重结点，得到503跨、784径向系数、194角通道和152096个未知数。原目标度量、同一时间解析族、全部物理Jacobian行与原G12/N1536训练规则继续使用。真实父场为 `3ca49d46da9c13392f93cd3a6f1dcc6a1cdc906731c4571adae7800405c93b54`，Boehm二进暖输入为 `ed281cfab427bef6f5cead3fc5e04218797da2e3756fac9955f150e4efdf5605`。同节点下实际原非线性目标以 λ=1e−13、α=1 接受一步。

| 6036个径向点、1536个角点 | 实际暖输入 | 实际接受步 |
|---|---:|---:|
| 全训练相对度量峰 | 5.424141904209173e−10 | 4.944025203556703e−10 |
| 全训练加权能量 | 2.138728330019075e−21 | 2.0712255458068243e−21 |

全部标量残差行悉数进入三个Gram项及其交叉通道（确数为 6036 × 1536 × 3 = 27,813,888）。增量的固定图表二阶筛查值0.01468808753259089，一阶2.19407535794512e−5，均为浮点筛查；对当前非线性场的独立物理梯度需待独立观察返回。旧Jacobian下未正则线性normal相对0.004786613563705107，正则后1.9743861820457904e−10。

首次运行在4104/6036处留下最后进度后被SIGKILL。此次保留全同几何/行列/权重和同一已登记的稀疏角求和方式。把1,416,317,952字节Fortran序唯一binary64带存为MAP_SHARED临时文件，在完整径向块间flush和MADV_DONTNEED；检查有限性、按既有对角因子缩放时使用连续列分块。LAPACK Cholesky仍实际核输入输出指针相同。此处未把与旧版不同浮点结合次序的完全Gram声称为逐字节相同。实际6036行完整累计进度565.068200704秒；打印该进度时全程RSS峰435408KiB。因子/缩放与求方向阶段合计84.703026274秒，接受后已释放单带和全部5个物理存储。

本条冻结时仅报告训练已接受，独立G14/N3072、11178点祖先并集、保存场、该场R226和连续几何/终值不在此条结论内。原G12/M48场5778的全域B=2e−9主证仍单独进行。

## 配方与原始身份

从[已返回的原13601点源和Boehm配方](2026-11-28-2ecf-m12-actual-m64-peak-h503-preparation.md)恢复全部原输入，随后在课题目录运行。将尖括号替为本机目录。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-refinement-execute.py --scripts scripts --data <M12-prefix-data> --old-grid <actual-M64-output>/grid.json --old-field <actual-M64-output>/result.json.field.npz --old-result <actual-M64-output>/result.json --old-correction-bounds <actual-M64-output>/correction-bounds.json --new-grid <h503-output>/grid.json --query-report <h503-output>/exact-tail-queries.json --query-cache <h503-output>/exact-tail-queries.json.npz --source-bounds <h503-output>/original-source-bounds.json --out-dir <fresh-h503-run> --solver-entry scripts/2ecf-m12-h2-mapped-disk-normal-cached-lm.py --lambda-step 1e-13 --steps 1 --hessian-step-cap .05 --block 24 --normal-assembly-block 8
```

- `2ecf-m12-complete-gram-mapped-assembly-only.py` SHA256 `0218724ed10857901e921026b9c031b535f3f594fc14e8e19311ba40f6f93ffd`。
- `2ecf-m12-h2-mapped-disk-normal-lm.py` SHA256 `90d4b7695d8afbee75d52e8a0a0b32fa1c92575f9f61620e67c65ba6c423f1c5`。
- `2ecf-m12-h2-c2-mapped-disk-normal-lm.py` SHA256 `5a80c9fd882e8d40a5ea66c03b8b9c8a5151328278ee879760dd3a8038ac002f`。
- `2ecf-m12-h2-mapped-disk-normal-cached-lm.py` SHA256 `81d6ac5e8ea02b4da6bab1317f218eb3fcc12061475268097143fa87c49956a0`。
- 原程序完整接受步单行（含尾LF）SHA256 `8ad0013ace0875e53e69bdfcaf244d13d52667b4063b2ee54e03ee9e9f264091`。整条管线仍在写日志。
