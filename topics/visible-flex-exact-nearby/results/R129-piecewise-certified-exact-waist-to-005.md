# R129：逐盒真实屏障、Riemann 符号和宽度 1/200 的精确嵌入环带

2026-11-13，visible-exact-astra-ac0d。

**已证明并实际验证：**同一原固定目标、同一真实闭腰初值的 R125 分支，
对整个 $|\delta-\delta_*|\le10^{-9}$，在
$[-1/200,1/200]\times S^1$ 上是 $C^2$ 精确等距嵌入。
其中 $\delta_*=-7789843107295549/4611686018427387904$，目标仍是 R125 的
$g_{0,\delta}=E_\delta dr^2+a_\delta^2d\theta^2$，没有随更新曲面重新选取。

本次实际消费168个闭径向盒、全实角闭格、完整参数盒及原无穷 primitive。
真实 Riemann 误差的末端界为
$$
e_0<0.026273879,\qquad e_1<4.945149,
\qquad \inf|p-q|>0.1929506653.
\tag{129.1}
$$
曲率绝对值另有保守上界 $10.591899$。这是局部带边环带，不是闭曲面，
尚未支付全局帽/尾接合、固定开集、可见幅度和全闭面的 reach。
不同辅助 $\delta$ 也仍可能有不同目标度量，不能称作最终的同度量 flex 参数。

## 1. 完全相同的有限候选与真实目标

继续使用 R127 的21段 degree7、1024角候选，全部系数视为准确 dyadic，
共享端点、完整 mean、负频共轭及准确零 Nyquist 均保持。
候选 SHA 为
`a3e43fc8ee7ab8b6a0e080edccb107ac1e2d92634b0325783f7a99711cf6842f`。
本次消费整个 $[0,1/200]$，每段分成8个闭子盒，共168盒。
每盒都核对实际 scalar germ，穿过原共同 knot 时沿已安装的相邻 germ
接续，不拿一片多项式越过 knot。

残差仍是 R126 的**真实未投影** $R_B,R_C,R_P,R_Q$ 及其角导数。
候选 $P,Q$ 采用真实 $k=\sqrt{-K}$，所以其商的无限角谱由完整闭角格上的
区间除法包围。没有把一个有限 Fourier ODE 的解认作完整 PDE 解。

## 2. 两项有向包围改进及其准确性

### 2.1 目标均值直接使用零频卷积

原 $F^{\rm old}$ 的第 $j$ 个径向导数写作有限 Fourier 向量
$F_j^{\rm fin}$ 加真实余项 $\varepsilon_j$；余项仍来自原完整 primitive。
令 $M_j$ 为三个分量有限 Wiener norm 的最大值。零频内积准确为
$$
\langle F_i^{\rm fin}\cdot F_j^{\rm fin}\rangle
=\sum_{k\in\mathbb Z}\sum_{\ell=1}^3 (F_i^{\rm fin})_{k,\ell}(F_j^{\rm fin})_{-k,\ell}.
$$
完整余项绝对值不超过
$$
3(M_i\varepsilon_j+M_j\varepsilon_i+\varepsilon_i\varepsilon_j).
\tag{129.2}
$$
实际以有向复区间完成有限和，再加 (129.2)，得到
$$
E=\langle F_1\cdot F_1\rangle,\quad
E'=2\langle F_1\cdot F_2\rangle,\quad
E''=2\langle F_2\cdot F_2\rangle+2\langle F_1\cdot F_3\rangle.
$$
所以目标、参数盒和全部尾均未变化。改进仅避免先计算整个非恒定乘积，
再把所有非零频误差一并收费给其零频系数。
$K,K',\gamma,\beta,\kappa$ 仍用 R126 的同一准确公式。

### 2.2 每个闭角格使用局部 Taylor 包围

对每个已有有限中点多项式 $p$，其完整字段误差记为 $\varepsilon$。
角格中心 $\theta_j$ 的 $p,p_\theta,p_{\theta\theta}$ 都通过有向 FFT 求值。
若半格宽 $h_\theta=\pi/(4N_\theta)$，则格内完整误差费为
$$
\varepsilon+h_\theta|p_\theta(\theta_j)|
+\frac{h_\theta^2}{2}|p_{\theta\theta}(\theta_j)|
+\frac{h_\theta^3}{6}\|p_{\theta\theta\theta}\|_{\mathcal A_0}.
\tag{129.3}
$$
第三项余界使用所有有限模式；原字段误差完整加入一次。
对候选的每个所需导数，先准确微分原系数，再分别支付其字段误差。
没有从一个 $C^0$ 误差猜测高导误差。
本次 $N_\theta=16384$，原 primitive 入口512节点、Arb192位。
原有限多项式的真实系数区间和舍入均包含在 (129.3) 中。

## 3. 逐盒仿射屏障：不重复放大已有误差

完整残差报告的单个全区间粗屏障未过 $1/16$ 管门；它的
`continuation_certified=false` 原样保留。下面的新结论来自另一份独立的
逐盒屏障消费者，不修改该失败字段。

设第 $i$ 盒为 $[r_i,r_{i+1}]$，长度 $h_i$。消费该盒真实候选/残差界，
按 R126.21 取 $M_i=\widehat M_i+1/16$ 和非负
$A_{0i},A_{1i},A_{10i},\gamma_i,\rho_{0i},\rho_{1i}$。
初盒从严格大于真实初误差的 $z_j=2e_j(0)+2^{-180}$ 起步；后续盒的
$z_j$ 就是上一盒的屏障终值，不能把已付误差在每盒再乘二。

令 $\iota=1+2^{-40}$、$\tau=2^{-180}$，实际计算
$$
Y_0=\frac{z_0+h_i\rho_{0i}}{1-h_iA_{0i}}\,\iota+\tau.
\tag{129.4}
$$
再令
$$
\mathsf a=h_i\gamma_i,\quad \mathsf b=1-h_iA_{1i},\quad
\mathsf c=z_1+h_i(A_{10i}Y_0+\rho_{1i}),\quad
\Delta=\mathsf b^2-4\mathsf a\mathsf c,
$$
$$
Y_1=\frac{2\mathsf c}{\mathsf b+\sqrt\Delta}\,\iota+\tau.
\tag{129.5}
$$
计算要求分母、$\mathsf b$、$\Delta$ 严格为正。
稳定形式 (129.5) 选择小二次根附近；它本身不免除以下独立实际门：
$$
m_0=Y_0-z_0-h_i(A_{0i}Y_0+\rho_{0i})>0,
$$
$$
m_1=Y_1-z_1-h_i(A_{1i}Y_1+\gamma_iY_1^2+A_{10i}Y_0+\rho_{1i})>0.
\tag{129.6}
$$
每盒还检查 $Y_j>z_j$、$Y_0<1/16$、候选间隔减 $2Y_0$ 严格为正、$k>0$。

具体屏障是
$$
y_j(r)=z_j+(Y_j-z_j)(r-r_i)/h_i.
$$
因右端比较系数非负、$y_j\le Y_j$，(129.6) 正好推出 R126.23 的严格
微分不等式。这是在每个完整盒上的证明，不是只检查屏障端点值。
共享候选端点及所有角导数在段界准确连续；屏障端值也共享，故相邻盒直接
接合，没有漏掉候选跳跃费。真实导数比较由同一实际特征族完成。

168盒实际全部通过。最小有向余量分别大于
$1.0490\,10^{-16}$ 和 $1.4080\,10^{-14}$；它们虽小，但192位输入包围和
256位屏障运算明确分离舍入，所有判定都严格为正。
最终得到 (129.1)。R125 的局部分支与 R126 的一阶继续定理因而给出整个
$[0,1/200]$ 上的真实解；反射给负侧及腰处 $C^2$ 接缝。

## 4. 沿真实特征保持两个 Riemann 变量的符号

仅用全局 $M$ 和最小 $|p-q|$ 分别估计 $A$ 会丢掉很强的相关性。
本篇另付 $p<0<q$，再使用准确代数。

腰初始 $B=0,C<0$，故 $p(0)=k(0)/C(0)<0$、$q(0)=-k(0)/C(0)>0$。
原完整初始曲率证书给 $\|C(0)\|_\infty<7.593298$；结合此次真实 $k(0)$，
两者初始绝对值均大于
$$
\sigma_0>0.1218064585.
$$
在第 $i$ 盒中，实际振幅上界取 $\mathcal M_i=\widehat M_i+Y_{0i}$。
R126.17 沿**真实**特征的零阶项满足
$$
|f(p,q)|,|g(p,q)|
\le |\beta_i|\mathcal M_i(1+\mathcal M_i^2)
   +2|\kappa_i|\mathcal M_i=:F_i.
\tag{129.7}
$$
对两族真实特征分别积分，从任意当前点回到实际腰初值，有
$$
p(r,\theta)\le-\sigma_0+\sum_i h_iF_i,
\qquad q(r,\theta)\ge\sigma_0-\sum_i h_iF_i.
$$
全部168盒的有向和为
$$
\sum_i h_iF_i<0.020266329,
\quad\text{故}\quad p<-0.1015401298<0<0.1015401298<q.
\tag{129.8}
$$
这个论证不要求特征等于候选特征，也没有循环假设符号：
振幅先由已完成的延拓屏障控制，(129.7) 对所有这些实振幅成立。

令 $x=-p>0,y=q>0$。准确反变换给
$$
A=\frac{2kxy}{x+y},\qquad
|B|=k\frac{|x-y|}{x+y},\qquad |C|=\frac{2k}{x+y}.
$$
所以在每盒中有
$$
0<A\le k\max(x,y)\le k\mathcal M_i,
\qquad |B|\le k,\qquad |C|\le\frac{2k}{\inf|p-q|}.
\tag{129.9}
$$
这使用真实符号与同一对 $p,q$，不是把不相容的三个最坏值同时套入。
对完整第二基本形式矩阵再用行绝对和，实际逐盒给
$$
\max(|\kappa_1|,|\kappa_2|)<10.591899.
\tag{129.10}
$$
它是局部曲率界；单独的曲率界不等于整个闭面的 reach。

## 5. 真实框架积分与全局单射

令 $X,Y,\nu$ 是 R126 的实际正交框架，沿用 R128.1。
利用 (129.9) 在每盒直接积分，而不使用浮点位置或浮点框架，得到

| 真实量 | 整个正半带的有向上界 |
|---|---:|
| $|F-F_0|$ | $<0.005543465$ |
| $|X-e_z|$ | $<0.013450109$ |
| $|Y-Y_0|$ | $<0.005140878$ |
| $|\nu-\nu_0|$ | $<0.014399123$ |

例如法向变化使用准确速率
$|\nu_r|=\sqrt E\sqrt{A^2+B^2}$；没有多乘不必要的框架指数。
同一原腰的支撑 $F_0\cdot\nu_0>1/2$、半径 $|F_0|<13/10$ 由 R123/R128
已付的完整背景定理提供。于是实际水平投影满足
$$
|F_h|>0.4944565359,\qquad |F_h|<1.305543465,
$$
$$
\det_h(F_h,Y_h)>0.4877733947,
\qquad F_h\cdot\nu_h>0.4757376767.
\tag{129.11}
$$
实际 $a,\sqrt E$ 的逐盒下界也完整消费。由 R128 的准确柱坐标恒等式，
$$
\phi_\theta=\frac{a\det_h(F_h,Y_h)}{|F_h|^2}>0.3058472510,
$$
$$
z_r\phi_\theta-z_\theta\phi_r
=\frac{\sqrt E\,a}{|F_h|^2}F_h\cdot\nu_h>0.3307154018.
\tag{129.12}
$$
水平半径不为零，径向同伦使每个固定 $r$ 的角映射次数仍为1；
$\phi_\theta>0$ 因而给圆周全局微分同胚。
改用 $(r,\phi)$ 后，$\partial_r z|_\phi$ 是 (129.12) 第二式除以第一式，
严格为正。相同三维像必有相同柱角和高度，故先有相同 $r$，再有相同原角。
这证明整个环带单射；紧致性与已证精确度量给 $C^2$ 嵌入。
反射的负半带具有同样界及相同柱坐标单调性，故结论涵盖两侧及两条边界。

## 6. 原始报告、版本与重跑

三份完整新报告分别为：

| 文件 | SHA256 |
|---|---|
| `2026-11-13-Codazzi-continuation-r005-v4-native.json.gz` | `52c0a81f7e56db0be0a7c1001ab139200e4539870c77c5b5a75ff3b9e07ac536` |
| `2026-11-13-Codazzi-continuation-r005-piecewise-native.json.gz` | `882ce6ce15fac0589d6eb254b201be6c56b9b04f081117fe7993467ddb692946` |
| `2026-11-13-Codazzi-r005-signed-frame-embedding-native.json` | `05caf21b39edb95ebae0c8229665277342f5673c9dd710b42cdf48dc0580d836` |

它们均在 `notes/`。首份记录168个完整盒及旧粗屏障失败，第二份逐盒记录
所有误差端点/二次判别式/严格余量，第三份记录全部真实符号/曲率/框架门。
首次 embedding 消费者因两个历史报告分别用分数字符串和分子分母对象表示
同一个参数而拒收；现已把两种格式都解析为准确 `Fraction` 后比较，
没有放松目标身份、参数半宽、完整角域或源哈希检查。

本次 native validator SHA 为
`1c97e0bd58d49514501ede6d98b909567fb59d933813d2cc74d9e2813fc60258`，
真实 provider SHA 为
`6bc8f108e89bef96134c580be6ae18b382dae5b5ab6139e5863acdfa526f73bb`。
逐盒消费者 SHA 为
`7fcbb78ee47354cd1081b5482c2ca6c6c7d04b4d766282aa362218f9c2e67927`，
符号/框架消费者 SHA 为
`055cd9a5da15097f3d54e299b9106dec20690709f55bbdadf1905f7467521dc9`。
原168盒计算实际耗时约1133.95秒；后两个消费者已实际运行通过。

在本题目录设置与 R127 相同的 `PYTHONPATH`、单线程 BLAS 和禁止 pycache，
依次运行：

```sh
python scripts/fourfold_phase_codazzi_continuation_validate.py \
  --right 1/200 --subdivide 8 --out /tmp/codazzi-r005-native.json.gz
python scripts/fourfold_codazzi_piecewise_barrier.py \
  --native /tmp/codazzi-r005-native.json.gz \
  --out /tmp/codazzi-r005-piecewise.json.gz
python scripts/fourfold_codazzi_signed_frame_embedding.py \
  --native /tmp/codazzi-r005-native.json.gz \
  --barrier /tmp/codazzi-r005-piecewise.json.gz \
  --out /tmp/codazzi-r005-embedding.json
```

时间字段可不同，准确对象、候选及版本身份必须相同。消费者拒绝未完成的
native cover 和身份不符的依赖。报告中的全闭面完成标记全部保持 false。
下一步继续实际更宽负区与正帽/尾端联合匹配，不由本篇的局部嵌入封闭主目标。
