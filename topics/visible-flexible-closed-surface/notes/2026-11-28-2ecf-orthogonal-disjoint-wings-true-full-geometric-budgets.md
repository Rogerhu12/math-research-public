# 正交开发翼的两项真实端自由与三分量整集法管

**已证明。** [R288](../results/R288-independent-orthogonal-developable-wings-and-two-true-terminal-directions.md) 给出长、短轴各有独立空间转角的实际开发盘及其两侧完整六 jets。两个非平带在材料盘上没有共同点，故整个开发盘的度量准确为平面度量。长、短轴两个真实竖直端速对两转幅的雅可比行列式绝对值大于 .599，两尖点的高度亦逐个可独立改变。异翼两点取压缩后的实际水平坐标得平方距离大于 .214²。含真喉、两固定整帽、原中央及所有边缘的三个分量并在所有相位 reach≥.097，同时满足既有两形变距离预算。全材料角最大真弦长小于 .713612，从而可在原材料长度接回 R284 所给端口准确且 E=1 的连接。完整曲面精度与法管仍需核算。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 "$S/2ecf-polar-true-orthogonal-wing-geometric-budgets.py" --port "$S/2ecf-polar-orthogonal-disjoint-wing-developable-port.py" --chords polar-R273-R282-all-material-slack-certified.json --output polar-orthogonal-true-geometric-bounds.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-orthogonal-disjoint-wing-developable-port.py | 7074f7e1cecf5b5d3d9700303379b8cda04f572abc832bc032be1df33bb50529 |
| 2ecf-polar-true-orthogonal-wing-geometric-budgets.py | 81b2d4d44e3ebac5e97949ecd1d9b3f3be398b121154636d846b49a70afd798c |
| polar-orthogonal-true-geometric-bounds.json | de1b33beeebf76b5003523d5100478e90eeb72779f899b51396b7edfff48227a |
| polar-orthogonal-true-geometric-bounds-exit.json | 8580231e94c630a207f140ab7fb30114fecdea88ec82d5f323c6065c723c8683 |
| polar-orthogonal-true-geometric-bounds.log | c7f92d83cc712efbb373a79233b8d045e4497b4333b8618dcec05282ab2c4a21 |
