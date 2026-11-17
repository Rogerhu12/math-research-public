# R641：固定 pulse 候选一个完整胞元的严格 Gram 上界

**已证明的范围：** 在下述标准 IEEE binary64 四则与平方根模型下，对已登记的同一 pulse 候选、同一构造 $q_{4096}$ 和同一精确积分标量，胞元 804 的全部径向位置与全部角度满足

$$
\|g^{-1/2}(\widehat F^*e-g)g^{-1/2}\|_{\rm op}
\le 4.726340178077320\times10^{-7}<10^{-6}.
\tag{1}
$$

这里胞元下标从 0 开始，端点是保存的精确 binary 数
`0.9997812499999889` 与 `0.9997968749999888`。这一个胞元包含此前全 818 胞采样读出的最大 Gram 点。本条没有证明其余 817 胞的度量界，没有改变候选、重新求解、认证曲率或闭曲面，也不支付 README 第 5 项的固定度量求解精化。

## 1. 同一场与精确标量

输入是[完整 pulse 前缀](../notes/2026-11-17-parallel-numerical-pulse-arclength-prefix.md)的 `parallel-pulse-a5-complete-base.json.gz`，SHA256：

`26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。

所有保存的共同 $F,F_s,F_{ss}$ 系数按精确 binary 数解释，唯一分片五次式定义基场 $F$。保持完整 M320 和原保存 `d2`；不以 M320 方程重新生成左侧 M112 二 jet。设 $V=F_s$、$T=F_\varphi$、$G=T\cdot T$。这些向量用正交移动标架计算，故点积不改变。$\rho$ 是同一初始核心的有限角密度，目标度量为 $ds^2+a(s)^2\rho(\theta)^2d\theta^2$。

标量沿[R636](R636-certified-inward-reference-radius-and-length.md)的精确积分定义：原点是 $.99$，先由原点三 jet 导出 $K=-a_0''/\sqrt{1-(a_0')^2}$，再精确运输到 $.995$ 切口。没有把原点盒子误当切口值，也没有另取浮点角度定义新度量。在本胞所在的第一 pulse 半段，令 $t=s-s_c$、$h_0=\operatorname{binary}(.02)$、$w_0=\operatorname{binary}(.005)$，

$$
\kappa(t)=K+(3/2-K)S(t/h_0)-5S(t/w_0),\qquad
S(u)=10u^3-15u^4+6u^5,
$$

$$
\alpha(t)=\alpha_c-\int_0^t\kappa(v)dv,\qquad
a(t)=a_c+\int_0^t\sin\alpha(v)dv.
\tag{2}
$$

源码对作用区间和 $3/2<K<2.153$ 显式检查。由 $\max|S'|=15/8$、$\max|S''|<6$，有

$$
|\kappa|<8,\quad |\kappa'|<1936.21875,\quad
|\kappa''|<1209795,
$$

$$
a^{(4)}=(\kappa^3-\kappa'')\cos\alpha
          -3\kappa\kappa'\sin\alpha,
\qquad |a^{(4)}|<1300000.
\tag{3}
$$

取胞元精确中点的三次 Taylor 多项式 $A(s)$。在此第一半段，基础曲率 $K+(3/2-K)S(t/h_0)$ 位于 $[3/2,K]$，而 $-5S(t/w_0)$ 位于 $[-5,0]$，故另有更紧的 $|\kappa|\le7/2$。因此 $|(\sin\alpha)^{\prime\prime}|\le1936.21875+(7/2)^2<2000$，以下求积常数合法。

中点 $a$ 由 4096 段整数区间复合中点求积得到；$|(\sin\alpha)''|<2000$ 支付其余项，上界 `5.455698636523926e−13`。$a',a'',a'''$ 直接用整数三角函数包围。式 (3) 给全胞

$$
|a-A|\le2.017865578314726\times10^{-16},\qquad
|a'-A'|\le1.033147176099548\times10^{-10}.
\tag{4}
$$

中点积分区间宽度已经进入 $A$ 的系数区间，不遗漏到 (4) 之外。计算得 $A\ge1.1700255728726427$、$\rho\ge.1625570563615079$。

## 2. 有限带宽的连续覆盖

径向归一坐标 $u\in[0,1]$。任何幂基多项式 $p(u,\varphi)=\sum_{k=0}^n c_k(\varphi)u^k$ 都转换为

$$
p=\sum_{j=0}^n B_j(\varphi)\binom nj u^j(1-u)^{n-j},\qquad
B_j=\sum_{k=0}^j\frac{\binom jk}{\binom nk}c_k.
\tag{5}
$$

Bernstein 权非负且和为 1，所以同时包围所有 $B_j$ 就包围整个径向胞元；这里没有遗留径向网格间隙。

### 2.1 角覆盖引理及自含证明

若实三角多项式 $p$ 的最大物理频率为 $L$，则 $\|p'\|_\infty\le L\|p\|_\infty$。证明如下。归一化 $\|p\|_\infty\le1$；若某点 $p'>L$，取略大于 1 的振幅 $b$，使同值且上升的 $b\cos(L\varphi+\eta)$ 在该点的导数小于 $p'$。在余弦相邻极值处，两函数之差严格交替正负。含该同值点的上升半波内，差函数在该点从负到正，而区间两端从正到负，故该半波至少有三个零点，其余 $2L-1$ 个半波各至少一个零点。非零次数 $L$ 的三角多项式不可能有 $2L+2$ 个不同零点：乘 $e^{iL\varphi}$ 后得到次数至多 $2L$ 的普通多项式。矛盾。负导数对 $-p$ 同理。再对 $p'$ 应用一次，得到

$$\|p''\|_\infty\le L^2\|p\|_\infty.\tag{6}$$

设 $Q$ 为等距角点数，$c_Q=\pi^2/(2Q^2)$。在 $|p|$ 的最大点有 $p'=0$，最近网格点相距不超过 $\pi/Q$，故

$$
\|p\|_\infty\le
\frac{\max_{\rm grid}|p|}{1-c_QL^2},\qquad c_QL^2<1.
\tag{7}
$$

本计算取区间 FFT 所给的 $\sum k^2|\widehat p_k|$ 与 (6)–(7) 两种合法二阶导数界的较小值，记为 $B_2$。这样不把反复区间 FFT 的独立宽度逐模乘 $k^2$ 后当作必须支付的唯一界。

对正分母 $d(\varphi)=\rho^j$，$j=0,1,2$，设 $d\ge\mu>0$、$\|d''\|_\infty\le D_2$，网格上 $|p|/d\le m$。相邻角点的线性插值余项最多为 $c_Q\|f''\|_\infty$；把它用于 $f=Ed\pm p$，可得

$$
\frac{|p|}{d}\le E:={m+c_QB_2/\mu\over1-c_QD_2/\mu}.
\tag{8}
$$

源码对两个分母均检查为正。式 (8) 对式 (5) 的全部 Bernstein 系数逐一成立，因而支付完整径向与角向覆盖。$\rho$ 下界用其有限 Fourier 一阶导数和半角网格损失直接支付。

### 2.2 真实带宽

构造插值固定 $N=4096$；证明网格 $Q=16384$。$\mathcal P_N$ 保留原 Nyquist **单个余弦**，在更大角网格上分为 $\pm N/2$ 两个半系数。$\mathcal I_N$ 是其非零余弦模的零基点原函数。全部数据偶对称且 $\pi$ 周期，所以只出现物理偶频率。角 FFT 没有越 Nyquist 混叠：

| 多项式 | 径向次数 | 最大物理角频率 |
|---|---:|---:|
| $|V|^2-1$ | 8 | 1280 |
| $M=V\cdot T$ | 9 | 1280 |
| $G,\ D=G-A^2\rho^2$ | 10 | 1280 |
| $R=AG_s-2A'G$ | 12 | 1280 |
| $d_N=\mathcal P_N(D/\rho)$ | 10 | 2048 |
| $J=\mathcal I_N(R/\rho)$ | 12 | 2048 |
| $P_f=2AM-\rho J$ | 12 | 2688 |
| $P_g=\rho d_N-D$ | 10 | 2688 |

商 $D/\rho,R/\rho$ 在固定的 4096 个构造点上取值后才插值。不是把这些商自身误当带限函数。最大带宽 2688 严格小于证明网格 Nyquist 8192。

## 3. 非多项式项的全部余项

在构造点令 $q=|T|$、$b=\langle q\rangle_N$，令

$$
z={D\over A^2\rho^2},\qquad
C=q_s-{A'\over A}q={R\over2A^2\rho\sqrt{1+z}}.
\tag{9}
$$

若 $|z|\le U<1$，平方根 Taylor 余项给

$$
q=A\rho+{D\over2A\rho}+\epsilon_q,\qquad
|\epsilon_q|\le {A_+\rho_+U^2\over8(1-U)^{3/2}}=:e_q,
$$

$$
C={R\over2A^2\rho}+\epsilon_C,\qquad
|\epsilon_C|\le
{\|R/\rho\|_\infty\over2A_-^2}
{U\over\sqrt{1-U}(1+\sqrt{1-U})}=:e_C.
\tag{10}
$$

离散 Parseval 给 $\|\mathcal P_N\|_{\ell^\infty\to L^\infty}\le\sqrt N$。对偶、$\pi$ 周期数据，同一 Parseval 与 Cauchy–Schwarz 给

$$
\|\mathcal I_N\|_{\ell^\infty\to L^\infty}^2
\le2\sum_{j\ge1}(2j)^{-2}\le1.
\tag{11}
$$

Nyquist 的单余弦项只占一个权，故有限和小于这里的无限和。式 (11) 使用 $\sum j^{-2}\le2$，可由 $1+\int_1^\infty x^{-2}dx$ 得出。

由 $\langle\rho\rangle_N=1$，$b-A$ 由径向多项式 $\langle D/\rho\rangle_N/(2A)$ 加 $e_q$ 控制。又令

$$
\gamma={\langle C\rangle_N\over b}
       ={b_s\over b}-{A'\over A},\qquad
B=\mathcal I_N(q_s-(b_s/b)q).
$$

于是

$$
q_N=A\rho+{d_N\over2A}+\epsilon_N,\quad
\|\epsilon_N\|_\infty\le\sqrt N e_q,
$$

$$
B={J\over2A^2}+\epsilon_B,\quad
\|\epsilon_B\|_\infty\le e_C+
|\gamma|\left(A_+\|\mathcal I_N\rho\|_\infty+
{\|\mathcal I_N(D/\rho)\|_\infty\over2A_-}+e_q\right).
\tag{12}
$$

$\langle R/\rho\rangle_N$ 同样保为径向多项式再包围，保留均值中的抵消。令 $\lambda=a/b$，使用

$$
\lambda_s=\lambda\left({a'\over a}-{A'\over A}-\gamma\right),
\tag{13}
$$

并用 (4) 控制前两项之差，未把有限求积的导数当精确标量导数。

## 4. 实际 Gram 恒等式与数值结清

设中心 $c=(0,0,Z_0(s))$，$\delta c=(1-\lambda)c_s+\lambda_s(F-c)$，$\psi_s=-B/q_N$。同一规范化场的实际速度为

$$W=\lambda V+\delta c+\lambda T\psi_s.$$

归一化 Gram 三项恰为

$$e_r=|W|^2-1,\qquad e_\theta=G/q_N^2-1,\qquad f=W\cdot T/q_N.\tag{14}$$

这不是把角项强制置零。写 $e=q_N/(A\rho)-1$、$B_0=J/(2A^2)$，混合项的主要抵消是

$$
\begin{aligned}
f={}&\lambda\Bigg[
{P_f\over2A^2\rho}
 +{M\over A\rho}\left({1\over1+e}-1\right)
 -B_0\left({1+z\over(1+e)^2}-1\right)
 -\epsilon_B{1+z\over(1+e)^2}\Bigg]
 +{\delta c\cdot T\over q_N}.
\end{aligned}\tag{15}
$$

角项的分子恒等式为

$$
q_N^2-G=P_g+{d_N^2\over4A^2}
 +2\left(A\rho+{d_N\over2A}\right)\epsilon_N+\epsilon_N^2.
\tag{16}
$$

径向项展开为

$$
e_r=(\lambda^2-1)+\lambda^2(|V|^2-1)
 +2\lambda V\cdot\delta c+|\delta c|^2
 +2\lambda\psi_s(\lambda M+T\cdot\delta c)
 +\lambda^2G\psi_s^2.
\tag{17}
$$

式 (15)–(17) 每项用上节多项式包围和非线性余项支付；所有正分母向下舍入，分子和误差预算向上舍入。实际报告给出：

| 完整预算 | 严格上界（此表向上取整） |
|---|---:|
| $\||V|^2-1\|_\infty$ | $1.917811\times10^{-7}$ |
| $\|D/\rho^2\|_\infty$ | $7.450319\times10^{-7}$ |
| $\|R/\rho\|_\infty$ | $6.218857\times10^{-4}$ |
| $\|P_f/\rho\|_\infty$ | $5.752263\times10^{-7}$ |
| $\|P_g/\rho^2\|_\infty$ | $4.301757\times10^{-7}$ |
| $|z|$、$|e|$ | $5.442321\times10^{-7}$、$3.100242\times10^{-7}$ |
| $e_q$、$\sqrt N e_q$ | $2.000163\times10^{-13}$、$1.280105\times10^{-11}$ |
| $|\lambda-1|$、$|\lambda_s|$ | $1.340514\times10^{-12}$、$1.710209\times10^{-10}$ |
| $\|\epsilon_B\|_\infty$、$\|\delta c\|_\infty$ | $1.670583\times10^{-10}$、$2.997141\times10^{-10}$ |
| $|e_r|$、$|e_\theta|$、$|f|$ | $1.924881\times10^{-7}$、$3.143704\times10^{-7}$、$2.105634\times10^{-7}$ |

若最后三项的上界为 $E,H,F$，逐项绝对值比较得到

$$
\left\|\begin{pmatrix}e_r&f\\f&e_\theta\end{pmatrix}\right\|_{
\rm op}
\le {E+H+\sqrt{(E-H)^2+4F^2}\over2}.
$$

采用报告中未作表格取整的有方向上界，得到 (1)。由[R638](R638-global-positive-arclength-coordinates-for-two-prefixes.md)的全域正坐标，原角与材料角为微分同胚；因此这里对全部原角的界就是该胞元全部材料角的界。

## 5. 实际入口、来源与成本边界

最小新源为 `notes/2026-11-17-parallel-model-pulse-gram-cancellation-certified.py`，SHA256：

`0609703352cbd0814425df5164a49adceed8922349445e38c76c3196ff7bc04e`。

仅依赖已经发表的区间 FFT 源 `scripts/parallel_20261117_arclength_interval_positive.py`（`f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`）和 R636 整数标量源（`babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0`）；后者自行校验整数三角 helper `e480a2ca...`。脚本校验输入与来源哈希、finite/shape/径向递增、第一 pulse 半段、正分母及出口来源不变。

先按完整 pulse 前缀说明中的实际生成命令重建相同 `26e53e8c...` 基场。随后从仓库根目录执行；`$WORK` 仅为仓库外工作目录，原始数据与输出不入库：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-pulse-gram-cancellation-certified.py \
  --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
  --interval-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
  --scalar-oracle topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-inward-integral-enclosure.py \
  --cell 804 --angles 16384 --scalar-panels 4096 \
  --out "$WORK/parallel-model-pulse-cell804-gram-certified.json"
```

本次真实报告 SHA256 为 `f11649810a1499228bede489a70aca52b48716413fde1fca3f2e4bbb0090cc9f`，运行 9.498 秒。报告包含 wall-clock，故重新执行时整份 JSON 哈希未承诺重复；数学定义、输入和各项有方向预算均完整保留。较早 Q8192 的同胞连续界尚为 `1.7021791e−6`；本次只加密证明角网格，构造 $q_{4096}$ 未变。

**未执行全 818 胞认证。** 以此冷启动每胞费用机械外推约 2.2 小时，只是成本估计，不是计时承诺。旧 498 胞中有宽约 `.0025` 的胞元，约为本胞宽度的 160 倍；它们需要原标量精确五次式/解析段分支，不能直接套本源的 pulse 第四导数预算。切口附近显式三 jet 桥的径向 Bernstein 松弛亦需实际检查。最后一个新胞还应按精确 binary 的 $s_c+w_0$ 分段，不能把显示为 `1.0` 的加法结果冒作精确第一半段边界。这些是下一全域入口的已识别任务，不是已观察到这些胞元失败；本轮没有启动无限或自适应无界细化。

## 6. 后续三个实际胞元的完整适配

[旧宽胞、接合桥与精确末分界](../notes/2026-11-17-parallel-model-pulse-representative-gram-addendum.md)在相同场/构造q4096/精确g上新增连续认证：胞381≤4.740275e−8、胞514≤1.247785e−7、胞817两片并的上界≤4.936515e−7。新20.5KB源保全部原预算；旧标量为exact binary Hermite，而末分界为准确的1−5/2^60，后面极短片实际计算，不被浮点显示吞掉。上文§1–5原胞804的声明保持；目前是四个指定胞元，仍非全818胞证明。完整域预先固定为819个有界调用，尚待逐片实际执行。
