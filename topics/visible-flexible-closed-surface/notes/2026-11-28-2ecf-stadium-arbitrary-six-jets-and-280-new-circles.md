# 较宽 p32 场的任意点实际六 jet 与 280 条新材料圈

以[真实长母线后的全空间场](2026-11-28-2ecf-stadium-longer-proven-coast-full-field.md)及[十次 500 维径角峰值修正](2026-11-28-2ecf-stadium-broad-active-peak-position.md)为输入。这个求值器在从中央到原 R205 外端接合点的任意张量积 $(x,u)$ 上返还当前物理 $s$ 导数的 $P,X_s,X_u,X_{ss},X_{su},X_{uu}$ 和当前 $f,f_s,f_{ss}$。

按真实执行顺序，它求原 HF/W 与两个材料钟，叠加原 6615、14820 舒展空间和上一 p8 的谱位置修正，变换到第一张新 $s$ 坐标。从 p32 准确端口与原端口的 $P,V,A$ 差施加实际选定的 .52 紧 Hermite 接合，再加入 p32 的位置修正、七个 guide 修正和真实 held 投影。正的两因子在逐点的完整链式下改变 $s,f$，然后叠加重设度量的第三态，作第二次 .014 材料延长、真实 Γ95 延长和实际 .06 宽接合。最后加 13455 维真实背景及指定历史谱修正。完整外端之前保留所有原非对称谱，最后的 500 维增量自身满足 Rz(π) 半周协变。实际原 R205 开发尾与闭帽仍按旧完整模型链接，新增任意点算子不覆盖其外侧。

原有三组各抽 35、35、36 个真径点，所抽角和径点编号存于回执，含新接缝两旁。
| 原组 | 位置最大差 | $X_s$ 最大差 | 六 jet 最大分量差 |
|---|---:|---:|---:|
| training | 1.443e-15 | 2.232e-14 | 1.243e-12 |
| observer | 2.22e-15 | 3.819e-14 | 2.476e-12 |
| independent | 6.439e-15 | 1.383e-13 | 9.954e-12 |

逐组 $f,f_s,f_{ss}$ 对照之最大差恰为零。另一组是新增的实际观察：对全部活动支撑结点跨度，在 $(j+.271)/4$ 四处分点，取全圈 320 个均匀角。280 条径圈均与原 G10、G11 相距 $10^{-13}$ 以上，共 89600 个实际物理点；原有 G10/G11 未用于训练这个模型评估器。

| 新圈的 metric | 新圈的绝对主曲率 | 新圈的 held |
|---:|---:|---:|
| .09821806706 | 11.72972433 | .64877277460 |

真正曲率极值在 $s=.22195025150,u=1.11919238284$，距新锁端 $b'=.21954147176$ 约 .002409。该真实有限峰高于旧 G11 的 11.55964 和 G10 的 11.56160。额外的 metric 峰在 $s=.81530186891,u=3.61283155163$。新有限网格不证明全域上界。

沿用前引 p32 场所列 `hfargs`、`stadium_args`。

```bash
parents=(--fixed-stadium stadium-p32-new018-full-03.json --prior-guide stadium-p32-geo015-03.json --projected stadium-p32-smooth-support-hold.json --redesigned-state stadium-p32-admissible-redesign-03.json --background stadium-p32-extend040-03.json --radius-spec stadium-p32-new018-full-source.json --design-spec stadium-p32-admissible-redesign-redesigned.json --longer-spec stadium-p32-extend040-longer.json --extra-state stadium-p32-minimax-b-ex10.json)
python "$SCRIPTS/2ecf-strong-stadium-arbitrary-physical-suffix.py" "${hfargs[@]}" "${stadium_args[@]}" "${parents[@]}" --prefix stadium-p32-arbitrary-m8
python "$SCRIPTS/2ecf-strong-stadium-fresh-suffix-grid.py" "${hfargs[@]}" "${stadium_args[@]}" "${parents[@]}" --prefix stadium-p32-new-rings-m8
```

任意点原回归和新实际圈的 JSON 身份分别为 `da3a522f49227f4607f0b336162427a44c05b50096e235a903e2662e65b140d1`、`17f5edde312f15367c2b8ea5eb17ce49b7a8ed276c151ed8a092eb3e8c6d63c1`。物理最终误差仍须全域证书。
