# 同一完整 Hold 模型的 63 维物理初猜修正

2026-11-20，geometry_path。**数值证据；尚未得到合格的等距场。**

本次实际运行了前稿定义的 63 维全局物理子空间拟合，保留原 M160、923 节点、
1845 个节点/真实五次中点及全 N2048 角值 Gram 目标，共 11,335,680 个标量残差。
R653 的反射轨道权将计算压到 513 个角代表，原目标不变。
所有 core 系数、固定标量 $a$、$S,R$、完整解析圆 lift 和原精确仿射端条件保留；
内部 prefix、低角模位置/速度/加速度以及帽高度可以联合变化。

## 实际六步

原 complete warm 来自本次真实重新生成，不冒作 11 月 17 日已丢失的 scratch 文件：
输入 bundle SHA256 为
`79c161cc11a0743209ca3947e2b0f51f7ab7046e14ebfadf519f5d6e7259edba`。

| 步 | 接受 alpha | 接受后 raw Frobenius SSE | 最大点值 Gram 算子误差 |
|---|---:|---:|---:|
| 初猜 | — | 24260.0538379903 | .655108956917 |
| 1 | 1 | 7688.0397104481 | .596795536977 |
| 2 | 1/2 | 7066.1051717845 | .587779988181 |
| 3 | 1 | 6628.1168977867 | .585360999899 |
| 4 | 1 | 6458.0493935867 | .586324107588 |
| 5 | 1 | 6453.8215757026 | .586473131875 |
| 6 | 1/2 | 6430.5554831177 | .586426369922 |

第二、六步的满步分别得到 SSE `9607.486986634407`、`6524.993615816507`，
因真实目标上升而拒绝；两次半步下降后接受。其余四次满步均接受。
这说明所优化的 SSE 下降不保证最大点误差逐步下降；表格保留这一区别。
所用初始 damping 为 $.001$，每次接受后除以 3，六步没有改变目标或径向网格。

终点的原 batch 算子直接读出给

$$\mathrm{SSE}=6430.555483124957,\qquad
\max\|e\|_{\rm op}=.5864263699217938,$$

点值 Gram determinant 最小值 `.7288904959648324`。
与 reduced 子空间求值的 SSE 相对差为 `1.1228389921093494e-12`。
帽高度从 `1.9479520470229232` 变为 `1.9392157715615652`。
原 `pack(require_affine=True)` 首末两次都返回完整仿射输入，未做隐含投影。
实际耗时 `27.341648696999982` 秒，过程自然退出。

这些结果仍远大于 $10^{-6}$，并且只有有限点值检查；没有连续 metric、嵌入、reach、
held 或同 $g$ 精化结论。63 维空间只用于得到较好的初猜，不被当作完整变量空间。

## 后续方向由实际限制确定

原 5 个粗径向帽在中心的一阶导数均为零。
末峰位于其第三个粗中心附近：中点 $s=1.3480413751845672$、$\phi=\pi/2$；
相邻粗中心为 $s=1.3580749679324564$。
因此仅有位置 cardinal 的子空间对该处的径向速度误差控制较弱；
下一层可以加入同一粗网格的一导 cardinal，保持共享 C² 和完整目标，或直接交给
原百万维空间求解。这个结构性限制不能被误读成方程不存在精确解的证据。

## 冻结身份与复现

- 拟合源 `fullclosed_physical_subspace.py`：
  `1da3fac6c2050f9615c9c023e87e58a67e1d36cb578e791abb8903a771d2bfc7`。
- 原 dense 定义：`e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d`。
- R653 batch source：`02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a`。
- 完整新报告：`799b1ed5593375c7005aa6b9df079af7effdd43844c43da60db72bd98d773080`。
- 完整新候选 bundle：
  `af89a4414fb0cee35d75dba5530e9b45b62abd248ddf7509cca92c2a9696a505`。

CLI：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$WORK/fullclosed_physical_subspace.py" \
 --bundle "$WORK/fullclosed-mode-damped-warm.npz" \
 --operator "$TOPIC/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --fft-source "$WORK/batched_closed_gram.py" \
 --quarter --angles 2048 --low-modes 3 --steps 6 --seconds 600 \
 --out "$WORK/physical-fit-six-step.json"
```

所有可重算 raw 文件留 scratch。保存原公式/脚本、输入配方、命令和 SHA 即可重建；
不同运行的时间/路径字段及压缩容器元数据可以改变容器 SHA，不改变真实模型定义。
