# R44 新端点：由真实主矩唯一确定幅值

## 结论与范围

对已登记的 raw `lambda=.02 / M16` 完整有限锚，将主圆化改为
`lambda=1, a=.21, bp=.32, bc=.4` 时，保持真实支撑主矩所唯一确定的新参数为

$$
q_* = 0.0346951158033042642359298631049597363244\ldots,
\qquad q_{\rm binary64}=0.03469511580330426.
$$

这应用 R35 关于基体主矩也必须匹配的提醒；没有扫描幅值或采用旧的高次幂增幅预测。
独立 Fraction 积分包围证明新主矩因子为正、该值为唯一最近的 binary64。
新值属于**新物理端点设计**。本条只完成主矩映射及旧实际构造语义核对，
没有构造新初猜，没有运行 BVP 或实际尾求解，也没有继承 R38、R40、R41 的几何门。

## 三种幅值不能混同

源锚为
`m3_work/beta4625-q040-raw-lam002-fixed-m16-neighbor/seed.json.gz`，
SHA `6f5a973c746e1112f827e5478432b9abe9d14931df90157f2a19381cc670b91e`。
它通过原有限内外层停止门；完整前缀 metric 仍为
`9.357262954211186e-5`，未过本题 `1e-6` 门。

| 量 | 实际值 | 构造含义 |
|---|---:|---|
| `gauge_amplitude` | `.04` | 表示系数场所用的数值坐标尺度 |
| 核基体参数 `oldcore.q` | `.03991248545080898` | 乘在 `unit_rho` 上的物理参数 |
| 完整支撑主系数 `Q=2<h cos(3phi)>` | `.03995165069840626…` | 包含主圆化基体之后的真实 Fourier 主矩 |

只读重建按原 `fixed=True` 类族和完整参数向量调用 `initial(p)`。
其原构造式为 `q=.04*math.exp(p[0])`，
`p[0]=-.0021902606002810548`；恢复出的 `oldcore.q`、
`support_amplitude`、CP 的 `actual_primary_amplitude` 与该式逐位同，
十六进制均为 `0x1.46f68c76d35b5p-5`。
全部十五个物理控制 `p[1:]*pscale` 与实际 core 内的 `c` 逐位同。
因此 CP 字段 `actual_primary_amplitude` 在这条源中是基体乘子，
尚未乘主矩因子；本条没有对已经转换的 Fourier 主矩再次乘因子。

## 真实主矩与符号

归一化内积采用全圆平均
$\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f$，
$x=\phi-\pi/3$、$T=2\pi/3$，故
$\cos(3\phi)=-\cos(3x)$。令

$$
I_k={2\over T}\int_0^{a+b_p}\chi(x)\cos(kx)\,dx,
\quad \beta=-{8(I_0-I_3)\over1-I_0}.
$$

原实际基体定义为

$$
\rho=1+q\bigl[-8\cos(3\phi)+\lambda
\{8\chi(1+\cos(3\phi))+\beta(1-\chi)\}\bigr]
+\sum_j c_j(b_j+b_j'').
$$

由 $h+h''=\rho$ 的周期分部积分，
$2\langle h\cos(3\phi)\rangle
=2\langle\rho\cos(3\phi)\rangle/(-8)$。
旧 locked raw 混合列以及新 R44 的 `T/U` 列均有零均值、零主矩的定义约束，故

$$
Q=qP_\lambda,\qquad
P_\lambda=1+\lambda\{(2-\beta/4)I_3-I_0-I_6\}.
$$

此处只分离完整基体和控制；不要求冻结其余支撑矩。
两个真实因子与唯一匹配是

$$
\begin{aligned}
P_{\rm old}&=1.0009812780926798566557849977507162995710\ldots,\\
P_{\rm new}&=1.1515064807652660623846741772778856031543\ldots,\\
q_*&=q_{\rm old}\,{P_{\rm old}\over P_{\rm new}}.
\end{aligned}
$$

宽度按已登记的十进制往返有理数定义，`q` 和 `lambda` 按实际 binary64 的精确实数定义。
高精度求值与独立 Fraction 的 $\pi$、三角 Taylor 及非负
`630*t^4*(1-t)^4` 积分余项一致。新 `P` 的严格有理外包围为

$$
(1.1515064807652660623846741772778856031543,
  1.1515064807652660623846741772778856031544).
$$

`q_*` 的有理包围严格落在选定浮点数与两个相邻浮点数中点之间，排除了 tie。
舍入后的主矩余差单独保留为

$$
Q_{\rm new}-Q_{\rm old}
=-2.59651595458104691712085682185838256012466\ldots\times10^{-18}.
$$

这些严格性仅属于上述标量定义积分及浮点选择；不声称数值 core 的 libm 求值、
整个新初猜或曲面已获严格证书。

## 独立读数

另一个只读探针用原构造出的完整 core，在两个窗口接点拆分后各用固定
128 点 Gauss 直接读取 `h` 与 `rho` 的主矩，包含全部十五个实际控制。
所得 `Q_h=.03995165069840415`、
`Q_rho=.0399516506984066`；与公式读数分别差
`-2.1094237467877974e-15`、`3.400058012914542e-16`。
控制的有限求积主系数为 `6.212020862233432e-19`。
这三项是实际浮点源的数值核对，没有宣称该 Gauss 求积余项已包围。

同探针还独立以 90 位精度对定义的 `chi`、均值补偿 `beta` 和完整基体
`rho*cos(3phi)` 直接积分，和 `q_old*P_old` 差约 `1.4861e-81`。
控制部分在定义积分中的主矩严格为零。这里的高精度数值一致性和前述
Fraction 标量包围分开记录。

## 复现与来源

源及紧凑记录：

- `scripts/resume_m3/match_m3_circle_primary_moment.py`
- `scripts/resume_m3/probe_m3_primary_parameter_identity.py`
- `scripts/resume_m3/circle_trace_primary_match_record.json`

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/match_m3_circle_primary_moment.py \
  --checkpoint /workspace/scratch/7322d0dee069/m3_work/beta4625-q040-raw-lam002-fixed-m16-neighbor/seed.json.gz \
  --endpoint-record /workspace/scratch/7322d0dee069/m3_work/beta4625-q039912-raw-lam1-b032-w040-m16-c2guard/seed-round-record.json \
  --out /workspace/scratch/7322d0dee069/m3_work/circle-trace-primary-match-v2.json
python topics/visible-flex-held-10pct/scripts/resume_m3/probe_m3_primary_parameter_identity.py \
  --mapping /workspace/scratch/7322d0dee069/m3_work/circle-trace-primary-match-v2.json \
  --reference-run /workspace/scratch/7322d0dee069/m3_work/beta4625-q039912-raw-lam1-b032-w040-m16-c2guard \
  --out /workspace/scratch/7322d0dee069/m3_work/circle-trace-primary-parameter-identity.json
```

标量工具 chunk `ec6eb8`、实际构造探针 chunk `d8bf61` 均真实 `exit 0`。
原始输出及全部源、CP、系数分块、端点定义的哈希保存在紧凑记录中。
构造探针没有调用原 `restart`，因而没有夹带 `ratio**j` 的控制或尾高预测。
这条唯一映射尚需通过后续新初猜的原正性、完整参考回投、C²入口、实际全 H 和初始域/RMS 检查。
