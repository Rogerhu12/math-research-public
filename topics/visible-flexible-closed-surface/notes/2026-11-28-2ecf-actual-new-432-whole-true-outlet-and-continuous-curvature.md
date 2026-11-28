# 真实出口、全部 128 个物理格与全核主曲率

**已证明。** [R297](../results/R297-actual-432-entire-true-core-continuous-principal-curvature.md) 将 432 个真实位置和完整 Bernstein–Fourier 底场按准确 Boehm 公共分片合成，对 10.41 I±II 的对角和行列式作全域向外包。127 个真多项式单元已覆盖，第 0 格另用准确 Gamma95 上 2048 个 native 角闭盒，经真入口弧长与出口特征线偏转计算 P,V,A 及角导和真实存储物理 FT140 的九项差，把每个带符号的 Hermite 权与其径导实际带入；首格 4096 完整角盒全通过。完整上下连接、R267 中央和真实平盘在全相位是浸入，处处 |κ|<10.41；完整 R293 帽亦有同一局部界。全局嵌入与 reach 不由此局部结果给出。
出口首试的脚本未向旧 Fourier API 显式传入箱阶数，因缺项而在首格前退出 1。正式有序调用使用中心12/闭盒10阶，完整原真实角域自然0。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-directed-full-polynomial-curvature.py" --scripts "$S" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --spatial polar-released40-genuine-floor-R293.json --start-cell 102 --end-cell 103 --output polar-R293-432-curvature-hottest-directed1.json
python3 -u "$S/2ecf-polar-released-directed-full-polynomial-curvature.py" --scripts "$S" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --spatial polar-released40-genuine-floor-R293.json --start-cell 1 --end-cell 102 --output polar-R293-432-curvature-interior-left.json
python3 -u "$S/2ecf-polar-released-directed-full-polynomial-curvature.py" --scripts "$S" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --spatial polar-released40-genuine-floor-R293.json --start-cell 103 --end-cell 128 --output polar-R293-432-curvature-interior-right.json
python3 -u "$S/2ecf-polar-released-directed-full-polynomial-curvature.py" --scripts "$S" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --spatial polar-released40-genuine-floor-R293.json --start-cell 94 --end-cell 97 --quarter-angles 4096 --radial-depth 7 --output polar-R293-432-curvature-three-fine.json
python3 -u "$S/2ecf-polar-released-accurate-gamma95-outlet-to-f140-ordered.py" --scripts "$S" --field polar-released-cut-flat40-enriched.npz --coast polar-new-gap-092-master-coast.npz --primitive polar-gap092-full-primitive.json --output polar-R293-432-true-Gamma95-F140-edge-ordered.json
python3 -u "$S/2ecf-polar-released-true-first-cell-curvature.py" --scripts "$S" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --spatial polar-released40-genuine-floor-R293.json --edge polar-R293-432-true-Gamma95-F140-edge-ordered.json --output polar-R293-432-directed-first-with-actual-edge.json
python3 -u "$S/2ecf-polar-released-432-complete-geometric-certificates.py" --mode curvature --field polar-released-cut-flat40-enriched.npz --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --cap-source "$S/2ecf-higher-bottom-cap-exact-budget.py" --prefix polar-gap092-entire-prefix-reach.json --output polar-R293-432-final-curvature.json --edge polar-R293-432-true-Gamma95-F140-edge-ordered.json --parts polar-R293-432-directed-first-with-actual-edge.json polar-R293-432-curvature-interior-left.json polar-R293-432-curvature-hottest-directed1.json polar-R293-432-curvature-interior-right.json polar-R293-432-curvature-three-fine.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-directed-full-polynomial-curvature.py | 1c56db323d9419eb1f6aeb11611fd8858add0991d9dfc39a31094dd0c341eff0 |
| 2ecf-polar-released-accurate-gamma95-outlet-to-f140-ordered.py | b5a1202290ae931341c8dcd758927c92c9ea666b55e9d5240e1eedd9e99f0c94 |
| 2ecf-polar-released-true-first-cell-curvature.py | a56b6dc423cbbe446e99e59179197d5ea7f4c18e27eb61aaf740f55049c08add |
| polar-R293-432-curvature-hottest-directed1.json | 4f7dd1dfba661afc7443c2ebe7cafbbebecc42d1e10c2bd6900ce32c95d4a821 |
| polar-R293-432-curvature-interior-left.json | f375122fa6250961d27a027b7301de612f890d978c885710bbbe209fb1dc6ec9 |
| polar-R293-432-curvature-interior-right.json | f00125afdee674e5c73854c2dc0301e5d52490f1bdbf82547e668e519bdeb0b7 |
| polar-R293-432-curvature-three-fine.json | 444ddec94604881866a28b0c75c5461804cd24e8ca4a07600c9530a41781d7f6 |
| polar-R293-432-true-Gamma95-F140-edge-ordered.json | eb46784a2974255971926453497c2a78f1fe4033f24ae2db54e6aca98acc055e |
| polar-R293-432-directed-first-with-actual-edge.json | 4d974c136209926cdb3c9263b0a8a339c8e9c44ad9cb9cb16547a633a88bc947 |
| polar-R293-432-final-curvature.json | a26e5e677544a97e22d8fbf4adeb7db562382070100021fbdbe76a8871fa6f83 |
| 2ecf-polar-released-accurate-gamma95-outlet-to-f140.py | 7e737584ebfaecf9ebc9e5e35e85ba7f6f5b134fb78dc56aeec7bb285d617405 |
| polar-R293-432-true-Gamma95-F140-edge-exit.json | 9b562f2ae1968ab557b721b2287938b7249c459c770d3bcb245a8e5723818107 |
| polar-R293-432-true-Gamma95-F140-edge.log | fb08938828bc57f46dd972b1ca09b3127fae009052c3759f228ab4778f6a4b4e |
| polar-R293-432-curvature-hottest-directed1-exit.json | 0daff5d2373790f7d9455fd15366c584455224cbc7e318a3d521d1f101844bc7 |
| polar-R293-432-curvature-hottest-directed1.log | 21ddbb6b7831d13225e34077ab55ab3645a0b8e6ba1fdddaa8513fa7a0c89b6d |
| polar-R293-432-curvature-interior-left-exit.json | b43f54d864a448e5f2d1c601ddd5522aa8a022951510252908d5c6fe94445b3d |
| polar-R293-432-curvature-interior-left.log | 6326979c909f02c355a9ffcc6aa0f85c06b3c5751df23b54971f187737a1d6a0 |
| polar-R293-432-curvature-interior-right-exit.json | fa33287930a014de44b11d022a2c2155036a001ac58e2f467366f71ccedafaf9 |
| polar-R293-432-curvature-interior-right.log | 2cdbb6fa43b18f37ccce3912d4c957a54be8c85294515db94f1974671430cd0c |
| polar-R293-432-curvature-three-fine-exit.json | 46a3a0b52d34606409fe1197519bb753ad2506eaab8f196ac67e2541d17c6ae4 |
| polar-R293-432-curvature-three-fine.log | 11161bd26bfe81eb2434dfa042a00585ccd0012c0e64cf13d08dcf4ef36473f2 |
| polar-R293-432-true-Gamma95-F140-edge-ordered-exit.json | 984d8abb0668f733b46499270c8486339e5710675861a7a6bee96de5c96b0370 |
| polar-R293-432-true-Gamma95-F140-edge-ordered.log | 5d1eb61fb8d73bb751b50a986e9101b68ec868e516b8be568382ddac99538324 |
| polar-R293-432-directed-first-with-actual-edge-exit.json | a2bb79185c1ff75d70994727240cca795f17d1d0a656ef95dd0a45f35c474f7d |
| polar-R293-432-directed-first-with-actual-edge.log | 3daccd2b28cbe7a256f0478767a0024fcb1146bf94fc1a0e4a71f0ee98c83074 |
| polar-R293-432-final-curvature-exit.json | 099f83b2911a2abbf63a25145087664657412faedd136020affb84585ffab1c2 |
| polar-R293-432-final-curvature.log | e3f1952dfc70a714c85c4b2341232bcd8adcffd48d6ea70d906ce390c3322919 |
