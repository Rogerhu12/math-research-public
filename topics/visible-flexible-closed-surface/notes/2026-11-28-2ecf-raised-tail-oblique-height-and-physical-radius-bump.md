# 两个真实端口之间的斜高度径线与物理径向鼓包

**数值证据。**

使用 R267 真 Γ95 和 R273 上弯 A=.4,c=.56 两个完整极坐标 PVA。角钟作五次 Hermite，固定空间极角 θ 时，q=z−kρ 的 n 次 Bernstein **速度**首末各两控制由端 q_s,q_ss 确定，余下控制共同分配准确总 q 增量。logρ 在真两端作五次 Hermite，并加 64β[t(1−t)]³sin⁴θ，其两端真零两 jets。置 z=q+kρ，再作完整 Cartesian 复合链求导。所有内部位置重新构造。
对 k=.55,.8、β=0,.12,.24,−.12、n=12,31 共 16 个新物理场，各自计算 4291840 行。有限端函数取 1024 个 native 角上值与前两角导数形成同一周期五次插值，G11 改用 2048 角。G10 有限速度控制均正的组中，取完整成本最小者 [k,β,n]=[0.55, 0.0, 31]。最小有限控制 .07671458，G11 实际斜速度最小 .07671489，G11 metric / κ / held 为 0.9961820401397121, 1836.8908398300496, 0.7147284686867468。各初图没有优化接受，未从正的有限控制宣布连续嵌入。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-raised-monotone-oblique-connector.py" --mode select --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --output polar-gap092-raised-oblique-select.json
python3 -u "$S/2ecf-polar-raised-monotone-oblique-connector.py" --mode observe --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --trace-nodes 2048 --selection polar-gap092-raised-oblique-select.json --output polar-gap092-raised-oblique-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-raised-monotone-oblique-connector.py | 1664895836d0774c2651b54277e532b8d0849951f027928934c8017f9ab5b514 |
| polar-gap092-raised-oblique-select.json | 5fedf617636130b9faa31081f26ff6665deae690a83174def96adc36c4db9639 |
| polar-gap092-raised-oblique-G11.json | bf48d81df68f06127aee5c59fd5af0acb18b5de5bc9c5f6132a5a358709e5098 |
| polar-gap092-raised-oblique-select-exit.json | b92e4aef201434961128b624abd3dd35c47741f94d4115cad4e28475f80965ad |
| polar-gap092-raised-oblique-select.log | 674ec9a4849ad3da636cd6c8a0eed210b9445a57555b36106e05036fe7b3766c |
| polar-gap092-raised-oblique-G11-exit.json | a17588e8e1951af0afdff174c1e053e49b1f89306283adab416815c994eb14b7 |
| polar-gap092-raised-oblique-G11.log | b9557959cd3e458c3a69c4fe809e59a60e76ce9957fc08cf237b10ded204eb84 |
