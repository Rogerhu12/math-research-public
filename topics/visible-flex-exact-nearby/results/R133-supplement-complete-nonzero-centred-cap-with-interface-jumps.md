# R133：含全部精确接口跳跃的非零中心全 Fourier 驱动帽

完整 $[1,25/8]$ 的实际非零中心残差、全部无限 Fourier 修正、所有精确径向接口跳跃和二阶角正则门均已原生通过。结论是固定真实度量的四端口驱动曲率 BVP：完整两 mean、内侧 body 两迹、真正 nonlinear regular 尾以及周期框架 holonomy 仍须联立，本文没有声称已经得到完整闭曲面。

原 v4 regular-residual 报告尚未单独支付浮点 PPoly 视为精确 dyadic 后的接口跳跃。本文只消费新增 `fourfold_codazzi_centered_cap_interface_jumps.py` 的完整补费结果；原报告的存在标志不单独使用。

## 1. 同一真实目标与四独立端口

工作区间为 $I=[1,25/8]$，目标、参数中心和 $|\eta|\le10^{-9}$ 盒均沿用完整
R133 旋转正帽。$a,\beta,\gamma,K,C_r,\ell$ 表示该真实目标的系数，
$C_r=C_{\rm ref}<0$，$\ell=K/C_r^2>0$。下标 $r$ 在 $C_r$ 中是参考标签，
其径向导数写作 $C_r'$。

写 $C=C_r+c$，保留物理 $B$ 的全部 Fourier 模及其均值。准确非线性项为

$$
Q(B,c)=\frac{B^2+\ell c^2}{C_r+c}.
\tag{N.1}
$$

对 $m\in4\mathbb Z\setminus\{0\}$，设 $M=|m|$、
$b_m=i\operatorname{sgn}(m)\widehat B_m$。这个变换是全部非零 Fourier
$\ell^1$ 空间的等距变换；$Q$ 中的平方仍是物理 $B$ 的平方，不能把它换成
$b^2$。准确方程为

$$
b_m'=M\gamma\ell c_m-2\beta b_m-M\gamma Q_m,
\qquad
c_m'=M\gamma b_m-\beta(\ell+1)c_m+\beta Q_m.
\tag{N.2}
$$

完整 mean 方程另为

$$
B_0'=-2\beta B_0,
\qquad c_0'=-\beta(\ell+1)c_0+\beta Q_0.
\tag{N.3}
$$

由真正 R74 regular Jacobi 线向内传播的 $q_m>0$ 定义
$d_m=b_m+q_m c_m$。与已证明的 R133 Green 核相同，四个独立端口是
$c_{\ne0}(1)$、$d_{\ne0}(25/8)$、$B_0(25/8)$ 和 $c_0(25/8)$。
完整 nonlinear regular 外尾关系、mean height/flux 和周期框架 holonomy
均没有被这些独立驱动端口替代。

## 2. 全模源核，不交换两个范数次序

采用

$$
\|f\|_{X_0}=\sum_{m\in4\mathbb Z}\max_i\sup_{r\in I_i}|f_{m,i}(r)|,
\qquad \|(B,c)\|=\|B\|_{X_0}+\|c\|_{X_0}.
\tag{N.4}
$$

这里 $I_i$ 是包含所有候选接口的有限闭分片；同一内部端点的左右迹分别保留。
径向空间是有限 $\bigoplus_i C(I_i)$ 取最大范数，外层再作 Fourier $\ell^1$。
精确中心不必径向连续，修正 $V$ 也允许相反的跳跃。真正解的连续性将从原积分方程推出。
这是 Banach 代数。它不是 $\sup_r\sum_m|f_m(r)|$；后者较小，不能替代
本篇的核消费。

原完整 1334 盒证书给每个物理频率的向内 Riccati 图，保留原 regular 入口的
非零指数费用。由此前完整核 consumer 的严格正率 $\sigma_D,\sigma_C$，
三角费 $T$ 和 $q_+$，记

$$
H_D=1+(1+q_+)T,\qquad H_C=1+q_+.
\tag{N.5}
$$

若一般非零模源为 $f_B,f_C$，则其对 pair 解的贡献不超过

$$
\frac{H_D}{\sigma_D}\|f_B/M\|_{X_0}
+\left(\frac{H_Dq_+}{\sigma_D}+\frac{H_C}{\sigma_C}\right)
 \|f_C/M\|_{X_0}.
\tag{N.6}
$$

这是先对每一模用正指数核积分，再作径向 supremum 和 Fourier 求和；
$M$ 来自真实角导数。均值 $c_0$ 的普通源核为

$$
K_0=\frac1{\beta_* (1+\ell_*)},
\quad \beta_*\le-\beta,\quad \ell_*\le\ell,
\tag{N.7}
$$

因为此区间 $\beta<0$，且从右端回积分。$B_0$ 的无源右端传播范数不超过
1。记完整非线性源算子 $G_Q:Q\mapsto(B,c)$ 的已付 pair 范数为 $K_G$；它包含
非零模和 $Q_0$，不是只对有限模的矩阵范数。一般 pair 普通源的完整逆记为 $G_{\rm vec}$，其费用由 (N.6)–(N.7) 给出；不能拿 $K_G$ 代替一般源费。

## 3. 完整有限中心及其真实残差

令 $(\widehat B,\widehat c)$ 为保存的 M64 候选的全部径向三次片和全部
$4,8,\ldots,256$ 物理模，保留 $\widehat c_0$。这些精确双精度系数视为
精确 dyadic 数；不把浮点求解器的 success 标志用作证明。

候选的紧支撑参数控制在 $r\ge.18$ 精确为零，所以本区间的真实参考系数
就是原 $C_r(\eta)$。中心 $\widehat c$ 是绝对曲率差，完整真实 $C$ 仍为
$C_r(\eta)+\widehat c$，不是把 M64 的浮点参考系数当成真实目标。

定义完整残差

$$
\begin{aligned}
R_{B,m}/M&=(\widehat b_m'+2\beta\widehat b_m)/M
          -\gamma\ell\widehat c_m+\gamma\widehat Q_m,\\
R_{C,m}/M&=[\widehat c_m'+\beta(\ell+1)\widehat c_m
                  -\beta\widehat Q_m]/M-\gamma\widehat b_m,\\
R_{C,0}&=\widehat c_0'+\beta(\ell+1)\widehat c_0-\beta\widehat Q_0,
\end{aligned}
\tag{N.8}
$$

其中 $\widehat Q=Q(\widehat B,\widehat c)$ 是完整有理函数。中心的
$\widehat B_0=0$，所以其 mean $B$ 残差为零，但真正解的独立 mean $B$ 输入
仍保留。

### 3.1 完整有限 Neumann 项和无限余项

若 $B_*\ge\|\widehat B\|_{X_0}$、$c_*\ge\|\widehat c\|_{X_0}$、
$C_*\le\inf|C_r|$、$\Lambda\ge\max(1,\sup\ell)$，令 $q=c_*/C_*<1$。
取完整有限多项式

$$
Q_J=\frac{\widehat B^2+\ell\widehat c^2}{C_r}
       \sum_{j=0}^J\left(-\frac{\widehat c}{C_r}\right)^j.
\tag{N.9}
$$

每一个有限乘法都保留其全部 Fourier 卷积，最高指标为 $(J+2)M_0$，
$M_0=64$。在全域范数 (N.4) 中，

$$
\|\widehat Q-Q_J\|_{X_0}
\le\frac{B_*^2+\Lambda c_*^2}{C_*}
       \frac{q^{J+1}}{1-q}=:\mathcal T_J.
\tag{N.10}
$$

因此，有限残差范数之外必须分别增加
$\gamma^*\mathcal T_J$、$\beta^*\mathcal T_J/4$ 和
$\beta^*\mathcal T_J$ 到 (N.8) 三行。这里非零频率最小为4；mean行不能除以4。

### 3.2 每个共同闭盒上的有向验证

将原完整目标盒进一步与所有候选径向三次片的接口求共同细分。每片严格留在
一个原 scalar germ 内。对每个完整有限 Fourier 系数，使用整个参数盒和
径向闭盒计算 $Q_J$ 及 (N.8)。程序保存每一模历经全部径向盒的最大上界，
最后才求和，因而直接验证 (N.4)。

在 $r<1.5$ 使用 [稳定正帽 jets](../results/R133-supplement-stable-positive-cap-first-jets.md)
对完整有限残差作共同径向 Taylor 展开；再与该完整有限系数的直接盒求值相交。
两个包络都对整个径向/参数盒有效，故逐系数交集有效；空交集拒绝。
在其余部分保留原直接求值。无限余项 (N.10) 在共同细分之外统一支付，
不把有限 Taylor 系数当作完整有理函数。

### 3.3 精确 dyadic 接口及完整点源费

原 `PPoly` 的系数和所有径向节点都逐个转成准确二进制有理数。
对每一个内部节点 $r_i$，准确 Horner 计算

$$
j_i=\widehat U(r_i+)-\widehat U(r_i-).
\tag{N.10a}
$$

只支付函数值的全部 jump 即足够一阶方程的分部积分恒等式；不假设相邻浮点片的值或导数准确相等。
真实径向 $C_r$ 连续，因此它的 jump 为零，但有限 $\widehat c_0$ 的 jump 保留。
对所有内部接口和全部 Fourier 系数，点源费用为

$$
\mathcal J=H_D\sum_i\|(j_{B,i})_{\ne0}\|_{A^0}
 +(H_Dq_++H_C)\sum_i\|(j_{c,i})_{\ne0}\|_{A^0}
 +\sum_i|(j_{B,i})_0|+\sum_i|(j_{c,i})_0|.
\tag{N.10b}
$$

这是完整点源估计，没有 $1/M$ 增益：每个 $d$ jump 为
$j_b+q_m(r_i)j_c$，向后的 D 指数核点值不超过1；由 D 驱动 C 的三角费仍为 $T$。
直接 C jump 的向前指数核点值也不超过1，再把 $b=d-qc$ 还原，得到 (N.10b) 的两个非零模系数。
两 mean 从右端回传播，核点值各不超过1。物理 $B$ 到 $b$ 的等距变换不改 jump 绝对值。

本次在 $[1,25/8]$ 内共有92个候选节点、11868个非零 dyadic jump 系数。
全部原始接口、每个接口的有理数 jump 范数和逐系数 jump 总和均保存。
计算不把这些小量舍入成零。

## 4. 非零中心映射及全部 $DQ$

设真正解为 $U=\widehat U+V$，$\|V\|\le\rho$。左非零 $c$ 输入选为中心
的准确完整有限迹；右端独立 $d,B_0,c_0$ 取给定预算内的数据。右端 $q_m$
采用完整 R74 入口，而非浮点稳定中心，故完整中心的右端迹不一致由

$$
\|\widehat b_{\ne0}(R)+q_m(R)\widehat c_{\ne0}(R)\|_{A^0}
\tag{N.11}
$$

另行有向计入。$\widehat c_0(R)$ 也不能删。

由 (N.5)–(N.8) 及全部端口残差得映射原点的严格上界

$$
\epsilon=H_{\rm boundary}+\mathcal J
+\frac{H_D}{\sigma_D}\|R_B/M\|_{X_0}
+\left(\frac{H_Dq_+}{\sigma_D}+\frac{H_C}{\sigma_C}\right)
 \|R_C/M\|_{X_0}+K_0\|R_{C,0}\|_{\infty,\mathrm{pw}}.
\tag{N.12}
$$

这里 $\|\cdot\|_{\infty,\mathrm{pw}}$ 取全部闭分片及两侧迹的最大值。

令 $d=C_*-c_*-\rho>0$、$B_+=B_*+\rho$、$c_+=c_*+\rho$。完整有理导数为

$$
D_BQ=\frac{2B}{C_r+c},\qquad
D_cQ=\frac{2\ell c}{C_r+c}
       -\frac{B^2+\ell c^2}{(C_r+c)^2}.
\tag{N.13}
$$

由完整 Banach 代数的 Neumann 逆，得到

$$
D_B^*=\frac{2B_+}d,\qquad
D_c^*=\frac{2\Lambda c_+}d
       +\frac{B_+^2+\Lambda c_+^2}{d^2},\qquad
\lambda=K_G\max(D_B^*,D_c^*).
\tag{N.14}
$$

pair 输入采用和范数，所以导数算子范数取这两列上界的最大值；没有把某一列
删除。两列都作用在全部无限 Fourier 模上。

若 $\lambda<1$ 且 $\epsilon+\lambda\rho<\rho$，则

$$
V=Hh_{\rm diff}-G_{\rm vec}\!\left(R_{\rm reg}+\sum_i j_i\delta_{r_i}\right)
  +G_Q[Q(\widehat U+V)-Q(\widehat U)]
\tag{N.15}
$$

在完整 $X_0\times X_0$ 闭球中严格自映且收缩。Banach 定理给唯一真正解，
且 $\|V\|\le\epsilon/(1-\lambda)<\rho$。这一步没有频率截断；仅作为
验证中心的 $\widehat U$ 有限。$h_{\rm diff}$ 是全部端口与中心迹的差。

逐片分部积分，保留 $j_i$ 的上述符号，说明 (N.15) 与原方程
$U=Hh+G_QQ(U)$ 完全等价。对有界分片源，每个有限模的 Green 积分在径向全局连续；
完整核界又给 Fourier 尾的一致可求和支配。因此实际 $U$ 径向全局连续，
$V$ 的相反 jump 准确抵消中心 jump。这里没有先假设中心或修正连续。

## 5. 角二阶正则性与未关闭的全局端口

完整 Green 核、真实径向系数和 $Q$ 都与角平移交换。若四端口的非零输入在
$A^2$，则它们的平移轨道在 $A^0$ 中为 $C^2$。严格球像余量保证小平移后的
解仍在同一个固定中心附近；中心本身的有限角多项式轨道在 $X_0$ 中连续。
因此固定点唯一性给 $U(h(\cdot+\tau))=U(h)(\cdot+\tau)$。

由于完整 $DQ$ 范数小于1，$(I-G_QDQ)^{-1}$ 的 Neumann 范数不超过
$(1-\lambda)^{-1}$。有理式 (N.1) 在 $d>0$ 邻域中二次可微。取
$S=B_*+c_*+\rho$，一个完整二阶导数上界为

$$
J_2=\Lambda\left(\frac2d+\frac{4S}{d^2}
                         +\frac{2S^2}{d^3}\right).
\tag{N.16}
$$

对端口作两次差商并用该逆，即得强 $X_0$ 中的两次角导数。连续 Fourier
坐标泛函把这两次强导数分别识别为 $imU_m$ 和 $-m^2U_m$，所以实际得到
完整 $\sum_m|m|^2\sup_r|U_m|<\infty$，没有先假定未知解的高阶正则性。
mean 输入的角导数严格为零。Codazzi 方程随后给全局连续的一阶径向导数（以及所需的混合角导数）。
与原真实 $E\in C^1$、$a\in C^2$ 和 R126 框架重建结合，得到局部 $C^2$ 等距浸入。
这里不额外声称曲率系数跨原 scalar 接口有未支付的高阶径向导数，
也不消除环绕圆周的 Euclidean holonomy。

最后还必须联立真正 nonlinear regular 帽/无限尾、内侧 body、两 mean、
位置高度与周期框架条件。本篇的独立驱动曲率 BVP 不能称完整闭曲面。

## 6. 实际完成的闭盒、补费和强正则数值

在参数中心
$-7789843107295549/4611686018427387904$ 的完整 $|\eta|\le10^{-9}$ 区间内，
实际目标保留全部 primitive 尾。参考核从完整1334原盒限制到本区间的898盒；
与完整 M64 中心的全部原三次接口共同细分后，regular 残差实际覆盖935个闭盒。
各片的原 scalar germ、逐 Fourier 系数径向 supremum 数组和全部外端实际费用都在原报告内。

同一个有限中心在较早直接盒/v3残差中没有通过球像门，这些 false 原报告仍保留。
新版先在同一真实 germ 上取消半径幂，严格计算完整 $\beta',\gamma',\ell',C_r'$，
再对完整有限 residual 逐系数作径向 Taylor 并与直接包络取交。
因此改善来自相关性恢复；完整无限 Neumann 余项、所有两 mean 和尾费没有被删。

下表为保守外舍入后的实际严格界：

| 项目 | 界 |
| --- | ---: |
| $\|\widehat B\|_{X_0}$ | $<.001710807041$ |
| $\|\widehat c\|_{X_0}$ | $<.001446821796$ |
| 完整有限 Neumann 的全域比值 | $<.008484076362$ |
| 全部无限 Neumann 余项 $\mathcal T_3$ | $<1.796810974\cdot10^{-13}$ |
| $\|R_B/M\|_{X_0}$，含无限尾 | $<8.676555470\cdot10^{-6}$ |
| $\|R_C/M\|_{X_0}$，含无限尾 | $<3.960229895\cdot10^{-6}$ |
| $\|R_{C,0}\|_{\infty,\mathrm{pw}}$，含无限尾 | $<8.400122901\cdot10^{-8}$ |
| 完整外端预算/中心不一致费用 | $<9.526210559\cdot10^{-8}$ |
| 所有 B 非零模接口 jump 范数之和 | $<6.895148352\cdot10^{-20}$ |
| 所有 c 非零模接口 jump 范数之和 | $<4.406143260\cdot10^{-20}$ |
| 所有 c mean 接口 jump 之和 | $<5.265023212\cdot10^{-23}$ |
| 完整 Green 点源费 $\mathcal J$ | $<1.027339658\cdot10^{-18}$ |
| 补全部接口后的 $\epsilon$ | $<3.707847151\cdot10^{-5}$ |
| 初始准确半径 | $\rho=1/500$ |
| 初始完整 $DQ$ 收缩因子 | $<.713068194$ |
| 初始完整球像 | $<.001463214858<.002$ |

于是**完整连续驱动解存在并在该校验球内唯一**。结论同时保留以下独立驱动数据：

$$
c_{\ne0}(1)=\widehat c_{\ne0}(1),\qquad
\|d_{\ne0}(25/8)\|_{A_2}\le10^{-8},\qquad
|B_0(25/8)|\le10^{-8},\qquad |c_0(25/8)|\le10^{-8}.
\tag{N.17}
$$

这里 $A_2$ 的权为 $(1+|m|)^2$，负模按实共轭保留；给定内端迹含完整64个正模及其负模，
其余输入模准确为零。实际解和修正的输出频率没有截断。左 mean 是输出。

### 6.1 只执行一次的实际残差小球细化

在已有严格存在球内，先算完整零半径导数
$\lambda_0<.292785702$，只提出一次明确半径

$$
\rho_1=\frac{2\epsilon}{1-\lambda_0}.
\tag{N.18}
$$

此式不是成功判据；程序对该半径重新支付 (N.14) 的两列完整 $DQ$、
分母和球像门，实际得到

$$
\begin{aligned}
\rho_1&<.000104857811,\\
\lambda_1&<.314365134,\\
\epsilon+\lambda_1\rho_1&<.000070042112<\rho_1,\\
\|U-\widehat U\|_{X_0^2}&<.000054079035,\\
|C|&>.1690329008.
\end{aligned}
\tag{N.19}
$$

两个球的解是原大球唯一解，因此这没有重新选择分支，也没有循环挑选一个看起来通过的管。
完整唯一候选半径、成功/失败门和原球数据都保留在 regularity 报告。

### 6.2 完整角二阶范数

内端准确输入给

$$
\|\partial_\theta c_L\|_{A_0}<.005781886101,
\qquad
\|\partial_\theta^2 c_L\|_{A_0}<.023133537557.
\tag{N.20}
$$

记外端非零 $d$ 的 $A_2$ 预算为 $e_D=10^{-8}$。因为
$|m|^j\le(1+|m|)^2$，$j=1,2$，令

$$
H_j=H_C\|\partial_\theta^j c_L\|_{A_0}+H_De_D,
\quad
U_1=\frac{H_1}{1-\lambda_1},
\quad
U_2=\frac{H_2+K_GJ_2U_1^2}{1-\lambda_1}.
\tag{N.21}
$$

完整原生消费给

$$
\begin{aligned}
J_2&<17.254171,\\
\|\partial_\theta U\|_{X_0^2}&<.018854834,\\
\|\partial_\theta^2 U\|_{X_0^2}&<.183600040,\\
\sum_m(1+|m|)^2\bigl(\max_r|B_m|+\max_r|c_m|\bigr)&<.224572194.
\end{aligned}
\tag{N.22}
$$

这些是完整未知解的强导数界。没有把有限中心的频谱当作未知解的频谱。
原两 mean 的角导数恰为零，但其值、径向方程和外部端口始终保留。

## 7. 可复跑的完整验证链和 SHA

从题目录依次运行，输出用未占用路径，不能覆盖已有报告：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_cap_centered_residual_v4.py \
  --out /tmp/R133-v4-regular-residual.json.gz
```

239个共同片付完整径向 Taylor，其余696片用直接闭盒值，935个共同片全部保留；本次完整原始运行 wall
为2952.3321642500014秒。该重算的 regular-residual 输出须再交给接口 consumer，
不能只读原报告的存在字段。使用已保存完整报告核验接口及正则：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_centered_cap_interface_jumps.py \
  --out /tmp/R133-v4-all-jumps.json.gz

PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_centered_cap_regularity.py \
  --out /tmp/R133-v4-strong-regularity.json.gz
```

所有依赖、真实输入和完整旧失败数据的 SHA 在原报告及 companion manifest 内。
主要本次文件如下：

| 文件 | SHA-256 |
| --- | --- |
| `scripts/fourfold_codazzi_cap_centered_residual_v4.py` | `ce4b1820a18532d78103bd0d3d93e08986b05612528421362ae6f6f7bc780fd9` |
| `notes/2026-11-13-R133-centered-cap-r1-v4-native.json.gz` | `77f7ecd9f9612eb8cc5213dd512aeecd89defe90f36e96f4ce6f1c93a1d8c8b7` |
| `scripts/fourfold_codazzi_centered_cap_interface_jumps.py` | `2bbb4e70d00e43a71219f5ab1d1a23af10ddc780227c4ada6ebeffa37a4a680b` |
| `notes/2026-11-13-R133-centered-cap-r1-v4-jumps-native.json.gz` | `7cac2a441ae9239168be0d4519957666167dc8883d957d68ce1eff11790842d8` |
| `scripts/fourfold_codazzi_centered_cap_regularity.py` | `29be6fef4f0228b22a99d95863f4acf5133971cea2502b8dad44785965a0044d` |
| `notes/2026-11-13-R133-centered-cap-r1-regularity-native.json.gz` | `0c2c663331032d04e9a3959201dda032743720dcd0c092bc989fccfc93302ef8` |
| `notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz` | `4046eb7ac8da162ab9aad9fcb4991933200abdbc2c22ed6329d49bb13d72b856` |
| `notes/2026-11-13-R133-A0-driven-cap-r1-native.json.gz` | `e780eb3caee46dbd19139ef6b4a2056408bf1039d3eab248fe0bf57fc387c70b` |

最后，\(r=1\) 的真实内侧 B 迹及两 mean 输出必须与 body 同时匹配；\(r=25/8\) 的独立 \(d\) 和 mean 还必须接真正 nonlinear regular 帽/无限尾及高度端口。本文没有以微小的外端浮点高度、\(d_R=0\) 或标签为零代替这些条件。完整周期框架和闭曲面几何仍属于后续联立目标。
