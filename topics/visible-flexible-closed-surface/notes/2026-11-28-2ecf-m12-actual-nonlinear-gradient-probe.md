# M12：在原独立 observer 中记录实际新场的 nonlinear JT r

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

H2 直接步已有的 physical normal 是 `J_oldᵀ(r_old+J_old d)`，不能把它改名为更新后实际场的 nonlinear stationarity。新入口 `2ecf-m12-h2-disk-normal-cached-lm-v2.py` 只扩充已有被动观察：在原 observer 已经得到的实际 Xs/Xt/bb 和完整三 Gram residual 上，按原权重、原 radial block 和原 Cartesian angular_adjoint 计算 `J_currentᵀ r_current`。

计算仍按原运算顺序先把 residual 乘 weight，再乘 weight；不以另一种代数等价归并冒充原 floating bytes。它不再求源、不增加或删除原能量行，不改变场、g、候选步、lambda、线搜索或 H2 上限。报告原独立点集上 before/after 的实际 nonlinear gradient 范数、最大分量、系数字节身份和 gradient 字节 SHA。原径向峰诊断照常保留。

同一个非零 C2 核（121 列、2304 行、8 个物理元素、2 个内三重结点）实际自然 exit 0，用原 StreamingLinearized 与原物理 JT 对照：全部 observer statistics 完全相同；实际 JT r 的字节 SHA 完全相同；8 个元素均已观察。该核 actual nonlinear gradient 范数为 0.5630060419676556，耗时 1.638153024 秒。它是有限接口一致性核，不是整片 M12 返回。

这项是诊断，没有增设完成门槛。README 第5项沿用已有 `2026-11-10-78718-fixed-g-refinement-composition.md` 的主求解容差 B=2e−9 和固定 g 加密规则，不把任何新 stationarity 阈值冒作额外完成条件。时间仍依赖既有解析覆盖，不添加伪时间积分。

现行 M48/G12 与 M64/G12 入口已冻结且未变；新入口只供明确声明的后继实际 h 或 lambda 步使用。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-nonlinear-gradient-c2-fixture.py --scripts scripts --out /tmp/m12-nonlinear-gradient-fixture.json
```

- `2ecf-m12-h2-disk-normal-cached-lm-v2.py` SHA256 `5d6dbfbcc3b585db57589947ad7d86376c4fa5918e3d0f04405da9015dea1114`。
- `2ecf-m12-nonlinear-gradient-c2-fixture.py` SHA256 `5aa663b67e9ef54f6a98a2cde038e8e5e44eead811886be165dab8a8d4334a58`。
- `nonlinear-gradient-c2-fixture.json` SHA256 `e6e975573cc798b7181849469ae750093159fdb053a79423053491cc3e736bc2`。
