# 实际 accepted6 中央轴长与轴差的严格区间

2026-11-12，fd2d / metric_closure。**已证明：这里只支付准确中央曲线的几何必要条件。**

准确中央对象是 `2026-11-12-fd2d-metric-balanced-curvature-core-accepted6-definition.json`：保留真实旧第六次 accepted 的 47 个 binary 参数，采用 `balanced_seed` 基点及已经给出 dyadic 区间的准确材料均值。它与旧有限求解器输入的区别已在中央 definition note 和 check 报告中明确；不将旧未收敛 BVP 改称成功。

## 1. 严格结果

完整报告：`2026-11-12-fd2d-metric-balanced-curvature-axis-intervals-01.json`。向外取较少位数，可写成

$$
1.4079572420517<A<1.4087272055200,
$$

$$
.4972051814157<B<.4996254432202,
$$

$$
.9083317988316<A-B<.9115220241043.
\tag{1}
$$

精确的 dyadic 端点保留在 JSON。特别是

$$
A>1.28,\qquad A-B>.9.
\tag{2}
$$

前一个实际连续中央曲率报告证明了

$$
.1455720383644<n<6.3929125027421,
\qquad n^{-1}>.1564232264356>.136.
\tag{3}
$$

因此中央曲线严格凸、嵌入，(1) 的 A、B 是轴向支持值，非仅截距。它实际支付 R121 所需的中央幅度必要条件。完整活动核的位置、曲率、法球、尾/帽接合和全域 reach 尚须由真正的全 BVP 图支付。

## 2. 不含嵌套数值积分的准确目标

沿用中央定义 note 的固定 seed 半径 $\rho(\phi)$、准确均值 $\mu_j$ 和真实参数 $d_j$。令

$$
P(\phi)=\sum_jd_j(\cos2j\phi-\mu_j),\quad
F(\phi)=\vartheta'(\phi)=1+\rho(\phi)P(\phi),\quad
\vartheta(0)=0.
\tag{4}
$$

准确均值保证 $\vartheta(\pi/2)=\pi/2$。相应轴长为

$$
A=\int_0^{\pi/2}\rho\sin\vartheta\,d\phi,
\qquad B=\int_0^{\pi/2}\rho\cos\vartheta\,d\phi.
\tag{5}
$$

这里用带已知余项的复合中点公式同时包围 $\vartheta$ 和 (5)，不以 Gauss 两档差作为误差证明。只须原函数二导的全域上界。

## 3. 明确的全域导数预算

R118 已证明 $0<\rho<R_0=317/100$。记 $U_2,U_4$ 为准确矩修正区间的绝对值上界。由 logistic 形式和两项余弦修正，R118 的直接求导给

$$
|\rho'|\le R_1=Dk+2U_2+4U_4,
$$

$$
|\rho''|\le R_2=D(2k+4k^2)+4U_2+16U_4.
\tag{6}
$$

令 $M_j$ 为准确 $\mu_j$ 区间的绝对值上界，置

$$
P_0=\sum_j|d_j|(1+M_j),\quad
P_1=\sum_j2j|d_j|,\quad
P_2=\sum_j(2j)^2|d_j|.
$$

这些是有理数，给出 $|P^{(k)}|\le P_k$（$k=0,1,2$）。由 (4) 得

$$
|F|\le F_0=1+R_0P_0,
\quad |F'|\le F_1=R_1P_0+R_0P_1,
$$

$$
|F''|\le F_2=R_2P_0+2R_1P_1+R_0P_2.
\tag{7}
$$

对 $G_A=\rho\sin\vartheta$ 或 $G_B=\rho\cos\vartheta$，连续两次求导并取绝对值得

$$
|G_A''|,|G_B''|\le G_2
=R_2+2R_1F_0+R_0(F_1+F_0^2).
\tag{8}
$$

本次准确有理预算的向外简写为

$$
F_0<11.300,\quad F_1<384.601,\quad
F_2<24991.406,\quad G_2<2479.891.
$$

程序使用完整有理数，不用这些展示的小数。

同一消费者也明确支持 `circle` 基点。这时把 $F$ 改成 $\rho(1/a_0+P)$，在 (7) 的三个界中分别增加 $R_0/a_0$、$R_1/a_0$、$R_2/a_0$（不再加 seed 的常数1）。本报告实际消费的是旧参数所对应的 seed 基点。

## 4. 每一格实际使用的包含式

若 $f\in C^2([x,x+h])$ 且 $|f''|\le M$，在中点 Taylor 展开，奇一次项积分为零，故

$$
\left|\int_x^{x+h}f(t)\,dt-hf(x+h/2)\right|
\le\int_{-h/2}^{h/2}\frac M2t^2\,dt=\frac{Mh^3}{24}.
\tag{9}
$$

取 $N=2048$、$L=\pi/2$、$h=L/N$、$x_i=ih$。设已经得到包含准确 $\vartheta(x_i)$ 的区间 $\Theta_i$，从 $\Theta_0=[0,0]$ 开始，按

$$
\Theta_{i+1}=\Theta_i+hF(x_i+h/2)
+[-1,1]F_2h^3/24
\tag{10}
$$

递推。式 (9) 严格保证归纳成立。对格中点，另用半格中点给

$$
\widehat\Theta_i=\Theta_i+(h/2)F(x_i+h/4)
+[-1,1]F_2(h/2)^3/24.
\tag{11}
$$

然后形成区间和

$$
S_A=\sum_i h\rho(x_i+h/2)\sin\widehat\Theta_i,
\quad S_B=\sum_i h\rho(x_i+h/2)\cos\widehat\Theta_i.
$$

对两个完整积分用 (8)、(9) 再付一次余项，得到

$$
A\in S_A+[-1,1]G_2Lh^2/24,\quad
B\in S_B+[-1,1]G_2Lh^2/24.
\tag{12}
$$

最后取区间差 $A-B$。这里既支付了计算 $\vartheta$ 的误差，也支付了轴积分的误差；没有把近似角值当成准确采样。单项轴积分余项上界实际为 $.00009548186989837$，累计角误差保留在各 $\widehat\Theta_i$ 内。

所有点值在 60 位区间算术中计算，准确 $\pi$、常数有理数和 dyadic 端点都进入区间。点上 $\cos2j\phi$ 用 Chebyshev 递推，全部保留，不截断参数模式。计算中再次确认准确四分之一周转角 $\pi/2$ 位于最终累计角区间；这与先前由准确零均值给出的恒等式一致。

因此 (10)–(12) 是覆盖完整积分的证明，有限网格只规定包含算法，没有把有限点检验冒充全角结论。

## 5. 运行实体

命令：

```sh
python scripts/fd2d-metric-balanced-curvature-axis-intervals.py \
  --definition notes/2026-11-12-fd2d-metric-balanced-curvature-core-accepted6-definition.json \
  --curvature-report notes/2026-11-12-fd2d-metric-balanced-curvature-core-check-01.json \
  --out notes/2026-11-12-fd2d-metric-balanced-curvature-axis-intervals-01.json
```

session32298 自然 exit0，6.14秒；只进行这一次 2048 格计算，没有为额外精度偏好重跑。

| 实体 | SHA-256 |
|---|---|
| `scripts/fd2d-metric-balanced-curvature-axis-intervals.py` | `58862d7f68560950a4e94c0f33ec34dc97f4a4413b0984fad081912630b9b6e1` |
| `notes/2026-11-12-fd2d-metric-balanced-curvature-axis-intervals-01.json` | `a2fff8bac442c3c96b6155a419345337d1df0920049a96c2ef583a7b68d4631f` |

报告绑定准确中央 definition、矩包、均值包、R118 及真实连续曲率报告的 SHA，保留所有输出的完整 dyadic 区间端点。原 provider、浮点 check 和已有 definition 全部未改。
